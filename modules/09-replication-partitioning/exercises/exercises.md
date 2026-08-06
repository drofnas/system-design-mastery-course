# Module 9 Guided Exercises

Use Northstar only. Freeze each response before opening the answer key.

## EX-01: Operation histories

Write violating histories for controller transfer, operator refresh, public
browse, and annotation reply. Name clients, versions, invocation/response order,
and the violated user outcome.

## EX-02: Weakest sufficient contract

Assign a measurable consistency/session contract and explicit failure response
to each EX-01 operation. Reject one unnecessarily strong choice.

## EX-03: Acknowledgement trace

Trace one write through acceptance, local persistence, remote receipt,
durability, acknowledgement, and follower visibility. Mark every unknown.

## EX-04: Topology comparison

Compare leader/follower, multi-leader, and leaderless designs for annotations
using latency, partition behavior, conflicts, repair, cost, and ownership.

## EX-05: Quorum arithmetic

For `(N,R,W)` values `(3,2,2)`, `(5,4,2)`, and `(5,2,3)`, calculate read/write
and write/write intersection separately.

## EX-06: Broken quorum assumptions

Take `(3,2,2)` and introduce stale membership, first-response reads, volatile
acknowledgements, and a sloppy substitute. Explain which conclusion fails.

## EX-07: Concurrent siblings

Classify base v1, west v2-from-v1, and east v2-from-v1. Design a resolution
record that preserves provenance and remains idempotent under retry.

## EX-08: Repair coverage and budget

Compare read repair with anti-entropy for hot and cold keys. Calculate the
minimum transfer time for 10,000 1-KiB objects at a 200-KiB/s repair budget.

## EX-09: Placement comparison

For eight named keys, calculate owners before/after adding one node using
modulo and the lab's consistent-hash function. Report moved-key ratio.

## EX-10: Reshard gate table

Define provision, copy, catch-up, verify, read-canary, write-cutover, rollback,
and decommission gates, with an owner and stop condition for each.

## EX-11: Session lag diagnosis

Given observed versions `[2,1]` after the session wrote version 2, count
read-your-writes and monotonic-read violations. Design routing/wait/rejection.

## EX-12: Ambiguous acknowledgement

A version-2 write commits but its response is lost. Compare blind retry,
version read-back, and idempotency-key reconciliation.

## EX-13: Hot-key and tenant fairness

For node loads `120/5/5`, calculate max/min and max/mean. Design a safe repair
for public immutable reads while preserving private controller capacity.

## EX-14: Partition decision matrix

For each Northstar operation, state behavior on the majority and minority sides,
formal/product availability, accepted staleness, and post-heal repair.

## EX-15: Regional placement and cost

Inventory primary data, replicas, logs, backups, indexes, keys, and support
access for private metadata. Calculate monthly storage and transfer from stated
assumptions; identify the policy owner.

## EX-16: ADR and defense rehearsal

Build a per-operation decision table and answer the frozen solo-review
challenges from data-platform, security/residency, finance, and on-call
perspectives. Record dissent, uncertainty, owners, migration/rollback, and one
quantified reversal threshold. A live panel is optional.
