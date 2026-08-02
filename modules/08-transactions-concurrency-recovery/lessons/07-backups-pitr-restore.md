lesson_id: L07

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

## Sources and next work

- PostgreSQL, [Continuous Archiving and PITR](https://www.postgresql.org/docs/current/continuous-archiving.html).
- GitLab, [Database outage postmortem](https://about.gitlab.com/blog/postmortem-of-database-outage-of-january-31/).
- Continue with EX-13–EX-14 and F07.
