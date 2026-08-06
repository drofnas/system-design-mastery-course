---
lesson_id: L03
title: "Ordering, Partition Keys, and Consumer Groups"
---

# Ordering, Partition Keys, and Consumer Groups

## Outcomes

- State the smallest ordering scope required by an invariant.
- Select and stress-test a partition key.
- Calculate consumer parallelism, skew, lag, and reassignment consequences.

## Prerequisites

Module 2 capacity, Module 9 partitioning, and L02 identities.

## Mechanism and decision procedure

A partitioned log usually offers total order only inside one partition. A
consumer group assigns each partition to at most one active member of that
group, so maximum useful parallelism is bounded by partition count and skew.
Global order is expensive and rarely required; per-aggregate version monotonicity
often preserves the real invariant.

For candidate key `k`, estimate peak records/s and service demand per hot key,
cardinality, growth, privacy/residency constraints, and operations that require
co-location. Then test:

1. Do all events that must be ordered share `k`?
2. Can one value exceed one partition's useful capacity?
3. Can the key change without moving identity or breaking replay?
4. Can tenants share fairly, or does one tenant monopolize a partition?
5. Does a rebalance preserve local state/checkpoint correctness?

Consumers must also enforce aggregate versions. Transport order does not stop a
retry from an older topic, a backfill, or two source partitions from presenting
an older fact.

## Worked example

Northstar keys by observation ID because versions for one observation must not
regress. With 12 partitions and 6 consumers, each consumer normally owns two.
A newly discovered object creates 45% of traffic, so adding consumers cannot
split that single key. Northstar measures per-key service demand, applies a
version check, and isolates optional analytics during the burst rather than
claiming uniform scale.

## Common expert mistakes

- **Require global order:** it reduces parallelism without preserving a named
  cross-aggregate invariant.
- **Key randomly for balance:** related versions can reorder across partitions.
- **Assume partitions equal capacity:** skew and record cost dominate counts.
- **Ignore rebalance state:** duplicate processing and cold local state can
  extend lag during deployments.

## Guided practice

Compare account ID, tenant ID, and random key for a metering stream. Calculate
parallelism and identify a hot-tenant counterexample. State consumer behavior
for version gaps and rebalances.

## Self-check

1. Do more consumers always reduce lag?
2. Does one partition guarantee business causality?
3. When may a consumer skip a stale version?

## Explained answers

1. No. Consumers beyond partition count are idle; a hot partition or shared
   dependency remains the bottleneck.
2. It gives a log order under its producer contract, not proof of causal or
   authoritative order from every source.
3. Only under a published version/repair contract that preserves required
   transitions and records the skip; otherwise it may hide missing state.

## Sources and next work

Use RES-01's producer, consumer, and partition sections; complete EX-05–EX-06
and the workflow practice partition/fairness review.
