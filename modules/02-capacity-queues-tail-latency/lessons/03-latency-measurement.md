---
lesson_id: L03
title: "Latency Measurement"
---

# Latency Measurement

## Outcomes

You can design an open-loop latency experiment, identify coordinated omission,
report generator error, and interpret percentile evidence with scope.

## Prerequisites

Lessons 1–2; percentiles and monotonic clocks.

## Mechanism

A latency distribution needs:

- population and operation
- start and stop boundary
- workload and environment
- observation window and sample count
- warm-up and repetitions
- treatment of timeouts, rejection, and missing observations
- measurement location and clock

A percentile is an order statistic. It does not mean “99% of the time,” predict
the next request, or describe requests omitted by the generator.

### Coordinated omission

A closed-loop generator waits for a response before sending the next request.
During a ten-second stall, it may record one ten-second request and issue no
other work. Real independent users would have continued arriving. The omitted
arrivals disappear from both throughput and latency data.

An open-loop generator assigns send times independently of completion. If it
cannot keep up, it must record generator lag:

```text
generator lag = actual send time - scheduled send time
```

Large lag means the offered workload was not achieved. Do not silently shift
the measurement start to actual send time; that hides waiting caused by the
generator or test host.

### Repeatable technique

1. Freeze the requested arrival schedule.
2. Use a monotonic clock for elapsed time.
3. Record scheduled, sent, admitted, service-start, and completed timestamps.
4. Keep rejection and timeout observations in the result.
5. Report p50, p95, p99, maximum, count, and useful throughput.
6. Report generator lag and actual offered rate.
7. Repeat and disclose host and configuration.
8. Compare open- and closed-loop only to demonstrate the bias; use open-loop for
   capacity decisions.

## Worked example

The Transit Signal scenario schedules 150 logical requests over five seconds.
Run it locally and treat the generated raw JSONL, metadata, and summary as the
only measured evidence. The seeded workload includes a 200 ms slow branch, so a
conforming run should preserve that qualitative tail mechanism, but its exact
percentiles and generator lag depend on the learner's host and load-generator
behavior. Do not copy reference microseconds into an empirical report.

Now imagine one closed-loop participant with 20 ms normal latency and a 2-second
stall. During the stall it records one slow observation. An open-loop 50/s
schedule assigns roughly 100 arrivals to the same interval. Those arrivals may
wait or be rejected; their user impact must remain visible.

## Common expert mistakes

- **Report only averages:** a small slow population can dominate user journeys.
- **Drop rejected work from the denominator:** overload appears faster than it
  was for attempted users.
- **Use wall clock for elapsed duration:** adjustments can produce invalid
  intervals.
- **Ignore generator lag:** the load driver may be the bottleneck.
- **Compare unmatched samples:** different operation mix, warm-up, or timeouts
  invalidate the conclusion.

## Guided practice

Sketch event timelines for a 10/s open-loop generator and a single closed-loop
participant during a one-second stall. Count scheduled arrivals and recorded
completions. State which denominator belongs in user-visible success rate.

## Self-check

1. Why does correct percentile arithmetic not fix coordinated omission?
2. What does a large generator-lag p99 mean?
3. Should a rejected request appear in latency evidence?
4. Why report maximum alongside p99?

## Explained answers

1. The missing observations were never collected; sorting the remaining values
   cannot reconstruct their experience without an explicit correction model.
2. The generator did not deliver the requested schedule, so system-capacity
   conclusions are confounded.
3. Yes, in the attempted-user population. Record rejection latency and outcome
   separately rather than mixing it with successful-service latency.
4. Maximum exposes extreme observations and timeout censoring, although it is
   not stable enough to replace percentiles.

## Sources and next work

- HdrHistogram maintainers, Corrected vs. raw recording (RES-05)
- Google Research, The Tail at Scale (RES-02)

Complete EX-04 and EX-05, then freeze the capacity prediction.
