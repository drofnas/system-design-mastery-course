---
lesson_id: L02
title: "Arrays, Dynamic Arrays, and Locality"
---

# Arrays, Dynamic Arrays, and Locality

## Outcomes

- Explain indexed access, append, resize, and traversal costs.
- Connect contiguous layout to cache behavior.
- Identify when linked structures are worth their pointer cost.

## Mechanism

An array stores elements contiguously, so index lookup is O(1) when the index is
known. A dynamic array adds spare capacity and resizes when full. Appends are
amortized O(1), but a resize copies many elements at once.

Linked structures make insertion and removal cheap when you already hold the
node, but traversal follows pointers. Pointer chasing often loses locality.

## Worked Example

For 10,000 events that must be scanned in order, an array is often a better
default than a linked list. Both do O(n) logical work, but the array lets the
processor fetch nearby elements predictably.

## Common Expert Mistakes

- Saying amortized O(1) means every append is cheap.
- Choosing a linked list for insertion while ignoring how the insertion point is found.
- Forgetting that contiguous growth can require copying and memory headroom.

## Guided Practice

Name one queue, buffer, or cache in your system. Identify whether traversal,
indexed access, append, deletion, or resize dominates.

## Self-Check

What does locality change? It changes the constant factors and tail behavior of
the same asymptotic operation.

## Sources And Next Work

Study RES-01 and RES-03. Then complete EX-02 and EX-04.
