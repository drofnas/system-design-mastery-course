---
lesson_id: L05
title: "Heaps and Priority Queues"
---

# Heaps and Priority Queues

## Outcomes

- Explain heap order and priority-queue operations.
- Connect priority queues to overload and scheduling decisions.
- State fairness risks.

## Mechanism

A binary heap stores a partial order that makes the minimum or maximum item cheap
to inspect. Insert and remove-priority are O(log n). Peek is O(1).

Priority queues are policy machines. They decide which work moves next. That can
protect critical work during overload, but it can also starve lower-priority
work unless the policy includes fairness or aging.

## Worked Example

M02 discusses admission control. If requests have priority classes, a priority
queue can admit evacuation alerts before analytics exports. The design must
still bound queue length and decide what gets rejected.

## Common Expert Mistakes

- Treating priority as a boolean instead of an ordered policy.
- Forgetting starvation.
- Using priority queues without rejection or backpressure.

## Guided Practice

Choose a queue in your system and define the comparison function. Then name one
case where that comparison function would produce an unfair result.

## Self-Check

What invariant should a priority queue preserve? It should return the highest
eligible priority item according to the stated policy.

## Sources And Next Work

Study RES-01. Then complete EX-06.
