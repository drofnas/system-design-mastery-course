---
lesson_id: L02
title: "DNS, Addressing, Routing, and Discovery"
---

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
selection first produces candidates (often A and AAAA records), then applies a
client policy to choose destination and compatible source addresses. A client
may race IPv6 and IPv4 attempts, so the first DNS answer shown in a tool is not
necessarily the address used by the successful socket.

Routing is a separate lookup. The host chooses the most-specific matching
prefix, then policy/metric, next hop, and interface. Routers repeat a forwarding
decision at each hop; equal-cost paths and return-path policy can make two
requests asymmetric. A route entry proves only a forwarding choice, not that a
neighbor, firewall, load balancer, or process will accept the request. Proxies
and service discovery may add another name-to-endpoint and route decision.
Cache layers can have different remaining TTLs.

Decision procedure:

1. List stub, recursive, authoritative, service-discovery, and application caches.
2. Record query name/type, response class, authority, TTL, and observation time.
3. Enumerate candidate destination/source address pairs and record the client's selection order.
4. For the chosen address, record longest-prefix match, next hop, interface, policy/metric, and observed socket peer.
5. Separate no-name, no-type, temporary failure, no compatible address, no route, filtered route, and unhealthy service.
6. Define retry/fallback bounds and prevent synchronized requery storms.
7. Assign record, resolver, address-policy, route, firewall, and endpoint owners.

## Worked example

Transit's local UDP stub returns `127.0.0.1` for `impact.transit.test` with a
bounded TTL. A DNS-failure scenario returns a temporary failure and the client
does not attempt TCP. That proves request gating and evidence shape only. It does
not reproduce recursive referral behavior or validate public DNS availability.
For a production mobile client, the prediction must additionally list the AAAA
and A candidates, selected source/destination pair, and route/interface used. A
successful IPv4 loopback connection cannot support an IPv6, carrier-routing,
firewall, or asymmetric-return-path claim.

## Common expert mistakes

- “DNS is down” collapses authoritative, recursive, network, validation, and cache failures.
- Infinite retry on timeout multiplies resolver load during failure.
- Using a stale address without a stated policy can route to decommissioned or unsafe infrastructure.
- Logging full queried names can expose tenant or user data.

## Guided practice

Draw the response path for a cached A record that expires during an authoritative
timeout. Specify what evidence distinguishes stale-answer service, immediate
failure, and repeated upstream queries. Then add an AAAA candidate and `/48`
plus default routes; apply longest-prefix match and name the observation that
proves the address and route the client actually used.

## Self-check

1. What does a successful DNS answer not prove?
2. How does NXDOMAIN differ from a timeout?
3. Why name the cache layer when reporting TTL?
4. Why does a route-table match not prove endpoint reachability?

## Explained answers

1. It does not prove route reachability, TLS identity, proxy capacity, or service health.
2. NXDOMAIN is an authoritative nonexistence result; timeout lacks a response and is temporary uncertainty.
3. Stub, recursive, and application caches can observe different insertion times and remaining lifetimes.
4. It selects a forwarding path only; neighbor reachability, filtering, downstream routing, and service admission remain separate mechanisms.

## Sources and next work

- RFC 1034, concepts and server algorithm: https://datatracker.ietf.org/doc/html/rfc1034
- RFC 6724, default address-selection policy: https://www.rfc-editor.org/rfc/rfc6724.html
- RFC 8305, connection racing across address families: https://www.rfc-editor.org/rfc/rfc8305.html
- RFC 1812, longest-prefix forwarding behavior: https://www.rfc-editor.org/rfc/rfc1812.html
- RFC 9520, negative caching of resolution failures: https://datatracker.ietf.org/doc/rfc9520/
- Continue with Lesson 3 to interpret connection evidence after resolution.
