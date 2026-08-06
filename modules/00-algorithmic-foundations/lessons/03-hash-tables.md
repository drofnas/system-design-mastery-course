---
lesson_id: L03
title: "Hash Tables"
---

# Hash Tables

## Outcomes

- Explain hashing, buckets, collisions, load factor, and resizing.
- State the assumption behind expected O(1) lookup.
- Connect hash behavior to abuse resistance.

## Prerequisites

Algebra, comfort reading loops and arrays in any language, and the ability to separate a model from a measurement.

## Mechanism

A hash table maps a key to a bucket. With a good hash function and controlled
load factor, lookup, insert, and delete are expected O(1). Collisions are handled
by chaining, probing, or another collision policy.

The guarantee is conditional. Adversarial keys, weak hashing, too much load, or
unbounded resize work can turn the structure into a latency problem.

### Load factor, resizing, and adversaries

Load factor `alpha = entries / buckets` is the pressure gauge. With separate chaining and uniform hashes, a successful lookup examines roughly `1 + alpha` items on average. With open addressing, probe counts rise sharply as the table fills; the simple approximation `1 / (1 - alpha)` shows the cliff. At `alpha = 0.5`, the factor is about 2. At `alpha = 0.9`, it is about 10 before implementation details are considered.

Resizing restores load factor by allocating a larger table and rehashing entries. Across many inserts this can be amortized, but the resize itself is a tail event. If the table is on a request path, the design needs pre-sizing, background rebuild, sharding, or a visible latency budget.

Hashing is also a trust boundary. User-controlled keys can collide under a weak hash and turn expected O(1) work into long chains or probe sequences. Randomized seeding, keyed hashing, collision caps, tree buckets, and per-principal quotas are security controls as much as performance controls. A hash table also does not maintain order; range scans, prefix iteration, and earliest-expiry cleanup need a second structure.

## Worked Example

An idempotency store receives request IDs and rejects duplicates. A hash table
fits insert-if-absent and lookup. Expiry still needs a second mechanism, such as
a heap or time buckets, or old keys stay forever.

## Common Expert Mistakes

- Assuming random input when keys are user-controlled.
- Forgetting resize spikes.
- Using only a hash table when ordered cleanup is required.

## Guided Practice

A table has 1,000,000 buckets. Compare approximate open-addressing probe factors at 500,000 entries and 900,000 entries using `1/(1-alpha)`. Then decide whether a 1 percent ordered scan requirement can be served by the hash table alone.

## Self-Check

1. What assumption makes expected O(1) lookup plausible?
2. Why can resize be amortized yet still dangerous?
3. Why is alpha 0.9 a cliff for open addressing?
4. What capability does a hash table lack for ordered scans?

## Explained answers

1. Keys distribute uniformly enough and the implementation keeps load factor bounded.
2. The sequence has bounded average cost, but one request can pay the rehash cost unless resize is moved or controlled.
3. `1/(1-0.9) = 10`, far higher than the `2` factor at alpha 0.5.
4. It lacks sorted order; use a tree, sorted index, heap, or expiry buckets depending on the operation. For the practice, alpha is 0.5 and 0.9, so the approximate factors are 2 and 10; the ordered scan needs another ordered mechanism.

## Sources And Next Work

Study RES-01 and RES-02. Then complete EX-03 and EX-09.
