# Module 19 Resources

### RES-01 Caching at Scale With Redis

- URL: https://redis.io/learn/howtos/solutions/microservices/caching-at-scale
- Use for: cache placement and operational strategy.
- Local alternative: L01.
- Boundary: use for placement vocabulary; local lessons define the course's
  authority, key-shape, and rollback expectations.

### RES-02 Cloudflare Cache Concepts

- URL: https://developers.cloudflare.com/cache/concepts/default-cache-behavior/
- Use for: HTTP caching, cache keys, and freshness.
- Local alternative: L03 and M16.

### RES-03 Caching Strategies and How to Choose the Right One

- URL: https://aws.amazon.com/caching/best-practices/
- Use for: cache-aside, write-through, write-around, and write-behind tradeoffs.
- Local alternative: L01.

### RES-04 Cache Stampede

- URL: https://en.wikipedia.org/wiki/Cache_stampede
- Use for: a compact definition of stampede behavior before local modeling.
- Local alternative: L04.

### RES-05 HTTP Caching

- URL: https://www.rfc-editor.org/rfc/rfc9111.html
- Use for: HTTP cache semantics, freshness, validation, and shared-cache behavior.
- Local alternative: L03 and M16 L04.
- Boundary: apply HTTP-specific semantics only where an HTTP cache is actually
  in the path; use local lessons for general cache policy.

### RES-06 TinyLFU: A Highly Efficient Cache Admission Policy

- URL: https://arxiv.org/abs/1512.00727
- Use for: modern admission policy and scan-resistant cache economics.
- Local alternative: L02.
- Boundary: use for admission-policy mechanism; validate any production choice
  against your own workload trace.

### RES-07 S3-FIFO cache eviction

- URL: https://s3fifo.com/
- Use for: modern FIFO-family scan-resistant eviction design.
- Local alternative: L02.
- Boundary: use as an eviction-design reference, not as a universal replacement
  for measuring hit rate, miss cost, and correctness risk.
