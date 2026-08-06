---
lesson_id: L05
title: "Profiling and Inference Metrics"
---

# Profiling and Inference Metrics

## Outcomes

- Design a reproducible inference measurement protocol.
- Separate queue, tokenization, prefill, decode, streaming, and provider time.
- Diagnose bottlenecks without confusing modeled and measured evidence.

## Prerequisites

Use Module 4 measurement discipline and the capacity predictions from Lesson 4.

## Mechanism: one request needs several clocks

Record monotonic timestamps for arrival, admission, execution start, prefill end,
each token, terminal result, and resource release. Under this module, TTFT is
`first_token - arrival`; queue time is not hidden. ITL is the distribution of
differences between adjacent output-token timestamps. End-to-end latency ends at
the terminal event. Report accepted, rejected, failed, cancelled, and deadline
outcomes separately.

Useful output throughput counts output tokens only from results that satisfy the
declared completion and quality contract. Report input tokens per second, output
tokens per second, requests per second, and utilization separately because each
can improve while another user outcome worsens.

Protocol:

1. Pin code, model/tokenizer/policy versions, precision, host, device, runtime,
   seed, workload, and power/performance mode when known.
2. Warm up compilation, allocation, and caches explicitly; do not hide warm-up.
3. Use open-loop arrivals for overload claims and record generator lag.
4. Repeat trials, preserve raw token timestamps, and report variation.
5. Profile one bounded window and quantify profiler overhead with an interleaved run.
6. Change one cause, rerun the same work, and retain competing explanations.

The portable scenario runner produces deterministic modeled evidence. The server
test produces measured CPU observations. Optional PyTorch profiling produces a
third evidence class. Never merge these rows into one unlabeled percentile.

## Worked example

Atlas reports 400 output tokens/s after increasing batch size, but interactive
p95 TTFT rises from 610 ms to 1.4 s because long prefill waits in front of decode.
An operator-only trace shows matrix time but omits queue delay. Adding arrival,
admission, and token timestamps exposes scheduling as the dominant user-facing
cause. Chunked prefill repairs TTFT while retaining most throughput under the
same seed and workload.

## Common expert mistakes

- Benchmarking a closed loop and claiming overload capacity.
- Reporting a mean for a mixed interactive/batch population.
- Omitting rejected requests from useful-throughput and cost analysis.
- Profiling every request and treating profiler overhead as production behavior.
- Comparing a CPU model with a GPU server without restating the evidence limit.

## Guided practice

Complete EX-10. Run the CPU profile three times after a declared warm-up and
produce a timestamp ledger for one streamed request.

## Self-check

1. Why include queue time in TTFT?
2. Why can output tokens/s rise while users wait longer?
3. What makes a profiler trace insufficient for a causal claim?
4. Why preserve raw token timestamps?

## Explained answers

1. The user waits from arrival, and admission policy is part of the service.
2. Larger or unfair batches improve aggregate work while delaying the first
   useful output for one class.
3. A trace identifies where time was recorded; same-work intervention and
   alternative causes establish a stronger causal argument.
4. Aggregates cannot reconstruct ITL distribution, stalls, or incorrect terminal timing.

## Sources and next work

Study RES-07 and the measurement parts of RES-09. Complete EX-10 before using
Lesson 6 to change scheduler behavior.
