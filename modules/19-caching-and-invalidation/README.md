# Module 19: Caching and Invalidation

This draft module gives caching a dedicated home. Earlier modules mention cache
behavior in storage engines, CDNs, and inference systems; this module teaches
the general mechanism and points back to those specializations.

## Prerequisites

- M02 for workload and overload reasoning.
- M07 for storage-engine context.
- M16 for browser, CDN, and edge-specific cache behavior.
- M17 for inference KV-cache specialization.

## Outcomes

- Place caches deliberately in read and write paths.
- Choose eviction and TTL policies from workload shape and freshness risk.
- Design invalidation, coherence, and stampede protection.
- Recognize cache failures involving cold start, poisoning, private data, and stale serving.

## Lessons

1. [Cache Placement and Read/Write Paths](lessons/01-cache-placement-read-write-paths.md)
2. [Eviction Policies and Hit-Rate Economics](lessons/02-eviction-policies-hit-rate-economics.md)
3. [Invalidation and Coherence](lessons/03-invalidation-coherence.md)
4. [Stampede Protection](lessons/04-stampede-protection.md)
5. [Cache Failure Modes](lessons/05-cache-failure-modes.md)
6. [Caching Decisions and Defense](lessons/06-caching-decisions-defense.md)

## Practice

Complete [exercises](exercises/exercises.md), then compare with the
[answer key](exercises/answer-key.md). This draft has no quiz package yet.

## Optional Project

Write a cache policy memo for one real or imagined system. Include keys, TTLs,
authority, invalidation, stampede protection, privacy controls, observability,
rollback, and the condition that would make you remove the cache.
