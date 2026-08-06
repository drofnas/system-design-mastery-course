# M15 Quiz Answer Key

This key covers all 38 questions for **Execution Models Across Languages**. Use it after an attempt, or provide it with the LLM grading prompt for feedback.

## M15-Q001

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** No. Borrow rules cover memory access; external-resource lifetime still needs an owned close path and observed cleanup.

**Explanation:** M15-Q001 uses self-check 1 from Memory Lifetime and Management; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M15-Q002

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** The runtime or allocator may keep reclaimed regions for reuse; object reachability, heap commitment, and RSS are different measures.

**Explanation:** M15-Q002 uses self-check 2 from Memory Lifetime and Management; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M15-Q003

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** Retainer paths or owner identities show continuing reachability; collector events plus falling live-set size suggest delayed reclamation instead.

**Explanation:** M15-Q003 uses self-check 3 from Memory Lifetime and Management; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M15-Q004

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** One core or executor thread may be saturated while the host has idle cores; throttling or a blocked scheduler can also hide behind aggregate CPU.

**Explanation:** M15-Q004 uses self-check 1 from Schedulers, Event Loops, and Tasks; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M15-Q005

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** It reduces the cost and coupling of one Java task to one OS thread. It does not add CPU, memory, connections, downstream capacity, deadlines, or bounds.

**Explanation:** M15-Q005 uses self-check 2 from Schedulers, Event Loops, and Tasks; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M15-Q006

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** When offered children are unbounded or cancellation/cleanup does not own their lifetime, task count and external work can grow beyond the budget.

**Explanation:** M15-Q006 uses self-check 3 from Schedulers, Event Loops, and Tasks; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M15-Q007

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** Orphan work consumes resources, may perform effects after authority expires, and can leak request or tenant context.

**Explanation:** M15-Q007 uses self-check 1 from Bounded Fan-out and Structured Cleanup; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M15-Q008

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** Validate a small bounded envelope, then admit before large allocation or child creation. Otherwise rejected work can still exhaust the service.

**Explanation:** M15-Q008 uses self-check 2 from Bounded Fan-out and Structured Cleanup; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M15-Q009

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** Stable task/resource identities, cancellation acknowledgement, zero owned active tasks and open resources after grace, plus matched acquisition/release.

**Explanation:** M15-Q009 uses self-check 3 from Bounded Fan-out and Structured Cleanup; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M15-Q010

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** No. The executed schedules may not expose the conflict and observations do not create a language-defined ordering.

**Explanation:** M15-Q010 uses self-check 1 from Memory Visibility and Races; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M15-Q011

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** No. The counter and list need one coherent protocol and completion boundary.

**Explanation:** M15-Q011 uses self-check 2 from Memory Visibility and Races; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M15-Q012

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** Workload and schedule coverage, tool/runtime identity, invariant checks, unsupported-code limits, and a separate static or causal argument.

**Explanation:** M15-Q012 uses self-check 3 from Memory Visibility and Races; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M15-Q013

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** Nothing at runtime; it only changes the compiler's assumed type.

**Explanation:** M15-Q013 uses self-check 1 from Types, Serialization, and Validation; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M15-Q014

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Calculate the M15 scoped measurement and record the limiting assumption before approving the change.
- Approve treating heap allocation as inherently slow while ignoring allocation rate for Memory Lifetime and Management; the local context makes that proposal familiar enough for review.
- Defer measurement until production for treating heap allocation as inherently slow while ignoring allocation rate; the team can monitor Memory Lifetime and Management after launch.
- Approve the M15 shortcut for alpha now.

**Answer:** Calculate the M15 scoped measurement and record the limiting assumption before approving the change.

**Explanation:** M15-Q014 enacts mistake 1 from Memory Lifetime and Management; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M15-Q015

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Approve treating low RSS as proof of release; allocators may retain pages and RSS may for Memory Lifetime and Management; the local context makes that proposal familiar enough for review.
- Draw the M15 scoped measurement before approving the change.
- Defer measurement until production for treating low RSS as proof of release; allocators may retain pages and RSS may; the team can monitor Memory Lifetime and Management after launch.
- Approve the M15 shortcut for bravo now.

**Answer:** Draw the M15 scoped measurement before approving the change.

**Explanation:** M15-Q015 enacts mistake 2 from Memory Lifetime and Management; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M15-Q016

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Approve claiming RAII closes asynchronous child work automatically. The scope must own for Memory Lifetime and Management; the local context makes that proposal familiar enough for review.
- Defer measurement until production for claiming RAII closes asynchronous child work automatically. The scope must own; the team can monitor Memory Lifetime and Management after launch.
- Separate the M15 scoped measurement before approval.
- Approve the M15 shortcut for charlie now.

**Answer:** Separate the M15 scoped measurement before approval.

**Explanation:** M15-Q016 enacts mistake 3 from Memory Lifetime and Management; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M15-Q017

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Approve comparing GC pauses without heap size, allocation rate, flags, warm-up, and for Memory Lifetime and Management; the local context makes that proposal familiar enough for review.
- Defer measurement until production for comparing GC pauses without heap size, allocation rate, flags, warm-up, and; the team can monitor Memory Lifetime and Management after launch.
- Approve the M15 shortcut for delta now.
- Verify the M15 scoped measurement and record the limiting assumption before approving the change.

**Answer:** Verify the M15 scoped measurement and record the limiting assumption before approving the change.

**Explanation:** M15-Q017 enacts mistake 4 from Memory Lifetime and Management; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M15-Q018

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Compare the M15 scoped measurement before approving the change.
- Approve calling all Node work single-threaded or all Go/Rust/Java work parallel for Schedulers, Event Loops, and Tasks; the local context makes that proposal familiar enough for review.
- Defer measurement until production for calling all Node work single-threaded or all Go/Rust/Java work parallel; the team can monitor Schedulers, Event Loops, and Tasks after launch.
- Approve the M15 shortcut for ember now.

**Answer:** Compare the M15 scoped measurement before approving the change.

**Explanation:** M15-Q018 enacts mistake 1 from Schedulers, Event Loops, and Tasks; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M15-Q019

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Approve measuring CPU utilization without runnable queue, throttling, and per-core use for Schedulers, Event Loops, and Tasks; the local context makes that proposal familiar enough for review.
- Reject the M15 scoped measurement before approval.
- Defer measurement until production for measuring CPU utilization without runnable queue, throttling, and per-core use; the team can monitor Schedulers, Event Loops, and Tasks after launch.
- Approve the M15 shortcut for fable now.

**Answer:** Reject the M15 scoped measurement before approval.

**Explanation:** M15-Q019 enacts mistake 2 from Schedulers, Event Loops, and Tasks; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M15-Q020

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Approve replacing a small thread pool with unbounded tasks and moving failure to for Schedulers, Event Loops, and Tasks; the local context makes that proposal familiar enough for review.
- Defer measurement until production for replacing a small thread pool with unbounded tasks and moving failure to; the team can monitor Schedulers, Event Loops, and Tasks after launch.
- Trace the M15 scoped measurement and record the limiting assumption before approving the change.
- Approve the M15 shortcut for harbor now.

**Answer:** Trace the M15 scoped measurement and record the limiting assumption before approving the change.

**Explanation:** M15-Q020 enacts mistake 3 from Schedulers, Event Loops, and Tasks; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M15-Q021

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Approve assuming async syntax proves non-blocking behavior for Schedulers, Event Loops, and Tasks; the local context makes that proposal familiar enough for review.
- Defer measurement until production for assuming async syntax proves non-blocking behavior; the team can monitor Schedulers, Event Loops, and Tasks after launch.
- Approve the M15 shortcut for indigo now.
- Require the M15 scoped measurement before approving the change.

**Answer:** Require the M15 scoped measurement before approving the change.

**Explanation:** M15-Q021 enacts mistake 4 from Schedulers, Event Loops, and Tasks; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M15-Q022

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** M15 Retained Memory case 1: Retained memory is 1800 x 12 KiB = 21600 KiB = 21.1 MiB.

**Explanation:** M15-Q022 uses retained memory from Memory Lifetime and Management and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M15-Q023

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** M15 Success Denominator case 2: Report 930/1000 = 93.0% against the same equivalent-work denominator.

**Explanation:** M15-Q023 uses success denominator from Schedulers, Event Loops, and Tasks and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M15-Q024

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** M15 Runtime Slots case 3: 12 - 8 = 4 tasks wait before any scheduling overhead.

**Explanation:** M15-Q024 uses runtime slots from Bounded Fan-out and Structured Cleanup and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M15-Q025

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** M15 diagnosis 1 identifies non-expanding deadline. The proving fields are cancellation.joined and cancellation.propagated; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M15-Q025 comes from emitted trial fields rather than fixture identifiers; Memory Lifetime and Management is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M15-Q026

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** M15 diagnosis 2 identifies non-expanding deadline. The proving fields are cancellation.joined and cancellation.propagated; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M15-Q026 comes from emitted trial fields rather than fixture identifiers; Schedulers, Event Loops, and Tasks is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M15-Q027

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** M15 diagnosis 3 identifies non-expanding deadline. The proving fields are cancellation.joined and cancellation.propagated; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M15-Q027 comes from emitted trial fields rather than fixture identifiers; Bounded Fan-out and Structured Cleanup is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M15-Q028

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** M15 diagnosis 4 identifies non-expanding deadline. The proving fields are cancellation.joined and cancellation.propagated; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M15-Q028 comes from emitted trial fields rather than fixture identifiers; Memory Visibility and Races is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M15-Q029

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** M15 diagnosis 5 identifies non-expanding deadline. The proving fields are cancellation.joined and cancellation.propagated; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M15-Q029 comes from emitted trial fields rather than fixture identifiers; Types, Serialization, and Validation is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M15-Q030

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** M15 diagnosis 6 identifies non-expanding deadline. The proving fields are cancellation.joined and cancellation.propagated; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M15-Q030 comes from emitted trial fields rather than fixture identifiers; Equivalent-work Runtime Measurement is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M15-Q031

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** M15 diagnosis 7 identifies non-expanding deadline. The proving fields are cancellation.joined and cancellation.propagated; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M15-Q031 comes from emitted trial fields rather than fixture identifiers; Northstar Polyglot Fan-out Tutorial is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M15-Q032

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** M15 diagnosis 8 identifies non-expanding deadline. The proving fields are cancellation.joined and cancellation.propagated; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M15-Q032 comes from emitted trial fields rather than fixture identifiers; Runtime Decision and Teach-back is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M15-Q033

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** M15 diagnosis 9 identifies non-expanding deadline. The proving fields are cancellation.joined and cancellation.propagated; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M15-Q033 comes from emitted trial fields rather than fixture identifiers; Memory Lifetime and Management is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M15-Q034

**Type:** `design_judgment`
**Difficulty:** `application`

**Answer:** For M15 decision 1, recommend against. The protected bound is 225 x 0.72 = 162.0/s, and the planned 198.0/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 198.0/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 36.0/s of lower-priority work.

**Explanation:** M15-Q034 turns on the forcing number from EX-01, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M15-Q035

**Type:** `design_judgment`
**Difficulty:** `synthesis`

**Answer:** For M15 decision 2, recommend against. The protected bound is 242 x 0.72 = 174.2/s, and the planned 213.0/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 213.0/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 38.8/s of lower-priority work.

**Explanation:** M15-Q035 turns on the forcing number from EX-02, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M15-Q036

**Type:** `design_judgment`
**Difficulty:** `recall`

**Answer:** For M15 decision 3, recommend against. The protected bound is 259 x 0.72 = 186.5/s, and the planned 227.9/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 227.9/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 41.4/s of lower-priority work.

**Explanation:** M15-Q036 turns on the forcing number from EX-03, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M15-Q037

**Type:** `design_judgment`
**Difficulty:** `application`

**Answer:** For M15 decision 4, recommend against. The protected bound is 276 x 0.72 = 198.7/s, and the planned 242.9/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 242.9/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 44.2/s of lower-priority work.

**Explanation:** M15-Q037 turns on the forcing number from EX-04, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M15-Q038

**Type:** `design_judgment`
**Difficulty:** `synthesis`

**Answer:** For M15 decision 5, recommend against. The protected bound is 293 x 0.72 = 211.0/s, and the planned 257.8/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 257.8/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 46.8/s of lower-priority work.

**Explanation:** M15-Q038 turns on the forcing number from EX-05, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.
