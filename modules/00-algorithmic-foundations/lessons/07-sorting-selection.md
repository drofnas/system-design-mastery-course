---
lesson_id: L07
title: "Sorting and Selection"
---

# Sorting and Selection

## Outcomes

- Explain comparison sorting and its lower bound.
- Distinguish sorting from selecting the top or median item.
- Recognize when data size forces external sorting.

## Prerequisites

Algebra, comfort reading loops and arrays in any language, and the ability to separate a model from a measurement.

## Mechanism

Comparison sorting needs O(n log n) comparisons in the general case. Real
systems use hybrids because existing order, small partitions, and memory layout
matter. Selection asks for a rank, such as top-k or median, and can often avoid a
full sort.

When data exceeds memory, the sort becomes an I/O plan: build runs, spill, merge,
and recover after interruption.

### Lower bounds, hybrids, and external work

General comparison sorting has an Omega(n log n) lower bound because a comparison sort must distinguish among `n!` possible input orders. The decision tree needs enough leaves for those permutations, so its height is at least `log2(n!)`, which grows as n log n. Counting sort and radix sort avoid this lower bound by using key structure rather than arbitrary comparisons.

Production sorts are hybrids. Timsort exploits existing runs and stability; introsort starts like quicksort and falls back to heapsort when recursion becomes risky. Stability matters when you sort by secondary keys or preserve prior ordering for equal keys.

External merge sort appears when data exceeds memory. With memory for `M` records, create sorted runs of size `M`, spill them, then merge runs in passes. Block size `B` matters because the cost is dominated by sequential reads and writes, not comparisons. This is the bridge to M07: the algorithm is also an I/O and recovery plan. Selection is separate: quickselect or a heap can find top-k or the nth item without imposing total order.

## Worked Example

A leaderboard that returns top 100 items should not sort every user on every
request. A heap, partial selection, or maintained ordered index can reduce work.

## Common Expert Mistakes

- Sorting when top-k is enough.
- Ignoring memory and temporary disk space.
- Comparing algorithms without checking input distribution.

## Guided Practice

You need the top 100 items from 10 million scores. Compare full sort with maintaining a min-heap of size 100. Then describe the external merge-sort plan if the full data set cannot fit in memory.

## Self-Check

1. Why does the comparison lower bound not apply to radix sort?
2. What does sort stability preserve?
3. Why is top-k different from full sorting?
4. What dominates external sort cost?

## Explained answers

1. Radix sort uses digit/key structure instead of arbitrary pairwise comparison decisions.
2. It preserves input order among equal keys, enabling multi-key sorting by repeated stable passes.
3. Top-k only needs the boundary set, not complete order among every item.
4. Sequential I/O passes, temporary space, and recovery after spill or merge interruption. For the practice, heap work is O(n log 100), far less than O(n log n) for full sort when only top 100 are needed.

## Sources And Next Work

Study RES-02 and RES-05. Then complete EX-07.
