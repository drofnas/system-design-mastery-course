# M12 Quiz Answer Key

This key covers all 100 questions for **Reliability, Incidents, and Disaster Recovery**. Use it after an attempt, or provide it with the LLM grading prompt for feedback.

## M12-Q001

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to define user-journey slis and slos with valid populations, windows, exclusions, latency, availability, freshness, and correctness.

**Explanation:** Use User Journeys, SLIs, and SLOs to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M12-Q002

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Error Budgets, Dependencies, and Composite Reliability', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Error Budgets, Dependencies, and Composite Reliability to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M12-Q003

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. - Calculate burn rate from observed error fraction and SLO error fraction.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M12-Q004

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Call errors degradation:** no priority or minimum-useful contract exists.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M12-Q005

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for run incidents with explicit command, operations, communications, liaison, handoff, escalation, and stop conditions..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. Study RES-04 and RES-08, complete EX-10–EX-11, and preserve the incident timeline as raw evidence for the postmortem rather than rewriting it afterward.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M12-Q006

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to produce an evidence-based postmortem and rank corrective work by risk reduction, effort, ownership, and verification.

**Explanation:** Use Postmortems and Corrective Work to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M12-Q007

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Backups, Restore, Failover, and Failback', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Backups, Restore, Failover, and Failback to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M12-Q008

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. - Design a controlled game day with hypothesis, safety, and evidence.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M12-Q009

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Measure component uptime:** users can fail while every process responds.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M12-Q010

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for calculate error budgets, burn, dependency exposure, shared fate, and composite reliability and use them in decisions..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. Complete EX-03–EX-05 and carry the dependency/common-cause model into Lesson 3.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M12-Q011

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to implement multi-window burn alerts and separate actionable journey symptoms from causal diagnostic telemetry.

**Explanation:** Use Burn Rates and Actionable Alerting to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M12-Q012

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Graceful Degradation and Degraded Capacity', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Graceful Degradation and Degraded Capacity to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M12-Q013

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. - Separate incident command, operations, communications, and liaison roles.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M12-Q014

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Tell a heroic story:** individual effort replaces system learning.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M12-Q015

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for verify backup integrity, rpo, rto, restore, failover, fencing, reconciliation, and failback with controlled evidence..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. Study RES-06, complete EX-14–EX-15, and preserve F05–F09 recovery versions, timestamps, epochs, hashes, approvals, and reconciliation as raw evidence.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M12-Q016

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to diagnose nine reliability failures and defend cumulative review across consensus, messaging, operations, security, cost, ownership, and recovery.

**Explanation:** Use Chaos, Game Days, and Reliability Decisions to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M12-Q017

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'User Journeys, SLIs, and SLOs', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use User Journeys, SLIs, and SLOs to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M12-Q018

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. - Calculate allowed bad events and consumed error budget.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M12-Q019

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Page at the SLO threshold:** noise arrives faster than useful action.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M12-Q020

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for build priority-aware degradation, load shedding, bounded dependency work, and degraded regional capacity..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. Study RES-03, complete EX-08–EX-09, implement the public lab contract, and record capacity predictions before running F01 or F07.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M12-Q021

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to run incidents with explicit command, operations, communications, liaison, handoff, escalation, and stop conditions.

**Explanation:** Use Incident Command, Communication, and Runbooks to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M12-Q022

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Postmortems and Corrective Work', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Postmortems and Corrective Work to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M12-Q023

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. - Derive RPO and RTO from user/data consequence and measured evidence.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M12-Q024

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Inject chaos without a hypothesis:** spectacle replaces learning.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M12-Q025

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for define user-journey slis and slos with valid populations, windows, exclusions, latency, availability, freshness, and correctness..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. Study RES-01, complete EX-01–EX-02, and save the Week 45 SLI population before opening the Northstar case or answer key.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M12-Q026

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to calculate error budgets, burn, dependency exposure, shared fate, and composite reliability and use them in decisions.

**Explanation:** Use Error Budgets, Dependencies, and Composite Reliability to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M12-Q027

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Burn Rates and Actionable Alerting', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Burn Rates and Actionable Alerting to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M12-Q028

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. - Define a priority order and user-visible degraded contract.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M12-Q029

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Best debugger commands:** coordination and impact become ownerless.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M12-Q030

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for produce an evidence-based postmortem and rank corrective work by risk reduction, effort, ownership, and verification..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. Study RES-05, complete EX-12–EX-13, and use the incident-postmortem template.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M12-Q031

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to verify backup integrity, rpo, rto, restore, failover, fencing, reconciliation, and failback with controlled evidence.

**Explanation:** Use Backups, Restore, Failover, and Failback to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M12-Q032

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Chaos, Game Days, and Reliability Decisions', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Chaos, Game Days, and Reliability Decisions to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M12-Q033

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. - Specify valid and good events for a complete user journey.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M12-Q034

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Subtract percentages:** budget is computed against valid events or time.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M12-Q035

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for implement multi-window burn alerts and separate actionable journey symptoms from causal diagnostic telemetry..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. Study RES-02, complete EX-06–EX-07, and test the alert series before building degraded modes in Lesson 4.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M12-Q036

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to build priority-aware degradation, load shedding, bounded dependency work, and degraded regional capacity.

**Explanation:** Use Graceful Degradation and Degraded Capacity to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M12-Q037

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Incident Command, Communication, and Runbooks', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Incident Command, Communication, and Runbooks to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M12-Q038

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. - Quantify impact and reconstruct a cited timeline.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M12-Q039

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Replica equals backup:** corruption or operator error can propagate.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M12-Q040

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for diagnose nine reliability failures and defend cumulative review across consensus, messaging, operations, security, cost, ownership, and recovery..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. Study RES-07, complete EX-16, finalize the disaster-recovery review, conduct the defense, save cumulative review in Week 68, and write the separate Week 69 synthesis project delta.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M12-Q041

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to define user-journey slis and slos with valid populations, windows, exclusions, latency, availability, freshness, and correctness.

**Explanation:** Use User Journeys, SLIs, and SLOs to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M12-Q042

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Error Budgets, Dependencies, and Composite Reliability', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Error Budgets, Dependencies, and Composite Reliability to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M12-Q043

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. - Calculate burn rate from observed error fraction and SLO error fraction.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M12-Q044

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Call errors degradation:** no priority or minimum-useful contract exists.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M12-Q045

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for run incidents with explicit command, operations, communications, liaison, handoff, escalation, and stop conditions..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. Study RES-04 and RES-08, complete EX-10–EX-11, and preserve the incident timeline as raw evidence for the postmortem rather than rewriting it afterward.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M12-Q046

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to produce an evidence-based postmortem and rank corrective work by risk reduction, effort, ownership, and verification.

**Explanation:** Use Postmortems and Corrective Work to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M12-Q047

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Backups, Restore, Failover, and Failback', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Backups, Restore, Failover, and Failback to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M12-Q048

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. - Design a controlled game day with hypothesis, safety, and evidence.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M12-Q049

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Measure component uptime:** users can fail while every process responds.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M12-Q050

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for calculate error budgets, burn, dependency exposure, shared fate, and composite reliability and use them in decisions..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. Complete EX-03–EX-05 and carry the dependency/common-cause model into Lesson 3.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M12-Q051

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to implement multi-window burn alerts and separate actionable journey symptoms from causal diagnostic telemetry.

**Explanation:** Use Burn Rates and Actionable Alerting to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M12-Q052

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Graceful Degradation and Degraded Capacity', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Graceful Degradation and Degraded Capacity to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M12-Q053

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. - Separate incident command, operations, communications, and liaison roles.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M12-Q054

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Tell a heroic story:** individual effort replaces system learning.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M12-Q055

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for verify backup integrity, rpo, rto, restore, failover, fencing, reconciliation, and failback with controlled evidence..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. Study RES-06, complete EX-14–EX-15, and preserve F05–F09 recovery versions, timestamps, epochs, hashes, approvals, and reconciliation as raw evidence.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M12-Q056

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to diagnose nine reliability failures and defend cumulative review across consensus, messaging, operations, security, cost, ownership, and recovery.

**Explanation:** Use Chaos, Game Days, and Reliability Decisions to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M12-Q057

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'User Journeys, SLIs, and SLOs', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use User Journeys, SLIs, and SLOs to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M12-Q058

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. - Calculate allowed bad events and consumed error budget.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M12-Q059

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Page at the SLO threshold:** noise arrives faster than useful action.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M12-Q060

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for build priority-aware degradation, load shedding, bounded dependency work, and degraded regional capacity..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. Study RES-03, complete EX-08–EX-09, implement the public lab contract, and record capacity predictions before running F01 or F07.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M12-Q061

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to run incidents with explicit command, operations, communications, liaison, handoff, escalation, and stop conditions.

**Explanation:** Use Incident Command, Communication, and Runbooks to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M12-Q062

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Postmortems and Corrective Work', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Postmortems and Corrective Work to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M12-Q063

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. - Derive RPO and RTO from user/data consequence and measured evidence.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M12-Q064

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Inject chaos without a hypothesis:** spectacle replaces learning.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M12-Q065

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for define user-journey slis and slos with valid populations, windows, exclusions, latency, availability, freshness, and correctness..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. Study RES-01, complete EX-01–EX-02, and save the Week 45 SLI population before opening the Northstar case or answer key.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M12-Q066

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to calculate error budgets, burn, dependency exposure, shared fate, and composite reliability and use them in decisions.

**Explanation:** Use Error Budgets, Dependencies, and Composite Reliability to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M12-Q067

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Burn Rates and Actionable Alerting', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Burn Rates and Actionable Alerting to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M12-Q068

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. - Define a priority order and user-visible degraded contract.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M12-Q069

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Best debugger commands:** coordination and impact become ownerless.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M12-Q070

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for produce an evidence-based postmortem and rank corrective work by risk reduction, effort, ownership, and verification..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. Study RES-05, complete EX-12–EX-13, and use the incident-postmortem template.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M12-Q071

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to verify backup integrity, rpo, rto, restore, failover, fencing, reconciliation, and failback with controlled evidence.

**Explanation:** Use Backups, Restore, Failover, and Failback to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M12-Q072

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Chaos, Game Days, and Reliability Decisions', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Chaos, Game Days, and Reliability Decisions to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M12-Q073

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. - Specify valid and good events for a complete user journey.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M12-Q074

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Subtract percentages:** budget is computed against valid events or time.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M12-Q075

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for implement multi-window burn alerts and separate actionable journey symptoms from causal diagnostic telemetry..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. Study RES-02, complete EX-06–EX-07, and test the alert series before building degraded modes in Lesson 4.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M12-Q076

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to build priority-aware degradation, load shedding, bounded dependency work, and degraded regional capacity.

**Explanation:** Use Graceful Degradation and Degraded Capacity to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M12-Q077

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Incident Command, Communication, and Runbooks', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Incident Command, Communication, and Runbooks to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M12-Q078

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. - Quantify impact and reconstruct a cited timeline.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M12-Q079

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Replica equals backup:** corruption or operator error can propagate.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M12-Q080

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for diagnose nine reliability failures and defend cumulative review across consensus, messaging, operations, security, cost, ownership, and recovery..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. Study RES-07, complete EX-16, finalize the disaster-recovery review, conduct the defense, save cumulative review in Week 68, and write the separate Week 69 synthesis project delta.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M12-Q081

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to define user-journey slis and slos with valid populations, windows, exclusions, latency, availability, freshness, and correctness.

**Explanation:** Use User Journeys, SLIs, and SLOs to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M12-Q082

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Error Budgets, Dependencies, and Composite Reliability', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Error Budgets, Dependencies, and Composite Reliability to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M12-Q083

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. - Calculate burn rate from observed error fraction and SLO error fraction.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M12-Q084

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Call errors degradation:** no priority or minimum-useful contract exists.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M12-Q085

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for run incidents with explicit command, operations, communications, liaison, handoff, escalation, and stop conditions..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. Study RES-04 and RES-08, complete EX-10–EX-11, and preserve the incident timeline as raw evidence for the postmortem rather than rewriting it afterward.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M12-Q086

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to produce an evidence-based postmortem and rank corrective work by risk reduction, effort, ownership, and verification.

**Explanation:** Use Postmortems and Corrective Work to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M12-Q087

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Backups, Restore, Failover, and Failback', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Backups, Restore, Failover, and Failback to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M12-Q088

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. - Design a controlled game day with hypothesis, safety, and evidence.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M12-Q089

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Measure component uptime:** users can fail while every process responds.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M12-Q090

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for calculate error budgets, burn, dependency exposure, shared fate, and composite reliability and use them in decisions..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. Complete EX-03–EX-05 and carry the dependency/common-cause model into Lesson 3.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M12-Q091

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to implement multi-window burn alerts and separate actionable journey symptoms from causal diagnostic telemetry.

**Explanation:** Use Burn Rates and Actionable Alerting to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M12-Q092

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Graceful Degradation and Degraded Capacity', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Graceful Degradation and Degraded Capacity to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M12-Q093

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. - Separate incident command, operations, communications, and liaison roles.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M12-Q094

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Tell a heroic story:** individual effort replaces system learning.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M12-Q095

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for verify backup integrity, rpo, rto, restore, failover, fencing, reconciliation, and failback with controlled evidence..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. Study RES-06, complete EX-14–EX-15, and preserve F05–F09 recovery versions, timestamps, epochs, hashes, approvals, and reconciliation as raw evidence.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M12-Q096

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to diagnose nine reliability failures and defend cumulative review across consensus, messaging, operations, security, cost, ownership, and recovery.

**Explanation:** Use Chaos, Game Days, and Reliability Decisions to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M12-Q097

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'User Journeys, SLIs, and SLOs', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use User Journeys, SLIs, and SLOs to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M12-Q098

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. - Calculate allowed bad events and consumed error budget.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M12-Q099

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Page at the SLO threshold:** noise arrives faster than useful action.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M12-Q100

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for build priority-aware degradation, load shedding, bounded dependency work, and degraded regional capacity..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. Study RES-03, complete EX-08–EX-09, implement the public lab contract, and record capacity predictions before running F01 or F07.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.
