---
lesson_id: L05
title: "Partitioning, Consistent Hashing, and Resharding"
---

# Partitioning, Consistent Hashing, and Resharding

## Outcomes

- Compare hash, range, and consistent-hash placement from workload evidence.
- Calculate balance and movement under membership change.
- Design a copy, verify, cutover, rollback, and decommission sequence.

## Prerequisites

Module 7 access paths and storage amplification, stable hashing, percentages,
and Lessons 2–4 replica-set and version concepts.

## Mechanism and decision procedure

Partitioning maps keys to ownership. Replication then maps each partition to
multiple replicas. Keep the layers separate: a balanced primary-key mapping can
still create correlated replica placement or a shared failure domain.

Hash partitioning usually balances many independent keys but destroys range
locality. Simple `hash(key) mod node_count` remaps most keys when membership
changes. Range partitioning preserves ordered scans and placement control but
inherits skew from key distribution and range growth. Consistent hashing places
nodes or virtual nodes in a hash space so a membership change moves a bounded
fraction of keys in expectation. It does not make a hot key divisible or remove
the need to balance heterogeneous nodes.

Calculate:

- load share per partition/node and max-to-min or max-to-mean imbalance;
- expected and observed moved keys divided by total keys;
- bytes to copy and time at an allowed transfer rate;
- foreground amplification from dual reads/writes;
- routing metadata size and propagation delay;
- recovery/rollback capacity.

A safe reshard is a migration, not a map edit:

1. Freeze the old and target maps with identities.
2. Provision target capacity and authorization.
3. Copy a bounded snapshot while old ownership remains authoritative.
4. Capture concurrent changes using a documented dual-write, log, or catch-up
   mechanism; do not claim cross-owner atomicity without proof.
5. Verify counts, versions, digests, permissions, and business invariants.
6. Shift reads, then writes, with observable gates.
7. Retain rollback while old state remains valid.
8. Reconcile, stop old writes, and decommission only after the rollback window.

Ownership generation and safe stale-owner rejection lead into Module 10; this
module may name the requirement but cannot claim to solve consensus.

## Worked example

Northstar's public catalog uses a stable hash of observation ID. Range
partitioning by discovery time made one current range hot. Adding n3 to a
two-node modulo map moves 6 of 8 toy keys; rendezvous-style consistent hashing
in the lab moves fewer. Northstar copies the affected keys, tails changes,
checks every version and permission, shifts 5% then 25% then 100% of reads,
shifts writes only after verification, and preserves the old route for rollback.

Researcher-private records add a placement filter: only eligible in-region
nodes enter the candidate set before hashing. A balanced global ring would be
incorrect if it violated that constraint.

## Common expert mistakes

- **Using averages to declare balance:** one hot partition controls tail latency.
- **Expecting consistent hashing to split one hot key:** all requests still map
  to one logical key unless the data/operation is redesigned.
- **Cutting routing before copy verification:** reads return missing or stale data.
- **Dual-writing without reconciliation:** partial success creates two authorities.
- **Deleting the old copy at cutover:** rollback becomes data recovery.

## Guided practice

Map 100 keys with modulo and consistent hashing before and after one node is
added. Calculate movement and copy time for 200 GiB at a safe 40 MiB/s. Design
gates for one write occurring during copy. Complete EX-09 and EX-10.

## Self-check

1. Which partitioner preserves range scans most directly?
2. What does consistent hashing bound?
3. When is target state allowed to become authoritative?
4. Why must placement eligibility precede hashing?

## Explained answers

1. Range partitioning.
2. Expected key movement for membership changes; not hot-key load or replica safety.
3. After catch-up and independent data, version, permission, and invariant
   verification satisfy the cutover gates.
4. Hashing across forbidden regions can satisfy balance while violating
   residency or isolation.

## Sources and next work

Use Dynamo's partitioning sections and the Meta Shard Manager case. Next study
skew and fairness when balanced key counts still produce unbalanced work.
