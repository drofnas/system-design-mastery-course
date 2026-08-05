# Module 19 Glossary

- **Cache-aside**: Application reads through a cache miss by loading from the authoritative store and writing the cache.
- **Coherence**: Agreement rules for cached copies across locations.
- **Eviction**: Removing cache entries to stay within capacity.
- **Invalidation**: Removing or marking cached data stale after authoritative change.
- **Stampede**: Many clients regenerate the same expired or missing item at once.
- **TTL**: Time-to-live, the duration a cached item may be served before refresh or expiry.
