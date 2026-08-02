# Week 39 Worksheet: Consensus Failure Matrix

Freeze predictions, scenario files, and shared-input hashes before execution.
Keep raw JSON immutable; interpretation and corrections are separate.

## Environment and provenance

- Implementation/version/source commit:
- Runtime/OS/storage/network model:
- Scenario and schema versions:
- Assistance disclosure:

## Pair matrix

| Pair | Frozen prediction | Shared input hash | Changed control | First divergence | Broken invariant | Repaired invariant | Alternative cause | Discriminating rerun |
|---|---|---|---|---|---|---|---|---|
| F01 leader termination | | | | | | | | |
| F02 stale partitioned leader | | | | | | | | |
| F03 restart persistence | | | | | | | | |
| F04 duplicate client | | | | | | | | |
| F05 delayed lease | | | | | | | | |
| F06 reordered append | | | | | | | | |
| F07 snapshot interruption | | | | | | | | |
| F08 membership replacement | | | | | | | | |

## Arithmetic and histories

Recalculate quorum sets, terms/votes, commit/application indexes, effect counts,
fencing comparisons, snapshot coverage, and membership overlap from raw data.

## Evidence boundary

List claims the model does and does not support: durability, real-time
availability, performance, Byzantine behavior, regional loss, and security
enforcement require separate evidence.

## Corrections

Append date, original claim, contradictory evidence, revised claim, and new
experiment. Never edit the original prediction or raw observation.
