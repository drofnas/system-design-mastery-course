---
lesson_id: L04
title: "Locks, Contention, Deadlock, and False Sharing"
---

# Locks, Contention, Deadlock, and False Sharing

## Outcomes

- Separate correctness synchronization from performance contention.
- Demonstrate a deadlock inside a watchdog-enforced boundary.
- Explain false sharing without assuming padding must improve every run.

## Prerequisites

Lessons 1–3 and familiarity with mutexes and atomic operations.

## Mechanism and decision method

A lock protects an invariant by serializing a critical section. Contention adds
waiting when multiple actors need the lock. Replacing a lock is valid only if the
new mechanism preserves ordering, visibility, lifetime, and failure semantics.

Deadlock requires a wait cycle. Apply this procedure:

1. List resources and owners.
2. Draw directed “holds” and “waits for” edges.
3. Identify a cycle and the condition that makes it reachable.
4. Break hold-and-wait, impose a global order, or add an external recovery action.
5. Test the failure in a child process with a strict timeout; never let the test
   runner become part of the deadlock.

False sharing is different. Independent variables on one coherence unit can
cause ownership traffic when different CPUs write them. Compare adjacent and
padded layouts with identical updates and checksums. Padding is a hypothesis:
allocator placement, thread placement, compiler layout, true sharing, and
measurement noise can dominate.

## Worked example

Transit begins with one mutex protecting all 64 route counters. Sharding by route
reduces the critical-section domain but adds merge work. The learner sweeps worker
count and route skew, recording throughput, context switches, and checksum.

A second probe assigns one counter per worker. Adjacent counters may share lines;
padded counters request separation. The result is accepted only across repeated
runs and is scoped to the recorded architecture. A deadlock fixture reverses two
lock acquisitions inside a child; the parent watchdog records `timeout` and
terminates it. That outcome is evidence of bounded detection, not recovery.

## Common expert mistakes

- **Optimizing away a correctness boundary:** throughput does not repair races.
- **Calling any slow lock a deadlock:** contention still makes progress.
- **Running a deadlock in the test process:** the suite can hang indefinitely.
- **Assuming cache-line size:** record or conservatively align; do not universalize.
- **Asserting padded must be faster:** tests should assert equal work and safe
  completion, not a machine-specific ratio.

## Guided practice

Draw a two-lock cycle for checkpoint metadata and route state. Propose a total
lock order and a watchdog experiment. Then name an invariant that sharded counters
must preserve during merge.

## Self-check

1. How does contention differ from deadlock?
2. Can atomics experience contention?
3. Why is a timeout not a production deadlock policy?
4. What evidence weakens a false-sharing explanation?

## Explained answers

1. Contended actors eventually progress; a deadlocked wait cycle cannot progress
   without outside change.
2. Yes. Coherence ownership and serialization can remain even without a mutex.
3. Killing a test bounds the demonstration; production needs invariant-aware
   cancellation, restart, or prevention semantics.
4. No repeated separation between layouts, no placement control, or a stronger
   bottleneck such as quota throttling or true shared-state serialization.

## Sources and next work

- Meta, *Serving Facebook Multifeed*: RES-05
- Continue with EX-06 through EX-08.
