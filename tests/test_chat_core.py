import json
import unittest
from pathlib import Path

import chat_core


class ChatCoreTests(unittest.TestCase):
    def test_catalogo_contiene_documentos_validos(self):
        catalog = chat_core.cargar_catalogo()

        self.assertEqual(len(catalog), 9)
        for metadata in catalog.values():
            self.assertTrue(chat_core.resolver_ruta_segura(metadata["file"]).is_file())

    def test_normaliza_aliases_de_detalle(self):
        self.assertEqual(chat_core.normalizar_nivel_detalle("corto"), "breve")
        self.assertEqual(chat_core.normalizar_nivel_detalle("estándar"), "normal")
        self.assertEqual(chat_core.normalizar_nivel_detalle("largo"), "detallado")

    def test_rechaza_nivel_de_detalle_desconocido(self):
        with self.assertRaises(ValueError):
            chat_core.normalizar_nivel_detalle("infinito")

    def test_instrucciones_cambian_con_el_nivel_de_respuesta(self):
        breve = chat_core.construir_instrucciones("breve")
        detallado = chat_core.construir_instrucciones("detallado")

        self.assertIn("Nivel de detalle: breve", breve)
        self.assertIn("Nivel de detalle: detallado", detallado)
        self.assertNotEqual(breve, detallado)

    def test_impide_rutas_fuera_del_proyecto(self):
        with self.assertRaises(ValueError):
            chat_core.resolver_ruta_segura("../secreto.txt")

    def test_lectura_documental_devuelve_contenido(self):
        catalog = chat_core.cargar_catalogo()
        trace = chat_core.AccessTrace()

        result = json.loads(
            chat_core.ejecutar_tool(
                "leer_documento",
                {"document_id": "education"},
                catalog,
                trace,
            )
        )

        self.assertTrue(result["ok"])
        self.assertIn("Grado en Inteligencia Artificial", result["content"])
        self.assertEqual(trace.accesses[0].document_id, "education")

    def test_acota_documento_extenso_y_prioriza_la_consulta(self):
        unrelated = "# Introducción\n" + ("contenido general " * 2_000)
        relevant = "# Proyecto de visión artificial\n" + ("visión artificial clasificación imágenes " * 2_000)
        content = f"{unrelated}\n{relevant}"

        selected = chat_core.seleccionar_contexto_documental(content, "¿Qué proyecto de visión artificial has desarrollado?")

        self.assertLessEqual(len(selected), chat_core.MAX_DOCUMENT_CONTEXT_CHARS)
        self.assertIn("Proyecto de visión artificial", selected)
        self.assertTrue(selected.endswith("[El documento se ha acotado a sus secciones más relevantes.]"))

    def test_indice_estructurado_contiene_proyectos_destacados(self):
        projects = chat_core.cargar_indice_proyectos()

        self.assertIn("project_rag_empresarial_tfg", projects)
        self.assertIn("project_asistente_profesional_web", projects)
        self.assertIn("project_bitcoin_sentiment_decision_chat", projects)
        self.assertTrue(projects["project_asistente_profesional_web"]["featured"])

    def test_busqueda_general_respeta_prioridad_de_entrevista(self):
        projects = chat_core.cargar_indice_proyectos()

        result = json.loads(
            chat_core.buscar_proyectos(
                "¿Cuáles son los tres proyectos más relevantes de Duarte?",
                3,
                projects,
            )
        )

        self.assertEqual(
            [project["project_id"] for project in result["projects"]],
            [
                "project_rag_empresarial_tfg",
                "project_asistente_profesional_web",
                "project_bitcoin_sentiment_decision_chat",
            ],
        )

    def test_busqueda_para_genai_prioriza_rag_y_proyectos_desplegados(self):
        projects = chat_core.cargar_indice_proyectos()

        result = json.loads(
            chat_core.buscar_proyectos(
                "Proyectos relevantes para IA generativa y RAG",
                3,
                projects,
            )
        )
        project_ids = [project["project_id"] for project in result["projects"]]

        self.assertEqual(project_ids[0], "project_rag_empresarial_tfg")
        self.assertEqual(project_ids[1], "project_asistente_profesional_web")
        self.assertIn("project_mineria_textos", project_ids)

    def test_aliases_del_asistente_resuelven_la_ficha_correcta(self):
        projects = chat_core.cargar_indice_proyectos()
        for alias in (
            "asistente profesional",
            "chat profesional de Duarte",
            "perfil profesional conversacional",
        ):
            result = json.loads(chat_core.buscar_proyectos(alias, 1, projects))
            self.assertEqual(
                result["projects"][0]["project_id"],
                "project_asistente_profesional_web",
            )

    def test_herramientas_estructuradas_de_proyecto(self):
        projects = chat_core.cargar_indice_proyectos()
        catalog = chat_core.cargar_catalogo()
        trace = chat_core.AccessTrace()

        search_result = json.loads(
            chat_core.ejecutar_tool(
                "buscar_proyectos",
                {"query": "asistente web", "limit": 2},
                catalog,
                trace,
                projects=projects,
            )
        )
        detail_result = json.loads(
            chat_core.ejecutar_tool(
                "leer_proyecto",
                {"project_id": "project_asistente_profesional_web"},
                catalog,
                trace,
                projects=projects,
            )
        )

        self.assertTrue(search_result["ok"])
        self.assertEqual(
            search_result["projects"][0]["project_id"],
            "project_asistente_profesional_web",
        )
        self.assertTrue(detail_result["ok"])
        self.assertIn("FastAPI", json.dumps(detail_result, ensure_ascii=False))

    def test_sanitizacion_bloquea_telefono_y_texto_interno(self):
        unsafe = (
            "Llama al +34 635 763 949. "
            "Could I retrieve project_asistente_profesional_web? Need tool likely "
            "leer_documento. errerrerrerr"
        )

        sanitized = chat_core.sanitizar_texto_publico(unsafe)

        self.assertNotIn("635", sanitized)
        self.assertNotIn("project_asistente", sanitized)
        self.assertNotIn("leer_documento", sanitized)
        self.assertNotIn("Could I retrieve", sanitized)
        self.assertNotIn("errerr", sanitized)

    def test_corpus_publico_no_contiene_telefonos(self):
        for document in Path(chat_core.PROJECT_ROOT / "Informacion").glob("*.md"):
            content = document.read_text(encoding="utf-8")
            self.assertIsNone(
                chat_core.PUBLIC_PHONE_PATTERN.search(content),
                f"Teléfono encontrado en {document.name}",
            )


if __name__ == "__main__":
    unittest.main()
