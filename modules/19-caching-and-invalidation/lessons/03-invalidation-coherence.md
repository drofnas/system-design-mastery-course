---
lesson_id: L03
title: "Invalidation and Coherence"
---

# Invalidation and Coherence

## Outcomes

- Explain invalidation, refresh, TTL, and versioned cache entries.
- Choose a coherence rule for multiple cached copies.
- Bound stale serving.

## Prerequisites

Modules 2, 6, 7, and 16 are helpful context; the required baseline is comfort tracing read/write paths and freshness requirements.

## Mechanism

Invalidation removes or marks cached data stale after an authoritative change.
Coherence defines how multiple copies converge. Common tools include versioned
keys, change events, explicit purge, short TTLs, read repair, and stale markers.

Not every cache needs strong freshness. Many do need honest stale limits. A
permission cache, billing cache, or personalized response has a different risk
profile from a public product-image cache.

### Keys, versions, and regional copies

TTL is a bounded guess: it limits age but does not know when authority changed. Explicit invalidation reacts to change events but must reach every copy. Versioned keys avoid many coherence races by making new writes produce new names; old entries can expire naturally without being mistaken for the latest representation. Write-invalidate removes stale copies after authority changes. Write-update pushes new values to caches. The right choice depends on write frequency, stale risk, and fanout.

Cache key design is part of correctness. A response may vary by tenant, subject, role, locale, device class, experiment flag, schema version, compression, and authorization state. Omitting one dimension can create a leak or a stale representation that looks like a hit. Negative caching has the same problem: a cached not-found result needs a short TTL or invalidation when the object is created.

Across regions, coherence should name the authority and conflict rule. If two regions can write a derived representation, the cache has become a multi-writer system and needs versions, fencing, or reconciliation from authority.

## Worked example

A permissions object should include subject, tenant, policy version, and resource
scope in its cache key or validation path. A role removal should invalidate or
bypass cached permissions before a sensitive action is allowed.

## Common expert mistakes

- Using TTL as the only invalidation strategy for high-risk data.
- Forgetting derived indexes and regional copies.
- Allowing two writers to update the same derived entry without version checks.

## Guided practice

A permission cache key includes tenant and resource but omits subject and policy version. Name two possible wrong responses. Then design a versioned key and a maximum stale window for role removal.

## Self-check

1. Why is TTL not the same as invalidation?
2. How do versioned keys sidestep many purge races?
3. What dimensions commonly belong in a cache key?
4. What is the risk of negative caching?

## Explained answers

1. TTL expires by time; invalidation responds to an authoritative change.
2. New writes use a new key, so old entries are no longer consulted for current reads.
3. Tenant, subject, authorization state, locale, device, feature flag, content negotiation, and schema version as applicable.
4. A newly created object can remain hidden until the negative entry expires. For the practice, subject A could receive subject B's permission, and old policy could survive role removal; include subject and policy version in the key and bypass or cap stale permission reads to a very short window.

## Sources and next work

Study RES-02 and RES-05. Then complete EX-05 and EX-06.
