# Module 14 Guided Exercises

Complete these on Northstar before opening the answer key. These exercises
practice the method; the independent graded artifacts use the learner's commerce
capability or a sanitized work-derived system.

## EX-01: Classify coupling

Classify five Northstar catalog dependencies as change, runtime, data, security,
or ownership coupling. For each, identify observed evidence and the user or team
outcome it affects.

## EX-02: Compare boundary options

Score modular monolith, synchronous service, and event projection against the
same six boundary-ledger drivers. Add one threshold that would favor each option
and one reversal condition.

## EX-03: Map flow of change

Trace a `publication_scope` change from request through decision, implementation,
contract review, deployment, operations, and support. Mark every team handoff
and approval queue.

## EX-04: Test ownership continuity

Assume the two registry engineers who know replay and rollback become
unavailable. Design an ownership exercise that can pass or fail without their
help. Include access, runbook, authority, escalation, and observed results.

## EX-05: Compare sourcing choices

Compare managed messaging, self-operated messaging, database polling, and the
platform event lane using the same outcome contract. Include security,
reliability, quota, cost, skills, support, and exit.

## EX-06: Define a paved road

Write the minimum platform event-lane offer: supported contract, self-service
path, telemetry, recovery, support, exception process, adoption metric, and
retirement condition.

## EX-07: Calculate unit cost

Using the Northstar table, calculate fully loaded monthly comparison cost and
cost per 1,000 good reads for both options. Explain why failed, stale, or slow
reads do not increase the denominator.

## EX-08: Run sensitivity

Recalculate the candidate for a 4× provider-price component that increases
direct cost from $15,000 to $33,000, 5% fewer good reads, and a six-month delay
that doubles monthly transition amortization. Identify the first stop threshold.

## EX-09: Build a compatibility matrix

For v1 and v2 producers and consumers, mark forward rollout, rollback, delayed
delivery, and replay combinations as pass, reject safely, or unsupported. State
the expected behavior for an unknown field.

## EX-10: Sequence expand and contract

Order these actions and give each an evidence gate: add `publication_scope`,
deploy tolerant reader, emit both fields, backfill, observe v1 use, remove
`public`, update replay fixtures, and expire rollback.

## EX-11: Define migration states

For Baseline, Expand, Backfill, Shadow, Cutover, Contract, and Decommission,
name the authority, read path, allowed writes, exit gate, stop condition, and
rollback.

## EX-12: Repair a backfill restart

A worker writes batch 42, crashes before recording completion, then restarts at
batch 43 because its cursor was advanced first. Explain the missing evidence and
design the corrected ordering, idempotency, version guard, and reconciliation.

## EX-13: Normalize shadow results

Define comparison rules for result ordering, timestamps, generated request IDs,
floating-point display, tenant scope, observation version, and missing results.
Separate harmless differences from semantic mismatches.

## EX-14: Critique dual writes

The registry writes its database and then calls the new catalog. Enumerate crash
points and externally visible states. Replace the design with one authoritative
write and a repairable derived path.

## EX-15: Design cutover and rollback

Choose cutover populations and observation windows. Define promotion and stop
thresholds for correctness, freshness, latency, cost, and operator control.
Prove what happens to state written after each cutover step.

## EX-16: Rehearse the failure matrix

For F01–F09, predict the failed invariant, first observable evidence, containment
action, repair, owner, and condition required before rerun.

## EX-17: Sequence technical strategy

Write four increments from instrumentation through decommissioning. Each must
deliver an outcome or new evidence even if later extraction stops. Add staffing,
dependency, cost, promotion, and reversal conditions.

## EX-18: Defend disagreement

Role-play a research-access lead asking for immediate extraction, a registry
lead asking to remain modular, finance challenging transition cost, and security
challenging the event boundary. Resolve the decision with shared drivers and
name one unresolved dissent item.

## PESD 2.0 extension to the final exercise

Extend the final guided exercise with a thin local platform product with a service catalog, self-service interface, golden path, policy guardrails, exception path, ownership metadata, platform SLO, adoption and support metrics, FinOps allocation, and an exit plan. Produce an
obligation/control/evidence row, a named owner, a bounded cost or capacity
effect, a failure or policy-drift test, a migration step, and a reversal trigger.
Label every observation with an accepted evidence mode and do not use fixture
replay as independent Build, Break, Implement, or Measure evidence.
