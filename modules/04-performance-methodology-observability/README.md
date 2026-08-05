# Module 4: Performance Methodology and Observability

> **Authoring status:** Review. PESD 2.0 content and machine-readable contracts are migrated. Refreshed evaluator calibration, full platform matrices, offline reruns, cleanup checks, and timed learner pilots remain required before Ready.

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

The 10–12 hour weekly figure is a capacity envelope. Core work is deliberately
budgeted below that ceiling; unused time is recovery buffer, not hidden work.

### Week 18: Model and derive — 8.5 hours

| Work | Time |
|---|---:|
| Bounded authoritative resources | 130 min |
| Local mechanism instruction | 120 min |
| Guided practice | 60 min |
| Model and derive core work | 200 min |

### Week 19: Guided build and prediction freeze — 9 hours

| Work | Time |
|---|---:|
| Bounded authoritative resources | 125 min |
| Local mechanism instruction | 120 min |
| Guided practice | 60 min |
| Required evidence components | 90 min |
| Guided build and prediction freeze core work | 145 min |

### Week 20: Independent build and integration — 10 hours

| Work | Time |
|---|---:|
| Independent build and integration core work | 540 min |
| Independent build and integration verification checkpoint | 60 min |

### Week 21: Break, repair, measure, and diagnose — 10 hours

| Work | Time |
|---|---:|
| Required evidence components | 120 min |
| Break, repair, measure, and diagnose core work | 480 min |

### Week 22: Decide, teach, assess, and freeze — 9.5 hours

| Work | Time |
|---|---:|
| Required evidence components | 120 min |
| Decide, teach, assess, and freeze core work | 390 min |
| Module teach-back | 30 min |
| Learning log and freeze check | 30 min |
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

The module contributes one performance investigation, one failure matrix, one
performance-regression policy ADR, and one recorded teach-back to the portfolio.

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
- Inspect the accepted [calibration results](assessment/calibration/results.md),
  [fixtures](assessment/calibration/README.md), and
  [six-run record](assessment/calibration/runs/README.md) when auditing evaluator
  behavior.

The evaluator runs structural gates before semantic scoring, cites submitted
headings, and returns Pass, Revise, or Repeat under the published thresholds.

## Evidence integrity and AI use

AI may explain a telemetry contract or propose test cases. It may not invent
measurements, reveal a hidden fixture before the diagnosis is frozen, rewrite
raw evidence, or answer during the defense. Disclose assistance and verify every
claim against source, schema, or experiment evidence.

## Course-wide completion contracts

- The machine-readable `module.json` time blocks are the canonical required-work budget.
- The [factual-claims ledger](assessment/factual-claims.json) maps each local lesson to its authoritative source boundary.
- Use the [provider-neutral evaluation workflow](../../EVALUATION_GUIDE.md) only after learner evidence is committed.
- Use the [sealed local gate workflow](../../SOLO_GATE_GUIDE.md) when a course gate applies. Human review is optional.

A frozen self-evaluation may establish **Solo Complete**; independent human or LLM review may establish **Independently Validated**. Synthetic lab values are not production measurements.

## PESD 2.0 scope addition

This 5-week module schedules 47 core hours. Its primary
decision is ADR A11. The added graded scope is
telemetry as a governed data product: schema ownership, PII restrictions, retention, sampling bias, lineage, cardinality, and cost budgets. See Lesson 8, the final guided exercise, final worksheet,
rubric anchors, and remediation map for the integrated evidence contract.
