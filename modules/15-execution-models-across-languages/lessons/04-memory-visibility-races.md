lesson_id: L04

# Memory Visibility and Races

## Outcomes

Build a happens-before graph, distinguish race freedom from business
correctness, and use detectors without overstating their coverage.

## Prerequisites

Module 8 concurrency histories and RES-02/RES-08.

## Mechanism and method

Two operations being “close in time” says nothing about visibility. Language
memory models define which synchronization actions order writes before reads.
Without the required edge, a compiler, runtime, or CPU may expose outcomes that
sequential source reading did not predict.

Use **EDGE**: enumerate shared locations; draw conflicting reads and writes;
derive program-order and synchronization edges; decide whether every conflict
is ordered; execute a detector or compile-time check; separate the tool result
from the invariant result.

Locks, channels, task joins, atomics, and volatile operations create different
edges under each language contract. A mutex can remove a data race while still
allowing a lost business update if the read-decide-write transaction spans
separate critical sections. Rust prevents many unsafe aliases in safe code, but
atomics can still implement the wrong protocol and external systems remain
outside the borrow checker.

## Worked example

Northstar increments `completed_children` and appends child results. The broken
Go variant updates a shared map from child goroutines without synchronization.
`go test -race` identifies conflicting accesses, but the real requirement is
one result per admitted child and a complete response snapshot. The repair sends
immutable child results to one owner goroutine, then joins it before assembly.
The race detector is clean and I06 passes.

A Rust compile-fail fixture tries to share `Rc<RefCell<_>>` across threads. Its
rejection demonstrates a static boundary, not the correctness of the repaired
Go protocol or of an `Arc<AtomicUsize>` algorithm.

## Common expert mistakes

- Calling a race detector a proof; it observes executed schedules and supported code.
- Using `volatile` as a general substitute for compound synchronization.
- Fixing a race by broad locking without measuring contention or cancellation.
- Treating race freedom as invariant preservation.

## Guided practice

Draw edges for a child write followed by channel send, parent receive, and
response serialization. Replace the channel with an unsynchronized boolean.
Identify the missing edge, one allowed bad observation, a tool, and an invariant
oracle independent of that tool.

## Self-check

1. Can repeated correct output prove a program race-free?
2. Can an atomic counter prove the associated result list is complete?
3. What must accompany a clean detector run?

## Explained answers

1. No. The executed schedules may not expose the conflict and observations do
   not create a language-defined ordering.
2. No. The counter and list need one coherent protocol and completion boundary.
3. Workload and schedule coverage, tool/runtime identity, invariant checks,
   unsupported-code limits, and a separate static or causal argument.

## Sources and next work

Use RES-02, RES-08, RES-09, and RES-10. Continue to [Lesson 5](05-types-serialization-validation.md).
