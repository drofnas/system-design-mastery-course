# Module 5 Explained Answer Key

These are reasoning checks, not canonical architectures. Alternative answers
are valid when they preserve mechanisms, evidence, and boundaries.

## EX-01: Cold path budget

The simplified case counts DNS, TCP, TLS, edge request/response, and dependency
as five serial 60 ms exchanges: 300 ms. Serialization is about 24.6 ms and BDP
is 30,000 bytes. A strong answer states that application work, headers,
congestion state, loss, overlap, and reuse can move the observation.

## EX-02: Journey percentile

Marginal p95 phases can represent different requests and dependence. Carry one
request identity across phases, compute each request's end-to-end time, then take
the journey percentile. Retain phase values for the same selected requests.

## EX-03: DNS response classes

Positive returns typed data but no health proof. NXDOMAIN states name
nonexistence; NODATA states the name lacks that type. SERVFAIL and timeout are
temporary uncertainty. Record authority, TTL/cache, attempt, and time; bound
fallback/retry rather than rewriting temporary failures as absence.

## EX-04: Discovery ownership

A defensible map assigns record/zone to DNS platform, recursive behavior to
resolver operator, routing and edge health to network/edge, service discovery to
platform/application owners, and certificate/key policy to security plus edge.
Escalation cites the first failed boundary rather than “network issue.”

## EX-05: Flow versus congestion

Slow reader evidence includes delayed consumption and send-buffer/receive-window
pressure. Congestion evidence includes path loss/recovery and reduced in-flight
progress. Application pacing shows idle sender intervals without either
constraint. Change one reader/path/application control at a time.

## EX-06: Equivalent goodput

Useful goodput is `120 KiB / 0.4 s = 300 KiB/s`. Wire-byte rate is
`132 KiB / 0.4 s = 330 KiB/s`. Useful goodput supports completed user capacity;
wire rate helps explain path cost. Both require equal result checks.

## EX-07: Trust rejection

Expected name plus trusted anchor succeeds. Wrong name fails identity matching;
missing anchor fails chain trust; expiry fails validity. The safe client does not
silently disable verification or downgrade. Owners fix certificate/DNS/time
configuration at the failed boundary.

## EX-08: Pool capacity

Little's Law predicts `800/s × 0.08 s = 64` average active connections. A 2×
burst target suggests 128, but a complete answer tests distributions, dependency
capacity, memory/descriptors, NAT/load-balancer limits, wait budget, and bounded rejection.

## EX-09: Slow reader versus slow dependency

Increase only client read rate: receiver-driven hold time should fall while
dependency phase stays stable. Then hold reader constant and vary dependency
delay: dependency phase should move while client consumption rate stays stable.
Preserve request bytes and checksum.

## EX-10: HTTP/2 loss boundary

Frames may arrive at the host out of order, but TCP cannot deliver later bytes
past the missing sequence gap. Because all streams share that byte stream,
otherwise independent later frames wait. The answer must distinguish arrival
from application delivery.

## EX-11: QUIC stream isolation

A missing frame on stream A delays ordered delivery for A, not already received
data on B or C. A connection-wide congestion response can still reduce sending
for all streams. Isolation changes ordering, not total path capacity or loss.

## EX-12: Blind fault diagnosis

A valid answer cites raw fields, keeps observation separate from mechanism,
ranks a credible alternative, and changes one causal variable with equal work.
Naming the hidden scenario or reading its source before freeze invalidates the exercise.

## EX-13: Evidence classification

Loopback timing is measured within its process/host boundary. Simulator events
are modeled. RFC behavior is standards-derived. Mobile p95 is untested until
production-like client/path evidence exists. Combining categories without labels
overstates transfer.

## EX-14: Protocol decision

A strong comparison uses identical operations and client/path distributions.
HTTP/1.1 trades more connections for isolation and compatibility; HTTP/2 reduces
setup/connection count but shares TCP ordering; HTTP/3 changes stream recovery
and deployment/observability. No option wins without reachability, cost,
fallback, security, ownership, and evidence thresholds.

## EX-15: Migration defense

Begin only after fallback capacity and observability pass. Expose a bounded
supported mobile cohort; succeed on user p95, error, fallback, CPU/memory, and
cost thresholds; stop or remove advertisement when thresholds fail. Decommission
old support only after client use and rollback windows meet published evidence.

## PESD 2.0 extension answer

A defensible answer covers workload identity, egress policy, residency-aware routing, encrypted naming implications, and a network certificate and algorithm inventory. It distinguishes the
requirement, enforcement mechanism, evidence, and owner; keeps modeled and
measured results separate; and names the failed condition that would reverse
the decision. Different architectures are acceptable when their invariants,
evidence boundaries, migration, and residual risk are explicit.
