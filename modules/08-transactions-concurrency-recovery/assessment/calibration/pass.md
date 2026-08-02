# Northstar Pass Fixture

## Submission identity

Artifact `fixture-m08-pass`, frozen baseline `fixture-m08-pass-baseline`, Python
3.13 toy lab plus PostgreSQL 18 verification. All A01–A09 paths, raw hashes,
environment, evidence labels, and assistance disclosure resolve.

## Frozen invariant and transaction model

The pre-result baseline maps N-01–N-06 to authority, writers, minimal boundary,
constraints, concurrency adversary, oracle, and owner. It freezes F01–F07
predictions and low/base/high contention plus RTO/RPO assumptions.

## Histories isolation and validation

F01 and F02 contain ordered histories, visibility timelines, read/write and
predicate sets, serialization edges, and PostgreSQL-specific checks. The
submission distinguishes snapshot write skew from same-key lost update and
shows one full serializable retry from fresh authorization and snapshot.

## Locks MVCC and retries

Compatibility and wait-for evidence reproduces F03. The victim rolls back all
state and locks; canonical order plus at most three whole-transaction attempts,
full jitter, deadline/authorization recheck, and zero leaked resources completes
both workflows. Conflict sensitivity records useful commits and old-version age.

## Constraints and atomic workflow

Window uniqueness, result/audit keys, and completeness probes agree. F05 shows
separate commits fail and one authoritative transaction passes. Summary rows
retain source LSN and F06 detects, quarantines, rebuilds, and revalidates them.
External telescope commands use durable intents and reconciliation without a
false cross-system atomicity claim.

## WAL crash and durable acknowledgement

BEGIN/UPDATE/COMMIT/checkpoint records have ordered LSNs and checksums. Six
crash boundaries demonstrate redo winners and undo losers. Every acknowledged
commit LSN is at or below durable LSN. Group sizes 1/4/16 reconcile flush count,
commit tail, log bytes, and recovery work. Hardware boundaries remain explicit.

## Restore validation and objectives

The immutable first restore report identifies base checkpoint, required WAL,
archive continuity, target, versions, credentials, checksums, and isolated
environment. F07 blocks traffic on a missing segment, then a same-input repair
meets measured RPO 0 acknowledged operations and RTO 41.2 seconds for the stated
fixture. N-01–N-06, security, dependency, and user-journey probes pass.

## Seven pair evidence and diagnosis

All F01–F07 pairs preserve prediction commits, matching shared-input hashes,
distinct control hashes, raw trials, alternatives, one-control repairs,
discriminating reruns, invariant-first analysis, and uncertainty. Counts,
commits, aborts, retries, LSNs, acknowledgements, RTO, and RPO reconcile.

## ADR migration security cost and ownership

The ADR compares snapshot restructuring, serializable validation, and strict
locking plus logical and base+WAL recovery. It maps every invariant to retry,
durability, restore, telemetry, owners, backup encryption/credentials,
retention, abort/log/archive/restore cost, capacity, mixed-version canary,
rollback, decommissioning, exceptions, and measurable reversal thresholds.

## Teach back and remediation

The recorded defense derives F02 and F04 without AI, answers application,
database, security, finance, and on-call challenges, records dissent and a
changed belief, and shows another team applying the method. Score-4 extensions
are dated addenda; immutable evidence remains unchanged.
