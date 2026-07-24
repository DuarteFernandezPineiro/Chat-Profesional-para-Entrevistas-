import unittest
from unittest.mock import patch

from fastapi.testclient import TestClient

import web_chat_app


class WebChatAppTests(unittest.TestCase):
    def test_sesion_guarda_contexto_en_el_servidor(self):
        store = web_chat_app.ConversationStore()
        session_id, _ = store.get_or_create(None)
        history, question_number, revision = store.begin(session_id, reset=False)

        self.assertEqual(history, [])
        self.assertEqual(question_number, 1)
        store.complete(session_id, revision, "Pregunta", "Respuesta")

        history, question_number, _ = store.begin(session_id, reset=False)
        self.assertEqual(history[-1]["content"], "Respuesta")
        self.assertEqual(question_number, 2)

    def test_reinicio_invalida_una_respuesta_antigua(self):
        store = web_chat_app.ConversationStore()
        session_id, _ = store.get_or_create(None)
        _, _, old_revision = store.begin(session_id, reset=False)
        history, question_number, new_revision = store.begin(session_id, reset=True)

        store.complete(session_id, old_revision, "Pregunta antigua", "Respuesta antigua")
        self.assertEqual(history, [])
        self.assertEqual(question_number, 1)
        self.assertNotEqual(old_revision, new_revision)

        current_history, current_question_number, _ = store.begin(session_id, reset=False)
        self.assertEqual(current_history, [])
        self.assertEqual(current_question_number, 1)

    def test_recordatorio_de_contacto_solo_en_preguntas_configuradas(self):
        for question_number in range(1, 27):
            expected = question_number in {3, 8, 15, 25}
            self.assertEqual(web_chat_app.mostrar_recordatorio_contacto(question_number), expected)

        self.assertIn("LinkedIn", web_chat_app.CONTACT_REMINDER)
        self.assertIn("mailto:", web_chat_app.CONTACT_REMINDER)
        self.assertIn("tel:", web_chat_app.CONTACT_REMINDER)

    def test_recordatorio_se_anade_al_final_en_los_tres_niveles(self):
        for detail_level in ("breve", "normal", "detallado"):
            self.assertIn(f"Nivel de detalle: {detail_level}", web_chat_app.chat_core.construir_instrucciones(detail_level))
            response = "".join(web_chat_app.incluir_recordatorio_contacto(iter(["Respuesta."]), 3))
            self.assertTrue(response.endswith(web_chat_app.CONTACT_REMINDER))

    def test_no_se_anade_recordatorio_en_otra_pregunta(self):
        response = "".join(web_chat_app.incluir_recordatorio_contacto(iter(["Respuesta."]), 4))
        self.assertEqual(response, "Respuesta.")

    def test_limite_global_de_concurrencia(self):
        gate = web_chat_app.RequestGate()
        for index in range(web_chat_app.MAX_CONCURRENT_GENERATIONS):
            gate.acquire(f"192.0.2.{index}")
        with self.assertRaises(Exception):
            gate.acquire("192.0.2.99")
        for index in range(web_chat_app.MAX_CONCURRENT_GENERATIONS):
            gate.release(f"192.0.2.{index}")

    def test_endpoints_de_estado_y_cabeceras_de_seguridad(self):
        with TestClient(web_chat_app.app, base_url="http://localhost") as client:
            response = client.get("/healthz")
            page = client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok"})
        self.assertEqual(response.headers["cache-control"], "no-store")
        self.assertEqual(page.status_code, 200)
        self.assertIn("Content-Security-Policy", page.headers)
        self.assertEqual(page.headers["x-frame-options"], "DENY")

    def test_api_mantiene_contexto_y_recordatorio_con_los_tres_niveles(self):
        def fake_stream(question, detail_level, history):
            self.assertIn(detail_level, {"breve", "normal", "detallado"})
            if history:
                self.assertEqual(history[-1]["role"], "assistant")
            yield f"Respuesta a: {question}"

        with (
            patch.object(web_chat_app, "CLIENT", object()),
            patch.object(web_chat_app, "SESSIONS", web_chat_app.ConversationStore()),
            patch.object(web_chat_app, "GATE", web_chat_app.RequestGate()),
            patch.object(web_chat_app, "stream_chat_response", fake_stream),
            TestClient(web_chat_app.app, base_url="http://localhost") as client,
        ):
            answers = []
            for index, detail_level in enumerate(("breve", "normal", "detallado"), start=1):
                response = client.post(
                    "/api/chat",
                    json={
                        "message": f"Pregunta {index}",
                        "detailLevel": detail_level,
                        "resetConversation": index == 1,
                        "history": [{"role": "user", "content": "No debe usarse"}],
                    },
                )
                self.assertEqual(response.status_code, 200)
                self.assertIn("duarte_chat_session", response.headers["set-cookie"])
                answers.append(response.content.decode("utf-8"))

        self.assertNotIn("## Contacto", answers[0])
        self.assertNotIn("## Contacto", answers[1])
        self.assertIn("## Contacto", answers[2])

    def test_api_rechaza_cuerpo_demasiado_grande(self):
        with TestClient(web_chat_app.app, base_url="http://localhost") as client:
            response = client.post("/api/chat", content=b"x" * (web_chat_app.MAX_REQUEST_BYTES + 1))

        self.assertEqual(response.status_code, 413)


if __name__ == "__main__":
    unittest.main()
