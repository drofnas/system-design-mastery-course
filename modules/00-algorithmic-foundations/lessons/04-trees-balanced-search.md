---
lesson_id: L04
title: "Trees and Balanced Search"
---

# Trees and Balanced Search

## Outcomes

- Explain binary search trees and balance.
- Compare hash lookup with ordered search.
- Explain why B-trees matter for storage systems.

## Prerequisites

Algebra, comfort reading loops and arrays in any language, and the ability to separate a model from a measurement.

## Mechanism

A search tree preserves order. If the tree is balanced, search, insert, and
delete are O(log n). If it degenerates into a chain, those operations become
linear. Balanced trees spend maintenance work to preserve height.

B-trees widen each node so one read brings many keys. That makes them a natural
bridge to M07's storage-engine indexes.

### Balance and page-shaped trees

A plain binary search tree can become a linked list if keys arrive in sorted order. Balance invariants prevent that by rotating or splitting nodes so height remains logarithmic. The design spends write work to preserve predictable lookup and range behavior. That is the core trade: more maintenance on mutation for bounded search depth.

B-trees and B+ trees widen a node to hold many keys and children. If fanout is `B`, height is roughly `log_B(n)`. With one billion keys and fanout 100, height is about `log_100(1,000,000,000)`, or 4.5 levels. With binary fanout, the same key count is about 30 levels. Storage engines care because each level can imply a page read, a latch, cache pressure, and recovery metadata.

Trees also preserve order. After a seek to the first key in a range, the scan can continue through adjacent leaves. That capability is why M07 treats B-tree indexes as access-path contracts, not just lookup accelerators.

## Worked Example

If an API needs "all events for tenant T between two timestamps," order matters.
A hash table can find one exact key quickly, but a tree can seek to the range and
scan forward.

## Common Expert Mistakes

- Choosing hashing for range queries.
- Forgetting that balance maintenance changes write cost.
- Treating a storage index as just an in-memory tree.

## Guided Practice

A B-tree-like index has 100-way fanout and 100,000,000 keys. Estimate height with `log_B(n)`. Compare that with binary height using powers of two. Then name one range query a hash table cannot serve alone.

## Self-Check

1. What happens when a BST degenerates?
2. What does a balancing invariant buy?
3. Why does fanout matter for disk-resident data?
4. Why are trees better than hash tables for ranges?

## Explained answers

1. Search, insert, and delete can become O(n).
2. It keeps height logarithmic at the cost of mutation maintenance.
3. Larger fanout reduces levels, and levels often map to page reads or cache misses.
4. Trees preserve sorted order, so they can seek then scan contiguous key ranges. For the practice, height is about 4; binary height is about 27; a tenant/time-window query is a typical range.

## Sources And Next Work

Study RES-01 and RES-06. Then connect this lesson to M07 L03.
