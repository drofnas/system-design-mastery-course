# Northstar Observatory Operations Registry

## Problem and isolation

Northstar coordinates public research observations across two telescopes. The
registry owns controller certification, control windows, exposure results, and
audit evidence. A nightly summary is derived. This case deliberately contains
no commerce entities or flows and is not a optional project answer.

Do not continue until the learner's transaction baseline is frozen. The
case shows one defensible design, not a mandatory architecture.

## Workload and failure model

- 18 controllers, two telescopes, 70 control-window changes per night
- 1,200 exposure-result commits per night, with a 12× burst after cloud cover
- At most four concurrent administrative changes and 24 exposure writers
- Process termination, deadlock, stale snapshot, operator corruption, and
  incomplete restore material are in scope
- Device destruction, malicious database administrator, regional loss, and
  distributed transaction atomicity are excluded from the local lab

## Invariants and authority

| ID | Invariant | Authority | Proof |
|---|---|---|---|
| N-01 | Every active observation retains at least one certified controller | controller assignment rows | serializable schedule or enforceable restructuring plus post-commit probe |
| N-02 | At most one controller owns a telescope window | window assignment constraint | uniqueness and concurrent insert test |
| N-03 | Every published exposure result has exactly one required audit record | result/audit transaction | atomic commit and completeness query |
| N-04 | An acknowledged result survives process restart | WAL and durable acknowledgement | commit LSN, flush evidence, crash, recovery probe |
| N-05 | The nightly summary equals authoritative committed results or is marked unavailable | result rows | hash/count comparison and deterministic rebuild |
| N-06 | A restore serves traffic only after target, integrity, and invariant probes pass | restore controller | backup/WAL identity, checksums, probes, traffic gate |

## Transaction boundaries

An exposure transaction writes the result and audit row together. Summary
updates are excluded because they are derived and can be rebuilt; making them
authoritative would enlarge contention and couple recovery to disposable state.

A controller-deactivation transaction reads all certified assignments for the
active observation and removes one assignment. Under snapshot isolation two
transactions can read two valid assignments, remove different rows, and both
commit. Their writes do not conflict, yet N-01 fails. Northstar chooses
serializable validation for this rare administrative operation. A schema
restructuring that locks one observation-coverage row would also be defensible.

## Lost update schedule

Two processors read `completed_exposures = 0`; each calculates 1; both write 1.
The final count is 1 although two result rows exist. A single atomic increment,
row lock, or version check repairs the schedule. Northstar treats result rows
as authority and the counter as derived, so it also validates and rebuilds the
counter rather than relying on it for correctness.

## Deadlock and retry

Two control transfers acquire telescope rows in opposite order. The wait-for
graph has T1→T2 and T2→T1. The database must abort a victim. The application
retries the entire transaction with bounded jitter only after rollback; it
does not retry the failed statement inside a partially observed transaction.
Canonical lock order reduces cycles but does not justify removing deadlock
handling.

## WAL and crash reasoning

Northstar's toy trace is BEGIN, UPDATE with before/after image, COMMIT, durable
flush, acknowledgement. Steal/no-force means an uncommitted update may reach
the data file and a committed update may not. Recovery therefore redoes
committed records and undoes loser records. Group commit may share one flush,
but no transaction is acknowledged beyond the durable LSN.

This establishes only a local host-level observation. Production evidence must
also cover OS, controller, device, filesystem, virtualization, and database
configuration assumptions.

## Backup and restore

The recoverable set is a checksum-verified base backup plus every required WAL
segment through the target. A replica cannot replace it because an operator
deletion can replicate. The restore procedure runs in an isolated environment,
verifies identities and checksums, replays to a named target, runs N-01–N-06
probes, rebuilds derived state, and only then permits traffic.

Northstar's local target is RPO 0 acknowledged operations and RTO 60 seconds
for the tiny fixture. Those numbers are tutorial thresholds, not credible
production objectives. Capacity, archive interval, transfer bandwidth, replay
rate, credentials, configuration, and downstream readiness determine a real
target.

## Decision and acceptable alternatives

Northstar uses narrow transaction boundaries, schema constraints for local
facts, serializable validation for the cross-row controller invariant, strict
locking for exclusive windows, bounded full retries, flush-before-ack, and
verified base-plus-WAL restore. It separates authoritative from rebuildable
state and names application, database, security, and on-call owners.

An observation-level coverage row, an append-only controller ledger, or a
database-specific constraint could be equally valid if concurrent evidence,
migration safety, and operating ownership support it. The exemplar does not
settle the learner's commerce choices.
