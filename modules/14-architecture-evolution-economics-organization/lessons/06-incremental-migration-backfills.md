---
lesson_id: L06
title: "Incremental Migration and Backfills"
---

# Incremental Migration and Backfills

## Outcomes

- Model a migration as evidence-gated states rather than a date-based checklist.
- Build resumable, idempotent, rate-limited backfill work.
- Preserve one authoritative write path and reconcile derived state.

## Prerequisites

Use Module 8 logging and recovery, Module 11 idempotent workflows and replay,
and Module 12 stop conditions and operator safety.

## Mechanism: each state preserves a safe next move

Use the state sequence Baseline → Expand → Backfill → Shadow → Cutover →
Contract → Decommission. Each state defines allowed writers, read routing,
entry evidence, exit gate, stop condition, and rollback. A calendar milestone
cannot replace those properties.

A safe backfill unit has a stable source identity and version, deterministic
transformation, idempotency key, checkpoint, bounded batch size, rate limit,
attempt record, and reconciliation result. The cursor advances only after the
batch result is durable. Restart may repeat a completed batch; idempotency makes
that safer than skipping uncertain work.

Prefer a single authoritative write followed by an outbox, log, change stream,
or reconciled projection. If dual writes are temporarily unavoidable, name the
commit order, partial-failure states, repair log, source of truth, and date the
second writer is removed. Two successful API calls do not form one atomic fact.

## Worked example

Northstar inserts a versioned event seam after registry commit. Publication
approval remains a registry transaction. An outbox row contains observation ID,
registry version, contract version, and idempotency key. The projection applies
only a newer registry version.

Backfill snapshots IDs and versions, processes 500-record batches, persists a
cursor after durable projection writes, and reconciles count, missing IDs,
version lag, and content hashes. A crash after the projection write but before
the cursor repeats the batch; the version guard makes it a no-op. New live
events can overtake backfill, but older versions cannot replace newer state.

## Common expert mistakes

- **Using offset pagination on changing data.** Inserts and deletes can skip or
  duplicate items without a stable snapshot or key.
- **Advancing the cursor first.** A crash then permanently skips uncertain work.
- **Counting rows as reconciliation.** Equal counts can hide different records,
  versions, tenant scope, or content.
- **Leaving transition components forever.** Every router, mimic, duplicate
  field, and repair job needs an owner and removal gate.

## Guided practice

Write the Backfill state contract for Northstar. Include crash points before
write, after write, and after checkpoint, then predict restart behavior.

## Self-check

1. Why is state-machine language useful?
2. What makes a backfill resumable?
3. How does a version guard help live-plus-backfill races?
4. When is a dual write acceptable?

## Explained answers

1. It makes authority, allowed actions, evidence, rollback, and unsafe
   transitions explicit.
2. Stable work identity, durable checkpoints after effects, idempotency, bounded
   batches, and reconciliation.
3. It prevents an older backfill result from overwriting newer live state.
4. Only as a bounded transition with explicit partial failures, source of truth,
   repair evidence, monitoring, and removal date.

## Sources and next work

Complete RES-05, RES-06, and EX-11–EX-12. Implement the same contracts in the
reference lab before adapting them to an independent stack.
