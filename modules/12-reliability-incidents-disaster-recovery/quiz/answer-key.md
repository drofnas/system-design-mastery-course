# M12 Quiz Answer Key

This key covers all 40 questions for **Reliability, Incidents, and Disaster Recovery**. Use it after an attempt, or provide it with the LLM grading prompt for feedback.

## M12-Q001

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** Outcome-dependent exclusions can remove bad events and invalidate the ratio.

**Explanation:** M12-Q001 uses self-check 1 from User Journeys, SLIs, and SLOs; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M12-Q002

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** Only when that component outcome is itself the user contract; otherwise it is diagnostic evidence for a journey SLI.

**Explanation:** M12-Q002 uses self-check 2 from User Journeys, SLIs, and SLOs; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M12-Q003

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** When they protect different populations, consequences, owners, or decisions. Separate reporting prevents abundant low-value traffic hiding critical failure.

**Explanation:** M12-Q003 uses self-check 3 from User Journeys, SLIs, and SLOs; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M12-Q004

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** `750,000 × 0.0005 = 375` bad events.

**Explanation:** M12-Q004 uses self-check 1 from Error Budgets, Dependencies, and Composite Reliability; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M12-Q005

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** One common network, deploy, credential, or data fault can fail several paths together, making their outcomes correlated.

**Explanation:** M12-Q005 uses self-check 2 from Error Budgets, Dependencies, and Composite Reliability; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M12-Q006

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** No. Error budgets govern user-visible reliability risk; safety invariants and authorization boundaries remain hard constraints.

**Explanation:** M12-Q006 uses self-check 3 from Error Budgets, Dependencies, and Composite Reliability; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M12-Q007

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** `0.005 / 0.0005 = 10`.

**Explanation:** M12-Q007 uses self-check 1 from Burn Rates and Actionable Alerting; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M12-Q008

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** The long window proves material budget spend; the short window proves impact is active and gives faster reset after recovery.

**Explanation:** M12-Q008 uses self-check 2 from Burn Rates and Actionable Alerting; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M12-Q009

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** The affected journey, user impact, scope, threshold, immediate safe action, owner, and links to diagnostics and the runbook.

**Explanation:** M12-Q009 uses self-check 3 from Burn Rates and Actionable Alerting; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M12-Q010

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** Its reduced behavior, freshness or completeness limits, and safe next action.

**Explanation:** M12-Q010 uses self-check 1 from Graceful Degradation and Degraded Capacity; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M12-Q011

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** Reconciliation, catch-up, and probes consume the same finite resources; if they starve, the system cannot exit degradation.

**Explanation:** M12-Q011 uses self-check 2 from Graceful Degradation and Degraded Capacity; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M12-Q012

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Require the M12 scoped measurement and record the limiting assumption before approving the change.
- Approve users can fail while every process responds for User Journeys, SLIs, and SLOs; the local context makes that proposal familiar enough for review.
- Defer measurement until production for users can fail while every process responds; the team can monitor User Journeys, SLIs, and SLOs after launch.
- Approve the M12 shortcut for alpha now.

**Answer:** Require the M12 scoped measurement and record the limiting assumption before approving the change.

**Explanation:** M12-Q012 enacts mistake 1 from User Journeys, SLIs, and SLOs; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M12-Q013

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Approve a deliberate rejection still affects a user for User Journeys, SLIs, and SLOs; the local context makes that proposal familiar enough for review.
- Calculate the M12 scoped measurement before approving the change.
- Defer measurement until production for a deliberate rejection still affects a user; the team can monitor User Journeys, SLIs, and SLOs after launch.
- Approve the M12 shortcut for bravo now.

**Answer:** Calculate the M12 scoped measurement before approving the change.

**Explanation:** M12-Q013 enacts mistake 2 from User Journeys, SLIs, and SLOs; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M12-Q014

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Approve a small harmed population disappears inside the mean for User Journeys, SLIs, and SLOs; the local context makes that proposal familiar enough for review.
- Defer measurement until production for a small harmed population disappears inside the mean; the team can monitor User Journeys, SLIs, and SLOs after launch.
- Draw the M12 scoped measurement before approval.
- Approve the M12 shortcut for charlie now.

**Answer:** Draw the M12 scoped measurement before approval.

**Explanation:** M12-Q014 enacts mistake 3 from User Journeys, SLIs, and SLOs; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M12-Q015

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Approve the objective stops supporting explicit risk trade-offs for User Journeys, SLIs, and SLOs; the local context makes that proposal familiar enough for review.
- Defer measurement until production for the objective stops supporting explicit risk trade-offs; the team can monitor User Journeys, SLIs, and SLOs after launch.
- Approve the M12 shortcut for delta now.
- Separate the M12 scoped measurement and record the limiting assumption before approving the change.

**Answer:** Separate the M12 scoped measurement and record the limiting assumption before approving the change.

**Explanation:** M12-Q015 enacts mistake 4 from User Journeys, SLIs, and SLOs; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M12-Q016

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Verify the M12 scoped measurement before approving the change.
- Approve missing end events can make the ratio look healthier for User Journeys, SLIs, and SLOs; the local context makes that proposal familiar enough for review.
- Defer measurement until production for missing end events can make the ratio look healthier; the team can monitor User Journeys, SLIs, and SLOs after launch.
- Approve the M12 shortcut for ember now.

**Answer:** Verify the M12 scoped measurement before approving the change.

**Explanation:** M12-Q016 enacts mistake 5 from User Journeys, SLIs, and SLOs; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M12-Q017

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Approve budget is computed against valid events or time for Error Budgets, Dependencies, and Composite Reliability; the local context makes that proposal familiar enough for review.
- Compare the M12 scoped measurement before approval.
- Defer measurement until production for budget is computed against valid events or time; the team can monitor Error Budgets, Dependencies, and Composite Reliability after launch.
- Approve the M12 shortcut for fable now.

**Answer:** Compare the M12 scoped measurement before approval.

**Explanation:** M12-Q017 enacts mistake 1 from Error Budgets, Dependencies, and Composite Reliability; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M12-Q018

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Approve optional, parallel, fallback, and correlated for Error Budgets, Dependencies, and Composite Reliability; the local context makes that proposal familiar enough for review.
- Defer measurement until production for optional, parallel, fallback, and correlated; the team can monitor Error Budgets, Dependencies, and Composite Reliability after launch.
- Reject the M12 scoped measurement and record the limiting assumption before approving the change.
- Approve the M12 shortcut for harbor now.

**Answer:** Reject the M12 scoped measurement and record the limiting assumption before approving the change.

**Explanation:** M12-Q018 enacts mistake 2 from Error Budgets, Dependencies, and Composite Reliability; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M12-Q019

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Approve priority journeys can have different consequences for Error Budgets, Dependencies, and Composite Reliability; the local context makes that proposal familiar enough for review.
- Defer measurement until production for priority journeys can have different consequences; the team can monitor Error Budgets, Dependencies, and Composite Reliability after launch.
- Approve the M12 shortcut for indigo now.
- Trace the M12 scoped measurement before approving the change.

**Answer:** Trace the M12 scoped measurement before approving the change.

**Explanation:** M12-Q019 enacts mistake 3 from Error Budgets, Dependencies, and Composite Reliability; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M12-Q020

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Require the M12 scoped measurement before approval.
- Approve invariant or security failures remain unacceptable for Error Budgets, Dependencies, and Composite Reliability; the local context makes that proposal familiar enough for review.
- Defer measurement until production for invariant or security failures remain unacceptable; the team can monitor Error Budgets, Dependencies, and Composite Reliability after launch.
- Approve the M12 shortcut for juniper now.

**Answer:** Require the M12 scoped measurement before approval.

**Explanation:** M12-Q020 enacts mistake 4 from Error Budgets, Dependencies, and Composite Reliability; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M12-Q021

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Approve noise arrives faster than useful action for Burn Rates and Actionable Alerting; the local context makes that proposal familiar enough for review.
- Calculate the M12 scoped measurement and record the limiting assumption before approving the change.
- Defer measurement until production for noise arrives faster than useful action; the team can monitor Burn Rates and Actionable Alerting after launch.
- Approve the M12 shortcut for keystone now.

**Answer:** Calculate the M12 scoped measurement and record the limiting assumption before approving the change.

**Explanation:** M12-Q021 enacts mistake 1 from Burn Rates and Actionable Alerting; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M12-Q022

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** M12 Error Budget case 1: Budget is 750,000 x (1 - 0.9995) = 375 bad events.

**Explanation:** M12-Q022 uses error budget from User Journeys, SLIs, and SLOs and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M12-Q023

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** M12 Burn Rate case 2: Burn multiple is 0.005 / 0.0005 = 10.0x the budget rate.

**Explanation:** M12-Q023 uses burn rate from Error Budgets, Dependencies, and Composite Reliability and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M12-Q024

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** M12 Capacity Deficit case 3: Capacity deficit is 1000 - 760 = 240/s.

**Explanation:** M12-Q024 uses capacity deficit from Burn Rates and Actionable Alerting and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M12-Q025

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** M12 Rpo case 4: Observable RPO is 20 - 7 = 13 minutes if the missing middle cannot be replayed.

**Explanation:** M12-Q025 uses RPO from Graceful Degradation and Degraded Capacity and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M12-Q026

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** M12 Journey Population case 5: Excluded failure share is 600 / 20000 = 3.0%.

**Explanation:** M12-Q026 uses journey population from Incident Command, Communication, and Runbooks and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M12-Q027

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** M12 Capacity Deficit case 6: Capacity deficit is 1000 - 760 = 240/s.

**Explanation:** M12-Q027 uses capacity deficit from Postmortems and Corrective Work and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M12-Q028

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** M12 diagnosis 1 identifies accepted priority work and queues remain bounded. The proving fields are alerts.actionable and alerts.long_window_minutes; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M12-Q028 comes from emitted trial fields rather than fixture identifiers; User Journeys, SLIs, and SLOs is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M12-Q029

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** M12 diagnosis 2 identifies Error Budgets, Dependencies, and Composite Reliability evidence scope. The proving fields are alerts.actionable and alerts.long_window_minutes; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M12-Q029 comes from emitted trial fields rather than fixture identifiers; Error Budgets, Dependencies, and Composite Reliability is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M12-Q030

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** M12 diagnosis 3 identifies material active burn produces an actionable alert. The proving fields are alerts.actionable and alerts.long_window_minutes; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M12-Q030 comes from emitted trial fields rather than fixture identifiers; Burn Rates and Actionable Alerting is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M12-Q031

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** M12 diagnosis 4 identifies Graceful Degradation and Degraded Capacity evidence scope. The proving fields are alerts.actionable and alerts.long_window_minutes; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M12-Q031 comes from emitted trial fields rather than fixture identifiers; Graceful Degradation and Degraded Capacity is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M12-Q032

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** M12 diagnosis 5 identifies journey measurement includes actual failures. The proving fields are alerts.actionable and alerts.long_window_minutes; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M12-Q032 comes from emitted trial fields rather than fixture identifiers; Incident Command, Communication, and Runbooks is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M12-Q033

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** M12 diagnosis 6 identifies Postmortems and Corrective Work evidence scope. The proving fields are alerts.actionable and alerts.long_window_minutes; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M12-Q033 comes from emitted trial fields rather than fixture identifiers; Postmortems and Corrective Work is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M12-Q034

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** M12 diagnosis 7 identifies incident changes, handoff, and communications are coordinated. The proving fields are alerts.actionable and alerts.long_window_minutes; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M12-Q034 comes from emitted trial fields rather than fixture identifiers; Backups, Restore, Failover, and Failback is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M12-Q035

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** M12 diagnosis 8 identifies Chaos, Game Days, and Reliability Decisions evidence scope. The proving fields are alerts.actionable and alerts.long_window_minutes; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M12-Q035 comes from emitted trial fields rather than fixture identifiers; Chaos, Game Days, and Reliability Decisions is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M12-Q036

**Type:** `design_judgment`
**Difficulty:** `recall`

**Answer:** For M12 decision 1, recommend against. The protected bound is 216 x 0.72 = 155.5/s, and the planned 190.1/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 190.1/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 34.6/s of lower-priority work.

**Explanation:** M12-Q036 turns on the forcing number from EX-01, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M12-Q037

**Type:** `design_judgment`
**Difficulty:** `application`

**Answer:** For M12 decision 2, recommend against. The protected bound is 233 x 0.72 = 167.8/s, and the planned 205.0/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 205.0/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 37.2/s of lower-priority work.

**Explanation:** M12-Q037 turns on the forcing number from EX-02, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M12-Q038

**Type:** `design_judgment`
**Difficulty:** `synthesis`

**Answer:** For M12 decision 3, recommend against. The protected bound is 250 x 0.72 = 180.0/s, and the planned 220.0/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 220.0/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 40.0/s of lower-priority work.

**Explanation:** M12-Q038 turns on the forcing number from EX-03, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M12-Q039

**Type:** `design_judgment`
**Difficulty:** `recall`

**Answer:** For M12 decision 4, recommend against. The protected bound is 267 x 0.72 = 192.2/s, and the planned 235.0/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 235.0/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 42.8/s of lower-priority work.

**Explanation:** M12-Q039 turns on the forcing number from EX-04, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M12-Q040

**Type:** `design_judgment`
**Difficulty:** `application`

**Answer:** For M12 decision 5, recommend against. The protected bound is 284 x 0.72 = 204.5/s, and the planned 249.9/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 249.9/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 45.4/s of lower-priority work.

**Explanation:** M12-Q040 turns on the forcing number from EX-05, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.
