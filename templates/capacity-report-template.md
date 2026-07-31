---
title:
module: "Capacity, Queues, and Tail Latency"
author:
prediction_commit:
experiment_commit:
status: draft
---

# Capacity Report

## Decision and user journey

Name the decision, user-visible outcome, and quality threshold.

## Workload and uncertainty

Record normal, peak, burst, projected, skewed, and failover workloads with
units, windows, sources, and confidence.

## Frozen prediction

Link the pre-experiment artifact. Restate, but do not rewrite, its predicted
bottleneck, capacity, concurrency, tail, and cost claims.

## Implementation and measurement boundary

Describe the fixed workers, bounded queues, fan-out, downstream limits, retry
policy, client location, clock, warm-up, duration, repetitions, and generator
limits.

## Results

### Load sweep

| % of measured capacity | Offered rate | Useful throughput | p95 | p99 | Queue slope | Rejected | Retry ratio |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 10 | | | | | | | |
| 25 | | | | | | | |
| 50 | | | | | | | |
| 75 | | | | | | | |
| 90 | | | | | | | |
| 100 | | | | | | | |
| 110 | | | | | | | |
| 125 | | | | | | | |
| 150 | | | | | | | |

### Failure matrix

| Failure | Prediction | Observation | User effect | Bound held? | Evidence |
|---|---|---|---|---|---|
| Slow requests | | | | | |
| Burst traffic | | | | | |
| Queue pressure | | | | | |
| Retry amplification | | | | | |
| Downstream limit | | | | | |
| Failover capacity loss | | | | | |

## Diagnosis

Separate observations from causal interpretation. Include competing
explanations and falsifying evidence.

## Safe operating region

Define the region jointly from latency, useful throughput, queue trend,
rejection policy, downstream bounds, retry budget, failover reserve, and cost.
State exclusions.

## Scaling signal and lead time

Name the signal, threshold, evaluation window, required action, action lead
time, owner, and stale or missing-signal behavior.

## Overload policy

State admission, priority, degradation, retry guidance, fairness, authorization,
and recovery behavior.

## Failover and recovery reserve

Show capacity after the stated loss and any backlog-clearance calculation.

## Cost per useful request

Include allocated hourly cost, unique successful work, normal/failover cost,
and low/base/high sensitivity.

## Ownership and rollout

Name owners for the service, load model, limits, downstream agreement, cost,
security review, and incident changes. Include staged rollout, rollback, and
configuration audit.

## Decision, risk, and reversal

State the choice, evidence, residual risks, rejected options, and measurable
conditions that require a new decision.

## AI assistance disclosure

- Tool:
- Assistance received:
- Verification performed:
