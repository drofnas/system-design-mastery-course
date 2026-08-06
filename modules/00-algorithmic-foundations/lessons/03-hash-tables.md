---
lesson_id: L03
title: "Hash Tables"
---

# Hash Tables

## Outcomes

- Explain hashing, buckets, collisions, load factor, and resizing.
- State the assumption behind expected O(1) lookup.
- Connect hash behavior to abuse resistance.

## Mechanism

A hash table maps a key to a bucket. With a good hash function and controlled
load factor, lookup, insert, and delete are expected O(1). Collisions are handled
by chaining, probing, or another collision policy.

The guarantee is conditional. Adversarial keys, weak hashing, too much load, or
unbounded resize work can turn the structure into a latency problem.

## Worked Example

An idempotency store receives request IDs and rejects duplicates. A hash table
fits insert-if-absent and lookup. Expiry still needs a second mechanism, such as
a heap or time buckets, or old keys stay forever.

## Common Expert Mistakes

- Assuming random input when keys are user-controlled.
- Forgetting resize spikes.
- Using only a hash table when ordered cleanup is required.

## Guided Practice

For one key-value structure you maintain, identify the hash key, collision
policy, load-factor limit, and cleanup path.

## Self-Check

Why does M13 care about hash tables? Because untrusted input can turn expected
constant-time work into an abuse vector.

## Sources And Next Work

Study RES-01 and RES-02. Then complete EX-03 and EX-09.
