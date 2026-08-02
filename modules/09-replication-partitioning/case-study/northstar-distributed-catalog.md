# Northstar Distributed Observation Catalog

## Problem and isolation

Northstar now operates telescope sites in west, central, and east regions. The
catalog stores controller-window authority, public exposure metadata,
scientific annotations, and researcher-private metadata. It extends Module 8's
non-commerce observatory case and contains no products, inventory, checkout,
orders, payments, merchants, or capstone solution.

Do not continue until the learner's independent Week 33 commerce baseline is
frozen. This is one defensible design, not a required architecture.

## Workload, topology, and failure model

- Three sites with 99.5% of reads local to their region
- 1,200 exposure writes/night and 18,000 public reads, with a 30× burst for one
  newly discovered object
- 70 controller-window changes/night; 24 concurrent ingest sessions
- Up to 600 concurrent annotation edits during a coordinated campaign
- Delay, loss, replica partition, stopped known leader, lost response, hot key,
  stale routing, and reshard during load are in scope
- Byzantine faults, malicious database administrator, disk-durability proof,
  automatic leader election, fencing, and legal-compliance certification are out
  of scope

The lab uses logical ticks, toy objects, and nodes n1–n3. Production numbers are
inputs to a separate capacity and cost model, not conclusions from the toy run.

## Operation contracts

| Operation | User/invariant | Contract | Cannot meet contract |
|---|---|---|---|
| Transfer controller window | one active owner | current authoritative/linearizable single-key decision | reject and retain last-known marked read |
| Publish then refresh exposure | author sees acknowledged version | read-your-writes and monotonic reads | route, wait within deadline, then explicit error |
| Browse public exposure | useful recent catalog | at most two versions or 30 seconds stale | mark stale, degrade browse, or reject beyond bound |
| Reply to annotation | reply never appears without parent | causal parent visibility | wait/reject; never publish orphan reply |
| Edit annotation at disconnected sites | no valid scientific work silently lost | preserve concurrent siblings | expose conflict for authorized domain merge |
| Read/write private metadata | confidentiality and placement | eligible-region replicas plus session contract | reject ineligible route and audit |

Each acknowledged session write returns a minimum-version token. A read presents
the token; routing chooses a sufficiently advanced eligible replica, waits, or
fails. Sticky routing is an optimization, not the guarantee.

## Replication and acknowledgement choices

Controller ownership has one known authority and two replicas. Success waits for
the leader and one eligible durable replica. If the leader stops, Northstar does
not let a follower accept authority-changing work. Module 10 will design and
prove safe failover.

Public exposure metadata has one write leader with asynchronous remote followers.
Acknowledgement means the authority has met the local durable boundary; remote
visibility is separately measured. Browse reads may use followers under the
staleness rule.

Annotations accept multi-site writes because disconnected scientific work is a
real requirement. Concurrent siblings retain their parents and site identity.
An authorized scientist creates a merge record referencing both parents; replay
of the same resolution is idempotent.

Private metadata uses a leaderless in-region set for selected operations. N/R/W
are calculated only after filtering nodes by region and authorization.

## Quorum assumption ledger

For the annotation fixture N=3, R=2, W=2. Read/write and write/write sets
nominally intersect. Northstar records these additional assumptions:

- all clients use the same versioned replica map;
- responses come from the normal eligible set, not arbitrary substitutes;
- write acknowledgements meet the stated durable boundary;
- reads compare all returned versions rather than taking the first;
- concurrent siblings remain visible;
- partitions have an operation deadline and an explicit error policy;
- hinted data is temporary and anti-entropy verifies normal ownership later.

The arithmetic does not establish controller linearizability or failover safety.

## Conflict and repair procedure

Read repair updates a stale replica contacted by a read. It is insufficient for
cold records. A background anti-entropy job compares owned ranges, transfers
missing versions, and verifies post-repair digests. It has a tenant-aware
admission budget and yields to controller operations.

The F01 repaired trial rejects unsafe minority work, retains two annotation
siblings, performs two repair rounds, and converges. The modeled byte count is
not a production transfer estimate. Production evidence must include key count,
bytes, comparison cost, retransmission, foreground interference, completion age,
and authorization failures.

## Placement and resharding

Public observation IDs use stable hash placement. Private records first filter
candidate nodes by policy, then hash. Discovery-time range placement was
rejected for the live catalog because new observations concentrated in the
current range, though it remains useful for a separate immutable archive scan.

To add a node, Northstar freezes old/target maps, provisions capacity and access,
copies selected keys while old ownership remains authoritative, catches up
concurrent changes, verifies counts/versions/digests/permissions/invariants,
canaries reads, shifts writes, and retains the old path for rollback. Missing
keys, duplicate authority, erased siblings, session regression, or ineligible
placement stops cutover. Decommission follows reconciliation and the rollback
window.

## Hot-key and tenant response

Transient-42 creates a 30× read burst. Because its public metadata is immutable
for the relevant window, Northstar serves it from authorized replicas and a
bounded cache with version markers. Private controller capacity has an explicit
reserve; excess public work rejects first. The controller ownership key is not
salted because independent authorities would violate the invariant.

Required telemetry includes per-key/node/tenant work, accepted and rejected
operations, useful-work ratio, replica lag, repair work, and the identity of the
scarce resource.

## Regional, security, and cost reasoning

The placement inventory includes primary records, replicas, hints, logs,
backups, indexes, caches, encryption keys, support exports, and repair staging.
Private records and every derived/durable copy stay within eligible locations.
Repair checks destination eligibility. Emergency exceptions expire, are audited,
and have a security-policy owner.

The cost model covers storage copies, cross-region writes, reads, repair passes,
standby capacity, routing metadata, monitoring, and on-call work. Normal
operation accepts remote coordination latency only for operations whose
invariant needs it. Public browse does not pay the controller-write policy.

## Failure-pair conclusions

| Pair | Broken observation | Isolated repair | Oracle |
|---|---|---|---|
| F01 partition | one concurrent annotation lost | reject unsafe side, preserve siblings, anti-entropy | intended replicas hold resolved version/parents |
| F02 leader stopped | follower invents authority | fail closed and recover known authority | no unauthorized owner/version |
| F03 lag | session reads v2 then v1 | minimum-version token | required ≤ observed; no regression |
| F04 lost ack | blind retry duplicates effect | identity/version read-back | one logical effect and stable response |
| F05 hot key | load 120/5/5, no reserve | replica reads plus tenant reserve | private objective holds; ratios bounded |
| F06 reshard | missing keys and duplicate authority | consistent placement plus staged transfer | every key present with one authority |

## Decision and acceptable alternatives

Northstar's per-operation choices follow its workload and failure model. A
single regional authority, a consensus-backed store, a managed globally
distributed database, or conflict-free data type could also be defensible if it
meets the same invariants and shows evidence for latency, durability, conflict,
placement, migration, ownership, and cost. The case does not settle the
learner's commerce choices.
