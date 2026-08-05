---
lesson_id: L04
title: "Graceful Degradation and Degraded Capacity"
---

# Graceful Degradation and Degraded Capacity

## Outcomes

- Define a priority order and user-visible degraded contract.
- Keep queues, concurrency, retries, and dependency work bounded.
- Calculate surviving capacity and validate control interactions.

## Prerequisites

Lessons 1–3 and Modules 2 and 6.

## Design and capacity procedure

List journeys in priority order, the invariants each must preserve, minimum
useful response, and work that may be rejected, deferred, cached, or disabled.
Degradation must be explicit to users and telemetry. Returning stale data as
fresh or accepting work that cannot finish is not graceful.

For each failure domain calculate:

`surviving headroom = surviving measured capacity - priority demand`

Then apply concurrency, queue, deadline, retry, and dependency limits. Include
warm-up, traffic redistribution, background repair, telemetry, and operator
work. Failover reserve that ignores those costs is fictional.

Test interactions. A load balancer that interprets shed requests as cheap
success can route more traffic into the failing region. Autoscaling can arrive
after queues are already unsafe. Circuit breakers can synchronize recovery.
Use the journey SLI as the control outcome and component signals as constraints.

## Worked example

Each Northstar region can serve 60% of peak priority reads. Losing one region
leaves a 40% deficit before repair work. Northstar disables enrichment and bulk
export, serves last-verified metadata with a freshness marker, reserves capacity
for validation, and sheds low-priority reads before queues grow. Accepted work
keeps its deadline and idempotency contract.

## Common expert mistakes

- **Call errors degradation:** no priority or minimum-useful contract exists.
- **Cache without freshness:** the system violates correctness silently.
- **Assume autoscaling is reserve:** startup and failure-domain limits matter.
- **Shed after queuing:** resources are already consumed.
- **Forget recovery traffic:** catch-up competes with users.

## Guided practice

Given regions with capacities 800 and 700 requests/s, priority demand 900,
optional demand 350, and recovery work 100, calculate post-loss deficits.
Design admission order, user responses, queue/concurrency bounds, and one test
for a load-balancer/load-shedder feedback loop.

## Self-check

1. What must a degraded response disclose?
2. Why reserve capacity for recovery?
3. Where should load shedding occur?

## Explained answers

1. Its reduced behavior, freshness or completeness limits, and safe next action.
2. Reconciliation, catch-up, and probes consume the same finite resources; if
   they starve, the system cannot exit degradation.
3. Before expensive work and before an unbounded queue, while preserving
   priority, fairness, retry guidance, and observability.

## Sources and next work

Study RES-03, complete EX-08–EX-09, implement the public lab contract, and
record capacity predictions before running F01 or F07.
