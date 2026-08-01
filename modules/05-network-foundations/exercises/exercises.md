# Module 5 Guided Exercises

Complete these against Transit Signal before opening the answer key. The
commerce journey remains independent graded work.

## EX-01: Cold path budget

Using the Transit inputs, enumerate serial exchanges and calculate lower-bound
setup, 12 KiB serialization, and BDP. Label assumptions and units.

## EX-02: Journey percentile

Explain why DNS p95 + TLS p95 + application p95 is not necessarily journey p95.
Design a correlated per-request measurement.

## EX-03: DNS response classes

For positive A, NXDOMAIN, NODATA, SERVFAIL, and timeout, state what is known,
what remains unknown, cache behavior to record, and safe next action.

## EX-04: Discovery ownership

Map Transit DNS record, recursive resolver, route, edge health, service
discovery, and certificate to owners and escalation evidence.

## EX-05: Flow versus congestion

Given falling sender goodput, design evidence that distinguishes a slow reader,
path congestion, and application pacing.

## EX-06: Equivalent goodput

Compute useful and wire-byte rates for 120 KiB useful bytes, 12 KiB
retransmission, and 400 ms completion. State which supports user capacity.

## EX-07: Trust rejection

Specify success, wrong-hostname, missing-anchor, and expired-certificate tests.
Name the property and expected client behavior for each.

## EX-08: Pool capacity

At 800 completions/s and 80 ms mean connection hold time, estimate average
active connections. Propose bounded burst headroom and rejection evidence.

## EX-09: Slow reader versus slow dependency

Design one rerun that changes reader consumption without changing dependency
work and one that changes dependency delay without changing reader behavior.

## EX-10: HTTP/2 loss boundary

Draw three streams on one TCP connection. Lose an early byte and show which
later frames can arrive versus which can be delivered to applications.

## EX-11: QUIC stream isolation

Repeat EX-10 with per-stream ordering. Add connection-wide congestion reduction
and distinguish delivery isolation from capacity sharing.

## EX-12: Blind fault diagnosis

For one unknown bundle, cite three exact observations, rank two mechanisms, and
design a same-work rerun that separates them before reveal.

## EX-13: Evidence classification

Classify DNS/TLS loopback timing, simulator loss events, RFC behavior, and a
mobile-production p95 claim as measured, modeled, standards-derived, or untested.

## EX-14: Protocol decision

Compare pooled HTTP/1.1, HTTP/2, and HTTP/3 with fallback for Transit using the
same client, workload, security, cost, ownership, and migration drivers.

## EX-15: Migration defense

Write entry, success, stop, rollback, and decommission conditions for a staged
mobile HTTP/3 canary while retaining safe HTTP/2 capacity.
