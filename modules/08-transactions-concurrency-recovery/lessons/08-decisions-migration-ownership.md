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

## PESD 2.0 extension: modern constraints and ownership

PESD 2.0 adds **retention, deletion, legal holds, key rotation, logs, replicas, exports, backups, restore-time policy replay, and resurrection prevention**.

### Repeatable decision procedure

1. Inventory the affected data, tenants, identities, providers, jurisdictions,
   control planes, evidence owners, and cost owners before selecting a mechanism.
2. State the invariant and the authority that may change it. Separate a claimed
   policy from the enforcement point and from the evidence that proves execution.
3. Freeze a prediction, implement or model the named mechanism, and record the
   accepted evidence mode and runtime boundary.
4. Inject one policy, isolation, recovery, or supplier failure in addition to the
   module's mechanism failure. Preserve raw evidence before interpretation.
5. Compare at least two options across product outcome, technical mechanism,
   security and governance, operations and recovery, economics, ownership,
   migration, and reversal triggers.

### Non-capstone extension

Apply the procedure to the module's continuing case. Add one tenant or governed
data class, one supplier or control-plane dependency, and one deletion, recovery,
or exit obligation. The completed case may demonstrate the method, but its
topology, thresholds, policy choices, and answer are not defaults for Global
Commerce.

### Evidence boundary

Use `derived`, `executed_deterministic`, `measured_loopback`,
`measured_container`, `modeled_capacity`, `fixture_replay`, or
`measured_accelerator` exactly as defined by the course. Fixture replay supports
practice and remediation only. Modeled remote scale is not local measurement.
Every trial records commit and input/configuration hashes, runtime and resource
limits, clock, warm-up/repetition policy, raw outcomes, and limitations.

### Source boundary

Use the module's bounded primary sources and preserve the local evidence boundary.
