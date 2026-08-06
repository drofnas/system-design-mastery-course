---
lesson_id: L05
title: "Bulkheads, Pools, Health, and Bounded Fan-Out"
---

# Bulkheads, Pools, Health, and Bounded Fan-Out

## Outcomes

- Derive concurrency bounds from capacity, latency, and failover assumptions.
- Separate total, dependency, tenant, and health-check resources.
- Define admission, queue, rejection, drain, and recovery behavior.

## Prerequisites

Modules 2–3, Lessons 1–4, and ability to interpret queue and pool telemetry.

## Mechanism

Every remote-call protection consumes a finite resource: task, thread, socket,
connection, queue position, rate token, or downstream capacity. A pool limits
simultaneous ownership; a semaphore limits in-flight work; a bulkhead partitions
capacity so one workload cannot take all of it. A bound without an admission
policy merely moves waiting elsewhere.

Use Little's Law as a first consistency check: `L = lambda * W`. If Beacon sends
360 attempts/s and average dependency time is 0.1 s, mean concurrency is 36.
The pool of 72 supplies burst/headroom, but a slowdown to 0.4 s implies 144
in-flight attempts without admission. The correct response is not silently grow
the pool; reject or degrade within the dependency's proven capacity.

Health checks need separate semantics. Process liveness, readiness for new
traffic, and dependency health are different signals. A deep check that shares
the saturated request pool can mark every instance unhealthy and shift overload
to peers. Isolate cheap liveness, bound readiness dependencies, and test drain.

## Decision procedure

1. Measure normal and degraded service time by dependency and request class.
2. Calculate expected concurrency and choose explicit failover reserve.
3. Set total, dependency, tenant/key, retry, and health-check bounds.
4. Define queue capacity and maximum wait; prefer early bounded rejection.
5. Specify fairness and what happens to required versus optional work.
6. Test burst, slowdown, pool exhaustion, instance drain, and health failure.
7. Assign configuration, capacity review, incident, and exception owners.

## Worked example

Beacon's 72 slots are divided into 52 primary, 12 retry/repair, and 8 reserved
for other districts/recovery; no district may hold more than 29 primary slots.
The queue has 18 places with a 35 ms maximum wait. A full queue rejects before
fan-out. Liveness uses no dependency; readiness samples one bounded synthetic
path and does not consume primary slots.

## Common expert mistakes

- **One global pool only:** a hot tenant still starves everyone.
- **Large queue to avoid errors:** latency grows until deadlines expire in queue.
- **Increasing the pool during slowdown:** pushes collapse into the dependency.
- **Deep liveness checks:** dependency faults trigger restart and traffic-shift loops.
- **No drain test:** deployment kills active work or sends traffic to an exiting process.

## Guided practice

A caller produces 500 attempts/s at 80 ms mean and 220 ms degraded latency.
Calculate mean concurrency in both states. Propose a total bound, queue wait,
tenant cap, and failover reserve, then state what evidence would justify each.

## Self-check

1. Why is a semaphore insufficient without queue/admission rules?
2. What can a deep health check amplify?
3. Which metric reveals that waiting moved from dependency to local pool?

## Explained answers

1. Work can accumulate unbounded before acquiring the semaphore.
2. It can mark healthy processes unavailable, restart them, or shift traffic to
   already loaded peers during a dependency failure.
3. Pool wait and rejection distributions correlated with active permits,
   remaining deadline, and dependency latency.

## Sources and next work

- Google SRE, Addressing Cascading Failures (RES-05), resource exhaustion and health checks.
- Next: complete EX-09 and EX-12 and prove peak active never exceeds the contract.
