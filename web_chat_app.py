"""Servidor web local para el asistente profesional de Duarte."""

from __future__ import annotations

import json
import os
from http import HTTPStatus
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any, Iterator
from urllib.parse import unquote, urlsplit

from dotenv import load_dotenv
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
HOST = "127.0.0.1"
MAX_REQUEST_BYTES = 32_768
MAX_HISTORY_MESSAGES = 8
MAX_HISTORY_CHARS = 24_000

load_dotenv(chat_core.ENV_PATH, override=True)

PORT = int(os.getenv("CHAT_WEB_PORT", "8000"))
MODEL = os.getenv("OPENAI_MODEL", chat_core.DEFAULT_MODEL)
CATALOG = chat_core.cargar_catalogo()


def is_blocked_local_proxy_configured() -> bool:
    """Detecta el proxy sumidero que algunos entornos locales inyectan."""
    proxy_names = (
        "HTTP_PROXY",
        "HTTPS_PROXY",
        "ALL_PROXY",
        "http_proxy",
        "https_proxy",
        "all_proxy",
    )
    blocked_values = {
        "http://127.0.0.1:9",
        "https://127.0.0.1:9",
        "http://localhost:9",
        "https://localhost:9",
    }
    return any(
        os.getenv(name, "").strip().rstrip("/") in blocked_values
        for name in proxy_names
    )


def create_openai_client() -> OpenAI | None:
    """Crea el cliente sin impedir que la interfaz arranque si falta la clave."""
    if not os.getenv("OPENAI_API_KEY"):
        return None

    options: dict[str, Any] = {
        "timeout": 45.0,
        "max_retries": 1,
    }
    if is_blocked_local_proxy_configured():
        options["http_client"] = DefaultHttpxClient(trust_env=False)
    return OpenAI(**options)


CLIENT = create_openai_client()


def normalizar_historial(raw_history: object) -> list[dict[str, str]]:
    """Acepta únicamente un historial breve de mensajes de usuario y asistente."""
    if raw_history is None:
        return []
    if not isinstance(raw_history, list):
        raise ValueError("El historial debe ser una lista.")

    normalized: list[dict[str, str]] = []
    total_chars = 0

    for item in raw_history[-MAX_HISTORY_MESSAGES:]:
        if not isinstance(item, dict):
            raise ValueError("Cada mensaje del historial debe ser un objeto.")

        role = item.get("role")
        content = item.get("content")
        if role not in {"user", "assistant"} or not isinstance(content, str):
            raise ValueError("El historial contiene un mensaje no válido.")

        content = content.strip()
        if not content:
            continue

        total_chars += len(content)
        if total_chars > MAX_HISTORY_CHARS:
            raise ValueError("El historial de conversación es demasiado largo.")
        normalized.append({"role": role, "content": content})

    return normalized


class ChatRequestHandler(SimpleHTTPRequestHandler):
    """Sirve la interfaz y expone la API local del chat."""

    server_version = "DuarteChat/2.0"

    def do_GET(self) -> None:
        request_path = urlsplit(self.path).path

        if request_path == "/api/health":
            self.send_json(
                {
                    "status": "ok" if CLIENT is not None else "configuration_required",
                    "ready": CLIENT is not None,
                }
            )
            return

        if request_path == "/":
            self.path = "/index.html"
        super().do_GET()

    def do_POST(self) -> None:
        if urlsplit(self.path).path != "/api/chat":
            self.send_json({"error": "Ruta no encontrada."}, HTTPStatus.NOT_FOUND)
            return

        if CLIENT is None:
            self.send_json(
                {
                    "error": (
                        "El servicio no está configurado. Añade OPENAI_API_KEY "
                        "al archivo .env y reinicia el servidor."
                    )
                },
                HTTPStatus.SERVICE_UNAVAILABLE,
            )
            return

        try:
            payload = self.read_json_body()
            question = str(payload.get("message", "")).strip()
            detail_level = chat_core.normalizar_nivel_detalle(
                str(payload.get("detailLevel", chat_core.DEFAULT_DETAIL_LEVEL))
            )
            history = normalizar_historial(payload.get("history"))

            if not question:
                raise ValueError("Escribe una pregunta antes de enviar.")
            if len(question) > 2_000:
                raise ValueError("La pregunta supera el máximo de 2.000 caracteres.")
        except (UnicodeError, json.JSONDecodeError, TypeError, ValueError) as exc:
            self.send_json({"error": str(exc)}, HTTPStatus.BAD_REQUEST)
            return

        self.stream_text_response(question, detail_level, history)

    def translate_path(self, path: str) -> str:
        path = unquote(urlsplit(path).path)
        relative_path = path.lstrip("/") or "index.html"
        requested_path = (WEB_ROOT / relative_path).resolve()

        try:
            requested_path.relative_to(WEB_ROOT)
        except ValueError:
            return str(WEB_ROOT / "__not_found__")
        return str(requested_path)

    def end_headers(self) -> None:
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "strict-origin-when-cross-origin")
        self.send_header("X-Frame-Options", "DENY")
        self.send_header(
            "Content-Security-Policy",
            "default-src 'self'; "
            "script-src 'self'; "
            "style-src 'self'; "
            "img-src 'self' data:; "
            "connect-src 'self'; "
            "object-src 'none'; "
            "base-uri 'none'; "
            "frame-ancestors 'none'",
        )
        super().end_headers()

    def read_json_body(self) -> dict[str, object]:
        content_type = self.headers.get_content_type()
        if content_type != "application/json":
            raise ValueError("La solicitud debe enviarse como JSON.")

        try:
            content_length = int(self.headers.get("Content-Length", "0"))
        except ValueError as exc:
            raise ValueError("La longitud de la solicitud no es válida.") from exc

        if content_length <= 0:
            return {}
        if content_length > MAX_REQUEST_BYTES:
            raise ValueError("La solicitud es demasiado grande.")

        body = self.rfile.read(content_length)
        data = json.loads(body.decode("utf-8"))
        if not isinstance(data, dict):
            raise ValueError("El cuerpo debe ser un objeto JSON.")
        return data

    def send_json(
        self,
        data: dict[str, object],
        status: HTTPStatus = HTTPStatus.OK,
    ) -> None:
        body = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def write_stream_event(self, event: dict[str, object]) -> None:
        payload = (json.dumps(event, ensure_ascii=False) + "\n").encode("utf-8")
        self.wfile.write(payload)
        self.wfile.flush()

    def stream_text_response(
        self,
        question: str,
        detail_level: str,
        history: list[dict[str, str]],
    ) -> None:
        response_stream = iter(stream_chat_response(question, detail_level, history))

        try:
            first_delta = next(response_stream)
        except StopIteration:
            self.send_json(
                {"error": "El servicio no generó ninguna respuesta."},
                HTTPStatus.BAD_GATEWAY,
            )
            return
        except Exception as exc:
            message, status = public_api_error(exc)
            print(f"[OpenAI] {type(exc).__name__}: {exc}", flush=True)
            self.send_json({"error": message}, status)
            return

        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", "application/x-ndjson; charset=utf-8")
        self.send_header("Cache-Control", "no-cache, no-transform")
        self.send_header("Connection", "close")
        self.end_headers()

        try:
            self.write_stream_event({"type": "delta", "text": first_delta})
            buffered_delta = ""
            for delta in response_stream:
                buffered_delta += delta
                if len(buffered_delta) >= 96 or "\n" in buffered_delta:
                    self.write_stream_event(
                        {"type": "delta", "text": buffered_delta}
                    )
                    buffered_delta = ""
            if buffered_delta:
                self.write_stream_event({"type": "delta", "text": buffered_delta})
            self.write_stream_event({"type": "done"})
        except (BrokenPipeError, ConnectionResetError):
            return
        except Exception as exc:
            public_message, _ = public_api_error(exc)
            print(f"[OpenAI] {type(exc).__name__}: {exc}", flush=True)
            try:
                self.write_stream_event(
                    {"type": "error", "message": public_message}
                )
            except (BrokenPipeError, ConnectionResetError):
                return

    def log_message(self, format: str, *args: object) -> None:
        return


class ChatHTTPServer(ThreadingHTTPServer):
    """Servidor local que no espera a peticiones abandonadas al cerrarse."""

    allow_reuse_address = True
    daemon_threads = True


def public_api_error(exc: Exception) -> tuple[str, HTTPStatus]:
    """Convierte errores del SDK en mensajes útiles sin filtrar datos sensibles."""
    if isinstance(exc, AuthenticationError):
        return (
            "La clave de OpenAI no es válida o no tiene acceso al proyecto.",
            HTTPStatus.UNAUTHORIZED,
        )
    if isinstance(exc, RateLimitError):
        return (
            "El servicio ha alcanzado temporalmente su límite de uso. "
            "Inténtalo de nuevo en unos segundos.",
            HTTPStatus.TOO_MANY_REQUESTS,
        )
    if isinstance(exc, APIConnectionError):
        return (
            "No se pudo establecer conexión con OpenAI. "
            "Revisa la conexión a internet y vuelve a intentarlo.",
            HTTPStatus.SERVICE_UNAVAILABLE,
        )
    if isinstance(exc, APIStatusError):
        return (
            f"OpenAI no pudo completar la solicitud (estado {exc.status_code}).",
            HTTPStatus.BAD_GATEWAY,
        )
    return (
        "No se pudo completar la respuesta. Vuelve a intentarlo.",
        HTTPStatus.INTERNAL_SERVER_ERROR,
    )


def stream_chat_response(
    question: str,
    detail_level: str,
    history: list[dict[str, str]] | None = None,
) -> Iterator[str]:
    """Selecciona documentos y transmite únicamente la respuesta final."""
    if CLIENT is None:
        raise RuntimeError("El cliente de OpenAI no está configurado.")

    tools = [chat_core.crear_tool_leer_documento(CATALOG)]
    instructions = chat_core.construir_instrucciones(detail_level)
    input_items: list[Any] = [*(history or []), {"role": "user", "content": question}]
    trace = chat_core.AccessTrace()

    planning_response = CLIENT.responses.create(
        model=MODEL,
        instructions=instructions,
        tools=tools,
        input=input_items,
    )
    input_items.extend(planning_response.output)
    tool_calls = [
        item for item in planning_response.output if item.type == "function_call"
    ]

    if not tool_calls:
        final_text = planning_response.output_text or ""
        if final_text:
            yield final_text
        return

    for tool_call in tool_calls:
        try:
            arguments = json.loads(tool_call.arguments)
            result = chat_core.ejecutar_tool(
                tool_name=tool_call.name,
                arguments=arguments,
                catalog=CATALOG,
                trace=trace,
            )
        except (json.JSONDecodeError, TypeError, ValueError) as exc:
            result = json.dumps(
                {"ok": False, "error": f"Argumentos inválidos: {exc}"},
                ensure_ascii=False,
            )

        input_items.append(
            {
                "type": "function_call_output",
                "call_id": tool_call.call_id,
                "output": result,
            }
        )

    completed_response = None
    streamed_text: list[str] = []

    with CLIENT.responses.create(
        model=MODEL,
        instructions=instructions,
        input=input_items,
        stream=True,
    ) as stream:
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
                error = getattr(event, "error", None)
                raise RuntimeError(f"Respuesta fallida: {error}")

    if completed_response is None:
        raise RuntimeError("No se recibió el evento response.completed.")

    if not streamed_text and completed_response.output_text:
        yield completed_response.output_text


def main() -> None:
    WEB_ROOT.mkdir(exist_ok=True)
    server = ChatHTTPServer((HOST, PORT), ChatRequestHandler)
    print(f"Chat web disponible en http://{HOST}:{PORT}")
    if CLIENT is None:
        print("Aviso: falta OPENAI_API_KEY; la interfaz se servirá sin respuestas.")
    print("Pulsa Ctrl+C para detener el servidor.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor detenido.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
