# Module 00 Exercises

## EX-01 Growth Classes

For operations with cost `n`, `n log n`, and `n^2`, describe what happens when
input size doubles. State one reason the fastest asymptotic class might still
lose on small inputs.

## EX-02 Amortized Resize

A dynamic array doubles capacity when full. Explain why append is amortized
O(1), then name the latency risk a single resize creates.

## EX-03 Operation Mix

A workload performs 90 percent key lookup, 9 percent insert, and 1 percent full
ordered scan. Compare hash table and balanced tree choices.

## EX-04 Locality

Two structures both require O(n) traversal. One stores values contiguously and
one follows pointers. Predict which is likely faster locally and why.

## EX-05 Graph Representation

A graph has 10 million nodes and average degree 3. Compare adjacency lists and
an adjacency matrix for memory and traversal.

## EX-06 Priority Semantics

Name the invariant a priority queue must preserve in an admission-control system.

## EX-07 Sorting Boundary

When data exceeds memory, what changes about a sort plan?

## EX-08 Tractability Signal

A placement problem needs to try every assignment of 40 shards across 8 regions.
Explain why exact search is suspect and name one practical fallback.

## EX-09 Hash Abuse

What happens if untrusted input causes many keys to collide? Name a mitigation.

## EX-10 Design Decision

Choose a data structure for idempotency keys with expiry. State operations,
complexity, and cleanup evidence.

## EX-11 Lab Prediction

Before running the lab, predict when a hash lookup should beat a linear scan and
when an array traversal should beat linked traversal.

## EX-12 Lab Limitation

After running the lab, name one conclusion the local result does not support.
