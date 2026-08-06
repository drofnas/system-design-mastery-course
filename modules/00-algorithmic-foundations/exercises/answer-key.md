# Module 00 Exercise Answer Key

## EX-01

Doubling `n` roughly doubles linear work, a little more than doubles `n log n`,
and quadruples quadratic work. Small inputs can still favor the slower growth
class because constants, allocation, cache locality, and branch behavior matter.

## EX-02

Most appends write one cell. A resize copies existing elements, but each copied
element can be charged to previous appends, so the sequence is amortized O(1).
For capacities 1, 2, 4, 8, and 16, total copied elements are 31 before reaching
capacity 32, which is less than twice the number of appended elements. The risk
is a visible latency spike on the resize operation, plus temporary memory
headroom during the copy.

## EX-03

A hash table fits the dominant lookup workload if ordering is not central and
the hash function is trustworthy. A balanced tree gives ordered traversal and
predictable O(log n) operations, but likely costs more per lookup. The 1 percent
ordered scan is the deciding detail: if it is rare and can use a secondary index
or batch path, the hash table can own the hot path. If the scan is user-facing or
latency-sensitive, the tree's order is part of the primary requirement.

## EX-04

The contiguous structure is usually faster because hardware prefetch and cache
lines make adjacent access cheap. Both remain O(n); locality changes constants.
The M00 lab does not prove raw cache behavior because CPython lists store
references to boxed objects and the measurements run through interpreter loops.

## EX-05

An adjacency list is appropriate for sparse graphs because memory grows near
nodes plus edges: about 30 million neighbor entries at average degree 3. A matrix
has `10^7 * 10^7 = 10^14` cells, which is already about 12.5 TB at one bit per
cell before overhead. Use the list unless constant-time edge existence checks are
worth that memory.

## EX-06

The queue must return the highest eligible priority item without starving work
that the policy promises to admit. Valid fairness rules include aging, per-class
quotas, maximum wait, or explicit rejection when lower-priority work is outside
the service contract.

## EX-07

The design becomes an external sort: read, spill sorted runs, merge, and account
for I/O volume, temporary space, and failure recovery. Comparisons are no longer
the only cost; sequential block reads and writes dominate, and the system needs a
restartable plan for partially written runs.

## EX-08

The exact search space is `8^40`; with `log10(8) ~= 0.903`, that is about
`10^36.12`, or roughly `1.3e36` assignments. Use heuristics, approximation,
constraint relaxation, decomposition, or an optimizer with bounded runtime while
keeping hard constraints outside the scoring function.

## EX-09

Collisions can degrade expected O(1) lookup toward linear work per bucket.
Mitigate with keyed hashing, collision caps, tree buckets, quotas, or rejection.

## EX-10

A hash table keyed by idempotency key is natural for insert-if-absent and lookup,
plus a min-heap or bucketed expiry index for cleanup. Evidence should include
bounded memory and duplicate rejection under retries. The choice becomes unsafe
if keys are adversarial without hash-flood controls, if expiry is not enforced,
or if the idempotency scope omits tenant or operation identity.

## EX-11

Hash lookup should beat linear scan as `n` grows and lookup is selective. Array
traversal should beat linked traversal for the same logical O(n) walk because it
uses locality. `median_scan_ns` and `lookup_time_ratio` should grow with `n`;
`median_hash_ns` should grow much more slowly for the fixed lookup count.

## EX-12

The lab does not prove production latency, universal hardware behavior, or a
complete language/runtime comparison. It is bounded local evidence. A strong
answer cites the model limits: Python-level loops, CPython list-of-references
layout, non-adversarial integer keys, and median-of-repetitions on a shared
machine.
