---
lesson_id: L08
title: Asynchronous Architecture Decisions
week: 44
---

# Asynchronous Architecture Decisions

## Outcomes

- Compare synchronous, queue, log, choreography, and orchestration options.
- Design migration, rollback, observability, security, cost, and ownership.
- Defend a decision with reversal evidence and teach the reasoning.

## Prerequisites

Lessons 1–7 and completed immutable failure evidence.

## Decision procedure

Begin with user outcome, authority, invariant, latency, failure, recovery, and
ownership—not a preference for events. Compare at least a simple synchronous or
single-database option, a bounded queue option, and a retained-log/workflow
option using the same drivers.

For each candidate state:

- commit and acknowledgement semantics;
- ordering, idempotency, replay, poison, and reconciliation;
- normal/peak/recovery capacity, storage retention, and unit cost;
- authentication, producer/consumer authorization, tenant isolation,
  encryption, sensitive payload minimization, audit, and deletion propagation;
- SLOs for publication lag, oldest age, poison ownership, workflow age, effect
  ambiguity, reconciliation drift, and recovery;
- schema compatibility, deployment order, operator controls, and owners.

Migrate with shadow publication, stable identities, dual-read comparison rather
than unsafe uncoordinated dual authority, bounded backfill, reconciliation,
canary consumers, rollback while old authority remains valid, and explicit
decommission gates. Reversal thresholds must be measurable.

## Worked example

Northstar rejects direct dual writes because F01 exposes loss. It compares a
database worker queue with a retained log. Independent replayable catalog and
analytics consumers plus tested backlog recovery justify the log; bulletin
effects retain their own idempotency contract. Migration publishes shadow
events, compares projections, then cuts reads over. The registry remains
authority until two clean reconciliation periods and rollback rehearsal pass.

## Common expert mistakes

- **Select a broker as modernization:** no workload or ownership driver supports it.
- **Ignore deletion/privacy:** retained payloads and dead letters outlive source data.
- **Make rollback "republish":** incompatible consumers or duplicated effects
  can make that unsafe.
- **Assign ownership to a platform team:** domain teams still own event meaning,
  schemas, poison decisions, and reconciliation.

## Guided practice

Use shared drivers to compare direct call, database queue, retained log, and
workflow engine for an archival-processing system. Define two dissenting views,
one migration rollback, and three reversal thresholds.

## Self-check

1. When is synchronous work preferable?
2. Who owns poison records?
3. What permits decommissioning the old path?

## Explained answers

1. When one authority and latency budget fit, failures can be returned directly,
   and asynchronous recovery/independent consumption do not justify complexity.
2. The domain owner decides meaning and repair, with platform support for safe
   storage and tooling; ownership cannot end at the broker.
3. Compatibility, shadow comparison, reconciliation, load/failure evidence,
   rollback rehearsal, and an agreed observation period—not elapsed time alone.

## Sources and next work

Study RES-06, complete EX-16, write the RFC, conduct the defense, and preserve
evaluation and remediation separately.
