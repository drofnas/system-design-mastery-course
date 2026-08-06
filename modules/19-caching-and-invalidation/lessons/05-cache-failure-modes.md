---
lesson_id: L05
title: "Cache Failure Modes"
---

# Cache Failure Modes

## Outcomes

- Recognize cold start, poisoning, key collision, privacy leak, and stale data failures.
- Connect cache failures to M13 and M16 controls.
- Name observability required for cache diagnosis.

## Prerequisites

Modules 2, 6, 7, and 16 are helpful context; the required baseline is comfort tracing read/write paths and freshness requirements.

## Mechanism

Caches fail by omission and commission. Cold start removes expected protection.
Poisoning stores a bad representation. Key collisions or incomplete keys serve
the wrong data. Private data leaks when subject or authorization context is
missing. Stale data becomes unsafe when it crosses a freshness or authority line.

The evidence is not just hit rate. You need key dimensions, freshness age,
origin fallback status, regeneration count, subject/tenant boundaries, and
whether stale responses are marked.

### Failure patterns beyond misses

Cold start after deploy, flush, or region failover removes the cache's protective effect at the exact time the origin may also be fragile. A metastable failure appears when origin is saturated, regeneration fails or times out, and the cache never warms enough to reduce origin load. Prewarming, admission control, stale serving, and gradual rollout are recovery controls.

Poisoning stores an incorrect or malicious representation. Key collision and incomplete key design serve the wrong value. Private-data leakage through a shared key is the general form of M16's `f06-private-cache-leak`: the cache treats two different authorization contexts as equivalent. M13's tenant-isolation lens applies directly.

Other failures include unbounded memory growth from high-cardinality keys, stale data after schema change, negative-cache entries hiding newly created objects, and observability that counts poisoned or unauthorized hits as success. A useful dashboard separates public/private hit rate, stale age, regeneration count, origin fallback status, eviction reason, and key dimensions.

## Worked Example

M16's private-cache-leak fixture is the web version of a general rule: a shared
cache key that omits subject identity can serve private content to another
subject.

## Common Expert Mistakes

- Counting a poisoned hit as success.
- Aggregating hit rate across public and private data.
- Missing negative-cache effects on newly created objects.

## Guided Practice

A cache is flushed during a deploy and receives 20,000 reads/minute. Before the flush it had 95 percent hit rate. Compute origin reads before and immediately after the flush. Then name two controls that prevent a cold-start overload from becoming metastable.

## Self-Check

1. Why can a cache hit be a failure?
2. What turns cold start into metastability?
3. Which key omission causes private-data leakage?
4. Why split public and private hit-rate metrics?

## Explained answers

1. It may return poisoned, stale, unauthorized, or schema-incompatible data.
2. Origin overload prevents successful regeneration, so the cache cannot refill and load remains high.
3. Missing subject, tenant, authorization, or private variation dimensions.
4. Aggregation can hide privacy and correctness failures behind good public-cache performance. For the practice, origin reads go from 1,000/minute to 20,000/minute; controls include prewarming, stale serving, single-flight, and regeneration admission limits.

## Sources And Next Work

Study RES-02 and revisit M16 F06. Then complete EX-08 and EX-09.
