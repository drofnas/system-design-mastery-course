# Northstar Pass Fixture

## Submission identity

The manifest resolves A01–A09 to `m11-pass-4a1b2c3`; the frozen baseline tag,
environment, assistance, schemas, and all scenario/trial hashes are present.

## Authority and semantics

The registry owns publication facts; outbox intent commits atomically. Stable
event, inbox, workflow-step, and bulletin effect identities are retained. The
exactly-once claim is limited to local inbox/projection transactions.

## Build and evidence

The standard-library build exposes SQLite authority/outbox and inbox/projection
transactions, deterministic log positions, effects, workflow history, poison,
watermarks, metrics, and reconciliation. Tests and schemas pass.

## Failure pairs

F01–F09 predictions predate 18 immutable trials. Each pair shares seed/input,
changes one control, the broken target fails, and repaired I01–I12 pass. Drain
and watermark arithmetic recalculate.

## Workflow and recovery

Valid transitions, step keys, compensation, point of no return, manual review,
late-data corrections, bounded poison handling, and authority-led reconciliation
are evidenced without production overclaim.

## Decision and defense

The RFC compares direct, queue, log/choreography, and orchestration choices;
covers security, cost, migration, rollback, owners, dissent, telemetry, and
reversal; and preserves evaluation/remediation separately.
