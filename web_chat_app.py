"""Servidor ASGI público para el asistente profesional de Duarte."""

from __future__ import annotations

import json
import logging
import os
import secrets
import threading
import time
from collections import defaultdict, deque
from dataclasses import dataclass, field
from http import HTTPStatus
from pathlib import Path
from typing import Any, Iterator

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse, JSONResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, ConfigDict, Field
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware

from openai import (
    APIConnectionError,
    APIStatusError,
    AuthenticationError,
    DefaultHttpxClient,
    OpenAI,
    RateLimitError,
)

import chat_core


PROJECT_ROOT = Path(__file__).resolve().parent
WEB_ROOT = PROJECT_ROOT / "web"
load_dotenv(chat_core.ENV_PATH, override=False)

MAX_REQUEST_BYTES = 32_768
MAX_HISTORY_MESSAGES = 8
MAX_HISTORY_CHARS = 24_000
MAX_CONCURRENT_GENERATIONS = int(os.getenv("CHAT_MAX_CONCURRENT_GENERATIONS", "2"))
MAX_QUEUED_GENERATIONS = int(os.getenv("CHAT_MAX_QUEUED_GENERATIONS", "20"))
MAX_REQUESTS_PER_MINUTE = int(os.getenv("CHAT_MAX_REQUESTS_PER_MINUTE", "12"))
SESSION_TTL_SECONDS = int(os.getenv("CHAT_SESSION_TTL_SECONDS", "3600"))
MAX_SESSIONS = int(os.getenv("CHAT_MAX_SESSIONS", "500"))
MAX_TRACKED_CLIENTS = int(os.getenv("CHAT_MAX_TRACKED_CLIENTS", "2000"))
SESSION_COOKIE = "duarte_chat_session"
COOKIE_SECURE = os.getenv("CHAT_COOKIE_SECURE", "false").lower() == "true"
ENABLE_HSTS = os.getenv("CHAT_ENABLE_HSTS", "false").lower() == "true"
PUBLIC_ORIGIN = os.getenv("CHAT_PUBLIC_ORIGIN", "").rstrip("/")
POSTHOG_PUBLIC_KEY = os.getenv("POSTHOG_PUBLIC_KEY", "").strip()
POSTHOG_HOST = os.getenv("POSTHOG_HOST", "https://eu.i.posthog.com").strip().rstrip("/")
POSTHOG_ALLOWED_HOSTS = frozenset({"https://eu.i.posthog.com", "https://us.i.posthog.com"})
CONTACT_REMINDER_QUESTION_NUMBERS = frozenset({3, 8, 15, 25})
CONTACT_REMINDER = (
    "## Contacto\n\n"
    "Puedes contactar a Duarte a través de "
    "[LinkedIn](https://www.linkedin.com/in/dfernandezpineiro), "
    "[correo](mailto:dfernandezpineiro@gmail.com) o "
    "[635 763 949](tel:+34635763949)."
)
OUTPUT_TOKEN_LIMITS = {"breve": 650, "normal": 1_200, "detallado": 2_400}

MODEL = os.getenv("OPENAI_MODEL", chat_core.DEFAULT_MODEL)
OPENAI_TIMEOUT_SECONDS = float(os.getenv("OPENAI_TIMEOUT_SECONDS", "30"))
CATALOG = chat_core.cargar_catalogo()
LOGGER = logging.getLogger("duarte_chat")


def is_blocked_local_proxy_configured() -> bool:
    """Detecta el proxy sumidero inyectado por algunos entornos locales."""
    proxy_names = ("HTTP_PROXY", "HTTPS_PROXY", "ALL_PROXY", "http_proxy", "https_proxy", "all_proxy")
    blocked_values = {"http://127.0.0.1:9", "https://127.0.0.1:9", "http://localhost:9", "https://localhost:9"}
    return any(os.getenv(name, "").strip().rstrip("/") in blocked_values for name in proxy_names)


def create_openai_client() -> OpenAI | None:
    """Crea un cliente de backend con un timeout y reintentos acotados."""
    if not os.getenv("OPENAI_API_KEY"):
        return None
    options: dict[str, Any] = {"timeout": OPENAI_TIMEOUT_SECONDS, "max_retries": 0}
    if is_blocked_local_proxy_configured():
        options["http_client"] = DefaultHttpxClient(trust_env=False)
    return OpenAI(**options)


CLIENT = create_openai_client()


@dataclass
class ConversationState:
    messages: list[dict[str, str]] = field(default_factory=list)
    completed_questions: int = 0
    revision: int = 0
    last_seen: float = field(default_factory=time.monotonic)


class ConversationStore:
    """Sesiones efímeras de una única instancia, sin confiar en el navegador."""

    def __init__(self) -> None:
        self._sessions: dict[str, ConversationState] = {}
        self._lock = threading.RLock()

    def _cleanup(self, now: float) -> None:
        expired = [key for key, value in self._sessions.items() if now - value.last_seen > SESSION_TTL_SECONDS]
        for key in expired:
            self._sessions.pop(key, None)
        overflow = len(self._sessions) - MAX_SESSIONS + 1
        if overflow > 0:
            oldest = sorted(self._sessions, key=lambda key: self._sessions[key].last_seen)[:overflow]
            for key in oldest:
                self._sessions.pop(key, None)

    def get_or_create(self, session_id: str | None) -> tuple[str, ConversationState]:
        now = time.monotonic()
        with self._lock:
            self._cleanup(now)
            if not session_id or session_id not in self._sessions:
                session_id = secrets.token_urlsafe(32)
                self._sessions[session_id] = ConversationState()
            state = self._sessions[session_id]
            state.last_seen = now
            return session_id, state

    def begin(self, session_id: str, reset: bool) -> tuple[list[dict[str, str]], int, int]:
        with self._lock:
            state = self._sessions[session_id]
            if reset:
                state.messages.clear()
                state.completed_questions = 0
                state.revision += 1
            state.last_seen = time.monotonic()
            return list(state.messages), state.completed_questions + 1, state.revision

    def complete(self, session_id: str, revision: int, question: str, answer: str) -> None:
        with self._lock:
            state = self._sessions.get(session_id)
            if state is None or state.revision != revision:
                return
            state.messages.extend(({"role": "user", "content": question}, {"role": "assistant", "content": answer}))
            state.messages = state.messages[-MAX_HISTORY_MESSAGES:]
            while (
                len(state.messages) > 2
                and sum(len(message["content"]) for message in state.messages) > MAX_HISTORY_CHARS
            ):
                state.messages = state.messages[2:]
            state.completed_questions += 1
            state.last_seen = time.monotonic()


@dataclass
class QueueTicket:
    """Representa una petición que espera su turno de generación."""

    position: int = 0
    acquired: bool = False
    created_at: float = field(default_factory=time.monotonic)


class RequestGate:
    """Permite dos respuestas en paralelo y ordena el resto en una cola FIFO."""

    def __init__(self) -> None:
        self._condition = threading.Condition()
        self._recent: dict[str, deque[float]] = defaultdict(deque)
        self._waiting: deque[QueueTicket] = deque()
        self._active_total = 0

    def reserve(self, client_ip: str) -> QueueTicket:
        """Registra la petición y devuelve un ticket inmediato o en cola."""
        now = time.monotonic()
        with self._condition:
            if client_ip not in self._recent and len(self._recent) >= MAX_TRACKED_CLIENTS:
                stale_clients = [
                    ip for ip, entries in self._recent.items()
                    if not entries or now - entries[-1] >= 60
                ]
                for stale_ip in stale_clients:
                    self._recent.pop(stale_ip, None)
                if len(self._recent) >= MAX_TRACKED_CLIENTS:
                    raise HTTPException(503, "El asistente no puede aceptar más consultas en este momento.")

            entries = self._recent[client_ip]
            while entries and now - entries[0] >= 60:
                entries.popleft()
            if len(entries) >= MAX_REQUESTS_PER_MINUTE:
                raise HTTPException(429, "Has alcanzado el límite temporal de consultas. Inténtalo de nuevo en un minuto.")
            entries.append(now)

            if self._active_total < MAX_CONCURRENT_GENERATIONS and not self._waiting:
                self._active_total += 1
                return QueueTicket(acquired=True)
            if len(self._waiting) >= MAX_QUEUED_GENERATIONS:
                raise HTTPException(503, "La cola de consultas está llena. Inténtalo de nuevo en unos minutos.")

            ticket = QueueTicket(position=len(self._waiting) + 1)
            self._waiting.append(ticket)
            return ticket

    def wait_for_turn(self, ticket: QueueTicket) -> None:
        """Bloquea solo las peticiones en cola hasta que haya capacidad disponible."""
        if ticket.acquired:
            return
        with self._condition:
            while not (self._waiting and self._waiting[0] is ticket and self._active_total < MAX_CONCURRENT_GENERATIONS):
                self._condition.wait()
            self._waiting.popleft()
            self._active_total += 1
            ticket.acquired = True

    def release(self, ticket: QueueTicket) -> None:
        with self._condition:
            if not ticket.acquired:
                try:
                    self._waiting.remove(ticket)
                except ValueError:
                    pass
                self._condition.notify_all()
                return
            ticket.acquired = False
            self._active_total = max(0, self._active_total - 1)
            self._condition.notify_all()


SESSIONS = ConversationStore()
GATE = RequestGate()


class ChatPayload(BaseModel):
    """Contrato público. El historial lo conserva exclusivamente el servidor."""

    model_config = ConfigDict(extra="ignore")
    message: str = Field(min_length=1, max_length=2_000)
    detailLevel: str = chat_core.DEFAULT_DETAIL_LEVEL
    resetConversation: bool = False


class RequestSizeLimitMiddleware:
    """Rechaza cuerpos grandes incluso si el cliente no envía Content-Length."""

    def __init__(self, app: Any) -> None:
        self.app = app

    async def __call__(self, scope: dict[str, Any], receive: Any, send: Any) -> None:
        if scope["type"] != "http" or scope["path"] != "/api/chat":
            await self.app(scope, receive, send)
            return

        headers = dict(scope.get("headers", []))
        content_length = headers.get(b"content-length", b"")
        if content_length.isdigit() and int(content_length) > MAX_REQUEST_BYTES:
            await JSONResponse({"detail": "La solicitud es demasiado grande."}, status_code=413)(scope, receive, send)
            return

        body = bytearray()
        while True:
            message = await receive()
            if message["type"] == "http.disconnect":
                return
            if message["type"] != "http.request":
                continue
            body.extend(message.get("body", b""))
            if len(body) > MAX_REQUEST_BYTES:
                await JSONResponse({"detail": "La solicitud es demasiado grande."}, status_code=413)(scope, receive, send)
                return
            if not message.get("more_body", False):
                break

        sent = False

        async def replay_receive() -> dict[str, Any]:
            nonlocal sent
            if sent:
                return await receive()
            sent = True
            return {"type": "http.request", "body": bytes(body), "more_body": False}

        await self.app(scope, replay_receive, send)


class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: Any) -> Any:
        request_id = secrets.token_hex(8)
        response = await call_next(request)
        response.headers["X-Request-ID"] = request_id
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["Permissions-Policy"] = "camera=(), geolocation=(), microphone=()"
        response.headers["Content-Security-Policy"] = (
            "default-src 'self'; script-src 'self' https://*.posthog.com; style-src 'self'; img-src 'self' data:; "
            "connect-src 'self' https://*.posthog.com; object-src 'none'; base-uri 'none'; "
            "frame-ancestors 'none'; form-action 'self'"
        )
        if request.url.path.startswith("/api/") or request.url.path in {"/healthz", "/readyz"}:
            response.headers["Cache-Control"] = "no-store"
        elif request.url.path.endswith((".js", ".css")):
            response.headers["Cache-Control"] = "public, max-age=31536000, immutable"
        elif request.url.path.endswith(".pdf"):
            response.headers["Cache-Control"] = "public, max-age=3600"
        if ENABLE_HSTS:
            response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
        return response


def allowed_hosts() -> list[str]:
    configured = [item.strip() for item in os.getenv("CHAT_ALLOWED_HOSTS", "").split(",") if item.strip()]
    koyeb_domain = os.getenv("KOYEB_PUBLIC_DOMAIN", "").strip()
    hosts = [*configured, "localhost", "127.0.0.1", koyeb_domain]
    return list(dict.fromkeys(host for host in hosts if host)) or ["*"]


app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)
app.add_middleware(TrustedHostMiddleware, allowed_hosts=allowed_hosts())
app.add_middleware(RequestSizeLimitMiddleware)
app.add_middleware(SecurityHeadersMiddleware)


def client_ip(request: Request) -> str:
    forwarded_for = request.headers.get("x-forwarded-for", "")
    if forwarded_for:
        return forwarded_for.split(",", 1)[0].strip()
    return request.client.host if request.client else "unknown"


def enforce_origin(request: Request) -> None:
    origin = request.headers.get("origin")
    if PUBLIC_ORIGIN and origin and origin.rstrip("/") != PUBLIC_ORIGIN:
        raise HTTPException(403, "Origen de la solicitud no permitido.")


def output_token_limit(detail_level: str) -> int:
    return int(os.getenv("OPENAI_MAX_OUTPUT_TOKENS", str(OUTPUT_TOKEN_LIMITS[detail_level])))


def mostrar_recordatorio_contacto(question_number: int) -> bool:
    return question_number in CONTACT_REMINDER_QUESTION_NUMBERS


def incluir_recordatorio_contacto(response_stream: Iterator[str], question_number: int) -> Iterator[str]:
    emitted_response = False
    for delta in response_stream:
        if delta:
            emitted_response = True
            yield delta
    if emitted_response and mostrar_recordatorio_contacto(question_number):
        yield f"\n\n{CONTACT_REMINDER}"


def ndjson_event(event: dict[str, object]) -> bytes:
    return (json.dumps(event, ensure_ascii=False) + "\n").encode("utf-8")


def public_api_error(exc: Exception) -> tuple[str, HTTPStatus]:
    if isinstance(exc, AuthenticationError):
        return "El servicio no está disponible temporalmente.", HTTPStatus.SERVICE_UNAVAILABLE
    if isinstance(exc, RateLimitError):
        return "El servicio ha alcanzado temporalmente su límite de uso. Inténtalo de nuevo en unos segundos.", HTTPStatus.TOO_MANY_REQUESTS
    if isinstance(exc, APIConnectionError):
        return "No se pudo establecer conexión con el servicio de respuestas.", HTTPStatus.SERVICE_UNAVAILABLE
    if isinstance(exc, APIStatusError):
        return "El servicio de respuestas no pudo completar la consulta.", HTTPStatus.BAD_GATEWAY
    return "No se pudo completar la respuesta. Vuelve a intentarlo.", HTTPStatus.INTERNAL_SERVER_ERROR


@app.get("/healthz")
def healthz() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/readyz")
def readyz() -> JSONResponse:
    if CLIENT is None:
        return JSONResponse({"status": "configuration_required"}, status_code=503)
    return JSONResponse({"status": "ready"})


@app.get("/api/health")
def api_health() -> dict[str, object]:
    return {"status": "ok" if CLIENT is not None else "configuration_required", "ready": CLIENT is not None}


@app.get("/api/public-config")
def public_config() -> dict[str, object]:
    """Configuración segura que el navegador puede conocer.

    La clave de proyecto de PostHog es pública por diseño; la clave de OpenAI nunca
    se incluye aquí. Una configuración de host no reconocida desactiva la analítica.
    """
    analytics_enabled = bool(POSTHOG_PUBLIC_KEY and POSTHOG_HOST in POSTHOG_ALLOWED_HOSTS)
    return {
        "analytics": {
            "enabled": analytics_enabled,
            "posthogKey": POSTHOG_PUBLIC_KEY if analytics_enabled else "",
            "posthogHost": POSTHOG_HOST if analytics_enabled else "",
        }
    }


@app.post("/api/chat")
def api_chat(request: Request, payload: ChatPayload) -> StreamingResponse:
    if CLIENT is None:
        raise HTTPException(503, "El servicio no está configurado.")
    enforce_origin(request)
    question = payload.message.strip()
    if not question:
        raise HTTPException(400, "Escribe una pregunta antes de enviar.")
    try:
        detail_level = chat_core.normalizar_nivel_detalle(payload.detailLevel)
    except ValueError as exc:
        raise HTTPException(400, str(exc)) from exc
    ip_address = client_ip(request)
    session_id, _ = SESSIONS.get_or_create(request.cookies.get(SESSION_COOKIE))
    ticket = GATE.reserve(ip_address)

    def event_stream() -> Iterator[bytes]:
        completed = False
        revision = -1
        answer_parts: list[str] = []
        generation_started_at: float | None = None
        first_delta_at: float | None = None
        question_number = 0
        try:
            if ticket.position:
                yield ndjson_event(
                    {
                        "type": "queued",
                        "message": f"Tu consulta está en cola (posición {ticket.position}).",
                        "position": ticket.position,
                    }
                )
            GATE.wait_for_turn(ticket)
            generation_started_at = time.monotonic()
            yield ndjson_event({"type": "status", "message": "El asistente está preparando una respuesta."})
            history, question_number, revision = SESSIONS.begin(session_id, payload.resetConversation)
            response_stream = incluir_recordatorio_contacto(
                stream_chat_response(question, detail_level, history),
                question_number,
            )
            for delta in response_stream:
                if first_delta_at is None:
                    first_delta_at = time.monotonic()
                answer_parts.append(delta)
                yield ndjson_event({"type": "delta", "text": delta})
            completed = True
            finished_at = time.monotonic()
            yield ndjson_event(
                {
                    "type": "metrics",
                    "detailLevel": detail_level,
                    "questionNumber": question_number,
                    "queueWaitMs": round((generation_started_at - ticket.created_at) * 1_000),
                    "timeToFirstTokenMs": (
                        round((first_delta_at - ticket.created_at) * 1_000) if first_delta_at is not None else None
                    ),
                    "generationDurationMs": round((finished_at - generation_started_at) * 1_000),
                    "answerCharacters": sum(len(part) for part in answer_parts),
                }
            )
            yield ndjson_event({"type": "done"})
        except (BrokenPipeError, ConnectionResetError):
            return
        except HTTPException as exc:
            message = str(exc.detail)
            yield ndjson_event({"type": "error", "message": message})
        except Exception as exc:
            LOGGER.warning("chat_stream_failed type=%s", type(exc).__name__)
            yield ndjson_event({"type": "error", "message": public_api_error(exc)[0]})
        finally:
            if completed and revision >= 0:
                SESSIONS.complete(session_id, revision, question, "".join(answer_parts))
            GATE.release(ticket)

    response = StreamingResponse(event_stream(), media_type="application/x-ndjson; charset=utf-8")
    response.headers["X-Accel-Buffering"] = "no"
    response.set_cookie(SESSION_COOKIE, session_id, max_age=SESSION_TTL_SECONDS, httponly=True, secure=COOKIE_SECURE, samesite="lax", path="/")
    return response


def stream_chat_response(question: str, detail_level: str, history: list[dict[str, str]] | None = None) -> Iterator[str]:
    """Selecciona documentos y transmite únicamente la respuesta final."""
    if CLIENT is None:
        raise RuntimeError("El cliente de OpenAI no está configurado.")
    tools = [chat_core.crear_tool_leer_documento(CATALOG)]
    instructions = chat_core.construir_instrucciones(detail_level)
    input_items: list[Any] = [*(history or []), {"role": "user", "content": question}]
    trace = chat_core.AccessTrace()
    planning_response = CLIENT.responses.create(model=MODEL, instructions=instructions, tools=tools, input=input_items, max_output_tokens=output_token_limit(detail_level))
    input_items.extend(planning_response.output)
    tool_calls = [item for item in planning_response.output if item.type == "function_call"]
    if not tool_calls:
        if planning_response.output_text:
            yield planning_response.output_text
        return
    for tool_call in tool_calls:
        try:
            arguments = json.loads(tool_call.arguments)
            result = chat_core.ejecutar_tool(tool_call.name, arguments, CATALOG, trace, query=question)
        except (json.JSONDecodeError, TypeError, ValueError) as exc:
            result = json.dumps({"ok": False, "error": "No se pudo consultar el documento solicitado."}, ensure_ascii=False)
            LOGGER.warning("tool_failed type=%s", type(exc).__name__)
        input_items.append({"type": "function_call_output", "call_id": tool_call.call_id, "output": result})
    completed_response = None
    streamed_text: list[str] = []
    with CLIENT.responses.create(model=MODEL, instructions=instructions, input=input_items, stream=True, max_output_tokens=output_token_limit(detail_level)) as stream:
        for event in stream:
            event_type = getattr(event, "type", "")
            if event_type == "response.output_text.delta":
                delta = getattr(event, "delta", "")
                if delta:
                    streamed_text.append(delta)
                    yield delta
            elif event_type == "response.completed":
                completed_response = event.response
            elif event_type == "response.failed":
                raise RuntimeError("Respuesta fallida")
    if completed_response is None:
        raise RuntimeError("No se recibió una respuesta completa.")
    if not streamed_text and completed_response.output_text:
        yield completed_response.output_text


@app.get("/")
def index() -> FileResponse:
    return FileResponse(WEB_ROOT / "index.html")


app.mount("/", StaticFiles(directory=WEB_ROOT, html=False), name="web")
