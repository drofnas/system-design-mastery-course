---
lesson_id: L08
title: Causal Diagnosis and Production Decisions
---

# Causal Diagnosis and Production Decisions

## Outcomes

- Explain one counterintuitive result through a falsifiable causal chain.
- Transfer or reject lab evidence for a production workload.
- Defend a systems-performance decision with owners and reversal conditions.

## Prerequisites

Lessons 1–7 and completed raw experiment evidence.

## Mechanism and decision method

A systems-performance report is an argument from evidence, not a catalog of
counters. Use this sequence:

1. Restate the frozen prediction and decision it could affect.
2. Separate raw observation from interpretation.
3. Draw `code → runtime/library → syscall/lock → kernel → hardware/device → outcome`.
4. Name at least two competing explanations.
5. Change one driver and repeat to falsify them.
6. Reconcile useful throughput, latency, CPU, faults, switches, RSS, I/O, and
   controller evidence without requiring every counter to improve.
7. Compare production and lab workload, topology, limits, failure, and ownership.
8. Decide: adopt, stage another experiment, or reject transfer.
9. Specify rollout, rollback, cost, security, owners, and reversal evidence.

Counterintuitive results are valuable when they reveal a false model. More
workers can reduce throughput; batching can increase tail recovery time; padding
can do nothing; a memory limit can improve isolation while worsening useful
latency. The result is not a novelty contest. It must change a decision or an
evidence plan.

## Worked example

Transit predicts eight workers will outperform four. Eight is slower. The report
first records identical checksums and repeated distributions. It tests three
explanations: shared-lock serialization, CPU oversubscription, and quota throttling.
Sharded state improves both counts; removing the quota removes throttle time but
does not eliminate the plateau; four workers remain best under route skew.

The decision is to stage sharded state with four workers for the declared 2-CPU
quota, retain the existing recovery path, and alert on throttle ratio plus backlog
age. Platform owns quota changes; the service team owns worker configuration and
checkpoint correctness. Reverse if production traces show a different bottleneck,
route skew makes a shard unsafe, or cost per recovered update rises above budget.

## Common expert mistakes

- **Starting with the desired answer:** the experiment becomes confirmation theater.
- **Counter shopping:** one favorable metric cannot override failed useful work.
- **Editing the prediction:** it destroys evidence of learning.
- **Transferring by technology label:** “same language” is not the same workload.
- **Skipping ownership:** a configuration without an operator is not a decision.

## Guided practice

Choose one failed Transit prediction. Write observation, two competing causes,
one discriminating experiment, a production transfer table, and a reversal
condition. Practice a two-minute explanation for a platform engineer and a
product owner without changing the causal model.

## Self-check

1. What makes an explanation causal rather than descriptive?
2. When should a lab result not change production?
3. Why preserve an incorrect prediction?
4. What turns an optimization into a staff-plus decision artifact?

## Explained answers

1. A mechanism links controlled changes to observations and survives attempts to
   falsify competing causes.
2. When workload, environment, failure semantics, or ownership differ enough that
   the mechanism is not supported.
3. It proves what the experiment taught and prevents hindsight from rewriting the
   evidence trail.
4. It connects user/business outcomes, quantified evidence, safety, operations,
   cost, cross-team ownership, rollout, and teaching.

## Sources and next work

- Julia Lawall, *Opening the Box*: https://www.usenix.org/conference/srecon24emea/presentation/lawall
- Meta, *Serving Facebook Multifeed*: https://engineering.fb.com/2015/03/10/production-engineering/serving-facebook-multifeed-efficiency-performance-gains-through-redesign/
- Complete EX-12, the report, defense, and Gate 1.
