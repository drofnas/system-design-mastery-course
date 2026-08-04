# Module 18 Resource Guide

Local lessons are sufficient for required work. External sources provide
original notation, broader datasets, maintainer behavior, and operating
experience. All required sources were free on 2026-08-03. Recheck access before
assigning them; record a dated note rather than silently changing the boundary.

## Week 69

### RES-01: Introduction to Information Retrieval, Chapters 6 and 8

- **Authors/publisher:** Christopher D. Manning, Prabhakar Raghavan, Hinrich Schütze / Stanford University
- **URL/type/status:** <https://nlp.stanford.edu/IR-book/>; free online textbook; required
- **Boundary/time:** Chapter 6 Sections 6.1–6.2 and Chapter 8 Sections 8.1–8.4; 90 minutes
- **Purpose:** derive probabilistic ranking and evaluate ranked results from explicit judgments
- **Produce:** one BM25 calculation, one nDCG calculation, and the judgment assumption behind each
- **Local alternative:** Lessons 1–2
- **Reflection:** Which product failure can Recall@k expose that nDCG can hide? Which cannot either metric expose?

### RES-02: Efficient and robust approximate nearest neighbor search using HNSW

- **Authors/publisher:** Yu. A. Malkov and D. A. Yashunin
- **URL/type/status:** <https://arxiv.org/abs/1603.09320>; original paper; free; required
- **Boundary/time:** Sections 1–4; 75 minutes
- **Purpose:** connect graph layers and search/construction work to recall and memory
- **Produce:** an annotated insertion/search path and a table for `M`, `efConstruction`, and `efSearch`
- **Local alternative:** Lesson 3 and the portable HNSW implementation
- **Reflection:** Which paper claim cannot be tested on five CivicAid vectors, and what larger experiment would test it?

### RES-03: BEIR

- **Authors/publisher:** Nandan Thakur et al.
- **URL/type/status:** <https://arxiv.org/abs/2104.08663>; original paper; free; required
- **Boundary/time:** Sections 3, 4, and 7; 60 minutes
- **Purpose:** expose domain shift, relevance-judgment, and benchmark-selection limits
- **Produce:** lexical/dense/reranker comparison plus two relevant dataset biases
- **Local alternative:** Lessons 1 and 4
- **Reflection:** Why can a model win on one corpus and still be an unsafe default for permit guidance?

### RES-08: HNSW for Vector Search Explained and Implemented with Faiss

- **Author/publisher:** James Briggs / Pinecone
- **URL/type/status:** <https://www.youtube.com/watch?v=QvKMwLjdK-s>; technical video; free; required
- **Boundary/time:** 00:41–33:33; 40 minutes
- **Purpose:** visualize layer construction and tuning before reading the lab
- **Produce:** one drawn search path and a claim-by-claim comparison with RES-02
- **Captions/equivalent:** YouTube caption availability can vary by locale and playback mode; Lesson 3 is the complete required written equivalent and must be offered without penalty
- **Reflection:** Which simplifications in a visualization could cause a false operational conclusion?

## Week 70

### RES-04: Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks

- **Authors/publisher:** Patrick Lewis et al.
- **URL/type/status:** <https://arxiv.org/abs/2005.11401>; original paper; free; required
- **Boundary/time:** Introduction and Sections 2–4; 60 minutes
- **Purpose:** distinguish parametric generation from explicit non-parametric evidence
- **Produce:** a data-flow map for retrieval, conditioning, generation, provenance, and update
- **Local alternative:** Lesson 5
- **Reflection:** Why does inspectable evidence improve reviewability without proving every generated claim?

### RES-05: LLM Prompt Injection Prevention Cheat Sheet

- **Publisher:** OWASP Cheat Sheet Series
- **URL/type/status:** <https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html>; security guidance; free; required
- **Boundary/time:** indirect injection, RAG poisoning, agent-specific attacks, least privilege, and testing; 50 minutes
- **Purpose:** move safety from prompt wording into deterministic system boundaries
- **Produce:** threat/control/residual-risk map with one enforcement owner per control
- **Local alternative:** Lesson 6
- **Reflection:** Which attacks can input filtering reduce, and which still require tool authorization and approval?

### RES-06: AI Agent Reference Architecture

- **Publisher:** Temporal Technologies
- **URL/type/status:** <https://go.temporal.io/platform-hub/ai-engineering/ai-reference-architecture>; maintainer guide; free; required
- **Boundary/time:** architecture overview, orchestrator, activities, and approval; 50 minutes
- **Purpose:** study replay-safe boundaries for nondeterministic providers and side effects
- **Produce:** a general-principle/vendor-mechanism table and one replay history
- **Local alternative:** Lesson 7 and the portable workflow journal
- **Reflection:** Why must a provider response be recorded as an activity result instead of recomputed during replay?

## Week 72

### RES-07: Using LLMs to amplify human labeling and improve Dash search relevance

- **Publisher:** Dropbox Engineering
- **URL/type/status:** <https://dropbox.tech/machine-learning/llm-human-labeling-improving-search-relevance-dropbox-dash>; first-person case; free; required
- **Boundary/time:** full article; 45 minutes
- **Purpose:** connect retrieval judgments, human review, ranking evidence, and production decisions
- **Produce:** measurements/interventions/limits table and three transfer conditions
- **Local alternative:** Lesson 8
- **Reflection:** Where may machine-assisted labels help, and where must independent human judgment remain authoritative?

## Source and license notes

The course links to external work but does not reproduce papers, articles, or
video scripts. Local explanations and fixtures are original course material.
External sources retain their own copyright and license terms.
