# Module 4 Explained Answer Key

These are reasoning checks, not canonical architectures.

## EX-01

One defensible question is: "Under the 30 requests/second three-leg workload,
why did rider p95 rise from the preserved baseline by more than 15% while useful
throughput and outcome mix stayed stable?" It excludes unrelated journeys,
traffic changes, and claims about production scale.

## EX-02

CPU work predicts higher process CPU and a concentrated CPU profile. Lock
contention predicts lock-wait growth and serialized server spans. Slow I/O
predicts a widening dependency span without proportional CPU. A falsifier must
name evidence that would weaken the cause, not merely another metric to inspect.

## EX-03

Hash the ordered route identifiers, approved-impact versions, and response
payload. Compare successful request count and branch count too. A matching
latency with a changed checksum is different work.

## EX-04

Fix scenario and work; randomize or interleave candidate order; measure host
load and profiler mode; restart processes deliberately as a repetition level.
An excluded factor must be documented because it limits transfer.

## EX-05

Valid version `00` context continues when identifiers and length are valid.
All-zero identifiers are invalid. Unknown versions follow their length rules and
must not be parsed as version `00`. Missing or invalid context starts a new root
without failing the user request. Trace identity grants no authority.

## EX-06

Trace and span identifiers directly join logs to spans. An exemplar can link one
aggregated observation to a trace, but a histogram cannot reconstruct every
request. Profiles usually correlate through resource/time bounds unless the
format supports direct span links.

## EX-07

If there are 3 operations, 4 outcomes, and 2 regions, the upper bound is 24
series. A unique request identifier at 30/second produces up to 9,000 series in
five minutes before retries. Keep identity in traces/logs and aggregate metrics.

## EX-08

Interleave collection disabled and enabled under one schedule, preserve raw
samples, and compare process CPU, journey percentiles, bytes, and series count.
Report profiler modes separately because they have different overhead.

## EX-09

High CPU plus a concentrated hot stack and flat lock wait supports CPU work.
High lock wait with serialized spans and lower runnable CPU supports contention.
Both can rise when code performs CPU work while holding a lock; vary the
critical section to discriminate.

## EX-10

Transient allocation raises allocated bytes but releases retained objects and
connections after the trial. Connection retention leaves active connections or
descriptor count elevated. Memory can lag reclamation, so one RSS value alone
cannot classify the cause.

## EX-11

Cache state, selectivity, row count, stale statistics, and measurement noise are
credible explanations. Capture the plan and equivalent result checksum across
repeated cold/warm boundaries with a representative data distribution.

## EX-12

The frozen record separates observations from interpretation, cites exact
signal files, assigns confidence, and proposes a rerun whose outcomes distinguish
alternatives. Reading source first converts diagnosis into recognition.

## EX-13

A usable budget resembles: "For the declared route-impact workload on the same
host class, candidate p95 may not exceed baseline by 10% when the interval and
raw repetitions exclude zero improvement; otherwise block and investigate."
The exact statistic can differ, but action and uncertainty cannot be omitted.

## EX-14

Median improvement does not settle a rider p99 decision. Compare the actual
journey objective, saturation headroom, telemetry spend, and failover exposure.
The service owner accepts rollout; the observability owner accepts collection
cost and privacy; both name rollback evidence.

## EX-15

A strong teach-back moves from outcome to workload, observation, mechanism,
alternatives, discriminating test, validated change, and reversal. Vocabulary
without that chain does not demonstrate diagnosis.

## PESD 2.0 extension answer

A defensible answer covers telemetry as a governed data product: schema ownership, PII restrictions, retention, sampling bias, lineage, cardinality, and cost budgets. It distinguishes the
requirement, enforcement mechanism, evidence, and owner; keeps modeled and
measured results separate; and names the failed condition that would reverse
the decision. Different architectures are acceptable when their invariants,
evidence boundaries, migration, and residual risk are explicit.
