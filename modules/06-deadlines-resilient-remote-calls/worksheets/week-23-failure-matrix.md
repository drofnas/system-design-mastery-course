# Week 23 Remote-Call Failure Matrix

Preserve raw trials before interpretation and never rewrite the Week 21 freeze.

## Trial identity

- Frozen baseline commit:
- Code/config commit:
- Environment, seed, workload, and schema version:
- Raw trial hashes:

## Matrix

| ID | Fault | Invariant/prediction | Raw observations | Causal model and alternatives | Repair | Same-work rerun | Uncertainty |
|---|---|---|---|---|---|---|---|
| F01 | retry storm | | | | | | |
| F02 | pool exhaustion | | | | | | |
| F03 | dependency slowdown | | | | | | |
| F04 | partial response | | | | | | |
| F05 | duplicate request | | | | | | |
| F06 | cancellation leak | | | | | | |

## Required cross-trial calculations

Report logical requests, attempts, useful-work ratio, remaining-budget waste,
peak active/queued, rejections, fairness, effect count, duplicate conflicts,
cancellation drain, unit cost, and recovery time.

## Evidence integrity

Record scenario/trial hashes, changed variables, cleanup, and whether every
result is measured runtime evidence or deterministic model evidence.
