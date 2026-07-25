const REQUEST_TIMEOUT_MS = 600_000;
// Sustituye el archivo en `web/` manteniendo este nombre para actualizar el CV.
const CV_URL = "/CV_Duarte_Fernandez_Pineiro.pdf";

const form = document.querySelector("#chat-form");
const chatPanel = document.querySelector(".chat-panel");
const input = document.querySelector("#message-input");
const messages = document.querySelector("#messages");
const conversation = messages.querySelector(".conversation-inner");
const submitButton = form.querySelector(".send-button");
const submitLabel = submitButton.querySelector("span");
const themeToggle = document.querySelector("#theme-toggle");
const statusRegion = document.querySelector("#chat-status");
const newChatButton = document.querySelector("#new-chat");
const detailInputs = [...document.querySelectorAll("input[name='detail']")];
const contactLinks = document.querySelector(".contact-links");
const cvPlaceholder = document.querySelector("#cv-placeholder");
const cvLinkTemplate = document.querySelector("#cv-link-template");
const welcomeTemplate = conversation.querySelector("[data-welcome]").cloneNode(true);
const analyticsConsent = document.querySelector("#analytics-consent");
const ANALYTICS_CONSENT_KEY = "duarte-chat-analytics-consent";

let isRequestPending = false;
let activeController = null;
let stopRequested = false;
let conversationHistory = [];
let conversationGeneration = 0;
let sessionResetPending = true;
let posthogClient = null;
let analyticsConfig = null;

function safeStorageGet(key) {
  try {
    return window.localStorage.getItem(key);
  } catch {
    return null;
  }
}

function safeStorageSet(key, value) {
  try {
    window.localStorage.setItem(key, value);
  } catch {
    // La analítica sigue siendo opcional cuando el navegador bloquea el almacenamiento.
  }
}

function isDoNotTrackEnabled() {
  return navigator.doNotTrack === "1" || window.doNotTrack === "1";
}

function captureAnalyticsEvent(name, properties = {}) {
  if (posthogClient && typeof posthogClient.capture === "function") {
    posthogClient.capture(name, properties);
  }
}

function posthogAssetHost(host) {
  return host.replace(".i.posthog.com", "-assets.i.posthog.com");
}

function startAnalytics(config) {
  if (posthogClient || !config?.posthogKey || !config?.posthogHost) {
    return;
  }

  const queuedClient = (window.posthog = window.posthog || []);
  if (!queuedClient.__SV) {
    queuedClient.__SV = 1;
    queuedClient._i = queuedClient._i || [];
    queuedClient.init = (projectKey, options, instanceName) => {
      const instance = instanceName ? (queuedClient[instanceName] = []) : queuedClient;
      instance._i = instance._i || [];
      instance._i.push([projectKey, options, instanceName]);
    };
  }

  queuedClient.init(config.posthogKey, {
    api_host: config.posthogHost,
    autocapture: false,
    capture_pageview: false,
    capture_pageleave: false,
    disable_session_recording: true,
    opt_out_capturing_by_default: true,
    defaults: "2026-05-30",
  });

  const script = document.createElement("script");
  script.async = true;
  script.src = `${posthogAssetHost(config.posthogHost)}/static/array.js`;
  script.onload = () => {
    if (!window.posthog || typeof window.posthog.opt_in_capturing !== "function") {
      return;
    }
    posthogClient = window.posthog;
    posthogClient.opt_in_capturing();
    captureAnalyticsEvent("chat_page_viewed", { application: "chat_profesional" });
  };
  document.head.appendChild(script);
}

async function configureAnalytics() {
  if (isDoNotTrackEnabled()) {
    return;
  }

  try {
    const response = await fetch("/api/public-config", { cache: "no-store" });
    if (!response.ok) {
      return;
    }
    const config = await response.json();
    if (!config.analytics?.enabled) {
      return;
    }
    analyticsConfig = config.analytics;
    const choice = safeStorageGet(ANALYTICS_CONSENT_KEY);
    if (choice === "accepted") {
      startAnalytics(analyticsConfig);
    } else if (choice !== "rejected") {
      if (analyticsConsent) {
        analyticsConsent.hidden = false;
      }
    }
  } catch {
    // La aplicación funciona igual si el servicio de analítica no está disponible.
  }
}

analyticsConsent?.addEventListener("click", (event) => {
  const button = event.target.closest("[data-analytics-choice]");
  if (!button) {
    return;
  }
  const accepted = button.dataset.analyticsChoice === "accept";
  safeStorageSet(ANALYTICS_CONSENT_KEY, accepted ? "accepted" : "rejected");
  analyticsConsent.hidden = true;
  if (accepted) {
    startAnalytics(analyticsConfig);
  }
});

function selectedDetailLevel() {
  return document.querySelector("input[name='detail']:checked").value;
}

function isNearBottom() {
  return messages.scrollHeight - messages.scrollTop - messages.clientHeight < 96;
}

function scrollToLatest(force = false) {
  if (force || isNearBottom()) {
    messages.scrollTop = messages.scrollHeight;
  }
}

function clearWelcome() {
  conversation.querySelector("[data-welcome]")?.remove();
  conversation.classList.add("has-conversation");
  chatPanel.classList.remove("chat-empty");
  chatPanel.classList.add("chat-active");
  newChatButton.hidden = false;
}

function createMessage(role, text = "") {
  const row = document.createElement("article");
  row.className = `message-row ${role}`;

  if (role !== "user") {
    const mark = document.createElement("span");
    mark.className = "assistant-mark";
    mark.setAttribute("aria-hidden", "true");
    mark.textContent = "DF";
    row.appendChild(mark);
  }

  const stack = document.createElement("div");
  stack.className = "message-stack";

  const author = document.createElement("p");
  author.className = "message-author";
  author.textContent = role === "user" ? "Tú" : "Asistente de Duarte";

  const bubble = document.createElement("div");
  bubble.className = "message-bubble";

  const content = document.createElement("div");
  content.className = "message-content";
  content.textContent = text;

  bubble.appendChild(content);
  stack.append(author, bubble);
  row.appendChild(stack);
  conversation.appendChild(row);

  scrollToLatest(true);
  return { row, stack, bubble, content, author };
}

function createLoadingMessage() {
  const message = createMessage("assistant");
  message.row.classList.add("is-loading");
  message.row.setAttribute("aria-busy", "true");
  message.bubble.replaceChildren();

  const loadingContent = document.createElement("div");
  loadingContent.className = "loading-content";

  const dots = document.createElement("span");
  dots.className = "loading-dots";
  dots.setAttribute("aria-hidden", "true");
  dots.append(
    document.createElement("span"),
    document.createElement("span"),
    document.createElement("span"),
  );

  const label = document.createElement("span");
  label.textContent = "Consultando el perfil de Duarte…";

  loadingContent.append(dots, label);
  message.bubble.appendChild(loadingContent);
  return message;
}

function beginStreaming(message) {
  message.row.classList.remove("is-loading");
  message.row.classList.add("is-streaming");
  message.bubble.replaceChildren(message.content);
  message.content.textContent = "";
  message.author.textContent = "Asistente de Duarte · respondiendo";
}

function addCopyAction(message, answer) {
  const actions = document.createElement("div");
  actions.className = "message-actions";

  const copyButton = document.createElement("button");
  copyButton.type = "button";
  copyButton.className = "copy-button";
  copyButton.textContent = "Copiar respuesta";
  copyButton.addEventListener("click", async () => {
    try {
      await navigator.clipboard.writeText(answer);
      copyButton.textContent = "Copiada";
      statusRegion.textContent = "Respuesta copiada al portapapeles.";
      window.setTimeout(() => {
        copyButton.textContent = "Copiar respuesta";
      }, 1_600);
    } catch {
      statusRegion.textContent = "No se pudo copiar la respuesta.";
    }
  });

  actions.appendChild(copyButton);
  message.stack.appendChild(actions);
}

function finishStreaming(message, answer, wasStopped = false) {
  message.row.classList.remove("is-streaming");
  message.row.classList.remove("is-loading");
  message.row.removeAttribute("aria-busy");
  message.author.textContent = wasStopped
    ? "Asistente de Duarte · respuesta detenida"
    : "Asistente de Duarte";
  addCopyAction(message, answer);
}

function showError(message, error, question) {
  const friendlyError = /^connection error\.?$/i.test(error)
    ? "No se pudo conectar con el servicio de respuestas."
    : error;

  message.row.className = "message-row assistant error";
  message.row.removeAttribute("aria-busy");
  message.author.textContent = "No se pudo responder";
  message.content.textContent = friendlyError;
  message.bubble.replaceChildren(message.content);

  const retryButton = document.createElement("button");
  retryButton.className = "retry-button";
  retryButton.type = "button";
  retryButton.textContent = "Volver a intentar";
  retryButton.addEventListener("click", () => {
    input.value = question;
    resizeInput();
    form.requestSubmit();
  });
  message.bubble.appendChild(retryButton);
}

function setLoading(isLoading) {
  isRequestPending = isLoading;
  submitButton.classList.toggle("is-stop", isLoading);
  submitLabel.textContent = isLoading ? "Detener" : "Enviar";
  submitButton.setAttribute(
    "aria-label",
    isLoading ? "Detener la respuesta" : "Enviar pregunta",
  );
  detailInputs.forEach((detailInput) => {
    detailInput.disabled = isLoading;
  });
  if (isLoading) {
    statusRegion.textContent = "El asistente está preparando una respuesta.";
  }
}

function resizeInput() {
  input.style.height = "auto";
  input.style.height = `${Math.min(input.scrollHeight, 152)}px`;
}

function applyTheme(theme) {
  document.documentElement.dataset.theme = theme;
  try {
    localStorage.setItem("duarte-chat-theme", theme);
  } catch {
    // El tema funciona aunque el navegador bloquee el almacenamiento local.
  }
  const themeAction = theme === "dark" ? "Activar modo claro" : "Activar modo oscuro";
  themeToggle.setAttribute("aria-label", themeAction);
  themeToggle.title = themeAction;
  document.querySelector('meta[name="theme-color"]').content =
    theme === "dark" ? "#0d1411" : "#edf2ef";
}

function initialTheme() {
  try {
    const savedTheme = localStorage.getItem("duarte-chat-theme");
    if (savedTheme === "dark" || savedTheme === "light") {
      return savedTheme;
    }
  } catch {
    // Se utiliza la preferencia del sistema si no hay almacenamiento disponible.
  }
  return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
}

function appendInlineContent(parent, text) {
  const tokenPattern = /(\*\*[^*\n]+\*\*|`[^`\n]+`|\[[^\]\n]+\]\((?:https?:\/\/|mailto:|tel:)[^)]+\))/g;
  let cursor = 0;

  for (const match of text.matchAll(tokenPattern)) {
    if (match.index > cursor) {
      parent.appendChild(document.createTextNode(text.slice(cursor, match.index)));
    }

    const token = match[0];
    if (token.startsWith("**")) {
      const strong = document.createElement("strong");
      strong.textContent = token.slice(2, -2);
      parent.appendChild(strong);
    } else if (token.startsWith("`")) {
      const code = document.createElement("code");
      code.textContent = token.slice(1, -1);
      parent.appendChild(code);
    } else {
      const parts = token.match(/^\[([^\]]+)\]\(([^)]+)\)$/);
      const link = document.createElement("a");
      link.textContent = parts[1];
      link.href = parts[2];
      if (parts[2].startsWith("http")) {
        link.target = "_blank";
        link.rel = "noreferrer";
      }
      parent.appendChild(link);
    }
    cursor = match.index + token.length;
  }

  if (cursor < text.length) {
    parent.appendChild(document.createTextNode(text.slice(cursor)));
  }
}

function renderMarkdown(container, markdown) {
  container.replaceChildren();
  const lines = markdown.replace(/\r\n?/g, "\n").split("\n");
  let paragraphLines = [];
  let activeList = null;

  const flushParagraph = () => {
    if (!paragraphLines.length) {
      return;
    }
    const paragraph = document.createElement("p");
    appendInlineContent(paragraph, paragraphLines.join(" "));
    container.appendChild(paragraph);
    paragraphLines = [];
  };

  const closeList = () => {
    activeList = null;
  };

  for (const line of lines) {
    const trimmed = line.trim();
    if (!trimmed) {
      flushParagraph();
      closeList();
      continue;
    }

    const headingMatch = trimmed.match(/^(#{1,3})\s+(.+)$/);
    const unorderedMatch = trimmed.match(/^[-*]\s+(.+)$/);
    const orderedMatch = trimmed.match(/^\d+[.)]\s+(.+)$/);
    const quoteMatch = trimmed.match(/^>\s?(.+)$/);

    if (headingMatch) {
      flushParagraph();
      closeList();
      const heading = document.createElement(`h${Math.min(headingMatch[1].length + 2, 5)}`);
      appendInlineContent(heading, headingMatch[2]);
      container.appendChild(heading);
    } else if (unorderedMatch || orderedMatch) {
      flushParagraph();
      const listTag = unorderedMatch ? "ul" : "ol";
      if (!activeList || activeList.tagName.toLowerCase() !== listTag) {
        activeList = document.createElement(listTag);
        container.appendChild(activeList);
      }
      const item = document.createElement("li");
      appendInlineContent(item, (unorderedMatch || orderedMatch)[1]);
      activeList.appendChild(item);
    } else if (quoteMatch) {
      flushParagraph();
      closeList();
      const quote = document.createElement("blockquote");
      appendInlineContent(quote, quoteMatch[1]);
      container.appendChild(quote);
    } else {
      closeList();
      paragraphLines.push(trimmed);
    }
  }

  flushParagraph();
}

function bindSuggestedQuestions(root = document) {
  root.querySelectorAll("[data-question]").forEach((button) => {
    button.addEventListener("click", () => {
      input.value = button.dataset.question;
      resizeInput();
      form.requestSubmit();
    });
  });
}

async function configureCVLink() {
  if (!CV_URL || !contactLinks || !cvPlaceholder || !cvLinkTemplate) {
    return;
  }

  try {
    const response = await fetch(CV_URL, { method: "HEAD", cache: "no-store" });
    if (!response.ok) {
      return;
    }

    const fragment = cvLinkTemplate.content.cloneNode(true);
    const cvLink = fragment.querySelector(".cv-link");
    cvLink.href = CV_URL;
    cvLink.addEventListener("click", (event) => {
      event.preventDefault();

      const preview = window.open(CV_URL, "_blank", "noopener");
      if (preview) {
        preview.opener = null;
      }

      const download = document.createElement("a");
      download.href = CV_URL;
      download.download = CV_URL.split("/").at(-1);
      download.hidden = true;
      document.body.appendChild(download);
      download.click();
      download.remove();
    });
    cvPlaceholder.replaceWith(fragment);
  } catch {
    // El botón permanece inactivo hasta que el PDF exista en la ruta configurada.
  }
}

function resetConversation() {
  conversationGeneration += 1;
  activeController?.abort();
  activeController = null;
  stopRequested = false;
  conversationHistory = [];
  sessionResetPending = true;
  conversation.classList.remove("has-conversation");
  chatPanel.classList.remove("chat-active");
  chatPanel.classList.add("chat-empty");
  const welcome = welcomeTemplate.cloneNode(true);
  conversation.replaceChildren(welcome);
  bindSuggestedQuestions(welcome);
  newChatButton.hidden = true;
  input.value = "";
  resizeInput();
  setLoading(false);
  statusRegion.textContent = "Nueva conversación iniciada.";
  input.focus();
}

function processStreamLine(line, onDelta, onStatus, onMetrics) {
  let event;
  try {
    event = JSON.parse(line);
  } catch {
    throw new Error("La respuesta del servidor no tiene un formato válido.");
  }

  if (event.type === "delta" && typeof event.text === "string") {
    onDelta(event.text);
    return false;
  }
  if ((event.type === "queued" || event.type === "status") && typeof event.message === "string") {
    onStatus(event);
    return false;
  }
  if (event.type === "metrics") {
    onMetrics(event);
    return false;
  }
  if (event.type === "done") {
    return true;
  }
  if (event.type === "error") {
    throw new Error(event.message || "La respuesta se interrumpió.");
  }
  throw new Error("El servidor envió un evento desconocido.");
}

themeToggle.addEventListener("click", () => {
  const currentTheme = document.documentElement.dataset.theme || "light";
  applyTheme(currentTheme === "dark" ? "light" : "dark");
});

newChatButton.addEventListener("click", resetConversation);
bindSuggestedQuestions();
void configureCVLink();
void configureAnalytics();

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  if (isRequestPending) {
    stopRequested = true;
    activeController?.abort();
    statusRegion.textContent = "Deteniendo la respuesta.";
    return;
  }

  const question = input.value.trim();
  if (!question) {
    input.focus();
    return;
  }

  const requestGeneration = conversationGeneration;
  const detailLevel = selectedDetailLevel();
  const requestStartedAt = performance.now();

  clearWelcome();
  createMessage("user", question);
  input.value = "";
  resizeInput();
  setLoading(true);

  const pendingMessage = createLoadingMessage();
  const controller = new AbortController();
  activeController = controller;
  stopRequested = false;
  let answer = "";
  let buffer = "";
  let hasStartedStreaming = false;
  let streamCompleted = false;
  let timedOut = false;
  let renderTimer = null;
  let followOnNextRender = false;
  let firstDeltaAt = null;
  let serverMetrics = null;
  let queueReported = false;
  captureAnalyticsEvent("chat_question_started", {
    detail_level: detailLevel,
    has_existing_context: !sessionResetPending,
  });
  const timeout = window.setTimeout(() => {
    timedOut = true;
    controller.abort();
  }, REQUEST_TIMEOUT_MS);

  const flushRender = () => {
    if (renderTimer !== null) {
      window.clearTimeout(renderTimer);
      renderTimer = null;
    }
    renderMarkdown(pendingMessage.content, answer);
    if (followOnNextRender) {
      scrollToLatest(true);
      followOnNextRender = false;
    }
  };

  const appendDelta = (delta) => {
    if (requestGeneration !== conversationGeneration) {
      return;
    }
    if (!hasStartedStreaming) {
      beginStreaming(pendingMessage);
      hasStartedStreaming = true;
    }
    if (firstDeltaAt === null) {
      firstDeltaAt = performance.now();
    }
    answer += delta;
    followOnNextRender = followOnNextRender || isNearBottom();
    if (renderTimer === null) {
      renderTimer = window.setTimeout(flushRender, 50);
    }
  };

  const updateStreamStatus = (streamEvent) => {
    if (requestGeneration !== conversationGeneration) {
      return;
    }
    const { message } = streamEvent;
    statusRegion.textContent = message;
    const loadingLabel = pendingMessage.bubble.querySelector(".loading-content > span:last-child");
    if (loadingLabel) {
      loadingLabel.textContent = message;
    }
    if (streamEvent.type === "queued" && !queueReported) {
      queueReported = true;
      captureAnalyticsEvent("chat_question_queued", {
        detail_level: detailLevel,
        queue_position: Number.isInteger(streamEvent.position) ? streamEvent.position : null,
      });
    }
  };

  const storeServerMetrics = (metrics) => {
    serverMetrics = metrics;
  };

  try {
    const response = await fetch("/api/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        message: question,
        detailLevel,
        resetConversation: sessionResetPending,
      }),
      signal: controller.signal,
      credentials: "same-origin",
    });

    if (!response.ok) {
      const errorData = await response.json().catch(() => ({}));
      throw new Error(errorData.error || "No se pudo generar la respuesta.");
    }
    if (!response.body) {
      throw new Error("El navegador no pudo iniciar la respuesta en tiempo real.");
    }

    const reader = response.body.getReader();
    const decoder = new TextDecoder("utf-8");

    while (true) {
      const { value, done } = await reader.read();
      buffer += decoder.decode(value || new Uint8Array(), { stream: !done });

      let newlineIndex = buffer.indexOf("\n");
      while (newlineIndex !== -1) {
        const line = buffer.slice(0, newlineIndex).trim();
        buffer = buffer.slice(newlineIndex + 1);
        if (line) {
          streamCompleted = processStreamLine(line, appendDelta, updateStreamStatus, storeServerMetrics) || streamCompleted;
        }
        newlineIndex = buffer.indexOf("\n");
      }

      if (done) {
        break;
      }
    }

    if (buffer.trim()) {
      streamCompleted = processStreamLine(buffer.trim(), appendDelta, updateStreamStatus, storeServerMetrics) || streamCompleted;
    }
    if (!streamCompleted) {
      throw new Error("La conexión se cerró antes de completar la respuesta.");
    }
    if (!answer.trim()) {
      throw new Error("La respuesta llegó vacía. Puedes volver a intentarlo.");
    }

    if (requestGeneration !== conversationGeneration) {
      return;
    }

    flushRender();
    finishStreaming(pendingMessage, answer);
    conversationHistory.push(
      { role: "user", content: question },
      { role: "assistant", content: answer },
    );
    conversationHistory = conversationHistory.slice(-8);
    sessionResetPending = false;
    statusRegion.textContent = "Respuesta completada.";
    scrollToLatest();
    captureAnalyticsEvent("chat_question_completed", {
      detail_level: detailLevel,
      question_number: Number.isInteger(serverMetrics?.questionNumber) ? serverMetrics.questionNumber : null,
      response_duration_ms: Math.round(performance.now() - requestStartedAt),
      queue_wait_ms: Number.isFinite(serverMetrics?.queueWaitMs) ? serverMetrics.queueWaitMs : null,
      time_to_first_token_ms: Number.isFinite(serverMetrics?.timeToFirstTokenMs)
        ? serverMetrics.timeToFirstTokenMs
        : firstDeltaAt === null
          ? null
          : Math.round(firstDeltaAt - requestStartedAt),
      generation_duration_ms: Number.isFinite(serverMetrics?.generationDurationMs)
        ? serverMetrics.generationDurationMs
        : null,
      answer_characters: Number.isFinite(serverMetrics?.answerCharacters)
        ? serverMetrics.answerCharacters
        : answer.length,
      was_queued: queueReported,
    });
  } catch (error) {
    if (requestGeneration !== conversationGeneration) {
      return;
    }

    if (renderTimer !== null) {
      window.clearTimeout(renderTimer);
      renderTimer = null;
    }
    const wasAborted = error instanceof DOMException && error.name === "AbortError";
    if (wasAborted && stopRequested && !timedOut) {
      if (answer.trim()) {
        flushRender();
        finishStreaming(pendingMessage, answer, true);
        conversationHistory.push(
          { role: "user", content: question },
          { role: "assistant", content: answer },
        );
      } else {
        pendingMessage.row.remove();
        conversationHistory.push({ role: "user", content: question });
      }
      conversationHistory = conversationHistory.slice(-8);
      statusRegion.textContent = "Respuesta detenida. Se conserva el contenido recibido.";
      scrollToLatest();
      captureAnalyticsEvent("chat_question_cancelled", {
        detail_level: detailLevel,
        response_duration_ms: Math.round(performance.now() - requestStartedAt),
        received_partial_response: Boolean(answer.trim()),
      });
      return;
    }

    let message = error instanceof Error ? error.message : "Ha ocurrido un error inesperado.";
    if (wasAborted && timedOut) {
      message =
        "La respuesta tardó demasiado y se detuvo automáticamente. Puedes volver a intentarlo.";
    }
    showError(pendingMessage, message, question);
    statusRegion.textContent = "No se pudo completar la respuesta.";
    captureAnalyticsEvent("chat_question_failed", {
      detail_level: detailLevel,
      response_duration_ms: Math.round(performance.now() - requestStartedAt),
      error_category: timedOut ? "timeout" : wasAborted ? "aborted" : "request_error",
      was_queued: queueReported,
    });
  } finally {
    window.clearTimeout(timeout);
    if (renderTimer !== null) {
      window.clearTimeout(renderTimer);
    }
    if (activeController === controller) {
      activeController = null;
    }
    if (requestGeneration === conversationGeneration) {
      setLoading(false);
      input.focus();
    }
  }
});

input.addEventListener("input", resizeInput);

input.addEventListener("keydown", (event) => {
  if (event.key === "Enter" && !event.shiftKey && !event.isComposing) {
    event.preventDefault();
    form.requestSubmit();
  }
});

applyTheme(initialTheme());
resizeInput();
