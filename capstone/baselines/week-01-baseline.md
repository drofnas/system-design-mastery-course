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

## 2. Functional scope and non-goals

### In scope

<!-- List the user-visible and business behaviors included in this baseline.
Use domain language, not components or technologies. -->

-

### Non-goals

<!-- List related behavior intentionally excluded from the current planning
horizon. Explain why each exclusion is safe and does not hide a required
invariant. -->

| Non-goal | Reason excluded | Condition that would bring it into scope |
|---|---|---|
| | | |

## 3. Workload model

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

### Sensitivity

<!-- Which two or three uncertain inputs could change the first design? Show a
low/base/high range and the resulting workload difference. -->

| Input | Low | Base | High | Decision affected |
|---|---:|---:|---:|---|
| | | | | |

## 4. Assumptions and constraints

Classify each statement. A constraint removes a choice in the current scope; an
assumption is an unverified planning claim; a preference can be traded.

| ID | Statement | Type | Source/owner | Confidence | Consequence if false | Test or review date |
|---|---|---|---|---|---|---|
| AC-01 | | | | | | |

### Explicit facts

<!-- Record relevant facts supported by inspectable evidence. -->

| Fact | Evidence | Date verified |
|---|---|---|
| | | |

## 5. Cost boundaries

Use ranges when evidence is weak. Include human and operating cost, not only
infrastructure.

| Cost area | Boundary or target | Unit/window | Evidence status | Consequence if exceeded |
|---|---|---|---|---|
| Delivery team and calendar | | | | |
| Build or migration effort | | | | |
| Recurring infrastructure/vendor | | | | |
| Cost per useful outcome | | | | |
| On-call and incident load | | | | |
| Security/compliance operation | | | | |
| Recovery/degraded capacity | | | | |

## 6. Decision drivers

Rank five to seven facts, outcomes, invariants, scenarios, constraints, costs, or
risks that should distinguish candidate designs.

| Rank | Driver | Evidence | Consequence if unmet |
|---:|---|---|---|
| 1 | | | |

## 7. Invariants

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

## 8. Quality-attribute scenarios

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

## 9. Failure and overload model

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

<!-- Which faults are not covered by this first design? For each, state the user
or business consequence and who accepts the risk. -->

| Excluded fault | Consequence | Risk owner | Revisit condition |
|---|---|---|---|
| | | | |

## 10. System context

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

## 11. State ownership

Identify the authority for each business fact. Do not choose storage products.

| Business state | Authoritative owner | Allowed writers | Readers or derived copies | Repair/rebuild rule | Retention or residency constraint |
|---|---|---|---|---|---|
| | | | | | |

## 12. Simplest design believed to work

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

## 13. Strongest arguments

| For this design | Against this design |
|---|---|
| | |
| | |
| | |

## 14. Open questions

| Question | Why it matters | Evidence needed | Owner/decision date |
|---|---|---|---|
| | | | |

## 15. Reversal evidence

For the most consequential assumptions or design choices, state the evidence
that should trigger reconsideration. Do not write “when we scale.”

| Current claim or choice | Original driver | Measurable reversal condition | Credible migration seam |
|---|---|---|---|
| | | | |

## 16. Self-check before freezing

- [ ] Functional scope and explicit non-goals are stated.
- [ ] Workloads have numbers, units, time windows, and labeled assumptions.
- [ ] Workload sensitivity identifies decision-changing uncertainty.
- [ ] Constraints, assumptions, facts, and preferences are distinguished.
- [ ] Delivery, recurring, operational, security, and recovery cost boundaries exist.
- [ ] Five to seven decision drivers are ranked.
- [ ] At least ten invariants are independently testable.
- [ ] At least five quality scenarios have measurable thresholds.
- [ ] The five required failure scenarios have predicted behavior.
- [ ] Excluded faults state consequences and risk owners.
- [ ] The context diagram names actors, boundaries, and flows.
- [ ] Every important business fact has an authority and repair rule.
- [ ] The design avoids vendor, framework, database, broker, and service names.
- [ ] The strongest arguments for and against the design are recorded.
- [ ] Open questions have evidence, owners, and decision dates.
- [ ] Material choices include measurable reversal conditions and migration seams.
- [ ] `completed_on` and `status` are updated before the freeze commit.

## 17. AI assistance disclosure

- Template supplied with AI assistance: yes
- Design content supplied by AI before baseline freeze: no
- Other tools used:
- Verification performed:
