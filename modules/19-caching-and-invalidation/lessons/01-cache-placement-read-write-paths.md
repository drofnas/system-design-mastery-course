---
lesson_id: L01
title: "Cache Placement and Read/Write Paths"
---

# Cache Placement and Read/Write Paths

## Outcomes

- Compare in-process, shared, database-adjacent, and edge caches.
- Explain cache-aside, write-through, write-around, and write-behind.
- Name the authoritative source for each cached representation.

## Prerequisites

Modules 2, 6, 7, and 16 are helpful context; the required baseline is comfort tracing read/write paths and freshness requirements.

## Mechanism

A cache stores a derived copy to reduce latency, cost, or load. Placement decides
which hop is avoided and which failure mode is introduced. A cache close to the
caller may be fast but harder to invalidate. A shared cache centralizes policy
but becomes another dependency. An edge cache helps public content but must not
serve private variants under a public key.

Write policy determines how authority and freshness move. Cache-aside is simple:
miss, load, write cache. Write-through updates cache and authority together.
Write-around skips cache on write. Write-behind accepts temporary divergence and
needs durability, ordering, and reconciliation.

### Tiers and ownership

Useful cache placement starts with the tier. A client cache can skip the network but only knows one user's context. A CDN or edge cache can absorb global read load for public or carefully keyed variants, but it cannot safely infer private authorization. A reverse proxy cache sits near application routing. An application in-process cache is fast but duplicated per instance. A shared cache centralizes policy at the cost of another dependency. A near-cache beside storage can protect expensive reads without improving client-edge latency. A database buffer pool is also a cache, but its authority and eviction rules belong to the storage engine.

Read-through and cache-aside differ in ownership. In cache-aside, the application owns miss loading and cache population. In read-through, the cache abstraction owns the miss path. Write-through synchronously updates cache and authority. Write-around writes authority and lets reads repopulate. Write-back or write-behind accepts divergence and needs durable queues, ordering, replay, and reconciliation. Every policy should state which representation is authoritative after a partial failure.

## Worked example

A product catalog read can use CDN cache for public product pages and a shared
cache for internal inventory summaries. Checkout authorization must still read
from authority or a tightly bounded permission cache.

## Common expert mistakes

- Caching before naming the authoritative source.
- Treating write-behind as a performance switch instead of a consistency change.
- Ignoring private representation keys.

## Guided practice

For a product page with 95 percent anonymous reads, 4 percent personalized reads, and 1 percent writes, draw two paths: public catalog read through CDN/shared cache and personalized checkout authorization through authority. Compute how many of 10,000 reads are not anonymous and must not share the public key.

## Self-check

1. What can a client cache know that a CDN usually cannot?
2. Who owns a miss in cache-aside?
3. Why is write-behind a consistency change?
4. Which tier protects origin but not client-edge latency?

## Explained answers

1. The exact local user/session context, though it may not know global freshness.
2. The application path that detects the miss, reads authority, and writes the cache.
3. Authority and cache can diverge, and lost or reordered buffered writes need recovery.
4. A database-adjacent or storage near-cache. For the practice, 5 percent of 10,000 reads, or 500, are personalized or otherwise not anonymous and need a separate key or authority path.

## Sources and next work

Study RES-01 and RES-03. Then complete EX-01 and EX-02.
