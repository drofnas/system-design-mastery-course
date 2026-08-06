# M16 Quiz Answer Key

This key covers all 43 questions for **Browser, Frontend, CDN, and Edge Architecture**. Use it after an attempt, or provide it with the LLM grading prompt for feedback.

## M16-Q001

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** Its continuation runs as a microtask before the event loop can reach a rendering opportunity; a self-feeding microtask chain can keep delaying paint.

**Explanation:** M16-Q001 uses self-check 1 from Browser Work and the Rendering Pipeline; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M16-Q002

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** A compositor-supported change whose required properties and pixels are already available may reuse work, but the trace must confirm the path.

**Explanation:** M16-Q002 uses self-check 2 from Browser Work and the Rendering Pipeline; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M16-Q003

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** Transfer cost, queue bounds, cancellation, stale results, and ownership still determine whether the user journey and capacity are safe.

**Explanation:** M16-Q003 uses self-check 3 from Browser Work and the Rendering Pipeline; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M16-Q004

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** INP is derived from eligible interactions over page visits and reported at a field population percentile; the lab is one controlled observation.

**Explanation:** M16-Q004 uses self-check 4 from Browser Work and the Rendering Pipeline; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M16-Q005

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** Routes differ in critical content, interaction, personalization, rendering, cacheability, and client populations.

**Explanation:** M16-Q005 uses self-check 1 from Performance Budgets and Evidence; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M16-Q006

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** It can reject a change under equivalent controlled conditions; it cannot establish the population impact without field evidence.

**Explanation:** M16-Q006 uses self-check 2 from Performance Budgets and Evidence; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M16-Q007

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** Visits with no eligible interaction produce no INP; treating them as fast or dropping them silently changes the observed population.

**Explanation:** M16-Q007 uses self-check 3 from Performance Budgets and Evidence; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M16-Q008

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** The signal/window, owner, release or mitigation action, exception process, and reversal/expiry condition.

**Explanation:** M16-Q008 uses self-check 4 from Performance Budgets and Evidence; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M16-Q009

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** At minimum route existence/authorization, safe response headers, cache policy, and the error contract that cannot be expressed after commitment.

**Explanation:** M16-Q009 uses self-check 1 from Route Rendering and Hydration; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M16-Q010

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** Each island is still a hydration root whose server markup and initial client state must match.

**Explanation:** M16-Q010 uses self-check 2 from Route Rendering and Hydration; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M16-Q011

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** When browser-local state or interaction dominates and the route still has a useful, recoverable, accessible shell with bounded code/data dependencies.

**Explanation:** M16-Q011 uses self-check 3 from Route Rendering and Hydration; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M16-Q012

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** It does not prove useful content, interactivity, accessibility, correct status, completion, or failure recovery.

**Explanation:** M16-Q012 uses self-check 4 from Route Rendering and Hydration; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M16-Q013

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** Cookies are high-cardinality and sensitive, and a shared cache remains the wrong authority for subject access; bypass shared storage instead.

**Explanation:** M16-Q013 uses self-check 1 from HTTP and CDN Cache Safety; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M16-Q014

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** It identifies a selected representation for validation under its scope; it does not prove authorization or universal semantic freshness.

**Explanation:** M16-Q014 uses self-check 2 from HTTP and CDN Cache Safety; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M16-Q015

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Measure every callback data for review case one; limit the change.
- Measure promises free data for review case one; limit the change. with margin
- Measure reading flame data for review case one; limit the change.
- Measure forcing layout data for review case one; limit the change.

**Answer:** Measure every callback data for review case one; limit the change.

**Explanation:** M16-Q015 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects every callback as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M16-Q016

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Measure average frame data for review case two; limit the change.
- Measure promises free data for review case two; limit the change.
- Measure lighthouse score data for review case two; limit the change.
- Measure mixing cold data for review case two; limit the change.

**Answer:** Measure promises free data for review case two; limit the change.

**Explanation:** M16-Q016 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects promises free as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M16-Q017

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Measure reporting five data for review case three; limit the change.
- Measure milestone users data for review case three; limit the change.
- Measure reading flame data for review case three; limit the change.
- Measure telemetry overhead data for review case three; limit the change.

**Answer:** Measure reading flame data for review case three; limit the change.

**Explanation:** M16-Q017 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects reading flame as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M16-Q018

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Measure declaring whole data for review case four; limit the change.
- Measure streaming knowing data for review case four; limit the change.
- Measure suppressing hydration data for review case four; limit the change.
- Measure forcing layout data for review case four; limit the change.

**Answer:** Measure forcing layout data for review case four; limit the change.

**Explanation:** M16-Q018 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects forcing layout as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M16-Q019

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Measure average frame data for review case five; limit the change.
- Measure hydrating whole data for review case five; limit the change.
- Measure equating server data for review case five; limit the change.
- Measure keying only data for review case five; limit the change.

**Answer:** Measure average frame data for review case five; limit the change.

**Explanation:** M16-Q019 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects average frame as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M16-Q020

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Measure ttl deletion data for review case six; limit the change.
- Measure lighthouse score data for review case six; limit the change.
- Measure caching authorization data for review case six; limit the change.
- Measure purge instantaneous data for review case six; limit the change.

**Answer:** Measure lighthouse score data for review case six; limit the change.

**Explanation:** M16-Q020 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects lighthouse score as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M16-Q021

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Measure serving stale data for review case seven; limit the change.
- Measure aria recreate data for review case seven; limit the change.
- Measure mixing cold data for review case seven; limit the change.
- Measure moving focus data for review case seven; limit the change.

**Answer:** Measure mixing cold data for review case seven; limit the change.

**Explanation:** M16-Q021 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects mixing cold as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M16-Q022

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Measure loading skeletons data for review case eight; limit the change.
- Measure only happy data for review case eight; limit the change.
- Measure accepting automated data for review case eight; limit the change.
- Measure reporting five data for review case eight; limit the change.

**Answer:** Measure reporting five data for review case eight; limit the change.

**Explanation:** M16-Q022 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects reporting five as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M16-Q023

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Measure milestone users data for review case nine; limit the change.
- Measure high heap data for review case nine; limit the change. with margin
- Measure measuring only data for review case nine; limit the change.
- Measure loading third data for review case nine; limit the change.

**Answer:** Measure milestone users data for review case nine; limit the change.

**Explanation:** M16-Q023 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects milestone users as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M16-Q024

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Measure putting sensitive data for review case ten; limit the change.
- Measure telemetry overhead data for review case ten; limit the change.
- Measure trusting browser data for review case ten; limit the change.
- Measure model timing data for review case ten; limit the change. with margin

**Answer:** Measure telemetry overhead data for review case ten; limit the change.

**Explanation:** M16-Q024 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects telemetry overhead as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M16-Q025

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** Calculation for browser work and the rendering pipeline, serialization is 110 x 8 / 900 = 0.98 s; RTT adds 360 ms, for about 1338 ms.

**Explanation:** M16-Q025 uses frontend shell delivery from Browser Work and the Rendering Pipeline and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M16-Q026

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** Calculation for performance budgets and evidence, it exceeds the budget by 220 - 100 = 120 ms.

**Explanation:** M16-Q026 uses interaction block from Performance Budgets and Evidence and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M16-Q027

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** Calculation for route rendering and hydration, serialization is 280 KiB x 8 / 900 Kbps = 2.49 seconds, ignoring protocol overhead.

**Explanation:** M16-Q027 uses serialization from Route Rendering and Hydration and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M16-Q028

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** Calculation for http and cdn cache safety, setup lower bound is 3 x 90 ms = 270 ms before payload work.

**Explanation:** M16-Q028 uses RTT setup from HTTP and CDN Cache Safety and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M16-Q029

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** Diagnosis for browser work and the rendering pipeline, accessibility.focus_preserved and cache.private_cache_entries separate the mechanism. accessibility.focus_preserved = 1 while cache.private_cache_entries = 0, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare accessibility.focus_preserved with cache.private_cache_entries and connect that contrast to browser work and the rendering pipeline.

**Grading notes:** Full credit names Browser Work and the Rendering Pipeline, cites accessibility.focus_preserved and cache.private_cache_entries, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M16-Q030

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** Diagnosis for performance budgets and evidence, accessibility.keyboard_path and cache.private_cache_entries separate the mechanism. accessibility.keyboard_path = 1 while cache.private_cache_entries = 0, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare accessibility.keyboard_path with cache.private_cache_entries and connect that contrast to performance budgets and evidence.

**Grading notes:** Full credit names Performance Budgets and Evidence, cites accessibility.keyboard_path and cache.private_cache_entries, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M16-Q031

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** Diagnosis for route rendering and hydration, accessibility.focus_preserved and cache.degraded_marked separate the mechanism. accessibility.focus_preserved = 0 while cache.degraded_marked = 1, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare accessibility.focus_preserved with cache.degraded_marked and connect that contrast to route rendering and hydration.

**Grading notes:** Full credit names Route Rendering and Hydration, cites accessibility.focus_preserved and cache.degraded_marked, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M16-Q032

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** Diagnosis for http and cdn cache safety, accessibility.semantic_structure and cache.private_cache_entries separate the mechanism. accessibility.semantic_structure = 1 while cache.private_cache_entries = 0, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare accessibility.semantic_structure with cache.private_cache_entries and connect that contrast to http and cdn cache safety.

**Grading notes:** Full credit names HTTP and CDN Cache Safety, cites accessibility.semantic_structure and cache.private_cache_entries, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M16-Q033

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** Diagnosis for accessibility and resilient interaction, cache.degraded_marked and cache.private_cache_entries separate the mechanism. cache.degraded_marked = 1 while cache.private_cache_entries = 0, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare cache.degraded_marked with cache.private_cache_entries and connect that contrast to accessibility and resilient interaction.

**Grading notes:** Full credit names Accessibility and Resilient Interaction, cites cache.degraded_marked and cache.private_cache_entries, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M16-Q034

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** Diagnosis for memory, third parties, and observability, accessibility.focus_preserved and cache.private_cache_entries separate the mechanism. accessibility.focus_preserved = 1 while cache.private_cache_entries = 0, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare accessibility.focus_preserved with cache.private_cache_entries and connect that contrast to memory, third parties, and observability.

**Grading notes:** Full credit names Memory, Third Parties, and Observability, cites accessibility.focus_preserved and cache.private_cache_entries, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M16-Q035

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** Diagnosis for northstar browser-edge tutorial, accessibility.keyboard_path and cache.private_cache_entries separate the mechanism. accessibility.keyboard_path = 1 while cache.private_cache_entries = 0, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare accessibility.keyboard_path with cache.private_cache_entries and connect that contrast to northstar browser-edge tutorial.

**Grading notes:** Full credit names Northstar Browser-Edge Tutorial, cites accessibility.keyboard_path and cache.private_cache_entries, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M16-Q036

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** Diagnosis for frontend-edge decision and teach-back, accessibility.manual_boundary_recorded and cache.private_cache_entries separate the mechanism. accessibility.manual_boundary_recorded = 1 while cache.private_cache_entries = 0, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare accessibility.manual_boundary_recorded with cache.private_cache_entries and connect that contrast to frontend-edge decision and teach-back.

**Grading notes:** Full credit names Frontend-Edge Decision and Teach-Back, cites accessibility.manual_boundary_recorded and cache.private_cache_entries, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M16-Q037

**Type:** `design_judgment`
**Difficulty:** `application`

**Answer:** Approve Interaction trace at 152.2/s. The deciding number is 228 x 0.72 = 164.2/s, leaving 12/s before the reserve is consumed. Withdraw approval if a drill, trace, or workload sample shows interaction trace demand above 164.2/s or proves the shed point cannot protect lower-priority work.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to interaction trace demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 164.2/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M16-Q038

**Type:** `design_judgment`
**Difficulty:** `synthesis`

**Answer:** Decline One-control long-task pair at 187.8/s. The deciding number is 245 x 0.72 = 176.4/s, so planned demand exceeds the usable region by 11.4/s. Approve later if repeated measurements lift usable capacity above 187.8/s or a named policy removes at least 11.4/s of deferrable work before saturation.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to one-control long-task pair demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 176.4/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M16-Q039

**Type:** `design_judgment`
**Difficulty:** `recall`

**Answer:** Approve conditionally for Critical-path calculation. The deciding number is 262 x 0.72 = 188.6/s, and 183.6/s fits only while the fallback remains enforceable. Keep the condition until recovery traffic, priority demand, or fallback tests show less than 5/s of usable margin.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to critical-path calculation demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 188.6/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M16-Q040

**Type:** `design_judgment`
**Difficulty:** `application`

**Answer:** Approve Evidence classification at 183.8/s. The deciding number is 279 x 0.72 = 200.9/s, leaving 17.1/s before the reserve is consumed. Require redesign if a drill, trace, or workload sample shows evidence classification demand above 200.9/s or proves the shed point cannot protect lower-priority work.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to evidence classification demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 200.9/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M16-Q041

**Type:** `design_judgment`
**Difficulty:** `synthesis`

**Answer:** Decline Route rendering matrix at 228.7/s. The deciding number is 296 x 0.72 = 213.1/s, so planned demand exceeds the usable region by 15.6/s. Lift the decline if repeated measurements lift usable capacity above 228.7/s or a named policy removes at least 15.6/s of deferrable work before saturation.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to route rendering matrix demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 213.1/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M16-Q042

**Type:** `design_judgment`
**Difficulty:** `recall`

**Answer:** Approve Streaming commitment at 204.9/s. The deciding number is 313 x 0.72 = 225.4/s, leaving 20.5/s before the reserve is consumed. Reverse the call if a drill, trace, or workload sample shows streaming commitment demand above 225.4/s or proves the shed point cannot protect lower-priority work.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to streaming commitment demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 225.4/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M16-Q043

**Type:** `design_judgment`
**Difficulty:** `application`

**Answer:** Decline Hydration identity at 256/s. The deciding number is 330 x 0.72 = 237.6/s, so planned demand exceeds the usable region by 18.4/s. Accept the proposal when repeated measurements lift usable capacity above 256/s or a named policy removes at least 18.4/s of deferrable work before saturation.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to hydration identity demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 237.6/s, compares it with planned demand, and names a scenario-specific reversal condition.
