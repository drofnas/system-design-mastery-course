# Retrieval, RAG, Agents, and Optional Project Defense Resource Guide

Local lessons are sufficient to complete the module. External sources reinforce
the instruction and provide a checkable primary or practitioner reference; they
never replace the local explanation, practice, or answer key.

## Required authoritative spine

The required records are RES-01, RES-02, RES-04, RES-05, RES-09, RES-10.
Every required record is free and has a local written alternative. All other
records below are optional enrichment and do not consume required module time.

| Week | Required resources | Assigned minutes |
|---:|---|---:|
| 98 | RES-01, RES-05, RES-10 | 160 |
| 99 | RES-02, RES-04, RES-09 | 155 |

For each assigned source, preserve the requested evidence, one transfer limit,
and one observation that would falsify the claim. A required source that is
temporarily unavailable is replaced by its local alternative and the same evidence
task; record the substitution.

## Resource records

### RES-01: Introduction to Information Retrieval, Chapters 6 and 8

- **Author/publisher:** Christopher D. Manning, Prabhakar Raghavan, Hinrich Schütze / Stanford University
- **URL:** https://nlp.stanford.edu/IR-book/
- **Type/status:** free online textbook; Required
- **Access:** free
- **Lesson/time:** the relevant lesson; 90 minutes assigned
- **Purpose:** Ground probabilistic ranking and empirical retrieval evaluation.
- **Boundary and evidence:** Read Chapter 6 Sections 6.1-6.2 and Chapter 8 Sections 8.1-8.4; derive one BM25 score and one nDCG example, then name the judgment assumption behind each.
- **Local alternative:** [lessons/01-retrieval-contracts-evaluation.md](lessons/01-retrieval-contracts-evaluation.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-02: Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs

- **Author/publisher:** Yu. A. Malkov and D. A. Yashunin
- **URL:** https://arxiv.org/abs/1603.09320
- **Type/status:** original research paper; Required
- **Access:** free
- **Lesson/time:** the relevant lesson; 75 minutes assigned
- **Purpose:** Connect the portable index to HNSW layers, graph navigation, construction, and recall/work controls.
- **Boundary and evidence:** Read Sections 1-4; annotate layer assignment, neighbor selection, efConstruction, efSearch, and claims that the small CivicAid lab cannot validate.
- **Local alternative:** [lessons/03-exact-ann-hnsw.md](lessons/03-exact-ann-hnsw.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-04: Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks

- **Author/publisher:** Patrick Lewis et al.
- **URL:** https://arxiv.org/abs/2005.11401
- **Type/status:** original research paper; Required
- **Access:** free
- **Lesson/time:** the relevant lesson; 60 minutes assigned
- **Purpose:** Separate parametric generation from inspectable non-parametric evidence and its provenance limits.
- **Boundary and evidence:** Read the introduction and Sections 2-4; trace retrieval, conditioning, provenance, and update assumptions into the CivicAid evidence envelope.
- **Local alternative:** [lessons/05-provenance-grounding-freshness.md](lessons/05-provenance-grounding-freshness.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-05: LLM Prompt Injection Prevention Cheat Sheet

- **Author/publisher:** OWASP Cheat Sheet Series
- **URL:** https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html
- **Type/status:** security guidance; Required
- **Access:** free
- **Lesson/time:** the relevant lesson; 50 minutes assigned
- **Purpose:** Model indirect injection, exfiltration, tool abuse, least privilege, and approval as system boundaries.
- **Boundary and evidence:** Read indirect injection, RAG poisoning, agent-specific attacks, least privilege, and testing sections; map each defense to a deterministic enforcement point and residual risk.
- **Local alternative:** [lessons/06-tools-authorization-prompt-injection.md](lessons/06-tools-authorization-prompt-injection.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-03: BEIR: A Heterogeneous Benchmark for Zero-shot Evaluation of Information Retrieval Models

- **Author/publisher:** Nandan Thakur et al.
- **URL:** https://arxiv.org/abs/2104.08663
- **Type/status:** original research paper; Optional enrichment
- **Access:** free
- **Lesson/time:** the relevant lesson; 60 minutes optional
- **Purpose:** Show why one in-domain result does not establish retrieval generalization.
- **Boundary and evidence:** Read Sections 3, 4, and 7; compare lexical, dense, and reranking evidence and list two dataset biases relevant to CivicAid.
- **Local alternative:** [lessons/04-hybrid-reranking-release-gates.md](lessons/04-hybrid-reranking-release-gates.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-06: AI Agent Reference Architecture

- **Author/publisher:** Temporal Technologies
- **URL:** https://go.temporal.io/platform-hub/ai-engineering/ai-reference-architecture
- **Type/status:** maintainer architecture guide; Optional enrichment
- **Access:** free
- **Lesson/time:** the relevant lesson; 50 minutes optional
- **Purpose:** Study recorded side effects, workflow replay, checkpoints, approvals, and nondeterministic provider boundaries.
- **Boundary and evidence:** Read architecture overview, orchestrator, activities, and human approval sections; identify which claims are general durable-execution principles and which depend on Temporal.
- **Local alternative:** [lessons/07-durable-agent-workflows.md](lessons/07-durable-agent-workflows.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-07: Using LLMs to amplify human labeling and improve Dash search relevance

- **Author/publisher:** Dropbox Engineering
- **URL:** https://dropbox.tech/machine-learning/llm-human-labeling-improving-search-relevance-dropbox-dash
- **Type/status:** first-person engineering case; Optional enrichment
- **Access:** free
- **Lesson/time:** the relevant lesson; 45 minutes optional
- **Purpose:** Examine how a production team connects retrieval judgments, human labels, search relevance, and grounded answers.
- **Boundary and evidence:** Read the full case; separate measured outcomes, labeling process, scale assumptions, and practices that do or do not transfer to CivicAid.
- **Local alternative:** [lessons/08-civicaid-decision-defense.md](lessons/08-civicaid-decision-defense.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-08: HNSW for Vector Search Explained and Implemented with Faiss

- **Author/publisher:** James Briggs / Pinecone
- **URL:** https://www.youtube.com/watch?v=QvKMwLjdK-s
- **Type/status:** technical video with written equivalent; Optional enrichment
- **Access:** free
- **Lesson/time:** the relevant lesson; 40 minutes optional
- **Purpose:** Visualize HNSW layers, navigation, construction, and tuning before inspecting the portable implementation.
- **Boundary and evidence:** Watch 00:41-33:33; draw one search path and compare each tuning claim with the original paper and local Lesson 3. Use the local lesson if video access or captions are unsuitable.
- **Local alternative:** [lessons/03-exact-ann-hnsw.md](lessons/03-exact-ann-hnsw.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

Do not copy articles, chapters, slides, or transcripts into learner artifacts.
Use short attributed quotations only when necessary and otherwise paraphrase with
the source ID, exact section boundary, and stated evidence limit.
