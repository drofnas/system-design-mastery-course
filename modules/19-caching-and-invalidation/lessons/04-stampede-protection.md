---
lesson_id: L04
title: "Stampede Protection"
---

# Stampede Protection

## Outcomes

- Explain cache stampede and thundering-herd behavior.
- Use coalescing, jitter, leases, and bounded stale responses.
- Preserve useful work during regeneration.

## Prerequisites

Modules 2, 6, 7, and 16 are helpful context; the required baseline is comfort tracing read/write paths and freshness requirements.

## Mechanism

A stampede happens when many callers miss or expire the same item and all try to
regenerate it. The cache meant to protect the origin becomes an amplifier.

Common controls are request coalescing, single-flight locks, lease tokens,
jittered expiry, probabilistic early refresh, stale-while-revalidate with a
bounded age, and admission control for regeneration work.

### Bounding regeneration work

Without coalescing, 10,000 simultaneous misses can become 10,000 origin regenerations. With single-flight, the target is one regeneration per key while other callers wait, receive bounded stale data, or fail fast within their M06 deadline. The caller behavior is part of the mechanism: unbounded wait just moves the outage from origin to the application queue.

TTL jitter spreads expiry. If 10,000 keys all expire at noon, the origin sees a wall of misses. If each TTL is jittered uniformly across a 10-minute window, the expected expiry pressure is about 1,000 keys/minute before request skew. Probabilistic early refresh refreshes before expiry with increasing probability as age approaches TTL; one simple form is `p = max(0, age - soft_ttl) / (hard_ttl - soft_ttl)`. At age 55 seconds with soft TTL 50 and hard TTL 60, `p = 0.5`.

Leases make one owner responsible for regeneration. Stale-while-revalidate preserves user-visible useful work while that owner runs, but stale age must be marked and bounded. Admission control protects origin when regeneration itself becomes the hot path.

Stampede controls should be scoped per key, not globally, unless the origin itself
is the constrained resource. A global lock can serialize unrelated keys and turn
a local hot item into a sitewide slowdown. A per-key single-flight group keeps
independent regeneration parallel while still bounding duplicate work for the
same object. The policy also needs a negative path: if regeneration fails, waiters
must not all become new owners at once. Keep the lease until a bounded retry,
serve marked stale data if allowed, or fail callers cleanly inside their deadline.

## Worked example

A homepage fragment expires at exactly noon. Ten thousand requests arrive. A
single-flight lock lets one request regenerate while others wait or receive a
marked stale response within a strict bound.

## Common expert mistakes

- Giving every item the same TTL.
- Letting regeneration bypass normal deadline and retry budgets.
- Serving unmarked stale data indefinitely.

## Guided practice

A hot key expires for 5,000 callers. Compare origin regenerations with no coalescing and with single-flight. Then use a 50-second soft TTL, 60-second hard TTL, and age 57 seconds to compute early-refresh probability.

## Self-check

1. What is the stampede invariant?
2. Why is TTL jitter useful?
3. What must waiters do during single-flight regeneration?
4. Why does stale-while-revalidate need an age bound?

## Explained answers

1. Many misses for the same key cause bounded regeneration work, ideally one in flight.
2. It spreads expirations so origin work is not synchronized.
3. Wait within their deadline, receive marked bounded stale data, or fail fast; they must not retry into a new stampede.
4. Otherwise stale data can become an unbounded correctness failure. For the practice, no coalescing can cause 5,000 regenerations; single-flight targets 1; probability is `(57-50)/(60-50) = 0.7`.

## Sources and next work

Study RES-04. Then complete EX-07.
