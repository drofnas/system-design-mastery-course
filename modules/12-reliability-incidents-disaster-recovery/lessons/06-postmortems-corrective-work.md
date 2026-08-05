---
lesson_id: L06
title: "Postmortems and Corrective Work"
---

# Postmortems and Corrective Work

## Outcomes

- Quantify impact and reconstruct a cited timeline.
- Separate trigger, contributing conditions, causal evidence, and uncertainty.
- Rank corrective actions by expected exposure reduction and verification.

## Prerequisites

Lesson 5 and an immutable incident record.

## Analysis procedure

Start with user and data impact: journey failures, budget consumed, duration,
population, data exposure, and uncertainty. Build the timeline from raw events,
not recollection alone. Mark detection, declaration, mitigation, recovery, and
normalization separately.

The trigger begins the incident. Contributing conditions enlarge probability,
blast radius, or duration. A causal claim needs evidence that discriminates it
from another plausible explanation. “Human error” is not a stopping point;
identify why the system permitted, amplified, or failed to detect the action.

Corrective actions need an owner, risk addressed, expected reduction, effort,
confidence, due date, and verifiable end state. Rank using the same drivers.
Documentation and dashboards may help but do not outrank controls that prevent
or bound the demonstrated failure without evidence.

## Worked example

Northstar records 27 minutes of elevated catalog failures and 18% budget burn.
The trigger is a dependency release. Unbounded enrichment concurrency and
missing priority admission amplify impact. Slow declaration extends duration.
The postmortem ranks a concurrency bound and degradation test above a new
dashboard because paired evidence shows the controls reduce failed journeys.

## Common expert mistakes

- **Tell a heroic story:** individual effort replaces system learning.
- **Name one root cause:** interacting conditions and organizational gaps vanish.
- **List every idea:** ownerless actions dilute the highest-risk work.
- **Use MTTR alone:** detection, mitigation, recovery, data exposure, and users
  are collapsed into one ambiguous number.
- **Hide uncertainty:** estimates appear stronger than evidence.

## Guided practice

Given an immutable archive incident timeline, classify trigger and five
contributing conditions. Falsify one attractive causal claim. Rank six actions
by expected exposure reduction, effort, confidence, owner, and verification.

## Self-check

1. Why distinguish mitigation from resolution?
2. What makes an action measurable?
3. Is blamelessness the absence of accountability?

## Explained answers

1. User impact can stop before the fault and unsafe conditions are repaired.
2. It has a testable end state tied to the risk, not merely “improve” or “review.”
3. No. It directs accountability toward owned system and organizational changes
   without using blame as a substitute for causal analysis.

## Sources and next work

Study RES-05, complete EX-12–EX-13, and use the incident-postmortem template.
Preserve raw evidence and write later corrections as dated addenda.
