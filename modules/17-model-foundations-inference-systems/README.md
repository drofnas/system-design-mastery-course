# Module 17: Model Foundations and Inference Systems

> **Authoring status:** Ready. The portable CPU lab, F01–F06 pairs, six isolated
> evaluator records, deterministic calibration, semantic/resource review, and
> focused/full validation all pass.

## What this module changes

An inference API is a resource allocator wrapped around a probabilistic program.
Its useful capacity depends on prompt and output length, weight and key/value
memory, prefill and decode work, batching, queue policy, numerical precision,
cache identity, and provider behavior. This module teaches you to derive those
mechanisms, expose them in a small implementation, and defend a serving design
with measured limits rather than model or accelerator labels.

The continuing non-capstone case is the **Atlas Museum Exhibit Label Service**.
Four museums request interactive previews and overnight batches of draft exhibit
labels. The case has no products, inventory, checkout, retrieval index, grounded
answers, or agent tools. Freeze independent commerce inference decisions before
opening the completed Atlas case or answer key.

## Prerequisites

- Modules 1–16, especially capacity, systems, observability, deadlines,
  security, architecture evolution, and execution models
- Python 3.11+ for the required lab; no model download or accelerator required
- Optional PyTorch installation for operator profiling on CPU or an available
  accelerator; optional results never replace required portable evidence
- Preserved capstone baselines and Gate 5 evidence; this module does not rewrite them

## Learning outcomes

By the end of the module, you can:

1. Derive the mathematical operations that shape transformer inference.
2. Implement tokenization, embeddings, attention, and a tiny generation path.
3. Calculate weight, activation, KV-cache, bandwidth, concurrency, and unit cost.
4. Measure prefill, decode, TTFT, inter-token latency, throughput, and memory.
5. Design bounded batching, admission, quotas, and traffic-class fairness.
6. Operate versioned caches and precision changes within privacy and quality bounds.
7. Diagnose memory, scheduling, overload, cache, precision, and provider failures.
8. Defend an inference architecture across quality, reliability, security, cost,
   ownership, migration, and reversal.

## Schedule

### Week 65: Model and freeze inference predictions — 11 hours

| Work | Time |
|---|---:|
| Lessons 1–4 and bounded sources | 4 h |
| EX-01–EX-09 with Atlas calculations | 2.5 h |
| Independent capacity, quality, and F01–F06 baseline | 3 h |
| Freeze, self-check, and learning log | 1.5 h |

Use the [Week 65 worksheet](worksheets/week-65-inference-model.md).

### Week 66: Build the transformer and serving contract — 12 hours

| Work | Time |
|---|---:|
| Lessons 2–5 and Atlas tutorial | 2.5 h |
| EX-05–EX-12 with conformance rehearsal | 2 h |
| Independent tensor, model, and server implementation | 6.5 h |
| Internals review and learning log | 1 h |

Use the [Week 66 worksheet](worksheets/week-66-inference-build.md).

### Week 67: Break and measure inference assumptions — 12 hours

| Work | Time |
|---|---:|
| Lessons 4–7 and bounded sources | 2 h |
| EX-10–EX-17 and experiment rehearsal | 2 h |
| F01–F06 broken/repaired trials and CPU profile | 6 h |
| Failure matrix, performance report, and cost model | 2 h |

Use the [Week 67 worksheet](worksheets/week-67-inference-failures.md).

### Week 68: Decide, teach, assess, and remediate — 11 hours

| Work | Time |
|---|---:|
| Lesson 8, practitioner case, and EX-18 | 1.5 h |
| Inference RFC, deployment-policy ADR, and architecture defense | 4 h |
| Module evaluation and teach-back | 2 h |
| Separate remediation and learning log | 3.5 h |

Use the [Week 68 worksheet](worksheets/week-68-inference-defense.md).

## Learn

1. [Mathematics for inference decisions](lessons/01-mathematics-for-inference.md)
2. [Tokens, embeddings, and attention](lessons/02-tokens-embeddings-attention.md)
3. [Transformer inference from prefill to decode](lessons/03-transformer-inference-path.md)
4. [Compute, memory, and capacity accounting](lessons/04-compute-memory-capacity.md)
5. [Profiling and inference metrics](lessons/05-profiling-inference-metrics.md)
6. [Scheduling, batching, admission, and fairness](lessons/06-scheduling-admission-fairness.md)
7. [Caches, quantization, and provider failure](lessons/07-caches-quantization-failover.md)
8. [Atlas tutorial, architecture decision, and teach-back](lessons/08-atlas-inference-decision.md)

Use the [glossary](glossary.md), [resource guide](resources.md), and
[lab interface](lab/README.md) as references after studying the mechanisms.

## Practice and independent evidence

- Freeze A01 before the completed [Atlas case](case-study/atlas-museum-service.md).
- Complete the [guided exercises](exercises/exercises.md) before opening the
  [explained answers](exercises/answer-key.md).
- Run the deterministic model and measured CPU path in the [inference lab](lab/README.md).
  Preserve scenario, input, configuration, environment, and output hashes.
- Treat accelerator results as environment-bound. Modelled trials prove contract
  logic, not real device performance; measured CPU results do not predict a GPU.
- Preserve frozen predictions and raw trials. Corrections belong in dated addenda.

This module contributes one substantial RFC, one capacity-and-cost model, one
performance investigation, one failure matrix, one source-code internals review,
one inference-deployment policy ADR, and one recorded architecture teach-back.

## Assessment and completion

- Read the [assessment contract](assessment/README.md), [anchored rubric](assessment/rubric.md),
  [evaluator prompt](assessment/evaluator-prompt.md), [remediation map](assessment/remediation-map.md),
  and [readiness review](assessment/semantic-readiness-review.md).
- Pass G01–G06, average at least 3.0, and avoid a zero in R05, R06, R08, or R09.
- Gate 6 occurs in Week 72 after Module 18; Module 17 creates inputs but no final
  capstone defense submission.

## Evidence boundary and AI use

The portable model exposes shapes, arithmetic, causal masking, KV growth,
scheduling, hashes, bounds, and controlled numerical error. It cannot establish
large-model quality, production accelerator utilization, vendor pricing,
population percentiles, or provider equivalence. Optional profiles must name the
exact host, device, runtime, warm-up, repetitions, and changed evidence boundary.

AI may challenge calculations, hypotheses, experiment design, and alternatives.
It may not choose the graded architecture, invent measurements, rewrite frozen
work, produce replacement graded answers, or answer during the defense.

## Course-wide completion contracts

- The machine-readable `module.json` time blocks are the canonical required-work budget.
- The [factual-claims ledger](assessment/factual-claims.json) maps each local lesson to its authoritative source boundary.
- Use the [provider-neutral evaluation workflow](../../EVALUATION_GUIDE.md) only after learner evidence is committed.
- Use the [sealed local gate workflow](../../SOLO_GATE_GUIDE.md) when a course gate applies. Human review is optional.

Self-scoring is provisional and cannot establish Pass. Synthetic lab values are not production measurements.
