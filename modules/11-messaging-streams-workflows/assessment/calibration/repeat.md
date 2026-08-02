# Northstar Repeat Fixture

## Submission identity

No frozen baseline exists. Raw outputs were edited after execution and fixture
names were used as diagnoses. Assistance and hashes are absent.

## Authority and semantics

The database and broker are dual-written. New event IDs are generated on retry,
and the submission claims the entire pipeline is exactly once.

## Build and evidence

The consumer advances offsets before local state. An external bulletin is sent
twice after a crash. Schemas, tests, immutable trials, and cleanup are absent.

## Failure pairs

Only happy-path screenshots exist. Seeds and controls differ between alleged
pairs; lag uses `B/mu` while arrivals continue; no invariant oracle is supplied.

## Workflow and recovery

Workflow progress is held in memory. Compensation deletes current state and can
repeat. Late records are silently discarded and poison records retry forever.

## Decision and defense

The RFC chooses events for scalability without alternatives, security, cost,
migration, rollback, ownership, reconciliation, dissent, or reversal evidence.
