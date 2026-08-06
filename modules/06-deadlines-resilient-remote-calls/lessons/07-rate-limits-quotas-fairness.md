---
lesson_id: L07
title: "Rate Limits, Quotas, and Fairness"
---

# Rate Limits, Quotas, and Fairness

## Outcomes

- Separate rate, concurrency, quota, and cost controls.
- Design fair admission across tenants, operations, and retries.
- Reason about identity, clock, distributed enforcement, and abuse boundaries.

## Prerequisites

Module 2 queue controls, Lesson 5 resource bounds, and basic token-bucket math.

## Mechanism

A rate limit bounds arrivals per interval; a concurrency limit bounds active
work; a quota bounds cumulative entitlement; a cost budget bounds weighted
consumption. A cheap read and expensive fan-out should not consume identical
tokens if their risk differs.

A token bucket with refill `r` tokens/s and capacity `b` permits long-run rate
`r` and bursts up to `b`. It does not bound how long accepted work remains
active, so pair it with concurrency. Scope keys to an authenticated principal,
tenant, operation, and sometimes hot resource. Define behavior when identity is
missing and protect limit metadata from enumeration.

Distributed enforcement trades precision for availability and cost. A single
global counter is coordinated but can become a dependency; local buckets admit
bounded overshoot. State the overshoot under `n` independent enforcers rather
than calling a limit exact. Reserve capacity for recovery and critical traffic,
and prevent retries from bypassing original-request fairness.

## Decision procedure

1. Name scarce resources and economic/abuse risks.
2. Choose identities and workload classes; weight by expected resource cost.
3. Set rate, burst, concurrency, and cumulative quota separately.
4. Calculate distributed overshoot and fail-open/fail-closed consequences.
5. Specify retry, repair, operator, and health-check priority without starvation.
6. Expose accepted, rejected, queued, active, token, and per-class outcome metrics.
7. Test hot tenant, missing identity, limit-store failure, and recovery ramp.

## Worked example

Beacon allows 120 logical requests/s with burst 300 for 20 seconds, but only 72
active dependency attempts. Districts receive weighted shares and a 40% active
cap. Extra attempts consume both the district share and a caller-wide retry
token. Emergency operator traffic has a small reserved lane; it cannot borrow
unbounded general capacity. If distributed local buckets can overshoot by 8
tokens across four instances, the policy records that exposure.

## Common expert mistakes

- **Rate limit only:** slow accepted calls still exhaust concurrency.
- **One tenant key:** a hot product or operation hides within the aggregate.
- **Retry traffic uncharged:** failing tenants get more capacity than healthy ones.
- **Global exactness by default:** the limiter becomes a critical dependency.
- **Permanent priority:** low-priority work starves even after recovery.

## Guided practice

Design controls for two tenants: A sends cheap reads; B sends five-times-cost
fan-outs. Both have the same business entitlement. Choose weights, burst,
concurrency shares, and a distributed overshoot bound. Explain fairness in user
outcomes, not just equal request counts.

## Self-check

1. Why pair rate and concurrency limits?
2. What does a local distributed bucket sacrifice?
3. Why charge retry attempts to fairness budgets?

## Explained answers

1. Rate controls arrivals; concurrency controls residence time and active cost.
2. Exact global enforcement; bounded overshoot buys independence and availability.
3. Otherwise failures grant extra resource share and amplify pressure on healthy tenants.

## Sources and next work

- Google SRE, Addressing Cascading Failures (RES-05), load shedding and client isolation.
- Marc Brooker, Timeouts, retries, and backoff with jitter (RES-04).
- Next: complete EX-12 and integrate fairness evidence into the failure matrix.
