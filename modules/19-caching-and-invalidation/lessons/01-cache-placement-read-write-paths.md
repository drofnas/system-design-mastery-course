---
lesson_id: L01
title: "Cache Placement and Read/Write Paths"
---

# Cache Placement and Read/Write Paths

## Outcomes

- Compare in-process, shared, database-adjacent, and edge caches.
- Explain cache-aside, write-through, write-around, and write-behind.
- Name the authoritative source for each cached representation.

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

## Worked Example

A product catalog read can use CDN cache for public product pages and a shared
cache for internal inventory summaries. Checkout authorization must still read
from authority or a tightly bounded permission cache.

## Common Expert Mistakes

- Caching before naming the authoritative source.
- Treating write-behind as a performance switch instead of a consistency change.
- Ignoring private representation keys.

## Guided Practice

Draw a read and write path for one object. Mark where cached data can be served
and where authority must be consulted.

## Self-Check

What does cache placement decide? It decides which cost is avoided and which
staleness, dependency, privacy, or recovery risk is accepted.

## Sources And Next Work

Study RES-01 and RES-03. Then complete EX-01 and EX-02.
