lesson_id: L08

# Transaction and Recovery Decisions

## Outcomes

Defend per-invariant isolation, constraint, retry, acknowledgement, backup, and
tested recovery choices with ownership, cost, security, migration, and reversal
evidence.

## Prerequisites

Lessons 1–7 and completed raw F01–F07 evidence.

## Mechanism and decision procedure

Build one row per invariant: authority, writers, transaction boundary,
constraint, admitted concurrency, retry rule, acknowledgement boundary, backup
material, tested target, telemetry, owner, and reversal evidence. Compare at
least three concurrency/enforcement options and two recovery options against
the same drivers.

Account for abort/wait cost, log/archive/storage cost, restore compute and
bandwidth, degraded capacity, on-call work, and security of backup data and
restore credentials. Assign application, database, security, and incident
owners. Migration uses additive constraints or validation, shadow invariant
probes, compatibility windows, canary traffic, rollback/roll-forward rules, and
decommissioning. Never change isolation or transaction boundaries across mixed
versions without analyzing both behaviors.

A decision reverses when measured anomaly risk, abort rate, lock tail, restore
time, archive gap, cost, ownership, or regulation crosses a declared threshold.

## Worked example

Northstar keeps narrow result/audit transactions, uses uniqueness for windows,
serializable controller changes, bounded full retry, flush-before-ack, and
verified base-plus-WAL recovery. It rejects global serializable mode because
exposure ingestion does not need it and abort cost would be unproven. The
coverage-row alternative becomes preferable if predicate aborts exceed the
budget and the hotspot remains within capacity. Restore ownership is shared by
database and incident leads; security owns credentials and isolated validation.

## Common expert mistakes

- Choosing one isolation level for the whole architecture.
- Ignoring mixed-version semantics during rollout.
- Optimizing commit latency by weakening an unstated durability promise.
- Assigning “the platform team” without a named operating interface.

## Guided practice

Compare snapshot plus restructuring, serializable validation, and strict
locking for N-01. Compare logical backup and physical base-plus-WAL recovery.
Run a defense with application, database, security, finance, and on-call
questions. Record dissent and the experiment that would resolve it.

## Self-check

1. What belongs in every invariant decision row?
2. Why can an isolation migration need a compatibility window?
3. What makes a recovery target defensible?

## Explained answers

1. Authority, boundary, enforcement, concurrency, retry, durability, recovery,
evidence, telemetry, owner, and reversal. 2. Old/new code can admit different
histories and retry behavior. 3. A stated workload/failure model plus measured
restore, integrity and business probes, RTO/RPO, and owned gaps.

## Sources and next work

- GitHub, [October 21 post-incident analysis](https://github.blog/news-insights/company-news/oct21-post-incident-analysis/).
- Google, [Testing recovery from data loss](https://docs.cloud.google.com/architecture/framework/reliability/perform-testing-for-recovery-from-data-loss).
- Continue with EX-15–EX-16, the ADR, and defense.
