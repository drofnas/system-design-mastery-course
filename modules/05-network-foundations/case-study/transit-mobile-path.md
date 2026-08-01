# Transit Signal Mobile Route-Impact Journey

## Problem statement

Transit Signal serves a small route-impact response to riders opening a mobile
app. Clients include regional fiber, congested commuter Wi-Fi, and mobile links
with changing addresses. The request resolves `impact.transit.test`, reaches an
edge proxy, calls a route-impact application, and queries a schedule dependency.
The response is useful only when its route identifier and version checksum agree.

The team currently says the endpoint is “fast because the JSON is small.” That
claim ignores cold DNS, connection setup, encryption, downstream work, loss,
receiver speed, and connection reuse.

## Initial workload and constraints

- 70% warm mobile sessions, 20% cold mobile sessions, 10% station kiosks
- 12 KiB useful response plus 800 B request headers and body
- warm p95 target: 250 ms; cold p95 target: 600 ms
- modeled path: 60 ms RTT, 4 Mbit/s downlink, 1 Mbit/s uplink
- burst: 600 requests/s; each edge worker may hold 64 upstream connections
- certificates terminate at the edge; proxy-to-application traffic remains on a
  loopback teaching boundary, not a claim about production security
- DNS and certificate ownership belong to different teams

## Worked path prediction

For a cold TCP/TLS request with no overlapping work, the first useful byte has
at least a DNS exchange, TCP establishment, TLS 1.3 handshake, request/response
exchange, and downstream exchange. With the simplified 60 ms RTT boundary, five
serial exchanges consume about 300 ms before serialization and application
work. The arithmetic is a prediction, not a protocol guarantee: caching,
resumption, parallel address attempts, proxy reuse, and packet loss change it.

The 4 Mbit/s downlink serializes 12 KiB in roughly 24.6 ms:

`12 × 1024 × 8 / 4,000,000 = 0.024576 seconds`

The bandwidth-delay product is about 30 KiB:

`4,000,000 bits/s × 0.060 s / 8 = 30,000 bytes`

The response fits below that modeled product, but that does not guarantee one
RTT completion because congestion window, headers, application pacing, and the
receiver remain outside this calculation.

## Layer and owner table

| Boundary | Mechanism | Evidence | Owner | Failure example |
|---|---|---|---|---|
| name to address | recursive DNS and cache | response class, TTL, attempts | platform DNS | timeout or negative answer |
| client to edge | TCP or QUIC | setup and stream events | client/edge | loss or reset |
| peer identity | TLS | certificate and hostname result | security/edge | untrusted certificate |
| edge to app | proxy and pool | wait, active, reuse | edge platform | pool exhaustion |
| app to schedule | dependency call | phase timing and checksum | schedule team | delay or failure |

## Failed approaches

1. **“Use HTTP/3 because it is newer.”** This ignores client support, UDP
   reachability, fallback, load balancing, observability, cost, and whether loss
   affects the journey enough to repay migration risk.
2. **“DNS succeeded, so the service is healthy.”** DNS returns naming data; it
   does not prove routing, certificate validity, proxy capacity, or application
   health.
3. **“The response is small, so bandwidth cannot matter.”** A slow reader can
   retain buffers and connections even when serialization time is modest.
4. **“One loopback result predicts mobile production.”** Loopback proves wiring,
   trust handling, and cleanup. The simulator teaches causal comparisons. Neither
   measures a carrier network.

## Completed Transit decision boundary

Transit Signal keeps the measured TLS loopback path as evidence of phase
instrumentation and uses the deterministic model only to compare mechanisms.
The team will not claim a universal HTTP/3 win. A production recommendation
would require client-population telemetry, UDP reachability, fallback success,
regional loss/RTT distributions, load-balancer support, cost, and rollback
evidence.

Alternative answers remain valid. A kiosk-only population may favor stable
pooled HTTP/2; a lossy mobile population may justify an HTTP/3 trial. The method
requires shared drivers, bounded evidence, and reversal conditions rather than
one canonical protocol.
