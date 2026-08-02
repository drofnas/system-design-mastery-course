lesson_id: L04

# Optimistic Control, MVCC, Snapshots, and Write Skew

## Outcomes

Explain version visibility, implement optimistic validation, diagnose snapshot
write skew, and bound conflict/garbage-collection costs.

## Prerequisites

Lessons 2–3 and Module 7 record/version storage concepts.

## Mechanism and decision procedure

MVCC stores logical objects with version metadata. A snapshot selects versions
visible at a read timestamp; uncommitted versions from other transactions are
hidden. OCC records read/write sets in a private workspace, validates that the
assumptions still hold, then publishes or aborts.

Write-write validation protects one object. A predicate invariant also needs
read-write dependency tracking, predicate locking, or materialization into a
conflicting object. Long snapshots retain old versions; hot keys increase
abort cost. Measure useful commits, abort rate, wasted work, version retention,
and tail latency—not only uncontended throughput.

## Worked example

Northstar's two controller deactivations read the same predicate and write
different rows. Snapshot isolation preserves each transaction's view but not
the cross-row invariant. Serializable validation records each read predicate
and detects the cycle. An alternative creates one observation-coverage row
that both transactions update, converting predicate conflict into a direct
write conflict at the cost of a hotspot and migration.

## Common expert mistakes

- Saying MVCC means “readers never block” without vacuum/version limits.
- Validating only keys written, not predicates read.
- Retrying high-conflict OCC indefinitely and amplifying overload.
- Assuming timestamps imply wall-clock truth.

## Guided practice

For F02, enumerate versions visible to T1/T2, their read/write sets, validation
edges, and the abort. Compare serializable validation with a coverage-row
design under low, base, and high administrative contention.

## Self-check

1. Why can two non-overlapping writes still conflict logically?
2. What makes an OCC retry expensive?
3. Which metric reveals snapshot retention pressure?

## Explained answers

1. They can jointly falsify a predicate read by both transactions. 2. Work is
discarded after reads/computation, then repeated under continued contention.
3. Oldest active snapshot/version-retention age and retained bytes, paired with
cleanup lag and transaction age.

## Sources and next work

- CMU 15-445, [MVCC lectures and notes](https://15445.courses.cs.cmu.edu/spring2026/schedule.html).
- PostgreSQL, [MVCC introduction](https://www.postgresql.org/docs/current/mvcc-intro.html).
- Continue with EX-07–EX-08.
