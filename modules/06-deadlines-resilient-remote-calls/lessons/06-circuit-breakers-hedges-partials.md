---
lesson_id: L06
title: "Circuit Breakers, Hedges, and Partial Results"
---

# Circuit Breakers, Hedges, and Partial Results

## Outcomes

- Evaluate stateful breakers by scope, sampling, probe, and recovery dynamics.
- Quantify hedge benefit against extra attempts and correlated failure.
- Design explicit complete, degraded, unavailable, and stale outcomes.

## Prerequisites

Lessons 1–5, conditional probability intuition, and workload/failure models.

## Mechanism

A circuit breaker converts recent observations into local admission state. It
can fail fast and reduce wasted work, but its window, scope, thresholds, and
half-open probes create a second control system. Many callers may open and probe
together; a broad breaker can reject healthy partitions; stale state can slow
recovery. Compare it with simpler concurrency limits, load shedding, and clear
overload responses before adoption.

A hedge issues a duplicate while the first attempt is still active. If tail
latency is caused by independent stragglers and spare capacity exists, a hedge
can improve the minimum completion time. Under correlated slowdown, it merely
duplicates load. Measure `p99_saved_ms / extra_attempt` and ensure idempotency,
cancellation of losers, and a separate hedge budget.

Partial results require a product contract. For each dependency mark required,
optional, substitutable, or stale-eligible. Responses must carry completeness,
age, and provenance; omission cannot silently become success.

## Decision procedure

1. Name the failure mode: fail-fast, slow, partitioned, overloaded, or straggler.
2. Measure correlation, spare capacity, and useful-work loss.
3. Compare bounded admission, breaker, hedge, fallback, stale data, and explicit failure.
4. Model synchronized state transitions and destination capacity during recovery.
5. Define required/optional response semantics and user consequence.
6. Run trigger, sustained-failure, recovery, and false-positive experiments.
7. Adopt only with owner, rollback, and measurable reversal gate.

## Worked example

Beacon refuses to hedge road calls during citywide congestion because slowdowns
are correlated and pool utilization exceeds 70%. Optional weather expires at
180 ms and returns `degraded(weather_omitted)`. Missing road data returns
`unavailable`, because dispatchers must not infer a road is clear. A road breaker
remains experimental until it reduces wasted slot-ms without rejecting healthy
district partitions or synchronizing probes.

## Common expert mistakes

- **Breaker as a universal best practice:** state and recovery can cause new outages.
- **Hedging at p99 unconditionally:** high load and correlation turn it into amplification.
- **Not canceling the losing hedge:** latency improves while cost doubles.
- **“Partial success” without a schema:** consumers treat missing required data as valid.
- **Stale fallback without age/provenance:** safety decisions use obsolete state.

## Guided practice

Compare two road-latency datasets: independent 1% stragglers with 45% spare
capacity, and region-wide 30% slowdown with 5% spare capacity. Propose a hedge
gate for the first and explain why it fails for the second. Define complete and
degraded response fields.

## Self-check

1. What new state does a breaker introduce?
2. When is a hedge likely harmful?
3. Why must partial results name missing required data?

## Explained answers

1. Observation window, closed/open/half-open state, probe schedule, and scope,
   each with synchronization and recovery behavior.
2. When slowness is correlated, capacity is scarce, effects are unsafe, or the
   losing attempt is not canceled.
3. Otherwise downstream consumers can mistake absence for a valid negative and
   violate the user or safety invariant.

## Sources and next work

- L. Huang et al., Metastable Failures in the Wild (RES-06), OSDI 2022.
- Google SRE, Addressing Cascading Failures (RES-05).
- Next: complete EX-10 and EX-11 and record a breaker/hedge reversal gate.
