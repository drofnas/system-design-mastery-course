---
lesson_id: L05
title: "Replay, Poison Records, and Reconciliation"
---

# Replay, Poison Records, and Reconciliation

## Outcomes

- Design replay across code, schema, effect, and retention boundaries.
- Quarantine poison records without losing ownership or blocking progress.
- Prove derived state converges by comparing it with authority.

## Prerequisites

L04 outbox/inbox and Module 9 repair.

## Mechanism and procedure

Replay is a migration and recovery operation, not simply resetting an offset.
Freeze the source range and hashes, select code/schema versions, disable or
idempotently gate irreversible effects, isolate capacity, write to a shadow
view when possible, compare with authority, then cut over or discard.

A poison record has a stable failure such as invalid schema or violated domain
precondition. Infinite retry pins progress and burns capacity. A bounded policy
records original bytes, identity, source position, attempts, classification,
owner, privacy/retention class, and the decision to repair, skip, or replay.
Dead-letter placement is an open work item, not success.

Reconciliation enumerates authoritative identities/versions and compares them
with projections and effect ledgers. It must detect missing, extra, stale, and
conflicting rows; produce idempotent bounded repairs; and rerun the oracle. Lag
alone cannot detect a change absent from the log.

## Worked example

Northstar quarantines an observation with unsupported schema version after
three attempts and advances the partition under an explicit policy. The owner
deploys a compatible transformer and replays into a shadow catalog. A daily
authority-versus-catalog comparison finds one missing version caused by a
dropped CDC record and rebuilds it from the registry, proving equal IDs,
versions, counts, and checksums afterward.

## Common expert mistakes

- **Replay into live effects:** old records resend notifications.
- **Skip poison silently:** the consumer appears healthy while business state is
  incomplete.
- **Trust counts only:** equal counts can contain different identities/versions.
- **Repair authority from a projection:** a derived bug can corrupt the source.

## Guided practice

Design a replay for an audit projection after a schema bug. Include source
freeze, compatibility, effect suppression, capacity, comparison, rollback, and
owner. Classify one poison record and one reconciliation diff.

## Self-check

1. Why is a dead-letter count of zero weak evidence?
2. When can replay bypass inbox deduplication?
3. What is the final reconciliation step?

## Explained answers

1. Records may have been dropped before quarantine, retention may have expired,
   or the consumer may not have observed them.
2. When rebuilding a new projection with a new consumer identity; irreversible
   effects still require suppression or stable keys.
3. Rerun the authority comparison and preserve proof that repairs converged
   without changing authoritative facts.

## Sources and next work

Complete EX-09–EX-10 and the replay/reconciliation sections of the workflow practice
worksheet before opening failure fixtures.
