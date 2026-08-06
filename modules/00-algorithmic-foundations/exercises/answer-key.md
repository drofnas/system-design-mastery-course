# Module 00 Exercise Answer Key

## EX-01

Doubling `n` roughly doubles linear work, a little more than doubles `n log n`,
and quadruples quadratic work. Small inputs can still favor the slower growth
class because constants, allocation, cache locality, and branch behavior matter.

## EX-02

Most appends write one cell. A resize copies existing elements, but each copied
element can be charged to previous appends, so the sequence is amortized O(1).
The risk is a visible latency spike on the resize operation.

## EX-03

A hash table fits the dominant lookup workload if ordering is not central and
the hash function is trustworthy. A balanced tree gives ordered traversal and
predictable O(log n) operations, but likely costs more per lookup.

## EX-04

The contiguous structure is usually faster because hardware prefetch and cache
lines make adjacent access cheap. Both remain O(n); locality changes constants.

## EX-05

An adjacency list is appropriate for sparse graphs because memory grows near
nodes plus edges. A matrix grows with nodes squared and is usually wasteful here.

## EX-06

The queue must return the highest eligible priority item without starving work
that the policy promises to admit.

## EX-07

The design becomes an external sort: read, spill sorted runs, merge, and account
for I/O volume, temporary space, and failure recovery.

## EX-08

The exact search space grows exponentially. Use heuristics, approximation,
constraint relaxation, decomposition, or an optimizer with bounded runtime.

## EX-09

Collisions can degrade expected O(1) lookup toward linear work per bucket.
Mitigate with keyed hashing, collision caps, tree buckets, quotas, or rejection.

## EX-10

A hash table keyed by idempotency key is natural for insert-if-absent and lookup,
plus a min-heap or bucketed expiry index for cleanup. Evidence should include
bounded memory and duplicate rejection under retries.

## EX-11

Hash lookup should beat linear scan as `n` grows and lookup is selective. Array
traversal should beat linked traversal for the same logical O(n) walk because it
uses locality.

## EX-12

The lab does not prove production latency, universal hardware behavior, or a
complete language/runtime comparison. It is bounded local evidence.
