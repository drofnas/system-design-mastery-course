# Module 15: Execution Models Across Languages

> **Authoring status:** Ready. Four-runtime conformance, paired failure evidence,
> six isolated evaluator runs, calibration checking, semantic and resource
> review, and focused and full-course validation passed on 2026-08-03.

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

### Week 57: Model execution and freeze predictions — 11 hours

| Work | Time |
|---|---:|
| Lessons 1–5 and bounded sources | 4 h |
| EX-01–EX-04 and Northstar modeling | 2 h |
| Independent workload, equivalence, and F01–F09 baseline | 3.5 h |
| Freeze, self-check, and learning log | 1.5 h |

Use the [Week 57 worksheet](worksheets/week-57-execution-model.md).

### Week 58: Build four equivalent services — 12 hours

| Work | Time |
|---|---:|
| Lessons 3, 5, and 7; lab tutorial | 2.5 h |
| EX-05–EX-09 and contract rehearsal | 2 h |
| TypeScript, Go, Rust, and Java implementations | 6.5 h |
| Conformance review and learning log | 1 h |

Use the [Week 58 worksheet](worksheets/week-58-polyglot-build.md).

### Week 59: Break and measure runtime assumptions — 12 hours

| Work | Time |
|---|---:|
| Lessons 4 and 6; bounded sources | 2 h |
| EX-10–EX-17 and experiment rehearsal | 2 h |
| F01–F09 broken/repaired trials | 6 h |
| Failure matrix, investigation, and learning log | 2 h |

Use the [Week 59 worksheet](worksheets/week-59-runtime-failure-matrix.md).

### Week 60: Decide, teach, assess, and complete Gate 5 — 11 hours

| Work | Time |
|---|---:|
| Lesson 8, Discord case, and EX-18 | 1.5 h |
| Two comparison reports and runtime-selection ADR | 3 h |
| Defense and module evaluation | 1.5 h |
| Four-part Gate 5 | 3.5 h |
| Remediation and learning log | 1.5 h |

Use the [Week 60 worksheet](worksheets/week-60-runtime-decision-gate-05.md).

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

This module contributes two runtime-comparison reports, the course's third
source-code internals review, one ADR, one failure matrix, one performance
investigation, one Gate 5 submission, and one recorded teach-back.

## Assessment and completion

- Read the [assessment contract](assessment/README.md), [anchored rubric](assessment/rubric.md),
  [Gate 5](assessment/gate-05.md), [evaluator prompt](assessment/evaluator-prompt.md),
  [remediation map](assessment/remediation-map.md), and current
  [readiness review](assessment/semantic-readiness-review.md) before independent work.
- Pass G01–G06, average at least 3.0, and avoid a zero in R05–R08.
- Gate 5 reviews Modules 13–15. It does not create a Week 60 capstone revision.

## Evidence boundary and AI use

The lab can expose scheduling, bounds, cancellation, cleanup, validation,
allocation, GC, and race-detector evidence on the recorded host. It cannot prove
production tail latency, every compiler optimization, physical memory safety,
ecosystem quality, future runtime behavior, legal compliance, or team ability.

AI may challenge arithmetic, hypotheses, experiment design, and alternatives.
It may not choose the graded runtime, invent measurements, rewrite frozen work,
produce replacement graded answers, or answer during the defense.
