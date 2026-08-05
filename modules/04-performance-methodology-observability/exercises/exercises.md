# Module 4 Guided Exercises

Complete these with the Transit Signal case. Freeze each answer before opening
the explained key.

## EX-01: Rewrite the question

Rewrite "the service is slow" as a user journey, metric, workload, comparison,
and time window. List what the question excludes.

## EX-02: Build a hypothesis ledger

Create three competing causes for a stable-throughput p95 regression. For each,
predict two signals and one falsifier.

## EX-03: Preserve equivalent work

Design a checksum or invariant that would detect an optimization which silently
drops one Transit route branch.

## EX-04: Bound experiment dimensions

Classify scenario seed, request schedule, process restart, host load, profiler
mode, and candidate order as controlled, randomized, measured, or excluded.

## EX-05: Validate trace context

Classify one valid `traceparent`, an all-zero trace identifier, an unknown
version with invalid length, and a missing context. State whether the service
continues a trace or starts a new one.

## EX-06: Correlate signals

Given one slow server span, a structured log, a latency histogram exemplar, and
a CPU profile, write the identifier path used to join them. State where exact
joining is impossible.

## EX-07: Set a cardinality budget

Estimate metric series for `operation × outcome × region`. Compare that with an
added `request_id` label for 30 requests/second over five minutes.

## EX-08: Measure instrumentation overhead

Design baseline and instrumented trials that estimate telemetry CPU, latency,
bytes, and series overhead without changing useful work.

## EX-09: Diagnose CPU versus lock contention

Choose the smallest combination of profile, process, lock-wait, and span
evidence that distinguishes the two causes. Name an ambiguous outcome.

## EX-10: Diagnose allocation versus connection retention

Explain how allocation snapshots, retained objects, active connections, and
descriptor deltas separate transient pressure from a leak.

## EX-11: Challenge a query plan

An indexed query is slower in one run. Name four explanations and a test that
preserves results, data shape, and cache boundary.

## EX-12: Freeze a blind diagnosis

For an opaque fault bundle, write observation, causal claim, alternatives,
confidence, and a discriminating rerun before viewing the fixture definition.

## EX-13: Define a regression budget

Define the metric, workload, environment, allowed ratio, uncertainty rule,
minimum repetitions, and action for a candidate change.

## EX-14: Review an optimization

Challenge a proposal that improves median latency but worsens p99, telemetry
cost, and failover CPU. Identify the decision drivers and owner.

## EX-15: Teach the causal model

Prepare a five-minute explanation that begins with the rider outcome, traces the
mechanism through resource evidence, and ends with uncertainty and reversal.
