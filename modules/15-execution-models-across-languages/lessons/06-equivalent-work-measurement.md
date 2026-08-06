---
lesson_id: L06
title: "Equivalent-work Runtime Measurement"
---

# Equivalent-work Runtime Measurement

## Outcomes

Design a fair cross-runtime experiment, calculate useful throughput and latency,
and distinguish protocol facts from empirical host observations.

## Prerequisites

Modules 2–4 and Lessons 1–5.

## Mechanism and method

A benchmark compares systems only when inputs, required effects, success rules,
limits, and measurement boundaries match. Source code that “looks similar” may
perform different parsing, copies, retries, buffering, or validation.

Use **SAME**: specify semantic work and success; align limits and environment;
measure warm-up separately from steady repetitions; expose attempts, bytes,
queues, memory, GC, tasks, and cleanup. Hash canonical logical inputs and record
configuration, toolchain, container image, CPU/memory limits, host platform,
clock, warm-ups, repetitions, and rejected trials.

Useful throughput is valid completed requests divided by measured time. Offered
requests, attempts, and partial invalid responses are separate. Report a latency
distribution, not only an average. Do not force unlike counters into a false
common unit: event-loop delay, goroutine count, virtual-thread count, GC pause,
and deterministic `Drop` answer different questions.

## Worked example

Northstar runs three warm-ups and five measured repetitions of the same request
hash. Each request has four children and 1 MiB of total returned payload. One
variant silently omits runtime validation and counts malformed responses as
success; its apparent throughput is not equivalent. After restoring validation,
the report gives median and p95 per repetition, useful completions, maximum
in-flight children, peak resident memory, allocation/GC evidence, cancellation
cleanup, and confidence intervals or ranges. A Node win on this host remains a
host/workload result, not “Node is fastest.”

## Common expert mistakes

- Mixing cold compilation/startup with steady request service without labeling it.
- Fixing concurrency per request but allowing different global concurrency.
- Comparing RSS without heap, stack, native buffer, and allocator context.
- Removing outliers after seeing which runtime benefits.

## Guided practice

Audit two hypothetical trial records. Reject one for a different success
denominator and one for a different memory limit. Propose the smallest rerun
that restores comparability without deleting raw results.

## Self-check

1. Why hash logical input rather than raw JSON alone?
2. When may a failed request count toward throughput?
3. What does a clean protocol-conformance result say about performance?

## Explained answers

1. Field order or encoding may differ while meaning is identical; retain both
   wire and canonical semantic hashes when boundary behavior matters.
2. It counts as offered load or explicit rejection, never useful throughput
   unless the product contract defines that outcome as useful.
3. Only that the observed response met the public contract and invariants. It
   says nothing about suitability, capacity, or production tails.

## Sources and next work

Use RES-11, reuse Module 4 measurement rules, and continue to
[Lesson 7](07-northstar-polyglot-tutorial.md).
- RES-17 -- Rigorous Benchmarking in Reasonable Time, for the local mechanism boundary.
