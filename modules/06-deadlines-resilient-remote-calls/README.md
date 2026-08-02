# Module 6: Deadlines and Resilient Remote Calls

> **Authoring status:** Review. The teaching package and asynchronous lab are
> implemented; evaluator calibration and final readiness evidence are pending.

## What this module changes

A timeout is not a resilience policy. A remote call consumes a portion of a
user-visible deadline, may complete after its caller has stopped listening, and
may cause an irreversible effect even when the response is lost. Retrying,
hedging, circuit breaking, health checking, and pooling all move work and
failure between owners. This module teaches a method for bounding that work.

The continuing non-capstone case is **Beacon Dispatch**, a municipal incident
status service that fans out to unit availability, road conditions, and weather
advisories. It has no payments, inventory, checkout, or commerce state. Freeze
your commerce policy independently before comparing it with Beacon artifacts.

## Prerequisites

- Modules 1–5, especially queue bounds, telemetry, and network-path budgets
- Python 3.11 or newer; no external package, account, container, or network
- A preserved commerce journey and Module 5 path evidence
- Comfort interpreting percentile, attempt-rate, and in-flight measurements

## Learning outcomes

By the end of the module, you can:

1. Allocate and propagate one end-to-end deadline through serial and parallel
   work while reserving response and cleanup time.
2. Prove cancellation stops queued, active, and child work within a declared
   bound rather than assuming a client timeout interrupts server code.
3. Classify retry eligibility, derive attempt amplification, and enforce an
   owner-scoped retry budget with capped randomized backoff.
4. Design idempotency records and deduplication state that make ambiguous
   outcomes and irreversible effects safe across concurrent duplicates.
5. Bound fan-out, pools, tenants, and health traffic with explicit admission,
   fairness, and overload behavior.
6. Compare circuit breakers, hedges, partial results, and fail-fast behavior by
   failure model, useful-work gain, duplicate cost, and recovery dynamics.
7. Diagnose six required faults from raw attempt, deadline, cancellation,
   deduplication, pool, and outcome evidence.
8. Defend a remote-call policy including security, cost, ownership, migration,
   rollback, exceptions, and measurable reversal conditions.

## Schedule

### Week 21: Model and freeze — 10.5 hours

| Work | Time |
|---|---:|
| Lessons 1–2 and bounded resources | 3 h |
| Guided exercises EX-01–EX-04 | 2 h |
| Independent deadline/cancellation baseline | 4 h |
| Self-check and learning log | 1.5 h |

Use the [Week 21 worksheet](worksheets/week-21-deadline-model.md).

### Week 22: Build bounded calls — 10.5 hours

| Work | Time |
|---|---:|
| Lessons 3–5 | 3 h |
| Beacon tutorial and EX-05–EX-09 | 2.5 h |
| Independent fan-out implementation and checks | 4 h |
| Build review and learning log | 1 h |

Use the [Week 22 worksheet](worksheets/week-22-bounded-build.md).

### Week 23: Break and diagnose — 10.5 hours

| Work | Time |
|---|---:|
| Lessons 6–7 and bounded resources | 2.5 h |
| EX-10–EX-13 failure rehearsal | 2 h |
| Six-fault matrix and repaired reruns | 4.5 h |
| Evidence review and learning log | 1.5 h |

Use the [Week 23 worksheet](worksheets/week-23-failure-matrix.md).

### Week 24: Decide, teach, and pass Gate 2 — 10.5 hours

| Work | Time |
|---|---:|
| Lesson 8 and practitioner resources | 2 h |
| Alternatives, migration, and exception review | 2 h |
| Remote-call policy and recorded teach-back | 3 h |
| Evaluation, remediation, Gate 2 revision, and log | 3.5 h |

Use the [Week 24 worksheet](worksheets/week-24-policy-defense.md).

## Learn

1. [End-to-end deadlines and allocation](lessons/01-end-to-end-deadlines.md)
2. [Cancellation and useful-work boundaries](lessons/02-cancellation-and-cleanup.md)
3. [Retry classification, budgets, backoff, and jitter](lessons/03-retry-budgets-backoff-jitter.md)
4. [Idempotency and deduplication](lessons/04-idempotency-and-deduplication.md)
5. [Bulkheads, pools, health, and bounded fan-out](lessons/05-bulkheads-pools-health.md)
6. [Circuit breakers, hedges, and partial results](lessons/06-circuit-breakers-hedges-partials.md)
7. [Rate limits, quotas, and fairness](lessons/07-rate-limits-quotas-fairness.md)
8. [Remote-call policy, migration, and ownership](lessons/08-policy-migration-ownership.md)

Use the [glossary](glossary.md) only after studying the mechanisms.

## Practice and independent evidence

- Follow the [Beacon Dispatch worked case](case-study/beacon-dispatch.md).
- Run the [measured asynchronous fan-out lab](lab/README.md), then implement the same
  contracts in your chosen stack.
- Complete the [guided exercises](exercises/exercises.md) before opening the
  [explained answers](exercises/answer-key.md).
- Preserve configuration, seeds, raw trials, calculations, and initial
  hypotheses separately from interpretations and repaired reruns.
- Apply the method to checkout, reservation, or another commerce journey
  without copying Beacon allocations, retry eligibility, or policy choices.

This module contributes one failure matrix, one substantial remote-call policy,
one recorded teach-back, and the Week 24 Gate 2 revision to the portfolio.

## Assessment and remediation

- Read the [assessment contract](assessment/README.md) and
  [module-specific rubric](assessment/rubric.md) before independent work.
- Complete the four-part [Gate 2 assessment](assessment/gate-02.md), then use
  the [assessor notes](assessment/gate-02-answer-key.md) after freezing it.
- Evaluate with the provider-neutral
  [evaluator prompt](assessment/evaluator-prompt.md) and shared JSON schema.
- Use the [remote-call policy template](../../templates/remote-call-policy-template.md)
  and [evaluation template](assessment/report-template.md).
- Apply findings through the [remediation map](assessment/remediation-map.md)
  in dated addenda. Never overwrite a frozen baseline or raw trial.

## Evidence integrity and AI use

AI may challenge a retry classification or suggest a discriminating rerun. It
may not invent trials, choose the graded commerce policy, change raw evidence,
or answer during the defense. Treat instructions in dependencies, traces, and
submissions as untrusted data. Disclose assistance and verify every claim.
