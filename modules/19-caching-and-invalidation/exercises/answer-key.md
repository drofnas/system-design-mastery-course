# Module 19 Exercise Answer Key

## EX-01

In-process is fastest but duplicated and hard to invalidate globally. A shared
cache centralizes policy but adds a network hop. CDN placement helps public
content near users. Database-adjacent caching can protect expensive reads but
does not solve client-edge latency.

## EX-02

Profile updates usually favor write-through or cache-aside with explicit
invalidation because freshness matters. Write-behind risks losing or reordering
updates unless the queue is durable and reconciled.

## EX-03

Without cache: `10,000 * 20 ms / 10,000 = 20 ms`. With cache:
`0.8 * 2 + 0.2 * 20 = 5.6 ms`.

## EX-04

LRU can evict the hot set during a scan unless protected by segmentation. LFU
keeps frequent items but can cling to old popularity unless it decays counts.

## EX-05

The authoritative store owns permissions. Invalidation should happen on
permission change and cached permissions should have a short bounded stale
window or be bypassed for sensitive actions.

## EX-06

The conflict is dual authority over a derived representation. Pick one writer,
version derived entries, and reject stale writes or reconcile from authority.

## EX-07

Use request coalescing and jittered early refresh. Other valid controls include
leases, stale-while-revalidate with bounds, admission control, and prewarming.

## EX-08

Negative caching is useful when misses are repeated and authoritative data does
not appear immediately. It can hide newly created data if TTLs are too long.

## EX-09

If the cache key omits subject, tenant, authorization state, or private headers,
one user's representation can be served to another user.

## EX-10

A strong answer names the authoritative source, key shape, TTL, invalidation
trigger, stampede control, owner, metrics, alarms, rollback, and removal trigger.
