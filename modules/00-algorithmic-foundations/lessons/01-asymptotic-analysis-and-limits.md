---
lesson_id: L01
title: "Asymptotic Analysis and Its Limits"
---

# Asymptotic Analysis and Its Limits

## Outcomes

- Describe Big-O, theta, omega, and amortized cost.
- Separate growth claims from local runtime claims.
- State the evidence needed before a design decision.

## Prerequisites

Algebra, comfort reading loops and arrays in any language, and the ability to separate a model from a measurement.

## Mechanism

Asymptotic analysis asks how work grows as input size grows. Big-O gives an upper
bound, theta gives a tight bound, and omega gives a lower bound. The notation is
useful because system data rarely stays the size it was during development.

The trap is treating a growth class as a stopwatch. O(n) code can beat O(log n)
code for small or cache-friendly data. A hash table can be expected O(1) and
still become poor under bad hashing, high load factor, or memory pressure.

### Formal boundary and amortization

`f(n) = O(g(n))` means there are positive constants `c` and `n0` such that `f(n) <= c*g(n)` for every `n >= n0`. `Theta` means both upper and lower bounds hold; `Omega` means a lower bound. Those constants matter in engineering because production `n` may live below the crossing point for years. The notation is a statement about growth after the boundary, not a runtime promise.

Amortized analysis is different from average case. Average case depends on a probability distribution over inputs. Amortized analysis bounds a sequence of operations even when one operation is expensive. For a dynamic array that doubles capacity, appends copy capacities `1 + 2 + 4 + ... < 2n` across `n` appends. The total work is original writes `n` plus copied elements less than `2n`, so the sequence is O(n) and each append is O(1) amortized. The single resize is still a worst-case latency spike.

For a loop nest, count the number of times the inner body runs. If `for i in 1..n` contains `for j in 1..i`, the work is `1 + 2 + ... + n = n(n+1)/2`, which is Theta(n^2). If the inner loop halves a value each time, it contributes logarithmic growth instead.

### Repeatable technique

1. Name the input variable that can grow.
2. Count dominant operations as a function of that variable.
3. State upper, lower, and tight bounds only when the evidence supports them.
4. Separate worst-case, expected, average-case, and amortized claims.
5. Record the constant, locality, and measurement assumptions that could reverse a small-input decision.

## Worked example

If an operation scans 1,000 items today and 1,000,000 tomorrow, a linear scan
grows by 1,000x. A balanced-tree lookup grows from about 10 comparisons to about
20. That difference is a design signal. It is not proof that the tree is faster
for today's workload.

## Common expert mistakes

- Ignoring constants for hot paths.
- Using worst-case notation without naming the adversary or input condition.
- Calling amortized cost a latency guarantee.
- Comparing algorithms without checking memory layout.

## Guided practice

A dynamic array starts with capacity 1 and doubles when full. For 17 appends, list the resize capacities copied and compute the total copied elements. Then state the amortized append cost and the worst single append cost.

## Self-check

1. What constants appear in the formal Big-O definition?
2. Why is amortized O(1) not the same as average-case O(1)?
3. What is the complexity of `for i in 1..n: for j in 1..i`?
4. What must be measured before choosing between two structures with different constants?

## Explained answers

1. A positive multiplier `c` and a threshold `n0`; the bound only needs to hold beyond `n0`.
2. Amortized cost bounds a sequence without assuming random input; average case depends on an input distribution.
3. The body runs `n(n+1)/2` times, so the tight bound is Theta(n^2).
4. Representative input sizes, operation mix, memory layout, branch behavior, allocation cost, and tail latency for the actual workload. For the practice, copied capacities are `1 + 2 + 4 + 8 = 15`; total work is bounded by a small multiple of 17, but the append that grows from 16 to 32 copies 16 existing elements.

## Sources and next work

Study RES-01 and RES-02. Then complete EX-01.
