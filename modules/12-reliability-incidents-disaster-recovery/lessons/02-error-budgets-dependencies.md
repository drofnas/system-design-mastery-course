---
lesson_id: L02
title: "Error Budgets, Dependencies, and Composite Reliability"
---

# Error Budgets, Dependencies, and Composite Reliability

## Outcomes

- Calculate allowed bad events and consumed error budget.
- Model dependency contribution, correlation, and shared fate.
- Use sensitivity and expected exposure to compare reliability work.

## Prerequisites

Lesson 1 and basic probability.

## Derivation and decision procedure

For target `S` and `N` valid events:

- allowed bad events = `N × (1 - S)`;
- consumed fraction = observed bad events / allowed bad events;
- remaining events = allowed minus observed bad events.

Use unrounded counts for decisions. State whether the objective uses event or
time weighting. A ten-minute total outage and a partial two-hour correctness
fault can consume different budgets even when their wall-clock duration matches.

For a journey requiring independent serial dependencies, multiplying their
success probabilities can provide a planning estimate. Independence is a claim,
not a default. Shared control planes, networks, credentials, deployments, data,
or traffic can correlate failures. Model common causes explicitly and validate
with incident or experiment evidence.

Compare corrective work by expected user or data exposure reduced, not by the
largest component percentage. Include confidence, effort, cost, owner, and how
completion will be verified.

## Worked example

Northstar has 2,000,000 valid reads and a 99.9% SLO. It allows 2,000 bad reads.
Six hundred bad reads consume 30% of the budget. A plan that rounds the target
to “about 100%” cannot support that decision.

If routing succeeds 99.99%, catalog lookup 99.95%, and version verification
99.98%, an independent serial estimate is approximately 99.92%. Northstar does
not publish that as truth: routing and lookup share a regional network, so one
regional event can fail both. The model records a regional common-cause branch
and uses game-day evidence to estimate its exposure.

## Common expert mistakes

- **Subtract percentages:** budget is computed against valid events or time.
- **Multiply every dependency:** optional, parallel, fallback, and correlated
  paths do not share one formula.
- **Spend budget equally:** priority journeys can have different consequences.
- **Treat budget as permission:** invariant or security failures remain unacceptable.

## Guided practice

Calculate budget for 750,000 events at 99.95%. Then model an archive journey
with an identity service, search index, and optional thumbnail service. Draw
serial, optional, fallback, and shared-fate paths. Run low/base/high sensitivity
for the common-cause probability.

## Self-check

1. How many bad events does 99.95% allow in 750,000 events?
2. Why can independence overstate reliability?
3. Can an error budget permit duplicated irreversible effects?

## Explained answers

1. `750,000 × 0.0005 = 375` bad events.
2. One common network, deploy, credential, or data fault can fail several paths
   together, making their outcomes correlated.
3. No. Error budgets govern user-visible reliability risk; safety invariants and
   authorization boundaries remain hard constraints.

## Sources and next work

Complete EX-03–EX-05 and carry the dependency/common-cause model into Lesson 3.
