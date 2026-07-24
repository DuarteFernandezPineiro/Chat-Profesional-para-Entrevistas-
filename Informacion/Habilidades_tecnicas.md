---
schema_version: "1.0"
document_id: technical_skills
document_type: structured_skill_source
language: es
last_updated: "2026-07-21"
source_of_truth:
  - Indice_de_proyectos.md
  - current_markdown_project_summaries
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

skill_categories:
  - category_id: applied_ai
    name: Inteligencia artificial aplicada
  - category_id: nlp_ir
    name: NLP y recuperación de información
  - category_id: computer_vision
    name: Visión artificial
  - category_id: symbolic_ai_algorithms
    name: IA simbólica y algoritmos
  - category_id: software_development
    name: Desarrollo de software
  - category_id: semantic_data
    name: Datos semánticos
  - category_id: reactive_concurrent_systems
    name: Sistemas reactivos y concurrencia
  - category_id: professional_practice
    name: Práctica técnica transversal

skills:
  - skill_id: skill_rag_hibrido
    name: RAG híbrido
    aliases: [RAG, retrieval augmented generation, RAG híbrido, búsqueda híbrida, respuestas con fuentes]
    category_id: applied_ai
    subcategory_id: rag
    knowledge_level: advanced
    implementation_level: advanced_applied
    professional_experience_level: none
    production_experience: false
    experience_contexts: [academic]
    evidence_strength: strong_summary
    evidence:
      - project_id: project_rag_empresarial_tfg
        document_type: summary
        section_titles: [Presentación del proyecto, Solución desarrollada, Tecnologías algoritmos y conocimientos aplicados]
        evidence_type: implementation
        description: Pipeline RAG con ingesta, chunking, BM25, ChromaDB, embeddings OpenAI, RRF, Jina Reranker y generación con fuentes.
      - project_id: project_mineria_textos
        document_type: summary
        section_titles: [Tecnologías algoritmos y conocimientos aplicados]
        evidence_type: academic_usage
        description: Prácticas con ChromaDB, BM25, RRF, RAG y sistemas LLM.
    can_claim:
      - Ha implementado un prototipo RAG híbrido académico con recuperación léxica y vectorial.
      - Ha combinado BM25 y embeddings mediante RRF y ha integrado reranking externo.
      - Ha trabajado respuestas con fuentes numeradas y control de evidencia.
    cannot_claim:
      - No afirmar operación de un RAG en producción.
      - No afirmar experiencia profesional consolidada en RAG.
    known_limitations: [Evidencia académica, sin despliegue productivo documentado]
    related_technology_ids: [python, bm25, chromadb, rrf, jina_reranker, openai_responses_api, openai_embeddings]

  - skill_id: skill_openai_api
    name: Integración con OpenAI
    aliases: [OpenAI, OpenAI Responses API, embeddings OpenAI, text-embedding-3-large]
    category_id: applied_ai
    subcategory_id: llm_integration
    knowledge_level: intermediate_high
    implementation_level: independent
    professional_experience_level: none
    production_experience: false
    experience_contexts: [academic]
    evidence_strength: strong_summary
    evidence:
      - project_id: project_rag_empresarial_tfg
        document_type: summary
        section_titles: [Presentación del proyecto, Funcionamiento paso a paso, Tecnologías algoritmos y conocimientos aplicados]
        evidence_type: integration
        description: Integración de OpenAI Responses API para extracción/generación y text-embedding-3-large para chunks y consultas.
    can_claim:
      - Ha integrado OpenAI Responses API en un prototipo RAG académico.
      - Ha usado text-embedding-3-large para recuperación semántica documentada.
    cannot_claim:
      - No afirmar uso documentado de Chat Completions API en este repositorio.
      - No afirmar uso documentado de text-embedding-3-small.
      - No afirmar que implementó internamente modelos de OpenAI.
    known_limitations: [Integración mediante API externa, sin producción documentada]
    related_technology_ids: [openai_responses_api, openai_embeddings]

  - skill_id: skill_ir_bm25_tfidf
    name: Recuperación léxica
    aliases: [BM25, TF-IDF, recuperación de información, ranking documental, búsqueda léxica]
    category_id: nlp_ir
    subcategory_id: lexical_retrieval
    knowledge_level: advanced
    implementation_level: advanced_applied
    professional_experience_level: none
    production_experience: false
    experience_contexts: [academic]
    evidence_strength: strong_summary
    evidence:
      - project_id: project_recuperacion_informacion
        document_type: summary
        section_titles: [Tecnologías algoritmos y conocimientos aplicados]
        evidence_type: implementation
        description: Prácticas con TF-IDF, similitud coseno, BM25 manual, rank_bm25 y Whoosh BM25F.
      - project_id: project_rag_empresarial_tfg
        document_type: summary
        section_titles: [Solución desarrollada]
        evidence_type: implementation
        description: Índice BM25 local dentro de un sistema RAG híbrido.
      - project_id: project_mineria_textos
        document_type: summary
        section_titles: [Tecnologías algoritmos y conocimientos aplicados]
        evidence_type: academic_usage
        description: BM25 como búsqueda léxica sobre documentos tokenizados.
    can_claim:
      - Ha implementado y usado BM25 en contextos académicos y prototipos.
      - Ha comparado técnicas de ranking como TF-IDF, BM25 y modelos de lenguaje.
    cannot_claim:
      - No afirmar operación de buscadores a escala industrial.
    known_limitations: [Evidencia académica y de prototipo local]
    related_technology_ids: [bm25, scikit_learn, pandas]

  - skill_id: skill_modelos_lenguaje_ir
    name: Modelos probabilísticos de recuperación
    aliases: [BIM, Query Likelihood, RM3, suavizado, Dirichlet, Jelinek-Mercer]
    category_id: nlp_ir
    subcategory_id: probabilistic_ir
    knowledge_level: intermediate_high
    implementation_level: independent
    professional_experience_level: none
    production_experience: false
    experience_contexts: [academic]
    evidence_strength: strong_summary
    evidence:
      - project_id: project_recuperacion_informacion
        document_type: summary
        section_titles: [Tecnologías algoritmos y conocimientos aplicados]
        evidence_type: implementation
        description: Uso de BIM, RM3, Query Likelihood y suavizados Laplace, Jelinek-Mercer y Dirichlet.
    can_claim:
      - Conoce y ha aplicado modelos probabilísticos de recuperación en prácticas académicas.
    cannot_claim:
      - No afirmar uso profesional de estos modelos en un buscador productivo.
    known_limitations: [Contexto académico]
    related_technology_ids: [bm25]

  - skill_id: skill_embeddings_nlp
    name: Embeddings para NLP
    aliases: [embeddings, Word2Vec, Skip-gram, SBERT, BERT, embeddings contextuales]
    category_id: nlp_ir
    subcategory_id: embeddings
    knowledge_level: advanced
    implementation_level: independent
    professional_experience_level: none
    production_experience: false
    experience_contexts: [academic]
    evidence_strength: strong_summary
    evidence:
      - project_id: project_procesamiento_lenguaje_natural_bpe_skipgram
        document_type: summary
        section_titles: [Tecnologías algoritmos y conocimientos aplicados]
        evidence_type: implementation
        description: Implementación de Skip-gram con negative sampling y persistencia de embeddings.
      - project_id: project_mineria_textos
        document_type: summary
        section_titles: [Tecnologías algoritmos y conocimientos aplicados]
        evidence_type: academic_usage
        description: Uso de Word2Vec, BERT, SBERT y embeddings de frase para similitud y recuperación.
    can_claim:
      - Ha implementado fundamentos de Word2Vec/Skip-gram.
      - Ha usado embeddings estáticos, contextuales y de frase en prácticas de NLP.
    cannot_claim:
      - No afirmar entrenamiento a gran escala de modelos fundacionales.
    known_limitations: [Contexto académico]
    related_technology_ids: [word2vec, bert, sbert, numpy]

  - skill_id: skill_tokenizacion_bpe
    name: Tokenización subword
    aliases: [BPE, byte-level BPE, tokenización subword, tokenización UTF-8]
    category_id: nlp_ir
    subcategory_id: tokenization
    knowledge_level: intermediate_high
    implementation_level: independent
    professional_experience_level: none
    production_experience: false
    experience_contexts: [academic]
    evidence_strength: strong_summary
    evidence:
      - project_id: project_procesamiento_lenguaje_natural_bpe_skipgram
        document_type: summary
        section_titles: [Tecnologías algoritmos y conocimientos aplicados]
        evidence_type: implementation
        description: Implementación de tokenización UTF-8 byte-level y aprendizaje de fusiones BPE.
    can_claim:
      - Ha implementado un tokenizador byte-level BPE en contexto académico.
    cannot_claim:
      - No afirmar que ha diseñado el tokenizador de un modelo comercial.
    known_limitations: [Contexto académico]
    related_technology_ids: [bpe, python]

  - skill_id: skill_topic_modeling
    name: Topic modeling y clustering semántico
    aliases: [topic modeling, BERTopic, UMAP, HDBSCAN, clustering de reviews]
    category_id: nlp_ir
    subcategory_id: topic_modeling
    knowledge_level: intermediate
    implementation_level: limited
    professional_experience_level: none
    production_experience: false
    experience_contexts: [academic]
    evidence_strength: strong_summary
    evidence:
      - project_id: project_mineria_textos
        document_type: summary
        section_titles: [Tecnologías algoritmos y conocimientos aplicados]
        evidence_type: academic_usage
        description: Uso de BERTopic, UMAP y HDBSCAN para clustering y triaje guiado.
    can_claim:
      - Ha aplicado topic modeling no supervisado y guiado en prácticas de minería de textos.
    cannot_claim:
      - No afirmar experiencia productiva en sistemas de clasificación temática.
    known_limitations: [Uso académico]
    related_technology_ids: [bertopic, umap, hdbscan]

  - skill_id: skill_text_mining_ingesta
    name: Ingesta y limpieza textual
    aliases: [scraping, OCR, extracción PDF, BeautifulSoup, PyMuPDF, Tesseract, normalización Unicode]
    category_id: nlp_ir
    subcategory_id: text_ingestion
    knowledge_level: intermediate_high
    implementation_level: independent
    professional_experience_level: none
    production_experience: false
    experience_contexts: [academic]
    evidence_strength: strong_summary
    evidence:
      - project_id: project_mineria_textos
        document_type: summary
        section_titles: [Tecnologías algoritmos y conocimientos aplicados]
        evidence_type: implementation
        description: Extracción de HTML, PDFs, OCR, normalización Unicode, detección de idioma y deduplicación.
      - project_id: project_rag_empresarial_tfg
        document_type: summary
        section_titles: [Solución desarrollada]
        evidence_type: implementation
        description: Procesamiento de PDFs por páginas, generación de Markdown limpio y metadatos.
    can_claim:
      - Ha trabajado ingesta documental desde HTML, PDF y OCR.
      - Ha normalizado corpus para recuperación y NLP.
    cannot_claim:
      - No afirmar operación de pipelines documentales empresariales en producción.
    known_limitations: [Contexto académico y prototipo local]
    related_technology_ids: [beautifulsoup, pymupdf, tesseract, fasttext, presidio]

  - skill_id: skill_resumen_extractivo
    name: Resumen extractivo y grafos semánticos
    aliases: [TextRank, QFS, PageRank, NetworkX, resumen extractivo]
    category_id: nlp_ir
    subcategory_id: summarization
    knowledge_level: intermediate
    implementation_level: limited
    professional_experience_level: none
    production_experience: false
    experience_contexts: [academic]
    evidence_strength: strong_summary
    evidence:
      - project_id: project_mineria_textos
        document_type: summary
        section_titles: [Tecnologías algoritmos y conocimientos aplicados]
        evidence_type: academic_usage
        description: TextRank y QFS con NetworkX y PageRank.
    can_claim:
      - Ha aplicado resumen extractivo basado en grafos en prácticas académicas.
    cannot_claim:
      - No afirmar despliegue de un sistema de resumen en producción.
    known_limitations: [Uso académico]
    related_technology_ids: [networkx]

  - skill_id: skill_opencv_imagen
    name: OpenCV y procesamiento de imagen
    aliases: [OpenCV, cv2, procesamiento de imagen, filtros, warping, undistortion]
    category_id: computer_vision
    subcategory_id: classical_vision
    knowledge_level: advanced
    implementation_level: advanced_applied
    professional_experience_level: none
    production_experience: false
    experience_contexts: [academic]
    evidence_strength: strong_summary
    evidence:
      - project_id: project_vision_artificial_fundamentos
        document_type: summary
        section_titles: [Tecnologías algoritmos y conocimientos aplicados]
        evidence_type: implementation
        description: Calibración, esquinas, warping, undistortion, filtros, color y procesamiento de imagen.
      - project_id: project_vision_artificial_video_temporalidad
        document_type: summary
        section_titles: [Tecnologías algoritmos y conocimientos aplicados]
        evidence_type: academic_usage
        description: VideoCapture, VideoWriter, ROI, flujo óptico, histogramas y tracking.
    can_claim:
      - Ha usado OpenCV en prácticas de imagen y vídeo.
      - Ha implementado y comparado pipelines de visión clásica.
    cannot_claim:
      - No afirmar experiencia profesional en inspección industrial o producción visual.
    known_limitations: [Contexto académico]
    related_technology_ids: [opencv, python, cpp]

  - skill_id: skill_geometria_vision
    name: Geometría de cámara y visión 3D
    aliases: [calibración de cámara, homografías, DLT, RANSAC, error de reproyección, geometría multivista]
    category_id: computer_vision
    subcategory_id: geometry
    knowledge_level: intermediate_high
    implementation_level: independent
    professional_experience_level: none
    production_experience: false
    experience_contexts: [academic]
    evidence_strength: strong_summary
    evidence:
      - project_id: project_vision_artificial_fundamentos
        document_type: summary
        section_titles: [Presentación del proyecto, Tecnologías algoritmos y conocimientos aplicados]
        evidence_type: implementation
        description: Calibración Zhang, DLT normalizado, RANSAC y error de reproyección.
      - project_id: project_vision_artificial_escena_3d
        document_type: summary
        section_titles: [Tecnologías algoritmos y conocimientos aplicados]
        evidence_type: academic_usage
        description: SfM, MVS, geometría epipolar, NCC y triangulación.
    can_claim:
      - Ha aplicado fundamentos de geometría de cámara, homografías y reconstrucción 3D en prácticas académicas.
    cannot_claim:
      - No afirmar experiencia profesional en calibración industrial.
    known_limitations: [Contexto académico]
    related_technology_ids: [opencv, numpy, scipy]

  - skill_id: skill_procesamiento_imagen
    name: Procesamiento digital de imagen
    aliases: [FFT, aliasing, Canny, Sobel, morfología, convolución, CLAHE]
    category_id: computer_vision
    subcategory_id: image_processing
    knowledge_level: intermediate_high
    implementation_level: independent
    professional_experience_level: none
    production_experience: false
    experience_contexts: [academic]
    evidence_strength: strong_summary
    evidence:
      - project_id: project_vision_artificial_fundamentos
        document_type: summary
        section_titles: [Tecnologías algoritmos y conocimientos aplicados]
        evidence_type: implementation
        description: FFT, aliasing, Canny por etapas, filtros y operaciones morfológicas.
    can_claim:
      - Ha implementado operaciones clásicas de procesamiento digital de imagen en prácticas.
    cannot_claim:
      - No afirmar uso productivo en control de calidad.
    known_limitations: [Contexto académico]
    related_technology_ids: [opencv, numpy, scipy, pytorch]

  - skill_id: skill_pytorch_vision
    name: PyTorch aplicado a visión
    aliases: [PyTorch, TorchVision, deep learning visual, transfer learning]
    category_id: computer_vision
    subcategory_id: deep_learning_vision
    knowledge_level: advanced
    implementation_level: advanced_applied
    professional_experience_level: none
    production_experience: false
    experience_contexts: [academic]
    evidence_strength: strong_summary
    evidence:
      - project_id: project_vision_artificial_percepcion_deep_learning
        document_type: summary
        section_titles: [Tecnologías algoritmos y conocimientos aplicados]
        evidence_type: implementation
        description: Modelos, tensores, autograd, entrenamiento, pérdidas y backbones de visión.
      - project_id: project_vision_artificial_video_temporalidad
        document_type: summary
        section_titles: [Tecnologías algoritmos y conocimientos aplicados]
        evidence_type: implementation
        description: MDNet, C3D, Two-Stream, DFF y STM en PyTorch.
      - project_id: project_percepcion_para_accion
        document_type: summary
        section_titles: [Tecnologías algoritmos y conocimientos aplicados]
        evidence_type: academic_usage
        description: Redes neuronales, optimización, pérdidas y políticas para control visual.
    can_claim:
      - Ha implementado y adaptado modelos visuales en PyTorch en contexto académico.
      - Ha trabajado clasificación, segmentación, detección, vídeo y control visual.
    cannot_claim:
      - No afirmar entrenamiento de modelos fundacionales propios.
      - No afirmar despliegue productivo de modelos PyTorch.
    known_limitations: [Contexto académico y experimental]
    related_technology_ids: [pytorch, torchvision, python]

  - skill_id: skill_clasificacion_visual
    name: Clasificación visual
    aliases: [ResNet, MobileNet, Vision Transformer, SE, CBAM, clasificación de imágenes]
    category_id: computer_vision
    subcategory_id: classification
    knowledge_level: intermediate_high
    implementation_level: independent
    professional_experience_level: none
    production_experience: false
    experience_contexts: [academic]
    evidence_strength: strong_summary
    evidence:
      - project_id: project_vision_artificial_percepcion_deep_learning
        document_type: summary
        section_titles: [Tecnologías algoritmos y conocimientos aplicados]
        evidence_type: implementation
        description: Uso de ResNet, MobileNet, Vision Transformer, SE y CBAM.
    can_claim:
      - Ha trabajado clasificación visual con CNNs, transformers y mecanismos de atención en prácticas.
    cannot_claim:
      - No afirmar diseño original de ResNet, MobileNet o ViT.
    known_limitations: [Uso académico de arquitecturas conocidas]
    related_technology_ids: [pytorch, torchvision]

  - skill_id: skill_segmentacion
    name: Segmentación de imagen y vídeo
    aliases: [U-Net, FCN, DeepLabV3+, Mini-SAM, segmentación de imagen, segmentación visual]
    category_id: computer_vision
    subcategory_id: segmentation
    knowledge_level: intermediate_high
    implementation_level: independent
    professional_experience_level: none
    production_experience: false
    experience_contexts: [academic]
    evidence_strength: strong_summary
    evidence:
      - project_id: project_vision_artificial_percepcion_deep_learning
        document_type: summary
        section_titles: [Tecnologías algoritmos y conocimientos aplicados]
        evidence_type: implementation
        description: U-Net, FCN, DeepLabV3+ y Mini-SAM.
      - project_id: project_vision_artificial_video_temporalidad
        document_type: summary
        section_titles: [Tecnologías algoritmos y conocimientos aplicados]
        evidence_type: academic_usage
        description: STM con memoria key/value y máscaras para segmentación temporal.
    can_claim:
      - Ha implementado o adaptado pipelines de segmentación visual en PyTorch.
    cannot_claim:
      - No afirmar autoría de las arquitecturas originales.
    known_limitations: [Contexto académico]
    related_technology_ids: [pytorch, torchvision]

  - skill_id: skill_deteccion_objetos
    name: Detección de objetos
    aliases: [YOLO, FCOS, FPN, NMS, Soft-NMS, COCO API, mAP]
    category_id: computer_vision
    subcategory_id: object_detection
    knowledge_level: intermediate_high
    implementation_level: independent
    professional_experience_level: none
    production_experience: false
    experience_contexts: [academic]
    evidence_strength: strong_summary
    evidence:
      - project_id: project_vision_artificial_percepcion_deep_learning
        document_type: summary
        section_titles: [Tecnologías algoritmos y conocimientos aplicados]
        evidence_type: implementation
        description: YOLO, FCOS, COCO API, NMS, Soft-NMS, pérdidas y métricas de detección.
    can_claim:
      - Ha trabajado detección de objetos de una etapa y anchor-free en prácticas académicas.
    cannot_claim:
      - No afirmar despliegue productivo de detectores.
    known_limitations: [Contexto académico]
    related_technology_ids: [pytorch, torchvision]

  - skill_id: skill_video_tracking
    name: Visión en vídeo y tracking
    aliases: [tracking, KLT, Lucas-Kanade, MeanShift, CamShift, Kalman, Particle Filter, MOSSE]
    category_id: computer_vision
    subcategory_id: video_tracking
    knowledge_level: intermediate_high
    implementation_level: independent
    professional_experience_level: none
    production_experience: false
    experience_contexts: [academic]
    evidence_strength: strong_summary
    evidence:
      - project_id: project_vision_artificial_video_temporalidad
        document_type: summary
        section_titles: [Tecnologías algoritmos y conocimientos aplicados]
        evidence_type: implementation
        description: KLT, Lucas-Kanade, MeanShift, CamShift, Kalman, Particle Filter, SSD y MOSSE.
    can_claim:
      - Ha implementado o ejecutado técnicas de seguimiento visual clásico y probabilístico.
    cannot_claim:
      - No afirmar uso profesional en sistemas de vigilancia o robótica real.
    known_limitations: [Contexto académico y experimental]
    related_technology_ids: [opencv, numpy, pytorch]

  - skill_id: skill_reconocimiento_acciones
    name: Reconocimiento de acciones en vídeo
    aliases: [C3D, Two-Stream, flujo óptico, UCF-101, Deep Feature Flow, STM]
    category_id: computer_vision
    subcategory_id: action_recognition
    knowledge_level: intermediate_high
    implementation_level: independent
    professional_experience_level: none
    production_experience: false
    experience_contexts: [academic]
    evidence_strength: strong_summary
    evidence:
      - project_id: project_vision_artificial_video_temporalidad
        document_type: summary
        section_titles: [Tecnologías algoritmos y conocimientos aplicados, Resultados y validación]
        evidence_type: implementation
        description: C3D, Two-Stream, DFF, STM y logs sobre UCF-101.
    can_claim:
      - Ha trabajado modelos temporales y flujo óptico para reconocimiento de acciones.
    cannot_claim:
      - No afirmar una precisión final consolidada si no está documentada.
    known_limitations: [No hay métrica final consolidada documentada en el summary]
    related_technology_ids: [pytorch, torchvision, opencv]

  - skill_id: skill_vision_3d
    name: Visión 3D
    aliases: [stereo depth, SfM, MVS, PointNet, NeRF, PointPillars, reconstrucción 3D]
    category_id: computer_vision
    subcategory_id: vision_3d
    knowledge_level: intermediate
    implementation_level: limited
    professional_experience_level: none
    production_experience: false
    experience_contexts: [academic]
    evidence_strength: strong_summary
    evidence:
      - project_id: project_vision_artificial_escena_3d
        document_type: summary
        section_titles: [Tecnologías algoritmos y conocimientos aplicados]
        evidence_type: academic_usage
        description: DispNet, GC-Net, PSMNet, SfM, MVS, PointNet, PointPillars y NeRF.
    can_claim:
      - Ha estudiado y aplicado prácticas de profundidad, reconstrucción y representaciones 3D.
    cannot_claim:
      - No afirmar implementación desde cero de NeRF o PointPillars salvo evidencia más detallada.
    known_limitations: [Contexto académico]
    related_technology_ids: [python, numpy, opencv, pytorch, scipy]

  - skill_id: skill_control_visual_rl
    name: Percepción para acción y aprendizaje por refuerzo visual
    aliases: [visual RL, PPO, SAC, DQN, EKF-SLAM, Dreamer, World Models, imitación]
    category_id: computer_vision
    subcategory_id: visual_control
    knowledge_level: intermediate_high
    implementation_level: independent
    professional_experience_level: none
    production_experience: false
    experience_contexts: [academic]
    evidence_strength: strong_summary
    evidence:
      - project_id: project_percepcion_para_accion
        document_type: summary
        section_titles: [Tecnologías algoritmos y conocimientos aplicados]
        evidence_type: academic_usage
        description: EKF-SLAM, Particle Filter, DQN, PPO, SAC, VAE, World Models, Dreamer, GAIL, DAgger, CURL, DrQ, RAD y Domain Randomization.
    can_claim:
      - Ha trabajado la relación entre percepción visual, estado, política y acción en prácticas académicas.
    cannot_claim:
      - No afirmar experiencia profesional en robótica física.
      - No afirmar despliegue sim-to-real real sin evidencia.
    known_limitations: [Contexto académico]
    related_technology_ids: [python, numpy, opencv, pytorch]

  - skill_id: skill_busqueda_estados
    name: Búsqueda en espacio de estados
    aliases: [BFS, profundidad iterativa, A*, IDA*, Weighted A*, búsqueda heurística]
    category_id: symbolic_ai_algorithms
    subcategory_id: state_space_search
    knowledge_level: advanced
    implementation_level: advanced_applied
    professional_experience_level: none
    production_experience: false
    experience_contexts: [academic]
    evidence_strength: strong_summary
    evidence:
      - project_id: project_cubo_rubik_busqueda_estados
        document_type: summary
        section_titles: [Tecnologías algoritmos y conocimientos aplicados]
        evidence_type: implementation
        description: BFS, profundidad acotada, profundidad iterativa, voraz, A*, IDA* y Weighted A*.
      - project_id: project_assistant_home_multiagente
        document_type: summary
        section_titles: [Tecnologías algoritmos y conocimientos aplicados]
        evidence_type: academic_usage
        description: BFS sobre connect/3 para planificación simbólica en grafos.
    can_claim:
      - Ha implementado algoritmos de búsqueda en espacio de estados y heurísticas.
      - Ha aplicado BFS en planificación simbólica de agentes.
    cannot_claim:
      - No afirmar aplicación profesional en sistemas productivos.
    known_limitations: [Contexto académico]
    related_technology_ids: [python, bfs, astar, ida_star]

  - skill_id: skill_busqueda_adversarial
    name: Búsqueda adversarial
    aliases: [MiniMax, poda alfa-beta, teoría de juegos, Conecta 4]
    category_id: symbolic_ai_algorithms
    subcategory_id: adversarial_search
    knowledge_level: intermediate_high
    implementation_level: independent
    professional_experience_level: none
    production_experience: false
    experience_contexts: [academic]
    evidence_strength: strong_summary
    evidence:
      - project_id: project_conecta4_minimax_alfabeta
        document_type: summary
        section_titles: [Tecnologías algoritmos y conocimientos aplicados, Resultados y validación]
        evidence_type: implementation
        description: MiniMax, poda alfa-beta, heurística ponderada, búsqueda local y comparativas de 100 partidas.
    can_claim:
      - Ha trabajado búsqueda adversarial y poda alfa-beta en Java.
    cannot_claim:
      - No atribuir línea por línea todos los componentes del proyecto en equipo.
    known_limitations: [Contexto académico en equipo]
    related_technology_ids: [java, minimax, alpha_beta]

  - skill_id: skill_heuristicas
    name: Diseño de heurísticas
    aliases: [heurísticas, funciones de evaluación, H1, H2, evaluador ponderado, búsqueda local]
    category_id: symbolic_ai_algorithms
    subcategory_id: heuristics
    knowledge_level: intermediate_high
    implementation_level: independent
    professional_experience_level: none
    production_experience: false
    experience_contexts: [academic]
    evidence_strength: strong_summary
    evidence:
      - project_id: project_cubo_rubik_busqueda_estados
        document_type: summary
        section_titles: [Tecnologías algoritmos y conocimientos aplicados]
        evidence_type: implementation
        description: Heurísticas H1 y H2 para búsqueda informada.
      - project_id: project_conecta4_minimax_alfabeta
        document_type: summary
        section_titles: [Tecnologías algoritmos y conocimientos aplicados]
        evidence_type: implementation
        description: Heurística ponderada y búsqueda local de pesos.
    can_claim:
      - Ha diseñado y evaluado heurísticas interpretables en proyectos académicos.
    cannot_claim:
      - No afirmar optimización profesional de heurísticas en producción.
    known_limitations: [Contexto académico]
    related_technology_ids: [astar, ida_star, minimax, alpha_beta]

  - skill_id: skill_sistemas_multiagente
    name: Sistemas multiagente BDI
    aliases: [Jason, AgentSpeak, BDI, agentes, sistemas multiagente]
    category_id: symbolic_ai_algorithms
    subcategory_id: multi_agent_systems
    knowledge_level: intermediate_high
    implementation_level: independent
    professional_experience_level: none
    production_experience: false
    experience_contexts: [academic]
    evidence_strength: strong_summary
    evidence:
      - project_id: project_assistant_home_multiagente
        document_type: summary
        section_titles: [Presentación del proyecto, Tecnologías algoritmos y conocimientos aplicados]
        evidence_type: implementation
        description: Jason, AgentSpeak, arquitectura BDI, comunicación .send, BFS, grafo connect/3, batería y guardias lógicas.
    can_claim:
      - Ha participado en un sistema multiagente académico con Jason y AgentSpeak.
    cannot_claim:
      - No afirmar experiencia profesional en robótica doméstica real.
      - No afirmar modificación del entorno base indicado como no modificable.
    known_limitations: [Contexto académico en equipo]
    related_technology_ids: [jason, agentspeak, bfs]

  - skill_id: skill_python
    name: Python
    aliases: [Python, programación en Python, scripting Python]
    category_id: software_development
    subcategory_id: programming_language
    knowledge_level: advanced
    implementation_level: advanced_applied
    professional_experience_level: none
    production_experience: false
    experience_contexts: [academic, personal]
    evidence_strength: strong_summary
    evidence:
      - project_id: project_rag_empresarial_tfg
        document_type: summary
        section_titles: [Tecnologías algoritmos y conocimientos aplicados]
        evidence_type: implementation
        description: Pipeline, CLI, servidor web y tests en Python.
      - project_id: project_cubo_rubik_busqueda_estados
        document_type: summary
        section_titles: [Tecnologías algoritmos y conocimientos aplicados]
        evidence_type: implementation
        description: Dominio, algoritmos y experimentación en Python.
      - project_id: project_mineria_textos
        document_type: summary
        section_titles: [Tecnologías algoritmos y conocimientos aplicados]
        evidence_type: academic_usage
        description: 39 scripts de prácticas.
      - project_id: project_vision_artificial_fundamentos
        document_type: summary
        section_titles: [Tecnologías algoritmos y conocimientos aplicados]
        evidence_type: academic_usage
        description: Scripts de visión artificial, generación de datos y procesamiento.
    can_claim:
      - Ha usado Python de forma amplia en IA, NLP, recuperación, visión y algoritmos.
    cannot_claim:
      - No afirmar experiencia profesional en Python si no hay evidencia externa en estos documentos.
    known_limitations: [Evidencia de proyectos académicos y personales documentados, sin producción documentada]
    related_technology_ids: [python]

  - skill_id: skill_java
    name: Java
    aliases: [Java, programación orientada a objetos en Java, Maven]
    category_id: software_development
    subcategory_id: programming_language
    knowledge_level: intermediate_high
    implementation_level: independent
    professional_experience_level: none
    production_experience: false
    experience_contexts: [academic]
    evidence_strength: strong_summary
    evidence:
      - project_id: project_conecta4_minimax_alfabeta
        document_type: summary
        section_titles: [Tecnologías algoritmos y conocimientos aplicados]
        evidence_type: implementation
        description: Implementación Java con POO, patrón Estrategia, MiniMax y alfa-beta.
      - project_id: project_web_semantica_rdf_sparql_jena
        document_type: summary
        section_titles: [Tecnologías algoritmos y conocimientos aplicados]
        evidence_type: academic_usage
        description: Programas Maven para SPARQL, razonamiento y enriquecimiento.
    can_claim:
      - Ha usado Java en proyectos académicos de IA y Web Semántica.
    cannot_claim:
      - No afirmar experiencia profesional Java.
    known_limitations: [Contexto académico]
    related_technology_ids: [java, apache_jena]

  - skill_id: skill_go
    name: Go
    aliases: [Go, Golang]
    category_id: software_development
    subcategory_id: programming_language
    knowledge_level: intermediate
    implementation_level: independent
    professional_experience_level: none
    production_experience: false
    experience_contexts: [academic]
    evidence_strength: strong_summary
    evidence:
      - project_id: project_sistemas_reactivos
        document_type: summary
        section_titles: [Tecnologías algoritmos y conocimientos aplicados]
        evidence_type: implementation
        description: Paquetes Go, slices, maps, interfaces, panic/recover, goroutines, channels y WaitGroup.
    can_claim:
      - Ha usado Go para prácticas de concurrencia y organización modular.
    cannot_claim:
      - No afirmar experiencia profesional en Go.
    known_limitations: [Contexto académico]
    related_technology_ids: [go, goroutines, channels]

  - skill_id: skill_cpp
    name: C++
    aliases: [C++, cpp, OpenCV C++]
    category_id: software_development
    subcategory_id: programming_language
    knowledge_level: solid_foundation
    implementation_level: limited
    professional_experience_level: none
    production_experience: false
    experience_contexts: [academic]
    evidence_strength: strong_summary
    evidence:
      - project_id: project_vision_artificial_fundamentos
        document_type: summary
        section_titles: [Tecnologías algoritmos y conocimientos aplicados]
        evidence_type: academic_usage
        description: Implementaciones OpenCV de calibración y undistortion en C++.
    can_claim:
      - Ha usado C++ en prácticas de visión artificial con OpenCV.
    cannot_claim:
      - No afirmar experiencia profesional o avanzada general en C++.
    known_limitations: [Uso acotado a visión artificial académica]
    related_technology_ids: [cpp, opencv]

  - skill_id: skill_api_web_local
    name: APIs e interfaces web locales
    aliases: [HTTPServer, interfaz web local, endpoint /api/answer, CLI]
    category_id: software_development
    subcategory_id: local_backend
    knowledge_level: intermediate
    implementation_level: independent
    professional_experience_level: none
    production_experience: false
    experience_contexts: [academic]
    evidence_strength: strong_summary
    evidence:
      - project_id: project_rag_empresarial_tfg
        document_type: summary
        section_titles: [Tecnologías algoritmos y conocimientos aplicados]
        evidence_type: implementation
        description: HTTPServer, HTML/CSS/JS, endpoint /api/answer, CLI y chat interactivo.
    can_claim:
      - Ha expuesto un prototipo de IA mediante CLI e interfaz web local.
    cannot_claim:
      - No afirmar despliegue productivo multiusuario.
    known_limitations: [Interfaz local y demo temporal documentada]
    related_technology_ids: [python]

  - skill_id: skill_testing_validacion
    name: Testing y validación
    aliases: [unittest, tests, métricas, benchmarks, evaluación experimental]
    category_id: software_development
    subcategory_id: validation
    knowledge_level: intermediate_high
    implementation_level: independent
    professional_experience_level: none
    production_experience: false
    experience_contexts: [academic]
    evidence_strength: strong_summary
    evidence:
      - project_id: project_rag_empresarial_tfg
        document_type: summary
        section_titles: [Presentación del proyecto, Tecnologías algoritmos y conocimientos aplicados]
        evidence_type: evaluation
        description: 57 tests ejecutados correctamente y validación de contratos.
      - project_id: project_conecta4_minimax_alfabeta
        document_type: summary
        section_titles: [Resultados y validación]
        evidence_type: evaluation
        description: Comparativas de 100 partidas y métricas de nodos/tiempo.
      - project_id: project_cubo_rubik_busqueda_estados
        document_type: summary
        section_titles: [Tecnologías algoritmos y conocimientos aplicados]
        evidence_type: evaluation
        description: Métricas de tiempo, nodos y longitud de solución.
    can_claim:
      - Ha usado tests y evaluación experimental para validar comportamiento y comparar alternativas.
    cannot_claim:
      - No afirmar cobertura completa de producción.
    known_limitations: [Validación académica o de prototipo]
    related_technology_ids: [python]

  - skill_id: skill_pydantic_contratos
    name: Contratos de datos con Pydantic
    aliases: [Pydantic, esquemas, validación de datos, contratos de datos]
    category_id: software_development
    subcategory_id: data_contracts
    knowledge_level: intermediate_high
    implementation_level: independent
    professional_experience_level: none
    production_experience: false
    experience_contexts: [academic]
    evidence_strength: strong_summary
    evidence:
      - project_id: project_rag_empresarial_tfg
        document_type: summary
        section_titles: [Tecnologías algoritmos y conocimientos aplicados]
        evidence_type: implementation
        description: Esquemas de extracción, metadatos y validación con Pydantic.
    can_claim:
      - Ha usado Pydantic para contratos de datos en un prototipo RAG académico.
    cannot_claim:
      - No afirmar experiencia profesional en plataformas de validación productivas.
    known_limitations: [Contexto de prototipo académico]
    related_technology_ids: [pydantic, python]

  - skill_id: skill_resiliencia_operativa
    name: Resiliencia de pipelines
    aliases: [Tenacity, reintentos, timeouts, multiprocessing, fallback]
    category_id: software_development
    subcategory_id: robustness
    knowledge_level: intermediate
    implementation_level: independent
    professional_experience_level: none
    production_experience: false
    experience_contexts: [academic]
    evidence_strength: strong_summary
    evidence:
      - project_id: project_rag_empresarial_tfg
        document_type: summary
        section_titles: [Tecnologías algoritmos y conocimientos aplicados]
        evidence_type: implementation
        description: Reintentos con Tenacity ante errores transitorios de OpenAI.
      - project_id: project_cubo_rubik_busqueda_estados
        document_type: summary
        section_titles: [Tecnologías algoritmos y conocimientos aplicados]
        evidence_type: implementation
        description: Timeout por experimento con multiprocessing.
    can_claim:
      - Ha aplicado reintentos, timeouts y fallback en proyectos académicos/prototipos.
    cannot_claim:
      - No afirmar operación SRE o alta disponibilidad en producción.
    known_limitations: [Prototipos y prácticas]
    related_technology_ids: [python]

  - skill_id: skill_rdf_sparql
    name: RDF y SPARQL
    aliases: [RDF, Turtle, SPARQL SELECT, SPARQL CONSTRUCT, SPARQL SERVICE]
    category_id: semantic_data
    subcategory_id: semantic_query
    knowledge_level: intermediate_high
    implementation_level: independent
    professional_experience_level: none
    production_experience: false
    experience_contexts: [academic]
    evidence_strength: strong_summary
    evidence:
      - project_id: project_web_semantica_rdf_sparql_jena
        document_type: summary
        section_titles: [Tecnologías algoritmos y conocimientos aplicados]
        evidence_type: implementation
        description: Modelado RDF, Turtle, SPARQL SELECT/CONSTRUCT/SERVICE, OPTIONAL, UNION, FILTER, BIND y agregaciones.
    can_claim:
      - Ha modelado y consultado grafos RDF con SPARQL en prácticas académicas.
    cannot_claim:
      - No afirmar administración productiva de knowledge graphs empresariales.
    known_limitations: [Contexto académico en equipo]
    related_technology_ids: [rdf, rdfs, sparql]

  - skill_id: skill_apache_jena
    name: Apache Jena y Fuseki
    aliases: [Apache Jena, Jena, Fuseki, TDB2, Jena ARQ]
    category_id: semantic_data
    subcategory_id: semantic_tooling
    knowledge_level: intermediate_high
    implementation_level: independent
    professional_experience_level: none
    production_experience: false
    experience_contexts: [academic]
    evidence_strength: strong_summary
    evidence:
      - project_id: project_web_semantica_rdf_sparql_jena
        document_type: summary
        section_titles: [Tecnologías algoritmos y conocimientos aplicados]
        evidence_type: integration
        description: Modelos RDF, lectura Turtle, consultas, inferencia, serialización, Fuseki y TDB2.
    can_claim:
      - Ha usado Apache Jena y Fuseki para prácticas de grafos RDF.
    cannot_claim:
      - No afirmar operación productiva de servidores Fuseki.
    known_limitations: [Contexto académico]
    related_technology_ids: [apache_jena, fuseki, java]

  - skill_id: skill_modelado_semantico
    name: Modelado semántico
    aliases: [RDFS, FOAF, WGS84 Geo, Linked Open Data, Wikidata, DBpedia]
    category_id: semantic_data
    subcategory_id: semantic_modeling
    knowledge_level: intermediate_high
    implementation_level: independent
    professional_experience_level: none
    production_experience: false
    experience_contexts: [academic]
    evidence_strength: strong_summary
    evidence:
      - project_id: project_web_semantica_rdf_sparql_jena
        document_type: summary
        section_titles: [Tecnologías algoritmos y conocimientos aplicados]
        evidence_type: academic_usage
        description: FOAF, WGS84 Geo, RDFS, Wikidata, DBpedia y Linked Open Data.
    can_claim:
      - Ha reutilizado vocabularios estándar y fuentes Linked Open Data en prácticas.
    cannot_claim:
      - No afirmar diseño de una ontología empresarial productiva.
    known_limitations: [Contexto académico]
    related_technology_ids: [rdfs, wikidata, dbpedia]

  - skill_id: skill_pandas_datos
    name: Análisis tabular con pandas
    aliases: [pandas, CSV, limpieza tabular, metadatos]
    category_id: software_development
    subcategory_id: data_processing
    knowledge_level: intermediate
    implementation_level: independent
    professional_experience_level: none
    production_experience: false
    experience_contexts: [academic]
    evidence_strength: strong_summary
    evidence:
      - project_id: project_recuperacion_informacion
        document_type: summary
        section_titles: [Tecnologías algoritmos y conocimientos aplicados]
        evidence_type: academic_usage
        description: Representación tabular de documentos, limpieza, metadatos y persistencia CSV.
    can_claim:
      - Ha usado pandas para estructurar documentos y metadatos en prácticas de recuperación.
    cannot_claim:
      - No afirmar experiencia profesional de analítica de datos.
    known_limitations: [Contexto académico]
    related_technology_ids: [pandas, python]

  - skill_id: skill_lustre
    name: Lustre y programación síncrona
    aliases: [Lustre, sistemas reactivos, operador pre de Lustre, map red Lustre, máquina de estados síncrona]
    category_id: reactive_concurrent_systems
    subcategory_id: synchronous_programming
    knowledge_level: intermediate
    implementation_level: independent
    professional_experience_level: none
    production_experience: false
    experience_contexts: [academic]
    evidence_strength: strong_summary
    evidence:
      - project_id: project_sistemas_reactivos
        document_type: summary
        section_titles: [Tecnologías algoritmos y conocimientos aplicados]
        evidence_type: implementation
        description: Nodos Lustre para semáforos, cámaras de temperatura, historial y sistema de frío.
    can_claim:
      - Ha usado Lustre para modelar sistemas reactivos deterministas en prácticas.
    cannot_claim:
      - No afirmar uso industrial de Lustre.
    known_limitations: [Contexto académico]
    related_technology_ids: [lustre]

  - skill_id: skill_concurrencia_go
    name: Concurrencia en Go
    aliases: [goroutines, channels, WaitGroup, select, ticker, workers Go]
    category_id: reactive_concurrent_systems
    subcategory_id: go_concurrency
    knowledge_level: intermediate
    implementation_level: independent
    professional_experience_level: none
    production_experience: false
    experience_contexts: [academic]
    evidence_strength: strong_summary
    evidence:
      - project_id: project_sistemas_reactivos
        document_type: summary
        section_titles: [Tecnologías algoritmos y conocimientos aplicados]
        evidence_type: implementation
        description: Goroutines, channels, WaitGroup, productores/consumidores, workers, ticker y select.
    can_claim:
      - Ha implementado patrones básicos y medios de concurrencia en Go en prácticas.
    cannot_claim:
      - No afirmar experiencia profesional en sistemas concurrentes de producción.
    known_limitations: [Contexto académico]
    related_technology_ids: [go, goroutines, channels]

  - skill_id: skill_diseno_modular
    name: Diseño modular
    aliases: [arquitectura modular, separación de responsabilidades, capas, contratos]
    category_id: professional_practice
    subcategory_id: architecture
    knowledge_level: advanced
    implementation_level: advanced_applied
    professional_experience_level: none
    production_experience: false
    experience_contexts: [academic, personal]
    evidence_strength: strong_summary
    evidence:
      - project_id: project_rag_empresarial_tfg
        document_type: summary
        section_titles: [Arquitectura y partes principales]
        evidence_type: implementation
        description: Separación por ingesta, chunking, indexación, retrieval, generación, CLI e interfaz.
      - project_id: project_conecta4_minimax_alfabeta
        document_type: summary
        section_titles: [Arquitectura y partes principales]
        evidence_type: implementation
        description: Separación entre tablero, jugador, estrategia, evaluador y experimentos.
      - project_id: project_cubo_rubik_busqueda_estados
        document_type: summary
        section_titles: [Arquitectura y partes principales]
        evidence_type: implementation
        description: Separación entre dominio, problema, nodos y algoritmos de búsqueda.
      - project_id: project_web_semantica_rdf_sparql_jena
        document_type: summary
        section_titles: [Arquitectura y partes principales]
        evidence_type: academic_usage
        description: Separación de datasets, consultas, razonamiento, resultados y servicios.
    can_claim:
      - Tiende a estructurar proyectos por responsabilidades, contratos y fases.
    cannot_claim:
      - No presentar esta habilidad como experiencia profesional de arquitectura empresarial.
    known_limitations: [Evidencia académica y de proyectos documentados]
    related_technology_ids: [python, java, pydantic]

  - skill_id: skill_experimentacion
    name: Experimentación técnica
    aliases: [comparativas técnicas, logs experimentales, evaluación reproducible, análisis experimental]
    category_id: professional_practice
    subcategory_id: experimentation
    knowledge_level: intermediate_high
    implementation_level: independent
    professional_experience_level: none
    production_experience: false
    experience_contexts: [academic]
    evidence_strength: strong_summary
    evidence:
      - project_id: project_conecta4_minimax_alfabeta
        document_type: summary
        section_titles: [Resultados y validación]
        evidence_type: evaluation
        description: 100 partidas por test, medición de nodos y tiempos.
      - project_id: project_cubo_rubik_busqueda_estados
        document_type: summary
        section_titles: [Tecnologías algoritmos y conocimientos aplicados]
        evidence_type: evaluation
        description: Métricas de tiempo, nodos y tamaño de ABIERTOS.
      - project_id: project_vision_artificial_video_temporalidad
        document_type: summary
        section_titles: [Resultados y validación]
        evidence_type: evaluation
        description: Logs de entrenamiento y sanity runs descritos.
    can_claim:
      - Ha medido y comparado algoritmos con métricas en proyectos académicos.
    cannot_claim:
      - No afirmar evaluación productiva o A/B testing profesional.
    known_limitations: [Evaluación académica]
    related_technology_ids: [python, java]

  - skill_id: skill_documentacion_tecnica
    name: Documentación técnica para recuperación
    aliases: [documentación técnica, documentación para RAG, summaries, advanced docs, trazabilidad]
    category_id: professional_practice
    subcategory_id: technical_documentation
    knowledge_level: advanced
    implementation_level: independent
    professional_experience_level: none
    production_experience: false
    experience_contexts: [personal, academic]
    evidence_strength: strong_summary
    evidence:
      - project_id: project_rag_empresarial_tfg
        document_type: summary
        section_titles: [Presentación del proyecto]
        evidence_type: implementation
        description: Documentación trazable, chunks, fuentes y control de evidencia en el sistema RAG.
      - project_id: project_mineria_textos
        document_type: summary
        section_titles: [Presentación del proyecto]
        evidence_type: academic_usage
        description: Documentación de prácticas y pipelines de texto.
      - project_id: project_vision_artificial_fundamentos
        document_type: summary
        section_titles: [Presentación del proyecto]
        evidence_type: academic_usage
        description: Documentación de prácticas de visión artificial.
    can_claim:
      - Ha estructurado documentación técnica para que sea trazable y recuperable.
    cannot_claim:
      - No afirmar que todos los documentos advanced están disponibles en esta carpeta.
    known_limitations: [En esta carpeta solo están disponibles los summaries]
    related_technology_ids: [python]
```

## Nota para mantenimiento humano

La fuente de verdad estructurada está en el bloque YAML anterior. Para responder entrevistas, el asistente debe cruzar `skills[].evidence[].project_id` con `Indice_de_proyectos.md` y recuperar el summary disponible antes de afirmar detalles.
