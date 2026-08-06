# Module 19 Exercises

Treat each answer as a cache policy fragment. Name authority, key shape,
freshness, and failure behavior whenever the prompt gives enough information.
If the prompt gives numbers, calculate both latency and origin-load effects; if
it gives private data, state the key dimensions that prevent cross-principal
serving. Avoid answers that only name a cache product; the policy is the answer.

## EX-01 Placement

For a product catalog read path, compare in-process, shared service, CDN, and
database-adjacent cache placement. Include which hop each placement avoids and
which invalidation or privacy risk it introduces.

## EX-02 Write Policy

Choose cache-aside, write-through, write-around, or write-behind for user profile
updates. State the freshness, ordering, durability, and loss risks.

## EX-03 Hit-Rate Economics

A cache serves 80 percent of 10,000 requests per minute. Origin requests cost 20
ms and cache requests cost 2 ms. Estimate average service time and origin request
rate before and after caching.

## EX-04 Eviction

Compare LRU, LFU, and a scan-resistant policy for a workload with one large scan
plus a small hot set. State which policy you would test first and what trace
evidence would change your mind.

## EX-05 Invalidation

Design invalidation for a permissions object. State the authority source and the
maximum stale window. Include subject, tenant, and policy version in the key or
validation path.

## EX-06 Coherence

Two regions can update the same derived cache. Name the conflict and coherence
rule. Include whether the design uses write-invalidate, write-update, versioned
keys, or reconciliation from authority.

## EX-07 Stampede

A hot item expires and 5,000 clients request it within one second. Name two
controls. Estimate origin regenerations with no coalescing and with single-flight.

## EX-08 Negative Caching

When should a system cache a "not found" result, and what can go wrong?
Include a TTL or invalidation trigger.

## EX-09 Privacy

Explain how a public cache key can leak private content.
Name the missing key dimensions.

## EX-10 Decision Defense

Write a cache policy decision with owner, rollback, observability, and removal
conditions. Include one numeric target for hit rate, stale age, or origin load.

## EX-11 Lab Deferral

M19 has no executable lab in this phase. Write the first two scenarios you would
want a future cache lab to model, and name the emitted field that would prove
each mechanism.
