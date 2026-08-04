# Runtime Comparison Report

## Decision and evidence identity

- Workload and user outcome:
- Commit, toolchain lock, host/container limits:
- Frozen prediction and raw-evidence paths:
- Assistance disclosure:

## Equivalent-work contract

Define logical input, required effects, success denominator, deadlines,
concurrency, payload, warm-up, repetitions, exclusion rules, and hashes.

## Execution-model map

| Runtime | Request scheduler | Blocking/CPU scheduler | Memory/release model | Cancellation owner | Validation boundary |
|---|---|---|---|---|---|

## Results

Report useful throughput, latency distribution, queue/in-flight work, memory,
allocation, GC where applicable, task/thread counts, cancellation, cleanup,
race/static diagnostics, and uncertainty. Preserve runtime-specific metrics.

## Failure evidence

Link broken/repaired pairs. Separate observation, causal interpretation,
alternatives, falsification, and remaining uncertainty.

## Operational decision

Compare safety, operability, ecosystem, security, cost, ownership, migration,
staffing, and rollback. State choice, alternatives, dissent, stopping
conditions, and measurable reversal evidence.

## Evidence boundary

State what the host, harness, detector, workload, and sample cannot prove.
