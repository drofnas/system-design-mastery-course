# Module 19 Glossary

- **Cache:** derived copy used to reduce latency, cost, or load.
- **Authoritative source:** the system of record that determines whether cached
  data is correct.
- **Cache-aside:** application-owned miss handling: read authority, then populate
  the cache.
- **Read-through:** cache abstraction owns the miss path and loads from authority.
- **Write-through:** writes update cache and authority synchronously.
- **Write-around:** writes skip the cache and let later reads repopulate it.
- **Write-back/write-behind:** writes are accepted into a cache or buffer and
  propagated later, requiring durability and reconciliation.
- **TTL:** time-to-live, a maximum age after which an entry expires.
- **TTL jitter:** randomized expiry variation that prevents synchronized misses.
- **Invalidation:** marking cached data stale after authority changes.
- **Coherence:** rule for how multiple cached copies converge.
- **Versioned key:** cache key containing a version so new authoritative writes
  naturally bypass old entries.
- **Negative caching:** caching absence, such as a not-found result.
- **Eviction:** removing an entry because capacity or policy requires it.
- **LRU:** least-recently-used eviction, based on recency.
- **LFU:** least-frequently-used eviction, based on observed frequency.
- **Scan resistance:** protection against one-time scans evicting the hot set.
- **Working set:** items repeatedly accessed within the cache's useful window.
- **Stampede:** many callers regenerating the same expired item.
- **Single-flight:** one regeneration owner with coalesced waiters.
- **Lease:** temporary ownership of regeneration for one key.
- **Stale-while-revalidate:** serving marked bounded stale data while a refresh
  runs.
- **Cache poisoning:** storing an incorrect or malicious representation.
- **Private cache leak:** serving one principal's representation to another
  because the key omitted an authorization dimension.
- **Origin load:** requests or regeneration work that reaches the authoritative
  backing service after cache hits are removed.
- **Regeneration:** rebuilding a cached representation from authority or an
  expensive derived computation.
- **Prewarming:** filling cache entries before serving traffic so cold start does
  not send all reads to origin at once.
- **Removal condition:** the evidence threshold that says the cache is no longer
  worth its correctness, invalidation, and operational cost.
