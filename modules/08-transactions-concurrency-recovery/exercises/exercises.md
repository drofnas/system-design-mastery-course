# Module 8 Guided Exercises

Complete these with Northstar only. Freeze independent commerce work before
opening the answer key.

## EX-01: Invariant enforcement map

Map N-01–N-06 to authority, writers, boundary, constraint, oracle, and owner.

## EX-02: Minimal transaction boundary

Classify result, audit, summary, notification, and telescope command as
authoritative, derived, or external; draw commit and repair boundaries.

## EX-03: Lost-update history

Write F01 as ordered reads/writes/commits, calculate expected and observed
counts, and identify the dependency that makes one update disappear.

## EX-04: Write-skew graph

Draw F02 snapshots and serialization edges. Explain why same-row write-conflict
detection is insufficient and compare two repairs.

## EX-05: Lock compatibility

Create a compatibility table for shared, exclusive, and update-intent locks;
apply it to an exclusive telescope window.

## EX-06: Deadlock and bounded retry

Draw F03's wait-for graph, choose a victim for the exercise, and specify whole-
transaction retry eligibility, attempt/time bounds, jitter, and cleanup.

## EX-07: MVCC visibility timeline

List versions visible to two controller transactions at begin, first commit,
validation, abort, and retry.

## EX-08: OCC sensitivity

Estimate useful commits and discarded work at 1%, 10%, and 40% conflict. State
the threshold that favors locking or a coverage-row restructuring.

## EX-09: Constraint design

Select local constraints for window exclusivity and result/audit identity. Mark
which cross-row invariant they cannot directly express.

## EX-10: Torn workflow and external effect

Repair F05, then add a telescope command and explain why the database
transaction does not make the command atomic.

## EX-11: WAL crash table

For crashes before log write, after update log, after data write, after commit
log, after flush, and after acknowledgement, list required redo/undo and allowed
client outcome.

## EX-12: Group-commit arithmetic

For 64 commits and batch sizes 1, 4, and 16, calculate minimum flushes. Name the
latency and failure assumptions missing from that arithmetic.

## EX-13: Recoverable set and RPO

Given a base at LSN 100 and archived segments 101–140 except 126, identify the
last continuous target and data-loss exposure relative to requested target 140.

## EX-14: Restore traffic gate

Define database, invariant, security, derived-state, dependency, and user-
journey probes with owners and fail-closed behavior.

## EX-15: Seven-pair diagnosis

Before results, classify F01–F07 by predicted invariant, observation points,
alternative cause, isolated repair, and uncertainty. After results, add only a
dated comparison and discriminating rerun.

## EX-16: Decision defense

Build the invariant decision matrix; compare three concurrency and two recovery
options; answer the frozen solo-review questions from application, database,
security, finance, and on-call perspectives. Record dissent, changed belief,
and a reversal experiment. A live panel is optional.
