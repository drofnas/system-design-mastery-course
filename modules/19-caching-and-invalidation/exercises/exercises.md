# Module 19 Exercises

## EX-01 Placement

For a product catalog read path, compare in-process, shared service, CDN, and
database-adjacent cache placement.

## EX-02 Write Policy

Choose cache-aside, write-through, write-around, or write-behind for user profile
updates. State the freshness and loss risks.

## EX-03 Hit-Rate Economics

A cache serves 80 percent of 10,000 requests per minute. Origin requests cost 20
ms and cache requests cost 2 ms. Estimate average service time before and after.

## EX-04 Eviction

Compare LRU and LFU for a workload with one large scan plus a small hot set.

## EX-05 Invalidation

Design invalidation for a permissions object. State the authority source and the
maximum stale window.

## EX-06 Coherence

Two regions can update the same derived cache. Name the conflict and coherence
rule.

## EX-07 Stampede

A hot item expires and 5,000 clients request it within one second. Name two
controls.

## EX-08 Negative Caching

When should a system cache a "not found" result, and what can go wrong?

## EX-09 Privacy

Explain how a public cache key can leak private content.

## EX-10 Decision Defense

Write a cache policy decision with owner, rollback, observability, and removal
conditions.
