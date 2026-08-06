---
lesson_id: L03
title: "Locks, Two-Phase Locking, Deadlocks, and Retries"
---

# Locks, Two-Phase Locking, Deadlocks, and Retries

## Outcomes

Derive lock compatibility and wait-for graphs, explain strict 2PL, recover from
deadlock, and implement bounded whole-transaction retry.

## Prerequisites

Lesson 2 dependency graphs and Module 6 deadline, jitter, and idempotency rules.

## Mechanism and decision procedure

Shared locks permit compatible readers; exclusive locks exclude conflicting
readers/writers. In strict 2PL, a transaction acquires locks and retains write
locks until commit or abort, preventing other transactions from observing an
uncommitted write. Predicate/range protection may be required when absence is
part of the invariant.

For each wait, add waiter→holder. A cycle is a deadlock. Detection aborts a
victim; rollback releases its locks. The application classifies the error,
confirms the operation is safe to retry, waits with bounded jitter, and begins
the entire transaction again with a fresh deadline and authorization check.
Canonical resource order reduces cycles, but timeouts are not proof that a
cycle cannot occur.

## Worked example

T1 locks telescope A then requests B; T2 locks B then requests A. The graph is
T1→T2→T1. Northstar chooses one victim, rolls it back, commits the survivor,
then retries the victim from its first read. Ordering telescope IDs avoids this
particular cycle; deadlock handling remains because other access paths exist.

## Common expert mistakes

- Treating a lock timeout as a deadlock detector.
- Retrying the last statement inside a transaction marked aborted.
- Assuming row locks protect a predicate over rows that do not yet exist.
- Holding locks while calling a slow external dependency.

## Guided practice

Construct compatibility and wait-for tables for two control transfers. Add a
third transaction, choose a deterministic victim only for the exercise, and
write retry eligibility, maximum attempts, time budget, jitter, cleanup, and
telemetry.

## Self-check

1. Why does canonical order reduce but not eliminate deadlocks?
2. What state must be reset before retry?
3. Why can a “check then insert” need predicate or uniqueness protection?

## Explained answers

1. Other code paths, database internals, and lock upgrades can introduce new
orders. 2. The whole transaction, snapshot, locks, authorization decision, and
deadline-derived work. 3. A concurrent row may appear after the check; a
constraint or protected predicate decides against commit-time state.

## Failure-mode bridge to the lab

Locks turn invisible conflict into explicit waiting. That is useful, but the
wait itself becomes part of the system. Two-phase locking can preserve
serializability when locks are acquired and released under the right discipline.
It can also create deadlocks when transactions acquire resources in different
orders. Retrying a deadlocked transaction is safe only when the operation is
idempotent or when the partial effects were never committed.

In the lab, do not stop at "there was a lock." Ask which resource was protected,
which transaction held it, which transaction waited, and whether the retry
replayed external effects. A good repair may be stable lock ordering, shorter
transactions, a unique constraint, or an idempotency key. The right answer
depends on whether the problem is contention, deadlock, duplicate effect, or a
missing invariant.

## Second worked example

Transaction A locks account 1 then waits for account 2. Transaction B locks
account 2 then waits for account 1. The system can abort one transaction to
break the deadlock, but the retry must not send a second receipt, enqueue a
second shipment, or charge a card twice. A stable lock order reduces the
deadlock. An idempotency key or outbox protects external effects. Shorter
transactions reduce the time locks are held, but they must not split the
invariant they were meant to protect.

## Decision checklist

Record lock order, lock duration, wait owner, abort policy, retry identity, and
external effects. A retry without idempotency is a new failure mode.

## Sources and next work

- PostgreSQL, Explicit Locking (RES-02).
- Continue with EX-05–EX-06 and F03.
