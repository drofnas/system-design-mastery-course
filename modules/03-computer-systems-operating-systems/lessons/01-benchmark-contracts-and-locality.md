---
lesson_id: L01
title: "Benchmark Contracts, Pipelines, Caches, and Locality"
---

# Benchmark Contracts, Pipelines, Caches, and Locality

## Outcomes

- Freeze equivalent work and a falsifiable prediction before measuring.
- Explain how instruction flow, branches, cache lines, and locality affect work.
- Reject benchmark conclusions that exceed their environment or evidence.

## Prerequisites

Module 2 measurement boundaries, percentiles, repetitions, and useful work.

## Mechanism and decision method

A processor overlaps instruction fetch, decode, execution, and retirement. It
speculates about branches and serves memory through a hierarchy. The useful
question is not “how many nanoseconds is RAM?” It is which dependency prevents
this workload from making progress on this machine.

Use this benchmark contract:

1. **Claim:** name the production decision the result may inform.
2. **Equivalent work:** fix inputs, outputs, checksum, and correctness checks.
3. **Mechanism:** predict the constrained resource and direction of change.
4. **Environment:** record CPU/architecture, OS/kernel, compiler, flags, power
   context, runtime, filesystem, limits, and competing work.
5. **Method:** define warm-up, repetitions, order randomization, clocks, and
   counters before observing results.
6. **Falsifier:** state an observation that would reject the mechanism.
7. **Transfer boundary:** name the production differences that require a new test.

For a row-major array with `R` rows, `C` columns, and element size `s`, adjacent
row traversal has address delta `s`; column traversal has delta `C × s`. The
latter may consume a new cache line or page for every access. This calculation
does not predict an exact speedup because cache geometry, prefetching, vector
generation, and compiler transformations differ.

Branches create a similar dependency. Predictable branches let speculative work
remain useful. An unpredictable branch may discard work, but a branchless rewrite
can do more instructions. Measure equal outputs before preferring either.

Copying is a workload transformation, not free locality. Let `C` be the measured
cost to copy a structure once and let `Δ = D - P` be the saving per reuse between
direct access cost `D` and packed-copy access cost `P`. Copying can break even
only when `k × Δ > C`, or `k > C / Δ`, and only while ownership, lifetime, update
visibility, and memory headroom remain acceptable. Include allocation and copy in
the timed boundary when the production request pays them.

## Worked example

Transit replays 2,000,000 updates. A contiguous route table and a 4 KiB-strided
table produce the same checksum. The prediction says contiguous access will have
lower median elapsed time after warm-up because it touches fewer lines and pages.

The method uses one warm-up and seven measured repetitions, alternates variant
order, records every sample, and reports the median plus range. If a compiler
report shows one loop vectorized and the other not, vectorization becomes part of
the causal model instead of being hidden as “cache.” If checksums differ, the run
is invalid.

A second Transit pair scans route state directly or copies it into a packed
buffer and then scans it. Both report the same logical bytes and checksum; the
copying variant times allocation, `memcpy`, and the scan. One scan therefore
tests copy overhead. A separate repeated-reuse experiment is needed to establish
a break-even count.

## Common expert mistakes

- **Timing unequal work:** a faster wrong checksum is not an optimization.
- **Using one iteration:** startup, interrupts, and frequency state dominate.
- **Naming a cache as cause without evidence:** layout, vectorization, or copying
  may have changed simultaneously.
- **Reporting only the best run:** it selects favorable noise and hides variance.
- **Generalizing across machines:** cache and branch behavior are not API contracts.

## Guided practice

For 64-byte records and a 64-byte line, compare a scan of every record with a
scan of every 64th record. Write the address delta, prediction, equivalent-work
check, and a falsifier. Then identify why “the strided loop is 64 times slower”
is not a valid prediction.

Next, suppose a packed copy costs 1.8 ms and saves 0.3 ms per later scan. Derive
the first reuse count that can pay back the copy, then name two conditions that
could still reject the change.

## Self-check

1. Why must a checksum be consumed outside the timed loop?
2. What does a lower elapsed time prove when no counter is available?
3. When is a warm cache the correct state rather than benchmark contamination?
4. Why can a branchless implementation lose?
5. When does a faster packed scan fail to justify copying?

## Explained answers

1. It prevents dead-code elimination and establishes equivalent output without
   adding output I/O to the timed region.
2. It proves only that the complete measured variant finished sooner under the
   recorded conditions. It does not isolate a cache or branch mechanism.
3. When production repeatedly reuses the same working set and the claim is about
   steady-state behavior. The contract must say so.
4. It may execute more instructions or create longer data dependencies than a
   well-predicted branch.
5. When copy/allocation cost is outside the measurement, reuse is too low to
   cross `C / Δ`, or ownership, freshness, and memory requirements make the extra
   representation unsafe. Measure the complete boundary the decision will pay.

## Sources and next work

- Intel, *Optimization Reference Manual*, current Volume 1 sections on front end
  and data access: https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html
- Continue with EX-01 and EX-02, then freeze the systems prediction.
