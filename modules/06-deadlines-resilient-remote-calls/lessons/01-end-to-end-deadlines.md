---
lesson_id: L01
title: End-to-End Deadlines and Allocation
---

# End-to-End Deadlines and Allocation

## Outcomes

- Distinguish a user usefulness deadline from local timeout durations.
- Allocate serial, parallel, queue, network, response, and cleanup budgets.
- Propagate remaining time without resetting the parent promise.

## Prerequisites

Little's Law, percentile distributions, the Module 5 request path, and the
ability to label assumptions separately from observations.

## Mechanism

A deadline answers “after what instant is this result no longer useful?” A
timeout answers “how long will this component wait?” Resetting a full timeout at
each hop lets a request live longer than the user promise. Instead carry one
absolute logical deadline, convert it to a local remaining duration at each
boundary, subtract explicit response/cleanup reserve, and refuse work that
cannot plausibly finish.

For serial stages, a first allocation is:

`D_user >= Q_ingress + L_local + sum(C_i) + A_response + R_cleanup`

For parallel children, use the maximum completion time of required children,
not their sum, but count every child against concurrency and cost. If stage `i`
starts at `t_i`, the allowed child duration is:

`child_i = min(operation_cap_i, D_absolute - t_i - response_reserve)`

Percentile allocations are not additive guarantees. Correlation, queueing, and
fan-out change the journey tail, so freeze a prediction and validate the whole
journey under its workload.

## Decision procedure

1. Name the user outcome, population, percentile, and usefulness boundary.
2. Draw every serial stage and parallel fan-out edge, including queues.
3. Reserve response assembly, delivery, and cancellation cleanup first.
4. Allocate operation caps from measured distributions and criticality.
5. Define insufficient-budget behavior before dispatch.
6. Record remaining time at admission, dispatch, completion, and cancellation.
7. Test low/base/high latency and burst sensitivity against the journey result.

## Worked example

Beacon has 420 ms from ingress. It reserves 60 ms for delivery/cleanup and 40 ms
for assembly. Admission consumes 20 ms, leaving 300 ms. Unit, road, and weather
start in parallel; required unit/road have a 260 ms stage cap while optional
weather has 180 ms. The parallel stage consumes at most 260 ms, not 700 ms, but
it creates three attempts. A child dispatched 75 ms after ingress receives at
most `420 - 75 - 60 = 285 ms`, further limited by its operation cap.

## Common expert mistakes

- **Resetting 300 ms at each hop:** nested calls outlive the 420 ms promise.
- **Adding parallel budgets:** overstates latency while hiding resource cost.
- **Using mean latency:** misses the stuck minority that occupies all slots.
- **Giving every child the parent deadline:** leaves no time to assemble or cancel.
- **Treating a deadline as proof of interruption:** the caller may stop while the server continues.

## Guided practice

For a 600 ms incident journey, reserve 80 ms response/cleanup and 30 ms local
validation. Required children A and B start after a 25 ms queue; optional C may
use 200 ms. Calculate the largest shared required-stage cap and the remaining
duration seen by a child dispatched 140 ms after ingress. Then define behavior
when only 45 ms remains but the child's measured minimum useful duration is 70 ms.

## Self-check

1. Why is an absolute deadline safer than resetting local timeouts?
2. Why can three parallel calls cost more without adding their latencies?
3. What must happen before expensive work when insufficient budget remains?

## Explained answers

1. The absolute deadline preserves elapsed time across hops and prevents nested
   work from extending the user promise.
2. Parallel completion follows the slowest required child, while attempts,
   slots, CPU, and dependency load still accumulate across all children.
3. Reject, degrade, or use an approved fallback before dispatch; record the
   budget decision rather than starting predictably late work.

## Sources and next work

- gRPC Authors, [Deadlines](https://grpc.io/docs/guides/deadlines/), especially
  propagation and application cleanup responsibility.
- Google SRE, [Addressing Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/), “Latency and Deadlines.”
- Next: complete EX-01 and EX-02, then freeze the Week 21 call graph.
