---
title: "Week 1 Baseline: Global Commerce Platform"
course_week: 1
module: "Architectural Judgment"
author:
started_on:
completed_on:
status: draft
frozen_commit:
---

# Week 1 Baseline: Global Commerce Platform

> Complete this document independently before requesting architectural
> recommendations or AI critique. Use domain language only: do not name
> frameworks, cloud vendors, databases, brokers, or deployable service
> boundaries. Once completed and tagged `week-01-baseline`, never edit this
> file. Put all criticism and revisions in separate artifacts.

## 1. User journey and business outcome

### Primary user

<!-- Who is the primary user, and what are they trying to accomplish? -->

### User journey

<!-- Describe one end-to-end journey in user-visible steps. -->

### Measurable business outcome

<!-- Include a metric, target, population, and time window. -->

## 2. Workload model

Use explicit units and time windows. Distinguish measured facts from assumptions.

| Dimension | Normal | Peak | Burst | Projected | Unit and window | Evidence or assumption |
|---|---:|---:|---:|---:|---|---|
| Active shoppers | | | | | | |
| Browse/search operations | | | | | | |
| Checkout attempts | | | | | | |
| Product updates | | | | | | |
| Merchant ingestion | | | | | | |
| Assistant interactions | | | | | | |
| Stored products | | | | | | |
| Orders retained | | | | | | |
| Other: | | | | | | |

### Traffic shape and growth

<!-- Describe seasonality, regional distribution, skew, burst duration, and
growth horizon. -->

## 3. Invariants

Write at least ten statements that can be proven true or false. Avoid goals such
as "the system should be reliable."

| ID | Invariant | Event that could violate it | Observable proof |
|---|---|---|---|
| INV-01 | | | |
| INV-02 | | | |
| INV-03 | | | |
| INV-04 | | | |
| INV-05 | | | |
| INV-06 | | | |
| INV-07 | | | |
| INV-08 | | | |
| INV-09 | | | |
| INV-10 | | | |

## 4. Quality-attribute scenarios

Write at least five measurable scenarios. Each must name the stimulus,
environment, response, threshold, time window, and measurement method. Include
performance, overload, availability, recovery, and tenant-security scenarios.

| ID | Attribute | Stimulus and environment | Required response | Threshold and window | Measurement |
|---|---|---|---|---|---|
| QA-01 | Performance | | | | |
| QA-02 | Overload | | | | |
| QA-03 | Availability | | | | |
| QA-04 | Recovery | | | | |
| QA-05 | Tenant security | | | | |

## 5. Failure and overload model

Predict behavior before testing. Name excluded faults rather than implying that
the design covers every possible failure.

| Scenario | Scope and duration | Expected behavior | Invariant at risk | Detection or evidence |
|---|---|---|---|---|
| 10× traffic burst | | | | |
| One slow dependency | | | | |
| Stale data | | | | |
| Operator mistake | | | | |
| Loss of one hosting zone | | | | |
| Other: | | | | |

### Explicit exclusions

<!-- Which faults are not covered by this first design? -->

## 6. System context

Replace the placeholders with actors, the commerce platform boundary, and
external systems. Show information or command flow on each arrow.

```mermaid
flowchart LR
    U["<primary user>"]
    P["<commerce platform>"]
    E["<external system>"]
    U -->|"<request or information>"| P
    P -->|"<request or information>"| E
```

## 7. State ownership

Identify the authority for each business fact. Do not choose storage products.

| Business state | Authoritative owner | Readers or derived copies | Retention or residency constraint |
|---|---|---|---|
| | | | |

## 8. Simplest design believed to work

<!-- Explain the design in domain terms. State how requests, business state,
irreversible actions, and background work interact without naming technologies
or choosing deployable boundaries. -->

### Design diagram

```mermaid
flowchart LR
    A["<actor>"] --> B["<system responsibility>"]
```

### Why this is the simplest credible design

<!-- Identify what has intentionally not been added and why. -->

## 9. Strongest arguments

| For this design | Against this design |
|---|---|
| | |
| | |
| | |

## 10. Open questions

| Question | Why it matters | Evidence needed |
|---|---|---|
| | | |

## 11. Self-check before freezing

- [ ] Workloads have numbers, units, time windows, and labeled assumptions.
- [ ] At least ten invariants are independently testable.
- [ ] At least five quality scenarios have measurable thresholds.
- [ ] The five required failure scenarios have predicted behavior.
- [ ] The context diagram names actors, boundaries, and flows.
- [ ] Every important business fact has an authoritative owner.
- [ ] The design avoids vendor, framework, database, broker, and service names.
- [ ] The strongest arguments for and against the design are recorded.
- [ ] Open questions name the evidence needed to resolve them.
- [ ] `completed_on` and `status` are updated before the freeze commit.

## 12. AI assistance disclosure

- Template supplied with AI assistance: yes
- Design content supplied by AI before baseline freeze: no
- Other tools used:
- Verification performed:
