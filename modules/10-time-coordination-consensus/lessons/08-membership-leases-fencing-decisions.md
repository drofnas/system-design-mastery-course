---
lesson_id: L08
title: "Membership, Leases, Fencing, and Coordination Decisions"
---

# Membership, Leases, Fencing, and Coordination Decisions

## Outcomes

- Prove quorum overlap through a membership transition.
- Audit lease assumptions and enforce monotonic fencing at the resource.
- Produce an operated coordination decision with migration and reversal gates.

## Prerequisites

Lessons 1–7 and Modules 1, 6, and 9 decision methods.

## Mechanism and decision procedure

Consensus safety depends on one membership definition. A direct old-to-new
switch can let disjoint quorums act. For old `{n1,n2,n3}` and new `{n2,n3,n4}`,
commit a joint configuration whose decisions require a majority of old and a
majority of new. Catch up new voters, verify the committed prefix, then commit
the new-only configuration. Limit concurrent configuration changes.

A lease grants permission for a time interval. Correctness depends on maximum
clock-rate error, synchronization uncertainty, communication delay, process
pause, renewal margin, and resource behavior. If any bound can fail silently,
the lease alone cannot protect correctness.

A fencing token is a monotonically increasing epoch attached to every resource
request. The protected resource stores the greatest accepted token and rejects
lower values. The token must come from an authoritative ordered allocation, and
every write path must enforce it. Fencing turns a stale owner from a correctness
failure into a rejected request.

Decision procedure:

1. Name operation-level safety/liveness and excluded faults.
2. Compare single authority/manual failover, transactional conditional update,
   managed coordinator, consensus log, and idempotent reconciliation.
3. Budget latency, quorum capacity, snapshots, membership, upgrades, security,
   audit, on-call, and cost.
4. Plan shadowing, backfill, dual-read verification, fenced cutover, rollback,
   and decommissioning; never rely on unverified dual authority.
5. Assign application, data/platform, resource, security, finance, and incident owners.
6. Publish reversal thresholds and dissent.

## Worked example

Northstar adds `n4` and removes `n1`. It first makes `n4` a non-voting learner,
copies snapshot/log state, verifies applied index and checksum, commits joint
`old+new`, exercises partition cases, then commits new-only. A rollback before
new-only returns through the joint configuration; afterward it is a new change.

Every telescope command carries committed epoch 44. A paused controller with
epoch 43 wakes and sends a validly authenticated command. Authentication proves
identity, not current authority; the mount rejects token 43.

## Common expert mistakes

- **Changing local config files independently.** Consensus quorums may no longer
  intersect under one history.
- **Checking the lease only at the client.** The stale process is precisely the
  component that cannot be trusted to self-reject.
- **Using authentication as fencing.** A credential can remain valid after
  authority changes.
- **Ignoring coordinator operating cost.** Snapshots, upgrades, certificates,
  quorum capacity, and membership incidents require owners and budget.

## Guided practice

For old `{a,b,c}` and new `{c,d,e}`, show a disjoint old/new majority. Then
write the joint quorum predicate. Design a fencing cutover for a database writer
whose old credential remains valid for ten minutes.

## Self-check

1. Why is one-step membership replacement unsafe?
2. Where must a fencing token be checked?
3. When is a single authority preferable to consensus?

## Explained answers

1. Old `{a,b}` and new `{d,e}` can decide independently with no shared witness.
   Joint decisions require `majority(old) AND majority(new)`.
2. At every protected-resource mutation boundary, against stored maximum authority.
3. When its failure/restore and manual-failover behavior meets the operation's
   objective at lower delivery and operating cost.

## Sources and next work

- Ongaro and Ousterhout, Section 6 and dissertation membership extension.
- Burrows, *The Chubby Lock Service*, Sections 2–5.
- Next: EX-16 and the decision worksheet turn the mechanisms into an RFC and defense.
- RES-07 -- The Chubby Lock Service for Loosely-Coupled Distributed Systems, for the local mechanism boundary.
