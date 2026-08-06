# Module 00 Exercises

Use these exercises after the lessons, not as a separate algorithms quiz. Show
the calculation or decision boundary that supports each answer.
When a prompt asks for a choice, include the workload assumption that would make
you reverse it. Prefer small numeric estimates over adjectives like "large" or
"fast" whenever the prompt supplies enough data.

## EX-01 Growth Classes

For operations with cost `n`, `n log n`, and `n^2`, describe what happens when
input size doubles. State one reason the fastest asymptotic class might still
lose on small inputs.

## EX-02 Amortized Resize

A dynamic array doubles capacity when full. Explain why append is amortized
O(1), then name the latency risk a single resize creates. Use the copy series
for 1, 2, 4, 8, and 16 elements as evidence.

## EX-03 Operation Mix

A workload performs 90 percent key lookup, 9 percent insert, and 1 percent full
ordered scan over 2 million records. Compare hash table and balanced tree
choices. Include the operation that each structure serves poorly.

## EX-04 Locality

Two structures both require O(n) traversal. One stores values contiguously and
one follows pointers. Predict which is likely faster locally and why. State why
the M00 lab result is not proof of raw CPU cache behavior.

## EX-05 Graph Representation

A graph has 10 million nodes and average degree 3. Compare adjacency lists and
an adjacency matrix for memory and traversal. Compute edge entries and matrix
cells before deciding.

## EX-06 Priority Semantics

Name the invariant a priority queue must preserve in an admission-control system.
Then add one fairness rule that prevents starvation under sustained high-priority
load.

## EX-07 Sorting Boundary

When data exceeds memory, what changes about a sort plan? Include run creation,
merge passes, temporary space, and recovery after interruption.

## EX-08 Tractability Signal

A placement problem needs to try every assignment of 40 shards across 8 regions.
Explain why exact search is suspect and name one practical fallback. Use
`log10(8) ~= 0.903` to estimate the candidate count.

## EX-09 Hash Abuse

What happens if untrusted input causes many keys to collide? Name a mitigation.

## EX-10 Design Decision

Choose a data structure for idempotency keys with expiry. State operations,
complexity, cleanup evidence, and the condition that would make your choice
unsafe.

## EX-11 Lab Prediction

Before running the lab, predict when a hash lookup should beat a linear scan and
when an array traversal should beat linked traversal. State one metric you expect
to grow with `n` and one metric you expect to stay roughly flat.

## EX-12 Lab Limitation

After running the lab, name one conclusion the local result does not support.
Use one `model_limits` entry as evidence.
