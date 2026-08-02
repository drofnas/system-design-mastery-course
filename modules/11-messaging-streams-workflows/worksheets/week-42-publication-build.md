# Week 42 Worksheet: Publication Build and Internals Review

## Observable contract

Implement the same observable contract as the reference lab in the learner's
chosen stack; do not copy its private implementation. Record authority/outbox,
publisher/log, consumer/inbox/projection, workflow, effect, watermark, poison,
and reconciliation interfaces.

## Atomic publication

Show schema, transaction pseudocode, commit evidence, stable envelope, publisher
checkpoint, retry behavior, retention, and a crash before/after commit.

## Consumer application

Show inbox uniqueness, projection transaction, offset order, external effect
key/read-back, stale/gap behavior, dedupe retention, and replay mode.

## CDC and storage

Record snapshot/position semantics, restart, retained-log capacity, schema
compatibility, credentials, privacy, cleanup, and owner. If polling rather than
CDC is used, explain which behavior differs.

## Tests and evidence

Include happy path, duplicate, lost acknowledgement, reorder, restart, invalid
schema, poison, replay, and reconciliation tests. Preserve commands, versions,
scenario/trial hashes, raw outputs, and cleanup evidence.

## Internals review

Trace one event from authoritative commit through derived state. At every
boundary name persistent/volatile state, atomicity, failure, retry, resource
bound, telemetry, security boundary, and unsupported production claim.
