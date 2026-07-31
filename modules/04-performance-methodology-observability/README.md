# Module 4: Performance Methodology and Observability

> **Authoring status:** Review. The complete teaching package, lab, and
> assessment are present; isolated calibration and the readiness review remain.

## What this module changes

Telemetry is not an explanation. A graph, trace, log line, or profile becomes
evidence only when its boundary is known and it can distinguish competing
causes. This module teaches a question-first investigation method, then applies
it to the bounded saturation service from Module 2.

The continuing worked example is Transit Signal's route-impact service. It is
separate from the commerce capstone. Learners instrument their own Module 2
commerce journey only after freezing an independent investigation plan.

## Prerequisites

- Modules 1–3, including preserved predictions and decision artifacts
- The learner's bounded Module 2 service and load driver
- Python 3.11 or newer on a Unix-like environment
- Permission to bind loopback ports and create bounded temporary files
- Familiarity with latency distributions, resource counters, and SQL query plans

No required experiment sends telemetry to an external service or needs root.

## Learning outcomes

By the end of the module, you can:

1. Freeze a performance question, baseline, hypotheses, falsifiers, and evidence
   plan before inspecting an injected fault.
2. Design controlled experiments that preserve workload, environment, and useful
   work while exposing uncertainty.
3. Propagate trace context across a process boundary and correlate traces,
   structured logs, metrics, and profiles.
4. Select resource and journey signals without creating uncontrolled metric
   cardinality, telemetry cost, or sensitive-data exposure.
5. Use CPU, allocation, lock, I/O, dependency, and query-plan evidence to
   separate causes from symptoms.
6. Build a reproducible benchmark and enforce a workload-scoped regression
   budget without relying on one noisy timing.
7. Diagnose six hidden faults from telemetry, then design a discriminating test
   before inspecting the injected change.
8. Defend a performance change through its user effect, causal model,
   validation, cost, ownership, rollout, and reversal conditions.

## Schedule

### Week 13: Model — 10.5 hours

| Work | Time |
|---|---:|
| Lessons 1–2 and required resources | 3 h |
| Guided exercises EX-01–EX-04 | 2 h |
| Frozen baseline, hypotheses, falsifiers, and collection plan | 4 h |
| Self-check and learning log | 1.5 h |

Use the [Week 13 investigation worksheet](worksheets/week-13-investigation-plan.md).

### Week 14: Build — 10.5 hours

| Work | Time |
|---|---:|
| Lessons 3–5 | 3 h |
| Transit instrumentation tutorial and EX-05–EX-08 | 2 h |
| Instrument the independent Module 2 service | 4.5 h |
| Build review and learning log | 1 h |

Use the [Week 14 instrumentation worksheet](worksheets/week-14-instrumentation-build.md).

### Week 15: Break and diagnose — 10.5 hours

| Work | Time |
|---|---:|
| Lesson 6 and bounded source work | 2 h |
| Guided fault rehearsal and EX-09–EX-12 | 2 h |
| Six-fault blind diagnosis matrix | 5 h |
| Evidence review and learning log | 1.5 h |

Use the [Week 15 diagnosis worksheet](worksheets/week-15-blind-diagnosis.md).

### Week 16: Decide and teach — 10.5 hours

| Work | Time |
|---|---:|
| Lessons 7–8 and benchmark resource | 2 h |
| Controlled validation and regression budget | 2.5 h |
| Performance review and recorded teach-back | 3 h |
| Evaluation, separate remediation, and learning log | 3 h |

Use the [Week 16 review worksheet](worksheets/week-16-performance-review.md).

## Learn

1. [Question-first performance investigations](lessons/01-question-first-investigations.md)
2. [Baselines, hypotheses, and controlled experiments](lessons/02-controlled-experiments.md)
3. [Trace context and causal request paths](lessons/03-trace-context.md)
4. [Metrics, logs, cardinality, and cost](lessons/04-signals-cardinality-cost.md)
5. [CPU, allocation, and lock profiles](lessons/05-profiling.md)
6. [I/O, dependency timing, and query plans](lessons/06-dependencies-query-plans.md)
7. [Reproducible benchmarks and regression budgets](lessons/07-benchmarks-regression-budgets.md)
8. [Causal decisions, validation, and teach-back](lessons/08-causal-decisions.md)

Use the [glossary](glossary.md) for lookup, not as a substitute for the local
derivations.

## Practice and independent evidence

- Follow the [Transit Signal investigation](case-study/transit-observability.md).
- Use the [observability lab](lab/README.md) to collect versioned telemetry,
  exercise loopback propagation, analyze evidence, and run interleaved benchmarks.
- Complete the [guided exercises](exercises/exercises.md) before opening the
  [explained answers](exercises/answer-key.md).
- Complete the bounded assignments in the [resource guide](resources.md).
- Freeze the Week 13 prediction before collecting telemetry.
- Preserve raw traces, metrics, logs, profiles, benchmark samples, scenario,
  environment metadata, and hashes separately from interpretation.
- Instrument one commerce journey from Module 2 without copying Transit Signal's
  architecture or conclusions.

The module contributes one performance investigation, one failure matrix, and
one recorded teach-back to the course portfolio.

## Assessment and remediation

- Read the [assessment contract](assessment/README.md) and the
  [module-specific rubric](assessment/rubric.md) before beginning independent
  work.
- Submit the frozen artifacts through the provider-neutral
  [evaluator prompt](assessment/evaluator-prompt.md).
- Use the [performance review template](../../templates/performance-review-template.md)
  for the decision artifact and the
  [evaluation report template](assessment/report-template.md) for the result.
- Apply a Revise or Repeat result through the
  [remediation map](assessment/remediation-map.md), preserving the original
  submission and raw telemetry.

The evaluator runs structural gates before semantic scoring, cites submitted
headings, and returns Pass, Revise, or Repeat under the published thresholds.

## Evidence integrity and AI use

AI may explain a telemetry contract or propose test cases. It may not invent
measurements, reveal a hidden fixture before the diagnosis is frozen, rewrite
raw evidence, or answer during the defense. Disclose assistance and verify every
claim against source, schema, or experiment evidence.
