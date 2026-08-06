---
lesson_id: L07
title: "QUIC and HTTP/3 Stream Behavior"
---

# QUIC and HTTP/3 Stream Behavior

## Outcomes

- Explain QUIC connection, packet-number-space, and stream recovery boundaries.
- Compare loss effects with HTTP/2 over TCP without claiming loss disappears.
- State deployment, security, migration, and model limitations.

## Prerequisites

Lessons 3, 4, and 6.

## Mechanism and method

QUIC runs over UDP but implements authenticated connection state, congestion
control, loss recovery, flow control, and multiple ordered streams in user
space. Ordering is per stream: a missing frame on stream A need not prevent
delivery of already received data on stream B. Congestion control remains
connection-scoped, so streams still compete for path capacity. HTTP/3 maps HTTP
semantics onto QUIC streams.

QUIC does not eliminate loss, congestion, handshake security, or operational
work. UDP blocking, load balancer routing, connection IDs, migration, encrypted
transport metadata, library maturity, and fallback affect deployment.

Comparison procedure:

1. Hold path, bytes, stream schedule, congestion rule, and loss event constant.
2. Change only ordered-delivery boundary: shared TCP bytes versus per-stream QUIC bytes.
3. Record each stream completion and overall goodput.
4. Classify modeled behavior separately from real interoperability evidence.
5. Add reachability, fallback, routing, debugging, and rollback requirements.

## Worked example

Transit's deterministic simulation loses an early packet for stream A. The
HTTP/2-over-TCP mode delays later frames for A, B, and C until shared ordering
recovers. The QUIC-style mode delays A while B and C can complete if their data
arrived. Both modes pay the same configured recovery delay and capacity, so the
experiment isolates ordering rather than asserting a complete protocol benchmark.

## Common expert mistakes

- “QUIC fixes packet loss” confuses isolation with loss removal.
- A loopback QUIC demo says little about carrier UDP reachability or regional benefit.
- 0-RTT is not universally safe for side-effecting operations because replay matters.
- Encrypted transport metadata changes debugging and load-balancing tools.

## Guided practice

Given three streams and loss on stream A, predict completion under shared
ordering and per-stream ordering. Then add a connection-wide congestion window
reduction and explain why all streams may still slow.

## Self-check

1. What ordering boundary changes from HTTP/2/TCP to QUIC?
2. What capacity mechanism remains shared?
3. Why is UDP reachability part of the decision?

## Explained answers

1. TCP orders all connection bytes; QUIC orders data within each stream.
2. Connection/path congestion control and total link capacity remain shared.
3. Some networks block or degrade UDP, so a deployable HTTP/3 design needs fallback and measured reachability.

## Sources and next work

- RFC 9000, QUIC: RES-05
- RFC 9114, HTTP/3: RES-13
- Continue with Lesson 8 to turn mechanics into a migration decision.
