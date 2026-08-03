# Module 12 Resource Guide

All required sources are free. Local lessons are complete alternatives, so an
inaccessible external source does not block the module. Verification dates
record URL and access checks, not endorsement of every provider-specific choice.

## Week 45

### RES-01: Implementing SLOs

- Author/publisher: Steven Thurgood, David Ferguson, Alex Hidalgo, Betsy Beyer;
  Google Site Reliability Engineering
- URL: https://sre.google/workbook/implementing-slos/
- Type/access: practitioner book chapter, required, free
- Boundary/time: “Getting Started” through “Decision Making Using SLOs and
  Error Budgets,” 80 minutes
- Purpose: derive a user-centered SLO, budget, owner, and decision policy
- Evidence: one SLI specification, budget calculation, and policy action
- Reflection: Which exclusion could make the SLI look healthy while users fail?
- Local alternative: Lesson 1 and Lesson 2
- Last verified: 2026-08-02

### RES-02: Alerting on SLOs

- Author/publisher: Google Site Reliability Engineering
- URL: https://sre.google/workbook/alerting-on-slos/
- Type/access: practitioner book chapter, required, free
- Boundary/time: approaches 4–6 plus “Low-Traffic Services,” 70 minutes
- Purpose: derive burn-rate windows, notification class, and reset behavior
- Evidence: recalculate one page and one ticket threshold; test a low-traffic case
- Reflection: What action makes the page worth waking a human?
- Local alternative: Lesson 3
- Last verified: 2026-08-02

## Week 46

### RES-03: Managing Load

- Author/publisher: Google Site Reliability Engineering
- URL: https://sre.google/workbook/managing-load/
- Type/access: practitioner book chapter, required, free
- Boundary/time: load balancing, autoscaling, load shedding, combined
  strategies, and conclusions, 65 minutes
- Purpose: reason about feedback between controls and reserve after failure
- Evidence: one interaction diagram and a degraded-capacity calculation
- Reflection: Which control can make another control's signal misleading?
- Local alternative: Lesson 4
- Last verified: 2026-08-02

## Week 47

### RES-04: Incident Response

- Author/publisher: Google Site Reliability Engineering
- URL: https://sre.google/workbook/incident-response/
- Type/access: first-person engineering cases, required, free
- Boundary/time: complete chapter including the power-outage case, 75 minutes
- Purpose: separate command, operations, communications, and coordination
- Evidence: role map, first three mitigations, and one handoff contract
- Reflection: Which missing role would extend user impact in your system?
- Local alternative: Lesson 5
- Last verified: 2026-08-02

### RES-05: Postmortem Culture: Learning from Failure

- Author/publisher: Daniel Rogers et al.; Google Site Reliability Engineering
- URL: https://sre.google/workbook/postmortem-culture/
- Type/access: first-person engineering case and guidance, required, free
- Boundary/time: case comparison, action items, incentives, and tools, 70 minutes
- Purpose: write causal, measurable, owned corrective work without blame
- Evidence: rewrite three weak findings and rank five actions
- Reflection: Which action verifies risk reduction instead of merely adding work?
- Local alternative: Lesson 6
- Last verified: 2026-08-02

### RES-06: Contingency Planning Guide for Federal Information Systems

- Author/publisher: National Institute of Standards and Technology
- URL: https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-34r1.pdf
- Type/access: standards-body guidance, required, free
- Boundary/time: Sections 3.2, 3.5, 4.3, and 4.4, 90 minutes
- Purpose: connect business impact, recovery order, exercises, validation, and
  reconstitution while separating general guidance from local requirements
- Evidence: recovery priority table, exercise charter, and reconstitution checks
- Reflection: Which resource or access dependency would invalidate the plan?
- Local alternative: Lesson 7 and Lesson 8
- Last verified: 2026-08-02

## Week 48

### RES-07: Preparedness and Disaster Testing

- Author/publisher: Google Site Reliability Engineering
- URL: https://sre.google/sre-book/lessons-learned/
- Type/access: first-person engineering experience, required, free
- Boundary/time: “Preparedness and Disaster Testing” and DiRT discussion, 40 minutes
- Purpose: design exercises that reveal unknown weaknesses without uncontrolled harm
- Evidence: game-day hypothesis, abort conditions, and evidence plan
- Reflection: Which result would prove the exercise itself was unsafe?
- Local alternative: Lesson 8
- Last verified: 2026-08-02

### RES-08: Incident Management with Adrienne Walcer

- Author/publisher: Google SRE Prodcast
- URL: https://sre.google/prodcast/transcripts/sre-prodcast-01-08/
- Type/access: recorded practitioner interview with HTML transcript, required, free
- Boundary/time: complete episode or transcript, 45 minutes
- Purpose: hear incident coordination decisions and transfer them into a runbook
- Evidence: communication cadence, role boundaries, and two practice prompts
- Reflection: What must be decided before the pager fires?
- Written equivalent: the HTML transcript at the same URL and Lesson 5
- Last verified: 2026-08-02

## Optional enrichment

- Colette Alexander, USENIX SREcon26 Americas, “Three Lies We Tell Ourselves
  about Disaster Recovery and What to Do about Them.” Use the slides to
  challenge one comfortable assumption in the disaster-recovery review.
