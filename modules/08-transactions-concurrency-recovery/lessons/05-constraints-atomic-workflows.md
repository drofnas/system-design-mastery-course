---
lesson_id: L05
title: "Constraints, Authority, and Atomic Workflows"
---

# Constraints, Authority, and Atomic Workflows

## Outcomes

Choose enforceable constraints, keep required authoritative writes atomic, and
separate reconstructable state and external effects from the transaction.

## Prerequisites

Lessons 1–4 and Module 6 idempotency boundaries.

## Mechanism and decision procedure

Constraints are executable invariant fragments. Prefer declarative enforcement
at the authority: types/`NOT NULL`, `CHECK`, uniqueness, foreign keys, and
database-specific exclusion or deferred constraints. Application validation is
still useful for errors and authorization, but it cannot replace commit-time
protection against concurrent writes.

Partition a workflow into: authoritative facts that must commit together,
derived facts that can rebuild, and external side effects. Keep the first set
atomic. Mark derived state with provenance and reconcile it. For external work,
commit an idempotency/outbox intent and perform the effect outside the database
transaction with deduplication and repair.

## Worked example

Northstar writes exposure result and required audit row in one transaction, so
termination cannot publish only one. A completeness constraint/query is the
oracle. The nightly summary is updated asynchronously and carries the
authoritative result LSN. If it diverges, the reader marks it unavailable and a
job rebuilds it. Sending a telescope command inside the transaction would not
make the physical device action atomic.

## Common expert mistakes

- Relying on a pre-insert existence check instead of uniqueness.
- Treating an audit log as optional derived telemetry when it is required
  evidence.
- Dual-writing authoritative facts in two stores without a recovery protocol.
- Keeping a transaction open across remote work.

## Guided practice

Classify Northstar result, audit, summary, notification, and device command as
authoritative, derived, or external. Draw commit and reconciliation boundaries.
Name the constraint/oracle and failure repair for each.

## Self-check

1. Why is application validation still useful if a constraint exists?
2. Can an outbox make two systems one ACID transaction?
3. What must a derived record retain?

## Explained answers

1. It improves authorization and feedback, while the constraint remains the
concurrency-safe final guard. 2. No; it creates a durable intent and a
retriable/reconcilable workflow. 3. Authority identity/version or LSN, rebuild
rule, and freshness/validity state.

## Failure-mode bridge to the lab

Constraints are executable design decisions. A unique constraint, foreign key,
check constraint, exclusion constraint, or idempotency table turns an assumption
into something the storage system can reject. That matters because application
checks can be stale by the time a concurrent commit lands.

Atomic workflows extend the same idea beyond one database row. If a committed
fact must later trigger an email, shipment, message, or index update, the system
needs a durable handoff. Otherwise a crash can commit the fact and lose the
intent, or replay the intent twice. In the lab, separate authoritative facts
from derived effects. A repair should make the fact durable, make the effect
idempotent, and provide reconciliation for any derived state that can fall
behind. This is the bridge from transactions to M11's outbox and replay work.

## Second worked example

A payment row commits, then the process crashes before publishing
`PaymentCaptured`. If downstream fulfillment depends only on the event, the
order stalls. If the process publishes before commit, fulfillment can observe an
event for a payment that later aborts. The outbox pattern stores the event
intent in the same transaction as the authoritative fact. A relay publishes it
later, and consumers deduplicate by event identity. The transaction stays small,
but the workflow remains recoverable.

## Decision checklist

Name the durable fact, constraint, outbox or handoff row, relay retry behavior,
consumer idempotency key, and reconciliation query. Every external effect should
be either committed, retryable, or safely absent.

## Sources and next work

- PostgreSQL, DDL Constraints (RES-09).
- Continue with EX-09–EX-10 and F05/F06.
