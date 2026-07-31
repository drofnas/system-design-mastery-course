---
lesson_id: L01
title: "Workload and Useful Work"
week: 5
---

# Lesson 1: Workload and Useful Work

## Outcomes

You can define a workload boundary, distinguish logical work from attempts, and
model normal, peak, burst, projected, and skewed demand with visible uncertainty.

## Prerequisites

Module 1 workload and quality-scenario artifacts; rates, ratios, and units.

## Mechanism

A capacity model begins with work crossing a named boundary. “One million users”
does not state how often they act, which operations they choose, how requests
cluster in time, or how much resource each operation consumes.

Define at least:

```text
logical arrival rate = distinct user/business operations / time
attempt rate         = all initial and retry attempts / time
operation mix        = fraction of each operation class
useful throughput    = distinct successful operations / time
```

The boundary matters. A browser retry is a new server attempt but not a new
checkout. A three-leg journey lookup is one rider operation and three
downstream branches. If the numerator changes halfway through a report, the
capacity conclusion becomes unreviewable.

Traffic shape needs a rate and a window. A five-minute 800/s burst is different
from 800/s sustained for a day. Include:

- normal and peak steady periods
- burst rate, duration, and onset
- operation mix
- key, tenant, or route skew
- growth horizon
- background and recovery work
- low/base/high inputs that could change the decision

Data growth is also work. Retention increases stored bytes, index size, scan
cost, and recovery time. Express growth as new records or bytes per time and
apply retention, replication, and amplification explicitly rather than hiding
them in a single multiplier.

### Repeatable technique

1. Name the user journey and business completion.
2. Choose the system boundary.
3. Define one logical-work identity.
4. Split the journey into operation classes and branch work.
5. State normal, peak, burst, projected, skewed, and recovery rates.
6. Label each input measured, calculated, assumed, or unknown.
7. Run sensitivity on the two or three inputs that can change the decision.

## Worked example

Transit Signal models one rider journey lookup as one logical request. A
three-leg journey creates three branch attempts.

At 170 logical requests/s:

```text
downstream branch rate = 170 × 3 = 510 branches/s
```

If 2% of logical requests retry once:

```text
server attempt rate = 170 × 1.02 = 173.4 attempts/s
```

Useful throughput remains at most 170 journeys/s. Calling 173.4 “throughput”
would reward duplicated work.

The 800/s five-minute burst contains:

```text
800/s × 300 s = 240,000 logical journey requests
```

If a citywide alert concentrates 70% of requests on one route, fleet-wide
average capacity says little about the hot route’s queue.

## Common expert mistakes

- **Start from host count:** host count is supply, not demand.
- **Average a whole day:** it erases burst duration and recovery debt.
- **Mix requests and attempts:** retries appear as successful scaling.
- **Model only foreground work:** reconciliation and backlog drain consume the
  same resources during recovery.
- **Treat projections as measurements:** false precision hides the sensitivity
  that should guide experiments.

## Guided practice

For 300 browse operations/s, 20 checkout operations/s, and a 5% browse retry
rate, calculate logical work, attempt work, and useful throughput if all logical
operations succeed. Then add a two-minute 4× browse burst and state which rate
must drive admission.

## Self-check

1. Why can daily request count not determine required concurrency?
2. Does a successful retry add useful throughput?
3. Which workload dimension exposes a hot tenant?
4. Why include recovery work in a capacity model?

## Explained answers

1. Concurrency depends on rate and time in the boundary; a daily total provides
   neither short-window rate nor service time.
2. No. It may recover one logical operation, but it remains another attempt for
   the same identity.
3. Key or tenant skew, including the rate and concentration window.
4. Recovery often overlaps new demand. Ignoring it produces a design that can
   serve normally but cannot catch up.

## Sources and next work

- MIT OpenCourseWare, [Queueing Systems lecture notes](https://ocw.mit.edu/courses/1-203j-logistical-and-transportation-planning-methods-fall-2006/resources/lec5/)
- Google SRE, [Addressing Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/)

Complete EX-01 and EX-02, then continue to Lesson 2.
