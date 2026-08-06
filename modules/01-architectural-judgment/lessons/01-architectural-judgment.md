---
lesson_id: L01
title: "Architectural Judgment"
---

# Architectural Judgment

## Outcomes

After this lesson, you can:

- Separate a system-design problem from a technology-selection exercise.
- Frame an architectural decision as an evidence-backed claim under uncertainty.
- Identify the decisions that need broad review and the decisions that should
  remain local.
- Explain how Principal-level judgment differs from having a large pattern
  vocabulary.

## Prerequisites

You should have participated in at least one production design review or
post-incident review. No architecture notation is required.

## The job is to improve decisions

Architecture work begins when consequences outlive the code change that created
them. The consequences may affect data correctness, user trust, incident blast
radius, team ownership, cost, delivery speed, or the ability to migrate later.

Patterns and products are useful only after the problem is framed. “Use events,”
“move to services,” and “put it behind a cache” are proposed mechanisms. They
are not outcomes and they do not explain which trade-off is being accepted.

Principal-level judgment has four recurring moves:

1. **Make the decision frame explicit.** Name the outcome, workload, invariant,
   constraints, failure assumptions, owners, and time horizon.
2. **Convert opinions into claims.** “This is simpler” becomes “this option has
   one authoritative state owner, one deployment sequence, and no cross-boundary
   compatibility contract for the next twelve months.”
3. **Ask what would falsify the claim.** A claim that no observation can change
   is a preference, not engineering evidence.
4. **Improve the group’s reasoning.** A strong architect makes assumptions,
   disagreements, and consequences visible so other engineers can decide well.

The goal is not to be the person with the answer. The goal is to make the
organization less likely to commit to an expensive answer for the wrong reason.

## A repeatable decision frame

Use this order before naming technologies:

```text
Outcome
  ↓
Users and journeys
  ↓
Workload and growth
  ↓
Invariants and quality scenarios
  ↓
Constraints, ownership, and failure model
  ↓
Decision drivers
  ↓
Options and evidence
  ↓
Decision, consequences, and reversal conditions
```

Each arrow is a challenge. A design may need to revisit an earlier statement.
That is useful learning, not failure.

### Outcomes

An outcome describes a change in the world for a user or the business. “Build an
alert platform” is an output. “Riders receive trusted disruption information
soon enough to choose another route” is an outcome.

### Claims

A design argument has this form:

```text
Given [workload, constraints, and failure model],
option [X] should achieve [measurable response]
because [causal mechanism].
We will reconsider it if [evidence threshold].
```

This format exposes the part most architecture discussions hide: why the
mechanism should create the desired behavior.

### Decision scope

Escalate a decision into an ADR or RFC when it materially affects one or more of:

- Business or safety invariants
- Persistent data meaning or ownership
- Public interfaces or compatibility
- Failure isolation or recovery
- Security and privacy boundaries
- Multiple teams or operating groups
- Long-lived cost or vendor commitment
- Migration difficulty

Keep reversible implementation detail local when it has a small blast radius,
an obvious test, and no cross-team contract. Architecture review is scarce
attention. Spending it on naming a helper function weakens it.

## Evidence levels

Not all evidence is equal. Record what you actually have:

1. **Assumption:** plausible but unverified.
2. **Analogy:** observed in a related system with different context.
3. **Calculation:** a model based on stated inputs.
4. **Prototype or experiment:** controlled observation with known limits.
5. **Production observation:** relevant behavior under real load and operations.
6. **Repeated evidence:** stable result across time, workloads, or systems.

Higher is not always available. A transparent assumption can support a
reversible early decision. The error is presenting it as production fact.

## Worked example: Transit Signal

A city asks for “a modern real-time rider-alerting platform.”

A technology-first response might propose a stream, multiple regional services,
and push notifications. That response has not established:

- Which riders and journeys matter most
- What “real-time” means
- Whether the authoritative fact is an operator declaration or a sensor event
- How duplicate or revoked alerts behave
- Whether the city has one operations team or several
- What cost and recovery targets are credible

A better first frame is:

> During a service disruption, a rider planning or taking a trip needs a
> trustworthy route-impact update early enough to change plans. The first
> decision is how an operator-approved disruption becomes authoritative and how
> downstream channels expose its current version.

This frame identifies an outcome and a likely correctness boundary without
choosing a database, broker, cloud, or deployment shape.

### Initial decision claim

> Given one transit authority, one operations group, a regional user base, and
> a requirement to publish approved alerts within two minutes, begin with one
> authoritative alert workflow and independently replaceable delivery adapters.
> Reconsider deployable separation when measured delivery load, failure
> isolation, or ownership prevents the target from being met.

This is not yet a final design. It is useful because it can be challenged.

## Common expert mistakes

### Treating experience as evidence

“I have seen this before” can identify a hypothesis quickly. It does not prove
that the workload, constraints, or team topology match.

### Using architecture labels as conclusions

“Event-driven,” “hexagonal,” and “microservices” compress many choices into one
label. Review the actual state transitions, boundaries, failure behavior, and
ownership.

### Optimizing for a hypothetical distant future

Unbounded future flexibility creates present complexity. Choose a credible
planning horizon and name evidence that would justify the next state.

### Confusing disagreement with obstruction

A reviewer who asks for a failure model may be protecting a different
invariant. Restate the decision drivers before debating mechanisms.

### Recording only the winning option

Future engineers need to know why an attractive alternative lost. Without that
context they either preserve a stale decision blindly or reverse it blindly.

## Guided practice

Rewrite each statement as a decision claim:

1. “We need microservices because usage will grow.”
2. “The system must be highly available.”
3. “A queue will make checkout reliable.”

For each, name:

- Missing workload or environment
- Desired measurable behavior
- Causal mechanism that must be tested
- Evidence that would reverse the choice

Complete [EX-01](../exercises/exercises.md#ex-01-from-solution-to-decision-frame)
before reading the answer key.

## Self-check

1. Why is “use a distributed architecture” not an architectural outcome?
2. When is an assumption acceptable evidence?
3. What makes a decision architecturally significant?
4. What is the Principal engineer’s contribution when several options could
   work?

## Explained answers

1. It names a structural approach, not a user or business result. It also hides
   the workload, failure model, and costs that might justify distribution.
2. An assumption is acceptable when it is labeled, its consequence if false is
   understood, the decision is proportionately reversible, and there is a plan
   to obtain stronger evidence.
3. Significance comes from consequence and reversal cost: correctness, data,
   interfaces, failure behavior, trust, ownership, cost, or migration impact.
4. Make the shared drivers and evidence visible, surface unresolved risk, help
   the group choose, and record what would cause reconsideration.

## Sources and next work

- Course foundation: [`00_COURSE_SYLLABUS.md`](../../../00_COURSE_SYLLABUS.md)
- Decision records: [Michael Nygard, “Documenting Architecture
  Decisions”](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)
- Next: [Lesson 2](02-problem-framing-and-workloads.md)
