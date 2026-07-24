import json
import unittest

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


if __name__ == "__main__":
    unittest.main()
