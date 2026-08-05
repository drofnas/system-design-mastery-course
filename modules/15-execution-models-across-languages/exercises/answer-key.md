# Module 15 Explained Answers

These are reasoning boundaries, not graded commerce answers.

## EX-01–EX-02

The inventory must include external resources and tasks, not only objects.
Minimum bytes are `4 × 256 KiB × 2 + 128 KiB = 2,176 KiB`; at 40 concurrent
requests, 85 MiB. Missing classes include encoded bytes, object headers,
collections, stacks, allocator/runtime metadata, telemetry, and native buffers.

## EX-03–EX-04

Credit exact scheduler and queue placement with uncertainty where libraries may
vary. Dependency capacity caps child concurrency at 64, hence at most 16
four-child requests before headroom. Memory alone gives 32 requests, so the
dependency bound wins before reserving failover, runtime, or OS memory.

## EX-05–EX-09

Validation precedes large allocation and admission. At 120 ms, child work has
`500 - 120 - 50 = 330 ms` before assembly reserve. Admission before task creation
bounds captured work; admission inside a task does not. Cleanup evidence pairs
stable acquire/release identities and verifies no owned task/resource remains
after grace. Conformance requires semantic equality, not identical field order
or runtime-specific telemetry.

## EX-10–EX-11

Likely mismatches include validation, retries, copies, payload, concurrency,
success denominator, warm-up, resource limit, and optional-work policy. Hash
logical input and config; count offered/useful work, attempts, bytes, and bounds.
The observation supports workload/host-specific distribution differences. It
does not rank languages or equate RSS with live managed objects.

## EX-12–EX-13

A completion signal must order child writes before parent reads. Program order
alone does not cross threads. A detector exercises schedules; the oracle checks
one result per admitted child, complete snapshot, and correct aggregate. Rust's
compile rejection shows a static rule, not business correctness or Go coverage.

## EX-14–EX-15

Examples include a string concurrency limit, oversized child array, invalid
enum, or client-selected tenant. Assertions do no runtime validation. A safe
contract returns a bounded machine-readable 400 without tasks. An optional
field needs a declared unknown-field policy, semantic default, authorization,
mixed-version tests, and rollback; syntax-level optionality is insufficient.

## EX-16–EX-18

Findings must cite exact evidence and class. Paired repair retains seed, logical
input, limits, and all controls except one; raw evidence remains immutable. A
runtime defense passes when choice follows drivers and contains operations,
security, economics, migration, ownership, dissent, stops, and reversal. Any of
keep-current, bounded adoption, or broad adoption may be defensible.

## PESD 2.0 extension answer

A defensible answer covers four transport/schema shells while the learner implements admission, task ownership, cancellation, cleanup, memory and lifetime behavior, synchronization, and validation in TypeScript, Go, Rust, and Java. It distinguishes the
requirement, enforcement mechanism, evidence, and owner; keeps modeled and
measured results separate; and names the failed condition that would reverse
the decision. Different architectures are acceptable when their invariants,
evidence boundaries, migration, and residual risk are explicit.
