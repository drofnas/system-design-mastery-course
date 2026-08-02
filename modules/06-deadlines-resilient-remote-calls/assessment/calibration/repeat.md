# Beacon Dispatch Repeat Fixture

## Submission identity

Casey submits `fixture-m06-repeat` with no baseline tag, no immutable manifest,
and no evidence that predictions predate results. The text claims a production
run but provides only edited summary prose.

## Overwritten baseline and inconsistent evidence

The “baseline” says “updated after testing.” It reports 10 logical requests,
30 initial attempts, 40 retries, and 50 total attempts; the arithmetic is false.
The retry graph resets a 420 ms timeout at three layers and permits unlimited
immediate retries. No seed, raw output, hash, or evidence-kind label exists.

## Duplicate effect and false completeness

Two concurrent reservation calls with the same key create two authoritative
unit allocations. The response still says “dedup succeeded.” Missing required
road data is returned as a complete clear-road status. Idempotency state is an
expiring local cache separate from the effect, and authorization is not checked
on replay.

## Unbounded cancellation and missing fault work

After caller cancellation, child work continues indefinitely and permits are
not released. The pool and queue have no bounds. Only a happy-path screenshot is
submitted; F01–F06 raw and repaired trials, policy alternatives, migration,
rollback, defense, Gate 2 revision, and remediation record are absent.
