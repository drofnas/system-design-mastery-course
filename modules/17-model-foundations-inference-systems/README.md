# Module 17: Model Foundations and Inference Systems

> **Authoring status:** Review. PESD 2.0 content and machine-readable contracts are migrated. Refreshed evaluator calibration, full platform matrices, offline reruns, cleanup checks, and timed learner pilots remain required before Ready.

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

The 10–12 hour weekly figure is a capacity envelope. Core work is deliberately
budgeted below that ceiling; unused time is recovery buffer, not hidden work.

### Week 92: Model and derive — 8.5 hours

| Work | Time |
|---|---:|
| Bounded authoritative resources | 180 min |
| Local mechanism instruction | 120 min |
| Guided practice | 60 min |
| Required evidence components | 30 min |
| Model and derive core work | 120 min |

Optional contingency capacity: 210 minutes. It is not core work, carries no required evidence, and may remain unused.

### Week 93: Guided build and prediction freeze — 9 hours

| Work | Time |
|---|---:|
| Bounded authoritative resources | 155 min |
| Local mechanism instruction | 120 min |
| Guided practice | 60 min |
| Required evidence components | 30 min |
| Guided build and prediction freeze core work | 175 min |

Optional contingency capacity: 180 minutes. It is not core work, carries no required evidence, and may remain unused.

### Week 94: Independent build and integration — 10 hours

| Work | Time |
|---|---:|
| Required evidence components | 60 min |
| Independent build and integration core work | 540 min |

Optional contingency capacity: 120 minutes. It is not core work, carries no required evidence, and may remain unused.

### Week 95: Independent build and integration II — 10 hours

| Work | Time |
|---|---:|
| Independent build and integration II core work | 540 min |
| Independent build and integration II verification checkpoint | 60 min |

Optional contingency capacity: 120 minutes. It is not core work, carries no required evidence, and may remain unused.

### Week 96: Break, repair, measure, and diagnose — 10 hours

| Work | Time |
|---|---:|
| Required evidence components | 120 min |
| Break, repair, measure, and diagnose core work | 480 min |

Optional contingency capacity: 120 minutes. It is not core work, carries no required evidence, and may remain unused.

### Week 97: Decide, teach, assess, and freeze — 9.5 hours

| Work | Time |
|---|---:|
| Required evidence components | 120 min |
| Decide, teach, assess, and freeze core work | 390 min |
| Module teach-back | 30 min |
| Learning log and freeze check | 30 min |

Optional contingency capacity: 150 minutes. It is not core work, carries no required evidence, and may remain unused.
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
- Gate 6 runs in Week 103 after Module 18; Module 17 creates inputs but no duplicate final capstone defense submission.

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

A frozen self-evaluation may establish **Solo Complete**; independent human or LLM review may establish **Independently Validated**. Synthetic lab values are not production measurements.

## PESD 2.0 scope addition

This 6-week module schedules 57 core hours. Its primary
decision is ADR A12. The added graded scope is
an actual streaming tiny-transformer path with incremental KV state, token scheduling, byte-budget admission, tenant/version cache identity, bounded provider failure, profiling, and an AI System Dossier. See Lesson 8, the final guided exercise, final worksheet,
rubric anchors, and remediation map for the integrated evidence contract.
