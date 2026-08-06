# M06 Quiz Answer Key

This key covers all 40 questions for **Deadlines and Resilient Remote Calls**. Use it after an attempt, or provide it with the LLM grading prompt for feedback.

## M06-Q001

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** The absolute deadline preserves elapsed time across hops and prevents nested work from extending the user promise.

**Explanation:** M06-Q001 uses self-check 1 from End-to-End Deadlines and Allocation; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M06-Q002

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** Parallel completion follows the slowest required child, while attempts, slots, CPU, and dependency load still accumulate across all children.

**Explanation:** M06-Q002 uses self-check 2 from End-to-End Deadlines and Allocation; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M06-Q003

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** Reject, degrade, or use an approved fallback before dispatch; record the budget decision rather than starting predictably late work.

**Explanation:** M06-Q003 uses self-check 3 from End-to-End Deadlines and Allocation; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M06-Q004

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** Only that an owner was asked to stop; observation and cleanup need evidence.

**Explanation:** M06-Q004 uses self-check 1 from Cancellation and Useful-Work Boundaries; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M06-Q005

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** Completing an already-started atomic effect plus its durable outcome can preserve correctness better than creating an unknown partial state.

**Explanation:** M06-Q005 uses self-check 2 from Cancellation and Useful-Work Boundaries; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M06-Q006

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** A time series of queued/active children, permits, handles, and effect starts through `t_drained`, correlated to `t_signal`.

**Explanation:** M06-Q006 uses self-check 3 from Cancellation and Useful-Work Boundaries; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M06-Q007

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** No. It changes timing; attempt count needs a separate cap or budget.

**Explanation:** M06-Q007 uses self-check 1 from Retry Classification, Budgets, Backoff, and Jitter; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M06-Q008

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** Singular ownership prevents multiplicative retries and makes cost visible.

**Explanation:** M06-Q008 uses self-check 2 from Retry Classification, Budgets, Backoff, and Jitter; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M06-Q009

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** More dependency work is producing fewer logical outcomes, a possible positive feedback loop rather than a harmless transient symptom.

**Explanation:** M06-Q009 uses self-check 3 from Retry Classification, Budgets, Backoff, and Jitter; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M06-Q010

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** Nothing conclusive; the outcome is ambiguous until authoritative state or a durable idempotency result is consulted.

**Explanation:** M06-Q010 uses self-check 1 from Idempotency and Deduplication; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M06-Q011

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** It prevents one key from silently representing two different intentions.

**Explanation:** M06-Q011 uses self-check 2 from Idempotency and Deduplication; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M06-Q012

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Require the M06 scoped measurement and record the limiting assumption before approving the change.
- Approve nested calls outlive the 420 ms promise for End-to-End Deadlines and Allocation; the local context makes that proposal familiar enough for review.
- Defer measurement until production for nested calls outlive the 420 ms promise; the team can monitor End-to-End Deadlines and Allocation after launch.
- Approve the M06 shortcut for alpha now.

**Answer:** Require the M06 scoped measurement and record the limiting assumption before approving the change.

**Explanation:** M06-Q012 enacts mistake 1 from End-to-End Deadlines and Allocation; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M06-Q013

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Approve overstates latency while hiding resource cost for End-to-End Deadlines and Allocation; the local context makes that proposal familiar enough for review.
- Calculate the M06 scoped measurement before approving the change.
- Defer measurement until production for overstates latency while hiding resource cost; the team can monitor End-to-End Deadlines and Allocation after launch.
- Approve the M06 shortcut for bravo now.

**Answer:** Calculate the M06 scoped measurement before approving the change.

**Explanation:** M06-Q013 enacts mistake 2 from End-to-End Deadlines and Allocation; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M06-Q014

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Approve misses the stuck minority that occupies all slots for End-to-End Deadlines and Allocation; the local context makes that proposal familiar enough for review.
- Defer measurement until production for misses the stuck minority that occupies all slots; the team can monitor End-to-End Deadlines and Allocation after launch.
- Draw the M06 scoped measurement before approval.
- Approve the M06 shortcut for charlie now.

**Answer:** Draw the M06 scoped measurement before approval.

**Explanation:** M06-Q014 enacts mistake 3 from End-to-End Deadlines and Allocation; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M06-Q015

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Approve leaves no time to assemble or cancel for End-to-End Deadlines and Allocation; the local context makes that proposal familiar enough for review.
- Defer measurement until production for leaves no time to assemble or cancel; the team can monitor End-to-End Deadlines and Allocation after launch.
- Approve the M06 shortcut for delta now.
- Separate the M06 scoped measurement and record the limiting assumption before approving the change.

**Answer:** Separate the M06 scoped measurement and record the limiting assumption before approving the change.

**Explanation:** M06-Q015 enacts mistake 4 from End-to-End Deadlines and Allocation; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M06-Q016

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Verify the M06 scoped measurement before approving the change.
- Approve treating a deadline as proof of interruption:: the caller may stop while the ser for End-to-End Deadlines and Allocation; the local context makes that proposal familiar enough for review.
- Defer measurement until production for treating a deadline as proof of interruption:: the caller may stop while the ser; the team can monitor End-to-End Deadlines and Allocation after launch.
- Approve the M06 shortcut for ember now.

**Answer:** Verify the M06 scoped measurement before approving the change.

**Explanation:** M06-Q016 enacts mistake 5 from End-to-End Deadlines and Allocation; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M06-Q017

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Approve underlying work and sockets remain alive for Cancellation and Useful-Work Boundaries; the local context makes that proposal familiar enough for review.
- Compare the M06 scoped measurement before approval.
- Defer measurement until production for underlying work and sockets remain alive; the team can monitor Cancellation and Useful-Work Boundaries after launch.
- Approve the M06 shortcut for fable now.

**Answer:** Compare the M06 scoped measurement before approval.

**Explanation:** M06-Q017 enacts mistake 1 from Cancellation and Useful-Work Boundaries; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M06-Q018

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Approve reported capacity exceeds reality for Cancellation and Useful-Work Boundaries; the local context makes that proposal familiar enough for review.
- Defer measurement until production for reported capacity exceeds reality; the team can monitor Cancellation and Useful-Work Boundaries after launch.
- Reject the M06 scoped measurement and record the limiting assumption before approving the change.
- Approve the M06 shortcut for harbor now.

**Answer:** Reject the M06 scoped measurement and record the limiting assumption before approving the change.

**Explanation:** M06-Q018 enacts mistake 2 from Cancellation and Useful-Work Boundaries; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M06-Q019

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Approve abandoned requests later dispatch for Cancellation and Useful-Work Boundaries; the local context makes that proposal familiar enough for review.
- Defer measurement until production for abandoned requests later dispatch; the team can monitor Cancellation and Useful-Work Boundaries after launch.
- Approve the M06 shortcut for indigo now.
- Trace the M06 scoped measurement before approving the change.

**Answer:** Trace the M06 scoped measurement before approving the change.

**Explanation:** M06-Q019 enacts mistake 3 from Cancellation and Useful-Work Boundaries; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M06-Q020

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Require the M06 scoped measurement before approval.
- Approve state can become ambiguous or corrupt for Cancellation and Useful-Work Boundaries; the local context makes that proposal familiar enough for review.
- Defer measurement until production for state can become ambiguous or corrupt; the team can monitor Cancellation and Useful-Work Boundaries after launch.
- Approve the M06 shortcut for juniper now.

**Answer:** Require the M06 scoped measurement before approval.

**Explanation:** M06-Q020 enacts mistake 4 from Cancellation and Useful-Work Boundaries; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M06-Q021

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Approve counting an error response as cleanup evidence:: the resource lifecycle is unobs for Cancellation and Useful-Work Boundaries; the local context makes that proposal familiar enough for review.
- Calculate the M06 scoped measurement and record the limiting assumption before approving the change.
- Defer measurement until production for counting an error response as cleanup evidence:: the resource lifecycle is unobs; the team can monitor Cancellation and Useful-Work Boundaries after launch.
- Approve the M06 shortcut for keystone now.

**Answer:** Calculate the M06 scoped measurement and record the limiting assumption before approving the change.

**Explanation:** M06-Q021 enacts mistake 5 from Cancellation and Useful-Work Boundaries; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M06-Q022

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** M06 Deadline Allocation case 1: Usable budget is 900 - 180 = 720 ms; per stage is 240 ms.

**Explanation:** M06-Q022 uses deadline allocation from End-to-End Deadlines and Allocation and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M06-Q023

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** M06 Attempt Count case 2: Worst count is 2^3 = 8 attempts for one original operation.

**Explanation:** M06-Q023 uses attempt count from Cancellation and Useful-Work Boundaries and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M06-Q024

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** M06 Dependency Concurrency case 3: Mean dependency concurrency is 180 x 0.060 = 10.8 active calls.

**Explanation:** M06-Q024 uses dependency concurrency from Retry Classification, Budgets, Backoff, and Jitter and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M06-Q025

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** M06 Dependency Concurrency case 4: Mean dependency concurrency is 180 x 0.060 = 10.8 active calls.

**Explanation:** M06-Q025 uses dependency concurrency from Idempotency and Deduplication and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M06-Q026

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** M06 Dependency Concurrency case 5: Mean dependency concurrency is 180 x 0.060 = 10.8 active calls.

**Explanation:** M06-Q026 uses dependency concurrency from Bulkheads, Pools, Health, and Bounded Fan-Out and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M06-Q027

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** M06 Dependency Concurrency case 6: Mean dependency concurrency is 180 x 0.060 = 10.8 active calls.

**Explanation:** M06-Q027 uses dependency concurrency from Circuit Breakers, Hedges, and Partial Results and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M06-Q028

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** M06 diagnosis 1 identifies End-to-End Deadlines and Allocation evidence scope. The proving fields are attempts.initial and attempts.per_dependency.road; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M06-Q028 comes from emitted trial fields rather than fixture identifiers; End-to-End Deadlines and Allocation is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M06-Q029

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** M06 diagnosis 2 identifies Cancellation and Useful-Work Boundaries evidence scope. The proving fields are attempts.backoff_logical_ms.0 and attempts.backoff_logical_ms.1; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M06-Q029 comes from emitted trial fields rather than fixture identifiers; Cancellation and Useful-Work Boundaries is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M06-Q030

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** M06 diagnosis 3 identifies Retry Classification, Budgets, Backoff, and Jitter evidence scope. The proving fields are attempts.backoff_logical_ms.0 and attempts.backoff_logical_ms.1; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M06-Q030 comes from emitted trial fields rather than fixture identifiers; Retry Classification, Budgets, Backoff, and Jitter is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M06-Q031

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** M06 diagnosis 4 identifies Idempotency and Deduplication evidence scope. The proving fields are attempts.initial and attempts.per_dependency.road; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M06-Q031 comes from emitted trial fields rather than fixture identifiers; Idempotency and Deduplication is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M06-Q032

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** M06 diagnosis 5 identifies Bulkheads, Pools, Health, and Bounded Fan-Out evidence scope. The proving fields are attempts.initial and attempts.per_dependency.road; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M06-Q032 comes from emitted trial fields rather than fixture identifiers; Bulkheads, Pools, Health, and Bounded Fan-Out is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M06-Q033

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** M06 diagnosis 6 identifies Circuit Breakers, Hedges, and Partial Results evidence scope. The proving fields are attempts.initial and attempts.per_dependency.road; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M06-Q033 comes from emitted trial fields rather than fixture identifiers; Circuit Breakers, Hedges, and Partial Results is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M06-Q034

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** M06 diagnosis 7 identifies Rate Limits, Quotas, and Fairness evidence scope. The proving fields are attempts.initial and attempts.per_dependency.road; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M06-Q034 comes from emitted trial fields rather than fixture identifiers; Rate Limits, Quotas, and Fairness is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M06-Q035

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** M06 diagnosis 8 identifies Remote-Call Policy, Migration, and Ownership evidence scope. The proving fields are attempts.initial and attempts.per_dependency.road; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M06-Q035 comes from emitted trial fields rather than fixture identifiers; Remote-Call Policy, Migration, and Ownership is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M06-Q036

**Type:** `design_judgment`
**Difficulty:** `recall`

**Answer:** For M06 decision 1, recommend against. The protected bound is 198 x 0.72 = 142.6/s, and the planned 174.2/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 174.2/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 31.6/s of lower-priority work.

**Explanation:** M06-Q036 turns on the forcing number from EX-01, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M06-Q037

**Type:** `design_judgment`
**Difficulty:** `application`

**Answer:** For M06 decision 2, recommend against. The protected bound is 215 x 0.72 = 154.8/s, and the planned 189.2/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 189.2/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 34.4/s of lower-priority work.

**Explanation:** M06-Q037 turns on the forcing number from EX-02, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M06-Q038

**Type:** `design_judgment`
**Difficulty:** `synthesis`

**Answer:** For M06 decision 3, recommend against. The protected bound is 232 x 0.72 = 167.0/s, and the planned 204.2/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 204.2/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 37.2/s of lower-priority work.

**Explanation:** M06-Q038 turns on the forcing number from EX-03, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M06-Q039

**Type:** `design_judgment`
**Difficulty:** `recall`

**Answer:** For M06 decision 4, recommend against. The protected bound is 249 x 0.72 = 179.3/s, and the planned 219.1/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 219.1/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 39.8/s of lower-priority work.

**Explanation:** M06-Q039 turns on the forcing number from EX-04, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M06-Q040

**Type:** `design_judgment`
**Difficulty:** `application`

**Answer:** For M06 decision 5, recommend against. The protected bound is 266 x 0.72 = 191.5/s, and the planned 234.1/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 234.1/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 42.6/s of lower-priority work.

**Explanation:** M06-Q040 turns on the forcing number from EX-05, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.
