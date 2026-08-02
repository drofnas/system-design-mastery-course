# Northstar Revise Fixture

## Submission identity

Artifact `fixture-m08-revise`, baseline `fixture-m08-revise-baseline`, Python
3.13. Required paths resolve, but two raw environment labels and backup-key
owner evidence are incomplete. Assistance is disclosed.

## Frozen model with gaps

N-01–N-06 and F01–F07 predictions predate results. Result/audit authority is
clear, but the controller predicate oracle and external-effect boundary are
only partly specified. High-contention sensitivity is absent.

## Histories and concurrency evidence

Lost update and write skew schedules are correct, with basic dependency edges.
The submission selects serializable controller changes but does not verify the
chosen vendor's retry code. Lock waits and deadlock victim are shown; retry is
whole-transaction and bounded, though jitter and starvation measurements are
missing. MVCC visibility is correct but old-version retention is not measured.

## Constraints and workflow

Result/audit commit atomically and window uniqueness is tested. Derived summary
rebuild works on one fixture. Telescope command is described as external, but
the durable intent's authorization replay and reconciliation evidence is thin.

## WAL and crash evidence

WAL-before-data and flush-before-ack are correctly explained. Redo is tested;
undo is inferred from code rather than a raw loser trial. Group-commit flush
arithmetic is correct but tail sensitivity is missing. The submission properly
limits hardware claims.

## Restore evidence gaps

Base and WAL identities, target, checksums, RTO 38 seconds, and RPO 0 are
reported for the small fixture. Archive continuity and N-01/N-03 probes pass.
Security credential isolation, dependency readiness, production-size replay,
and a second restore are missing, so the recovery claim needs revision but no
submitted invariant is shown failing.

## Failure matrix

All seven pairs exist and hashes match. F01–F05 have raw same-input reruns; F06
and F07 lack a discriminating alternative-cause rerun. Predictions remain
immutable. One environment field and two LSN-to-ack arithmetic explanations
need clarification, without an observed contradiction.

## ADR and defense gaps

The ADR compares three concurrency and two recovery choices with basic owners,
cost, migration, and rollback. Backup security, mixed-version isolation,
decommissioning, and quantified reversal thresholds are incomplete. The
defense answers application/database/on-call questions but lacks finance and
security challenge evidence, dissent resolution, and independent application.

## Revision boundary

The learner proposes dated addenda using Lessons 3, 6–8 and EX-06, EX-11,
EX-14–EX-16. No original baseline, raw trial, restore report, or ADR is changed.
