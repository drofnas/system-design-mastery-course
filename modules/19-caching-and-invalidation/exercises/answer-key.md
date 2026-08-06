# Module 19 Exercise Answer Key

## EX-01

In-process is fastest but duplicated and hard to invalidate globally. A shared
cache centralizes policy but adds a network hop. CDN placement helps public
content near users. Database-adjacent caching can protect expensive reads but
does not solve client-edge latency. Public catalog pages can use CDN keys by
version and locale; personalized inventory or authorization data needs a separate
key or authority read.

## EX-02

Profile updates usually favor write-through or cache-aside with explicit
invalidation because freshness matters. Write-behind risks losing or reordering
updates unless the queue is durable and reconciled. Write-around can be useful
when immediate rereads are rare, but it will make the next read pay the miss.

## EX-03

Without cache: `10,000 * 20 ms / 10,000 = 20 ms`. With cache:
`0.8 * 2 + 0.2 * 20 = 5.6 ms`. Origin request rate drops from 10,000/minute to
2,000/minute. The answer is incomplete if it reports only average latency and
omits the origin-load effect.

## EX-04

LRU can evict the hot set during a scan unless protected by segmentation. LFU
keeps frequent items but can cling to old popularity unless it decays counts. A
scan-resistant policy uses admission or segments so one-time objects do not evict
interactive hot data.

## EX-05

The authoritative store owns permissions. Invalidation should happen on
permission change and cached permissions should have a short bounded stale
window or be bypassed for sensitive actions. The key or validation path must
include subject, tenant, resource, and policy version; otherwise role removal can
serve a stale allow decision.

## EX-06

The conflict is dual authority over a derived representation. Pick one writer,
version derived entries, and reject stale writes or reconcile from authority.
Write-invalidate is usually safer when updates are rare and correctness matters;
write-update can fit read-heavy derived copies when update fanout is bounded.

## EX-07

Use request coalescing and jittered early refresh. Other valid controls include
leases, stale-while-revalidate with bounds, admission control, and prewarming.
Without coalescing, 5,000 clients can cause 5,000 regenerations. Per-key
single-flight targets one regeneration while other callers wait, receive marked
bounded stale data, or fail inside their deadline.

## EX-08

Negative caching is useful when misses are repeated and authoritative data does
not appear immediately. It can hide newly created data if TTLs are too long or
if creation events do not purge the negative entry. Sensitive paths should use a
short TTL, explicit invalidation on create, or bypass for newly written objects.

## EX-09

If the cache key omits subject, tenant, authorization state, or private headers,
one user's representation can be served to another user. Locale, device class,
feature flag, schema version, and content negotiation can also matter for
correctness, though the privacy boundary is usually subject/tenant/auth state.

## EX-10

A strong answer names the authoritative source, key shape, TTL, invalidation
trigger, stampede control, owner, metrics, alarms, rollback, and removal trigger.
It should include numeric evidence such as target hit rate, maximum stale age,
origin request budget, or regeneration concurrency limit.

## EX-11

Good scenarios include synchronized TTL versus jittered TTL, no coalescing versus
single-flight, LRU under a scan versus scan-resistant admission, and shared-key
private leak versus subject-aware keys. Useful emitted fields include origin
regeneration count, expiry distribution, hit rate by workload class, stale age,
and cross-principal response detection.
Each scenario should have a broken and repaired variant whose input workload is
the same, so the emitted field proves the mechanism rather than a different
traffic mix.
