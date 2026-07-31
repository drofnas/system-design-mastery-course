---
lesson_id: L02
week: 1
estimated_hours: 0.75
---

# Lesson 2: Problem Framing and Workloads

## Outcomes

After this lesson, you can:

- Express a critical user journey and its measurable business outcome.
- Separate functional scope, non-goals, constraints, and assumptions.
- Model normal, peak, burst, projected, and skewed work with explicit units.
- Perform a first-order sensitivity analysis without pretending estimates are
  measurements.

## Prerequisites

Complete [Lesson 1](01-architectural-judgment.md). You should be comfortable
with rates, percentages, and unit conversion.

## Start from a journey, not a feature list

A feature list describes what teams intend to build. A critical user journey
describes what a user must accomplish across several interactions.

Use this framing:

```text
For [user in context],
when [trigger or need],
the system helps them [completed outcome],
measured by [metric, target, population, and window].
```

Example:

> For a rider planning a trip during a disruption, when an operator approves a
> route-impact alert, the rider can see the current alert before choosing a
> route, measured as 99% of eligible alert views showing the approved version
> within two minutes over a rolling 28-day window.

This does not yet say how the system works. It tells us what future mechanisms
must support.

Google’s SRE guidance distinguishes an indicator specification from its
implementation. “The proportion of eligible alert views that show the approved
version within two minutes” is the desired observation. Server logs may be one
measurement implementation, but they could miss failures before a request
reaches the server. Record that limitation.

## Scope, non-goals, constraints, and assumptions

These terms prevent four different kinds of confusion.

| Term | Question | Example |
|---|---|---|
| Functional scope | What behavior is included? | Operators approve, update, and revoke alerts |
| Non-goal | What related behavior is intentionally excluded? | Predicting disruptions from raw vehicle telemetry |
| Constraint | What boundary is imposed? | Must support the existing operator identity system |
| Assumption | What unverified claim supports planning? | No more than 200 operators are active at once |

An assumption needs:

- Owner
- Confidence
- Consequence if false
- Test or evidence source
- Review date

A non-goal needs a reason and a scope boundary. “Security is a non-goal” is
invalid when the system handles private or authoritative data.

## Build the workload model

Architecture responds to work, not monthly active-user counts alone. Model the
operations and state transitions that consume different resources or create
different risks.

### Workload dimensions

Include:

- Request or event rate by operation
- Concurrent work
- Payload and response size
- Read/write mix
- Data volume and retention
- Key, tenant, geographic, and time skew
- Fan-out per accepted action
- Background work
- Normal, peak, burst, and projected conditions
- Failure or recovery workload

### Use units on every number

“50,000 users” is not load. Ask how often they act and over what window.

If 300,000 riders make 4 alert checks during a 2-hour morning peak:

```text
checks = 300,000 riders × 4 checks/rider = 1,200,000 checks
average rate = 1,200,000 checks ÷ 7,200 seconds ≈ 167 checks/second
```

The average can hide a short burst. If 20% arrive during the busiest 5 minutes:

```text
burst checks = 1,200,000 × 0.20 = 240,000
burst rate = 240,000 ÷ 300 seconds = 800 checks/second
```

The difference between 167 and 800 is a design driver. Neither number is a
capacity requirement yet. Both depend on assumptions.

### Describe projection separately

Projection is not peak. A useful table distinguishes:

- **Normal:** recurring expected operation
- **Peak:** predictable high period
- **Burst:** short exceptional concentration
- **Projected:** credible future point and horizon

Do not multiply every dimension by ten simultaneously without a scenario. A
tenfold user increase may change write rate, read rate, tenancy, or geography
differently.

### Model skew

Uniform averages are often optimistic. For transit alerts:

- One major route may receive 40% of all reads.
- A regional incident may concentrate traffic in one city.
- One alert may fan out to millions of device subscriptions.
- Operator writes remain small while public reads spike.

Name the skew key and concentration. “Zipfian traffic” is less useful than “the
top 1% of alert identifiers receive 55% of reads during disruptions.”

## Sensitivity before precision

An early estimate should reveal which assumption matters most.

Suppose burst rate is:

```text
population × checks per rider × burst share ÷ burst duration
```

Vary one input at a time:

| Input | Low | Base | High | Effect |
|---|---:|---:|---:|---|
| Eligible riders | 200k | 300k | 500k | Linear |
| Checks/rider | 2 | 4 | 6 | Linear |
| Burst share | 10% | 20% | 35% | Linear |
| Burst duration | 10 min | 5 min | 2 min | Inverse |

The burst duration may create more uncertainty than annual growth. That tells
you which measurement to obtain first.

Module 2 develops queueing and capacity models. Here, the goal is to make the
shape and uncertainty visible enough to frame architecture.

## Worked example: Transit Signal

### Journey

Rider opens a trip view during a disruption and sees the currently approved
route alert soon enough to change plans.

### Initial workload

| Dimension | Normal | Peak | Burst | 18-month projection | Basis |
|---|---:|---:|---:|---:|---|
| Alert-view reads | 60/s | 170/s | 800/s for 5 min | 1,200/s burst | Planning assumption |
| Approved alert changes | 2/min | 10/min | 40/min | 60/min | Historical incident estimate |
| Subscribers per alert | 5k | 50k | 1.2m | 1.8m | Route concentration assumption |
| Alert payload | 1.5 KiB | 2 KiB | 4 KiB | 4 KiB | Sample content |
| Retained alert versions | 50k/year | same | same | 90k/year | Regulatory assumption |

### High-sensitivity assumptions

1. The busiest 5-minute concentration.
2. Notification fan-out for a citywide alert.
3. Whether clients poll or receive pushed updates.

These need evidence before implementation commitments.

## Common expert mistakes

### Using daily volume as a throughput target

Daily averages erase bursts and geography. Convert volume into a rate for the
relevant window.

### Treating estimates as promises

Label source and confidence. A precise decimal does not create evidence.

### Modeling only user requests

Include ingestion, replication, fan-out, retries, backfills, reconciliation, and
recovery traffic when relevant.

### Ignoring product response to failure

A dependency failure can change the workload: retries, refreshes, and support
traffic may grow while useful throughput falls.

### Declaring non-goals that hide correctness

Scope can defer features. It cannot defer preserving a business invariant for
behavior already in scope.

## Guided practice

Complete:

- [EX-02](../exercises/exercises.md#ex-02-scope-assumption-or-constraint)
- [EX-03](../exercises/exercises.md#ex-03-workload-and-sensitivity)

Use the transit case. Do not use the commerce capstone until the exercises are
finished.

## Self-check

1. Why is monthly active users insufficient for capacity or architecture?
2. What is the difference between a peak and a burst?
3. How should an unverified workload number appear in a design?
4. Why perform sensitivity analysis before seeking precise estimates?
5. What makes a service metric different from a user-journey outcome?

## Explained answers

1. It does not specify operations per user, concurrency, time concentration,
   payload, read/write mix, skew, or background work.
2. A peak is a predictable high operating period; a burst is a shorter,
   concentrated event that may be exceptional and can exceed steady capacity.
3. Label it as an assumption with units, source, confidence, consequence if
   false, and a plan to verify it.
4. Sensitivity shows which uncertain input can change the decision, focusing
   measurement effort where it matters.
5. A service metric observes one implementation boundary. A journey may cross
   clients, networks, and dependencies and can fail even when one server reports
   success.

## Sources and next work

- [Google SRE Workbook, “Implementing
  SLOs”](https://sre.google/workbook/implementing-slos/)
- [Module resource assignment](../resources.md#google-sre-workbook-implementing-slos)
- Next: [Lesson 3](03-invariants-and-state-ownership.md)

