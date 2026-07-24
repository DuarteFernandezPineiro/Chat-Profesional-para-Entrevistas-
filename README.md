# Asistente profesional de Duarte

Aplicación web para consultar mediante lenguaje natural la formación, experiencia,
habilidades, proyectos y objetivos profesionales de Duarte Fernández Piñeiro. Las
respuestas se generan a partir de los documentos Markdown de `Informacion/`.

La aplicación se ejecuta como servidor ASGI con FastAPI y Uvicorn, por lo que se
puede usar en local y desplegar directamente como servicio web en Koyeb.

## Puesta en marcha local

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

   Sustituye `your_openai_api_key` por tu clave real. `.env` está excluido de Git
   y nunca debe compartirse.

3. Inicia la aplicación:

   ```powershell
   Entorno\Scripts\python.exe -m uvicorn web_chat_app:app --host 127.0.0.1 --port 8000
   ```

4. Abre [http://127.0.0.1:8000](http://127.0.0.1:8000).

La interfaz mantiene el contexto entre respuestas completadas, permite detener una
consulta y empezar una conversación nueva. El historial de la conversación y su
contador se guardan en el servidor durante una hora, no en datos que el navegador
pueda manipular.

## Despliegue en Koyeb

El repositorio contiene un `Dockerfile` listo para Koyeb. Crea un servicio web desde
el repositorio de GitHub, selecciona la compilación mediante Dockerfile y configura
la ruta de comprobación de salud como `/healthz`. No hace falta definir un comando de
ejecución: el contenedor usa el puerto asignado por Koyeb (`PORT`) y escucha en
`0.0.0.0`.

Configura estos valores como secretos o variables de entorno en Koyeb:

| Variable | Valor de producción |
| --- | --- |
| `OPENAI_API_KEY` | Clave secreta de OpenAI, solo en Koyeb; nunca en el repositorio. |
| `OPENAI_MODEL` | `gpt-5.5` o el modelo aprobado que se utilice. |
| `CHAT_COOKIE_SECURE` | `true` |
| `CHAT_ENABLE_HSTS` | `true` |
| `CHAT_PUBLIC_ORIGIN` | URL pública exacta, por ejemplo `https://tu-app.koyeb.app`. |
| `CHAT_ALLOWED_HOSTS` | Dominio público separado por comas; añade el dominio propio si se configura. |

Para una instancia Eco Micro con 2–3 usuarios simultáneos, los valores predeterminados
son deliberadamente conservadores: una respuesta activa por IP, tres generaciones
globales y doce solicitudes por minuto e IP. Pueden ajustarse con
`CHAT_MAX_CONCURRENT_GENERATIONS` y `CHAT_MAX_REQUESTS_PER_MINUTE` si las métricas lo
justifican.

La sesión es efímera y se conserva en la memoria de una sola instancia. Mantén una
réplica mientras se use esta arquitectura; si en el futuro se escala a varias
réplicas, sustituye el almacén de sesiones por Redis o una base de datos compartida.

## Seguridad y rendimiento

- La clave de OpenAI permanece exclusivamente en el backend y no se expone al navegador.
- Las cookies de sesión son `HttpOnly`, con `SameSite=Lax` y `Secure` en producción.
- El servidor aplica cabeceras de seguridad, limita tamaño de petición, tasa de uso,
  concurrencia y sesiones activas para proteger el coste y la disponibilidad.
- El contexto se limita a las últimas cuatro interacciones y los documentos extensos
  se reducen a sus secciones más relevantes antes de enviarlos al modelo.
- Los recursos estáticos se sirven con caché larga; las API y páginas no se almacenan
  en caché.

## Estructura

- `web_chat_app.py`: servidor web ASGI, sesiones, límites y conexión con la API.
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
control de versiones. Antes de publicar cambios, revisa siempre los archivos que se
incluirán con `git status`.
