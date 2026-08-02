# Week 43 Worksheet: Messaging Failure Matrix

## Evidence protocol

1. Preserve the Week 41 commit and F01–F09 predictions.
2. Hash every scenario before execution.
3. Run broken and repaired variants with the same seed/shared input.
4. Store raw trial JSON without editing it.
5. Recalculate identities, offsets, effects, versions, lag, workflow states,
   watermarks, reconciliation diffs, and all I01–I12 invariants.
6. Explain first divergence, causal mechanism, alternatives, repair, and limits.

## Pair matrix

| Pair | Prediction commit | Shared input hash | Changed control | First divergence | Broken invariant | Repaired proof | Remaining uncertainty |
|---|---|---|---|---|---|---|---|
| F01 | | | | | | | |
| F02 | | | | | | | |
| F03 | | | | | | | |
| F04 | | | | | | | |
| F05 | | | | | | | |
| F06 | | | | | | | |
| F07 | | | | | | | |
| F08 | | | | | | | |
| F09 | | | | | | | |

## Recovery calculations

For F05/F06 include attempts, oldest age, per-partition lag, `lambda`, `mu`, net
drain, overhead, serving reserve, and whether recovery is actually possible.

## Repair integrity

For every repair prove that it does not change workload/fault input, suppress
evidence, mutate authority, leak sensitive payloads, or shift unbounded work to
another component.
