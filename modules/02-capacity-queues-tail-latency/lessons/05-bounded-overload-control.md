---
lesson_id: L05
title: "Bounded Overload Control"
---

# Bounded Overload Control

## Outcomes

You can locate every place work waits, choose explicit queue and concurrency
bounds, and define admission, priority, degradation, and recovery behavior.

## Prerequisites

Lessons 1–4; Module 1 invariants and quality scenarios.

## Mechanism

When arrivals exceed completions, one of four things happens:

1. work waits,
2. work is rejected,
3. work is degraded or deferred, or
4. the system consumes an unbounded resource until it fails.

A queue stores time debt. With `Q` requests ahead and completion capacity `μ`,
a rough lower bound on added wait is `Q/μ`. A larger queue can absorb a short
burst but cannot create service capacity. It can also ensure that accepted work
finishes after its deadline.

Every wait must have:

- a maximum size or concurrency
- an admission rule
- an expiry or deadline rule
- an observable depth and age
- an owner and change procedure
- recovery behavior after arrivals fall

Admission belongs before the constrained resource. Rejecting after expensive
parsing, authorization, or fan-out may preserve no useful capacity. Security
still precedes priority: a caller cannot claim high-priority work without the
required authorization.

Load shedding should maximize useful outcomes, not request success count.
Possible policies include:

- reject newest work when the queue is full
- expire work that cannot meet its deadline
- reserve capacity for invariant-preserving operations
- serve a cheaper, explicitly degraded response
- defer non-interactive work

Each policy creates product and fairness decisions. Record who approves them.

### Repeatable technique

1. Inventory every explicit and implicit queue.
2. Connect each queue to the resource that drains it.
3. Calculate acceptable wait from the remaining user deadline.
4. Choose the smallest bound that supports intended bursts.
5. Define cheap rejection, retry guidance, and priority authorization.
6. Test normal, full, recovery, and configuration-error states.
7. Alert on user outcome and queue age, not depth alone.

## Worked example

Transit Signal has eight workers and 25.35 ms mean request service in the model.
An eight-entry queue adds roughly:

```text
8 / 315.63/s ≈ 25.35 ms
```

at nominal aggregate completion capacity. A 64-entry queue adds roughly
203 ms before variance. That may still fit the one-second p99 target, but it
consumes most of the 300 ms p95 target for requests behind the queue.

The case prioritizes authorized operator transitions over rider refreshes during
overload. Rider work receives explicit rejection or a tested degraded response.
Notification delivery cannot exhaust the same downstream slots used for
authoritative changes.

## Common expert mistakes

- **Treat a queue as capacity:** it changes when work fails, not how fast work
  completes.
- **Hide queues in clients and pools:** unmeasured waiting still consumes the
  deadline.
- **Reject too late:** expensive failed work continues to saturate the system.
- **Prioritize by caller-supplied labels:** this creates an abuse path.
- **Never exercise degraded mode:** emergency-only code is least trustworthy
  when needed.

## Guided practice

A four-worker service completes 80 requests/s and has 150 ms remaining in its
user deadline. Calculate the maximum queue implied by the simple `Q/μ` bound.
Then state why you would choose a smaller operational limit.

## Self-check

1. What is the difference between admission control and scaling?
2. Why monitor queue age?
3. When is zero waiting queue defensible?
4. What must happen when the overload configuration is missing?

## Explained answers

1. Admission bounds current work; scaling changes future supply after its lead
   time.
2. Depth without drain rate cannot reveal deadline consumption or recovery.
3. For steady interactive traffic where waiting cannot improve success and
   another replica or caller can handle an immediate rejection.
4. Fail to a documented safe default, emit an operational signal, and preserve
   invariant-protecting work; do not silently accept unbounded load.

The simple practice bound is `0.15 s × 80/s = 12` waiting requests. A smaller
limit covers variance, service already in progress, and measurement error.

## Sources and next work

- Google SRE, [Addressing Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/)
- David Yanacek, [Avoiding Insurmountable Queue Backlogs](https://aws.amazon.com/builders-library/avoiding-insurmountable-queue-backlogs/)

Complete EX-07 and EX-08, then inspect the lab’s queue-full events.
