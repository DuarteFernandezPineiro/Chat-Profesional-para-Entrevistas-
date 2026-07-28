"""Regresiones opcionales contra OpenAI; no se ejecutan en la suite local normal."""

from __future__ import annotations

import os
import unittest

import chat_core
import web_chat_app


REGRESSION_CASES = (
    (
        "T01",
        "detallado",
        "Enumera los logros, resultados verificables y métricas concretas más sólidos "
        "de Duarte para LinkedIn. Para cada uno, indica el proyecto o experiencia que "
        "lo respalda y cualquier límite importante para no exagerarlo.",
        True,
    ),
    (
        "T02",
        "normal",
        "¿Cuáles son los tres proyectos más relevantes de Duarte para un puesto junior "
        "de IA generativa o RAG, y qué resultado verificable demuestra cada uno?",
        True,
    ),
    (
        "T03",
        "normal",
        "¿Cuáles son sus proyectos más relevantes?",
        True,
    ),
    ("T04", "breve", "¿Qué experiencia práctica tiene Duarte?", True),
    (
        "T05",
        "breve",
        "¿Qué habilidades técnicas puede defender Duarte con evidencia concreta?",
        False,
    ),
    (
        "T06",
        "breve",
        "¿Qué límites o carencias de su experiencia debería conocer un reclutador para "
        "no sobrevalorar el perfil?",
        False,
    ),
    (
        "T07",
        "breve",
        "¿Cuáles son los tres proyectos más relevantes de Duarte y qué demuestra cada uno?",
        False,
    ),
    (
        "T08",
        "breve",
        "¿Qué sabes del asistente profesional web de Duarte, cómo está construido y qué "
        "resultados verificables tiene?",
        False,
    ),
)


@unittest.skipUnless(
    os.getenv("RUN_LIVE_OPENAI_TESTS") == "1",
    "Requiere RUN_LIVE_OPENAI_TESTS=1 y una clave de OpenAI.",
)
class LiveRegressionTests(unittest.TestCase):
    def test_ocho_consultas_del_informe(self):
        self.assertIsNotNone(web_chat_app.CLIENT)
        shared_history: list[dict[str, str]] = []

        for case_id, detail_level, question, reset_history in REGRESSION_CASES:
            with self.subTest(case_id=case_id):
                if reset_history:
                    history: list[dict[str, str]] = []
                    if case_id == "T04":
                        shared_history = history
                else:
                    history = shared_history

                answer = "".join(
                    web_chat_app.stream_chat_response(
                        question,
                        detail_level,
                        history,
                    )
                )

                self.assertGreater(len(answer.strip()), 120)
                self.assertIsNone(chat_core.PUBLIC_PHONE_PATTERN.search(answer))
                self.assertNotIn("project_", answer.lower())
                self.assertNotIn("leer_documento", answer.lower())
                self.assertNotIn("buscar_proyectos", answer.lower())
                self.assertNotIn("leer_proyecto", answer.lower())
                self.assertNotIn("errerr", answer.lower())
                self.assertNotIn("could i retrieve", answer.lower())

                if case_id in {"T03", "T07"}:
                    self.assertIn("RAG", answer)
                    self.assertIn("Asistente profesional", answer)
                    self.assertIn("Bitcoin", answer)
                if case_id == "T08":
                    self.assertIn("FastAPI", answer)
                    self.assertIn("OpenAI Responses API", answer)

                if case_id in {"T04", "T05", "T06", "T07", "T08"}:
                    shared_history.extend(
                        (
                            {"role": "user", "content": question},
                            {"role": "assistant", "content": answer},
                        )
                    )
                    shared_history[:] = shared_history[-8:]


if __name__ == "__main__":
    unittest.main()
