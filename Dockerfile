FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

RUN addgroup --system app && adduser --system --ingroup app app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=app:app . ./
USER app

EXPOSE 8000

CMD ["sh", "-c", "uvicorn web_chat_app:app --host 0.0.0.0 --port ${PORT:-8000} --workers 1 --no-server-header"]
