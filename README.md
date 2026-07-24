# Asistente profesional de Duarte

Aplicación web local para consultar mediante lenguaje natural la formación,
experiencia, habilidades, proyectos y objetivos profesionales de Duarte
Fernández Piñeiro. Las respuestas se generan a partir de los documentos
Markdown de `Informacion/`.

## Puesta en marcha

Requisitos: Python 3.11 o posterior y una clave de la API de OpenAI.

1. Crea el entorno virtual e instala las dependencias:

   ```powershell
   python -m venv Entorno
   Entorno\Scripts\python.exe -m pip install -r requirements.txt
   ```

2. Crea la configuración local a partir del ejemplo:

   ```powershell
   Copy-Item .env.example .env
   ```

   Abre `.env` y sustituye `your_openai_api_key` por tu clave real. Este archivo
   está excluido de Git y nunca debe compartirse.

3. Inicia la aplicación:

   ```powershell
   Entorno\Scripts\python.exe web_chat_app.py
   ```

4. Abre [http://127.0.0.1:8000](http://127.0.0.1:8000).

La interfaz permite elegir la extensión de las respuestas, mantener el contexto
entre preguntas, detener una consulta y empezar una conversación nueva.

## Estructura

- `web_chat_app.py`: servidor local y conexión con la API.
- `chat_core.py`: reglas del asistente y acceso seguro a la documentación.
- `document_catalog.yaml`: catálogo que guía la selección de documentos.
- `Informacion/`: fuente de verdad del perfil profesional.
- `web/`: interfaz HTML, CSS y JavaScript.
- `tests/`: comprobaciones locales que no consumen la API.

## Verificación

```powershell
Entorno\Scripts\python.exe -m unittest discover -s tests -v
```

## Seguridad

`.env`, los entornos virtuales, cachés, claves y registros están excluidos del
control de versiones. Antes de publicar cambios, revisa siempre los archivos
que se incluirán con `git status`.
