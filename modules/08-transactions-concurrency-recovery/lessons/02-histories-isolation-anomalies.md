---
lesson_id: L02
title: "Histories, Serializability, and Isolation Anomalies"
---

# Histories, Serializability, and Isolation Anomalies

## Outcomes

Read a history, construct dependencies, identify lost update and write skew,
and select an isolation claim per operation rather than per product.

## Prerequisites

Lesson 1 and the ability to write ordered read/write/commit events.

## Mechanism and decision procedure

Represent each transaction as reads `rT(x)`, writes `wT(x)`, and a commit or
abort. A conflict exists when two committed transactions access the same
logical fact and at least one writes. Add an edge from the earlier effect to
the later dependent effect. A cycle in the serialization graph proves that the
history is not conflict-serializable.

Visibility and conflict detection are separate. Read committed usually takes a
new snapshot per statement. Snapshot isolation gives a stable transaction
snapshot and rejects overlapping writes to the same item, yet may admit write
skew across different items. Serializable execution must reject or prevent a
history that has no serial equivalent. The application must retry the whole
transaction after a serialization failure.

Choose isolation by: invariant → adversarial history → required visibility and
conflict rule → abort/retry behavior → measured contention. Never infer vendor
semantics from an isolation label alone.

## Worked example

Controllers A and B are certified. T1 and T2 both read A+B as active. T1
deactivates A; T2 deactivates B. Their writes are disjoint, so snapshot
write-write checks allow both. The result has zero controllers and violates
N-01. Serializable validation finds the read/write dependency cycle and aborts
one; a full retry observes the remaining controller and refuses deactivation.

## Common expert mistakes

- Listing ANSI anomaly names without drawing the violating schedule.
- Assuming repeatable read or snapshot means serializable in every database.
- Retrying only the failed statement after the transaction snapshot is invalid.
- Raising isolation globally without measuring abort and latency costs.

## Guided practice

Annotate F01 and F02 histories. Draw dependency edges, name the violated
invariant, and propose both a concurrency-control repair and a schema
restructuring. State how each repair can be falsified.

## Self-check

1. Can a history contain no dirty reads and still violate an invariant?
2. What distinguishes lost update from write skew?
3. What must happen after a serialization failure?

## Explained answers

1. Yes; write skew uses committed snapshots. 2. Lost update overwrites the
same logical value; write skew uses disjoint writes whose combined effect
violates a predicate. 3. Roll back and retry the entire transaction from fresh
state, subject to bounded eligibility and deadline rules.

## Failure-mode bridge to the lab

Isolation anomalies are not vocabulary trivia; they are explanations for how a
history that looks plausible at the statement level violates an invariant at the
transaction level. Dirty reads expose uncommitted state. Non-repeatable reads
change an answer inside one transaction. Phantoms add or remove rows that match a
predicate. Write skew lets two transactions each observe a safe condition and
commit updates that make the combined result unsafe.

When the lab presents interleavings, draw the history before naming the anomaly.
Mark each read, each write, and the predicate or row it touches. Then ask what
serial order, if any, would produce the same result. If none exists, the history
is not serializable. If a serial order exists but violates a business invariant,
the boundary or constraint is wrong. This separation prevents the common mistake
of demanding the strongest isolation when the real fix is an explicit invariant.

## Second worked example

Two doctors each check that at least one doctor remains on call, then each marks
themselves off call in separate rows. Under snapshot isolation both reads can
see two doctors on call and both writes can commit because they touch different
rows. The final state violates the predicate invariant. The anomaly is not a
dirty read or lost update; it is write skew. A repair makes the predicate
conflict concrete through serializable isolation, a guard row, or a constraint
that the storage system can enforce.

## Decision checklist

For each history, list reads, writes, predicates, commit order, and candidate
serial orders. Then separate the isolation anomaly from any missing business
constraint.

## Sources and next work

- PostgreSQL, [Transaction Isolation](https://www.postgresql.org/docs/current/transaction-iso.html).
- CMU 15-445, [Spring 2026 concurrency-control materials](https://15445.courses.cs.cmu.edu/spring2026/schedule.html).
- Continue with EX-03–EX-04 and the F01/F02 predictions.
