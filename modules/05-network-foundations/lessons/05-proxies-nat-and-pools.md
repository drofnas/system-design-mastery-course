---
lesson_id: L05
title: "Proxies, NAT, Pooling, and Exhaustion"
---

# Proxies, NAT, Pooling, and Exhaustion

## Outcomes

- Trace connection ownership across client, proxy, application, and dependency.
- Calculate pool capacity and diagnose wait, rejection, and slow-reader retention.
- Include NAT, load-balancer, security, cost, and operational boundaries.

## Prerequisites

Lessons 1–4 and Module 2 bounded-concurrency reasoning.

## Mechanism and method

A proxy creates at least two transport relationships. Client connections and
upstream connections can have different lifetimes, identities, limits, and TLS
boundaries. A pool replaces repeated setup with retained scarce state. At limit,
work must wait, reject, or use a bounded fallback.

For average held connections, Little's Law still applies:

`connections ≈ completion_rate × connection_hold_time`

NAT and load balancers retain mappings with timeouts outside application
ownership. Reuse can cross a route or certificate change unless lifetime and
drain behavior are explicit.

Diagnostic procedure:

1. Draw each connection separately and name its owner/security boundary.
2. Measure active, idle, peak, wait, rejection, reuse, and cleanup.
3. Compare arrival rate × hold time with pool/NAT limits.
4. Inject slow readers and pool exhaustion independently.
5. Define admission, timeout, drain, rotation, and rollback behavior.

## Worked example

Transit's edge admits at most four modeled upstream connections. Five concurrent
slow consumers cause one bounded pool wait or rejection rather than unbounded
socket growth. The useful response checksum remains equal for completions. A
rerun increasing reader rate separates receiver retention from dependency delay.

## Common expert mistakes

- Counting requests but not held connections misses slow-reader capacity.
- One “connection count” metric mixes client and upstream ownership.
- Unlimited pools move overload to file descriptors, NAT state, or dependencies.
- Rotating a certificate without draining retained connections can preserve old state longer than expected.

## Guided practice

At 800 completions/s and 80 ms mean hold time, estimate average active
connections. Then size 2× burst headroom and explain why that is not a complete
pool decision.

## Self-check

1. Why can a small response exhaust a pool?
2. What does connection reuse trade?
3. Which evidence distinguishes dependency delay from pool wait?

## Explained answers

1. A receiver can retain the connection while consuming slowly, so size alone does not determine hold time.
2. It saves setup but retains state, identity, routing, memory, and failure history.
3. Separate acquisition wait from service timing with active/peak pool counters and dependency spans.

## Sources and next work

- RFC 9293 keep-alive and connection behavior: https://www.rfc-editor.org/rfc/rfc9293.html
- Continue with Lesson 6 to compare request concurrency over connections.
