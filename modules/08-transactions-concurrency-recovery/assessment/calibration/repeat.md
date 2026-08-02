# Northstar Repeat Fixture

## Missing identity and overwritten baseline

Artifact `fixture-m08-repeat` has no baseline tag, raw manifest, environment,
hashes, or assistance disclosure. The file says predictions were edited after
the trials to “match reality.”

## Incorrect isolation model

The submission claims snapshot isolation is serializable because the two
transactions update different rows. Both controller deactivations commit and
leave `certified_controllers = 0`, yet the report marks N-01 preserved. No
ordered history, dependency graph, abort, or retry exists.

## Unsafe locks and retry

F03 deadlocks. The application retries only the second statement inside the
aborted transaction, retains one stale application-side value, and leaks a
lock/connection. Attempts are immediate and unlimited. No cleanup or useful-
work evidence exists.

## Torn workflow and false atomicity

The result commits before its audit row. A process stop leaves one result and
zero audits. The report calls a later repair job “atomic.” It also claims a
database rollback can undo a physical telescope command.

## Lost acknowledged commit

F04 acknowledges before WAL flush. After termination the acknowledged result
is absent. The report deletes the failed trial and keeps a screenshot from a
clean run. LSN 9 is called durable while durable LSN is 6. A loser update
remains visible after recovery.

## Invalid restore served traffic

The restore uses an unverified stale replica, has a missing WAL segment and
checksum mismatch, runs no invariant/security probes, and enables traffic.
One acknowledged exposure is absent, the summary says 999, and controller
coverage remains zero. RTO/RPO are copied from a vendor page rather than
measured.

## Missing failure evidence

F01–F07 raw pairs, predictions, schedules, hashes, alternative causes,
same-input repairs, and uncertainty are absent. Reported arithmetic says two
commits plus two retries equals three attempts.

## Missing decision defense and remediation

There is no alternatives comparison, security boundary, cost, owner,
migration, rollback, restore runbook, teach-back, or defense. The proposal is
to replace the original artifacts with evaluator-written answers.
