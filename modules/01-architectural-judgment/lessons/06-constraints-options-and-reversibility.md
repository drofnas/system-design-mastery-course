---
lesson_id: L06
week: 2
estimated_hours: 1.25
---

# Lesson 6: Constraints, Options, and Reversibility

## Outcomes

After this lesson, you can:

- Separate constraints, assumptions, preferences, and decision drivers.
- Define a cost envelope without inventing false precision.
- Compare simple, moderate, and distributed candidates on a shared basis.
- State evidence thresholds, migration seams, and reversal conditions.

## Prerequisites

Freeze the independent Week 1 baseline before applying this lesson to the
commerce capstone. Complete Lessons 1–5.

## Constraints remove choices

A constraint is imposed by the current decision context:

- A legal residency rule
- A contractual interface
- A fixed launch date
- A team with known skills and on-call capacity
- An existing system that cannot be replaced in the decision window

An assumption may turn out false. A preference can be traded. A decision driver
helps distinguish candidates.

Classify statements:

| Statement | Likely type | Why |
|---|---|---|
| Must use the authority’s existing identity provider this year | Constraint | Current contract and migration scope remove choice |
| Alert traffic will double in 18 months | Assumption | Forecast needs evidence |
| Team prefers one language | Preference or soft constraint | Strength depends on hiring, operations, and delivery impact |
| Revocation must reach riders within one minute | Decision driver | Measurable behavior can distinguish designs |

Misclassification damages reviews. A preference presented as a constraint ends
discussion. A real constraint presented as an assumption produces infeasible
options.

## Build a constraint and assumption register

For each item record:

| Field | Purpose |
|---|---|
| Statement | Precise claim |
| Type | Constraint, assumption, preference, or fact |
| Source/owner | Who can confirm or change it |
| Confidence | High, medium, or low |
| Consequence if false | Which decision or invariant changes |
| Evidence/date | How and when it will be tested |

Review high-impact, low-confidence assumptions first.

## Define a cost envelope

Cost is more than infrastructure:

- Build and migration effort
- On-call and incident load
- Security and compliance operation
- Vendor and license spend
- Change coordination
- Cognitive load
- Opportunity cost
- Recovery and degraded-mode capacity

An early envelope can use ranges:

```text
Delivery:
  One team, no more than 16 engineer-weeks before pilot.

Operations:
  Existing on-call group; no new 24×7 specialist rotation.

Recurring:
  Target under $0.002 per useful rider alert view at projected peak,
  with a monthly planning ceiling to be validated later.

Migration:
  Must allow rollback within one release window without data reconstruction.
```

These numbers are planning assumptions until measured. Their value is that they
make trade-offs visible.

## Prioritize decision drivers

Candidate comparison fails when every criterion has equal priority. Choose
roughly five to seven drivers and rank them.

Example:

1. Preserve alert-version authority and revocation.
2. Meet rider freshness targets during the projected burst.
3. Keep channel failure off the approval critical path.
4. Fit one team’s delivery and on-call capacity.
5. Permit a channel to be replaced without rewriting approval.
6. Remain inside the recurring cost envelope.

State why each driver matters and which evidence supports its rank.

## Three candidates, same problem

The syllabus requires simple, moderate, and distributed designs. These are not
labels for good, better, and best.

### Simple candidate

Minimize independently operated parts and contracts. Keep authoritative state
and workflow together unless a driver requires separation.

### Moderate candidate

Add one or two boundaries for a measured workload, failure, security, or
delivery need. Preserve one clear authority for business facts.

### Distributed candidate

Use independently deployed responsibilities, asynchronous flows, replicated or
partitioned state, or multiple operating regions where drivers justify their
cost.

Describe every candidate with the same views:

- Responsibilities and state owners
- Critical journey flow
- Failure and overload behavior
- Consistency or staleness rules
- Operations and ownership
- Security and trust
- Cost range
- Migration and reversal
- Supporting and missing evidence

Do not give the preferred candidate more detail than the others.

## Decision table

Use qualitative ratings only when each rating has an explanation:

| Driver | Weight | Simple | Moderate | Distributed |
|---|---:|---|---|---|
| Preserve version authority | 5 | Strong: one owner | Strong: one owner, copied delivery | Risk: cross-boundary transitions |
| Burst freshness | 4 | Unknown: needs load evidence | Plausible: delivery isolated | Plausible but higher operating cost |
| One-team operation | 4 | Strong | Moderate | Weak |

Weighted totals can organize discussion. They do not turn judgment into an
objective fact. Sensitivity-test the weights and uncertain ratings.

## Reversibility is designed

“We can change it later” is not a migration plan.

For each decision identify:

- Stable seam where an alternative could be introduced
- Data that must move or be rebuilt
- Compatibility period
- Verification method
- Rollback or roll-forward path
- Decommission work
- Trigger evidence

### Reversal condition

Good:

> Reconsider separating notification delivery when either the measured
> five-minute burst consumes more than 60% of the shared worker budget, channel
> incidents consume more than 20% of the rider-view error budget in two
> consecutive windows, or a separate owning team is funded.

Weak:

> Split it when we scale.

The good condition connects evidence to the reason for separation.

## Worked example: Transit Signal candidates

### Simple

One deployable application owns authoring, approval, current-version reads, and
delivery work. Delivery runs through an internal bounded work queue.

- Strength: one authoritative transition and one operating unit.
- Risk: channel load can compete with rider views unless resources are bounded.
- Test: measure shared resource interference during citywide fan-out.

### Moderate

One application owns authoring, approval, and rider reads. A separate delivery
worker consumes versioned delivery intents and can rebuild from approved
history.

- Strength: isolates channel slowness while preserving one state authority.
- Risk: introduces delivery lag, replay, and reconciliation.
- Test: stop the worker, grow backlog, resume, and prove bounded recovery.

### Distributed

Regional alert responsibilities accept changes under a coordination and
conflict policy; delivery and reads operate regionally.

- Strength: potential regional autonomy and latency.
- Risk: the current-version invariant, operator authority, replication, and
  failover become much harder.
- Missing driver: one transit authority and one regional operating team do not
  yet justify regional write authority.

The moderate candidate may win, but only if failure isolation matters enough to
pay for replay and reconciliation. The simple candidate should not lose because
it looks less advanced.

## Common expert mistakes

### Designing only one serious option

Straw alternatives make review ceremonial. Give each candidate its strongest
credible form.

### Hiding team cost

Independent deployment creates on-call, dashboards, access controls,
compatibility, release, and incident coordination work.

### Treating a score as evidence

A weighted matrix records judgment. It cannot validate an unsupported rating.

### Calling an assumption a constraint

“We must scale globally” often hides an untested forecast.

### Deferring migration thinking

The earliest design decisions often determine whether migration is safe.

## Guided practice

Complete:

- [EX-08](../exercises/exercises.md#ex-08-decision-drivers-and-candidates)
- [EX-09](../exercises/exercises.md#ex-09-reversal-conditions)

Then compare your candidate-design reasoning with the practice answer key.

## Self-check

1. What distinguishes a constraint from an assumption?
2. Why compare candidates using identical views and drivers?
3. What belongs in a cost envelope besides infrastructure?
4. Why is a weighted score not a proof?
5. What makes a reversal condition actionable?

## Explained answers

1. A constraint removes a choice in the current scope; an assumption is an
   unverified planning claim that may change the decision.
2. Shared views prevent the preferred option from receiving richer explanation
   and make trade-offs visible on the same basis.
3. Delivery, migration, operations, security, coordination, cognitive load,
   opportunity cost, and recovery capacity.
4. Weights and ratings are judgments. They organize reasoning but still require
   causal explanation and evidence.
5. It names a measurable trigger tied to the original driver and a credible
   migration or rollback path.

## Sources and next work

- [Michael Nygard, “Documenting Architecture
  Decisions”](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)
- Next: [Lesson 7](07-failure-models-and-adversarial-review.md)
