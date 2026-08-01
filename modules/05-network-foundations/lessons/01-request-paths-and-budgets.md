lesson_id: L01

# Request Paths, Round Trips, and Byte Budgets

## Outcomes

- Decompose one user operation into observable network phases.
- Calculate lower-bound setup, serialization, and bandwidth-delay-product costs.
- Freeze predictions that a trace can falsify.

## Prerequisites

Module 2 latency distributions and Module 4 controlled-experiment boundaries.

## Mechanism and method

Begin with an operation, client population, and percentile. Draw actors in the
order bytes visit them. Mark which edges can overlap and which require a reply
before the next begins. A round trip is meaningful only with named endpoints:
client-to-resolver RTT is not client-to-edge RTT.

For serial phase estimates:

`T_lower = Σ(RTT_boundary × serial_exchanges) + bytes/bandwidth + fixed_work`

For a path with capacity `C` bytes/s and RTT `R` seconds:

`bandwidth_delay_product = C × R`

This is the volume needed in flight to fill the path, not a promise that TCP or
the application will reach it. Goodput excludes headers, retransmissions, and
discarded work. A p95 journey is not the sum of unrelated p95 phases; preserve
per-request correlation or model dependence explicitly.

Repeatable procedure:

1. Fix operation, client class, warm/cold state, workload, and target percentile.
2. Enumerate resolution, address selection, transport, trust, proxy, app, and dependencies.
3. Count serial exchanges and bytes at each boundary.
4. Calculate setup, serialization, BDP, and application lower bounds with units.
5. Name overlap, caches, reuse, retransmission, and unobserved boundaries.
6. Predict evidence for at least two causes, then freeze before measurement.

## Worked example

Transit Signal's cold 60 ms path has five simplified serial exchanges before a
complete response: DNS, TCP, TLS, edge request/response, and downstream call.
That predicts 300 ms plus work and serialization. A 12 KiB response on a 4
Mbit/s downlink needs about 24.6 ms to serialize. A 30 KiB BDP exceeds the body,
but initial congestion state and headers remain unknown. The correct conclusion
is a bounded prediction, not “cold requests take exactly 325 ms.”

## Common expert mistakes

- Adding marginal percentiles from different requests creates a journey that
  may never have occurred.
- Treating payload bytes as wire bytes hides headers and retransmissions.
- Counting every phase as serial overstates cost when DNS/address attempts or
  proxy work overlap.
- Calling a lower bound an SLO prediction hides queues, loss, and application work.

## Guided practice

For a 100 ms RTT, 10 Mbit/s link, 50 KiB body, and four serial exchanges,
calculate setup lower bound, serialization, and BDP. Then name three reasons the
observed p95 could be higher and one reason it could be lower.

## Self-check

1. Why is BDP not a throughput guarantee?
2. When may two RTT costs overlap?
3. Why can summing phase p95s misstate journey p95?

## Explained answers

1. BDP describes path volume; sender windows, receiver flow control, congestion,
   loss, and application pacing can prevent filling it.
2. Only when the implementation starts independent work concurrently and the
   critical path does not wait for both sequentially.
3. Each phase p95 may come from a different request; dependence and correlation
   determine the journey tail.

## Sources and next work

- RFC 9293, TCP concepts and data communication: https://www.rfc-editor.org/rfc/rfc9293.html
- Continue with Lesson 2 before interpreting a DNS phase.
