---
lesson_id: L04
title: "Quality-Attribute Scenarios"
---

# Quality-Attribute Scenarios

## Outcomes

After this lesson, you can:

- Explain why “fast,” “reliable,” and “secure” are not requirements.
- Write a six-part quality-attribute scenario.
- Connect a scenario to a user journey, measurement, and design decision.
- Prioritize scenarios and expose conflicts between qualities.

## Prerequisites

Complete [Lessons 1–3](01-architectural-judgment.md). Read the assigned CMU SEI
and Google SRE sections in the [resource guide](../resources.md).

## Quality names do not constrain a design

Most systems should be reliable, secure, maintainable, usable, and affordable.
That list does not distinguish one architecture from another.

CMU SEI uses scenarios to make a quality operational. A useful scenario has six
parts:

1. **Stimulus source:** Who or what creates the event?
2. **Stimulus:** What happens?
3. **Environment:** Under which operating condition?
4. **Artifact:** Which system responsibility or information is affected?
5. **Response:** What must the system do?
6. **Response measure:** How well, how often, or how quickly?

Template:

```text
When [source] produces [stimulus]
during [environment],
[artifact] must [response],
measured by [threshold, population, unit, and window].
```

### Example

> When an authorized operator approves a route-disruption alert during the
> morning peak, the rider-facing alert responsibility makes that version
> observable to eligible journey requests, measured as 99% within two minutes
> and 99.9% within five minutes over a rolling 28-day window.

This scenario identifies work, urgency, and measurement. It still leaves
several mechanisms open.

## Scenarios are architectural test cases

A functional use case asks whether an operator can approve an alert. A quality
scenario asks how the system behaves when approval occurs during peak load,
when a channel is slow, or when a regional operator account is compromised.

Scenarios reveal:

- Critical paths and queues
- Required redundancy or degradation
- Authorization and audit boundaries
- Observability needs
- Repair and recovery
- Cost and staffing consequences

They also reveal impossible combinations. Zero cost, zero latency, no downtime,
instant global consistency, and unlimited scale cannot all be independent
requirements.

## Write the measure carefully

Include:

- Population or eligibility rule
- Numerator and denominator when using a ratio
- Percentile when using a distribution
- Threshold and unit
- Time window
- Measurement location
- Known blind spots

Weak:

> Alerts load in under 200 ms.

Stronger:

> For eligible rider alert-view attempts during normal operation, 95% complete
> within 200 ms and 99% within 800 ms as measured at the client over a rolling
> 28-day window, excluding user cancellations and including dependency errors.

The stronger statement may still change after measurement. It is precise enough
to challenge.

### Specification versus implementation

An indicator specification states what outcome matters. An implementation
states how it is measured.

```text
Specification:
  Ratio of rider alert views showing the latest approved version within 2 min.

Implementation A:
  Join client view events to approved alert versions.

Implementation B:
  Probe the public alert endpoint from each supported region.
```

Implementation A may have client-event loss. Implementation B may not represent
real user devices. Record coverage, quality, and cost.

## Five scenario families for the baseline

### Performance

Name the operation mix, concurrency or load, and response distribution. Avoid
averages when the user experiences tail latency.

### Overload

Name what is rejected, queued, degraded, or protected after a finite resource
saturates. “Auto-scale” is a mechanism, not an overload policy.

### Availability

Define useful success from the user’s viewpoint. Partial success and stale
responses require explicit classification.

### Recovery

Name the fault, authoritative data exposure, recovery time, recovery point, and
proof from a restoration or failover exercise.

### Security and tenant isolation

Name the actor, attempted action, protected object, decision, audit response,
and allowed error rate. For isolation, a single cross-tenant success is usually
an invariant violation rather than a small error budget.

## Prioritize with business impact

Do not make every scenario top priority. Rank by:

- User or business impact
- Invariant exposure
- Frequency or credible likelihood
- Recovery difficulty
- Decision influence
- Evidence uncertainty

A simple utility tree can group and rank scenarios:

```text
Trusted rider information
├── Freshness
│   ├── Approved alert visible in 2 min [High impact, Medium uncertainty]
│   └── Revocation visible in 1 min [High impact, High uncertainty]
├── Availability
│   └── Journey lookup during channel outage [Medium, Medium]
└── Security
    └── Regional operator cannot approve outside region [High, Low]
```

The ranking directs review effort. It does not calculate an architecture.

## Worked example: Transit Signal

### Vague requirement

> The platform must be resilient.

### Scenario

> When one downstream notification channel stops accepting work during a
> citywide disruption, the authoritative alert workflow continues accepting
> authorized updates and rider journey lookups continue showing the current
> alert, while channel work remains bounded; measured as no lost authoritative
> update, 99% successful journey lookups over the incident window, and a backlog
> that can be cleared within 30 minutes after recovery.

### Architectural questions exposed

- Is channel delivery on the approval critical path?
- What queue or concurrency bound exists?
- What is the authoritative acceptance point?
- Can the channel rebuild missed work?
- How is backlog age measured?
- Which cost buys the 30-minute recovery?

One scenario generated a review agenda.

## Common expert mistakes

### Treating the quality name as a scenario

“99.9% available” still lacks eligible operations, success definition,
environment, measurement location, and window.

### Choosing a target because it sounds professional

Every additional nine changes engineering and operating cost. Connect targets
to user harm and budget.

### Excluding failures from the denominator without reason

Exclusions can turn an indicator into a report of the system only when it
works. State why each excluded event is not a service responsibility.

### Writing a scenario around a chosen mechanism

“When load rises, Kubernetes adds pods” tests a product configuration. State
the user-visible overload response first.

### Ignoring conflicts

Encryption, audit detail, consistency, low latency, cost, and modifiability can
pull in different directions. Record the trade-off rather than claiming every
quality improves.

## Guided practice

Complete [EX-06](../exercises/exercises.md#ex-06-six-part-quality-scenarios).
Write one scenario in each baseline family and identify the likely conflict
between two of them.

## Self-check

1. What are the six parts of a quality scenario?
2. Why is a scenario different from a use case?
3. What is missing from “99.99% availability”?
4. Why separate an indicator specification from its implementation?
5. How does a quality scenario influence architecture without naming a design?

## Explained answers

1. Stimulus source, stimulus, environment, artifact, response, and response
   measure.
2. A use case describes functional interaction. A scenario probes how a system
   responds under a quality-relevant condition such as load, fault, attack, or
   change.
3. The eligible population, success definition, environment, measurement
   location, time window, and handling of partial or stale results.
4. The outcome can remain stable while measurement changes. Separating them
   exposes implementation blind spots and avoids optimizing the easiest metric.
5. It defines observable behavior and constraints that candidate mechanisms
   must explain and support.

## Sources and next work

- CMU SEI, “Reasoning About Software Quality Attributes” (RES-01)
- CMU SEI Quality Attribute Workshop webcast (RES-02)
- Google SRE Workbook, “Implementing SLOs” (RES-03)
- Next: [Lesson 5](05-context-and-boundaries.md)
- RES-08 -- ISO/IEC 25010:2023 Product quality model, for the local mechanism boundary.
