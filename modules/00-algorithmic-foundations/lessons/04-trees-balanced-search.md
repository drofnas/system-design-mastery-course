---
lesson_id: L04
title: "Trees and Balanced Search"
---

# Trees and Balanced Search

## Outcomes

- Explain binary search trees and balance.
- Compare hash lookup with ordered search.
- Explain why B-trees matter for storage systems.

## Mechanism

A search tree preserves order. If the tree is balanced, search, insert, and
delete are O(log n). If it degenerates into a chain, those operations become
linear. Balanced trees spend maintenance work to preserve height.

B-trees widen each node so one read brings many keys. That makes them a natural
bridge to M07's storage-engine indexes.

## Worked Example

If an API needs "all events for tenant T between two timestamps," order matters.
A hash table can find one exact key quickly, but a tree can seek to the range and
scan forward.

## Common Expert Mistakes

- Choosing hashing for range queries.
- Forgetting that balance maintenance changes write cost.
- Treating a storage index as just an in-memory tree.

## Guided Practice

Take one query from a database-backed service and name whether it is point
lookup, prefix lookup, range lookup, or ordered aggregation.

## Self-Check

Why do B-trees use high fanout? To reduce the number of block or page reads per
lookup.

## Sources And Next Work

Study RES-01. Then connect this lesson to M07 L03.
