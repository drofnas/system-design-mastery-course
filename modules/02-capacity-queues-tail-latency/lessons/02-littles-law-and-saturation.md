---
lesson_id: L02
title: "Little’s Law and Saturation"
---

# Little’s Law and Saturation

## Outcomes

You can apply Little’s Law to consistent boundaries, calculate service-demand
limits, distinguish utilization from latency, and state the limits of the model.

## Prerequisites

Lesson 1; algebra; mean, rate, and time units.

## Mechanism

For a stable long-run boundary:

```text
L = λW
```

`L` is average work in the boundary, `λ` is the rate that enters and eventually
leaves that boundary, and `W` is average time in it. The identity is broad, but
it does not predict a percentile, prove stability, or tell you how service times
are distributed.

Boundary consistency is non-negotiable. If `L` counts work waiting plus work in
service, `W` must include queue plus service time. If rejected work never enters,
use admitted rate rather than attempted rate.

For a resource with `m` identical workers and mean service demand `D` seconds:

```text
nominal service capacity μ = m / D
offered utilization ρ      = λD / m
```

When sustained admitted `λ` exceeds service capacity, backlog must grow, work
must be rejected, or arrivals must be reduced. At exactly the nominal boundary,
any variance or interruption leaves no recovery margin.

For multiple resources, calculate demand per logical request at each resource:

```text
capacity at resource r = available parallelism_r / demand_r
system nominal capacity = minimum resource capacity
```

This bottleneck calculation excludes scheduler, protocol, interference, and
measurement overhead. Its purpose is to predict what to test.

### Repeatable technique

1. Draw the queueing boundary.
2. State which arrivals enter and which completions leave.
3. Align units before applying `L = λW`.
4. Calculate service demand per logical request at each finite resource.
5. Identify the minimum nominal capacity.
6. Predict what saturation will change: queue, rejection, latency, or useful
   throughput.
7. Record model exclusions and a falsifying experiment.

## Worked example

Transit Signal’s three-leg lookup has expected request service time 25.34618 ms
under the case’s two-point branch model. At 170 admitted requests/s:

```text
L = 170/s × 0.02534618 s = 4.309 average requests in service
```

Eight workers provide nominal worker capacity:

```text
8 / 0.02534618 s = 315.63 requests/s
```

At 170/s, offered worker utilization is about 53.9%. This does not mean p99 is
safe: approximately 2.97% of three-way requests contain a slow branch. It also
does not validate 315.63/s because the model excludes connection and scheduler
cost.

## Common expert mistakes

- **Combine different boundaries:** server concurrency with client end-to-end
  time gives a meaningless identity.
- **Use attempted rate after rejection:** rejected work did not occupy the
  service boundary.
- **Call the nominal limit safe capacity:** the calculation has no variance,
  failure reserve, or SLO.
- **Infer percentiles from a mean:** Little’s Law relates long-run averages.
- **Assume every worker is interchangeable:** shared downstreams can bind first.

## Guided practice

A service admits 120 requests/s. Mean end-to-end time inside its boundary is
80 ms, including 30 ms waiting. Calculate average in-system and in-service
concurrency. With six workers, calculate offered worker utilization.

## Self-check

1. When is `λ` attempted rather than admitted rate?
2. Can `L = λW` prove a queue is stable?
3. Why is 100% modeled utilization not a safe target?
4. What evidence reveals that a downstream binds before workers?

## Explained answers

1. Only when attempted work enters the chosen boundary; cheap pre-admission
   rejection belongs outside it.
2. No. The identity assumes suitable long-run averages; queue trend and
   completion evidence establish stability.
3. It leaves no room for variance, bursts, interruptions, recovery, or model
   error.
4. Downstream concurrency reaches its bound and rejection or waiting appears
   while service workers remain below their own bound.

For the practice: in-system `L = 120 × 0.08 = 9.6`; in-service demand is
`120 × 0.05 = 6`, so six workers are modeled at 100%.

## Sources and next work

- MIT OpenCourseWare, [Queueing Systems lecture notes](https://ocw.mit.edu/courses/1-203j-logistical-and-transportation-planning-methods-fall-2006/resources/lec5/)
- Julius Plenz, [How to Trade off Server Utilization and Tail Latency](https://www.usenix.org/conference/srecon19asia/presentation/plenz)

Complete EX-03 and freeze the first model before measuring.
