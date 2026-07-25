---
schema_version: "1.0"
document_id: project_index
document_type: structured_project_routing_index
language: es
last_updated: "2026-07-25"
source_of_truth:
  - current_markdown_project_summaries
  - verified_local_files
---

```yaml
policies:
  evidence_policy:
    only_claim_supported_information: true
    retrieve_evidence_for_professional_claims: true
    distinguish_facts_from_inferences: true
    acknowledge_missing_information: true
    do_not_fill_gaps_with_general_knowledge: true
  external_sources_policy:
    personal_facts: forbidden
    professional_claims: forbidden
    project_claims: forbidden
    general_technical_explanations: allowed_if_requested
  interview_policy:
    focus_on_real_experience: true
    state_experience_context: true
    cite_project_evidence: true
    avoid_exaggerated_language: true
    distinguish_used_integrated_implemented_designed: true

areas:
  - area_id: applied_artificial_intelligence
    name: Inteligencia artificial aplicada
  - area_id: natural_language_processing
    name: Procesamiento de lenguaje natural
  - area_id: information_retrieval
    name: Recuperación de información
  - area_id: computer_vision
    name: Visión artificial
  - area_id: deep_learning
    name: Deep learning
  - area_id: robotics_control
    name: Robótica y control
  - area_id: symbolic_ai
    name: IA simbólica y búsqueda
  - area_id: reactive_systems
    name: Sistemas reactivos y concurrencia
  - area_id: semantic_web
    name: Web semántica y grafos de conocimiento
  - area_id: software_engineering
    name: Ingeniería de software

technology_categories:
  - category_id: programming_language
    name: Lenguaje de programación
  - category_id: machine_learning_framework
    name: Framework de machine learning
  - category_id: computer_vision_library
    name: Librería de visión artificial
  - category_id: retrieval
    name: Recuperación de información
  - category_id: llm_api
    name: API o servicio LLM
  - category_id: data_processing
    name: Procesamiento de datos
  - category_id: semantic_web
    name: Web semántica
  - category_id: algorithm
    name: Algoritmo o técnica
  - category_id: systems
    name: Sistemas y concurrencia
  - category_id: tooling
    name: Herramientas y validación
  - category_id: web_framework
    name: Framework web y servidor ASGI
  - category_id: cloud_deployment
    name: Contenedores y despliegue cloud
  - category_id: product_analytics
    name: Analítica de producto

technologies:
  - technology_id: python
    canonical_name: Python
    aliases: [Python]
    category_id: programming_language
  - technology_id: java
    canonical_name: Java
    aliases: [Java]
    category_id: programming_language
  - technology_id: go
    canonical_name: Go
    aliases: [Golang, Go]
    category_id: programming_language
  - technology_id: cpp
    canonical_name: C++
    aliases: [C++, cpp]
    category_id: programming_language
  - technology_id: javascript
    canonical_name: JavaScript
    aliases: [JavaScript, JS, JavaScript vanilla]
    category_id: programming_language
  - technology_id: fastapi
    canonical_name: FastAPI
    aliases: [FastAPI, ASGI]
    category_id: web_framework
  - technology_id: uvicorn
    canonical_name: Uvicorn
    aliases: [Uvicorn]
    category_id: web_framework
  - technology_id: docker
    canonical_name: Docker
    aliases: [Docker, Dockerfile, contenedores]
    category_id: cloud_deployment
  - technology_id: digitalocean_app_platform
    canonical_name: DigitalOcean App Platform
    aliases: [DigitalOcean App Platform, DigitalOcean, App Platform]
    category_id: cloud_deployment
  - technology_id: posthog
    canonical_name: PostHog
    aliases: [PostHog, analítica de producto, product analytics]
    category_id: product_analytics
  - technology_id: openai_responses_api
    canonical_name: OpenAI Responses API
    aliases: [OpenAI Responses API, Responses API]
    category_id: llm_api
  - technology_id: openai_embeddings
    canonical_name: OpenAI embeddings
    aliases: [OpenAI embeddings, text-embedding-3-large]
    category_id: llm_api
  - technology_id: chromadb
    canonical_name: ChromaDB
    aliases: [Chroma, ChromaDB]
    category_id: retrieval
  - technology_id: bm25
    canonical_name: BM25
    aliases: [BM25, rank-bm25, rank_bm25]
    category_id: retrieval
  - technology_id: rrf
    canonical_name: Reciprocal Rank Fusion
    aliases: [RRF, Reciprocal Rank Fusion]
    category_id: retrieval
  - technology_id: jina_reranker
    canonical_name: Jina Reranker
    aliases: [Jina Reranker, Jina reranker]
    category_id: retrieval
  - technology_id: pydantic
    canonical_name: Pydantic
    aliases: [Pydantic]
    category_id: tooling
  - technology_id: pymupdf
    canonical_name: PyMuPDF
    aliases: [PyMuPDF, fitz]
    category_id: data_processing
  - technology_id: numpy
    canonical_name: NumPy
    aliases: [NumPy, numpy]
    category_id: data_processing
  - technology_id: pandas
    canonical_name: pandas
    aliases: [pandas]
    category_id: data_processing
  - technology_id: scikit_learn
    canonical_name: scikit-learn
    aliases: [scikit-learn, sklearn]
    category_id: data_processing
  - technology_id: pytorch
    canonical_name: PyTorch
    aliases: [PyTorch, torch]
    category_id: machine_learning_framework
  - technology_id: torchvision
    canonical_name: TorchVision
    aliases: [TorchVision, torchvision]
    category_id: machine_learning_framework
  - technology_id: opencv
    canonical_name: OpenCV
    aliases: [OpenCV, cv2]
    category_id: computer_vision_library
  - technology_id: scipy
    canonical_name: SciPy
    aliases: [SciPy]
    category_id: data_processing
  - technology_id: transformers
    canonical_name: Transformers
    aliases: [Transformers, Hugging Face Transformers]
    category_id: machine_learning_framework
  - technology_id: bert
    canonical_name: BERT
    aliases: [BERT]
    category_id: algorithm
  - technology_id: sbert
    canonical_name: SBERT
    aliases: [SBERT, sentence-transformers]
    category_id: algorithm
  - technology_id: word2vec
    canonical_name: Word2Vec
    aliases: [Word2Vec, Skip-gram]
    category_id: algorithm
  - technology_id: bpe
    canonical_name: Byte Pair Encoding
    aliases: [BPE, byte-level BPE]
    category_id: algorithm
  - technology_id: bertopic
    canonical_name: BERTopic
    aliases: [BERTopic]
    category_id: algorithm
  - technology_id: umap
    canonical_name: UMAP
    aliases: [UMAP]
    category_id: algorithm
  - technology_id: hdbscan
    canonical_name: HDBSCAN
    aliases: [HDBSCAN]
    category_id: algorithm
  - technology_id: networkx
    canonical_name: NetworkX
    aliases: [NetworkX]
    category_id: data_processing
  - technology_id: beautifulsoup
    canonical_name: BeautifulSoup
    aliases: [BeautifulSoup, bs4]
    category_id: data_processing
  - technology_id: tesseract
    canonical_name: Tesseract
    aliases: [Tesseract, OCR]
    category_id: data_processing
  - technology_id: presidio
    canonical_name: Presidio
    aliases: [Presidio]
    category_id: data_processing
  - technology_id: fasttext
    canonical_name: FastText
    aliases: [FastText]
    category_id: machine_learning_framework
  - technology_id: apache_jena
    canonical_name: Apache Jena
    aliases: [Apache Jena, Jena]
    category_id: semantic_web
  - technology_id: rdf
    canonical_name: RDF
    aliases: [RDF]
    category_id: semantic_web
  - technology_id: rdfs
    canonical_name: RDFS
    aliases: [RDFS]
    category_id: semantic_web
  - technology_id: sparql
    canonical_name: SPARQL
    aliases: [SPARQL]
    category_id: semantic_web
  - technology_id: fuseki
    canonical_name: Apache Fuseki
    aliases: [Fuseki, Apache Fuseki]
    category_id: semantic_web
  - technology_id: wikidata
    canonical_name: Wikidata
    aliases: [Wikidata]
    category_id: semantic_web
  - technology_id: dbpedia
    canonical_name: DBpedia
    aliases: [DBpedia]
    category_id: semantic_web
  - technology_id: jason
    canonical_name: Jason
    aliases: [Jason]
    category_id: systems
  - technology_id: agentspeak
    canonical_name: AgentSpeak
    aliases: [AgentSpeak, asl]
    category_id: systems
  - technology_id: lustre
    canonical_name: Lustre
    aliases: [Lustre]
    category_id: systems
  - technology_id: goroutines
    canonical_name: Goroutines
    aliases: [goroutines]
    category_id: systems
  - technology_id: channels
    canonical_name: Go channels
    aliases: [channels, Go channels]
    category_id: systems
  - technology_id: minimax
    canonical_name: MiniMax
    aliases: [MiniMax, minimax]
    category_id: algorithm
  - technology_id: alpha_beta
    canonical_name: Poda alfa-beta
    aliases: [alfa-beta, alpha-beta, poda alfa-beta]
    category_id: algorithm
  - technology_id: astar
    canonical_name: A*
    aliases: [A*, A star]
    category_id: algorithm
  - technology_id: ida_star
    canonical_name: IDA*
    aliases: [IDA*, IDA star]
    category_id: algorithm
  - technology_id: bfs
    canonical_name: BFS
    aliases: [BFS, búsqueda en anchura]
    category_id: algorithm

projects:
  - project_id: project_rag_empresarial_tfg
    canonical_name: RAG empresarial para consulta de documentación corporativa
    short_name: RAG empresarial TFG
    aliases:
      - RAG empresarial para consulta de documentación corporativa
      - RAG empresarial TFG
      - prototipo RAG híbrido
      - consulta inteligente de PDFs corporativos
      - recuperación híbrida BM25 Chroma OpenAI
      - TFG
      - Trabajo de fin de grado
    project_type: academic
    status: completed
    featured: true
    interview_priority: 1
    areas: [applied_artificial_intelligence, natural_language_processing, information_retrieval, software_engineering]
    tags: [rag, recuperación de información, openai, chromadb, bm25]
    primary_technology_ids: [python, openai_responses_api, openai_embeddings, bm25, chromadb, rrf, jina_reranker, pydantic, pymupdf]
    secondary_technology_ids: [scikit_learn]
    role:
      collaboration_type: individual
      title: designer_and_developer
      context: academic
    personal_contributions:
      - Diseño e implementación del prototipo RAG híbrido descrito en el TFG.
      - Preparación del pipeline de ingesta, chunking, indexación, recuperación, reranking, generación y validación.
      - Integración de OpenAI, ChromaDB, BM25, RRF, Jina Reranker, CLI, interfaz web local y pruebas.
    team_contributions: []
    provided_components:
      - OpenAI Responses API como servicio externo de generación y extracción.
      - OpenAI embeddings como servicio externo de vectorización.
      - Jina Reranker como servicio externo de reordenación.
      - ChromaDB, PyMuPDF, Pydantic y librerías Python utilizadas como dependencias.
    not_personally_implemented:
      - Modelos internos de OpenAI.
      - Modelo externo de Jina Reranker.
      - Algoritmos internos de ChromaDB.
    short_pitch: Sistema RAG híbrido para consultar documentación corporativa en PDF mediante lenguaje natural, con recuperación léxica y semántica, reranking y respuestas con fuentes. El proyecto demuestra la cadena completa desde ingesta documental hasta interfaz local y validación.
    objective: Diseñar, implementar y validar un prototipo RAG híbrido trazable para documentación corporativa.
    problem_solved: Reduce el esfuerzo de localizar respuestas en PDFs corporativos dispersos y limita la generación a evidencia recuperada.
    verifiable_results:
      - 109 documentos procesados según el summary.
      - 2913 chunks indexados en BM25 y Chroma según el summary.
      - 57 tests ejecutados correctamente según el summary.
      - Uso documentado de text-embedding-3-large con vectores de 3072 dimensiones.
    competency_ids: [skill_rag_hibrido, skill_openai_api, skill_ir_bm25_tfidf, skill_diseno_modular, skill_testing_validacion]
    summary_path: rag-empresarial-tfg_summary.md
    advanced_path: null
    repository: null
    demo: local_web_interface_and_ngrok_demo_described
    rag_enabled: true
    retrieval_metadata:
      project_id: project_rag_empresarial_tfg
      allowed_document_types: [summary]
    evidence_strength: strong_summary
    known_limitations:
      - Contexto académico de TFG, no uso productivo documentado.
      - La ruta advanced declarada en el summary no existe en esta carpeta.
      - Dependencia de APIs externas para generación, embeddings y reranking.

  - project_id: project_mineria_textos
    canonical_name: Minería de Textos
    short_name: Minería de Textos
    aliases: [Minería de Textos, NLP aplicado, recuperación híbrida y sistemas LLM, topic modeling y RAG]
    project_type: academic
    status: completed
    featured: true
    interview_priority: 3
    areas: [natural_language_processing, information_retrieval, applied_artificial_intelligence]
    tags: [procesamiento de lenguaje natural, embeddings, recuperación de información, llm, rag]
    primary_technology_ids: [python, beautifulsoup, pymupdf, tesseract, fasttext, word2vec, bert, sbert, chromadb, bm25, rrf, bertopic, umap, hdbscan, networkx, transformers, pytorch]
    secondary_technology_ids: [presidio]
    role: {collaboration_type: academic_practice, title: implementer_and_documenter, context: academic}
    personal_contributions:
      - Integración documentada de prácticas de ingesta, limpieza, OCR, deduplicación, embeddings, recuperación, topic modeling, resumen y agentes.
    team_contributions: []
    provided_components:
      - APIs de noticias y modelos/librerías preentrenadas usados como dependencias.
      - Gemma, BERT, SBERT, FastText y otros modelos no implementados desde cero.
    not_personally_implemented: [Modelos preentrenados de terceros, algoritmos internos de librerías externas]
    short_pitch: Conjunto amplio de prácticas de NLP y minería de textos que cubre ingesta, limpieza, embeddings, recuperación híbrida, topic modeling, resumen y sistemas LLM. Es una evidencia transversal de manejo de corpus y pipelines de texto.
    objective: Aplicar técnicas modernas de minería de textos y NLP sobre distintos tipos de corpus.
    problem_solved: Organiza el procesamiento de texto desde fuentes heterogéneas hasta recuperación, análisis temático y generación.
    verifiable_results:
      - 39 scripts de prácticas indicados en el summary.
      - Uso documentado de ChromaDB, BM25, RRF, BERTopic, UMAP, HDBSCAN y Transformers.
    competency_ids: [skill_text_mining_ingesta, skill_embeddings_nlp, skill_rag_hibrido, skill_topic_modeling, skill_resumen_extractivo]
    summary_path: mineria-de-textos_summary.md
    advanced_path: null
    repository: null
    demo: null
    rag_enabled: true
    retrieval_metadata: {project_id: project_mineria_textos, allowed_document_types: [summary]}
    evidence_strength: strong_summary
    known_limitations:
      - Contexto académico.
      - La ruta advanced declarada en el summary no existe en esta carpeta.

  - project_id: project_procesamiento_lenguaje_natural_bpe_skipgram
    canonical_name: Procesamiento de Lenguaje Natural con BPE y Skip-gram
    short_name: BPE y Skip-gram
    aliases: [PLN con BPE y Skip-gram, tokenización byte-level BPE y embeddings, Word2Vec desde cero con negative sampling, Procesamiento de Lenguaje Natural]
    project_type: academic
    status: completed
    featured: true
    interview_priority: 5
    areas: [natural_language_processing, deep_learning]
    tags: [procesamiento de lenguaje natural, python, numpy, bpe, skipgram, embeddings]
    primary_technology_ids: [python, numpy, bpe, word2vec]
    secondary_technology_ids: []
    role: {collaboration_type: academic_practice, title: implementer, context: academic}
    personal_contributions:
      - Implementación documentada de tokenizador byte-level BPE y entrenamiento Skip-gram con negative sampling.
    team_contributions: []
    provided_components: [NumPy como dependencia de cálculo numérico]
    not_personally_implemented: []
    short_pitch: Implementación formativa de tokenización subword y embeddings tipo Word2Vec. Permite explicar desde bytes UTF-8 y fusiones BPE hasta entrenamiento Skip-gram con negative sampling.
    objective: Comprender e implementar fundamentos de tokenización y embeddings.
    problem_solved: Convierte texto en representaciones tokenizadas y vectores reutilizables.
    verifiable_results:
      - Formato de embeddings documentado con cabecera 500 100.
      - Uso documentado de 5 negativos por par positivo.
    competency_ids: [skill_tokenizacion_bpe, skill_embeddings_nlp, skill_python]
    summary_path: procesamiento-lenguaje-natural-bpe-skipgram_summary.md
    advanced_path: null
    repository: null
    demo: null
    rag_enabled: true
    retrieval_metadata: {project_id: project_procesamiento_lenguaje_natural_bpe_skipgram, allowed_document_types: [summary]}
    evidence_strength: strong_summary
    known_limitations: [Contexto académico, La ruta advanced declarada en el summary no existe en esta carpeta]

  - project_id: project_recuperacion_informacion
    canonical_name: Recuperación de Información
    short_name: Recuperación de Información
    aliases: [Recuperación de Información, motor de búsqueda EFE, BM25 RM3 y modelos de lenguaje, Information Retrieval]
    project_type: academic
    status: completed
    featured: true
    interview_priority: 4
    areas: [information_retrieval, natural_language_processing]
    tags: [recuperación de información, python, bm25, tf-idf, procesamiento de lenguaje natural]
    primary_technology_ids: [python, pandas, scikit_learn, bm25]
    secondary_technology_ids: [bfs]
    role: {collaboration_type: academic_practice, title: implementer_and_analyst, context: academic}
    personal_contributions:
      - Desarrollo documentado de prácticas de ranking con TF-IDF, BM25, modelos probabilísticos, RM3 y modelos de lenguaje.
    team_contributions: []
    provided_components: [Corpora EFE y MEDLINE como datos de práctica, librerías pandas, scikit-learn, NLTK, Whoosh y rank_bm25]
    not_personally_implemented: [Motores internos de librerías externas]
    short_pitch: Proyecto académico centrado en motores de búsqueda y modelos de recuperación. Cubre TF-IDF, BM25, modelos probabilísticos, expansión de consultas y suavizado de modelos de lenguaje.
    objective: Comparar técnicas clásicas de recuperación documental.
    problem_solved: Permite indexar, representar y ordenar documentos frente a consultas textuales.
    verifiable_results:
      - Uso documentado de EFE, MEDLINE, TF-IDF, BM25, Whoosh BM25F, RM3 y Query Likelihood.
    competency_ids: [skill_ir_bm25_tfidf, skill_modelos_lenguaje_ir, skill_pandas_datos]
    summary_path: recuperacion-informacion_summary.md
    advanced_path: null
    repository: null
    demo: null
    rag_enabled: true
    retrieval_metadata: {project_id: project_recuperacion_informacion, allowed_document_types: [summary]}
    evidence_strength: strong_summary
    known_limitations: [Contexto académico, La ruta advanced declarada en el summary no existe en esta carpeta]

  - project_id: project_vision_artificial_fundamentos
    canonical_name: Fundamentos de Visión Artificial
    short_name: Visión artificial fundamentos
    aliases: [Fundamentos de Visión Artificial, visión artificial fundamentos, calibración de cámara y procesamiento de imagen, Computer Vision Labs]
    project_type: academic
    status: completed
    featured: true
    interview_priority: 6
    areas: [computer_vision]
    tags: [visión artificial, opencv, procesamiento de imagen]
    primary_technology_ids: [python, cpp, opencv, numpy, scipy, pytorch]
    secondary_technology_ids: []
    role: {collaboration_type: academic_practice, title: implementer_and_analyst, context: academic}
    personal_contributions:
      - Implementación y comparación de prácticas de calibración, homografías, distorsión, color, filtrado, bordes y morfología.
    team_contributions: []
    provided_components: [OpenCV, SciPy, scikit-image y PyTorch como librerías, paper de Zhang como referencia]
    not_personally_implemented: [Algoritmos internos optimizados de OpenCV y SciPy]
    short_pitch: Prácticas de base matemática y aplicada de visión artificial. Demuestra calibración de cámara, geometría de imagen, filtrado, bordes, morfología y comparación con librerías estándar.
    objective: Consolidar fundamentos de procesamiento de imagen y geometría visual.
    problem_solved: Transforma imágenes en parámetros, mapas, bordes y representaciones interpretables.
    verifiable_results:
      - Uso documentado de calibración Zhang, DLT, RANSAC, error de reproyección, FFT, Canny y morfología.
    competency_ids: [skill_opencv_imagen, skill_geometria_vision, skill_procesamiento_imagen]
    summary_path: vision-artificial-fundamentos_summary.md
    advanced_path: null
    repository: null
    demo: null
    rag_enabled: true
    retrieval_metadata: {project_id: project_vision_artificial_fundamentos, allowed_document_types: [summary]}
    evidence_strength: strong_summary
    known_limitations: [Contexto académico, La ruta advanced declarada en el summary no existe en esta carpeta]

  - project_id: project_vision_artificial_percepcion_deep_learning
    canonical_name: Percepción con deep learning para visión artificial
    short_name: Percepción visual con deep learning
    aliases: [Percepción con deep learning, visión artificial con PyTorch, clasificación segmentación y detección de objetos, ResNet U-Net Mini-SAM YOLO y FCOS]
    project_type: academic
    status: completed
    featured: true
    interview_priority: 7
    areas: [computer_vision, deep_learning]
    tags: [visión artificial, deep learning, pytorch, segmentación, detección de objetos]
    primary_technology_ids: [python, pytorch, torchvision]
    secondary_technology_ids: [opencv]
    role: {collaboration_type: academic_practice, title: implementer_and_experimenter, context: academic}
    personal_contributions:
      - Implementación y adaptación documentada de pipelines de clasificación, segmentación, detección y atención visual en PyTorch.
    team_contributions: []
    provided_components: [Backbones y datasets de TorchVision, modelos y métricas externas como COCO API]
    not_personally_implemented: [Arquitecturas originales de ResNet, U-Net, DeepLabV3+, YOLO, FCOS y Mini-SAM]
    short_pitch: Conjunto de prácticas de percepción visual con deep learning en PyTorch. Cubre clasificación, segmentación, detección, atención visual, pérdidas y evaluación.
    objective: Aplicar redes profundas a tareas visuales densas y discriminativas.
    problem_solved: Resuelve tareas visuales de clasificación, segmentación y detección mediante modelos entrenables.
    verifiable_results:
      - Uso documentado de ResNet, Vision Transformer, U-Net, FCN, DeepLabV3+, Mini-SAM, YOLO, FCOS, COCO API y TensorBoard.
    competency_ids: [skill_pytorch_vision, skill_clasificacion_visual, skill_segmentacion, skill_deteccion_objetos]
    summary_path: vision-artificial-percepcion-deep-learning_summary.md
    advanced_path: null
    repository: null
    demo: null
    rag_enabled: true
    retrieval_metadata: {project_id: project_vision_artificial_percepcion_deep_learning, allowed_document_types: [summary]}
    evidence_strength: strong_summary
    known_limitations: [Contexto académico, La ruta advanced declarada en el summary no existe en esta carpeta]

  - project_id: project_vision_artificial_video_temporalidad
    canonical_name: Visión artificial aplicada a vídeo y temporalidad
    short_name: Visión artificial en vídeo
    aliases: [Visión artificial en vídeo, seguimiento visual y reconocimiento de acciones, Tracking C3D Two-Stream STM y Deep Feature Flow, prácticas de visión artificial sobre vídeo y temporalidad]
    project_type: academic
    status: completed
    featured: true
    interview_priority: 8
    areas: [computer_vision, deep_learning]
    tags: [visión artificial, vídeo, tracking, deep learning, pytorch, opencv]
    primary_technology_ids: [python, opencv, numpy, pytorch, torchvision]
    secondary_technology_ids: []
    role: {collaboration_type: academic_practice, title: implementer_and_experimenter, context: academic}
    personal_contributions:
      - Implementación, adaptación y documentación de pipelines de tracking, reconocimiento de acciones y propagación temporal.
    team_contributions: []
    provided_components: [Pesos preentrenados y datasets como Sports-1M y UCF-101 cuando aparecen en el summary]
    not_personally_implemented: [Arquitecturas originales C3D, Two-Stream, Deep Feature Flow y STM]
    short_pitch: Proyecto sobre visión artificial temporal, desde tracking clásico hasta modelos profundos para acciones y memoria visual. Permite explicar movimiento, estado, flujo óptico y reutilización temporal de features.
    objective: Estudiar e implementar técnicas de visión sobre secuencias de vídeo.
    problem_solved: Extrae seguimiento, movimiento y señales temporales útiles desde vídeos.
    verifiable_results:
      - 20 scripts Python y 7 documentos Markdown indicados en el summary.
      - Logs documentados de Two-Stream sobre UCF-101 con 9537 vídeos de entrenamiento y 3783 de validación.
    competency_ids: [skill_video_tracking, skill_reconocimiento_acciones, skill_pytorch_vision]
    summary_path: vision-artificial-video-temporalidad_summary.md
    advanced_path: null
    repository: null
    demo: null
    rag_enabled: true
    retrieval_metadata: {project_id: project_vision_artificial_video_temporalidad, allowed_document_types: [summary]}
    evidence_strength: strong_summary
    known_limitations: [Contexto académico y experimental, La ruta advanced declarada en el summary no existe en esta carpeta]

  - project_id: project_vision_artificial_escena_3d
    canonical_name: Visión artificial para profundidad y escena 3D
    short_name: Visión artificial 3D
    aliases: [Visión artificial 3D, estimación de profundidad y reconstrucción 3D, SfM MVS PointNet NeRF y stereo depth]
    project_type: academic
    status: completed
    featured: false
    interview_priority: 20
    areas: [computer_vision, deep_learning]
    tags: [visión artificial, reconstrucción 3D, deep learning, pytorch, geometría multivista]
    primary_technology_ids: [python, numpy, opencv, pytorch, torchvision, scipy]
    secondary_technology_ids: []
    role: {collaboration_type: academic_practice, title: implementer_and_analyst, context: academic}
    personal_contributions:
      - Implementación y documentación de prácticas sobre profundidad, geometría multivista, reconstrucción y representaciones 3D.
    team_contributions: []
    provided_components: [Arquitecturas y modelos de referencia como DispNet, GC-Net, PSMNet, PointNet, PointPillars y NeRF]
    not_personally_implemented: [Arquitecturas originales de terceros]
    short_pitch: Prácticas de visión 3D que conectan profundidad estereoscópica, geometría multivista, nubes de puntos y renderizado neural. Refuerza la comprensión de cómo pasar de imágenes a estructura espacial.
    objective: Aplicar métodos clásicos y profundos para estimar profundidad y representar escenas 3D.
    problem_solved: Reconstrucción y representación de información geométrica a partir de imágenes.
    verifiable_results:
      - Uso documentado de SfM, MVS, DispNet, GC-Net, PSMNet, PointNet, PointPillars y NeRF.
    competency_ids: [skill_vision_3d, skill_geometria_vision, skill_pytorch_vision]
    summary_path: vision-artificial-escena-3d_summary.md
    advanced_path: null
    repository: null
    demo: null
    rag_enabled: true
    retrieval_metadata: {project_id: project_vision_artificial_escena_3d, allowed_document_types: [summary]}
    evidence_strength: strong_summary
    known_limitations: [Contexto académico, La ruta advanced declarada en el summary no existe en esta carpeta]

  - project_id: project_percepcion_para_accion
    canonical_name: Percepción para acción en visión artificial y aprendizaje de políticas visuales
    short_name: Percepción para acción
    aliases: [Percepción para acción, Visual policy learning, visión artificial aplicada a control y robótica, aprendizaje por refuerzo visual]
    project_type: academic
    status: completed
    featured: true
    interview_priority: 9
    areas: [computer_vision, robotics_control, deep_learning]
    tags: [visión artificial, aprendizaje por refuerzo, robótica, deep learning, control visual]
    primary_technology_ids: [python, numpy, opencv, pytorch]
    secondary_technology_ids: []
    role: {collaboration_type: academic_practice, title: implementer_and_analyst, context: academic}
    personal_contributions:
      - Implementación y documentación de prácticas de control visual, filtros probabilísticos, RL, imitación y modelos latentes.
    team_contributions: []
    provided_components: [Gymnasium y arquitecturas/algoritmos de referencia usados para aprendizaje]
    not_personally_implemented: [Algoritmos originales de PPO, SAC, DQN, Dreamer y modelos fundacionales]
    short_pitch: Proyecto de conexión entre percepción visual y acción. Cubre filtros de estado, aprendizaje por refuerzo visual, imitación, modelos latentes y transferencia sim-to-real.
    objective: Explorar cómo la percepción alimenta políticas de control y decisión.
    problem_solved: Relaciona observaciones visuales con estado, política y acción en entornos de control.
    verifiable_results:
      - Uso documentado de EKF-SLAM, Particle Filter, DQN, PPO, SAC, VAE, World Models, Dreamer, GAIL, DAgger, CURL, DrQ, RAD y Domain Randomization.
    competency_ids: [skill_control_visual_rl, skill_pytorch_vision]
    summary_path: vision-artificial-percepcion_para_accion_summary.md
    advanced_path: null
    repository: null
    demo: null
    rag_enabled: true
    retrieval_metadata: {project_id: project_percepcion_para_accion, allowed_document_types: [summary]}
    evidence_strength: strong_summary
    known_limitations: [Contexto académico, La ruta advanced declarada en el summary no existe en esta carpeta]

  - project_id: project_cubo_rubik_busqueda_estados
    canonical_name: Resolución del Cubo de Rubik con búsqueda en espacio de estados
    short_name: Cubo de Rubik con búsqueda
    aliases: [Cubo de Rubik con algoritmos de búsqueda, búsqueda en espacio de estados, A* IDA* y heurísticas para Rubik, algoritmos básicos de inteligencia artificial]
    project_type: academic
    status: completed
    featured: false
    interview_priority: 30
    areas: [symbolic_ai, applied_artificial_intelligence, software_engineering]
    tags: [inteligencia artificial, búsqueda heurística, python, algoritmos]
    primary_technology_ids: [python, bfs, astar, ida_star]
    secondary_technology_ids: []
    role: {collaboration_type: academic_practice, title: implementer_and_experimenter, context: academic}
    personal_contributions:
      - Implementación documentada del dominio Rubik, operadores, búsquedas no informadas/informadas, heurísticas y experimentación.
    team_contributions: []
    provided_components: []
    not_personally_implemented: []
    short_pitch: Implementación de búsqueda en espacio de estados aplicada al Cubo de Rubik. Permite explicar modelado de estados, operadores, heurísticas y comparación de algoritmos como BFS, A*, IDA* y Weighted A*.
    objective: Modelar el Cubo de Rubik como problema de búsqueda y comparar estrategias.
    problem_solved: Encuentra secuencias de movimientos mediante algoritmos de búsqueda y heurísticas.
    verifiable_results:
      - Uso documentado de BFS, profundidad acotada, profundidad iterativa, voraz, A*, IDA* y Weighted A*.
      - Métricas documentadas de tiempo, nodos, abiertos y longitud de solución.
    competency_ids: [skill_busqueda_estados, skill_heuristicas, skill_python]
    summary_path: cubo-rubik-busqueda-estados_summary.md
    advanced_path: null
    repository: null
    demo: null
    rag_enabled: true
    retrieval_metadata: {project_id: project_cubo_rubik_busqueda_estados, allowed_document_types: [summary]}
    evidence_strength: strong_summary
    known_limitations: [Contexto académico, La ruta advanced declarada en el summary no existe en esta carpeta]

  - project_id: project_conecta4_minimax_alfabeta
    canonical_name: Conecta 4 con MiniMax, poda alfa-beta y heurística ponderada
    short_name: Conecta 4 IA
    aliases: [Conecta 4 con inteligencia artificial, MiniMax y alfa-beta en Java, agente heurístico para Connect Four]
    project_type: academic
    status: completed
    featured: false
    interview_priority: 31
    areas: [symbolic_ai, applied_artificial_intelligence, software_engineering]
    tags: [inteligencia artificial, java, minimax, alfa-beta, heurísticas]
    primary_technology_ids: [java, minimax, alpha_beta]
    secondary_technology_ids: []
    role: {collaboration_type: team, title: contributor_to_presented_project, context: academic}
    personal_contributions:
      - Participación documentada en el entregable presentado, con integración de heurística ponderada, poda alfa-beta, ajuste de pesos, batería experimental y análisis de resultados.
    team_contributions:
      - El proyecto fue presentado por un equipo según el summary.
    provided_components:
      - Algunas clases base contienen comentarios históricos de autoría docente según el summary.
    not_personally_implemented:
      - No atribuir línea por línea todos los componentes sin historial Git utilizable.
    short_pitch: Agente de Conecta 4 en Java basado en MiniMax, poda alfa-beta y heurística ponderada. El proyecto demuestra búsqueda adversarial, optimización del árbol de juego y evaluación experimental.
    objective: Comparar estrategias de decisión para Conecta 4 y medir coste computacional.
    problem_solved: Selección automática de movimientos en un juego adversarial con reducción de búsqueda mediante poda.
    verifiable_results:
      - Experimentos documentados de 100 partidas por test.
      - Reducción documentada de nodos en profundidad 6 de 1314596 a 243371 al comparar MiniMax y alfa-beta.
    competency_ids: [skill_busqueda_adversarial, skill_heuristicas, skill_java]
    summary_path: conecta4-minimax-alfabeta_summary.md
    advanced_path: null
    repository: null
    demo: null
    rag_enabled: true
    retrieval_metadata: {project_id: project_conecta4_minimax_alfabeta, allowed_document_types: [summary]}
    evidence_strength: strong_summary
    known_limitations:
      - Contexto académico en equipo.
      - No atribuir línea por línea todos los componentes.
      - La ruta advanced declarada en el summary no existe en esta carpeta.

  - project_id: project_assistant_home_multiagente
    canonical_name: assistantHome
    short_name: assistantHome
    aliases: [assistantHome, sistema multiagente de asistencia doméstica, robot limpiador BDI con Jason, domótica con agentes inteligentes]
    project_type: academic
    status: completed
    featured: false
    interview_priority: 32
    areas: [symbolic_ai, applied_artificial_intelligence, robotics_control]
    tags: [inteligencia artificial, sistemas multiagente, jason, agentspeak, planificación, domótica]
    primary_technology_ids: [jason, agentspeak, bfs]
    secondary_technology_ids: []
    role: {collaboration_type: team, title: contributor_to_presented_project, context: academic}
    personal_contributions:
      - Participación documentada en el desarrollo y documentación del sistema multiagente presentado.
    team_contributions:
      - Sistema desarrollado y documentado por Duarte y su equipo según el summary.
    provided_components:
      - Entorno domotic.HouseEnv(gui), HouseEnv, HouseModel y HouseView tratados como infraestructura no modificable según el summary.
    not_personally_implemented:
      - No atribuir modificación del entorno base no modificable.
    short_pitch: Sistema multiagente BDI en Jason que simula un hogar inteligente con robot limpiador, propietario e intruso/invitado. Demuestra agentes autónomos, comunicación, planificación y recuperación de contexto.
    objective: Coordinar agentes autónomos en un entorno doméstico dinámico.
    problem_solved: Navegación, limpieza, batería, colisiones e identificación de intrusos mediante agentes.
    verifiable_results:
      - "Tres agentes documentados: robot, owner e intruder."
      - Uso documentado de BFS sobre grafo connect/3, comunicación .send y gestión de batería.
    competency_ids: [skill_sistemas_multiagente, skill_busqueda_estados]
    summary_path: assistant_home_multiagente_summary.md
    advanced_path: null
    repository: null
    demo: null
    rag_enabled: true
    retrieval_metadata: {project_id: project_assistant_home_multiagente, allowed_document_types: [summary]}
    evidence_strength: strong_summary
    known_limitations:
      - Contexto académico en equipo.
      - La ruta advanced declarada en el summary no existe en esta carpeta.

  - project_id: project_sistemas_reactivos
    canonical_name: Sistemas Reactivos con Lustre y Go
    short_name: Sistemas Reactivos
    aliases: [Sistemas Reactivos, Lustre y Go concurrente, semáforos refrigeración industrial y concurrencia en Go]
    project_type: academic
    status: completed
    featured: false
    interview_priority: 40
    areas: [reactive_systems, software_engineering]
    tags: [sistemas reactivos, lustre, go, concurrencia, programación síncrona]
    primary_technology_ids: [lustre, go, goroutines, channels]
    secondary_technology_ids: []
    role: {collaboration_type: academic_practice, title: implementer, context: academic}
    personal_contributions:
      - Implementación documentada de nodos Lustre y prácticas Go con concurrencia, canales, workers y sincronización.
    team_contributions: []
    provided_components: [Compilación/generación C desde Lustre cuando aplica]
    not_personally_implemented: [Runtime y compilador de Lustre]
    short_pitch: Prácticas sobre sistemas reactivos y concurrencia. Une programación síncrona en Lustre con programación concurrente en Go mediante goroutines, canales y sincronización.
    objective: Modelar sistemas deterministas y flujos concurrentes.
    problem_solved: Control temporal, sensores, semáforos, refrigeración y procesamiento concurrente.
    verifiable_results:
      - Uso documentado de nodos Lustre, integración C, Go 1.21, goroutines, channels, WaitGroup, ticker y select.
    competency_ids: [skill_lustre, skill_concurrencia_go, skill_go]
    summary_path: sistemas-reactivos_summary.md
    advanced_path: null
    repository: null
    demo: null
    rag_enabled: true
    retrieval_metadata: {project_id: project_sistemas_reactivos, allowed_document_types: [summary]}
    evidence_strength: strong_summary
    known_limitations: [Contexto académico, La ruta advanced declarada en el summary no existe en esta carpeta]

  - project_id: project_web_semantica_rdf_sparql_jena
    canonical_name: Web Semántica con RDF, RDFS, SPARQL, Jena y Fuseki
    short_name: Web Semántica
    aliases: [Web Semántica, RDF y SPARQL con Apache Jena, prácticas de Web Semántica, Linked Open Data con Wikidata y DBpedia]
    project_type: academic
    status: completed
    featured: false
    interview_priority: 41
    areas: [semantic_web, software_engineering]
    tags: [web semántica, rdf, sparql, apache jena, fuseki, linked open data]
    primary_technology_ids: [java, apache_jena, rdf, rdfs, sparql, fuseki]
    secondary_technology_ids: [wikidata, dbpedia]
    role: {collaboration_type: team, title: contributor_to_presented_project, context: academic}
    personal_contributions:
      - Participación documentada en el modelado, implementación, integración y documentación de prácticas de Web Semántica.
    team_contributions:
      - Entregas de grupo con Duarte y otros integrantes según el summary.
    provided_components: [Wikidata, DBpedia, vocabularios FOAF/WGS84 y Apache Jena como recursos externos]
    not_personally_implemented: [Endpoints externos y ontologías/vocabularios estándar]
    short_pitch: Proyecto de Web Semántica con RDF, RDFS, SPARQL, Apache Jena y Fuseki. Demuestra modelado de conocimiento, consultas federadas, razonamiento básico y publicación de grafos.
    objective: Representar, consultar, inferir y publicar conocimiento RDF.
    problem_solved: Convierte y enriquece datos heterogéneos en grafos consultables e interoperables.
    verifiable_results:
      - Uso documentado de FOAF, WGS84 Geo, SPARQL SELECT/CONSTRUCT/SERVICE, Fuseki, TDB2, Wikidata y DBpedia.
      - Generación documentada de salidas como final.ttl y stops_2_1.ttl.
    competency_ids: [skill_rdf_sparql, skill_apache_jena, skill_modelado_semantico, skill_java]
    summary_path: web-semantica-rdf-sparql-jena_summary.md
    advanced_path: null
    repository: null
    demo: null
    rag_enabled: true
    retrieval_metadata: {project_id: project_web_semantica_rdf_sparql_jena, allowed_document_types: [summary]}
    evidence_strength: strong_summary
    known_limitations:
      - Contexto académico en equipo.
      - No atribuir línea por línea todos los componentes.
      - La ruta advanced declarada en el summary no existe en esta carpeta.

  - project_id: project_asistente_profesional_web
    canonical_name: Asistente profesional web para entrevistas
    short_name: Asistente profesional web
    aliases:
      - asistente profesional para entrevistas
      - chat profesional de Duarte
      - asistente personal de contratación
      - perfil profesional conversacional
      - chatbot público con FastAPI y OpenAI
    project_type: personal
    status: deployed_publicly
    featured: true
    interview_priority: 2
    areas: [applied_artificial_intelligence, natural_language_processing, software_engineering, reactive_systems]
    tags: [openai, fastapi, asgi, streaming, seguridad web, concurrencia, docker, digitalocean, posthog]
    primary_technology_ids: [python, javascript, fastapi, uvicorn, openai_responses_api, pydantic, docker, digitalocean_app_platform, posthog]
    secondary_technology_ids: []
    role:
      collaboration_type: individual
      title: designer_developer_and_deployer
      context: personal_public_project
    personal_contributions:
      - Diseño e implementación de una aplicación web pública para presentar el perfil profesional de Duarte mediante conversación.
      - Desarrollo del backend FastAPI/ASGI, la interfaz HTML/CSS/JavaScript y el streaming de respuestas mediante OpenAI Responses API.
      - Implementación del acceso controlado a documentos Markdown, selección de contexto, sesiones efímeras en servidor y tres niveles de detalle de respuesta.
      - Implementación de una cola FIFO que atiende dos generaciones en paralelo y mantiene en espera las consultas adicionales dentro de límites configurables.
      - Aplicación de medidas de seguridad web, contenedorización con Docker, despliegue en DigitalOcean App Platform y analítica opcional con consentimiento en PostHog.
    team_contributions: []
    provided_components:
      - OpenAI Responses API como servicio externo de planificación, consulta documental y generación en streaming.
      - DigitalOcean App Platform como plataforma gestionada de despliegue.
      - PostHog Cloud como servicio externo opcional de analítica agregada.
    not_personally_implemented:
      - Modelos y servicio gestionado de OpenAI.
      - Infraestructura gestionada de DigitalOcean y PostHog.
    short_pitch: Aplicación web pública que representa el perfil profesional de Duarte y responde en streaming con evidencia de documentos Markdown. Combina FastAPI/ASGI, OpenAI Responses API, sesiones efímeras en servidor, límites de seguridad, concurrencia con cola FIFO, Docker, despliegue cloud y analítica opcional respetuosa con la privacidad.
    objective: Ofrecer a reclutadores y entrevistadores una forma pública, rápida y conversacional de conocer el perfil, proyectos y capacidades de Duarte.
    problem_solved: Centraliza información profesional estructurada en una interfaz conversacional, manteniendo el contexto por sesión y controlando el acceso a documentos y recursos del servidor.
    verifiable_results:
      - Aplicación desplegada públicamente en DigitalOcean App Platform y servida desde un contenedor Docker.
      - Respuesta en streaming con tres niveles de detalle y recordatorios de contacto en las preguntas 3, 8, 15 y 25.
      - Dos generaciones simultáneas permitidas y hasta veinte consultas adicionales en cola FIFO mediante valores predeterminados configurables.
      - Sesiones HttpOnly con expiración, historial acotado y 18 pruebas automatizadas locales verificadas en el repositorio.
      - Analítica PostHog activable por consentimiento; registra métricas agregadas sin enviar preguntas, respuestas ni historial.
    competency_ids: [skill_python, skill_openai_api, skill_fastapi_asgi, skill_frontend_web, skill_concurrencia_web, skill_seguridad_web, skill_despliegue_cloud, skill_analitica_producto, skill_testing_validacion, skill_diseno_modular]
    summary_path: null
    advanced_path: null
    repository: https://github.com/tostadito33/Chat-Profesional-para-Entrevistas-.git
    demo: https://asistente-personal-contratacion-9i9eg.ondigitalocean.app/
    rag_enabled: true
    retrieval_metadata:
      project_id: project_asistente_profesional_web
      allowed_document_types: [repository]
    evidence_strength: verified_repository_and_deployment
    known_limitations:
      - Las sesiones se guardan en memoria de una sola instancia; escalar a varias réplicas requeriría un almacén compartido.
      - La generación de respuestas depende de la disponibilidad y configuración de OpenAI.
      - La analítica solo recoge eventos de los usuarios que dan consentimiento y no tienen bloqueada su carga.

generated_indexes:
  area_index: derived_from_projects_areas
  technology_index: derived_from_primary_and_secondary_technology_ids
  note: No mantener tablas manuales por área o tecnología; deben generarse programáticamente desde los registros.
```

## Nota para mantenimiento humano

La fuente de verdad estructurada está en el bloque YAML anterior. Los índices por área, tecnología, alias y prioridad deben generarse desde `projects`, `areas` y `technologies` para evitar duplicaciones manuales.
