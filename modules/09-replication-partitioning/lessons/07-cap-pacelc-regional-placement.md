lesson_id: L07

# CAP, PACELC, Regional Placement, Security, and Cost

## Outcomes

- Use CAP and PACELC as scoped reasoning tools rather than product labels.
- Make partition and normal-operation choices per operation.
- Include regional failure domains, residency, authorization, latency, and cost.

## Prerequisites

Module 5 partitions/latency, Module 8 authority/recovery, and Lessons 1–6.

## Mechanism and decision procedure

Gilbert and Lynch formalize an asynchronous model in which messages may be lost
and prove that a read/write object cannot provide both atomic consistency and
availability during a partition. The definitions matter. Atomic consistency is
linearizability. Availability requires every request to a non-failing node to
eventually return a non-error response. A product's 500-ms SLO or ability to
return an explicit error is a different measure.

CAP does not say "pick two" for normal operation, does not classify an entire
product, and does not decide data durability, recovery, or latency. Network
partition tolerance is not a removable feature when nodes communicate over a
fallible network; the operation policy chooses what happens when required
communication is unavailable.

PACELC adds the ordinary case: if partitioned, choose the operation's
availability/consistency behavior; else, choose how remote coordination trades
latency against consistency. Apply both branches to each operation:

1. State the operation, invariant, and formal/product availability definitions.
2. Name the partition and delay model.
3. Decide which sides may read/write and what errors or stale markers appear.
4. In normal operation, list synchronous hops and latency/failure-domain cost.
5. Add residency eligibility, authorization, encryption/key boundaries, audit,
   deletion propagation, and incident access.
6. Quantify storage copies, cross-region bytes, write/read amplification,
   repair, egress, standby capacity, and on-call ownership.

Data residency is a policy and evidence obligation, not a region name. Record
data classes, allowed locations, replicas/backups/logs/indexes, encryption keys,
administrative paths, deletion objective, audit proof, and policy owner. Obtain
legal/security review for real claims; the lab cannot prove compliance.

## Worked example

Northstar's public browse remains available on both sides of a partition with a
visible observation version and bounded-staleness policy; writes may queue or
be rejected depending on the operation. Controller-window changes reject on a
side without the known authority. Private researcher metadata is stored and
backed up only on eligible nodes, and repair refuses an ineligible destination.

In normal operation, Northstar accepts 80-ms extra coordination for controller
changes but not for public browse. The ADR calculates replica storage, cross-
region update/repair bytes, capacity reserve, and the owner who approves an
emergency residency exception.

## Common expert mistakes

- **Labeling a database CP/AP:** different APIs and configurations admit
  different histories and errors.
- **Treating latency as a partition:** delay thresholds are policy; the formal
  model allows unbounded delay.
- **Using CAP to justify data loss:** CAP does not define durability or backup.
- **Equating region with residency:** logs, backups, keys, support access, and
  derived indexes may cross boundaries.
- **Ignoring normal-operation cost:** synchronous remote copies consume latency
  and capacity even when nothing is broken.

## Guided practice

Write separate PACELC statements for controller transfer, operator refresh,
public browse, and private metadata. Calculate monthly bytes for two extra
copies and one repair pass. Create a residency inventory including backups,
logs, indexes, and keys. Complete EX-14 and EX-15.

## Self-check

1. What consistency property does the CAP proof use?
2. Does an explicit error satisfy formal availability?
3. What question does PACELC add?
4. Name three non-primary locations relevant to residency.

## Explained answers

1. Atomic consistency/linearizability.
2. No; availability requires a non-error response from every non-failing node.
3. The latency/consistency choice during normal, non-partitioned operation.
4. Backups, logs, derived indexes, caches, key stores, and administrative exports
   are all relevant examples.

## Sources and next work

Read Gilbert/Lynch and Abadi's PACELC paper using the bounded assignments. Next
turn the operation table and evidence into a reversible organizational decision.
