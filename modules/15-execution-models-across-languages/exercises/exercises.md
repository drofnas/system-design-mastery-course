# Module 15 Guided Exercises

Complete these with Northstar data. Freeze independent commerce choices first.

## EX-01: Lifetime inventory

Trace one request's descriptors, buffers, responses, aggregate, tasks, and files.
For each record placement, owner, aliases, release trigger, and leak evidence.

## EX-02: Allocation calculation

Four children return 256 KiB each. Decode makes one equal-size copy and assembly
makes a 128 KiB summary. Calculate minimum request-attributable bytes before
runtime overhead. Recalculate for 40 concurrent requests and name omissions.

## EX-03: Scheduler placement

Map accept, JSON decode, DNS, socket wait, 20 ms hash, logging, and assembly to
event loop/runtime task/worker/OS thread for each runtime. Name every queue.

## EX-04: Bound derivation

Given 8 CPU cores, dependency capacity 64, fan-out 4, and 16 MiB per active
request, propose request/child bounds under a 512 MiB service budget.

## EX-05: Request contract

Validate IDs, deadline, limit, children, required flags, payload, fault mode,
unknown fields, and cross-field rules before admission.

## EX-06: Deadline tree

For a 500 ms journey, 70 ms ingress, and 50 ms assembly reserve, calculate
remaining child time at 120 ms and define optional/required outcomes.

## EX-07: Admission placement

Compare acquiring a permit before task creation with acquiring inside each task.
Predict queued objects and captured bytes for 10,000 offered children.

## EX-08: Cleanup contract

Write pseudocode that owns tasks, responses, permits, and temporary files under
success, parse failure, timeout, cancellation, and exception.

## EX-09: Cross-runtime conformance

Run one baseline in all four services. Verify response shape, status, child
ordering policy, required completeness, deadline, bounds, and cleanup.

## EX-10: Equivalent-work audit

Find five reasons two superficially identical runtime trials may not do the same
work. Specify hashes and counters that detect each difference.

## EX-11: Measurement interpretation

One runtime has lower median latency but two GCs and higher p95. Another has no
GC but higher RSS. List supported claims, unsupported claims, and next tests.

## EX-12: Happens-before graph

Draw child writes, completion signal, parent read, and response serialization.
Identify the edges supplied by a channel, mutex, join, or volatile/atomic use.

## EX-13: Detector boundary

Design a Go race test and a separate invariant oracle. Explain what a clean run
would not prove. Add a Rust compile-fail contrast without claiming equivalence.

## EX-14: Type boundary

Construct JSON that a TypeScript assertion accepts but the wire contract rejects.
Specify the same safe error in all runtimes.

## EX-15: Compatibility change

Add an optional `priority` field. Define old/new producer and consumer behavior,
unknown-field policy, default, authorization, and rollback evidence.

## EX-16: Failure classification

For F01–F09 classify missing evidence, incorrect reasoning, unsupported claim,
invariant failure, internal contradiction, or communication gap.

## EX-17: Paired repair

Choose F07. Freeze prediction, run broken evidence, change only cancellation
propagation, rerun identical work, and rank one alternative explanation.

## EX-18: Runtime defense

Compare keep-current, bounded adoption, and broad adoption. Defend workload,
safety, operations, security, cost, migration, ownership, dissent, and reversal.

## PESD 2.0 extension to the final exercise

Extend the final guided exercise with four transport/schema shells while the learner implements admission, task ownership, cancellation, cleanup, memory and lifetime behavior, synchronization, and validation in TypeScript, Go, Rust, and Java. Produce an
obligation/control/evidence row, a named owner, a bounded cost or capacity
effect, a failure or policy-drift test, a migration step, and a reversal trigger.
Label every observation with an accepted evidence mode and do not use fixture
replay as independent Build, Break, Implement, or Measure evidence.
