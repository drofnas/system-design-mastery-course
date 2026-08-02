lesson_id: L05

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

## Sources and next work

- PostgreSQL, [DDL Constraints](https://www.postgresql.org/docs/current/ddl-constraints.html).
- Continue with EX-09–EX-10 and F05/F06.
