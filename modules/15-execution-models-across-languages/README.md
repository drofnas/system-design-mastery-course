# Module 15: Execution Models Across Languages

> **Authoring status:** Review. PESD 2.0 content and machine-readable contracts are migrated. Refreshed evaluator calibration, full platform matrices, offline reruns, cleanup checks, and timed learner pilots remain required before Ready.

## What this module changes

A language name does not tell you where work runs, when memory is released, or
what survives a boundary. This module teaches you to trace each request through
the scheduler, lifetime, cancellation, synchronization, and validation rules
that govern it. You will implement one bounded contract four times, measure
equivalent work, break runtime-specific assumptions, and choose from evidence.

The continuing non-capstone case is the **Northstar Observatory Observation
Enrichment Gateway**. It gathers ephemeris, weather, calibration, and quality
evidence for one observation. It contains no products, merchants, inventory,
checkout, payments, orders, or commerce architecture. Freeze independent
commerce decisions before opening the completed case or answer key.

## Prerequisites

- Modules 1–14, especially capacity, profiling, deadlines, concurrency,
  reliability, security boundaries, migration, cost, and ownership
- Docker 29 or equivalent container support; native substitutions are allowed
  when their versions and changed evidence boundary are recorded
- Python 3.11+ for the harness; Python is not a fifth service implementation
- Ability to read TypeScript, Go, Rust, and Java with language references
- Preserved Module 13 and 14 evidence; Gate 5 reviews it without rewriting it

## Learning outcomes

By the end of the module, you can:

1. Compare lifetime and memory-management models from observable consequences.
2. Trace work through OS threads and language-runtime schedulers.
3. Implement equivalent bounded fan-out in TypeScript, Go, Rust, and Java.
4. Measure latency, useful throughput, memory, allocation, and GC fairly.
5. Diagnose visibility and race failures with happens-before evidence.
6. Preserve meaning across static, dynamic, process, and JSON boundaries.
7. Diagnose F01–F09 while bounding operations, security, cost, and ownership.
8. Defend and teach a runtime choice, then complete Gate 5.

## Schedule

The 10–12 hour weekly figure is a capacity envelope. Core work is deliberately
budgeted below that ceiling; unused time is recovery buffer, not hidden work.

### Week 80: Model and derive — 8.5 hours

| Work | Time |
|---|---:|
| Bounded authoritative resources | 115 min |
| Local mechanism instruction | 120 min |
| Guided practice | 60 min |
| Model and derive core work | 215 min |

### Week 81: Guided build and prediction freeze — 9 hours

| Work | Time |
|---|---:|
| Bounded authoritative resources | 115 min |
| Local mechanism instruction | 120 min |
| Guided practice | 60 min |
| Required evidence components | 120 min |
| Guided build and prediction freeze core work | 125 min |

### Week 82: Independent build and integration — 10 hours

| Work | Time |
|---|---:|
| Independent build and integration core work | 540 min |
| Independent build and integration verification checkpoint | 60 min |

### Week 83: Break, repair, measure, and diagnose — 10 hours

| Work | Time |
|---|---:|
| Required evidence components | 90 min |
| Break, repair, measure, and diagnose core work | 510 min |

### Week 84: Decide, teach, assess, and freeze — 9.5 hours

| Work | Time |
|---|---:|
| Required evidence components | 60 min |
| Decide, teach, assess, and freeze core work | 450 min |
| Module teach-back | 30 min |
| Learning log and freeze check | 30 min |
## Learn

1. [Memory lifetime and management](lessons/01-memory-lifetime-management.md)
2. [Schedulers, event loops, and tasks](lessons/02-schedulers-event-loops-tasks.md)
3. [Bounded fan-out and structured cleanup](lessons/03-bounded-fanout-structured-cleanup.md)
4. [Memory visibility and races](lessons/04-memory-visibility-races.md)
5. [Types, serialization, and validation](lessons/05-types-serialization-validation.md)
6. [Equivalent-work runtime measurement](lessons/06-equivalent-work-measurement.md)
7. [Northstar polyglot fan-out tutorial](lessons/07-northstar-polyglot-tutorial.md)
8. [Runtime decision and teach-back](lessons/08-runtime-decision-teach-back.md)

Use the [glossary](glossary.md) and [interface reference](lab/README.md) after
studying the mechanisms.

## Practice and independent evidence

- Freeze the commerce execution-model baseline before the completed
  [Northstar case](case-study/northstar-observation-enrichment.md).
- Complete the [guided exercises](exercises/exercises.md) before opening the
  [explained answers](exercises/answer-key.md).
- Run the [polyglot lab](lab/README.md), preserve scenario and output hashes,
  then implement the same public contract independently.
- Keep protocol conformance separate from performance interpretation. A valid
  response does not prove suitability; one fast laptop trial does not establish
  a language property.
- Preserve predictions and raw results. Corrections belong in dated addenda.

This module contributes two distinct runtime comparisons—semantic conformance
and measured performance/operability—plus one ADR, one failure matrix, one
performance investigation, and one lightweight teach-back. Gate 5 owns its
standalone submission; the module does not duplicate it.

## Assessment and completion

- Read the [assessment contract](assessment/README.md), [anchored rubric](assessment/rubric.md),
  [Gate 5](../../gates/G05/assessment-brief.md), [evaluator prompt](assessment/evaluator-prompt.md),
  [remediation map](assessment/remediation-map.md), and current
  [readiness review](assessment/semantic-readiness-review.md) before independent work.
- Pass G01–G06, average at least 3.0, and avoid a zero in R05–R08.
- Gate 5 reviews Modules 13–15. The Week 85 gate freeze remains immutable; accepted findings belong in the separate Week 86 delta.

## Evidence boundary and AI use

The lab can expose scheduling, bounds, cancellation, cleanup, validation,
allocation, GC, and race-detector evidence on the recorded host. It cannot prove
production tail latency, every compiler optimization, physical memory safety,
ecosystem quality, future runtime behavior, legal compliance, or team ability.

AI may challenge arithmetic, hypotheses, experiment design, and alternatives.
It may not choose the graded runtime, invent measurements, rewrite frozen work,
produce replacement graded answers, or answer during the defense.

## Course-wide completion contracts

- The machine-readable `module.json` time blocks are the canonical required-work budget.
- The [factual-claims ledger](assessment/factual-claims.json) maps each local lesson to its authoritative source boundary.
- Use the [provider-neutral evaluation workflow](../../EVALUATION_GUIDE.md) only after learner evidence is committed.
- Use the [sealed local gate workflow](../../SOLO_GATE_GUIDE.md) when a course gate applies. Human review is optional.

A frozen self-evaluation may establish **Solo Complete**; independent human or LLM review may establish **Independently Validated**. Synthetic lab values are not production measurements.

## PESD 2.0 scope addition

This 5-week module schedules 47 core hours. Its primary
decision is ADR A08. The added graded scope is
four transport/schema shells while the learner implements admission, task ownership, cancellation, cleanup, memory and lifetime behavior, synchronization, and validation in TypeScript, Go, Rust, and Java. See Lesson 8, the final guided exercise, final worksheet,
rubric anchors, and remediation map for the integrated evidence contract.
