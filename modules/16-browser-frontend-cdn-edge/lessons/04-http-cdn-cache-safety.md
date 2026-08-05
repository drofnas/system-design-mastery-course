---
lesson_id: L04
title: "HTTP and CDN Cache Safety"
---

# HTTP and CDN Cache Safety

## Outcomes

- Derive storage, key, freshness, validation, and invalidation from data authority.
- Prove that shared reuse cannot cross representation or subject boundaries.
- Design bounded stale-on-error behavior that fails closed for private routes.

## Prerequisites

Use Module 5 HTTP, Module 9 consistency, Module 12 degraded operation, Module 13
authorization/privacy, and Module 14 migration/reversal reasoning.

## Mechanism: a cache reuses a representation under a declared equivalence

A cache key states which requests are equivalent for reuse. A freshness policy
states how long the cache may act without consulting authority. Validation asks
whether the stored representation remains current. Invalidation attempts to
shorten exposure after a change; it does not erase clients that already received data.

Create a **cache safety proof** for each route:

1. Name the authoritative object and monotonically identifiable content version.
2. Classify the response as public, representation-varying, or subject-private.
3. Normalize every representation dimension into the URL or cache key: method,
   host, path, selected query, locale/encoding, and any approved public variant.
4. Bypass shared storage for authenticated or subject-bound responses; use
   `private, no-store` when storage is unsafe.
5. Set browser/shared freshness separately where needed. Record who owns expiry.
6. Define validation (`ETag`/version) and purge or versioned-URL behavior.
7. For stale-on-error, name maximum age, eligible public routes, degraded marker,
   and the faults that must fail closed.
8. Test two distinct public representations and two pseudonymous subjects.

Do not put raw session identifiers into a shared cache key to “make it private.”
That creates an unbounded, sensitive key space and still relies on a shared system
to enforce subject isolation. Permission must be checked at authority; private
content should bypass shared reuse.

## Worked example

Northstar keys public event pages by normalized path, event content version, and
supported language. Region-specific viewing advice uses a region path segment,
not an unbounded location header. `/staff/schedule` is never stored by the edge.

F05 omits language from the public key. An English request populates the cache;
a Spanish request receives the English representation. The response is public,
so no private data leaks, but the representation contract fails. The repair adds
the bounded language dimension and proves both keys and content versions.

F06 is a different failure: the edge ignores `private, no-store` and stores a
staff schedule. A second pseudonymous session receives the first subject's HTML.
The repaired path bypasses lookup and storage for the private route, strips no
protective origin headers, and asserts zero shared-cache entries for both sessions.

During origin failure, Northstar may serve a public event description for at most
ten minutes beyond freshness with an explicit degraded timestamp. It never serves
a stale staff schedule or current safety status from shared storage.

## Common expert mistakes

- **Keying only by path.** Query, locale, encoding, method, or public variant may
  change the representation.
- **Using TTL as deletion.** Expiry bounds future reuse by a cache; it does not
  retract previously delivered or independently stored data.
- **Caching authorization results.** Possession of a cached response is not proof
  that the current subject may receive it.
- **Treating purge as instantaneous truth.** Multi-layer invalidation has delay,
  partial failure, retries, and observability requirements.
- **Serving stale everywhere during incidents.** Availability cannot override
  private authority, revoked data, or safety-critical freshness.

## Guided practice

Write the storage/key/freshness/validation/failure policy for all four Northstar
routes. Construct requests that differ by language, ignored tracking query,
content version, and subject. Predict the cache result before running F05–F07.

## Self-check

1. Why is `Vary: Cookie` usually a poor private-content strategy?
2. What does an ETag prove?
3. When may stale-on-error be safe?
4. Why are purge logs insufficient evidence?

## Explained answers

1. Cookies are high-cardinality and sensitive, and a shared cache remains the
   wrong authority for subject access; bypass shared storage instead.
2. It identifies a selected representation for validation under its scope; it
   does not prove authorization or universal semantic freshness.
3. For named public data whose authority permits bounded staleness, with age,
   degraded presentation, monitoring, and a fail-closed exclusion list.
4. A request log proves an attempt, not propagation to every layer or absence of
   stale objects; probe the affected keys and versions.

## Sources and next work

Study RES-04. Complete EX-08–EX-10 and freeze cache-key and stale-data predictions
before opening the completed Northstar policy.
