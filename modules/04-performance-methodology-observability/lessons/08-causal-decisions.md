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

Complete EX-14 and EX-15. Use the scripted solo-review packet to challenge the
strongest assumption, answer without live AI, record the evidence needed to
resolve disagreement, and freeze the responses. That record completes the solo
teach-back. A human reviewer or provider-neutral LLM may critique the frozen
record afterward as optional stronger portfolio evidence.

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

## PESD 2.0 extension: modern constraints and ownership

PESD 2.0 adds **telemetry as a governed data product: schema ownership, PII restrictions, retention, sampling bias, lineage, cardinality, and cost budgets**.

### Repeatable decision procedure

1. Inventory the affected data, tenants, identities, providers, jurisdictions,
   control planes, evidence owners, and cost owners before selecting a mechanism.
2. State the invariant and the authority that may change it. Separate a claimed
   policy from the enforcement point and from the evidence that proves execution.
3. Freeze a prediction, implement or model the named mechanism, and record the
   accepted evidence mode and runtime boundary.
4. Inject one policy, isolation, recovery, or supplier failure in addition to the
   module's mechanism failure. Preserve raw evidence before interpretation.
5. Compare at least two options across product outcome, technical mechanism,
   security and governance, operations and recovery, economics, ownership,
   migration, and reversal triggers.

### Non-capstone extension

Apply the procedure to the module's continuing case. Add one tenant or governed
data class, one supplier or control-plane dependency, and one deletion, recovery,
or exit obligation. The completed case may demonstrate the method, but its
topology, thresholds, policy choices, and answer are not defaults for Global
Commerce.

### Evidence boundary

Use `derived`, `executed_deterministic`, `measured_loopback`,
`measured_container`, `modeled_capacity`, `fixture_replay`, or
`measured_accelerator` exactly as defined by the course. Fixture replay supports
practice and remediation only. Modeled remote scale is not local measurement.
Every trial records commit and input/configuration hashes, runtime and resource
limits, clock, warm-up/repetition policy, raw outcomes, and limitations.

### Source boundary

Use the module's bounded primary sources and preserve the local evidence boundary.
