---
lesson_id: L04
title: "Transactional Outbox, Inbox, and Change Data Capture"
---

# Transactional Outbox, Inbox, and Change Data Capture

## Outcomes

- Implement one local transaction that records a fact and publication intent.
- Define restartable publisher and CDC checkpoint behavior.
- Apply a consumer event and inbox identity atomically.

## Prerequisites

Module 8 transactions/recovery and Lessons 1–3.

## Mechanism and implementation technique

Directly writing a database and broker creates two authorities with a crash gap.
The transactional outbox instead inserts the domain change and immutable event
intent in one database transaction. A publisher or CDC connector may repeat
delivery, but it cannot silently omit a committed fact while the outbox remains
queryable.

Minimum outbox columns are event ID, aggregate ID/version, type, schema version,
occurred time, public payload, and publication status/position. The publisher
must preserve event identity across retries. Deletion follows retention and
rebuild policy, not merely first publish success.

CDC derives changes from the commit log. Its correctness contract includes the
initial snapshot boundary, ordered commit position, slot/checkpoint durability,
acknowledgement, retained-log capacity, schema changes, access controls, and an
owner for lag or invalid positions.

At the consumer, begin a local transaction, insert `(consumer,event_id)` into an
inbox with a uniqueness constraint, apply the projection if inserted, and commit
before advancing external progress. An external side effect still needs an
effect-level identity.

## Worked example

Northstar's SQLite transaction updates observation version 3 and inserts
`evt-42`. A crash before commit leaves neither. A crash after commit leaves both,
and the publisher scan finds the pending row. The catalog transaction inserts
`(catalog,evt-42)` and version 3 together. A duplicate broker append is visible
but produces no second projection mutation.

## Common expert mistakes

- **Mark published before append:** a crash can suppress the only delivery.
- **Delete immediately:** replay, audit, and reconciliation lose their source.
- **Treat CDC slot as free:** stalled consumers retain logs and can exhaust disk.
- **Store inbox separately from projection:** a crash can mark consumed without
  applying, or apply without recording identity.

## Guided practice

Write transaction pseudocode for an approved maintenance record and outbox.
Then write consumer pseudocode with duplicate and crash branches. Identify what
must be atomic and what remains merely eventual.

## Self-check

1. Does an outbox prevent duplicate publication?
2. Which crash does the inbox repair?
3. What makes a CDC checkpoint meaningful?

## Explained answers

1. No. It prevents the fact/publication-intent gap; publication remains
   retryable and potentially duplicated.
2. Redelivery after local commit but before broker acknowledgement, provided the
   inbox and local effect committed together.
3. It resolves to a database commit position with compatible schema/snapshot
   state and enough retained log to resume.

## Sources and next work

Study RES-02 and RES-03, complete EX-07–EX-08, then build and inspect the the relevant lesson publication path.
