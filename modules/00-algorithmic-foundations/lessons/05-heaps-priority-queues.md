---
lesson_id: L05
title: "Heaps and Priority Queues"
---

# Heaps and Priority Queues

## Outcomes

- Explain heap order and priority-queue operations.
- Connect priority queues to overload and scheduling decisions.
- State fairness risks.

## Prerequisites

Algebra, comfort reading loops and arrays in any language, and the ability to separate a model from a measurement.

## Mechanism

A binary heap stores a partial order that makes the minimum or maximum item cheap
to inspect. Insert and remove-priority are O(log n). Peek is O(1).

Priority queues are policy machines. They decide which work moves next. That can
protect critical work during overload, but it can also starve lower-priority
work unless the policy includes fairness or aging.

### Heap mechanics and scheduling risk

A binary heap is usually stored in an array. For zero-based indexing, children of `i` are `2i + 1` and `2i + 2`; the parent is `(i - 1) // 2`. Insert appends at the end and sifts up until heap order holds. Remove-priority swaps the root with the last item, removes it, and sifts down. Both touch at most the height, so they are O(log n).

`build_heap` is O(n), not O(n log n), because most nodes are near the leaves and move little. The total sift-down work is bounded by the weighted sum of node heights, which is linear. That counterintuitive result matters when initializing a scheduler from an existing backlog.

In system design, the comparison function is policy. A priority queue can protect evacuation alerts from analytics exports, but sustained high-priority load can starve ordinary work. Aging, per-class quotas, maximum wait, and rejection policies turn priority from a slogan into an enforceable fairness contract.

## Worked example

M02 discusses admission control. If requests have priority classes, a priority
queue can admit evacuation alerts before analytics exports. The design must
still bound queue length and decide what gets rejected.

## Common expert mistakes

- Treating priority as a boolean instead of an ordered policy.
- Forgetting starvation.
- Using priority queues without rejection or backpressure.

## Guided practice

A heap contains 65,536 items. Estimate the maximum comparisons for one insert using heap height. Then initialize from 65,536 existing items: which bound is more appropriate, O(n) build-heap or n separate O(log n) inserts, and why?

## Self-check

1. Where are the children of array index `i` in a binary heap?
2. Why is peek O(1) but remove-priority O(log n)?
3. Why is build-heap O(n)?
4. What prevents starvation under priority scheduling?

## Explained answers

1. At `2i + 1` and `2i + 2` for zero-based arrays.
2. The root already has priority; removal must restore order down the tree.
3. Most nodes are low in the tree and have little distance to move, so total sift work is linear.
4. Aging, quotas, maximum waits, bounded queues, or explicit rejection. For the practice, height is 16, so one insert is bounded around that many levels; build-heap is the right initialization bound.

## Sources and next work

Study RES-01 and RES-05. Then complete EX-06.
