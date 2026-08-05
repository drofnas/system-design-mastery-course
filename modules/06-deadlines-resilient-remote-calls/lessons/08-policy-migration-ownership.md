---
lesson_id: L08
title: Remote-Call Policy, Migration, and Ownership
---

# Remote-Call Policy, Migration, and Ownership

## Outcomes

- Compare coherent policies under common user, safety, operating, and cost drivers.
- Plan compatibility, staged rollout, rollback, exceptions, and decommissioning.
- Lead a teach-back that resolves disagreement with evidence.

## Prerequisites

Lessons 1–7, the six-fault matrix, and Module 1 decision-artifact method.

## Reasoning method

A policy is a cross-team contract, not a library-default inventory. It must name
which caller owns the deadline and retries, how dependencies advertise semantics,
how commands handle ambiguity, where resources are bounded, what users see under
partial failure, and who can approve exceptions.

Compare at least three coherent options: minimal fixed bounds, bounded retries
with idempotency and fairness, and adaptive controls such as hedging/breaking.
Use the same drivers: useful journey success, invariant safety, recovery,
dependency load, tenant fairness, security/privacy, unit cost, observability,
delivery effort, and operator cognitive load.

Migration must tolerate mixed clients. Start with telemetry-only propagation,
then server-side maximums and cancellation observation, bounded concurrency,
idempotency for commands, and finally controlled retry changes. Canary by
operation/tenant, retain an immediate configuration rollback, and remove old
automatic retries only after attempt telemetry proves ownership.

## Repeatable technique

1. Freeze the current call graph, behavior, and evidence gaps.
2. Publish operation/error/idempotency contracts before changing retries.
3. Shadow remaining-deadline and attempt metrics without enforcement.
4. Roll out bounds and cancellation, then safe retry ownership.
5. Test all six faults, rollback, failover reserve, and mixed-version behavior.
6. Record exceptions with owner, reason, cap, evidence, expiry, and review date.
7. Teach the causal model; record dissent and evidence that would reverse it.

## Worked example

Beacon selects bounded retries with idempotent reservation, fixed fan-out pools,
district fairness, and explicit partial-result semantics. It first ships metrics,
then cancellation and pool caps, then retry-token enforcement at 5%, canaries to
10%, and removes dependency-client defaults. Rollback disables extra attempts
but keeps deadlines and deduplication. Breakers/hedges remain experiments with
separate budgets and expiry dates.

## Common expert mistakes

- **Mandating one timeout globally:** operation usefulness and latency differ.
- **Changing retries before visibility:** amplification becomes untraceable.
- **Rolling out idempotency keys without conflict semantics:** key reuse corrupts intent.
- **No exception expiry:** temporary unsafe behavior becomes permanent policy.
- **Counting library adoption as migration completion:** old callers still reset deadlines or retry.

## Guided practice

Build a three-option decision table for Beacon. Add one dissent from the road
data owner and one from dispatch operations. Define a canary gate, rollback
trigger, configuration owner, and evidence that would justify hedging later.

## Self-check

1. Why introduce telemetry before enforcement?
2. What should rollback preserve?
3. How does a policy expose organizational risk?

## Explained answers

1. It reveals current attempts, deadlines, compatibility, and false-rejection
   risk before behavior changes.
2. Safety improvements such as idempotency and bounded cleanup; rollback should
   remove the risky retry/control change without recreating duplicate effects.
3. Every call edge and exception has owners for semantics, capacity, rollout,
   incident response, and review; missing ownership becomes an explicit risk.

## Sources and next work

- Craig Fender and Ravindra Punati, [Avoiding Cascading Failures at eBay?](https://www.usenix.org/conference/srecon16/program/presentation/fender), SREcon 2016.
- Google SRE, [Addressing Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/).
- Next: complete EX-15 and EX-16, write the policy, and conduct the defense.

## PESD 2.0 extension: modern constraints and ownership

PESD 2.0 adds **per-tenant work and cost budgets, identity-aware quotas, provider compatibility, residency-safe fallback, and fairness across critical traffic classes**.

### Repeatable decision procedure

1. Inventory the affected data, tenants, identities, providers, jurisdictions,
   control planes, evidence owners, and cost owners before selecting a mechanism.
2. State the invariant and the authority that may change it. Separate a claimed
   policy from the enforcement point and from the evidence that proves execution.
3. Freeze a prediction, implement or model the named mechanism, and record the
   accepted evidence mode and runtime boundary.
4. Inject one policy, isolation, recovery, or supplier failure in addition to the
   module's mechanism failure. Preserve raw evidence before interpretation.
5. Compare at least two options across product outcome, technical mechanism,
   security and governance, operations and recovery, economics, ownership,
   migration, and reversal triggers.

### Non-capstone extension

Apply the procedure to the module's continuing case. Add one tenant or governed
data class, one supplier or control-plane dependency, and one deletion, recovery,
or exit obligation. The completed case may demonstrate the method, but its
topology, thresholds, policy choices, and answer are not defaults for Global
Commerce.

### Evidence boundary

Use `derived`, `executed_deterministic`, `measured_loopback`,
`measured_container`, `modeled_capacity`, `fixture_replay`, or
`measured_accelerator` exactly as defined by the course. Fixture replay supports
practice and remediation only. Modeled remote scale is not local measurement.
Every trial records commit and input/configuration hashes, runtime and resource
limits, clock, warm-up/repetition policy, raw outcomes, and limitations.

### Source boundary

Use the module's bounded primary sources and preserve the local evidence boundary.
