# Model Foundations and Inference Systems Resource Guide

Local lessons are sufficient to complete the module. External sources reinforce
the instruction and provide a checkable primary or practitioner reference; they
never replace the local explanation, practice, or answer key.

## Required authoritative spine

The required records are RES-02, RES-03, RES-05, RES-07, RES-09.
Every required record is free and has a local written alternative. All other
records below are optional enrichment and do not consume required module time.

| Week | Required resources | Assigned minutes |
|---:|---|---:|
| 65 | RES-02, RES-03 | 150 |
| 66 | RES-05 | 75 |
| 67 | RES-07 | 45 |
| 68 | RES-09 | 45 |

For each assigned source, preserve the requested evidence, one transfer limit,
and one observation that would falsify the claim. A required source that is
temporarily unavailable is replaced by its local alternative and the same evidence
task; record the substitution.

## Resource records

### RES-02: Attention Is All You Need

- **Author/publisher:** Ashish Vaswani et al.
- **URL:** https://arxiv.org/abs/1706.03762
- **Type/status:** original research paper; Required
- **Access:** free
- **Week/time:** Week 65; 60 minutes assigned
- **Purpose:** Connect the local attention implementation to the original transformer mechanism and notation.
- **Boundary and evidence:** Read Sections 3.1-3.5 only; annotate tensor shapes, scaling, masking, and parallelism claims.
- **Local alternative:** [lessons/02-tokens-embeddings-attention.md](lessons/02-tokens-embeddings-attention.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-03: CS336: Language Modeling from Scratch

- **Author/publisher:** Stanford University
- **URL:** https://cs336.stanford.edu/
- **Type/status:** course materials; Required
- **Access:** free
- **Week/time:** Week 65; 90 minutes assigned
- **Purpose:** Reinforce tokenization, resource accounting, architectures, hardware, and current inference-system reasoning.
- **Boundary and evidence:** Use only Lectures 1-5 and 10 materials; separate token, operator, memory, hardware, and serving claims in a concept ledger.
- **Local alternative:** [lessons/03-transformer-inference-path.md](lessons/03-transformer-inference-path.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-05: Efficient Memory Management for Large Language Model Serving with PagedAttention

- **Author/publisher:** Woosuk Kwon et al. / SOSP
- **URL:** https://arxiv.org/abs/2309.06180
- **Type/status:** original systems paper; Required
- **Access:** free
- **Week/time:** Week 66; 75 minutes assigned
- **Purpose:** Study KV-cache allocation, fragmentation, batching, scheduling, and their workload assumptions.
- **Boundary and evidence:** Read Sections 2-4 and 7; reproduce the fragmentation argument and list the assumptions that differ from Atlas.
- **Local alternative:** [lessons/04-compute-memory-capacity.md](lessons/04-compute-memory-capacity.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-07: PyTorch Profiler

- **Author/publisher:** PyTorch project
- **URL:** https://docs.pytorch.org/tutorials/recipes/recipes/profiler_recipe.html
- **Type/status:** maintainer tutorial; Required
- **Access:** free
- **Week/time:** Week 67; 45 minutes assigned
- **Purpose:** Define timing, shape, memory, warm-up, and trace-export evidence for the optional adapter.
- **Boundary and evidence:** Read timing, memory, trace, and long-running sections; write the Atlas measured-profile procedure and its overhead boundary.
- **Local alternative:** [lessons/05-profiling-inference-metrics.md](lessons/05-profiling-inference-metrics.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-09: Taming the tail utilization of ads inference at Meta scale

- **Author/publisher:** Meta Engineering
- **URL:** https://engineering.fb.com/2024/07/10/production-engineering/tail-utilization-ads-inference-meta/
- **Type/status:** first-person engineering case; Required
- **Access:** free
- **Week/time:** Week 68; 45 minutes assigned
- **Purpose:** Examine operator evidence connecting tail utilization, capacity, reliability, and user latency.
- **Boundary and evidence:** Read the full case; separate measurements, interventions, outcomes, scale assumptions, and claims that do not transfer to generative Atlas workloads.
- **Local alternative:** [lessons/08-atlas-inference-decision.md](lessons/08-atlas-inference-decision.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-01: Deep Learning: Chapters 2-4 bounded sections

- **Author/publisher:** Ian Goodfellow, Yoshua Bengio, Aaron Courville / MIT Press
- **URL:** https://www.deeplearningbook.org/
- **Type/status:** free online textbook; Optional enrichment
- **Access:** free
- **Week/time:** Week 65; 90 minutes optional
- **Purpose:** Ground linear algebra, probability, entropy, gradients, and numerical stability used in local derivations.
- **Boundary and evidence:** Read Chapter 2 Sections 2.1-2.5, Chapter 3 Sections 3.1-3.4 and 3.13, and Chapter 4 Sections 4.1-4.3; reproduce one matrix, entropy, and gradient calculation.
- **Local alternative:** [lessons/01-mathematics-for-inference.md](lessons/01-mathematics-for-inference.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-04: CS336 Lecture 10: Inference

- **Author/publisher:** Stanford Online
- **URL:** https://www.youtube.com/watch?v=fcgPYo3OtV0
- **Type/status:** captioned technical video; Optional enrichment
- **Access:** free
- **Week/time:** Week 66; 75 minutes optional
- **Purpose:** Visualize prefill, decode, batching, and serving trade-offs with a written equivalent.
- **Boundary and evidence:** Watch with captions; produce a prefill/decode/batching map and two claims that do not transfer to the Atlas portable CPU lab.
- **Local alternative:** [lessons/03-transformer-inference-path.md](lessons/03-transformer-inference-path.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-06: Optimization and Tuning

- **Author/publisher:** vLLM project
- **URL:** https://docs.vllm.ai/en/latest/configuration/optimization/
- **Type/status:** maintainer documentation; Optional enrichment
- **Access:** free
- **Week/time:** Week 67; 45 minutes optional
- **Purpose:** Compare current preemption, chunked-prefill, and input-processing controls with the local scheduler model.
- **Boundary and evidence:** Read preemption, chunked prefill, and input processing only; map each current control to the Atlas failure it could affect.
- **Local alternative:** [lessons/06-scheduling-admission-fairness.md](lessons/06-scheduling-admission-fairness.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-08: SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models

- **Author/publisher:** Guangxuan Xiao et al.
- **URL:** https://arxiv.org/abs/2211.10438
- **Type/status:** original research paper; Optional enrichment
- **Access:** free
- **Week/time:** Week 67; 60 minutes optional
- **Purpose:** Tie numerical representation changes to both hardware efficiency and protected quality evidence.
- **Boundary and evidence:** Read Sections 1-4 and 5.3-5.5; identify the precision, hardware, corpus, and metric boundaries behind each claim.
- **Local alternative:** [lessons/07-caches-quantization-failover.md](lessons/07-caches-quantization-failover.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

Do not copy articles, chapters, slides, or transcripts into learner artifacts.
Use short attributed quotations only when necessary and otherwise paraphrase with
the source ID, exact section boundary, and stated evidence limit.

## PESD 2.0 primary anchors

- [NIST AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) — NIST AIRC; required, free, 20 minutes; Read Govern 1.5–1.7 and Manage 3–4; map inventory, monitoring, supplier, incident, recovery, and decommission outcomes into the dossier. Local alternative: Lesson 8 PESD 2.0 extension. Last verified 2026-08-04.

For each source, submit the named control/evidence mapping and applicability or
scope uncertainty. A framework name is not evidence of implementation or legal
compliance.
