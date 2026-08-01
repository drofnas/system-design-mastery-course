lesson_id: L02

# DNS, Addressing, Routing, and Discovery

## Outcomes

- Distinguish names, cached records, addresses, routes, and healthy endpoints.
- Model positive, negative, timeout, expiry, and stale-answer behavior.
- Assign ownership and safe fallback at each discovery boundary.

## Prerequisites

Lesson 1 path boundaries and basic IP addressing.

## Mechanism and method

A stub resolver asks a recursive resolver. The recursive resolver may answer
from cache or follow referrals toward an authoritative server. A positive answer
maps a name and record type to data for a TTL. NXDOMAIN means the queried name
does not exist under the authority's response; NODATA means the name exists but
not the requested type. A timeout or SERVFAIL is temporary and must not be
silently rewritten as nonexistence.

An address is still not a route, and a route is not a healthy process. Address
selection may race IPv6 and IPv4. Proxies and service discovery may add another
name-to-endpoint step. Cache layers can have different remaining TTLs.

Decision procedure:

1. List stub, recursive, authoritative, service-discovery, and application caches.
2. Record query name/type, response class, authority, TTL, and observation time.
3. Separate no-name, no-type, temporary failure, unreachable address, and unhealthy service.
4. Define retry/fallback bounds and prevent synchronized requery storms.
5. Assign record, resolver, client, route, and endpoint owners.

## Worked example

Transit's local UDP stub returns `127.0.0.1` for `impact.transit.test` with a
bounded TTL. A DNS-failure scenario returns a temporary failure and the client
does not attempt TCP. That proves request gating and evidence shape only. It does
not reproduce recursive referral behavior or validate public DNS availability.

## Common expert mistakes

- “DNS is down” collapses authoritative, recursive, network, validation, and cache failures.
- Infinite retry on timeout multiplies resolver load during failure.
- Using a stale address without a stated policy can route to decommissioned or unsafe infrastructure.
- Logging full queried names can expose tenant or user data.

## Guided practice

Draw the response path for a cached A record that expires during an authoritative
timeout. Specify what evidence distinguishes stale-answer service, immediate
failure, and repeated upstream queries.

## Self-check

1. What does a successful DNS answer not prove?
2. How does NXDOMAIN differ from a timeout?
3. Why name the cache layer when reporting TTL?

## Explained answers

1. It does not prove route reachability, TLS identity, proxy capacity, or service health.
2. NXDOMAIN is an authoritative nonexistence result; timeout lacks a response and is temporary uncertainty.
3. Stub, recursive, and application caches can observe different insertion times and remaining lifetimes.

## Sources and next work

- RFC 1034, concepts and server algorithm: https://datatracker.ietf.org/doc/html/rfc1034
- RFC 9520, negative caching of resolution failures: https://datatracker.ietf.org/doc/rfc9520/
- Continue with Lesson 3 to interpret connection evidence after resolution.
