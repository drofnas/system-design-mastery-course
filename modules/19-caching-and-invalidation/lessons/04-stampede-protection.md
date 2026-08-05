---
lesson_id: L04
title: "Stampede Protection"
---

# Stampede Protection

## Outcomes

- Explain cache stampede and thundering-herd behavior.
- Use coalescing, jitter, leases, and bounded stale responses.
- Preserve useful work during regeneration.

## Mechanism

A stampede happens when many callers miss or expire the same item and all try to
regenerate it. The cache meant to protect the origin becomes an amplifier.

Common controls are request coalescing, single-flight locks, lease tokens,
jittered expiry, probabilistic early refresh, stale-while-revalidate with a
bounded age, and admission control for regeneration work.

## Worked Example

A homepage fragment expires at exactly noon. Ten thousand requests arrive. A
single-flight lock lets one request regenerate while others wait or receive a
marked stale response within a strict bound.

## Common Expert Mistakes

- Giving every item the same TTL.
- Letting regeneration bypass normal deadline and retry budgets.
- Serving unmarked stale data indefinitely.

## Guided Practice

Name one hot cached item. Design its expiry jitter, regeneration owner, and
fallback response while origin is slow.

## Self-Check

What is the central stampede invariant? Many misses should cause at most bounded
regeneration work.

## Sources And Next Work

Study RES-04. Then complete EX-07.
