lesson_id: L02

# Baselines, Hypotheses, and Controlled Experiments

## Outcomes

- Preserve equivalent work and identify multiple variation levels.
- Design interleaved comparisons with visible uncertainty.
- Distinguish statistical confidence from production transfer.

## Prerequisites

Lesson 1 and the Module 3 benchmark contract.

## Mechanism and method

A performance result varies within a process, between process starts, across
candidate order, and across environments. One long run samples only some of
those dimensions. A controlled experiment fixes or records every material
dimension and changes one intended factor.

Before collection, record:

- input, output checksum, request schedule, outcome mix, and useful work;
- machine, runtime, process start, warmup, and background-load boundary;
- baseline/candidate order and repetitions;
- profiler and telemetry modes;
- comparison statistic, smallest meaningful effect, and uncertainty rule.

Interleave candidate order so time-correlated host changes do not all favor one
variant. Preserve raw samples. A summary must not hide an outlier or select the
best run after seeing the result.

## Worked example

Transit Signal alternates baseline and candidate process starts while preserving
the same seeded arrivals and response checksum. It reports every p95 and process
CPU sample, the median ratio, range, and environment metadata. A result that
changes sign across process starts becomes a new noise investigation, not an
optimization claim.

## Common expert mistakes

- **Benchmark different work:** removing a branch or validation makes timing
  incomparable.
- **Warm only one candidate:** cache and compilation state become confounders.
- **Report one percentile from one trial:** sampling error and host noise remain
  invisible.
- **Treat significance as importance:** a tiny repeatable effect may not change a
  user objective or operating cost.

## Guided practice

Complete EX-03 and EX-04. Draw a table with controlled, randomized, measured,
and excluded dimensions.

## Self-check

1. Why interleave rather than run all baselines first?
2. What does an equivalent-work check protect?
3. Can a repeatable local result justify production rollout by itself?

## Explained answers

1. It reduces bias from time-correlated machine or environment changes.
2. It prevents a speedup obtained by changing the required result or doing less
   user work.
3. No. Transfer also requires comparable workload, resource boundaries, failure
   exposure, and operating evidence.

## Sources and next work

- Tomas Kalibera and Richard E. Jones,
  [Rigorous Benchmarking in Reasonable Time](https://kar.kent.ac.uk/33611/).
- Python Software Foundation, [timeit](https://docs.python.org/3/library/timeit.html).
- Next: propagate a causal request identity in Lesson 3.
