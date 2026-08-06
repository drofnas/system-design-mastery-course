---
lesson_id: L01
title: "Memory Lifetime and Management"
---

# Memory Lifetime and Management

## Outcomes

Explain stack and heap placement, compare manual release, RAII, ownership,
reference counting, and tracing collection, and predict workload-visible costs.

## Prerequisites

Module 3 memory hierarchy and Module 4 profiling. Read RES-03 within its boundary.

## Mechanism and method

Separate four questions that architecture discussions often collapse: where a
value is stored, who can reach it, who may mutate it, and what event releases
it. Stack versus heap is placement. Ownership is authority and lifetime. A
collector is a reclamation mechanism. None alone predicts locality or latency.

Use the **LORP** procedure: list allocations and acquired resources; identify
owners and aliases; record release triggers; predict observable pressure. For
each request, count bytes and objects, longest lifetime, cycles, copies, and
cleanup paths. Then test the prediction with allocation profiles, heap/RSS,
collector events, and open-resource counts.

Manual management makes release explicit but permits use-after-free, double
free, and leaks. RAII binds release to lexical destruction. Rust ownership and
borrowing constrain aliases and release values through `Drop`; unsafe code,
foreign calls, logical leaks, and external resources remain evidence problems.
Reference counting releases promptly at zero but cycles need weak references or
cycle detection. Tracing collectors trade programmer-visible release for root
scanning, marking, compaction, write barriers, and runtime policy. Escape
analysis may keep or move values without changing source-level semantics.

## Worked example

Northstar accepts one observation and creates four child descriptors. The
broken version retains every decoded weather payload in a process-wide history.
The response objects are unreachable from the request but reachable from the
history, so a tracing collector correctly keeps them. Raising heap size delays
the symptom; it does not repair ownership. The repair gives the request scope
ownership, records only bounded summaries, closes every response, and verifies
that post-grace live bytes and open resources return to the declared baseline.

For Rust, the analogous logical leak is an `Arc` held by a never-finished task.
Deterministic `Drop` cannot run while an owner remains. “No GC” is not “no leak.”

## Common expert mistakes

- Treating heap allocation as inherently slow while ignoring allocation rate,
  lifetime, locality, allocator contention, and equivalent work.
- Treating low RSS as proof of release; allocators may retain pages and RSS may
  include stacks, mappings, native buffers, and runtime metadata.
- Claiming RAII closes asynchronous child work automatically. The scope must own
  and join or cancel those tasks.
- Comparing GC pauses without heap size, allocation rate, flags, warm-up, and
  useful-work identity.

## Guided practice

For a request with four 256 KiB child responses, draw owners from socket buffer
to decoded value to aggregate. Mark one copy, one alias, release trigger, and
failure path in each runtime. Predict which metric changes when one response is
retained for ten minutes, then name a falsifying observation.

## Self-check

1. Does a compiler-proven borrow establish that a socket was closed on time?
2. Why can a tracing collector retain unreachable physical pages after objects die?
3. What evidence distinguishes a logical retention leak from collector delay?

## Explained answers

1. No. Borrow rules cover memory access; external-resource lifetime still needs
   an owned close path and observed cleanup.
2. The runtime or allocator may keep reclaimed regions for reuse; object
   reachability, heap commitment, and RSS are different measures.
3. Retainer paths or owner identities show continuing reachability; collector
   events plus falling live-set size suggest delayed reclamation instead.

## Sources and next work

Use RES-03 and local lab code. Continue to [Lesson 2](02-schedulers-event-loops-tasks.md)
because task ownership determines whether release points can occur.
