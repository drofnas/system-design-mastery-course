# Week 54 Migration Build Worksheet

## Contract and authority

- Public contract and semantic meanings:
- Supported producer/consumer pairs:
- Stored/replay population:
- Source of truth in every phase:
- Unsupported-version behavior:

## Expand-and-contract sequence

List expansion, tolerant readers, new writers, backfill, observation,
deprecation, rollback expiry, contraction, and evidence gates.

## Migration implementation

Implement Baseline, Expand, Backfill, Shadow, Cutover, Contract, and
Decommission states. For each, record entry, allowed writes, read path, exit,
stop, rollback, owner, and telemetry.

Backfill must expose stable identity/version, batch size, idempotency,
post-effect checkpoint, rate limit, retry, reconciliation, and restart evidence.
Shadow effects must be isolated and comparison normalization documented.

## Economics

Use the cost-model template. Show direct, shared, labor, transition, and risk
cost; good outcomes; allocation; formulas; sensitivity; break-even; threshold;
and owner.

## Tests and implementation review

Test invalid contracts, mixed versions, repeated batches, stale versions,
partial writes, mismatches, threshold crossings, rollback, dependency exit, and
owner loss. Record what the model cannot establish about production.
