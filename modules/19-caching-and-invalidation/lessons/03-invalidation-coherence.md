---
lesson_id: L03
title: "Invalidation and Coherence"
---

# Invalidation and Coherence

## Outcomes

- Explain invalidation, refresh, TTL, and versioned cache entries.
- Choose a coherence rule for multiple cached copies.
- Bound stale serving.

## Mechanism

Invalidation removes or marks cached data stale after an authoritative change.
Coherence defines how multiple copies converge. Common tools include versioned
keys, change events, explicit purge, short TTLs, read repair, and stale markers.

Not every cache needs strong freshness. Many do need honest stale limits. A
permission cache, billing cache, or personalized response has a different risk
profile from a public product-image cache.

## Worked Example

A permissions object should include subject, tenant, policy version, and resource
scope in its cache key or validation path. A role removal should invalidate or
bypass cached permissions before a sensitive action is allowed.

## Common Expert Mistakes

- Using TTL as the only invalidation strategy for high-risk data.
- Forgetting derived indexes and regional copies.
- Allowing two writers to update the same derived entry without version checks.

## Guided Practice

For one cached object, write the event that makes it stale and the maximum stale
duration you can tolerate.

## Self-Check

What is the simplest coherence rule? One authority writes, cached copies carry a
version, and stale writes lose.

## Sources And Next Work

Study RES-02. Then complete EX-05 and EX-06.
