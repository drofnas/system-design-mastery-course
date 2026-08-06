---
lesson_id: L07
title: "Backups, PITR, Restore Validation, and Objectives"
---

# Backups, PITR, Restore Validation, and Objectives

## Outcomes

Build a recoverable base-plus-log set, distinguish replicas from backups,
measure RTO/RPO, and gate traffic on restore integrity and application probes.

## Prerequisites

Lesson 6 WAL/LSN reasoning and Module 1 recovery scenarios.

## Mechanism and decision procedure

A backup claim has four parts: recoverable material, independent retention and
access, a tested procedure, and an application-valid result. For physical PITR,
retain a consistent base backup plus every required WAL segment to the target.
Verify identity, version, configuration, permissions, encryption keys,
checksums, archive continuity, target, and timeline before replay.

RPO is the maximum authoritative change absent at the accepted restore point;
RTO spans detection, decision, provisioning, transfer, replay, validation,
derived rebuild, dependency readiness, and traffic enablement. Measure both
from an exercise. A replica helps availability but usually repeats deletion or
corruption and shares credentials/failure domains; it is not a sufficient
backup by label.

Restore into isolation. Run database integrity checks and business invariant
probes, rebuild derived state, test authorization and downstream compatibility,
record approvers, then open traffic. A successful backup job is input evidence,
not restore evidence.

## Worked example

Northstar F07 starts a stale base without a required WAL record and loses an
exposure. The repaired flow checks base/WAL identity and checksums, proves
archive continuity to the target LSN, replays, runs N-01–N-06, rebuilds the
summary, and only then enables traffic. Its local RTO/RPO apply only to the tiny
fixture; production objectives require production-sized transfer and replay.

## Common expert mistakes

- Equating green backup jobs with recoverability.
- Quoting vendor RPO/RTO without including detection and validation.
- Restoring secrets, callbacks, or jobs into a test environment unsafely.
- Treating failover and restore as the same operation.

## Guided practice

Draw a base/WAL retention timeline with one missing segment. Identify the last
valid target and calculate RPO. Create a restore gate with database, invariant,
security, derived-state, dependency, and user-journey probes plus owners.

## Self-check

1. Why can a healthy replica contain the same harmful deletion?
2. What must RTO include after replay finishes?
3. When should traffic remain blocked despite a running database?

## Explained answers

1. Replication copies authoritative writes, including mistakes. 2. Integrity,
invariant, security, compatibility, derived rebuild, and service validation.
3. Whenever target identity, archive continuity, checksums, invariants,
authorization, dependencies, or user-journey probes have not passed.

## Failure-mode bridge to the lab

Backups are not recovery until a restore has been tested. Point-in-time recovery
adds a target: restore a base backup and replay logs to the chosen moment. The
target must be precise enough to avoid replaying the corrupting operation while
still preserving required committed work.

Three failure modes matter in the lab. First, a backup can be present but
corrupt, incomplete, or missing the keys needed to read it. Second, a restore can
choose the wrong target and silently lose valid writes. Third, a restored system
can rejoin with stale authority and overwrite newer state. A strong recovery
answer includes integrity verification before selection, the required version or
timestamp, the observed RPO, the observed RTO, and the fencing rule for failback.
That turns "we have backups" into a testable recovery claim.

## Second worked example

A bad migration runs at 10:07 and deletes valid rows. The last full backup is
from 02:00, and logs are available through 10:30. Restoring to 10:30 faithfully
replays the deletion. Restoring to 10:06 may avoid the deletion but lose valid
writes between 10:06 and detection. A recovery plan should identify the exact
target, quantify accepted data loss, preserve the corrupt state for analysis if
needed, and fence the restored system until authority is clear.

## Decision checklist

Verify backup integrity, restore target, required version, excluded bad change,
RPO, RTO, credentials, encryption keys, and failback fencing. A backup that was
not restored is only an artifact.

## Restore drill

Run the restore story as a drill before the incident. Choose a backup, restore
it into isolation, replay to the target, verify application invariants, compare
row counts and checksums, and record the exact command path. Then practice
failback separately. The first drill usually reveals missing credentials, wrong
retention assumptions, undocumented dependencies, or operators who can read the
runbook but cannot complete the procedure under time pressure.

## Sources and next work

- PostgreSQL, [Continuous Archiving and PITR](https://www.postgresql.org/docs/current/continuous-archiving.html).
- GitLab, [Database outage postmortem](https://about.gitlab.com/blog/postmortem-of-database-outage-of-january-31/).
- Continue with EX-13–EX-14 and F07.
