---
lesson_id: L06
title: "HTTP/1.1 and HTTP/2 Multiplexing"
---

# HTTP/1.1 and HTTP/2 Multiplexing

## Outcomes

- Compare connection reuse, pipelining constraints, and multiplexed streams.
- Locate connection-level and stream-level flow/ordering boundaries.
- Avoid claiming that HTTP/2 removes TCP head-of-line blocking.

## Prerequisites

Lessons 3 and 5.

## Mechanism and method

HTTP/1.1 commonly uses multiple reusable TCP connections because one connection
cannot freely interleave arbitrary response bytes. HTTP/2 frames messages into
streams on one connection and allows application-layer multiplexing. Each stream
has flow control, and the connection also has flow control. But all frames still
ride one ordered TCP byte stream. A missing TCP segment can therefore withhold
later bytes belonging to otherwise independent HTTP/2 streams.

Comparison procedure:

1. Fix request count, body sizes, dependency work, connections, and client path.
2. Count cold and warm setup separately.
3. Model application scheduling, stream limits, and connection-level ordering.
4. Inject one early loss and record which completions move.
5. Include proxy support, observability, failure radius, memory, and fallback.

## Worked example

Transit requests route impact, alerts, and accessibility data concurrently. In
the HTTP/1.1 model, three connections pay more setup but isolate transport loss.
In HTTP/2, one connection saves setup and multiplexes requests, but one missing
early TCP packet delays delivery of later frames on all streams. This is a
mechanism comparison, not a prediction that three connections always win.

## Common expert mistakes

- “Multiplexed” does not mean independent at every lower layer.
- Comparing one cold HTTP/1.1 connection with one warm HTTP/2 connection changes two variables.
- Treating maximum concurrent streams as free ignores memory and dependency concurrency.
- Ignoring client/proxy downgrade behavior creates an incomplete topology.

## Guided practice

Draw three requests under six warm HTTP/1.1 connections and one warm HTTP/2
connection. Lose a byte before response two. Mark which application responses
can be delivered and which evidence would falsify your model.

## Self-check

1. What blocking does HTTP/2 remove?
2. What blocking remains?
3. Why include connection count in the comparison?

## Explained answers

1. It removes HTTP/1.1 application serialization by interleaving frames from independent streams.
2. TCP provides one ordered byte stream, so missing bytes can delay all later frame delivery.
3. Connection count changes setup, congestion state, isolation, sockets, NAT state, and fairness.

## Sources and next work

- RFC 9113, HTTP/2: https://www.rfc-editor.org/rfc/rfc9113.html
- Continue with Lesson 7 for QUIC's different ordering boundary.
