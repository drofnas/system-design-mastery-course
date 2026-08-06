# Module 19: Caching and Invalidation

This draft module gives caching a dedicated home. Earlier modules mention cache
behavior in storage engines, CDNs, and inference systems; this module teaches
the general mechanism and points back to those specializations. It reads
naturally after M07's storage-engine lessons and before or alongside M16's
browser/CDN cache material, but it is numbered last because it acts as a
cross-course synthesis.

This module is intentionally labless in this phase. Caching is well suited to an
executable stampede and eviction harness, but Phase 2 reserves that build for a
future lab pass so the pre-quiz close-out can focus on lesson depth, citation
consistency, and the existing lab floor.

Use this module when a design conversation says "just cache it." The local work
turns that sentence into a concrete policy: what is authoritative, which key is
safe, how stale is allowed, who regenerates, and when the cache should be
removed.
That policy is the unit of learning; cache product names are secondary.

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
- Defend a cache with rollback and removal evidence, not just a faster happy path.

## Lessons

1. [Cache Placement and Read/Write Paths](lessons/01-cache-placement-read-write-paths.md)
2. [Eviction Policies and Hit-Rate Economics](lessons/02-eviction-policies-hit-rate-economics.md)
3. [Invalidation and Coherence](lessons/03-invalidation-coherence.md)
4. [Stampede Protection](lessons/04-stampede-protection.md)
5. [Cache Failure Modes](lessons/05-cache-failure-modes.md)
6. [Caching Decisions and Defense](lessons/06-caching-decisions-defense.md)

## Practice And Lab

Complete [exercises](exercises/exercises.md), then compare with the
[answer key](exercises/answer-key.md). No executable lab is required for this
draft module; use the exercises as the local reinforcement path.

## Quiz Status

This module is draft. Its quiz package is intentionally deferred to the next
quiz-bank cycle. The current exit condition is lesson and practice parity, not a
question bank.

## Optional Project

Write a cache policy memo for one real or imagined system. Include keys, TTLs,
authority, invalidation, stampede protection, privacy controls, observability,
rollback, and the condition that would make you remove the cache.
