# Week 7 Worksheet: Load Sweep and Failure Evidence

## Safety boundary

Run only against the local lab or an approved isolated environment. State CPU,
memory, duration, request-count, and data-safety bounds before starting.

## Reproducibility

- Code commit:
- Prediction commit:
- Python/runtime and host:
- Scenario files and seeds:
- Raw JSONL location:
- Warm-up, duration, repetitions:
- Clock and generator-lag check:

## Capacity discovery

Define measured capacity and show the coarse/fine trials that produced it.

## Required sweep

| Percent | Offered | Actual | Useful throughput | p95 | p99 | Queue slope | Rejected | Retry ratio | Generator p99 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 10 | | | | | | | | | |
| 25 | | | | | | | | | |
| 50 | | | | | | | | | |
| 75 | | | | | | | | | |
| 90 | | | | | | | | | |
| 100 | | | | | | | | | |
| 110 | | | | | | | | | |
| 125 | | | | | | | | | |
| 150 | | | | | | | | | |

## Failure matrix

| Fault | Frozen prediction | Injection | Observation | Bound | User effect | Raw evidence |
|---|---|---|---|---|---|---|
| Slow requests | | | | | | |
| Burst | | | | | | |
| Queue pressure | | | | | | |
| Retries | | | | | | |
| Downstream limit | | | | | | |
| Failover loss | | | | | | |

## Observation versus interpretation

List raw facts first. For every causal claim, name a competing explanation and
evidence that weakens it.

## Prediction errors

Do not edit Week 5. Record which predictions failed and why.
