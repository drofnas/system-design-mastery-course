lesson_id: L08

# Causal Decisions, Validation, and Teach-Back

## Outcomes

- Connect a user outcome to code, resource behavior, and controlled evidence.
- Include operations, security, cost, ownership, migration, and reversal.
- Teach the causal model under adversarial questioning.

## Prerequisites

Lessons 1–7 and one frozen blind diagnosis.

## Mechanism and method

A performance review is a decision record with an evidence chain:

```text
user outcome -> bounded observation -> mechanism -> alternatives
             -> discriminating test -> equivalent change -> validation
             -> rollout, owner, budget, and reversal
```

Start with the frozen question and cite raw evidence. Separate what happened
from why. State confidence and remaining uncertainty. Then cover the consequences
of owning the change: collection cost, privacy, retention, on-call response,
capacity under failure, migration from existing instrumentation, rollback, and
the evidence that reverses the decision.

The teach-back must preserve the submitted workload and failure model. A reviewer
may challenge assumptions, but changing them mid-defense creates a new claim
that needs new evidence.

## Worked example

Transit accepts a normalization optimization only after the response checksum,
branch count, process CPU, profile attribution, server spans, and p95 move as
predicted in an interleaved validation. The rollout owner watches journey p95,
error mix, CPU headroom, and telemetry overhead. A production profile that moves
the hot path elsewhere reverses the decision.

## Common expert mistakes

- **Lead with the patch:** reviewers cannot judge whether it solves the user
  problem.
- **Collapse correlation into cause:** alternatives and falsifiers disappear.
- **Ignore telemetry as production code:** cost, privacy, and failure modes remain
  unowned.
- **Claim universal improvement:** workload and environment boundaries vanish.

## Guided practice

Complete EX-14 and EX-15. Ask a reviewer to challenge the strongest assumption
and record the evidence needed to resolve disagreement.

## Self-check

1. What separates a performance report from a chart collection?
2. Why name migration for instrumentation?
3. What should happen when a reviewer changes the workload?

## Explained answers

1. A falsifiable causal model, alternatives, discriminating test, validated
   decision, and reversal conditions.
2. Signal names, labels, retention, dashboards, and owners are interfaces; an
   unsafe cutover can blind operators or duplicate cost.
3. Record it as a new scope and experiment. Do not pretend the submitted evidence
   already covers it.

## Sources and next work

- USENIX, [The Art of Performance Monitoring](https://www.usenix.org/conference/srecon16/program/presentation/smith).
- OpenTelemetry, [Specification overview](https://opentelemetry.io/docs/specs/otel/overview/).
- Next: complete the Week 16 performance review and defense.
