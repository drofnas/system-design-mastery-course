---
lesson_id: L02
title: "Arrays, Dynamic Arrays, and Locality"
---

# Arrays, Dynamic Arrays, and Locality

## Outcomes

- Explain indexed access, append, resize, and traversal costs.
- Connect contiguous layout to cache behavior.
- Identify when linked structures are worth their pointer cost.

## Prerequisites

Algebra, comfort reading loops and arrays in any language, and the ability to separate a model from a measurement.

## Mechanism

An array stores elements contiguously, so index lookup is O(1) when the index is
known. A dynamic array adds spare capacity and resizes when full. Appends are
amortized O(1), but a resize copies many elements at once.

Linked structures make insertion and removal cheap when you already hold the
node, but traversal follows pointers. Pointer chasing often loses locality.

### Growth, headroom, and locality

A dynamic array trades spare capacity for cheap appends. With doubling, capacity grows 1, 2, 4, 8, and so on. Immediately before a resize the array is full. During resize, the runtime may need old storage plus new storage, so a full array of `n` elements can transiently need about `3n` element slots of memory: `n` old, `2n` new. After the copy, half the new array is headroom. A smaller growth factor reduces waste but increases copy frequency.

Sequential access is friendly to cache lines and prefetching because nearby addresses are likely to be needed soon. Pointer-based structures can win when stable references matter, when inserts and deletes happen after the node is already found, or when moving large objects is unacceptable. They lose when every operation first has to search from the head.

The lab is intentionally modest about locality. It compares Python-level index traversal with Python-level node traversal so it does not confuse C builtin speed with data-structure speed. It still cannot prove CPU cache behavior because CPython integers are boxed objects and a list stores references, not packed primitive values. Treat the result as local evidence about this runtime, not as a universal locality benchmark.

## Worked Example

For 10,000 events that must be scanned in order, an array is often a better
default than a linked list. Both do O(n) logical work, but the array lets the
processor fetch nearby elements predictably.

## Common Expert Mistakes

- Saying amortized O(1) means every append is cheap.
- Choosing a linked list for insertion while ignoring how the insertion point is found.
- Forgetting that contiguous growth can require copying and memory headroom.

## Guided Practice

A dynamic array has 1,024 live elements and capacity 1,024. It doubles on the next append. Compute the new capacity, approximate peak slots during the copy, and post-resize unused headroom. Then name one workload where a linked structure could still be correct.

## Self-Check

1. Why is indexed array access O(1)?
2. What does doubling buy and what does it cost?
3. When is linked-list insertion actually O(1)?
4. Why does the lab not prove raw hardware cache behavior?

## Explained answers

1. The address is computed from base plus index times element width, or from an equivalent runtime table lookup.
2. It bounds total copy work across many appends but creates spare memory and occasional resize spikes.
3. Only when the insertion point or node reference is already known; finding that point may still be O(n).
4. CPython lists store references to objects and the lab runs interpreter loops, so it shows local runtime behavior, not isolated cache-line mechanics. For the practice, new capacity is 2,048, peak slots are about 3,072, and headroom after the append is 1,023 slots.

## Sources And Next Work

Study RES-01 and RES-03. Then complete EX-02 and EX-04.
