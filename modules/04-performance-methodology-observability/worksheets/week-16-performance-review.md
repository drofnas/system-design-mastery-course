# Week 16: Performance Review and Defense

## Decision header

- Decision, owner, date, workload, user objective, candidate commit:
- Frozen baseline and diagnosis commits:

## Evidence chain

State baseline, observed change, causal model, credible alternatives,
discriminating test, proposed change, and controlled validation. Cite raw files
and headings rather than restating uncited numbers.

## Regression budget

Record metric, workload, environment, comparison statistic, allowed change,
uncertainty rule, repetitions, and block/rollback action.

## A11: Performance-regression policy ADR — 45 minutes

Create `adr/module-04-performance-regression-policy.md`. The performance report
explains what the evidence shows; the ADR records the decision that follows from
it. State context, shared drivers, at least three policy alternatives, chosen
release threshold, inconclusive-result behavior, owner, rollout/rollback, and
reversal evidence. Link rather than copy raw benchmark evidence.

## Operations, security, cost, and change

Cover telemetry overhead and spend, cardinality, redaction, access, retention,
on-call use, owner, rollout, rollback, migration from current instrumentation,
and evidence that reverses the decision.

## Teach-back and challenge

Record a 12–15 minute explanation, reviewer questions, unresolved disagreement,
and evidence assigned to an owner. Do not change the submitted workload or
failure model during defense.
