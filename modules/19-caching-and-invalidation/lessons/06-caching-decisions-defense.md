---
lesson_id: L06
title: "Caching Decisions and Defense"
---

# Caching Decisions and Defense

## Outcomes

- Write a cache policy decision.
- Include ownership, observability, rollback, and removal criteria.
- Cross-reference specialized cache modules without duplicating them.

## Prerequisites

Modules 2, 6, 7, and 16 are helpful context; the required baseline is comfort tracing read/write paths and freshness requirements.

## Mechanism

A cache decision should name the workload, authoritative source, key shape,
freshness limit, invalidation trigger, eviction policy, stampede control,
privacy boundary, owner, dashboards, alerts, rollback, and removal trigger.

M07 owns storage-index internals. M16 owns browser, CDN, and edge behavior. M17
owns inference KV-cache behavior. This module owns the general mechanism and the
decision vocabulary that travels across those cases.

### Decision artifact and safe region

A defensible cache decision is an operating contract. It should state the user outcome, avoided cost, authoritative source, representation, key dimensions, freshness bound, invalidation trigger, eviction/admission policy, stampede control, privacy boundary, owner, metrics, alerts, rollback, and removal condition. The safe region names when the cache is allowed to serve: for example public product summaries, policy version current, stale age under 60 seconds, and origin errors below a declared threshold.

Rollout should start with shadow reads or read-through metrics before serving from cache. Compare hit rate, effective latency, origin load, stale age, wrong-answer reports, and regeneration concurrency. Reversal conditions should be mechanical: disable cache on stale age over the bound, unauthorized variant detection, origin regeneration saturation, or invalidation lag.

Removal criteria matter because caches become permanent complexity. If hit rate stays low, invalidation work exceeds savings, or correctness exceptions dominate, deleting the cache is the right architectural outcome.

### Repeatable technique

1. Name authority and representation.
2. Define key dimensions and freshness bound.
3. Pick read, write, eviction, and stampede policies.
4. Define observability and rollback triggers.
5. Revisit the cache after warm-up and remove it if evidence fails.

## Worked example

For a public catalog summary, choose cache-aside in a shared cache, key by
catalog version and locale, set TTL with jitter, invalidate on publication, use
single-flight regeneration, and serve bounded marked stale data during origin
failure. Remove the cache if hit rate stays low after warm-up or if invalidation
work exceeds origin savings.

## Common expert mistakes

- Adding a cache without an owner.
- Forgetting the removal condition.
- Measuring only latency and not correctness.

## Guided practice

Write a cache decision for a catalog summary. Use 12,000 reads/minute, 92 percent target hit rate, 3 ms hit cost, and 45 ms origin cost. Compute expected latency and origin read rate at target, then state one rollback trigger.

## Self-check

1. What is the first field in a cache decision?
2. Why include removal criteria?
3. What evidence proves the cache helps origin load?
4. What should happen when stale age exceeds the bound?

## Explained answers

1. The authoritative source and representation; without authority, freshness and correctness cannot be judged.
2. The cache is optional complexity and should disappear if it fails its economics or correctness contract.
3. Miss rate and origin request count before/after, not just average latency.
4. Disable serving stale entries, bypass cache, purge, or roll back depending on the policy. For the practice, expected latency is `0.92*3 + 0.08*45 = 6.36 ms`, and origin reads are 960/minute; rollback on invalidation lag, unauthorized variants, or regeneration saturation.

## Sources and next work

Study RES-01 and RES-03. Then complete EX-10.
