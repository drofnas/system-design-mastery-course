lesson_id: L03

# Bounded Fan-out and Structured Cleanup

## Outcomes

Derive admission, deadline, cancellation, and cleanup contracts for child work,
then implement them without changing request semantics across runtimes.

## Prerequisites

Modules 2 and 6, plus Lessons 1–2.

## Mechanism and method

A fan-out request consumes at least one admission slot, child task, response
buffer, dependency attempt, and result record per child. Parallel latency is
bounded by the slowest required child; resource cost includes every child.

Use **SCOPE**: set one caller-owned absolute deadline; classify required and
optional children; own every task and resource in the request scope; propagate
cancellation and remaining time; exit only after results are assembled and all
owned work has completed or reached a bounded cleanup result.

Admission must precede expensive allocation and child creation. Limit both
requests and total children when fan-out varies. Reject or degrade explicitly;
do not hide overload in an unbounded executor queue. Child deadlines never
extend the parent. Cancellation is a request to stop, not proof that work
stopped, so record acknowledgement and post-grace orphan counts.

## Worked example

Northstar requires ephemeris and calibration; weather and quality are optional.
The journey deadline is 500 ms with 50 ms reserved for assembly. At 120 ms after
ingress, no child may receive more than 330 ms. The service admits at most eight
children globally. If weather has not completed by the optional cutoff, the
scope cancels it, records `optional_timeout`, closes its response, joins owned
work, and returns the required evidence with explicit incompleteness.

The broken F07 variant gives each child a fresh 500 ms timeout. A late child can
run after the client has left and hold a connection. The repaired pair changes
only `propagate_cancellation`, keeps the request hash constant, and verifies
I03 and I04 after cleanup grace.

## Common expert mistakes

- Using a semaphore after spawning tasks, which bounds execution but not queued
  task objects or captured payloads.
- Returning after the first error while siblings continue unowned.
- Treating a timeout exception as proof that the dependency stopped work.
- Giving optional work the same completion requirement as required work.

## Guided practice

For six children, two required and four optional, derive an absolute deadline,
assembly reserve, child caps, global child bound, overload result, cancellation
tree, and cleanup grace. State what response is valid when one optional child
times out and when one required child fails validation.

## Self-check

1. Why is cancellation propagation a correctness concern rather than polish?
2. Where should admission occur relative to decoding and task creation?
3. What evidence shows cleanup completed?

## Explained answers

1. Orphan work consumes resources, may perform effects after authority expires,
   and can leak request or tenant context.
2. Validate a small bounded envelope, then admit before large allocation or
   child creation. Otherwise rejected work can still exhaust the service.
3. Stable task/resource identities, cancellation acknowledgement, zero owned
   active tasks and open resources after grace, plus matched acquisition/release.

## Sources and next work

Revisit Module 6 deadline derivation and continue to [Lesson 4](04-memory-visibility-races.md).
