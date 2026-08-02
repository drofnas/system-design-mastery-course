lesson_id: L01

# Invariants and Transaction Boundaries

## Outcomes

Map an invariant to authority, writers, a minimal atomic boundary, an
enforcement point, and a falsifiable proof. Distinguish database consistency
from application correctness.

## Prerequisites

Module 1 invariants and state ownership; Module 7 logical/physical data design.

## Mechanism and decision procedure

A transaction is a visibility and recovery boundary, not a bag of related
code. Start with a statement that can be false. Name the authoritative facts
needed to decide it, every concurrent writer, and the smallest update that must
be all-or-nothing. Then classify enforcement:

1. A local row/domain fact belongs in `NOT NULL`, `CHECK`, or a type boundary.
2. Key identity/exclusivity belongs in a unique or exclusion constraint.
3. A relationship may use a foreign key.
4. A multi-row predicate needs serialization, safe materialization into one
   lockable row, or a database-supported constraint.
5. An external effect cannot be made atomic merely by widening a database
   transaction; use an idempotent workflow and reconciliation later.

For each choice define a concurrent falsification test. An invariant without an
oracle is a hope; a transaction without a stated invariant is accidental
coupling.

## Worked example

Northstar N-03 says every published result has one audit row. Result and audit
are authoritative and share one database, so they commit together and a
completeness query is the oracle. The nightly summary is excluded: it is
derived, rebuildable, and would enlarge contention. N-01 spans controller rows;
snapshot visibility alone cannot enforce it, so the design needs serializable
validation or a lockable coverage-row restructuring.

## Common expert mistakes

- Calling a transaction “ACID” without naming the admitted histories.
- Putting network calls inside a transaction and assuming atomicity crosses the
  boundary.
- Treating a cache or summary as authority because it is convenient to query.
- Widening every boundary “for safety,” increasing lock duration and recovery
  work without proving a stronger invariant.

## Guided practice

For N-01, N-03, and N-05, fill in authority, writers, boundary, enforcement,
failure schedule, oracle, owner, and rollback. Mark which fact is derived.

## Self-check

1. Why is “the rows are consistent” not an invariant?
2. When is a schema constraint stronger than an application pre-check?
3. Why should a rebuildable summary usually remain outside the authoritative
   transaction?

## Explained answers

1. It has no falsifiable condition or named authority. 2. The constraint is
evaluated at the commit/write boundary against concurrent database state;
pre-checks can become stale. 3. Coupling it enlarges contention and recovery
scope while adding no authoritative correctness if it can be reconstructed.

## Sources and next work

- PostgreSQL, [Constraints](https://www.postgresql.org/docs/current/ddl-constraints.html).
- Continue with EX-01–EX-02 and Lesson 2; freeze the Week 29 map before the
  completed case or answers.
