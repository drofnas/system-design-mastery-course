# Module 6: Deadlines and Resilient Remote Calls

> **Authoring status:** Review. PESD 2.0 content and machine-readable contracts are migrated. Refreshed evaluator calibration, full platform matrices, offline reruns, cleanup checks, and timed learner pilots remain required before Ready.

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

The 10–12 hour weekly figure is a capacity envelope. Core work is deliberately
budgeted below that ceiling; unused time is recovery buffer, not hidden work.

### Week 28: Model and derive — 8.5 hours

| Work | Time |
|---|---:|
| Bounded authoritative resources | 130 min |
| Local mechanism instruction | 120 min |
| Guided practice | 60 min |
| Model and derive core work | 200 min |

Optional contingency capacity: 210 minutes. It is not core work, carries no required evidence, and may remain unused.

### Week 29: Guided build and prediction freeze — 9 hours

| Work | Time |
|---|---:|
| Bounded authoritative resources | 120 min |
| Local mechanism instruction | 120 min |
| Guided practice | 60 min |
| Required evidence components | 120 min |
| Guided build and prediction freeze core work | 120 min |

Optional contingency capacity: 180 minutes. It is not core work, carries no required evidence, and may remain unused.

### Week 30: Independent build and integration — 10 hours

| Work | Time |
|---|---:|
| Independent build and integration core work | 540 min |
| Independent build and integration verification checkpoint | 60 min |

Optional contingency capacity: 120 minutes. It is not core work, carries no required evidence, and may remain unused.

### Week 31: Break, repair, measure, and diagnose — 10 hours

| Work | Time |
|---|---:|
| Required evidence components | 60 min |
| Break, repair, measure, and diagnose core work | 540 min |

Optional contingency capacity: 120 minutes. It is not core work, carries no required evidence, and may remain unused.

### Week 32: Decide, teach, assess, and freeze — 9.5 hours

| Work | Time |
|---|---:|
| Required evidence components | 90 min |
| Decide, teach, assess, and freeze core work | 420 min |
| Module teach-back | 30 min |
| Learning log and freeze check | 30 min |

Optional contingency capacity: 150 minutes. It is not core work, carries no required evidence, and may remain unused.
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

This module contributes one failure matrix, one controlled retry-storm
postmortem, one substantial remote-call policy, one containment ADR, one recorded
teach-back, the Week 33 Gate 2 freeze, and the separate Week 34 capstone delta to the portfolio lineage.

## Assessment and remediation

- Read the [assessment contract](assessment/README.md) and
  [module-specific rubric](assessment/rubric.md) before independent work.
- Complete the standalone [Gate 2 assessment](../../gates/G02/assessment-brief.md) in Week 33 after freezing Module 6 evidence.
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

## Course-wide completion contracts

- The machine-readable `module.json` time blocks are the canonical required-work budget.
- The [factual-claims ledger](assessment/factual-claims.json) maps each local lesson to its authoritative source boundary.
- Use the [provider-neutral evaluation workflow](../../EVALUATION_GUIDE.md) only after learner evidence is committed.
- Use the [sealed local gate workflow](../../SOLO_GATE_GUIDE.md) when a course gate applies. Human review is optional.

A frozen self-evaluation may establish **Solo Complete**; independent human or LLM review may establish **Independently Validated**. Synthetic lab values are not production measurements.

## PESD 2.0 scope addition

This 5-week module schedules 47 core hours. Its primary
decision is RFC A05. The added graded scope is
per-tenant work and cost budgets, identity-aware quotas, provider compatibility, residency-safe fallback, and fairness across critical traffic classes. See Lesson 8, the final guided exercise, final worksheet,
rubric anchors, and remediation map for the integrated evidence contract.

## PESD 2.0 evaluation ownership

Gate G02 invokes this module's rubric and provider-neutral
evaluator once for its domain score. Do not create a second module semantic
evaluation report. The gate result is authoritative; remediation remains a
separate dated artifact only for Revise or Repeat.
