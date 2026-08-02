lesson_id: L03

# TCP Ordering, Flow, Congestion, and Goodput

## Outcomes

- Explain TCP's reliable ordered byte stream without claiming message boundaries.
- Distinguish receiver flow control from path congestion control.
- Calculate and interpret useful goodput under loss and slow readers.

## Prerequisites

Lessons 1–2 and Module 2 queue/utilization reasoning.

## Mechanism and method

TCP establishes shared connection state, numbers bytes, acknowledges progress,
and retransmits missing data. Applications receive an ordered byte stream: one
missing segment can delay delivery of later bytes even if they arrived.

Flow control protects receiver capacity through an advertised receive window.
Congestion control protects the path by adapting the sender's in-flight data.
Both can slow a sender, but evidence and ownership differ. A slow reader can
shrink effective receive capacity; congestion loss can shrink sending rate.

The application/kernel boundary matters. A successful `send` or buffered write
usually means bytes were accepted into the local socket send buffer, not that a
peer received or processed them. The kernel segments, queues, transmits,
retransmits, and retains data until acknowledgment. At the receiver, the kernel
can acknowledge bytes into a receive buffer before the application reads them.
When either buffer fills, blocking calls wait and nonblocking calls report
backpressure. File descriptors, event-loop readiness, socket queues, ACK
progress, and application read/write timestamps belong to different owners and
clocks.

Application spans can measure call duration and bytes offered or consumed.
Socket statistics can observe local queue state and transport counters when the
platform exposes them. A packet capture observes packets at one interface. None
alone proves the other boundaries; label “the remote reader stalled” as an
inference until a same-work rerun or peer evidence discriminates it.

`goodput = useful_application_bytes / elapsed_time`

Diagnostic procedure:

1. Preserve sent, useful, retransmitted, and completed byte counts.
2. Record setup separately from data transfer.
3. Align application write/read timestamps with local send/receive queue samples and transport counters.
4. Compare sender progress, receiver consumption, loss events, and in-flight limits.
5. Hold useful work and seed constant for a discriminating rerun.
6. State whether each claim is application-observed, kernel-observed, packet-observed, modeled, or inferred.

## Worked example

Transit models three streams sharing ordered TCP delivery. Losing an early
packet delays later bytes for every application stream carried after the gap.
The lab's real loopback trace cannot inject IP packet loss without privilege, so
it measures wiring and uses a discrete-event model for recovery. The evidence
must never label model output as a packet capture. Its slow-reader case measures
a configured client-consumption hold and connection-retention time; it does not
claim kernel receive-window pressure. A production diagnosis would add socket
queue/counter evidence or retain that mechanism as an explicit hypothesis.

## Common expert mistakes

- Equating socket writes with peer receipt ignores buffering and acknowledgments.
- Calling every throughput drop congestion ignores receiver and application pacing.
- Dividing payload by link rate and calling it latency ignores setup and round trips.
- Comparing changed payloads invalidates goodput conclusions.

## Guided practice

A 120 KiB response completes in 400 ms after retransmitting 12 KiB. Calculate
useful goodput and wire-byte rate. Explain which value supports a user-capacity
decision and what additional evidence locates the loss cause. Add application
call timing, local socket queues/counters, peer consumption, and one controlled
rerun; mark every conclusion as observed or inferred.

## Self-check

1. What semantic does TCP provide to the application?
2. Which control protects a receiver?
3. Why separate setup from transfer?
4. What does a successful socket write prove?

## Explained answers

1. A reliable, ordered, bidirectional byte stream without application message boundaries.
2. Flow control through receive capacity/window; congestion control protects the path.
3. Reuse can remove setup while transfer mechanics stay constant, so combining them hides the changed mechanism.
4. Usually only that the local kernel accepted bytes into its socket state; peer receipt and application processing require other evidence.

## Sources and next work

- RFC 9293, Sections 2.2, 3.5, 3.7, and 3.8: https://www.rfc-editor.org/rfc/rfc9293.html
- Continue with Lesson 4 for trust establishment over the connection.
