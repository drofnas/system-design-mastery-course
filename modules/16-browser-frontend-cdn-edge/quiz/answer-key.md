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

- Scope the M16 scoped measurement and record the limiting assumption before approving the change.
- Approve the platform contract uses tasks and for Browser Work and the Rendering Pipeline; the local context makes that proposal familiar enough for review.
- Defer measurement until production for the platform contract uses tasks and; the team can monitor Browser Work and the Rendering Pipeline after launch.
- Approve the M16 shortcut for alpha now.

**Answer:** Scope the M16 scoped measurement and record the limiting assumption before approving the change.

**Explanation:** M16-Q015 enacts mistake 1 from Browser Work and the Rendering Pipeline; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M16-Q016

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Approve promise continuations are for Browser Work and the Rendering Pipeline; the local context makes that proposal familiar enough for review.
- Measure the M16 scoped measurement before approving the change.
- Defer measurement until production for promise continuations are; the team can monitor Browser Work and the Rendering Pipeline after launch.
- Approve the M16 shortcut for bravo now.

**Answer:** Measure the M16 scoped measurement before approving the change.

**Explanation:** M16-Q016 enacts mistake 2 from Browser Work and the Rendering Pipeline; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M16-Q017

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Approve a long stack is evidence of time spent for Browser Work and the Rendering Pipeline; the local context makes that proposal familiar enough for review.
- Defer measurement until production for a long stack is evidence of time spent; the team can monitor Browser Work and the Rendering Pipeline after launch.
- Bound the M16 scoped measurement before approval.
- Approve the M16 shortcut for charlie now.

**Answer:** Bound the M16 scoped measurement before approval.

**Explanation:** M16-Q017 enacts mistake 3 from Browser Work and the Rendering Pipeline; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M16-Q018

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Approve alternating geometry reads and DOM for Browser Work and the Rendering Pipeline; the local context makes that proposal familiar enough for review.
- Defer measurement until production for alternating geometry reads and DOM; the team can monitor Browser Work and the Rendering Pipeline after launch.
- Approve the M16 shortcut for delta now.
- Freeze the M16 scoped measurement and record the limiting assumption before approving the change.

**Answer:** Freeze the M16 scoped measurement and record the limiting assumption before approving the change.

**Explanation:** M16-Q018 enacts mistake 4 from Browser Work and the Rendering Pipeline; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M16-Q019

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Preserve the M16 scoped measurement before approving the change.
- Approve one blocked critical interaction can be for Browser Work and the Rendering Pipeline; the local context makes that proposal familiar enough for review.
- Defer measurement until production for one blocked critical interaction can be; the team can monitor Browser Work and the Rendering Pipeline after launch.
- Approve the M16 shortcut for ember now.

**Answer:** Preserve the M16 scoped measurement before approving the change.

**Explanation:** M16-Q019 enacts mistake 5 from Browser Work and the Rendering Pipeline; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M16-Q020

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Approve a composite score hides the route for Performance Budgets and Evidence; the local context makes that proposal familiar enough for review.
- Model the M16 scoped measurement before approval.
- Defer measurement until production for a composite score hides the route; the team can monitor Performance Budgets and Evidence after launch.
- Approve the M16 shortcut for fable now.

**Answer:** Model the M16 scoped measurement before approval.

**Explanation:** M16-Q020 enacts mistake 1 from Performance Budgets and Evidence; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M16-Q021

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Approve they answer different questions for Performance Budgets and Evidence; the local context makes that proposal familiar enough for review.
- Defer measurement until production for they answer different questions; the team can monitor Performance Budgets and Evidence after launch.
- Account the M16 scoped measurement and record the limiting assumption before approving the change.
- Approve the M16 shortcut for harbor now.

**Answer:** Account the M16 scoped measurement and record the limiting assumption before approving the change.

**Explanation:** M16-Q021 enacts mistake 2 from Performance Budgets and Evidence; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M16-Q022

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Approve a tiny controlled sample is not a for Performance Budgets and Evidence; the local context makes that proposal familiar enough for review.
- Defer measurement until production for a tiny controlled sample is not a; the team can monitor Performance Budgets and Evidence after launch.
- Approve the M16 shortcut for indigo now.
- Test the M16 scoped measurement before approving the change.

**Answer:** Test the M16 scoped measurement before approving the change.

**Explanation:** M16-Q022 enacts mistake 3 from Performance Budgets and Evidence; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M16-Q023

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Scope the M16 scoped measurement before approval.
- Approve optimizing a milestone that users cannot use.: Early pixels can still be for Performance Budgets and Evidence; the local context makes that proposal familiar enough for review.
- Defer measurement until production for optimizing a milestone that users cannot use.: Early pixels can still be; the team can monitor Performance Budgets and Evidence after launch.
- Approve the M16 shortcut for juniper now.

**Answer:** Scope the M16 scoped measurement before approval.

**Explanation:** M16-Q023 enacts mistake 4 from Performance Budgets and Evidence; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M16-Q024

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Approve ignoring telemetry overhead and missingness.: Collection can change work for Performance Budgets and Evidence; the local context makes that proposal familiar enough for review.
- Measure the M16 scoped measurement and record the limiting assumption before approving the change.
- Defer measurement until production for ignoring telemetry overhead and missingness.: Collection can change work; the team can monitor Performance Budgets and Evidence after launch.
- Approve the M16 shortcut for keystone now.

**Answer:** Measure the M16 scoped measurement and record the limiting assumption before approving the change.

**Explanation:** M16-Q024 enacts mistake 5 from Performance Budgets and Evidence; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M16-Q025

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** M16 Frontend Shell Delivery case 1: Serialization is 110 x 8 / 900 = 0.98 s; RTT adds 360 ms, for about 1338 ms.

**Explanation:** M16-Q025 uses frontend shell delivery from Browser Work and the Rendering Pipeline and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M16-Q026

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** M16 Interaction Block case 2: It exceeds the budget by 220 - 100 = 120 ms.

**Explanation:** M16-Q026 uses interaction block from Performance Budgets and Evidence and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M16-Q027

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** M16 Serialization case 3: Serialization is 280 KiB x 8 / 900 Kbps = 2.49 seconds, ignoring protocol overhead.

**Explanation:** M16-Q027 uses serialization from Route Rendering and Hydration and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M16-Q028

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** M16 Rtt Setup case 4: Setup lower bound is 3 x 90 ms = 270 ms before payload work.

**Explanation:** M16-Q028 uses RTT setup from HTTP and CDN Cache Safety and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M16-Q029

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** M16 diagnosis 1 identifies controlled interaction is below guardrail and long work is attributed. The proving fields are accessibility.focus_preserved and accessibility.keyboard_path; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M16-Q029 comes from emitted trial fields rather than fixture identifiers; Browser Work and the Rendering Pipeline is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M16-Q030

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** M16 diagnosis 2 identifies Performance Budgets and Evidence evidence scope. The proving fields are accessibility.focus_preserved and accessibility.keyboard_path; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M16-Q030 comes from emitted trial fields rather than fixture identifiers; Performance Budgets and Evidence is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M16-Q031

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** M16 diagnosis 3 identifies server/client state hashes agree and recoverable mismatches are zero. The proving fields are accessibility.focus_preserved and accessibility.keyboard_path; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M16-Q031 comes from emitted trial fields rather than fixture identifiers; Route Rendering and Hydration is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M16-Q032

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** M16 diagnosis 4 identifies HTTP and CDN Cache Safety evidence scope. The proving fields are accessibility.focus_preserved and accessibility.keyboard_path; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M16-Q032 comes from emitted trial fields rather than fixture identifiers; HTTP and CDN Cache Safety is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M16-Q033

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** M16 diagnosis 5 identifies route-owned active resources and detached nodes return to baseline. The proving fields are accessibility.focus_preserved and accessibility.keyboard_path; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M16-Q033 comes from emitted trial fields rather than fixture identifiers; Accessibility and Resilient Interaction is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M16-Q034

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** M16 diagnosis 6 identifies Memory, Third Parties, and Observability evidence scope. The proving fields are accessibility.focus_preserved and accessibility.keyboard_path; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M16-Q034 comes from emitted trial fields rather than fixture identifiers; Memory, Third Parties, and Observability is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M16-Q035

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** M16 diagnosis 7 identifies core semantic route survives slow or blocked optional dependency. The proving fields are accessibility.focus_preserved and accessibility.keyboard_path; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M16-Q035 comes from emitted trial fields rather than fixture identifiers; Northstar Browser-Edge Tutorial is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M16-Q036

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** M16 diagnosis 8 identifies Frontend-Edge Decision and Teach-Back evidence scope. The proving fields are accessibility.focus_preserved and accessibility.keyboard_path; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M16-Q036 comes from emitted trial fields rather than fixture identifiers; Frontend-Edge Decision and Teach-Back is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M16-Q037

**Type:** `design_judgment`
**Difficulty:** `application`

**Answer:** For M16 decision 1, recommend against. The protected bound is 228 x 0.72 = 164.2/s, and the planned 200.6/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 200.6/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 36.4/s of lower-priority work.

**Explanation:** M16-Q037 turns on the forcing number from EX-01, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M16-Q038

**Type:** `design_judgment`
**Difficulty:** `synthesis`

**Answer:** For M16 decision 2, recommend against. The protected bound is 245 x 0.72 = 176.4/s, and the planned 215.6/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 215.6/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 39.2/s of lower-priority work.

**Explanation:** M16-Q038 turns on the forcing number from EX-02, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M16-Q039

**Type:** `design_judgment`
**Difficulty:** `recall`

**Answer:** For M16 decision 3, recommend against. The protected bound is 262 x 0.72 = 188.6/s, and the planned 230.6/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 230.6/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 42.0/s of lower-priority work.

**Explanation:** M16-Q039 turns on the forcing number from EX-03, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M16-Q040

**Type:** `design_judgment`
**Difficulty:** `application`

**Answer:** For M16 decision 4, recommend against. The protected bound is 279 x 0.72 = 200.9/s, and the planned 245.5/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 245.5/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 44.6/s of lower-priority work.

**Explanation:** M16-Q040 turns on the forcing number from EX-04, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M16-Q041

**Type:** `design_judgment`
**Difficulty:** `synthesis`

**Answer:** For M16 decision 5, recommend against. The protected bound is 296 x 0.72 = 213.1/s, and the planned 260.5/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 260.5/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 47.4/s of lower-priority work.

**Explanation:** M16-Q041 turns on the forcing number from EX-05, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M16-Q042

**Type:** `design_judgment`
**Difficulty:** `recall`

**Answer:** For M16 decision 6, recommend against. The protected bound is 313 x 0.72 = 225.4/s, and the planned 275.4/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 275.4/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 50.0/s of lower-priority work.

**Explanation:** M16-Q042 turns on the forcing number from EX-06, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M16-Q043

**Type:** `design_judgment`
**Difficulty:** `application`

**Answer:** For M16 decision 7, recommend against. The protected bound is 330 x 0.72 = 237.6/s, and the planned 290.4/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 290.4/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 52.8/s of lower-priority work.

**Explanation:** M16-Q043 turns on the forcing number from EX-07, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.
