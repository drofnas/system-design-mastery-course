---
lesson_id: L07
title: "Sorting and Selection"
---

# Sorting and Selection

## Outcomes

- Explain comparison sorting and its lower bound.
- Distinguish sorting from selecting the top or median item.
- Recognize when data size forces external sorting.

## Mechanism

Comparison sorting needs O(n log n) comparisons in the general case. Real
systems use hybrids because existing order, small partitions, and memory layout
matter. Selection asks for a rank, such as top-k or median, and can often avoid a
full sort.

When data exceeds memory, the sort becomes an I/O plan: build runs, spill, merge,
and recover after interruption.

## Worked Example

A leaderboard that returns top 100 items should not sort every user on every
request. A heap, partial selection, or maintained ordered index can reduce work.

## Common Expert Mistakes

- Sorting when top-k is enough.
- Ignoring memory and temporary disk space.
- Comparing algorithms without checking input distribution.

## Guided Practice

Find one API that sorts results. Decide whether it needs complete order, top-k,
or pagination over a stable index.

## Self-Check

What changes when data exceeds memory? I/O volume, temporary storage, merge
passes, and recovery become part of the algorithm.

## Sources And Next Work

Study RES-02. Then complete EX-07.
