---
lesson_id: L04
title: "Versions, Conflicts, Repair, and Convergence"
---

# Versions, Conflicts, Repair, and Convergence

## Outcomes

- Distinguish stale versions from concurrent siblings.
- Preserve conflicts until a valid ordering or domain merge exists.
- Compare read repair and anti-entropy by coverage, latency, and operating cost.

## Prerequisites

Lessons 1–3, Module 7 tombstones/compaction, and Module 8 authoritative versus
derived state. Detailed logical clocks are deferred to Module 10.

## Mechanism and decision procedure

Replication needs metadata that answers at least: which object, which version,
which replica or authority produced it, and whether one version supersedes
another. A single counter from one authority can order that authority's writes.
Multi-writer systems need richer causal metadata or must retain ambiguity. This
module treats causal context as an input; Module 10 derives clock algorithms.

When replicas disagree:

1. Validate object identity and authority.
2. Determine whether one version causally supersedes another.
3. Preserve incomparable siblings; never silently choose by arrival order.
4. Apply only a documented, associative/idempotent domain merge when valid.
5. Record resolution provenance.
6. Repair all intended replicas and verify convergence with an independent
   digest or version inventory.

Read repair compares replicas contacted by a read and may update stale copies.
It is workload-dependent: cold keys may never be repaired. Anti-entropy scans
or compares ranges in the background, often using hierarchical hashes to find
differences. It provides broader coverage but consumes CPU, I/O, network, and
storage; it needs scheduling, admission control, completion telemetry, and an
owner. Hinted handoff helps missed writes but is not a complete repair proof.

Convergence evidence names the expected replica set, pre-repair versions,
comparison method, bytes/keys transferred, rounds, post-repair versions, and
remaining divergence. "Repair completed" is a process result, not an invariant
unless the state is independently checked.

## Worked example

During a partition, Northstar's west and east sites edit one scientific
annotation from the same base. Neither edit supersedes the other. The broken
policy chooses the last arrival and loses scientific work. The repaired policy
stores both siblings, shows a conflict state to authorized scientists, records
their merged annotation with both parent versions, and runs anti-entropy. A
digest and per-replica version check demonstrate convergence.

Exposure browse uses read repair for frequently read stale metadata, but the
operations team still schedules anti-entropy because cold private records also
require completeness. Repair traffic has a bounded budget so it cannot starve
foreground controller operations.

## Common expert mistakes

- **Last-write-wins without a valid clock/order:** clock skew or arrival order
  discards valid concurrent work.
- **Calling retries conflict resolution:** retries may create more versions.
- **Depending only on read repair:** cold keys remain divergent.
- **Treating a Merkle-tree match as authorization:** equality does not prove
  data was permitted in that region.
- **Repairing derived indexes while authority diverges:** rebuild from a single
  verified authority only after authoritative convergence is settled.

## Guided practice

Given three versions—base v1, west v2 derived from v1, and east v2 derived from
v1—classify supersession and concurrency. Design a merge record and a repair
verification table. Calculate the foreground capacity consumed by 10,000
1-KiB repairs in a 60-second window. Complete EX-07 and EX-08.

## Self-check

1. Does a larger wall-clock timestamp prove causality?
2. Why can read repair leave divergence forever?
3. What makes a merge rule defensible?
4. What evidence demonstrates convergence rather than repair activity?

## Explained answers

1. No. Clock error and concurrent writers can make timestamps misleading.
2. A key that is never read is never compared.
3. It preserves the domain invariant, is deterministic under repeats/order,
   records provenance, and has tests for concurrent input.
4. The intended replica inventory and independent post-repair version/digest
   equality, with exclusions and errors recorded.

## Sources and next work

Read the Cassandra Dynamo and Repair documentation plus Dynamo Sections 4.4–4.7.
Next connect replica sets to key placement and safe ownership change.
- RES-05 -- Dynamo Architecture and Repair, for the local mechanism boundary.
