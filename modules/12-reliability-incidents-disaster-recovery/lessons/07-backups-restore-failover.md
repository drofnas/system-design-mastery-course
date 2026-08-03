---
lesson_id: L07
title: Backups, Restore, Failover, and Failback
week: 47
---

# Backups, Restore, Failover, and Failback

## Outcomes

- Derive RPO and RTO from user/data consequence and measured evidence.
- Validate backup integrity, restore, authority, and reconciliation.
- Design fenced failover and independently verified failback.

## Prerequisites

Modules 8–11 and Lessons 1–6.

## Recovery procedure

Inventory authoritative data, derived data, effect ledgers, workflow progress,
configuration, credentials, schemas, and owners. Rank recovery by minimum user
service and safety, not component convenience.

RPO measures authoritative data exposure backward from disruption to the last
recoverable point. RTO measures from disruption to the declared minimum service,
including detection, decision, access, restore, replay, validation, routing, and
dependencies. Measure both from timestamps and versions; do not substitute the
backup schedule or vendor claim.

Validate a backup in isolation: identity, manifest, hash, schema, constraints,
row/version counts, log continuity, credentials, security controls, workflow
positions, and a representative transaction. Restore into a new namespace.
Reconcile authoritative versions, derived views, and external effects.

Failover transfers authority only after the new epoch is durable and stale
owners are fenced. Failback is a new migration: catch up, compare, probe, stage
routing, observe, retain rollback, and declare reconstitution.

## Worked example

Northstar backs up every six hours and retains minute-granularity changes. Its
five-minute RPO depends on usable change logs, not the base backup. An exercise
restores through version 808, proves no missing or duplicate authoritative
versions, issues epoch 43, rejects epoch 42 writes, reconciles catalog/effects,
and reaches minimum service in 39 minutes. Those observations support the RPO
and RTO only for the tested failure model.

## Common expert mistakes

- **Replica equals backup:** corruption or operator error can propagate.
- **Backup completed means recoverable:** no isolated restore has passed.
- **RTO is restore duration:** detection, access, validation, and routing vanish.
- **Fail back immediately:** stale or dual authority returns.
- **Restore data but not controls:** credentials, audit, and deletion policies fail.

## Guided practice

For an archive registry, declare RPO/RTO, backup and log cadence, restore order,
verification oracle, authority epoch, derived-state reconciliation, security
checks, staged failback, and three abort conditions. Calculate observed RPO from
last durable and last restored versions, not from intent.

## Self-check

1. What proves a backup is useful?
2. When does RTO stop?
3. Why fence the old owner?

## Explained answers

1. An isolated restore that passes data, schema, security, workflow, and sample
   service verification under the declared failure model.
2. When the defined minimum user service is safely available, not necessarily
   when full capacity or all background repair is complete.
3. Network delay or operator action can let it resume; a higher durable epoch
   makes stale work rejectable instead of relying on belief that it is stopped.

## Sources and next work

Study RES-06, complete EX-14–EX-15, and preserve F05–F09 recovery versions,
timestamps, epochs, hashes, approvals, and reconciliation as raw evidence.
