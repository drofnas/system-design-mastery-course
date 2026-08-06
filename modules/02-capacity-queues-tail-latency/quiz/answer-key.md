# M02 Quiz Answer Key

This key covers all 41 questions for **Capacity, Queues, and Tail Latency**. Use it after an attempt, or provide it with the LLM grading prompt for feedback.

## M02-Q001

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** Concurrency depends on rate and time in the boundary; a daily total provides neither short-window rate nor service time.

**Explanation:** M02-Q001 uses self-check 1 from Workload and Useful Work; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M02-Q002

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** No. It may recover one logical operation, but it remains another attempt for the same identity.

**Explanation:** M02-Q002 uses self-check 2 from Workload and Useful Work; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M02-Q003

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** Key or tenant skew, including the rate and concentration window.

**Explanation:** M02-Q003 uses self-check 3 from Workload and Useful Work; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M02-Q004

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** Recovery often overlaps new demand. Ignoring it produces a design that can serve normally but cannot catch up.

**Explanation:** M02-Q004 uses self-check 4 from Workload and Useful Work; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M02-Q005

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** Only when attempted work enters the chosen boundary; cheap pre-admission rejection belongs outside it.

**Explanation:** M02-Q005 uses self-check 1 from Little’s Law and Saturation; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M02-Q006

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** No. The identity assumes suitable long-run averages; queue trend and completion evidence establish stability.

**Explanation:** M02-Q006 uses self-check 2 from Little’s Law and Saturation; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M02-Q007

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** It leaves no room for variance, bursts, interruptions, recovery, or model error.

**Explanation:** M02-Q007 uses self-check 3 from Little’s Law and Saturation; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M02-Q008

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** Downstream concurrency reaches its bound and rejection or waiting appears while service workers remain below their own bound.

**Explanation:** M02-Q008 uses self-check 4 from Little’s Law and Saturation; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M02-Q009

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** The missing observations were never collected; sorting the remaining values cannot reconstruct their experience without an explicit correction model.

**Explanation:** M02-Q009 uses self-check 1 from Latency Measurement; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M02-Q010

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** The generator did not deliver the requested schedule, so system-capacity conclusions are confounded.

**Explanation:** M02-Q010 uses self-check 2 from Latency Measurement; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M02-Q011

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** Yes, in the attempted-user population. Record rejection latency and outcome separately rather than mixing it with successful-service latency.

**Explanation:** M02-Q011 uses self-check 3 from Latency Measurement; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M02-Q012

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** Maximum exposes extreme observations and timeout censoring, although it is not stable enough to replace percentiles.

**Explanation:** M02-Q012 uses self-check 4 from Latency Measurement; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M02-Q013

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** It cannot be determined from the branch p99 alone; the full distribution, fan-out, correlation, and response rule matter.

**Explanation:** M02-Q013 uses self-check 1 from Fan-out and Tail Amplification; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M02-Q014

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Calculate the M02 scoped measurement and record the limiting assumption before approving the change.
- Approve host count is supply, not demand for Workload and Useful Work; the local context makes that proposal familiar enough for review.
- Defer measurement until production for host count is supply, not demand; the team can monitor Workload and Useful Work after launch.
- Approve the M02 shortcut for alpha now.

**Answer:** Calculate the M02 scoped measurement and record the limiting assumption before approving the change.

**Explanation:** M02-Q014 enacts mistake 1 from Workload and Useful Work; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M02-Q015

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Approve it erases burst duration and recovery debt for Workload and Useful Work; the local context makes that proposal familiar enough for review.
- Draw the M02 scoped measurement before approving the change.
- Defer measurement until production for it erases burst duration and recovery debt; the team can monitor Workload and Useful Work after launch.
- Approve the M02 shortcut for bravo now.

**Answer:** Draw the M02 scoped measurement before approving the change.

**Explanation:** M02-Q015 enacts mistake 2 from Workload and Useful Work; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M02-Q016

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Approve retries appear as successful scaling for Workload and Useful Work; the local context makes that proposal familiar enough for review.
- Defer measurement until production for retries appear as successful scaling; the team can monitor Workload and Useful Work after launch.
- Separate the M02 scoped measurement before approval.
- Approve the M02 shortcut for charlie now.

**Answer:** Separate the M02 scoped measurement before approval.

**Explanation:** M02-Q016 enacts mistake 3 from Workload and Useful Work; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M02-Q017

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Approve reconciliation and backlog drain consume the for Workload and Useful Work; the local context makes that proposal familiar enough for review.
- Defer measurement until production for reconciliation and backlog drain consume the; the team can monitor Workload and Useful Work after launch.
- Approve the M02 shortcut for delta now.
- Verify the M02 scoped measurement and record the limiting assumption before approving the change.

**Answer:** Verify the M02 scoped measurement and record the limiting assumption before approving the change.

**Explanation:** M02-Q017 enacts mistake 4 from Workload and Useful Work; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M02-Q018

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Compare the M02 scoped measurement before approving the change.
- Approve false precision hides the sensitivity for Workload and Useful Work; the local context makes that proposal familiar enough for review.
- Defer measurement until production for false precision hides the sensitivity; the team can monitor Workload and Useful Work after launch.
- Approve the M02 shortcut for ember now.

**Answer:** Compare the M02 scoped measurement before approving the change.

**Explanation:** M02-Q018 enacts mistake 5 from Workload and Useful Work; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M02-Q019

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Approve server concurrency with client end-to-end for Little’s Law and Saturation; the local context makes that proposal familiar enough for review.
- Reject the M02 scoped measurement before approval.
- Defer measurement until production for server concurrency with client end-to-end; the team can monitor Little’s Law and Saturation after launch.
- Approve the M02 shortcut for fable now.

**Answer:** Reject the M02 scoped measurement before approval.

**Explanation:** M02-Q019 enacts mistake 1 from Little’s Law and Saturation; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M02-Q020

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Approve rejected work did not occupy the for Little’s Law and Saturation; the local context makes that proposal familiar enough for review.
- Defer measurement until production for rejected work did not occupy the; the team can monitor Little’s Law and Saturation after launch.
- Trace the M02 scoped measurement and record the limiting assumption before approving the change.
- Approve the M02 shortcut for harbor now.

**Answer:** Trace the M02 scoped measurement and record the limiting assumption before approving the change.

**Explanation:** M02-Q020 enacts mistake 2 from Little’s Law and Saturation; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M02-Q021

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Approve the calculation has no variance for Little’s Law and Saturation; the local context makes that proposal familiar enough for review.
- Defer measurement until production for the calculation has no variance; the team can monitor Little’s Law and Saturation after launch.
- Approve the M02 shortcut for indigo now.
- Require the M02 scoped measurement before approving the change.

**Answer:** Require the M02 scoped measurement before approving the change.

**Explanation:** M02-Q021 enacts mistake 3 from Little’s Law and Saturation; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M02-Q022

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Calculate the M02 scoped measurement before approval.
- Approve little’s Law relates long-run averages for Little’s Law and Saturation; the local context makes that proposal familiar enough for review.
- Defer measurement until production for little’s Law relates long-run averages; the team can monitor Little’s Law and Saturation after launch.
- Approve the M02 shortcut for juniper now.

**Answer:** Calculate the M02 scoped measurement before approval.

**Explanation:** M02-Q022 enacts mistake 4 from Little’s Law and Saturation; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M02-Q023

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Approve shared downstreams can bind first for Little’s Law and Saturation; the local context makes that proposal familiar enough for review.
- Draw the M02 scoped measurement and record the limiting assumption before approving the change.
- Defer measurement until production for shared downstreams can bind first; the team can monitor Little’s Law and Saturation after launch.
- Approve the M02 shortcut for keystone now.

**Answer:** Draw the M02 scoped measurement and record the limiting assumption before approving the change.

**Explanation:** M02-Q023 enacts mistake 5 from Little’s Law and Saturation; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M02-Q024

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** M02 Retry Amplification case 1: Attempts are 120 x (1 + 0.25) = 150.0/s; useful throughput is still bounded by the 120/s logical identities.

**Explanation:** M02-Q024 uses retry amplification from Workload and Useful Work and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M02-Q025

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** M02 Little'S Law case 2: L = 124/s x 0.080 s = 9.92 requests inside the boundary.

**Explanation:** M02-Q025 uses Little's Law from Little’s Law and Saturation and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M02-Q026

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** M02 Fan-Out Tail Probability case 3: At least one slow branch = 1 - (1 - 0.020)^4 = 0.0776, or 7.76%.

**Explanation:** M02-Q026 uses fan-out tail probability from Latency Measurement and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M02-Q027

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** M02 Queue Drain Bound case 4: Drain time is 54,000 / 240/s = 225.0 seconds before overhead or new arrivals.

**Explanation:** M02-Q027 uses queue drain bound from Fan-out and Tail Amplification and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M02-Q028

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** M02 Layered Retry Attempts case 5: The multiplier is 3^4 = 81 attempts at the deepest dependency for one original request.

**Explanation:** M02-Q028 uses layered retry attempts from Bounded Overload Control and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M02-Q029

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** M02 Failover Headroom case 6: Failover-adjusted capacity is 315.6 x 0.75 = 236.7/s, so steady state must stay at or below about 236.7/s.

**Explanation:** M02-Q029 uses failover headroom from Retries and Downstream Protection and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M02-Q030

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** M02 Backlog Drain case 7: Net drain is (240 - 150) / 1.25 = 72.0/s, so drain time is 54,000 / 72.0 = 750.0 seconds.

**Explanation:** M02-Q030 uses backlog drain from Failover Headroom and Unit Cost and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M02-Q031

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** M02 diagnosis 1 identifies Workload and Useful Work evidence scope. The proving fields are arrival.rate_per_second and arrival.duration_seconds; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M02-Q031 comes from emitted trial fields rather than fixture identifiers; Workload and Useful Work is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M02-Q032

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** M02 diagnosis 2 identifies Little’s Law and Saturation evidence scope. The proving fields are arrival.rate_per_second and arrival.duration_seconds; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M02-Q032 comes from emitted trial fields rather than fixture identifiers; Little’s Law and Saturation is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M02-Q033

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** M02 diagnosis 3 identifies Latency Measurement evidence scope. The proving fields are arrival.rate_per_second and arrival.duration_seconds; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M02-Q033 comes from emitted trial fields rather than fixture identifiers; Latency Measurement is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M02-Q034

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** M02 diagnosis 4 identifies Fan-out and Tail Amplification evidence scope. The proving fields are arrival.rate_per_second and arrival.duration_seconds; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M02-Q034 comes from emitted trial fields rather than fixture identifiers; Fan-out and Tail Amplification is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M02-Q035

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** M02 diagnosis 5 identifies Bounded Overload Control evidence scope. The proving fields are arrival.rate_per_second and arrival.duration_seconds; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M02-Q035 comes from emitted trial fields rather than fixture identifiers; Bounded Overload Control is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M02-Q036

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** M02 diagnosis 6 identifies Retries and Downstream Protection evidence scope. The proving fields are arrival.rate_per_second and arrival.duration_seconds; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M02-Q036 comes from emitted trial fields rather than fixture identifiers; Retries and Downstream Protection is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M02-Q037

**Type:** `design_judgment`
**Difficulty:** `application`

**Answer:** For M02 decision 1, recommend against. The protected bound is 186 x 0.72 = 133.9/s, and the planned 163.7/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 163.7/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 29.8/s of lower-priority work.

**Explanation:** M02-Q037 turns on the forcing number from EX-01, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M02-Q038

**Type:** `design_judgment`
**Difficulty:** `synthesis`

**Answer:** For M02 decision 2, recommend against. The protected bound is 203 x 0.72 = 146.2/s, and the planned 178.6/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 178.6/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 32.4/s of lower-priority work.

**Explanation:** M02-Q038 turns on the forcing number from EX-02, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M02-Q039

**Type:** `design_judgment`
**Difficulty:** `recall`

**Answer:** For M02 decision 3, recommend against. The protected bound is 220 x 0.72 = 158.4/s, and the planned 193.6/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 193.6/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 35.2/s of lower-priority work.

**Explanation:** M02-Q039 turns on the forcing number from EX-03, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M02-Q040

**Type:** `design_judgment`
**Difficulty:** `application`

**Answer:** For M02 decision 4, recommend against. The protected bound is 237 x 0.72 = 170.6/s, and the planned 208.6/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 208.6/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 38.0/s of lower-priority work.

**Explanation:** M02-Q040 turns on the forcing number from EX-04, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M02-Q041

**Type:** `design_judgment`
**Difficulty:** `synthesis`

**Answer:** For M02 decision 5, recommend against. The protected bound is 254 x 0.72 = 182.9/s, and the planned 223.5/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 223.5/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 40.6/s of lower-priority work.

**Explanation:** M02-Q041 turns on the forcing number from EX-05, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.
