---
lesson_id: L05
title: "CPU, Allocation, and Lock Profiles"
---

# CPU, Allocation, and Lock Profiles

## Outcomes

- Choose a profiler that matches the resource question.
- Interpret CPU and allocation attribution without confusing samples and time.
- Separate CPU work, transient allocation, retention, and lock waiting.

## Prerequisites

Module 3 CPU, memory, and contention mechanisms; Lessons 1–4.

## Mechanism and method

A CPU profile attributes execution to call stacks. Deterministic profiling
records calls and elapsed time but adds instrumentation overhead; sampling
profiles approximate where execution spends time with different bias. An
allocation profile attributes created or retained memory to sites. Neither RSS
nor total allocated bytes alone proves a leak.

For each profile:

1. State resource, collection mode, interval, process, and overhead.
2. Preserve equivalent work and an unprofiled comparison.
3. Report inclusive and exclusive attribution where available.
4. Correlate profile time with the affected trace interval.
5. Use allocation snapshot differences to distinguish churn from retention.
6. Measure lock wait separately from code executing while holding a lock.

## Worked example

Transit records `cProfile` data during a bounded trial and `tracemalloc`
snapshots before and after processing. A CPU fault concentrates cumulative time
in normalization. An allocation fault raises allocated bytes; a retained-object
fault also leaves the final snapshot elevated. Lock contention appears in a
separate wait counter and span event, not as proof from CPU time alone.

## Common expert mistakes

- **Optimize the top line blindly:** inclusive time can belong to callees.
- **Call allocation rate a leak:** short-lived objects can create high churn with
  no retained growth.
- **Profile only the failing candidate:** collection overhead lacks a baseline.
- **Infer lock contention from low CPU:** dependency waiting can look similar.

## Guided practice

Complete EX-09 and EX-10. For one profile, state three conclusions it supports
and three it cannot support.

## Self-check

1. Why record both profiled and unprofiled trials?
2. What distinguishes allocation churn from retention?
3. Why is a lock-wait counter needed beside a CPU profile?

## Explained answers

1. To bound collection overhead and avoid attributing profiler effects to the
   candidate.
2. Snapshot differences, retained object evidence, and post-cleanup state;
   allocation volume alone measures churn.
3. A CPU profile attributes executing code, while waiting tasks may consume
   little CPU and disappear from the hot stacks.

## Failure-mode bridge to the lab

Profiles answer a different question from traces. A trace says where time sat in
one request path. A CPU or allocation profile says which code consumed a sample
of resource over an interval. The lab uses both because a wide span can be
caused by CPU, allocation pressure, lock wait, dependency wait, or measurement
distortion.

The common trap is treating a profile hotspot as a root cause without checking
equivalent work. A function can dominate samples because it is doing necessary
work, because it is accidentally repeated, or because the rest of the system is
blocked. Allocation profiles need the same care: retained objects matter more
than short-lived objects unless allocation churn itself creates latency. A good
lab diagnosis names the profile mode, sample window, top frame, and the
discriminating change that would reduce the hotspot while preserving response
checksum.

## Second worked example

Imagine a profile where JSON encoding dominates CPU after a schema change. The
wrong conclusion is "replace the JSON library" before checking payload shape.
First compare object count, field count, byte size, and checksum. If the new
schema emits twice as many fields, the profile is reporting changed work. If the
payload is equivalent and the encoder frame still grows, test allocation rate,
string conversion, and repeated serialization. A profile points to where samples
land; the investigation must still prove whether those samples are waste.

## Decision checklist

Record profile type, duration, workload, top frame, equivalent-work check, and
the falsifier. Then decide whether the next experiment changes code, input,
allocation, or instrumentation.

## Sources and next work

- Python Software Foundation, [The Python Profilers](https://docs.python.org/3/library/profile.html).
- Python Software Foundation, [`tracemalloc`](https://docs.python.org/3/library/tracemalloc.html).
- OpenTelemetry, [Profiles](https://opentelemetry.io/docs/specs/otel/profiles/).
- Next: inspect dependency boundaries in Lesson 6.
