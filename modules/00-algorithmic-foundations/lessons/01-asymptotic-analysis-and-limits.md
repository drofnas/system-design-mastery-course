---
lesson_id: L01
title: "Asymptotic Analysis and Its Limits"
---

# Asymptotic Analysis and Its Limits

## Outcomes

- Describe Big-O, theta, omega, and amortized cost.
- Separate growth claims from local runtime claims.
- State the evidence needed before a design decision.

## Mechanism

Asymptotic analysis asks how work grows as input size grows. Big-O gives an upper
bound, theta gives a tight bound, and omega gives a lower bound. The notation is
useful because system data rarely stays the size it was during development.

The trap is treating a growth class as a stopwatch. O(n) code can beat O(log n)
code for small or cache-friendly data. A hash table can be expected O(1) and
still become poor under bad hashing, high load factor, or memory pressure.

## Worked Example

If an operation scans 1,000 items today and 1,000,000 tomorrow, a linear scan
grows by 1,000x. A balanced-tree lookup grows from about 10 comparisons to about
20. That difference is a design signal. It is not proof that the tree is faster
for today's workload.

## Common Expert Mistakes

- Ignoring constants for hot paths.
- Using worst-case notation without naming the adversary or input condition.
- Calling amortized cost a latency guarantee.
- Comparing algorithms without checking memory layout.

## Guided Practice

For a recent design, write the dominant operation, input size today, plausible
input size later, and the growth class you are assuming.

## Self-Check

Why can an O(n) array scan beat an O(log n) tree lookup? Because contiguous
memory, fewer branches, and lower allocation overhead can dominate for small or
medium inputs.

## Sources And Next Work

Study RES-01 and RES-02. Then complete EX-01.
