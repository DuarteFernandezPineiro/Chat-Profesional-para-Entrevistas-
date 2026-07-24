## 5.4. Índice de contenidos

- [5.1. Portada](#51-portada)
- [5.4. Índice de contenidos](#54-índice-de-contenidos)
- [5.5. Índice de ilustraciones](#55-índice-de-ilustraciones)
- [5.6. Índice de tablas](#56-índice-de-tablas)
- [5.7. Introducción](#57-introducción)
- [5.8. Objetivos](#58-objetivos)
  - [Objetivo general](#objetivo-general)
  - [Objetivos específicos](#objetivos-específicos)
  - [Alcance incluido](#alcance-incluido)
- [5.9. Resumen de la solución propuesta](#59-resumen-de-la-solución-propuesta)
- [5.10. Planificación y seguimiento](#510-planificación-y-seguimiento)
- [5.11. Arquitectura](#511-arquitectura)
  - [5.11.1. Visión general de la arquitectura](#5111-visión-general-de-la-arquitectura)
  - [5.11.2. Flujo offline de procesamiento e indexación](#5112-flujo-offline-de-procesamiento-e-indexación)
  - [5.11.3. Flujo online de consulta y generación](#5113-flujo-online-de-consulta-y-generación)
  - [5.11.4. Componentes principales](#5114-componentes-principales)
  - [5.11.5. Persistencia y contratos entre fases](#5115-persistencia-y-contratos-entre-fases)
  - [5.11.6. Interfaz y exposición remota](#5116-interfaz-y-exposición-remota)
  - [5.11.7. Diagrama arquitectónico](#5117-diagrama-arquitectónico)
- [5.12. Tecnologías e integración de productos de terceros](#512-tecnologías-e-integración-de-productos-de-terceros)
  - [5.12.1. Entorno de desarrollo, configuración y ejecución](#5121-entorno-de-desarrollo-configuración-y-ejecución)
  - [5.12.2. Procesamiento documental y representación intermedia](#5122-procesamiento-documental-y-representación-intermedia)
  - [5.12.3. Segmentación, indexación y recuperación de información](#5123-segmentación-indexación-y-recuperación-de-información)
  - [5.12.4. Generación de respuestas y servicios externos](#5124-generación-de-respuestas-y-servicios-externos)
  - [5.12.5. Interfaz web y exposición temporal](#5125-interfaz-web-y-exposición-temporal)
  - [5.12.6. Resumen de tecnologías y criterios de selección](#5126-resumen-de-tecnologías-y-criterios-de-selección)
- [5.13. Especificación y análisis de requisitos](#513-especificación-y-análisis-de-requisitos)
  - [5.13.1. Contexto y criterios de análisis](#5131-contexto-y-criterios-de-análisis)
  - [5.13.2. Requisitos funcionales](#5132-requisitos-funcionales)
  - [5.13.3. Requisitos no funcionales](#5133-requisitos-no-funcionales)
- [5.14. Diseño del software](#514-diseño-del-software)
  - [5.14.1. Criterios de diseño](#5141-criterios-de-diseño)
  - [5.14.2. Diseño estático: organización del sistema](#5142-diseño-estático-organización-del-sistema)
  - [5.14.3. Artefactos e interfaces entre fases](#5143-artefactos-e-interfaces-entre-fases)
  - [5.14.4. Diseño dinámico: flujo de preparación e indexación](#5144-diseño-dinámico-flujo-de-preparación-e-indexación)
  - [5.14.5. Diseño dinámico: flujo de consulta y generación](#5145-diseño-dinámico-flujo-de-consulta-y-generación)
- [5.15. Gestión de datos e información](#515-gestión-de-datos-e-información)
  - [5.15.1. Tipos de datos e información gestionados](#5151-tipos-de-datos-e-información-gestionados)
  - [5.15.2. Ciclo de vida documental](#5152-ciclo-de-vida-documental)
  - [5.15.3. Metadatos, trazabilidad y procedencia](#5153-metadatos-trazabilidad-y-procedencia)
  - [5.15.4. Persistencia y organización de artefactos](#5154-persistencia-y-organización-de-artefactos)
  - [5.15.5. Coherencia y actualización de la información](#5155-coherencia-y-actualización-de-la-información)
- [5.16. Pruebas llevadas a cabo](#516-pruebas-llevadas-a-cabo)
  - [5.16.1. Pruebas automáticas por componentes](#5161-pruebas-automáticas-por-componentes)
  - [5.16.2. Pruebas cualitativas de recuperación](#5162-pruebas-cualitativas-de-recuperación)
  - [5.16.3. Estado del conjunto de evaluación](#5163-estado-del-conjunto-de-evaluación)
  - [5.16.4. Métricas disponibles](#5164-métricas-disponibles)
  - [5.16.5. Resultados verificables](#5165-resultados-verificables)
  - [5.16.6. Alcance y limitaciones de la validación](#5166-alcance-y-limitaciones-de-la-validación)
- [5.17. Manual de usuario](#517-manual-de-usuario)
  - [5.17.1. Finalidad y público objetivo](#5171-finalidad-y-público-objetivo)
  - [5.17.2. Requisitos de ejecución](#5172-requisitos-de-ejecución)
  - [5.17.3. Instalación y configuración inicial](#5173-instalación-y-configuración-inicial)
  - [5.17.4. Preparación e indexación del corpus documental](#5174-preparación-e-indexación-del-corpus-documental)
  - [5.17.5. Consulta mediante interfaz web y línea de comandos](#5175-consulta-mediante-interfaz-web-y-línea-de-comandos)
  - [5.17.6. Acceso remoto temporal mediante ngrok](#5176-acceso-remoto-temporal-mediante-ngrok)
- [5.18. Principales aportaciones](#518-principales-aportaciones)
  - [5.18.1. Pipeline documental reproducible](#5181-pipeline-documental-reproducible)
  - [5.18.2. Trazabilidad y procedencia](#5182-trazabilidad-y-procedencia)
  - [5.18.3. Recuperación híbrida y reranking](#5183-recuperación-híbrida-y-reranking)
  - [5.18.4. Generación con evidencias identificables](#5184-generación-con-evidencias-identificables)
  - [5.18.5. Prototipo modular y operable en local](#5185-prototipo-modular-y-operable-en-local)
- [5.19. Conclusiones](#519-conclusiones)
  - [5.19.1. Síntesis del trabajo realizado](#5191-síntesis-del-trabajo-realizado)
  - [5.19.2. Grado de cumplimiento de los objetivos](#5192-grado-de-cumplimiento-de-los-objetivos)
  - [5.19.3. Conclusiones técnicas](#5193-conclusiones-técnicas)
  - [5.19.4. Proyección](#5194-proyección)
  - [5.19.5. Conclusiones personales](#5195-conclusiones-personales)
- [5.20. Vías de trabajo futuro](#520-vías-de-trabajo-futuro)
  - [5.20.1. Automatización y consolidación del conjunto de evaluación](#5201-automatización-y-consolidación-del-conjunto-de-evaluación)
  - [5.20.2. Mejora del procesamiento documental y del tratamiento de tablas](#5202-mejora-del-procesamiento-documental-y-del-tratamiento-de-tablas)
  - [5.20.3. Experimentación con normalización para recuperación léxica](#5203-experimentación-con-normalización-para-recuperación-léxica)
  - [5.20.4. Sistema de retroalimentación y mejora continua](#5204-sistema-de-retroalimentación-y-mejora-continua)
  - [5.20.5. Optimización del rendimiento de la recuperación](#5205-optimización-del-rendimiento-de-la-recuperación)
  - [5.20.6. Seguridad frente a instrucciones maliciosas](#5206-seguridad-frente-a-instrucciones-maliciosas)
  - [5.20.7. Evolución de la interfaz de usuario](#5207-evolución-de-la-interfaz-de-usuario)
  - [5.20.8. Soporte para uso simultáneo por varios usuarios](#5208-soporte-para-uso-simultáneo-por-varios-usuarios)
  - [5.20.9. Priorización de las líneas futuras](#5209-priorización-de-las-líneas-futuras)
- [5.21. Referencias](#521-referencias)
- [5.22. Anexo: información de reproducibilidad](#522-anexo-información-de-reproducibilidad)

## 5.5. Índice de ilustraciones

| Figura | Ilustración | Apartado |
| --- | --- | --- |
| Figura 1 | Arquitectura conceptual de un sistema RAG aplicado a documentación corporativa | 5.7 |
| Figura 2 | Flujo *offline* desde los PDF originales hasta los índices BM25 y Chroma | 5.9 |
| Figura 3 | Flujo *online* desde la consulta del usuario hasta la respuesta con fuentes | 5.9 |
| Figura 4 | Cronograma relativo de desarrollo por hitos técnicos y comparación entre esfuerzo previsto y real | 5.10 |
| Figura 5 | Arquitectura funcional del prototipo RAG y relación entre los flujos *offline* y *online* | 5.11.7 |
| Figura 6 | Flujo de preparación documental e indexación | 5.14.4 |
| Figura 7 | Secuencia de consulta y generación | 5.14.5 |
| Figura 8 | Ciclo de transformación y conservación de la procedencia documental | 5.15.2 |

## 5.6. Índice de tablas

| Tabla | Contenido | Apartado |
| --- | --- | --- |
| Tabla 1 | Planificación y seguimiento por hitos técnicos | 5.10 |
| Tabla 2 | Fases del flujo *offline* de procesamiento e indexación | 5.11.2 |
| Tabla 3 | Componentes principales del sistema | 5.11.4 |
| Tabla 4 | Artefactos persistentes y contratos entre fases | 5.11.5 |
| Tabla 5 | Tecnologías y criterios de selección | 5.12.6 |
| Tabla 6 | Requisitos funcionales | 5.13.2 |
| Tabla 7 | Requisitos no funcionales | 5.13.3 |
| Tabla 8 | Evidencia disponible para los grupos de requisitos | 5.13.3 |
| Tabla 9 | Subsistemas y responsabilidades principales | 5.14.2 |
| Tabla 10 | Artefactos e interfaces entre fases | 5.14.3 |
| Tabla 11 | Tipos de datos e información gestionados | 5.15.1 |
| Tabla 12 | Pruebas automáticas por componentes | 5.16.1 |
| Tabla 13 | Resultados verificables de la validación | 5.16.5 |
| Tabla 14 | Requisitos de ejecución del manual de usuario | 5.17.2 |
| Tabla 15 | Variables principales de configuración | 5.17.3 |
| Tabla 16 | Principales aportaciones y alcance demostrado | 5.18.5 |
| Tabla 17 | Cumplimiento de objetivos y limitaciones | 5.19.2 |
| Tabla 18 | Priorización de líneas futuras | 5.20.9 |
| Tabla 19 | Entorno base para reproducibilidad | 5.22 |
| Tabla 20 | Variables de configuración externa | 5.22 |
| Tabla 21 | Artefactos que deben conservarse para reproducir resultados | 5.22 |

## 5.7. Introducción

En los últimos años, la inteligencia artificial ha experimentado un avance especialmente relevante en el ámbito del procesamiento del lenguaje natural. La arquitectura *Transformer*, basada en mecanismos de atención, supuso un cambio de paradigma respecto a modelos secuenciales como las redes neuronales recurrentes y las arquitecturas LSTM [1]. A partir de este enfoque se desarrollaron modelos de lenguaje de gran tamaño capaces de generar texto, resumir documentos y responder preguntas.

Sin embargo, estos modelos presentan limitaciones cuando se aplican directamente a documentación interna. Su conocimiento depende de los datos utilizados durante el entrenamiento y no incluye necesariamente información privada, especializada o actualizada de una organización. Además, pueden producir respuestas plausibles que no estén respaldadas por las fuentes disponibles. Estas limitaciones hacen necesario recuperar evidencia documental antes de generar una respuesta y conservar la procedencia de la información utilizada.

Esta problemática es relevante en organizaciones que disponen de conocimiento distribuido en manuales, documentación técnica y procedimientos internos. En estos contextos, la información puede estar dispersa, redactada con distintos niveles de detalle y sujeta a cambios. Por tanto, no basta con generar respuestas en lenguaje natural: es necesario localizar fragmentos pertinentes y permitir que el usuario revise las fuentes documentales que respaldan la respuesta.

La técnica *Retrieval-Augmented Generation* (RAG) combina recuperación de información y generación de lenguaje [2], [3]. Antes de generar una respuesta, el sistema localiza fragmentos relevantes en una base documental y los incorpora al contexto del modelo generativo. Este enfoque permite orientar la respuesta hacia información concreta del corpus y reducir la dependencia exclusiva del conocimiento interno del modelo, aunque no garantiza por sí mismo la corrección de la respuesta final.

La comprensión inicial de este tipo de soluciones y de su aplicación al conocimiento empresarial se apoyó también en la revisión de casos prácticos de sistemas RAG, como el presentado por Gentile [21]. Este tipo de ejemplos permitió identificar el potencial de integrar modelos de lenguaje con documentación interna para facilitar consultas en lenguaje natural.

El presente Trabajo Fin de Grado aborda el diseño e implementación de un prototipo RAG híbrido para consultar documentación corporativa en formato PDF. El trabajo comprende el procesamiento de los documentos, la construcción de índices de búsqueda, la recuperación léxica y vectorial, la fusión y reordenación de resultados y la generación de respuestas acompañadas de referencias a las evidencias recuperadas.

El proyecto se enmarca en un caso de uso real vinculado a la empresa AHORA. Su resultado es un prototipo funcional desarrollado y validado en un entorno local sobre un corpus concreto. No constituye una plataforma corporativa terminada ni una solución preparada para producción.

Desde el punto de vista académico y técnico, el interés del trabajo reside en integrar técnicas actuales de recuperación aumentada en un flujo reproducible. El problema no consiste únicamente en conectar un modelo de lenguaje a un conjunto de documentos, sino en extraer y estructurar la información, dividirla en unidades recuperables, combinar estrategias de búsqueda y conservar la relación entre las respuestas y sus fuentes. El prototipo incorpora modularidad, persistencia de artefactos y filtrado técnico por metadatos. La autenticación, la autorización por identidad, la auditoría de accesos, la integración con sistemas corporativos y el despliegue escalable quedan fuera del alcance desarrollado.

```{mermaid}
flowchart LR
    subgraph PREP["Preparación del corpus"]
        PDF["Documentos PDF corporativos"] --> PROC["Extracción, limpieza y metadatos"]
        PROC --> CHUNKS["Fragmentos trazables"]
        CHUNKS --> BM25["Índice léxico BM25"]
        CHUNKS --> VEC["Embeddings y colección Chroma"]
    end

    subgraph QUERY["Consulta RAG"]
        USER["Usuario"] --> Q["Pregunta en lenguaje natural"]
        Q --> RET["Recuperación híbrida"]
        BM25 --> RET
        VEC --> RET
        RET --> FUS["Fusión RRF y reranking"]
        FUS --> EVID["Contexto evidencial con fuentes"]
        EVID --> LLM["Modelo generativo"]
        LLM --> ANSWER["Respuesta citada y revisable"]
        ANSWER --> USER
    end
```

**Figura 1.** Arquitectura conceptual de un sistema RAG aplicado a documentación corporativa. Elaboración propia.

## 5.8. Objetivos

### Objetivo general

El objetivo general es diseñar, implementar y validar un prototipo RAG híbrido para consultar documentación corporativa en PDF mediante lenguaje natural, conservando la trazabilidad entre las evidencias recuperadas y sus documentos de origen.

### Objetivos específicos

1. Analizar las limitaciones de la consulta manual y de la recuperación exclusivamente léxica sobre documentación corporativa heterogénea.
2. Diseñar un flujo reproducible de procesamiento de PDF que conserve artefactos intermedios y metadatos de procedencia.
3. Implementar una estrategia de segmentación que produzca unidades recuperables manteniendo su contexto documental.
4. Combinar recuperación léxica y semántica mediante fusión de rankings y reordenación de candidatos.
5. Construir un contexto evidencial que permita generar respuestas acompañadas de referencias a sus fuentes.
6. Proporcionar mecanismos de operación y consulta mediante línea de comandos y una interfaz web local.
7. Validar los contratos principales del software y disponer de infraestructura para evaluar la recuperación cuando exista un conjunto de referencia versionado.
8. Identificar las limitaciones necesarias para evolucionar desde el prototipo local hacia un sistema corporativo.

### Alcance incluido

El alcance implementado incluye el procesamiento de PDF, la generación de artefactos documentales trazables, la construcción de índices BM25 y Chroma, la recuperación híbrida mediante RRF, el reranking local BGE, la construcción del contexto de generación, la respuesta mediante Ollama, la CLI y una interfaz web local. También se conserva una clasificación documental y puede aplicarse un umbral de seguridad como filtro técnico durante la recuperación.

## 5.9. Resumen de la solución propuesta

La solución desarrollada es un prototipo RAG documental con dos flujos diferenciados. El flujo *offline* prepara el corpus: procesa los PDF, genera representaciones Markdown y metadatos, divide el contenido en fragmentos y construye los índices BM25 y Chroma. El flujo *online* recibe una consulta, ejecuta recuperación léxica y vectorial, fusiona los rankings mediante *Reciprocal Rank Fusion* (RRF), reordena los candidatos cuando el reranker está habilitado y construye el contexto que recibe el modelo generativo.

Los resultados intermedios se conservan como artefactos persistentes. Esta decisión permite revisar el procesamiento documental, reconstruir únicamente las fases afectadas por un cambio y mantener la relación entre cada fragmento y su documento de origen. El contrato técnico de estos artefactos se detalla en los apartados 5.14 y 5.15.

La recuperación combina BM25, adecuado para términos y códigos concretos, con embeddings almacenados en Chroma, orientados a relaciones semánticas. RRF combina las posiciones de ambos rankings sin sumar puntuaciones de escalas incompatibles. El reranker BGE, cuando se activa, vuelve a puntuar los pares consulta-fragmento y ordena los candidatos antes de seleccionar las evidencias finales.

El prompt de generación instruye al modelo servido mediante Ollama para que utilice el contexto recuperado, cite las fuentes numeradas y reconozca la falta de evidencia. Esta instrucción constituye un mecanismo de diseño y no una garantía de factualidad; la corrección de las respuestas generadas no se ha evaluado sistemáticamente.

La ejecución utilizada para caracterizar el corpus contiene 109 salidas documentales y 2.913 fragmentos indexados. La colección vectorial emplea `text-embedding-3-large` con 3.072 dimensiones. Estas cifras describen los artefactos incluidos en la versión revisada y pueden variar si se modifica el corpus, el *chunking* o la configuración de indexación.

El prototipo se utiliza mediante CLI o interfaz web local. La exposición con ngrok se limita a demostraciones controladas. La versión actual no incorpora autenticación, autorización por identidad, auditoría de accesos, evaluación global del corpus, concurrencia multiusuario validada ni despliegue productivo.

```{mermaid}
flowchart LR
    PDF["PDF corporativo"] --> HASH["Hash y registro documental"]
    HASH --> RAW["document_raw.md"]
    RAW --> CLEAN["Limpieza y normalización"]
    CLEAN --> LIMPIO["document_limpio.md"]
    CLEAN --> META["document_metadata.json"]
    LIMPIO --> CHUNK["Chunking"]
    META --> CHUNK
    CHUNK --> CHUNKS["chunks.json"]
    CHUNKS --> BM25["Índice BM25"]
    CHUNKS --> EMB["Embeddings OpenAI"]
    EMB --> CHROMA["Colección Chroma"]
```

**Figura 2.** Flujo *offline* desde los PDF originales hasta los índices BM25 y Chroma. Elaboración propia.

```{mermaid}
flowchart LR
    USER["Usuario"] --> UI["CLI o interfaz web local"]
    UI --> QUERY["Consulta y filtros"]
    QUERY --> HYBRID["HybridRetriever"]
    HYBRID --> BM25S["Búsqueda BM25"]
    HYBRID --> CHROMAS["Búsqueda vectorial Chroma"]
    BM25S --> RRF["Fusión RRF"]
    CHROMAS --> RRF
    RRF --> FILTERS["Filtros por metadatos"]
    FILTERS --> RERANK["Reranking BGE/Jina"]
    RERANK --> CONTEXT["Contexto evidencial numerado"]
    CONTEXT --> GEN["Modelo generativo configurado"]
    GEN --> ANSWER["Respuesta con citas y fuentes"]
    ANSWER --> UI
```

**Figura 3.** Flujo *online* desde la consulta del usuario hasta la respuesta con fuentes. Elaboración propia.

## 5.10. Planificación y seguimiento

El desarrollo siguió una estrategia iterativa e incremental organizada por hitos técnicos. Cada hito produjo un resultado verificable y permitió realizar pruebas de componentes antes de integrar la fase siguiente. La planificación se documenta de forma retrospectiva por fases, ya que no se conserva un registro temporal suficientemente preciso para reconstruir fechas concretas de inicio y fin sin introducir estimaciones. La duración total estimada del desarrollo fue de aproximadamente trece semanas, distribuidas según las necesidades técnicas de cada fase.

| Hito                       | Duración estimada | Horas estimadas | Horas reales | Trabajo realizado                                                                                      | Resultado verificable                                               | Evolución durante el desarrollo                                                                             |
| -------------------------- | ----------------- | --------------- | ------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| Análisis y diseño inicial  | 1 semana          | 25 h            | 28 h         | Delimitación del caso de uso, flujo de datos y arquitectura.                                           | Estructura modular y contratos iniciales.                           | El alcance se restringió a documentos PDF y a la ejecución local del sistema.                               |
| Procesamiento documental   | 3 semanas         | 70 h            | 82 h         | Extracción, limpieza y generación de metadatos.                                                        | `document_raw.md`, `document_limpio.md` y `document_metadata.json`. | Se reforzaron la trazabilidad, la preservación de la estructura documental y el tratamiento de incidencias. |
| Segmentación               | 2 semanas         | 45 h            | 50 h         | Definición e implementación de reglas jerárquicas sobre Markdown para generar fragmentos recuperables. | `chunks.json`.                                                      | Se incorporaron campos diferenciados para BM25, embeddings y generación de contexto.                        |
| Indexación                 | 1 semana          | 25 h            | 28 h         | Construcción del índice BM25 y de la colección vectorial en Chroma.                                    | Índices persistentes.                                               | Se establecieron procedimientos explícitos de reconstrucción y actualización de los índices.                |
| Recuperación               | 3 semanas         | 70 h            | 78 h         | Integración de BM25, embeddings, fusión mediante RRF, filtros y reranking.                             | Ranking híbrido trazable.                                           | Se añadió reranking BGE local y filtrado técnico basado en metadatos.                                       |
| Generación e interfaz      | 1 semana          | 30 h            | 36 h         | Construcción del contexto con fuentes, integración con Ollama, interfaz CLI e interfaz web.            | Prototipo consultable en local.                                     | Se incorporó ngrok únicamente para demostraciones controladas desde dispositivos externos.                  |
| Validación y documentación | 2 semanas         | 35 h            | 42 h         | Pruebas de componentes, análisis de resultados, utilidades de diagnóstico y documentación técnica.     | Suite automatizada e infraestructura de evaluación.                 | Se realizó una evaluación global del proyecto a través de test y pruebas reales.                            |
| **Total**                  | **13 semanas**    | **300 h**       | **344 h**    | —                                                                                                      | —                                                                   | —                                                                                                           |

La fase de procesamiento documental concentró una parte relevante del esfuerzo debido a la heterogeneidad del corpus. Los documentos presentaban diferencias en estructura, extensión, calidad de extracción, presencia de tablas, secciones poco uniformes y formatos internos diversos. Por ello, fue necesario realizar varias iteraciones sobre el proceso de extracción y limpieza para encontrar una solución suficientemente generalizable que preservase la información relevante y la organización semántica de los documentos sin introducir pérdidas de calidad que afectasen a las fases posteriores de *chunking* y recuperación.

La persistencia de artefactos entre fases permitió modificar componentes sin repetir siempre el procesamiento completo. Por ejemplo, un cambio en la estrategia de segmentación exige regenerar `chunks.json` y reconstruir los índices, pero no necesariamente volver a extraer y limpiar los PDF. De forma análoga, un cambio en el reranker o en el modelo generativo puede estudiarse reutilizando los artefactos documentales e índices ya disponibles.

Las principales desviaciones respecto al planteamiento inicial fueron la incorporación de la recuperación híbrida mediante RRF, el reranking local, los filtros por metadatos y la interfaz web. Estas ampliaciones mejoraron la capacidad demostrativa y la calidad de recuperación del prototipo, aunque también introdujeron dependencias adicionales y dejaron como trabajo futuro una evaluación cuantitativa reproducible, pruebas de carga, validación con usuarios y mecanismos de seguridad propios de un entorno de producción.

En un principio se quería desarrollar un sistema RAG listo para el uso multiusuario empresarial, pero devido a las dificultades técnicas de seguridad y limitaciones de software, se dejan estas etapas para futuras mejoras.

```{mermaid}
flowchart LR
    A["Análisis y diseño inicial<br/>1 semana<br/>25 h previstas / 28 h reales"]
    B["Procesamiento documental<br/>3 semanas<br/>70 h previstas / 82 h reales"]
    C["Segmentación<br/>2 semanas<br/>45 h previstas / 50 h reales"]
    D["Indexación<br/>1 semana<br/>25 h previstas / 28 h reales"]
    E["Recuperación<br/>3 semanas<br/>70 h previstas / 78 h reales"]
    F["Generación e interfaz<br/>1 semana<br/>30 h previstas / 36 h reales"]
    G["Validación y documentación<br/>2 semanas<br/>35 h previstas / 42 h reales"]

    A --> B --> C --> D --> E --> F --> G
```

**Figura 4.** Cronograma relativo de desarrollo por hitos técnicos y comparación entre esfuerzo previsto y real. Elaboración propia.

## 5.11. Arquitectura

### 5.11.1. Visión general de la arquitectura

La solución desarrollada se articula como un sistema RAG documental híbrido orientado a la consulta de documentación corporativa en formato PDF mediante lenguaje natural. Su finalidad es transformar documentos estáticos en una base de conocimiento recuperable, localizar los fragmentos más relevantes para una consulta y generar respuestas fundamentadas en la evidencia documental obtenida.

La arquitectura se ha diseñado siguiendo un enfoque modular y desacoplado. Cada etapa recibe artefactos con una estructura definida, realiza una responsabilidad concreta y genera salidas persistentes que pueden reutilizarse en fases posteriores. Esta organización facilita la mantenibilidad del sistema y permite introducir mejoras en componentes específicos sin necesidad de repetir todo el procesamiento documental.

El sistema se divide en dos flujos principales:

* El flujo *offline* prepara la base de conocimiento: procesa los PDFs, extrae y limpia el contenido, genera fragmentos estructurados e construye los índices de recuperación.
* El flujo *online* responde a las consultas de usuario: recupera candidatos desde los índices, fusiona y reordena los resultados, construye un contexto evidencial y genera una respuesta mediante un modelo de lenguaje local servido con Ollama.

La arquitectura cubre el procesamiento documental, la indexación léxica y vectorial, la recuperación híbrida, el reranking, la generación de respuestas y la interacción mediante línea de comandos o interfaz web local. No se pretende que constituya una plataforma documental corporativa completa ni un sistema multiusuario de producción.

### 5.11.2. Flujo offline de procesamiento e indexación

El flujo *offline* tiene como objetivo convertir los documentos PDF de entrada en una base de conocimiento preparada para la recuperación. Los documentos se localizan en la carpeta `PDFs/` o se indican explícitamente mediante la interfaz de línea de comandos. A partir de ellos se generan artefactos persistentes en `outputs/` y en los directorios de índices situados en `data/indexes/`.

La extracción documental combina PyMuPDF con servicios de OpenAI para obtener una representación textual estructurada del contenido. Este proceso genera un archivo `document_raw.md`, que conserva el contenido extraído y permite revisar la calidad de la conversión desde el documento original.

Posteriormente, la fase de limpieza y normalización produce el archivo `document_limpio.md`. Este documento constituye una versión estructurada y preparada para el proceso de segmentación, en la que se preserva la organización semántica del contenido y se reduce el ruido documental que podría afectar a la recuperación posterior.

De forma complementaria, el sistema genera un archivo `document_metadata.json` que recoge información de trazabilidad, como el identificador del documento, su hash, el estado de procesamiento y el nivel de seguridad asignado. El uso de hashes permite identificar documentos ya procesados y evita repetir operaciones cuando no se han producido cambios relevantes en la fuente.

La fase de *chunking* recibe el documento limpio y sus metadatos para generar `chunks.json`. Este archivo contiene unidades recuperables con identificador propio, contenido, ruta jerárquica de sección, información de páginas cuando está disponible, nivel de seguridad y textos especializados para los mecanismos de recuperación léxica y vectorial.

A partir de los *chunks* se construyen dos índices independientes:

* Un índice BM25, basado en la representación textual `content_for_bm25`, orientado a recuperar coincidencias léxicas y terminología específica del dominio corporativo.
* Un índice vectorial persistente en Chroma, construido a partir de `content_for_embedding` y embeddings generados mediante OpenAI, orientado a recuperar fragmentos semánticamente relacionados con la consulta.

La separación entre ambos índices permite aplicar estrategias de recuperación complementarias. BM25 resulta especialmente útil cuando la consulta contiene términos técnicos, nombres propios o expresiones concretas, mientras que la búsqueda vectorial mejora la recuperación cuando existe equivalencia semántica entre la pregunta y el contenido documental aunque no coincidan literalmente las mismas palabras.

| Fase                      | Entrada principal                             | Salida principal             | Finalidad                                                         |
| ------------------------- | --------------------------------------------- | ---------------------------- | ----------------------------------------------------------------- |
| Localización documental   | Carpeta `PDFs/` o ruta PDF                    | Documento a procesar         | Identificar la fuente documental de entrada.                      |
| Extracción                | PDF, configuración y prompts                  | `document_raw.md`            | Obtener una representación textual auditable del documento.       |
| Limpieza y estructuración | Markdown bruto y configuración de limpieza    | `document_limpio.md`         | Preparar un contenido coherente y estructurado para segmentación. |
| Metadatos y registro      | Documento, hash y resultados de procesamiento | `document_metadata.json`     | Mantener trazabilidad, estado y nivel de seguridad documental.    |
| Segmentación              | Documento limpio y metadatos                  | `chunks.json`                | Generar unidades recuperables con contexto y metadatos.           |
| Indexación BM25           | `content_for_bm25`                            | Índice léxico persistente    | Permitir recuperación basada en términos.                         |
| Indexación vectorial      | `content_for_embedding`                       | Colección Chroma persistente | Permitir recuperación basada en similitud semántica.              |

### 5.11.3. Flujo online de consulta y generación

El flujo *online* comienza cuando el usuario formula una pregunta desde la CLI, el chat interactivo o la interfaz web local. La consulta se procesa mediante el componente `HybridRetriever`, que coordina la recuperación léxica en BM25 y la recuperación semántica sobre la colección vectorial de Chroma.

Cada recuperador genera una lista ordenada de candidatos con información sobre el fragmento, la posición obtenida en el ranking, la puntuación calculada y sus metadatos documentales. Dado que las puntuaciones de BM25 y de similitud vectorial no son directamente comparables, el sistema no las combina mediante una suma directa. En su lugar, fusiona ambos rankings mediante *Reciprocal Rank Fusion* (RRF), agrupando los resultados por `chunk_id`.

Tras la fusión, el sistema puede aplicar filtros basados en metadatos, como el documento de origen, la ruta de sección o el nivel máximo de seguridad permitido. Este mecanismo permite restringir técnicamente los resultados recuperados según la clasificación documental disponible. No obstante, debe diferenciarse de un sistema completo de autenticación y autorización por usuario, que queda fuera del alcance de la implementación.

Cuando el reranking está habilitado, los candidatos obtenidos mediante RRF se reordenan con un reranker BGE basado en FlagEmbedding. Este componente evalúa conjuntamente la consulta y el contenido de cada fragmento, proporcionando una estimación de relevancia más precisa para priorizar los textos que mejor responden a la necesidad informativa del usuario.

Los fragmentos finales se transforman en un contexto evidencial mediante la función `build_evidence_context()`. Cada fuente se identifica con marcadores como `[S1]`, `[S2]` o `[S3]`, e incorpora información de trazabilidad relativa al documento, las páginas, la sección y el identificador del *chunk*. Este contexto se envía al módulo de generación, que utiliza Ollama mediante el endpoint `/api/chat`.

El generador recibe únicamente las fuentes recuperadas como contexto documental y el prompt le indica que se apoye en ellas. Cuando no se recupera contexto suficiente, la aplicación solicita una respuesta de evidencia insuficiente. Este comportamiento reduce el uso de información ajena al corpus, pero no lo garantiza sin una evaluación específica del modelo.

### 5.11.4. Componentes principales

| Componente               | Responsabilidad                                                                                               |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| CLI principal            | Orquestar el procesamiento documental, la indexación, las consultas y las tareas de evaluación.               |
| Configuración global     | Cargar rutas, modelos, credenciales, parámetros de recuperación y valores definidos en `.env`.                |
| Extracción documental    | Transformar PDFs en contenido Markdown estructurado y revisable.                                              |
| Limpieza documental      | Normalizar el contenido extraído y conservar una estructura semántica adecuada para recuperación.             |
| Gestión de metadatos     | Mantener identificadores, hashes, estados de procesamiento y niveles de seguridad.                            |
| Chunking                 | Dividir los documentos en fragmentos recuperables con contexto y trazabilidad.                                |
| Índice BM25              | Proporcionar recuperación léxica sobre los fragmentos generados.                                              |
| Embeddings y Chroma      | Generar y persistir representaciones vectoriales para recuperación semántica.                                 |
| Recuperador híbrido      | Coordinar BM25, Chroma, filtros de metadatos y selección inicial de candidatos.                               |
| Fusión RRF               | Combinar rankings heterogéneos sin mezclar directamente puntuaciones incompatibles.                           |
| Reranker BGE             | Reordenar los candidatos según la relevancia conjunta entre consulta y fragmento.                             |
| Generación con Ollama    | Construir respuestas fundamentadas en el contexto recuperado.                                                 |
| Interfaz web             | Permitir consultas desde un navegador y mostrar respuestas, fuentes y diagnósticos.                           |
| Integración con ngrok    | Exponer temporalmente la interfaz local mediante una URL HTTPS pública para demostraciones y pruebas remotas. |
| Validación y diagnóstico | Ejecutar pruebas unitarias, diagnósticos y métricas de recuperación cuando existe un conjunto de referencia.  |

### 5.11.5. Persistencia y contratos entre fases

La persistencia de artefactos constituye uno de los elementos centrales de la arquitectura. Cada documento procesado dispone de una carpeta propia en `outputs/<documento>/`, donde se almacenan los archivos generados durante las fases de extracción, limpieza y segmentación.

Los principales artefactos son los siguientes:

| Artefacto                | Propósito                                                                             |
| ------------------------ | ------------------------------------------------------------------------------------- |
| `document_raw.md`        | Conserva el contenido extraído del PDF antes de la limpieza y estructuración final.   |
| `document_limpio.md`     | Proporciona el contenido estructurado que se utiliza como entrada para el *chunking*. |
| `document_metadata.json` | Recoge trazabilidad, hash, estado de procesamiento y clasificación de seguridad.      |
| `chunks.json`            | Contiene los fragmentos recuperables y sus metadatos asociados.                       |
| Índice BM25              | Almacena la representación léxica de los *chunks* para recuperación por términos.     |
| Colección Chroma         | Almacena vectores, contenido y metadatos para recuperación semántica.                 |

Estos artefactos actúan como contratos entre módulos. Por ejemplo, cualquier modificación en la estrategia de segmentación obliga a regenerar `chunks.json` y reconstruir los índices posteriores, pero no requiere repetir la extracción desde los PDFs originales. De manera equivalente, una modificación en el reranker o en el modelo de generación puede evaluarse utilizando los resultados de recuperación existentes, sin alterar el procesamiento documental previo.

Esta separación mejora la eficiencia del desarrollo, facilita la depuración y permite identificar con mayor precisión el origen de posibles errores o degradaciones de calidad en la respuesta final.

### 5.11.6. Interfaz y exposición remota

El sistema puede utilizarse desde la línea de comandos, mediante un chat interactivo o a través de una interfaz web local. La interfaz expone el endpoint `/api/answer`, que recibe la pregunta del usuario y devuelve la respuesta generada, las fuentes utilizadas, los fragmentos recuperados y datos de diagnóstico asociados a la recuperación.

Como complemento, el módulo de ngrok permite crear un túnel HTTPS temporal hacia la interfaz local. Esta funcionalidad facilita la demostración del sistema desde otros dispositivos o redes sin necesidad de desplegar una infraestructura pública propia. No obstante, su propósito es experimental y demostrativo; no debe considerarse un mecanismo de despliegue productivo ni una solución de control de acceso.

### 5.11.7. Diagrama arquitectónico

La Figura 5 resume la arquitectura y diferencia la preparación del corpus de la consulta interactiva.

```{mermaid}
flowchart LR
    subgraph OFF["Flujo offline"]
        PDF["Documentos PDF"] --> EXT["Extracción y limpieza"]
        EXT --> ART["Markdown y metadatos"]
        ART --> CH["Chunking"]
        CH --> CJ["chunks.json"]
        CJ --> BM["Índice BM25"]
        CJ --> EM["Embeddings OpenAI"]
        EM --> VC["Colección Chroma"]
    end
    subgraph ON["Flujo online"]
        Q["Consulta"] --> LEX["Recuperación BM25"]
        Q --> SEM["Recuperación vectorial"]
        LEX --> RRF["Fusión RRF"]
        SEM --> RRF
        RRF --> FIL["Filtros por metadatos"]
        FIL --> RR["Reranking opcional"]
        RR --> CTX["Contexto con fuentes"]
        CTX --> OLL["Generación con Ollama"]
        OLL --> UI["CLI o interfaz web local"]
    end
    BM --> LEX
    VC --> SEM
```

**Figura 5.** Arquitectura funcional del prototipo RAG y relación entre los flujos *offline* y *online*. Elaboración propia.

## 5.12. Tecnologías e integración de productos de terceros

El sistema desarrollado combina lógica propia, bibliotecas de código abierto y servicios externos para implementar un sistema RAG documental. La selección tecnológica se realizó según las necesidades de cada fase: procesamiento de documentos PDF, preparación de fragmentos, indexación, recuperación híbrida, generación de respuestas e interacción con el usuario.

Este apartado no pretende enumerar todas las dependencias del proyecto, sino justificar los componentes que influyen de forma relevante en su arquitectura, rendimiento, mantenibilidad y capacidad de recuperación.

### 5.12.1. Entorno de desarrollo, configuración y ejecución

El proyecto se implementó en Python por la disponibilidad de bibliotecas consolidadas para procesamiento documental, integración con servicios de inteligencia artificial, recuperación de información, bases de datos vectoriales y automatización de flujos de trabajo.

Python se emplea en todas las fases del sistema: extracción y limpieza documental, *chunking*, indexación, recuperación híbrida, reranking, generación, interfaz web y pruebas. Las dependencias se declaran en `requirements.txt`, lo que facilita reproducir el entorno de ejecución en otros equipos.

La configuración se gestiona mediante variables de entorno cargadas desde `.env` con `python-dotenv`. Este mecanismo permite separar del código fuente las claves de acceso, rutas, modelos y parámetros de recuperación. De este modo, la reproducción del sistema depende de mantener alineados el repositorio, las dependencias y la configuración del entorno.

Las operaciones principales se exponen mediante comandos de línea basados en `argparse`, permitiendo ejecutar de forma independiente el procesamiento documental, la indexación, la búsqueda híbrida o la interfaz web. La biblioteca `rich` se emplea únicamente para mejorar la legibilidad de los mensajes y diagnósticos mostrados en terminal.

### 5.12.2. Procesamiento documental y representación intermedia

La entrada principal del sistema está formada por documentos PDF corporativos con estructuras y contenidos diversos. Para su procesamiento se utiliza PyMuPDF, importada como `fitz`, mediante el módulo `src/extraccion_limpieza/pdf_utils.py` [16].

PyMuPDF se seleccionó porque permite acceder al contenido página a página, obtener información estructural del documento y renderizar páginas como imágenes cuando el proceso de extracción lo requiere. Estas capacidades resultan adecuadas para documentos con texto, tablas, formularios, encabezados o elementos visuales cuya interpretación no puede depender únicamente de una extracción textual simple.

La extracción y limpieza semántica se realizan mediante la API de OpenAI, integrada a través del SDK `openai` [9], [10]. Esta decisión se basa en la necesidad de tratar documentos con estructuras variables y contenido visual, para los que un enfoque exclusivamente basado en reglas locales puede resultar insuficiente. El sistema puede enviar páginas individuales o representaciones visuales acompañadas de instrucciones específicas almacenadas en `prompts/`.

Las respuestas producidas durante estas fases se validan mediante modelos definidos con Pydantic. Esta biblioteca permite comprobar que las estructuras generadas para extracción, limpieza, metadatos y configuración cumplen el formato esperado antes de que sean utilizadas por las fases posteriores. Asimismo, `tenacity` aplica reintentos ante errores transitorios de red o disponibilidad en las llamadas a servicios externos.

El resultado se conserva en Markdown estructurado. El archivo `document_raw.md` mantiene una representación inicial del contenido extraído, mientras que `document_limpio.md` contiene la versión preparada para la segmentación. Esta representación intermedia desacopla el PDF original de las fases posteriores, facilita la revisión de la extracción y permite reutilizar una estructura textual estable para el *chunking* e indexación.

No obstante, la calidad del resultado depende de la extracción y de las instrucciones empleadas. Por ello, este proceso no elimina la necesidad de revisión humana cuando se procesen documentos especialmente sensibles o de alta criticidad.

### 5.12.3. Segmentación, indexación y recuperación de información

La segmentación se implementa mediante lógica propia en `src/chunking/chunker.py`. El proceso analiza la estructura Markdown, incluyendo encabezados, rutas de sección, listas, tablas y patrones documentales, para generar los fragmentos almacenados en `chunks.json`.

Se optó por reglas jerárquicas y heurísticas en lugar de un modelo neuronal para definir los límites de los fragmentos. Esta decisión reduce el coste de procesamiento, permite controlar explícitamente los criterios de segmentación y facilita mantener la trazabilidad entre cada *chunk* y la estructura documental de la que procede. Como contrapartida, la calidad de los fragmentos depende de la calidad del Markdown limpio y del mantenimiento de las reglas implementadas.

La recuperación léxica se basa en BM25 mediante `rank-bm25` y su implementación `BM25Okapi` [4], [5], [17]. El índice se construye a partir de `content_for_bm25` y se persiste en `data/indexes/bm25/`. BM25 resulta útil para recuperar códigos, referencias exactas, cláusulas, nombres propios y terminología específica, aunque presenta limitaciones cuando la consulta utiliza un vocabulario diferente al del documento.

Para una consulta $q$ y un documento o fragmento $d$, BM25 puede expresarse como:

$$
\operatorname{BM25}(q,d)=
\sum_{t \in q}
\operatorname{IDF}(t)
\cdot
\frac{f(t,d)(k_1+1)}
{f(t,d)+k_1\left(1-b+b\frac{|d|}{\operatorname{avgdl}}\right)}
$$

donde $f(t,d)$ es la frecuencia del término, $|d|$ la longitud del fragmento,
$\operatorname{avgdl}$ la longitud media y $k_1$ y $b$ los parámetros de
saturación y normalización.

La recuperación semántica utiliza *embeddings* generados mediante la API de OpenAI y almacenados en ChromaDB [6], [11], [12]. La relación entre la consulta $q$ y un fragmento $d$ puede representarse conceptualmente mediante la similitud coseno:

$$
\operatorname{sim}(q,d)=
\frac{\mathbf{e}_q \cdot \mathbf{e}_d}
{\lVert \mathbf{e}_q \rVert \, \lVert \mathbf{e}_d \rVert}
$$

donde $\mathbf{e}_q$ y $\mathbf{e}_d$ son los *embeddings* de la consulta y del fragmento, respectivamente. La implementación delega en Chroma la métrica configurada y la recuperación de los vecinos más próximos.

La versión evaluada utiliza `text-embedding-3-large`, con vectores de 3.072 dimensiones. Es el modelo de embeddings más completo pero otros text-embedding-3-small que generan vectores de 1536 dimensiones otorgan resultados extremadamente precisos.

ChromaDB se utiliza como base vectorial persistente mediante `chromadb.PersistentClient`. Se seleccionó por su adecuación a una ejecución local, la posibilidad de persistir vectores y metadatos sin desplegar infraestructura adicional, y su integración directa con el entorno Python. Esta decisión permite concentrar el desarrollo propio en la preparación de los datos, los filtros, la recuperación híbrida y la evaluación, en lugar de implementar una solución vectorial desde cero. Como consecuencia, cualquier cambio en el modelo de embeddings, sus dimensiones o el contenido indexado requiere reconstruir la colección vectorial.

Durante la consulta, OpenAI también interviene para generar el embedding de la pregunta del usuario antes de realizar la búsqueda vectorial. Por tanto, aunque la generación final se ejecuta localmente mediante Ollama, la consulta semántica requiere acceso al servicio de embeddings configurado.

La recuperación híbrida combina BM25 y ChromaDB mediante *Reciprocal Rank Fusion* (RRF) [7]. Para un candidato $c$, la puntuación utilizada puede expresarse como:

$$
\operatorname{RRF}(c)=
\sum_{r \in R}
\frac{w_r}{k+\operatorname{rank}_r(c)}
$$

donde $R$ es el conjunto de recuperadores, $w_r$ su peso, $k$ una constante de amortiguación y $\operatorname{rank}_r(c)$ la posición del candidato. RRF permite combinar escalas heterogéneas sin sumar directamente sus puntuaciones. Solo puede fusionar candidatos recuperados previamente por alguno de los métodos.

Tras la fusión, los resultados pueden reordenarse mediante `BAAI/bge-reranker-v2-m3`, integrado a través de FlagEmbedding [8], [13], [14]. El reranker evalúa cada par consulta-fragmento mediante la función conceptual $s_i=f_\theta(q,c_i)$ y ordena los candidatos por $s_i$ de forma descendente. Su finalidad es promover los candidatos más relacionados antes de construir el contexto; la magnitud de esta mejora puede analizarse mediante un conjunto de evaluación reproducible. Su uso implica descarga de modelos, mayor consumo de memoria y una latencia adicional dependiente de PyTorch, `transformers` y los recursos del equipo.

### 5.12.4. Generación de respuestas y servicios externos

OpenAI constituye el principal servicio externo empleado durante la extracción, limpieza documental, indexación semántica y generación del embedding de las consultas. En consecuencia, el sistema no es completamente local: la documentación procesada o sus representaciones pueden enviarse al proveedor según la fase y la configuración. Esta integración facilita procesar documentos complejos y obtener representaciones vectoriales de alta calidad, pero requiere credenciales, conectividad y consideración de las políticas de privacidad aplicables a la documentación procesada.

La generación final de respuestas se realiza mediante Ollama. El módulo `src/generation/ollama/client.py` se comunica con su endpoint `/api/chat` y envía la pregunta junto con el contexto evidencial recuperado [15].

Ollama se seleccionó para desacoplar la generación final del proveedor utilizado para embeddings y permitir la utilización de modelos locales configurables. Durante la generación no se envía el contexto documental a un servicio externo: el modelo local recibe únicamente los fragmentos recuperados por el pipeline. Esta decisión aporta mayor control operativo, aunque el rendimiento depende del modelo elegido y de los recursos de CPU o GPU disponibles.

El modelo utilizado y la dirección del servicio se configuran mediante `.env`. La ejecución requiere que Ollama esté activo y que el modelo seleccionado se encuentre descargado localmente.

### 5.12.5. Interfaz web y exposición temporal

La interfaz web se implementa mediante HTML, CSS y JavaScript nativo, sin incorporar un framework web adicional. El backend utiliza `ThreadingHTTPServer`, incluido en la biblioteca estándar de Python [18], para servir los recursos estáticos y gestionar las solicitudes al endpoint `/api/answer`.

La elección de una interfaz ligera se ajusta al alcance del proyecto, centrado en ejecución local y demostración funcional. Permite mostrar la respuesta generada, las fuentes utilizadas, los fragmentos recuperados y determinada información de diagnóstico sin introducir dependencias adicionales.

El servidor HTTP utiliza hilos, pero el pipeline compartido no se ha diseñado ni validado para solicitudes simultáneas. La aplicación debe considerarse un prototipo de un solo usuario y no ofrece garantías de concurrencia segura.

La integración opcional con ngrok permite exponer temporalmente la interfaz local mediante una URL HTTPS [19]. El módulo `src/retrieval/hybrid/ngrok.py` inicia el binario de ngrok como proceso externo y consulta su API local para obtener la dirección pública generada. Esta solución facilita demostraciones desde otros dispositivos sin desplegar infraestructura propia, pero requiere que ngrok esté instalado y autenticado mediante `NGROK_AUTHTOKEN`.

Dado que la aplicación no incorpora autenticación ni control de acceso, esta funcionalidad debe utilizarse únicamente para pruebas controladas y no para exponer documentación corporativa sensible.

### 5.12.6. Resumen de tecnologías y criterios de selección

| Tecnología o producto                         | Papel en el sistema                                           | Criterio principal de selección                                                                     |
| --------------------------------------------- | ------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| Python                                        | Implementación de todas las fases del pipeline.               | Ecosistema amplio para procesamiento documental, IA y recuperación de información.                  |
| PyMuPDF (`fitz`)                              | Lectura, análisis y renderizado de páginas PDF.               | Permite procesamiento página a página y tratamiento de contenido visual.                            |
| OpenAI API                                    | Extracción, limpieza y generación de embeddings.              | Capacidad para procesar contenido complejo y generar representaciones semánticas de calidad.        |
| Pydantic y Tenacity                           | Validación estructural y reintentos ante fallos transitorios. | Permiten detectar estructuras inválidas y reintentar determinados fallos temporales.               |
| `rank-bm25`                                   | Recuperación léxica mediante BM25.                            | Adecuado para terminología exacta, códigos y referencias documentales.                              |
| `text-embedding-3-large`                      | Generación de vectores para chunks y consultas.               | Configuración utilizada; no comparada sistemáticamente con otros modelos.                           |
| ChromaDB                                      | Persistencia y búsqueda vectorial local.                      | Reduce la infraestructura necesaria y conserva metadatos junto con los vectores.                    |
| FlagEmbedding y `BAAI/bge-reranker-v2-m3`     | Reordenación local de candidatos.                             | Equilibrio entre relevancia, soporte multilingüe y control local de ejecución.                      |
| Ollama                                        | Generación local de respuestas.                               | Permite utilizar modelos configurables sin enviar el contexto de generación a un proveedor externo. |
| HTML, CSS, JavaScript y `ThreadingHTTPServer` | Interfaz web local y endpoint de consulta.                    | Solución ligera y suficiente para demostración y uso local.                                         |
| ngrok                                         | Exposición HTTPS temporal de la interfaz.                     | Facilita pruebas desde otros dispositivos sin desplegar infraestructura propia.                     |
| `unittest`                                    | Pruebas de módulos y contratos de datos.                      | Permite detectar regresiones sin depender siempre de servicios externos.                            |

## 5.13. Especificación y análisis de requisitos

### 5.13.1. Contexto y criterios de análisis

El proyecto tiene como objetivo facilitar la consulta de documentación corporativa en formato PDF mediante preguntas formuladas en lenguaje natural. Para ello, el sistema debe localizar información relevante dentro del corpus documental, construir un contexto suficiente a partir de los fragmentos recuperados y generar respuestas fundamentadas en las evidencias disponibles.

Los requisitos se definieron a partir de las necesidades propias de un sistema RAG documental: procesar documentos PDF, extraer y estructurar su contenido, generar fragmentos reutilizables, recuperar información mediante mecanismos léxicos y semánticos, y presentar respuestas trazables. Estos requisitos se trasladan a los distintos componentes de la arquitectura desarrollada, desde el procesamiento inicial del corpus hasta la recuperación híbrida y la generación de la respuesta final.

Se distinguen requisitos funcionales, que describen las capacidades ofrecidas por el sistema, y requisitos no funcionales, relacionados con cualidades como modularidad, trazabilidad, configurabilidad, reproducibilidad, seguridad documental, usabilidad y rendimiento. Asimismo, se delimitan las restricciones técnicas y los elementos que quedan fuera del alcance de la solución desarrollada.

### 5.13.2. Requisitos funcionales

| ID    | Requisito                                          | Descripción                                                                                                                                                            | Prioridad | Aplicación en el sistema                                                                                                                                                                                                            |
| ----- | -------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| RF-01 | Procesamiento de documentos PDF                    | El sistema debe permitir procesar documentos PDF individuales o lotes de documentos para incorporarlos al corpus.                                                      | Alta      | El flujo permite ejecutar el procesamiento sobre documentos individuales o sobre conjuntos de archivos. Para cada documento se genera una salida independiente y se emplean huellas de contenido para controlar el reprocesamiento. |
| RF-02 | Extracción y conservación del contenido documental | El sistema debe extraer el contenido de los documentos y conservar una representación inicial que permita revisar el resultado del procesamiento.                      | Alta      | El proceso genera una versión inicial del contenido extraído antes de las fases posteriores de limpieza, estructuración y segmentación.                                                                                             |
| RF-03 | Limpieza y estructuración documental               | El contenido extraído debe transformarse en una representación estructurada y adecuada para su uso posterior en recuperación.                                          | Alta      | El sistema genera documentos Markdown limpios y organizados mediante secciones, preparados para la fase de chunking.                                                                                                                |
| RF-04 | Generación de metadatos y trazabilidad             | El sistema debe conservar información sobre la procedencia, identificador, páginas, estado de procesamiento y nivel de seguridad de cada documento y fragmento.        | Alta      | Los artefactos generados y los chunks incorporan identificadores y metadatos que permiten mantener la relación con el documento de origen y su procesamiento.                                                                       |
| RF-05 | Segmentación en fragmentos recuperables            | El sistema debe dividir los documentos en unidades de información adecuadas para recuperación, manteniendo el contexto y los metadatos disponibles.                    | Alta      | Se generan chunks que incluyen contenido, ruta de sección, identificadores y campos específicos para las fases de indexación y recuperación.                                                                                        |
| RF-06 | Indexación léxica                                  | El sistema debe construir un índice que permita recuperar información mediante coincidencias terminológicas relevantes.                                                | Alta      | Se utiliza un índice BM25 persistente construido a partir de los chunks procesados.                                                                                                                                                 |
| RF-07 | Indexación y recuperación semántica                | El sistema debe representar los fragmentos mediante embeddings y recuperar resultados relacionados semánticamente con la consulta.                                     | Alta      | Los embeddings se almacenan en una base vectorial persistente y se emplean para recuperar fragmentos similares desde el punto de vista semántico.                                                                                   |
| RF-08 | Recuperación híbrida                               | El sistema debe combinar resultados procedentes de recuperación léxica y semántica para mejorar la cobertura de consultas formuladas de diferentes maneras.            | Alta      | Los rankings generados por BM25 y la base vectorial se fusionan mediante una estrategia de combinación de resultados.                                                                                                               |
| RF-09 | Reordenación de resultados                         | El sistema debe poder priorizar los fragmentos más relevantes entre los candidatos recuperados antes de construir el contexto final.                                   | Media     | El reranking puede activarse de forma configurable para reordenar los candidatos recuperados antes de seleccionar las evidencias finales.                                                                                           |
| RF-10 | Filtrado de resultados mediante metadatos          | El sistema debe permitir restringir la recuperación según atributos documentales, como el documento de origen, fichero, versión de procesamiento o nivel de seguridad. | Alta      | La recuperación incorpora filtros sobre los metadatos almacenados en los chunks, permitiendo acotar los resultados según los atributos documentales disponibles.                                                                    |
| RF-11 | Construcción de contexto evidencial                | El sistema debe transformar los resultados recuperados en un contexto estructurado que permita identificar los fragmentos utilizados durante la generación.            | Alta      | El contexto conserva referencias a los chunks, documentos, secciones y páginas cuando esta información está disponible.                                                                                                             |
| RF-12 | Generación orientada por evidencias                 | El sistema debe orientar la generación para que utilice el contexto recuperado y reconozca situaciones de evidencia insuficiente.                                      | Alta      | El generador recibe el contexto preparado por la recuperación y utiliza instrucciones para citar fuentes; el cumplimiento no se considera garantizado.                                                                              |
| RF-13 | Interfaz de operación y consulta                   | El sistema debe permitir ejecutar las principales fases mediante línea de comandos y realizar consultas desde una interfaz web local.                                  | Media     | La CLI permite procesar, indexar, buscar y evaluar. La interfaz web permite realizar consultas desde un navegador.                                                                                                                  |
| RF-14 | Regeneración de artefactos e índices               | El sistema debe permitir reconstruir los índices cuando cambien los documentos, los chunks, los campos indexables o la configuración de embeddings.                    | Alta      | La reconstrucción de los índices se realiza mediante comandos específicos destinados a regenerar las estructuras de recuperación cuando se modifica el corpus o la configuración relevante.                                         |
| RF-15 | Evaluación y diagnóstico de la recuperación        | El sistema debe proporcionar mecanismos para inspeccionar resultados y calcular métricas de recuperación cuando se disponga de preguntas y respuestas de referencia.   | Media     | El proyecto incorpora utilidades de diagnóstico y métricas como hit@k y MRR, que pueden aplicarse a conjuntos de consultas de evaluación definidos para el corpus.                                                                  |

### 5.13.3. Requisitos no funcionales

| ID     | Requisito                           | Descripción                                                                                                                                                          | Aplicación y alcance                                                                                                                                                                                                                                          |
| ------ | ----------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| RNF-01 | Modularidad                         | El sistema debe organizarse en módulos diferenciados para facilitar la evolución independiente de las fases de procesamiento, indexación, recuperación y generación. | La arquitectura se divide en módulos de extracción y limpieza, chunking, indexación, recuperación híbrida, generación e interfaz de consulta.                                                                                                                 |
| RNF-02 | Mantenibilidad                      | Los artefactos generados entre fases deben mantener contratos claros que permitan modificar componentes sin alterar innecesariamente el resto del sistema.           | Las fases intercambian artefactos persistidos con estructuras definidas, lo que permite intervenir sobre componentes concretos sin rediseñar el flujo completo.                                                                                               |
| RNF-03 | Trazabilidad                        | El usuario debe poder identificar las evidencias documentales que sustentan una respuesta generada.                                                                  | Los resultados recuperados conservan referencias a los documentos y fragmentos de origen, que se trasladan a las fuentes mostradas en la respuesta.                                                                                                           |
| RNF-04 | Configurabilidad                    | Los parámetros relevantes del sistema deben poder ajustarse sin modificar la lógica principal del código.                                                            | Se pueden configurar rutas, modelos, tamaño de contexto, parámetros de recuperación, reranking y otros valores mediante configuración externa y argumentos de ejecución.                                                                                      |
| RNF-05 | Reproducibilidad local              | El sistema debe poder ejecutarse de forma reproducible en un entorno local una vez instaladas las dependencias y configuradas las credenciales necesarias.           | El proyecto dispone de comandos, configuraciones y artefactos persistidos que permiten repetir el flujo de trabajo. Algunas fases requieren servicios, modelos o binarios externos previamente instalados y configurados.                                     |
| RNF-06 | Orientación al respaldo documental  | El generador debe recibir un contexto identificable e instrucciones para utilizarlo y reconocer la falta de evidencia.                                                | El prompt restringe la respuesta al contexto y solicita referencias. Esta medida no garantiza factualidad y requiere evaluación específica.                                                                                                                   |
| RNF-07 | Control de errores en PDF           | El procesamiento debe registrar incidencias y conservar artefactos que permitan revisar la extracción.                                                               | La solución incorpora extracción por páginas, estados, *warnings* y representaciones intermedias. La preservación completa del contenido no está garantizada para cualquier PDF.                                                                              |
| RNF-08 | Clasificación y filtrado documental         | El sistema debe conservar la clasificación asociada a los documentos y permitir utilizarla como criterio técnico de filtrado durante la recuperación.                   | El nivel de seguridad se almacena como metadato documental y puede emplearse para restringir los resultados recuperados. La autenticación de usuarios, la autorización basada en roles y la auditoría de accesos no forman parte del alcance de esta versión. |
| RNF-09 | Interacción básica                  | La interfaz debe permitir formular preguntas y revisar la respuesta y sus fuentes sin operar directamente los índices.                                               | La interfaz web ofrece esos elementos, pero no se ha realizado una evaluación formal de usabilidad con usuarios finales.                                                                                                                                      |
| RNF-10 | Separación offline/online           | Las tareas de preparación e indexación deben ejecutarse antes de la consulta para evitar repetirlas en cada pregunta.                                                 | El procesamiento documental y los índices se persisten.                                                                                                                         |
| RNF-11 | Extensibilidad                      | La arquitectura debe facilitar futuras sustituciones de modelos, recuperadores, fuentes documentales o mecanismos de generación.                                     | La separación entre módulos permite sustituir o ampliar componentes como el modelo de embeddings, el reranker, el generador o los mecanismos de recuperación.                                                                                                 |

La verificación de los requisitos se realiza con evidencias distintas según su naturaleza:

| Grupo de requisitos | Evidencia disponible | Alcance de la evidencia |
| --- | --- | --- |
| Procesamiento, metadatos y chunking | Pruebas automatizadas y artefactos persistentes | Casos controlados y 109 salidas documentales. |
| Indexación y recuperación | Pruebas de BM25, embeddings, RRF, filtros y reranking | Corrección funcional; no calidad global. |
| Generación e interfaz | Pruebas de contexto, fuentes y endpoint web | Funcionamiento local; no factualidad ni usabilidad formal. |
| Reproducibilidad | Comandos, configuración y estadísticas de índices | Requiere servicios y modelos externos; falta dataset de evaluación. |

## 5.14. Diseño del software

El software se ha diseñado como un sistema RAG documental modular, organizado en fases encadenadas que transforman documentos PDF en respuestas fundamentadas en evidencias recuperadas. El diseño diferencia las tareas de preparación del corpus, ejecutadas previamente, de las operaciones de consulta realizadas en tiempo de interacción.

Este apartado describe la estructura interna del sistema, los principales módulos que lo componen, los artefactos que intercambian información entre fases y los flujos dinámicos de indexación y consulta.

### 5.14.1. Criterios de diseño

El diseño se apoya en una arquitectura modular por responsabilidades. Cada fase del pipeline se encarga de una tarea concreta: extracción y limpieza documental, fragmentación, indexación léxica, indexación vectorial, recuperación híbrida, generación de respuestas e interacción con el usuario.

Esta organización permite que los componentes se comuniquen mediante artefactos persistentes y estructuras de datos definidas. De este modo, las fases de procesamiento documental generan salidas reutilizables por el chunking, la indexación y la recuperación, mientras que la generación final trabaja únicamente con los fragmentos recuperados.

Otro criterio central es la separación entre procesamiento *offline* y consulta *online*. Las operaciones asociadas al análisis completo del corpus, como la extracción, limpieza, creación de chunks e indexación, se realizan previamente. Durante la consulta, el sistema reutiliza los índices construidos para recuperar información relevante, preparar el contexto y generar una respuesta.

La trazabilidad también se incorpora como una propiedad transversal. Los documentos, fragmentos y resultados conservan identificadores y metadatos que permiten relacionar cada respuesta con las fuentes documentales utilizadas. Entre estos elementos se incluyen el identificador del documento, el fichero de origen, el identificador del chunk, la sección, las páginas disponibles y el nivel de seguridad asociado.

Finalmente, el diseño favorece la configurabilidad. Los parámetros relacionados con rutas, modelos, recuperación, número de resultados, reranking, contexto de generación e interfaz se gestionan mediante configuración externa y argumentos de línea de comandos.

### 5.14.2. Diseño estático: organización del sistema

La estructura estática se organiza en subsistemas especializados que colaboran mediante contratos de entrada y salida. La siguiente tabla resume los principales módulos del sistema.

| Subsistema | Responsabilidad principal |
| --- | --- |
| Configuración | Centraliza rutas, parámetros de ejecución, modelos, credenciales y valores de configuración del pipeline. |
| Procesamiento documental | Convierte documentos PDF en representaciones Markdown estructuradas y genera metadatos asociados. |
| Registro y metadatos | Mantiene la identidad de cada documento, su hash, estado de procesamiento, páginas, calidad y nivel de seguridad. |
| Chunking | Divide los documentos limpios en fragmentos trazables preparados para indexación y recuperación. |
| Indexación léxica | Construye un índice BM25 sobre representaciones textuales adaptadas a coincidencias terminológicas. |
| Indexación vectorial | Genera embeddings de los chunks y los almacena en una colección vectorial persistente mediante Chroma. |
| Recuperación híbrida | Coordina la recuperación BM25 y vectorial, aplica filtros, fusiona rankings y ejecuta reranking cuando está habilitado. |
| Generación | Construye un contexto evidencial a partir de los resultados recuperados y genera respuestas mediante Ollama. |
| Interfaz de operación | Proporciona comandos para ejecutar las fases del sistema y una interfaz web local para realizar consultas. |
| Diagnóstico y pruebas | Incluye mecanismos de validación, estadísticas, comparación de resultados y pruebas automatizadas. |

La organización de paquetes refleja esta separación de responsabilidades. Los módulos de extracción y limpieza gestionan la transformación inicial de los documentos; el módulo de chunking prepara las unidades recuperables; los componentes de indexación generan estructuras persistentes para búsqueda; el recuperador híbrido coordina los métodos de recuperación; y el módulo de generación transforma los resultados recuperados en una respuesta final.

La interfaz web y la línea de comandos actúan como capas de interacción con el usuario. Ambas reutilizan la misma lógica de recuperación y generación, evitando duplicar el comportamiento principal del sistema.

### 5.14.3. Artefactos e interfaces entre fases

El pipeline utiliza artefactos persistentes para comunicar las diferentes etapas. Esta decisión permite conservar los resultados intermedios, facilitar la trazabilidad y reutilizar las salidas en fases posteriores.

| Artefacto | Finalidad |
| --- | --- |
| `document_raw.md` | Conserva una representación inicial del contenido extraído del PDF, organizada por páginas. |
| `document_limpio.md` | Contiene la versión estructurada y normalizada del documento utilizada por el proceso de chunking. |
| `document_metadata.json` | Almacena identificadores, hash, fichero de origen, páginas, estado de procesamiento, información de calidad y nivel de seguridad. |
| `chunks.json` | Contiene los fragmentos generados a partir del documento limpio, junto con sus metadatos y campos preparados para indexación. |
| Índice BM25 | Persiste la estructura de recuperación léxica, los chunks indexados y la configuración empleada. |
| Colección Chroma | Almacena los embeddings y metadatos necesarios para la recuperación semántica. |

El contrato más relevante del sistema es `chunks.json`, ya que conecta la preparación documental con los mecanismos de recuperación. Cada fragmento conserva información como `chunk_id`, `document_id`, fichero de origen, secciones, páginas, contenido, nivel de seguridad y estadísticas de tamaño.

Además, el diseño define tres representaciones textuales para cada chunk:

- `content`: contenido principal del fragmento, utilizado para mostrar evidencias y construir el contexto de generación.
- `content_for_bm25`: representación enriquecida para recuperación léxica.
- `content_for_embedding`: representación contextualizada para la generación de embeddings.

Esta separación permite adaptar el mismo fragmento a las necesidades de cada recuperador sin modificar la unidad documental original.

Los resultados de BM25 y de la recuperación vectorial se transforman a una estructura común que incluye identificador del chunk, contenido, puntuación, rango, recuperador de origen y metadatos. A partir de esa estructura compartida, el sistema puede combinar resultados, aplicar reranking y generar fuentes numeradas para la respuesta final.

### 5.14.4. Diseño dinámico: flujo de preparación e indexación

El flujo de preparación comienza con la incorporación de uno o varios documentos PDF. El sistema calcula una huella criptográfica del fichero y utiliza un registro documental para identificar los documentos ya procesados.

A continuación, el contenido se extrae página a página y se conserva en una representación inicial. Posteriormente, el texto se limpia y estructura en formato Markdown, preservando títulos, secciones, listas, tablas y otros elementos relevantes para la recuperación posterior.

Una vez generado el documento limpio, el proceso de chunking analiza su estructura Markdown y crea fragmentos coherentes. Durante esta etapa se conservan las secciones, las páginas disponibles, los identificadores documentales y los campos textuales destinados a BM25 y embeddings.

Los chunks resultantes alimentan dos procesos de indexación complementarios:

1. **Indexación léxica:** tokeniza el contenido preparado para BM25 y construye un índice persistente orientado a coincidencias terminológicas.
2. **Indexación vectorial:** genera embeddings de los fragmentos y los almacena en una colección Chroma junto con sus metadatos.

La separación de ambos índices permite combinar búsquedas basadas en términos concretos con búsquedas basadas en similitud semántica.

```{mermaid}
flowchart TD
    A["PDF"] --> B["Extracción por páginas"]
    B --> C["document_raw.md"]
    C --> D["Limpieza y estructuración"]
    D --> E["document_limpio.md"]
    D --> M["document_metadata.json"]
    E --> F["Chunking"]
    M --> F
    F --> G["chunks.json"]
    G --> H["Índice BM25"]
    G --> I["Embeddings y colección Chroma"]
```

**Figura 6.** Flujo de preparación documental e indexación. Elaboración propia.

### 5.14.5. Diseño dinámico: flujo de consulta y generación

El flujo de consulta se inicia cuando el usuario formula una pregunta desde la línea de comandos o desde la interfaz web. Ambas vías de interacción reutilizan la misma lógica de recuperación y generación, por lo que el comportamiento principal del sistema se mantiene independiente de la capa desde la que se realiza la consulta.

En primer lugar, la consulta se prepara junto con los parámetros de ejecución seleccionados, como el número de resultados de cada recuperador, los filtros por metadatos, el número de candidatos destinados al reranking o el tamaño máximo del contexto. Cuando se indican filtros, estos se aplican sobre los metadatos asociados a los chunks para restringir la búsqueda según atributos como el documento de origen, el fichero, la versión de procesamiento o el nivel de seguridad.

A continuación, la pregunta se procesa secuencialmente mediante los dos mecanismos de recuperación disponibles. Aunque ambas búsquedas son independientes desde el punto de vista conceptual, su paralelización queda como posible optimización:

1. **Recuperación léxica:** el índice BM25 identifica fragmentos relevantes a partir de coincidencias terminológicas entre la consulta y la representación `content_for_bm25` de los chunks.
2. **Recuperación semántica:** la consulta se transforma en un embedding compatible con la colección vectorial y se recuperan los fragmentos más próximos mediante similitud semántica.

Los resultados de ambos recuperadores se normalizan a una estructura común que conserva el identificador del chunk, el contenido, la puntuación, la posición en el ranking, el recuperador de origen y los metadatos documentales. Posteriormente, los rankings se fusionan mediante *Reciprocal Rank Fusion* (RRF), una estrategia que combina las posiciones obtenidas por cada fragmento en los recuperadores léxico y vectorial.

Cuando el reranking está habilitado, los candidatos resultantes de la fusión se reordenan mediante un modelo específico que evalúa la relevancia conjunta de cada par formado por la consulta y el fragmento recuperado. Este paso permite priorizar las evidencias más adecuadas antes de construir el contexto que recibirá el modelo generativo.

Finalmente, el sistema selecciona los fragmentos mejor posicionados y construye un contexto evidencial estructurado. Cada evidencia conserva referencias al documento, sección, páginas disponibles e identificador del chunk, lo que permite asociar la respuesta final con sus fuentes documentales. Este contexto, junto con la pregunta original e instrucciones de generación, se envía al modelo accesible mediante Ollama.

El modelo genera una respuesta en lenguaje natural apoyada en las evidencias recuperadas. Las instrucciones de generación orientan la respuesta para utilizar el contexto proporcionado, reconocer situaciones de evidencia insuficiente y citar las fuentes correspondientes mediante referencias numeradas.

```{mermaid}
sequenceDiagram
    actor U as Usuario
    participant I as CLI / interfaz web
    participant R as HybridRetriever
    participant B as BM25
    participant C as Chroma
    participant X as Reranker
    participant O as Ollama
    U->>I: Formula una pregunta
    I->>R: Consulta y filtros
    R->>B: Búsqueda léxica
    B-->>R: Ranking BM25
    R->>C: Embedding y búsqueda vectorial
    C-->>R: Ranking semántico
    R->>R: Normalización, RRF y filtros
    opt Reranking habilitado
        R->>X: Consulta y candidatos
        X-->>R: Candidatos reordenados
    end
    R-->>I: Evidencias seleccionadas
    I->>O: Pregunta y contexto numerado
    O-->>I: Respuesta generada
    I-->>U: Respuesta, fuentes y fragmentos
```

**Figura 7.** Secuencia de consulta y generación. Elaboración propia.

## 5.15. Gestión de datos e información

La gestión de datos e información se estructura como un ciclo documental persistente que transforma cada documento PDF en representaciones textuales, estructuradas e indexadas para su consulta posterior. El proceso conserva la relación entre el documento original, los artefactos derivados, los fragmentos recuperables y las evidencias utilizadas durante la generación de respuestas.

Esta organización permite mantener la procedencia de la información a lo largo de todo el pipeline. De este modo, una respuesta puede vincularse con los fragmentos recuperados y, a través de sus metadatos, con el documento, sección y páginas de las que procede la evidencia.

### 5.15.1. Tipos de datos e información gestionados

El sistema gestiona cinco categorías de información:

| Categoría | Ejemplos | Función |
| --- | --- | --- |
| Fuentes primarias | Documentos PDF | Contenido original autorizado para el corpus. |
| Representaciones derivadas | Markdown bruto y limpio | Revisión y preparación para segmentación. |
| Metadatos | Identificadores, hash, estado, páginas y clasificación | Procedencia, control de cambios y filtrado técnico. |
| Estructuras de recuperación | Chunks, índice BM25 y colección Chroma | Localización de evidencias durante la consulta. |
| Configuración y estadísticas | Rutas, modelos, parámetros y recuentos | Reproducción y diagnóstico de la ejecución. |

La definición detallada de los artefactos y de las representaciones `content`, `content_for_bm25` y `content_for_embedding` se recoge en el apartado 5.14.3. Las credenciales y los valores dependientes del entorno se mantienen en `.env`, separado del código fuente y excluido del control de versiones.

### 5.15.2. Ciclo de vida documental

El ciclo de vida comienza con la incorporación de un documento PDF. Durante esta etapa, el sistema valida el archivo, calcula su hash SHA-256 y registra su identidad documental. Este identificador permite reconocer documentos ya procesados y asociar sus artefactos derivados con el fichero de origen.

El contenido extraído se almacena inicialmente en `document_raw.md`. A continuación, la fase de limpieza y estructuración genera `document_limpio.md`, una representación normalizada que facilita la segmentación posterior y reduce el ruido documental no relevante para la recuperación.

Posteriormente, el módulo de *chunking* transforma el documento limpio en fragmentos recuperables. Cada fragmento recibe un identificador propio y conserva su relación con el documento padre mediante campos como `document_id`, `source_file`, `file_hash_sha256` y `section_path`. Asimismo, incorpora información de tamaño, páginas disponibles, nivel de seguridad y los campos textuales necesarios para las fases de indexación.

A partir de `chunks.json`, el sistema genera dos estructuras de recuperación persistentes:

* Un índice BM25 para consultas basadas en coincidencias terminológicas.
* Una colección vectorial Chroma para consultas basadas en similitud semántica entre embeddings.

La separación entre los artefactos documentales y los índices permite regenerar las estructuras de búsqueda sin modificar el contenido procesado de los documentos.

```{mermaid}
flowchart LR
    A["PDF original"] --> B["Artefactos Markdown"]
    A --> M["Metadatos y hash"]
    B --> C["chunks.json"]
    M --> C
    C --> D["Índice BM25"]
    C --> E["Colección Chroma"]
    D --> F["Resultados recuperados"]
    E --> F
    F --> G["Fuentes de la respuesta"]
    G -. procedencia .-> C
    C -. procedencia .-> A
```

**Figura 8.** Ciclo de transformación y conservación de la procedencia documental. Elaboración propia.

### 5.15.3. Metadatos, trazabilidad y procedencia

La trazabilidad se fundamenta en el uso de identificadores y metadatos conservados desde el procesamiento inicial hasta la respuesta final. Cada documento dispone de un identificador propio, un hash SHA-256 y una carpeta de salida asociada que agrupa los resultados generados durante las distintas fases.

El archivo `document_metadata.json` reúne información como:

* `document_id`
* `source_file`
* `normalized_name`
* `original_path`
* `output_dir`
* `file_hash_sha256`
* `file_size_bytes`
* `page_count`
* nivel de seguridad
* estados e información de las fases de extracción, limpieza y chunking

Además, el registro global `outputs/document_registry.json` mantiene una referencia centralizada de los documentos procesados, sus hashes, identificadores y directorios de salida. Esta estructura facilita la identificación de ficheros ya incorporados al corpus y evita reprocesamientos innecesarios.

Cada chunk conserva metadatos de procedencia, entre ellos `chunk_id`, `document_id`, `source_file`, `file_hash_sha256`, `pages`, `section_path`, `security_level`, `token_count` y `char_count`. Gracias a estos campos, un resultado recuperado puede relacionarse con el fragmento concreto, el documento de origen y la sección documental correspondiente.

Durante la generación, los fragmentos seleccionados se presentan como fuentes identificadas mediante etiquetas como `[S1]`, `[S2]` o `[S3]`. Estas referencias permiten asociar la respuesta generada con las evidencias recuperadas y facilitan la revisión de la información utilizada.

### 5.15.4. Persistencia y organización de artefactos

La persistencia del sistema se distribuye principalmente entre los directorios `outputs/` y `data/indexes/`. Ambos pueden contener texto corporativo derivado y deben protegerse con medidas equivalentes a las aplicables a los documentos fuente. El prototipo no implementa políticas automáticas de retención, borrado seguro, copias de seguridad ni cifrado en reposo.

El directorio `outputs/` conserva los artefactos derivados de cada documento procesado:

```text
outputs/
├── document_registry.json
└── <documento>/
    ├── document_raw.md
    ├── document_limpio.md
    ├── document_metadata.json
    └── chunks.json
```

Por su parte, `data/indexes/` almacena las estructuras generadas durante la indexación:

```text
data/indexes/
├── bm25/
└── chroma/
```

El índice BM25 y la colección Chroma contienen información derivada de los chunks, junto con los identificadores y metadatos necesarios para recuperar la procedencia de cada resultado. Los índices no sustituyen los artefactos documentales originales, sino que actúan como estructuras especializadas para realizar búsquedas eficientes sobre el corpus procesado.

### 5.15.5. Coherencia y actualización de la información

La coherencia entre los documentos procesados, los chunks y los índices debe mantenerse durante la evolución del corpus. Cuando se modifica el contenido de un documento, la estrategia de chunking, los campos empleados para indexación o el modelo de embeddings, es necesario reconstruir los índices afectados.

El uso de hashes, identificadores persistentes y artefactos intermedios permite identificar el origen de los cambios y repetir únicamente las fases necesarias. No obstante, la actualización de los índices se realiza mediante procedimientos operativos explícitos, por lo que la responsabilidad de regenerarlos cuando se modifica el corpus o la configuración recae en el proceso de mantenimiento del sistema.

Esta organización proporciona una base reproducible para el tratamiento de la información documental, facilita la revisión de la procedencia de las respuestas y permite evolucionar los componentes de recuperación sin perder el vínculo con los documentos fuente.

## 5.16. Pruebas llevadas a cabo

La validación distingue entre la corrección del software, la calidad de la recuperación y la calidad de la respuesta generada. Estas dimensiones no son equivalentes: que un módulo se ejecute correctamente no implica que recupere la evidencia más adecuada, y disponer de evidencia relevante no garantiza que el modelo genere una respuesta completamente correcta.

### 5.16.1. Pruebas automáticas por componentes

El proyecto utiliza `unittest` [20]. En la revisión final se ejecutaron los siguientes comandos:

```bash
python -m compileall src tests
python -m unittest discover -s tests
```

La suite ejecutó 53 pruebas y finalizó correctamente en el entorno local revisado. Se emplean directorios temporales, clientes simulados y *mocks* para comprobar la lógica propia sin realizar llamadas reales a OpenAI, Ollama o modelos pesados en la mayoría de los casos.

| Área | Comprobaciones principales |
| --- | --- |
| Procesamiento documental | Hash, registro, artefactos de salida, páginas fallidas y limpieza por lotes. |
| Metadatos y *chunking* | Identificadores, procedencia, niveles de seguridad, estructura y tamaño de los fragmentos. |
| Indexación | Construcción, persistencia y carga de BM25; preparación e inserción de *embeddings*. |
| Recuperación | Fusión RRF, filtros, *reranking* y conservación de rangos y puntuaciones. |
| Generación | Contexto numerado, respuesta ante evidencia insuficiente y formato de fuentes. |
| Interfaz | Recursos web, endpoint de respuesta e integración opcional con ngrok. |

Estas pruebas validan contratos y casos controlados. No miden por sí solas la relevancia sobre todo el corpus, la factualidad de las respuestas, el rendimiento bajo carga ni la seguridad del sistema.

### 5.16.2. Pruebas cualitativas de recuperación

La inspección cualitativa se realizó mediante lotes de preguntas sobre los documentos procesados. Para cada consulta se revisaron el documento de origen, la sección, el contenido de los fragmentos recuperados y su posición en el ranking.

Los criterios aplicados fueron los siguientes:

- Relación efectiva entre la pregunta y los fragmentos recuperados.
- Contexto suficiente para responder sin introducir información no respaldada.
- Utilidad de BM25 para términos concretos, nombres o expresiones exactas.
- Utilidad de los *embeddings* para paráfrasis y relaciones semánticas.
- Efecto del *reranker* sobre el orden final de los candidatos.
- Conservación de la procedencia documental de cada fragmento.

Este análisis permite detectar fragmentos redundantes, coincidencias léxicas superficiales, respuestas distribuidas entre varias secciones y situaciones en las que un fragmento distinto del esperado también resulta válido. Asimismo, se comprobaron las respuestas generadas para verificar que utilizasen la evidencia recuperada y respondiesen de forma coherente a la consulta planteada.

### 5.16.3. Estado del conjunto de evaluación

El proyecto dispone del directorio `data/evaluation/`, que contiene conjuntos de preguntas utilizados para evaluar la recuperación de fragmentos y la adecuación de las respuestas generadas. Las utilidades de evaluación permiten asociar cada consulta con uno o varios `expected_chunk_ids` o con un fichero de origen esperado.

Estos conjuntos se emplearon durante el desarrollo para comprobar si el sistema recuperaba los fragmentos relevantes y si las respuestas generadas se correspondían con la evidencia disponible. También permitieron comparar distintas configuraciones de recuperación, incluyendo BM25, recuperación semántica, fusión mediante RRF y *reranking*.

Para reforzar la reproducibilidad de futuras evaluaciones cuantitativas, conviene conservar junto con cada ejecución la versión concreta del dataset utilizado, la configuración de los recuperadores y la salida detallada por consulta. De este modo, será posible comparar de forma consistente distintas versiones del sistema.

Los elementos que deben preservarse conjuntamente son los siguientes:

- Dataset de evaluación y criterios de anotación.
- Versión del corpus y de los archivos `chunks.json`.
- Configuración de BM25 y ChromaDB.
- Modelo de *embeddings* empleado.
- Parámetros de RRF, filtros y *reranking*.
- Resultados detallados por consulta y métricas agregadas.

### 5.16.4. Métricas disponibles

La infraestructura de evaluación calcula las métricas Hit@k y Mean Reciprocal Rank (MRR). Para un conjunto de $N$ consultas, Hit@k se define como:

$$
\operatorname{Hit@k} =
\frac{1}{N}
\sum_{i=1}^{N}
\mathbb{1}
\left[
\operatorname{rank}_i \leq k
\right]
$$

donde $\operatorname{rank}_i$ representa la posición del primer resultado anotado como relevante para la consulta $i$.

Por su parte, MRR se define como:

$$
\operatorname{MRR} =
\frac{1}{N}
\sum_{i=1}^{N}
\frac{1}{\operatorname{rank}_i}
$$

Cuando no aparece ningún resultado relevante dentro del corte evaluado, la consulta aporta un valor de cero a la métrica.

Hit@k mide la cobertura de resultados relevantes entre las primeras posiciones, mientras que MRR premia que la primera evidencia relevante aparezca cerca del inicio del ranking. Ambas métricas dependen de la calidad del *ground truth*: un fragmento alternativo puede ser útil para responder y, aun así, contabilizarse como fallo si no figura entre las evidencias anotadas. Además, algunas preguntas requieren combinar información procedente de varios fragmentos, mientras que estas métricas se centran principalmente en la primera coincidencia relevante.

### 5.16.5. Resultados verificables

Los resultados verificables de la versión entregada son los siguientes:

| Evidencia | Resultado |
| --- | ---: |
| Pruebas automatizadas ejecutadas | 53 |
| Directorios documentales con `chunks.json` | 109 |
| Fragmentos generados | 2.913 |
| Fragmentos registrados en las estadísticas del índice vectorial | 2.913 |
| Conjuntos de preguntas de evaluación | Disponibles en `data/evaluation/` |

Estas cifras acreditan la ejecución del pipeline, la consistencia básica entre las salidas documentales y las estadísticas de indexación, así como la disponibilidad de recursos para evaluar la recuperación y la generación. No constituyen, por sí solas, una medida global de precisión, cobertura o calidad del sistema RAG.

### 5.16.6. Alcance y limitaciones de la validación

La validación permite afirmar que los componentes principales y sus contratos funcionan en los casos automatizados incluidos, que el corpus local dispone de artefactos persistentes para la recuperación y que se realizaron pruebas con preguntas de evaluación para comprobar los fragmentos recuperados y las respuestas generadas.

No obstante, no permite garantizar la corrección de las respuestas ante cualquier consulta, el comportamiento ante cualquier tipo de PDF, la calidad sobre la totalidad del corpus, la resistencia frente a ataques ni la operación concurrente bajo carga.

Las principales líneas de mejora son consolidar los conjuntos de preguntas disponibles como datasets versionados, conservar resultados detallados por consulta, analizar errores por categoría y evaluar por separado la recuperación, la fidelidad de las citas, la suficiencia del contexto y la corrección de las respuestas generadas.

## 5.17. Manual de usuario

### 5.17.1. Finalidad y público objetivo

Este manual describe la instalación, configuración y utilización del sistema RAG desarrollado. La aplicación permite procesar documentos PDF, construir los índices necesarios para su consulta y generar respuestas fundamentadas en los fragmentos recuperados.

Está dirigido principalmente al personal técnico encargado de instalar, configurar, mantener y actualizar el sistema. Los usuarios finales pueden utilizar la interfaz web para realizar consultas sobre el corpus documental sin necesidad de conocer el funcionamiento interno del pipeline.

El flujo de uso habitual comprende la preparación del entorno, la configuración del archivo `.env`, la incorporación y procesamiento de documentos PDF, la construcción de índices y la consulta mediante interfaz web o línea de comandos.

### 5.17.2. Requisitos de ejecución

| Requisito                            | Finalidad                                                                               |
| ------------------------------------ | --------------------------------------------------------------------------------------- |
| Windows con PowerShell               | Entorno en el que se ha validado la ejecución de los comandos.                                                 |
| Python 3.11                          | Ejecución de los módulos de procesamiento, indexación y consulta.                       |
| Copia local del proyecto             | Acceso al código, la configuración y los directorios de datos.                          |
| Conexión a Internet                  | Uso de los servicios de OpenAI durante extracción, limpieza y generación de embeddings. |
| Clave de OpenAI                      | Autenticación de las operaciones que utilizan modelos externos.                         |
| Ollama instalado y modelo descargado | Generación local de respuestas.                                                         |
| Navegador web                        | Acceso a la interfaz de consulta.                                                       |
| Espacio de almacenamiento disponible | Conservación de documentos procesados, índices y modelos locales.                       |
| GPU compatible con CUDA, recomendada | Aceleración del reranking y de la generación local mediante Ollama.                     |
| ngrok instalado y autenticado        | Exposición temporal de la interfaz desde otros dispositivos, cuando sea necesario.      |

El sistema puede ejecutarse tanto en CPU como en una GPU compatible con CUDA. La ejecución en CPU permite utilizar todas las fases del proyecto, aunque la generación local de respuestas y el reranking pueden presentar tiempos de espera elevados. Para un uso interactivo con tiempos de respuesta adecuados, se recomienda disponer de una GPU compatible con CUDA, especialmente al utilizar modelos locales de mayor tamaño.

### 5.17.3. Instalación y configuración inicial

Los comandos deben ejecutarse desde la raíz del proyecto, donde se encuentran los directorios `src/`, `PDFs/`, `outputs/`, `data/` y el archivo `requirements.txt`.

En primer lugar, se crea y activa un entorno virtual con Python 3.11:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

A continuación, se instalan las dependencias del proyecto:

```powershell
python -m pip install -r requirements.txt
```

La configuración operativa se centraliza en el archivo `.env`, situado en la raíz del proyecto. Este archivo contiene credenciales, rutas, modelos y parámetros dependientes del entorno, por lo que debe mantenerse separado del código fuente y excluirse del control de versiones.

Las variables principales para la ejecución son las siguientes:

| Variable                 | Finalidad                                                |
| ------------------------ | -------------------------------------------------------- |
| `OPENAI_API_KEY`         | Clave utilizada por los servicios de OpenAI.             |
| `PDF_INPUT_DIR`          | Directorio que contiene los documentos PDF de entrada.   |
| `OUTPUT_DIR`             | Directorio donde se almacenan los documentos procesados. |
| `OLLAMA_MODEL`           | Modelo local empleado para generar respuestas.           |
| `OLLAMA_BASE_URL`        | Dirección del servicio local de Ollama.                  |
| `CHROMA_PERSIST_DIR`     | Directorio de persistencia de la base vectorial.         |
| `CHROMA_COLLECTION_NAME` | Nombre de la colección vectorial de Chroma.              |

También pueden configurarse parámetros avanzados, como `DEFAULT_SECURITY_LEVEL`, `DOCUMENT_REGISTRY_PATH`, `OPENAI_EMBEDDING_MODEL`, `OPENAI_EMBEDDING_DIMENSIONS`, `HYBRID_*`, `RERANK_*` y `NGROK_AUTHTOKEN`.

Una configuración habitual puede utilizar las siguientes rutas:

```text
PDF_INPUT_DIR=PDFs
OUTPUT_DIR=outputs
CHROMA_PERSIST_DIR=data/indexes/chroma
CHROMA_COLLECTION_NAME=rag_chunks_openai
```

Antes de continuar, se recomienda comprobar la versión de Python y la disponibilidad de los modelos locales:

```powershell
python --version
ollama list
```

El modelo definido mediante `OLLAMA_MODEL` debe aparecer en la salida de `ollama list`. En caso contrario, debe descargarse mediante:

```powershell
ollama pull <modelo_configurado>
```

Asimismo, el servicio de Ollama debe estar iniciado mediante el siguiente comando y accesible en la dirección indicada por `OLLAMA_BASE_URL`.

```powershell
ollama serve
```

### 5.17.4. Preparación e indexación del corpus documental

Los documentos PDF que formarán parte del corpus deben copiarse en el directorio configurado mediante `PDF_INPUT_DIR`, que por defecto corresponde a `PDFs/`.

```text
PDFs/
├── documento_1.pdf
├── documento_2.pdf
└── ...
```

El flujo recomendado para procesar el corpus completo es:

```powershell
python -m src.cli pipeline --build-embeddings
```

Este comando ejecuta de forma secuencial el procesamiento de los documentos, la extracción y limpieza del contenido, la generación de metadatos, el *chunking*, la construcción del índice BM25 y la creación de embeddings en Chroma.

Como resultado, se generan artefactos documentales en `outputs/` e índices persistentes en `data/indexes/`:

```text
outputs/<documento>/
├── document_raw.md
├── document_limpio.md
├── document_metadata.json
└── chunks.json

data/indexes/
├── bm25/
└── chroma/
```

Para tareas de mantenimiento o reconstrucción parcial, las fases pueden ejecutarse de forma independiente:

```powershell
python -m src.cli process-all

python -m src.cli chunk-all

python -m src.indexing.bm25.cli index-dir --input outputs --output data/indexes/bm25

python -m src.indexing.embeddings.cli index-dir --input outputs --persist-dir data/indexes/chroma --collection rag_chunks_openai
```

El estado de la colección vectorial puede consultarse mediante:

```powershell
python -m src.indexing.embeddings.cli stats --persist-dir data/indexes/chroma --collection rag_chunks_openai
```

Cuando se añaden o modifican documentos, cambian los chunks, los campos indexables o el modelo de embeddings, deben regenerarse las fases e índices afectados para mantener la coherencia del corpus.

### 5.17.5. Consulta mediante interfaz web y línea de comandos

La interfaz web constituye el método principal de consulta en las demostraciones locales. Antes de iniciarla, deben existir un índice BM25 y una colección Chroma generados durante la preparación del corpus.

```powershell
python -m src.retrieval.hybrid.cli chat-ui --host 127.0.0.1 --port 7860 --open-browser --bm25-index data/indexes/bm25 --chroma-persist-dir data/indexes/chroma --chroma-collection rag_chunks_openai
```

El parámetro `--open-browser` abre automáticamente la interfaz en el navegador predeterminado. La dirección local de acceso es:

```text
http://127.0.0.1:7860
```

El usuario debe formular una pregunta relacionada con el corpus y revisar la respuesta generada junto con las fuentes documentales mostradas. Las referencias `[S1]`, `[S2]` o `[S3]` permiten identificar los fragmentos recuperados que respaldan la respuesta.

Para detener la interfaz, debe pulsarse `Ctrl + C` en la ventana de PowerShell donde se ejecuta el servidor.

La línea de comandos permite recuperar evidencias o generar respuestas sin utilizar la interfaz web. Para realizar una búsqueda documental:

```powershell
python -m src.retrieval.hybrid.cli search --query "¿Qué condiciones establece el documento consultado?" --bm25-index data/indexes/bm25 --chroma-persist-dir data/indexes/chroma --chroma-collection rag_chunks_openai --final-top-k 5 --output-format pretty
```

Para generar una respuesta fundamentada en los resultados recuperados:

```powershell
python -m src.retrieval.hybrid.cli answer --query "¿Qué condiciones establece el documento consultado?" --bm25-index data/indexes/bm25 --chroma-persist-dir data/indexes/chroma --chroma-collection rag_chunks_openai --output-format markdown
```

La salida incluye la respuesta generada y las fuentes utilizadas como evidencia. Esta consulta constituye también una comprobación práctica de que los índices y el servicio de Ollama se encuentran disponibles.

### 5.17.6. Acceso remoto temporal mediante ngrok

La interfaz web puede exponerse temporalmente mediante ngrok para facilitar pruebas desde otros dispositivos conectados a Internet.

```powershell
python -m src.retrieval.hybrid.cli chat-ui --ngrok --host 127.0.0.1 --port 7860 --bm25-index data/indexes/bm25 --chroma-persist-dir data/indexes/chroma --chroma-collection rag_chunks_openai
```

El comando inicia la interfaz local y muestra una URL HTTPS pública. Al detener el proceso mediante `Ctrl + C`, también se finaliza el túnel temporal asociado.

Esta funcionalidad está destinada exclusivamente a pruebas controladas. La versión actual no incorpora autenticación de usuarios ni control de acceso, por lo que la URL pública no debe compartirse de forma indiscriminada ni utilizarse para exponer documentación corporativa sensible.

## 5.18. Principales aportaciones

La contribución del trabajo no reside en presentar BM25, embeddings, RRF o reranking como técnicas nuevas, sino en integrarlas en un prototipo documental reproducible y trazable.

### 5.18.1. Pipeline documental reproducible

El prototipo transforma PDF en representaciones Markdown, metadatos, fragmentos e índices persistentes. La separación entre fases permite inspeccionar resultados intermedios y repetir únicamente las etapas afectadas por un cambio.

### 5.18.2. Trazabilidad y procedencia

Los documentos y fragmentos conservan identificadores, hash, fichero de origen, ruta de sección, páginas cuando están disponibles y clasificación documental. Las fuentes mostradas con la respuesta mantienen el vínculo con los chunks recuperados. Esta trazabilidad facilita la revisión, aunque no sustituye una auditoría de accesos ni garantiza que cada afirmación generada esté correctamente respaldada.

### 5.18.3. Recuperación híbrida y reranking

La integración de BM25 y embeddings permite recuperar tanto coincidencias terminológicas como relaciones semánticas. RRF combina rankings heterogéneos y el reranker BGE reordena los candidatos ya recuperados. La memoria describe esta capacidad como una implementación funcional; su mejora cuantitativa global queda pendiente de una evaluación reproducible.

### 5.18.4. Generación con evidencias identificables

El sistema construye un contexto con fuentes numeradas e instruye a Ollama para responder a partir de ellas y reconocer la falta de evidencia. El resultado permite inspeccionar las fuentes utilizadas, pero no ofrece una garantía de factualidad ni ha sido validado sistemáticamente con usuarios finales.

### 5.18.5. Prototipo modular y operable en local

La CLI, la interfaz web y los artefactos persistentes permiten procesar documentos y realizar consultas en un entorno local. Las 53 pruebas automatizadas ejecutadas respaldan los contratos principales del software. El resultado no debe interpretarse como un servicio multiusuario ni como un despliegue productivo.

| Aportación | Resultado implementado | Alcance demostrado |
| --- | --- | --- |
| Pipeline documental | Extracción, limpieza, metadatos, fragmentación e indexación | Ejecución sobre 109 salidas documentales. |
| Procedencia | Identificadores, hashes, secciones y referencias | Relación entre documentos, chunks y fuentes mostradas. |
| Recuperación híbrida | BM25, Chroma, RRF y reranking BGE | Funcionamiento cubierto por pruebas; calidad global pendiente. |
| Generación | Contexto numerado y respuesta mediante Ollama | Demostración local; factualidad no evaluada sistemáticamente. |
| Modularidad | CLI, interfaz web y contratos persistentes | Operación local; sin garantías de concurrencia o escalabilidad. |

## 5.19. Conclusiones

### 5.19.1. Síntesis del trabajo realizado

Este TFG ha permitido diseñar e implementar un prototipo RAG híbrido para consultar documentación corporativa en PDF. El sistema transforma los documentos en representaciones estructuradas, genera índices léxicos y vectoriales, recupera evidencias mediante un enfoque híbrido y produce respuestas acompañadas de referencias a sus fuentes.

La versión revisada contiene 109 salidas documentales y 2.913 fragmentos indexados. Integra BM25, embeddings almacenados en Chroma, fusión RRF, reranking BGE configurable, generación mediante Ollama, CLI e interfaz web local. Estos resultados aportan evidencia de viabilidad técnica en el entorno y corpus utilizados, pero no permiten generalizar el rendimiento a otros corpus o escenarios.

### 5.19.2. Grado de cumplimiento de los objetivos

| Objetivo | Resultado | Limitación principal |
| --- | --- | --- |
| Preparación documental | Pipeline PDF y artefactos persistentes | Calidad variable según la estructura del PDF. |
| Trazabilidad | Identificadores, hashes, secciones y páginas disponibles | Las páginas pueden faltar tras el procesamiento. |
| Recuperación híbrida | BM25, Chroma, RRF y reranking | Sin evaluación cuantitativa reproducible global. |
| Generación con fuentes | Contexto numerado y referencias | Sin evaluación sistemática de factualidad. |
| Operación | CLI e interfaz web local | Sin concurrencia multiusuario validada. |
| Validación | 53 pruebas automatizadas | Sin pruebas de carga, seguridad o usuarios finales. |

Los objetivos de implementación se han alcanzado dentro del alcance local definido. Permanecen fuera de esta versión la autenticación, la autorización por identidad, la auditoría de accesos, el despliegue escalable y la evaluación global.

### 5.19.3. Conclusiones técnicas

La principal conclusión técnica es que la calidad de un sistema RAG depende de toda la cadena. La extracción condiciona el contenido disponible; el *chunking* define las unidades recuperables; la recuperación selecciona el contexto; y el modelo generativo interpreta ese contexto. Mejorar únicamente el generador no corrige errores originados en fases anteriores.

BM25 y los embeddings cubren necesidades complementarias. RRF permite combinar sus rankings sin equiparar directamente sus puntuaciones y el reranker vuelve a estimar la relevancia de los candidatos. No obstante, el reranker solo puede ordenar evidencia que haya sido recuperada previamente.

La persistencia de artefactos y metadatos facilita la depuración y la reconstrucción selectiva de fases. Como contrapartida, la coherencia entre documentos, chunks e índices depende actualmente de procedimientos operativos explícitos y no de una actualización transaccional automática.

### 5.19.4. Proyección

El prototipo dispone de pruebas de evaluación empleadas durante el desarrollo para comprobar la recuperación de fragmentos y la adecuación de las respuestas generadas. Como siguiente paso, será conveniente consolidar estos recursos mediante el versionado del dataset, la conservación de las configuraciones empleadas y el registro persistente de resultados por consulta, con el fin de facilitar comparaciones reproducibles entre versiones del sistema.

A partir de esta base, podrán abordarse la mejora del procesamiento de tablas, la evaluación más sistemática de la fidelidad de las respuestas y de sus citas, la seguridad, la concurrencia y el despliegue. El apartado 5.20 desarrolla y prioriza estas líneas.

### 5.19.5. Conclusiones personales

El desarrollo ha permitido comprender de forma práctica el ciclo completo de un sistema RAG y comprobar que la respuesta final depende en gran medida de la preparación del conocimiento y de la recuperación. También ha permitido profundizar en procesamiento documental, recuperación de información, embeddings, bases vectoriales, reranking, modelos locales y validación de sistemas de IA.

Un aprendizaje central ha sido diferenciar entre una demostración funcional y una evaluación rigurosa. Una respuesta plausible no basta: es necesario conservar las fuentes, comprobar los componentes, analizar los fallos y limitar las conclusiones a la evidencia disponible.

## 5.20. Vías de trabajo futuro

El sistema desarrollado constituye una base funcional y modular sobre la que pueden incorporarse nuevas mejoras orientadas a reforzar la calidad documental, la evaluación de la recuperación, la experiencia de uso y la capacidad de operación en escenarios compartidos. Las líneas de trabajo propuestas se han priorizado atendiendo a su impacto sobre la fiabilidad del sistema y a su relación con la arquitectura ya implementada. La identificación de varias de estas líneas se apoyó también en la revisión de soluciones RAG de carácter profesional, entre ellas RAGFlow [22].

### 5.20.1. Automatización y consolidación del conjunto de evaluación

Una de las principales líneas de evolución consiste en desarrollar un flujo automático para generar conjuntos de evaluación a partir de los documentos procesados. Este flujo podría proponer preguntas, respuestas de referencia y fragmentos potencialmente relevantes a partir del contenido estructurado de cada documento.

No obstante, la generación automática no debería considerarse por sí sola como una fuente definitiva de verdad de referencia. Las preguntas y evidencias propuestas tendrían que ser revisadas y validadas por una persona responsable antes de incorporarse al conjunto de evaluación final. De este modo, se podría diferenciar entre un conjunto preliminar de candidatos y un conjunto validado para medir el comportamiento del sistema.

La disponibilidad de un dataset versionado permitiría evaluar de forma sistemática la recuperación léxica, la recuperación vectorial, la fusión híbrida mediante RRF y el reranking. Asimismo, facilitaría el uso de métricas como Hit@k y MRR, además de la comparación entre distintas configuraciones de modelos, parámetros y estrategias de recuperación.

### 5.20.2. Mejora del procesamiento documental y del tratamiento de tablas

La calidad de la recuperación depende en gran medida de la calidad del contenido procesado antes de la indexación. Por este motivo, una futura ampliación consistiría en incorporar controles automáticos sobre los artefactos generados durante la extracción y limpieza documental.

Estos controles podrían detectar documentos vacíos, textos excesivamente breves, errores de codificación, estructuras de encabezados incoherentes, pérdida de contenido relevante o tablas incompletas. Su objetivo sería identificar documentos que requieran revisión antes de incorporarse a los índices del sistema.

Las tablas constituyen un caso especialmente relevante, ya que pueden contener información estructurada que pierde significado cuando se fragmenta incorrectamente. Como línea de mejora, sería conveniente evaluar comparativamente diferentes representaciones de tablas, tanto en formato textual como en formato Markdown, utilizando preguntas reales asociadas a su contenido.

Además, el proceso de *chunking* podría reforzarse para evitar dividir filas de una misma tabla. Cuando el tamaño lo permita, una tabla debería mantenerse como una unidad coherente dentro de un mismo fragmento. En el caso de tablas extensas, una alternativa consistiría en dividirlas por grupos de filas, repitiendo las cabeceras necesarias y conservando metadatos que permitan identificar la tabla, la sección y el rango de filas correspondiente.

Esta mejora permitiría preservar la relación entre cabeceras, columnas y valores, reduciendo el riesgo de recuperar fragmentos con datos aislados o difíciles de interpretar.

### 5.20.3. Experimentación con normalización para recuperación léxica

Otra línea de trabajo consiste en analizar el efecto de técnicas de normalización lingüística sobre la recuperación BM25. Entre estas técnicas podrían evaluarse la lematización, el *stemming* o la normalización de variantes ortográficas y morfológicas.

Estas transformaciones no deberían aplicarse directamente sobre el contenido limpio utilizado para generación o *embeddings*, ya que podrían reducir la legibilidad del texto o alterar nombres propios, códigos internos, siglas y terminología específica del ámbito empresarial. Su aplicación tendría mayor sentido en una representación específica para recuperación léxica, como el campo `content_for_bm25`.

La utilidad de estas técnicas debería comprobarse mediante el conjunto de evaluación, comparando el rendimiento de BM25 con y sin normalización. De esta forma, la decisión de incorporar *stemming* o lematización se basaría en resultados observables sobre el corpus real, evitando introducir transformaciones que no aporten mejoras significativas.

### 5.20.4. Sistema de retroalimentación y mejora continua

La interfaz podría incorporar un mecanismo mediante el cual los usuarios indiquen si una respuesta ha resultado incorrecta, incompleta o poco útil. Este *feedback* permitiría registrar casos reales de fallo y convertirlos en información útil para la mejora continua del sistema.

Cada incidencia podría almacenar la pregunta original, la respuesta generada, los fragmentos recuperados, las fuentes mostradas, la configuración utilizada y el motivo indicado por la persona usuaria. Tras una revisión por parte del equipo responsable, estos casos podrían clasificarse según su origen: fallo de extracción, *chunking*, recuperación, generación o presentación de la respuesta.

Los casos validados podrían incorporarse progresivamente al conjunto de evaluación y transformarse en pruebas de regresión. De este modo, una mejora futura del sistema podría verificarse frente a errores ya detectados, evitando que cambios en *prompts*, índices o parámetros degraden comportamientos previamente aceptados.

### 5.20.5. Optimización del rendimiento de la recuperación

La recuperación BM25 y la recuperación basada en *embeddings* son procesos independientes que pueden ejecutarse de forma concurrente. Por tanto, una mejora técnica razonable consistiría en paralelizar ambas búsquedas durante la fase de consulta.

Esta modificación podría reducir la latencia percibida por el usuario, especialmente cuando el corpus crezca o se utilicen servicios externos para generar *embeddings*. No obstante, su impacto debería medirse junto con el coste temporal del *reranking* y de la generación de la respuesta, ya que estas etapas también influyen en el tiempo total de consulta.

Otra posible mejora consiste en desacoplar el *reranker* mediante una interfaz de proveedor intercambiable. Esto permitiría comparar el modelo BGE ejecutado localmente con servicios de *reranking* ofrecidos mediante API. Una solución basada en API podría facilitar la operación en escenarios con mayor carga, mientras que el *reranking* local mantiene mayor control sobre la ejecución y la información procesada.

La selección entre ambas alternativas debería considerar calidad de resultados, latencia, coste, privacidad, disponibilidad y recursos de infraestructura.

### 5.20.6. Seguridad frente a instrucciones maliciosas

El uso de documentos como fuente de contexto hace recomendable incorporar medidas específicas frente a ataques de *prompt injection* directo o indirecto. Un documento recuperado podría contener instrucciones diseñadas para alterar el comportamiento del modelo generativo, por lo que el contenido documental debe tratarse como información de referencia y no como instrucciones de ejecución.

Como mejora futura, el sistema podría reforzar la separación entre instrucciones del sistema, consulta del usuario y contenido recuperado. Asimismo, podrían incorporarse delimitadores explícitos, filtros para detectar patrones sospechosos y validaciones que impidan que el modelo interprete fragmentos documentales como órdenes que deban seguirse.

Estas medidas deberían complementarse con pruebas de seguridad que incluyan documentos y consultas diseñados para comprobar la resistencia del sistema ante instrucciones conflictivas, intentos de extracción de información no autorizada o manipulación del contexto recuperado.

### 5.20.7. Evolución de la interfaz de usuario

La interfaz actual permite consultar el sistema y visualizar la respuesta generada junto con las fuentes recuperadas. Como evolución futura, podría rediseñarse mediante prototipado iterativo y pruebas de usabilidad para mejorar la claridad visual, la organización de la conversación y la accesibilidad de la información mostrada.

Más allá de la mejora estética, una ampliación especialmente útil consistiría en incorporar filtros de consulta. Estos filtros podrían permitir limitar la búsqueda por documento, sección, tipo documental, fecha, nivel de seguridad u otros metadatos disponibles en el corpus.

También sería conveniente mejorar la presentación de las fuentes, permitiendo desplegar los fragmentos recuperados, consultar sus metadatos y distinguir con claridad entre la respuesta generada y la evidencia documental que la respalda. Estas mejoras facilitarían una interacción más transparente y reforzarían la capacidad del usuario para comprobar la procedencia de la información.

### 5.20.8. Soporte para uso simultáneo por varios usuarios

La arquitectura actual está orientada a ejecución local y demostración funcional. Una evolución hacia un escenario de uso compartido requeriría adaptar el sistema para gestionar consultas simultáneas de varios usuarios.

Esta ampliación implicaría incorporar mecanismos de concurrencia, gestión de sesiones, control de recursos y límites de uso. También sería necesario integrar autenticación y autorización, de forma que cada usuario solo pudiera consultar la documentación para la que disponga de permisos.

En un contexto empresarial, esta evolución debería complementarse con auditoría de accesos, registro de actividad, protección de secretos, control de errores y una estrategia de despliegue estable. La interfaz actual y la integración temporal mediante ngrok podrían servir como punto de partida para definir los requisitos funcionales de esta futura arquitectura.

### 5.20.9. Priorización de las líneas futuras

La evolución propuesta puede organizarse en diferentes horizontes de desarrollo:

| Línea de trabajo | Objetivo principal | Prioridad propuesta |
| --- | --- | --- |
| Generación semiautomática y validación humana del dataset de evaluación | Medir la calidad de *retrieval* y generación de forma reproducible | Corto plazo |
| Evaluación del tratamiento de tablas y mejora de *chunking* | Preservar contexto estructurado y mejorar la recuperación de información tabular | Corto plazo |
| Controles de calidad documental | Detectar errores de extracción, limpieza y codificación antes de indexar | Corto plazo |
| Experimentación con normalización para BM25 | Determinar si la lematización o el *stemming* mejoran la recuperación léxica | Corto plazo |
| Sistema de *feedback* y pruebas de regresión | Convertir incidencias reales en conocimiento reutilizable para mejorar el sistema | Medio plazo |
| Paralelización de BM25 y *embeddings* | Reducir la latencia de consulta | Medio plazo |
| Comparación entre *reranking* local y mediante API | Seleccionar una solución adecuada según calidad, coste y operación | Medio plazo |
| Mitigación de *prompt injection* | Reforzar la seguridad del contexto documental y la generación | Medio plazo |
| Evolución visual de la interfaz y filtros por metadatos | Mejorar usabilidad, transparencia y control de las consultas | Medio plazo |
| Arquitectura multiusuario con autenticación y autorización | Adaptar el sistema a escenarios de acceso compartido | Largo plazo |

## 5.21. Referencias

Se adopta el estilo IEEE numerado. Las referencias académicas fundamentan los conceptos y técnicas empleados en el desarrollo del sistema, mientras que las fuentes web corresponden a la documentación oficial de las tecnologías, bibliotecas y servicios integrados en el proyecto. La evidencia relativa al comportamiento específico del sistema desarrollado procede del código fuente, las pruebas y los artefactos generados durante su ejecución.

[1] A. Vaswani *et al*., “Attention Is All You Need,” en *Advances in Neural Information Processing Systems 30*, 2017, pp. 5998–6008. [En línea]. Disponible en: https://proceedings.neurips.cc/paper/7181-attention-is-all-you-need. [Consulta: 2 jul. 2026].
[2] P. Lewis *et al*., “Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks,” en *Advances in Neural Information Processing Systems 33*, 2020, pp. 9459–9474. [En línea]. Disponible en: https://proceedings.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html. [Consulta: 2 jul. 2026].
[3] D. Candal Ventureira, “Tema 3.3: Generación aumentada por recuperación (RAG) y agentes,” materiales docentes de la asignatura Minería de Textos, 4.º curso del Grado en Inteligencia Artificial, Universidade de Vigo, 2026. [Material docente no publicado].

[4] S. Robertson y H. Zaragoza, “The Probabilistic Relevance Framework: BM25 and Beyond,” *Foundations and Trends in Information Retrieval*, vol. 3, n.º 4, pp. 333–389, 2009, doi: 10.1561/1500000019.

[5] M. Fernández Gavilanes, “Tema 4: Modelos de Recuperación de Información Clásicos — Parte 3 — Modelo probabilístico,” materiales docentes de la asignatura Recuperación de Información, 4.º curso del Grado en Inteligencia Artificial, Universidade de Vigo, 30 oct. 2025. [Material docente no publicado].

[6] V. Karpukhin *et al*., “Dense Passage Retrieval for Open-Domain Question Answering,” en *Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)*, 2020, pp. 6769–6781, doi: 10.18653/v1/2020.emnlp-main.550.

[7] G. V. Cormack, C. L. A. Clarke y S. Buettcher, “Reciprocal Rank Fusion Outperforms Condorcet and Individual Rank Learning Methods,” en *Proceedings of the 32nd International ACM SIGIR Conference on Research and Development in Information Retrieval*, 2009, pp. 758–759, doi: 10.1145/1571941.1572114.

[8] R. Nogueira y K. Cho, “Passage Re-ranking with BERT,” *arXiv preprint arXiv:1901.04085*, 2019. [En línea]. Disponible en: https://arxiv.org/abs/1901.04085.
[9] OpenAI, “Responses API Reference.” [En línea]. Disponible en: https://platform.openai.com/docs/api-reference/responses.
[10] OpenAI, “Images and Vision.” [En línea]. Disponible en: https://platform.openai.com/docs/guides/images-vision.
[11] OpenAI, “text-embedding-3-large Model.” [En línea]. Disponible en: https://platform.openai.com/docs/models/text-embedding-3-large.
[12] Chroma, “Manage Collections.” [En línea]. Disponible en: https://docs.trychroma.com/docs/collections/manage-collections.
[13] Beijing Academy of Artificial Intelligence, “BAAI/bge-reranker-v2-m3,” *Hugging Face*. [En línea]. Disponible en: https://huggingface.co/BAAI/bge-reranker-v2-m3.
[14] FlagOpen, “FlagEmbedding: Retrieval and Retrieval-Augmented LLMs,” GitHub. [En línea]. Disponible en: https://github.com/FlagOpen/FlagEmbedding.
[15] Ollama, “Generate a Chat Message.” [En línea]. Disponible en: https://docs.ollama.com/api/chat.
[16] Artifex Software, Inc., “PyMuPDF Documentation: Tutorial.” [En línea]. Disponible en: https://pymupdf.readthedocs.io/en/latest/tutorial.html.
[17] D. Brown, “rank_bm25: A Collection of BM25 Algorithms in Python,” GitHub. [En línea]. Disponible en: https://github.com/dorianbrown/rank_bm25.
[18] Python Software Foundation, “http.server — HTTP Servers,” *Python 3.11.15 Documentation*. [En línea]. Disponible en: https://docs.python.org/3.11/library/http.server.html. 
[19] ngrok, “Secure Tunnels.” [En línea]. Disponible en: https://ngrok.com/docs/guides/share-localhost/tunnels.
[20] Python Software Foundation, “unittest — Unit Testing Framework,” *Python 3.11.15 Documentation*. [En línea]. Disponible en: https://docs.python.org/3.11/library/unittest.html. 
[21] N. Gentile, “MEJORO mi EMPRESA usando IA: Chatbots, LLM, RAG y mucho más!,” YouTube, 2025. [En línea]. Disponible en: https://www.youtube.com/watch?v=W2YwMuxzyJY.
[22] InfiniFlow, “RAGFlow,” GitHub. [En línea]. Disponible en: https://github.com/infiniflow/ragflow.

## 5.22. Anexo: información de reproducibilidad

Este anexo resume la información necesaria para reproducir la ejecución local del prototipo a partir del repositorio, los documentos de entrada y la configuración externa. No incluye valores reales de credenciales ni contenido de `.env`, ya que esos datos deben mantenerse fuera de la memoria y del control de versiones.

**Entorno base**

| Elemento | Valor o condición reproducible |
| --- | --- |
| Sistema operativo validado | Windows con PowerShell |
| Versión de Python | Python 3.11 |
| Gestor de dependencias | `pip` con `requirements.txt` |
| Documentos de entrada | Carpeta `PDFs/` |
| Artefactos procesados | Carpeta `outputs/` |
| Índice BM25 | `data/indexes/bm25/` |
| Índice vectorial | `data/indexes/chroma/` |
| Colección Chroma por defecto | `rag_chunks_openai` |
| Pruebas automatizadas | Carpeta `tests/` mediante `unittest` |

**Dependencias principales**

Las dependencias Python se instalan desde `requirements.txt`. Entre ellas se incluyen `openai`, `python-dotenv`, `pydantic`, `pymupdf`, `pillow`, `tenacity`, `tqdm`, `rich`, `rank-bm25` y `chromadb`. La ejecución de extracción, limpieza, embeddings, reranking o generación puede requerir conectividad y credenciales externas según la configuración activa.

**Configuración externa**

La configuración se carga desde `.env`, tomando como plantilla `.env.example`. Para reproducir la ejecución se debe crear un archivo `.env` local y completar únicamente los valores necesarios para el entorno de prueba.

| Variable | Finalidad |
| --- | --- |
| `OPENAI_API_KEY` | Autenticación para extracción, limpieza, embeddings y generación configurada mediante OpenAI. |
| `OPENAI_EXTRACTION_MODEL` | Modelo empleado durante la extracción y limpieza documental. |
| `PDF_INPUT_DIR` | Directorio de documentos PDF de entrada. |
| `OUTPUT_DIR` | Directorio donde se generan los artefactos documentales. |
| `PAGE_RENDER_DPI` | Resolución usada al renderizar páginas cuando se procesa el PDF como imagen. |
| `EXTRACTION_MODE` | Modo de extracción, `page_image` o `page_pdf`. |
| `DEFAULT_SECURITY_LEVEL` | Nivel de seguridad asignado por defecto a los documentos. |
| `DOCUMENT_REGISTRY_PATH` | Ruta del registro documental basado en huellas de contenido. |
| `SKIP_DUPLICATES` | Control de omisión de documentos ya registrados. |
| `HYBRID_BM25_TOP_K` | Número de candidatos recuperados mediante BM25. |
| `HYBRID_EMBEDDING_TOP_K` | Número de candidatos recuperados mediante búsqueda vectorial. |
| `HYBRID_FINAL_TOP_K` | Número final de resultados tras la recuperación híbrida. |
| `HYBRID_RRF_K` | Parámetro de suavizado usado por RRF. |
| `RERANK_ENABLED` | Activa o desactiva el reranking. |
| `JINA_API_KEY` | Autenticación del reranker Jina cuando está habilitado. |
| `RERANKER_MODEL` | Modelo de reranking configurado. |
| `RERANK_CANDIDATE_K` | Número de candidatos enviados al reranker. |
| `RERANK_TOP_K` | Número de resultados conservados tras el reranking. |
| `OPENAI_GENERATION_MODEL` | Modelo usado para la generación de respuestas. |
| `OPENAI_MAX_OUTPUT_TOKENS` | Límite máximo de salida de la respuesta generada. |
| `RAG_MAX_CONTEXT_CHARS` | Tamaño máximo del contexto evidencial enviado al generador. |
| `RAG_MAX_CHUNK_CHARS` | Tamaño máximo por fragmento incluido en el contexto. |
| `CHROMA_PERSIST_DIR` | Directorio de persistencia de Chroma. |
| `CHROMA_COLLECTION_NAME` | Nombre de la colección vectorial. |
| `NGROK_AUTHTOKEN` | Token opcional para exposición temporal mediante ngrok. |

**Preparación del entorno**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
```

Después de crear `.env`, se deben completar las credenciales y parámetros locales necesarios. El archivo `.env` no debe incorporarse al repositorio ni compartirse junto con la memoria.

**Reconstrucción del corpus y de los índices**

El flujo completo puede reproducirse ejecutando las fases en orden. Si ya existen artefactos procesados y no se desea sobrescribirlos, no debe usarse `--force`.

```powershell
python -m src.cli process-all
python -m src.cli chunk-all
python -m src.indexing.bm25.cli index-dir --input outputs --output data/indexes/bm25
python -m src.indexing.embeddings.cli index-dir --input outputs --persist-dir data/indexes/chroma --collection rag_chunks_openai
```

Como alternativa, el comando `pipeline` permite encadenar procesamiento, segmentación e indexación desde la CLI principal:

```powershell
python -m src.cli pipeline --build-embeddings
```

Si cambia `document_limpio.md`, `document_metadata.json`, la lógica de *chunking* o el esquema de `chunks.json`, deben regenerarse los fragmentos y reconstruirse los índices BM25 y Chroma. Si cambia el modelo de embeddings, las dimensiones o el contenido indexado, debe reconstruirse la colección vectorial.

**Consultas reproducibles**

Una vez generados los índices, pueden ejecutarse consultas desde línea de comandos:

```powershell
python -m src.retrieval.hybrid.cli search --query "pregunta" --bm25-index data/indexes/bm25 --chroma-persist-dir data/indexes/chroma --chroma-collection rag_chunks_openai
```

Para obtener una respuesta generada con fuentes:

```powershell
python -m src.retrieval.hybrid.cli answer --query "pregunta" --bm25-index data/indexes/bm25 --chroma-persist-dir data/indexes/chroma --chroma-collection rag_chunks_openai
```

La interfaz web local se inicia con:

```powershell
python -m src.retrieval.hybrid.cli chat-ui --bm25-index data/indexes/bm25 --chroma-persist-dir data/indexes/chroma --chroma-collection rag_chunks_openai
```

Y, para una demostración remota temporal mediante ngrok:

```powershell
python -m src.retrieval.hybrid.cli chat-ui --ngrok --host 127.0.0.1 --port 7860 --bm25-index data/indexes/bm25 --chroma-persist-dir data/indexes/chroma --chroma-collection rag_chunks_openai
```

**Validación**

Las comprobaciones mínimas para verificar que el código compila y que los contratos principales siguen funcionando son:

```powershell
python -m compileall src tests
python -m unittest discover -s tests
```

Para cambios centrados en una fase concreta, puede ejecutarse además el módulo de pruebas correspondiente, por ejemplo:

```powershell
python -m unittest discover -s tests -p test_hybrid_retrieval.py
```

**Artefactos que deben conservarse para reproducir resultados**

| Artefacto | Motivo |
| --- | --- |
| `PDFs/` | Define el corpus documental de entrada. |
| `outputs/*/document_raw.md` | Permite auditar la extracción inicial. |
| `outputs/*/document_limpio.md` | Es la entrada principal del proceso de *chunking*. |
| `outputs/*/document_metadata.json` | Conserva identidad, hash, estado, páginas y nivel de seguridad. |
| `outputs/*/chunks.json` | Conecta el procesamiento documental con BM25, Chroma y generación. |
| `outputs/document_registry.json` | Registra documentos procesados y evita duplicados cuando está habilitado. |
| `data/indexes/bm25/` | Permite repetir recuperación léxica sin reconstruir el índice. |
| `data/indexes/chroma/` | Permite repetir recuperación vectorial con la colección persistente. |
| `data/evaluation/` | Contiene conjuntos de preguntas o referencias disponibles para diagnóstico. |

**Limitaciones de reproducibilidad**

La reproducción exacta puede verse afectada por cambios en servicios externos, modelos configurados, versiones de dependencias, contenido del corpus, parámetros de `.env` y disponibilidad de credenciales. Además, las respuestas generadas por modelos de lenguaje pueden variar entre ejecuciones aunque el contexto recuperado sea equivalente. Por ello, la reproducibilidad más fuerte del proyecto se encuentra en los artefactos persistidos, los índices reconstruibles y las pruebas automatizadas; la calidad factual de las respuestas requiere evaluación específica con un conjunto de referencia controlado.
