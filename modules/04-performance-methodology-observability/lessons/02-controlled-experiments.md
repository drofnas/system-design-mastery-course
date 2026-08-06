---
lesson_id: L02
title: "Baselines, Hypotheses, and Controlled Experiments"
---

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

## Failure-mode bridge to the lab

The lab's strongest experiments keep one claim under pressure. Baseline and
candidate runs should preserve input, useful-work definition, seed, dependency
shape, and output checksum unless the question explicitly changes one of those.
If the candidate improves latency by skipping work, the experiment is invalid
for a performance claim even if the chart looks better.

Watch for three subtle failures. First, changing two controls at once creates an
ambiguous win; you no longer know which control caused the movement. Second,
selecting the best candidate run and the worst baseline run turns noise into a
story. Third, stopping at "candidate faster" misses whether the result matters:
a 2 ms median improvement may not change a p95 objective, while a small mean
change can hide a damaging tail. In the lab, compare order, dispersion, and
equivalence before naming a winner.

## Second worked example

Suppose a cache change appears to reduce p95 from 220 ms to 170 ms. The
experiment is not controlled if the candidate run also uses a warmer cache,
fewer tenants, or a lower request rate. Preserve the request mix first. Then run
baseline and candidate in an interleaved order so machine drift is less likely
to masquerade as a win. Finally, verify the response checksum or semantic result.
Only then does the latency movement support the cache claim. If the cache serves
stale data, the performance improvement may be real and still unacceptable.

## Decision checklist

Before accepting the result, confirm baseline and candidate use the same input,
same useful-work definition, same environment notes, and an interleaved or
otherwise justified run order. Then state the smallest decision the result
supports.

## Sources and next work

- Tomas Kalibera and Richard E. Jones,
  [Rigorous Benchmarking in Reasonable Time](https://kar.kent.ac.uk/33611/).
- Python Software Foundation, [timeit](https://docs.python.org/3/library/timeit.html).
- Next: propagate a causal request identity in Lesson 3.
