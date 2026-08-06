---
lesson_id: L08
title: "Capacity Decisions and Defense"
---

# Capacity Decisions and Defense

## Outcomes

You can turn predictions and experiments into a scoped capacity decision with a
safe region, scaling signal, overload policy, owners, rollout, and reversal
conditions.

## Prerequisites

Lessons 1–7; Module 1 ADR and defense method.

## Mechanism

A capacity report is a decision artifact, not a benchmark dump. It connects:

```text
user outcome
→ workload and uncertainty
→ resource demand and predicted bottleneck
→ measurement method
→ observed saturation and failures
→ operating policy
→ cost, ownership, rollout, and reversal
```

Define the safe operating region as the intersection of all applicable
constraints:

- latency distribution remains within the journey objective
- useful throughput follows admitted logical demand
- queue depth and age do not grow persistently
- rejection matches the published overload contract
- downstream and retry bounds hold
- failover capacity covers the declared loss or sheds safely
- unit cost stays inside its boundary
- the load generator delivers the intended schedule

The first violated constraint defines the boundary for that workload, not for
all possible workloads. Record excluded operation mixes, skew, hosts, and
failure combinations.

A scaling signal requires threshold, evaluation window, action, action lead
time, and owner. Queue depth alone may be too late; a forecasted arrival rate or
service-demand change may act earlier. Use more than one signal only when the
decision rule remains explainable and testable.

The overload-policy ADR states:

- admission and priority
- authorization and tenant fairness
- degraded responses
- client retry guidance
- behavior when configuration is missing
- recovery and backlog handling
- rollout, rollback, and change audit
- owner of cross-team downstream agreements

### Defense procedure

1. State the decision and strongest evidence in two minutes.
2. Separate prediction from observation.
3. Explain the first saturating resource causally.
4. Show a failed prediction and what changed.
5. Defend the safe region under failover.
6. Answer cost, security, ownership, and rollout challenges.
7. Restate uncertainty without changing submitted assumptions.
8. Record reviewer disagreement and the experiment that resolves it.

## Worked example

Transit Signal may conclude:

> For the tested three-leg lookup mix on the stated host, admit rider work while
> p99, queue trend, and downstream bounds remain inside the measured region.
> Preserve separately authorized operator transitions. Reject excess rider work
> cheaply with bounded retry guidance. Do not claim the normal worker model as
> safe capacity until the 75% failover experiment also passes.

This is stronger than “scale at 70% CPU.” It names the journey, boundary,
priority authority, failure reserve, and missing evidence. A reviewer can
challenge any link.

Roll out the policy with shadow measurement first, then a small traffic slice,
then broader enforcement. Roll back to the prior finite limits if false
rejection exceeds its threshold. Never roll back to an unbounded queue.

## Common expert mistakes

- **Select the prettiest chart:** a decision needs falsifying and failure
  evidence.
- **Average incompatible trials:** different mixes form different capacity
  claims.
- **Hide rejection:** safe overload deliberately trades some availability for
  bounded recovery.
- **Name no owner:** limits drift and downstream agreements decay.
- **Make rollback unsafe:** disabling the control reintroduces the incident.
- **Treat reviewer preference as evidence:** resolve disagreement with shared
  drivers and a bounded test.

## Guided practice

Draft one safe-region sentence using a measured latency threshold, useful
throughput, queue trend, failover state, and exclusion. Then write the strongest
objection from a product owner who fears false rejection.

## Self-check

1. Why is a saturation curve insufficient as a capacity report?
2. What makes a scaling signal actionable?
3. Why must overload policy include authorization?
4. What is a credible reversal condition?

## Explained answers

1. It omits workload scope, user thresholds, failure reserve, operating action,
   cost, and ownership.
2. Its threshold and window leave enough time for a named owner to complete a
   defined action before the unsafe boundary.
3. Priority without authorization lets abusive callers consume protected
   capacity.
4. A measurable change in workload, service demand, failure reserve, SLO, cost,
   or downstream agreement that changes the option ranking.

## Sources and next work

- Google SRE, Addressing Cascading Failures (RES-03)
- Google Research, The Tail at Scale (RES-02)

Complete EX-12, the capacity report, ADR, and defense.
