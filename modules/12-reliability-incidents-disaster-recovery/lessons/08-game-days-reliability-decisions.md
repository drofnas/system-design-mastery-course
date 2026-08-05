---
lesson_id: L08
title: Chaos, Game Days, and Reliability Decisions
week: 48
---

# Chaos, Game Days, and Reliability Decisions

## Outcomes

- Design a controlled game day with hypothesis, safety, and evidence.
- Compare reliability and recovery tiers using user, risk, cost, and ownership.
- Defend Gate 4 and teach the reasoning without exposing a canonical design.

## Prerequisites

Lessons 1–7 and frozen Module 12 incident and recovery evidence.

## Exercise and decision procedure

Write the hypothesis as observable behavior under a named fault. Define scope,
authorized environment, users/data protected, roles, start state, instrumentation,
abort conditions, maximum blast radius, rollback, and cleanup. Verify that the
exercise cannot traverse production links or credentials unexpectedly. Practice
communications and access before injecting faults.

Compare at least three tiers, such as single-region tested restore, warm standby,
and active regional serving. Use the same journeys, RPO/RTO, failure model,
capacity, security, privacy, cost, staffing, ownership, migration, and rollback
drivers. Name common control planes and residual risk. The most redundant option
is not automatically best if it is unaffordable or unoperable.

Gate 4 connects consensus epochs and fencing, messaging identities and workflow
reconciliation, reliability measurement, incident response, and recovery. A
defensible alternative may differ from Northstar if evidence and assumptions align.

## Worked example

Northstar's game day injects regional unavailability after verifying alternate
capacity, immutable registry evidence, epoch fencing, abort access, and user
communications. The first run fails RTO because secret delivery and DNS control
depend on the lost region. The plan is revised in a new artifact; the failed run
remains evidence. A warm-standby tier wins over active/active authority because
tested RPO/RTO meets the journey need at an operable cost.

## Common expert mistakes

- **Inject chaos without a hypothesis:** spectacle replaces learning.
- **Test only technical failover:** roles, access, communications, and vendors fail.
- **Expand scope during the exercise:** authorization and safety assumptions break.
- **Select maximum availability:** cost and operational complexity create new risk.
- **Rewrite the first run:** learning chronology and evaluator trust disappear.

## Guided practice

Design a tabletop, component test, and live isolated game day for an archive.
For each, state the new claim it can support and the claim it cannot. Compare
three recovery tiers and use the frozen solo-review packet to conduct a
teach-back from product, security, finance, and on-call perspectives. Record
dissent and evidence needed to resolve it. A live panel is optional.

## Self-check

1. What makes a game day controlled?
2. Can a tabletop prove RTO?
3. What evidence justifies a more expensive recovery tier?

## Explained answers

1. Authorization, bounded scope, protected data/users, roles, instrumentation,
   aborts, rollback, cleanup, and immutable evidence.
2. It can validate decisions, roles, and missing prerequisites but cannot prove
   technical restore or failover elapsed time.
3. Quantified user/data exposure reduced under credible faults, plus evidence
   that the organization can build and operate the tier safely.

## Sources and next work

Study RES-07, complete EX-16, finalize the disaster-recovery review, conduct the
defense, freeze Gate 4 in Week 68, and write the separate Week 69 capstone delta.

## PESD 2.0 extension: modern constraints and ownership

PESD 2.0 adds **cyber recovery, corrupted-backup recovery, provider concentration, control-plane outages, clean-room assumptions, evidence preservation, and notification ownership**.

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
