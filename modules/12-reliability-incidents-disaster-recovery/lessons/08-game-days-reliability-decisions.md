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
three recovery tiers and conduct a teach-back to product, security, finance, and
on-call reviewers. Record dissent and evidence needed to resolve it.

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
defense, freeze Gate 4, and write the separate Week 48 capstone revision.
