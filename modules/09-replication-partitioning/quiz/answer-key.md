# M09 Quiz Answer Key

This key covers all 43 questions for **Replication and Partitioning**. Use it after an attempt, or provide it with the LLM grading prompt for feedback.

## M09-Q001

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** No. It is scoped to one session unless a stronger contract is also present.

**Explanation:** M09-Q001 uses self-check 1 from Operation Semantics and Session Guarantees; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M09-Q002

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** Yes. A session can observe versions 5, 5, 6 while authority is already at 9.

**Explanation:** M09-Q002 uses self-check 2 from Operation Semantics and Session Guarantees; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M09-Q003

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** A unit and bound, reference version/time, measurement point, failure action, and oracle.

**Explanation:** M09-Q003 uses self-check 3 from Operation Semantics and Session Guarantees; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M09-Q004

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** Eventual convergence permits a window where conflicting owners can act; the invariant is violated before convergence repairs state.

**Explanation:** M09-Q004 uses self-check 4 from Operation Semantics and Session Guarantees; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M09-Q005

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** No. The acknowledgement and placement contracts must prove durability and independence.

**Explanation:** M09-Q005 uses self-check 1 from Replication Topologies and Acknowledgement Boundaries; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M09-Q006

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** Detect concurrent versions and define who or what resolves them without violating the business invariant.

**Explanation:** M09-Q006 uses self-check 2 from Replication Topologies and Acknowledgement Boundaries; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M09-Q007

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** Followers can lag and the router may select one without a minimum-version rule.

**Explanation:** M09-Q007 uses self-check 3 from Replication Topologies and Acknowledgement Boundaries; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M09-Q008

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** Explicitly reject authority-changing writes or recover the known authority; do not invent an unproved election.

**Explanation:** M09-Q008 uses self-check 4 from Replication Topologies and Acknowledgement Boundaries; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M09-Q009

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** Both: 3+3>5 and 2×3>5.

**Explanation:** M09-Q009 uses self-check 1 from Quorums, Intersections, and Hidden Assumptions; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M09-Q010

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** Write/write intersection fails because 4 is not greater than 5.

**Explanation:** M09-Q010 uses self-check 2 from Quorums, Intersections, and Hidden Assumptions; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M09-Q011

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** Not from arithmetic alone; it may need to compare versions and meet the operation's freshness rule.

**Explanation:** M09-Q011 uses self-check 3 from Quorums, Intersections, and Hidden Assumptions; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M09-Q012

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** The formal CAP definition and a product's bounded success SLO measure different outcomes; mixing them produces false claims.

**Explanation:** M09-Q012 uses self-check 4 from Quorums, Intersections, and Hidden Assumptions; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M09-Q013

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** No. Clock error and concurrent writers can make timestamps misleading.

**Explanation:** M09-Q013 uses self-check 1 from Versions, Conflicts, Repair, and Convergence; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M09-Q014

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** A key that is never read is never compared.

**Explanation:** M09-Q014 uses self-check 2 from Versions, Conflicts, Repair, and Convergence; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M09-Q015

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Scope the M09 scoped measurement and record the limiting assumption before approving the change.
- Approve it over-constrains cheap reads or for Operation Semantics and Session Guarantees; the local context makes that proposal familiar enough for review.
- Defer measurement until production for it over-constrains cheap reads or; the team can monitor Operation Semantics and Session Guarantees after launch.
- Approve the M09 shortcut for alpha now.

**Answer:** Scope the M09 scoped measurement and record the limiting assumption before approving the change.

**Explanation:** M09-Q015 enacts mistake 1 from Operation Semantics and Session Guarantees; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M09-Q016

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Approve equating acknowledgement with universal visibility:: an asynchronous for Operation Semantics and Session Guarantees; the local context makes that proposal familiar enough for review.
- Measure the M09 scoped measurement before approving the change.
- Defer measurement until production for equating acknowledgement with universal visibility:: an asynchronous; the team can monitor Operation Semantics and Session Guarantees after launch.
- Approve the M09 shortcut for bravo now.

**Answer:** Measure the M09 scoped measurement before approving the change.

**Explanation:** M09-Q016 enacts mistake 2 from Operation Semantics and Session Guarantees; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M09-Q017

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Approve using wall-clock timestamps as version proof:: clock skew can order events for Operation Semantics and Session Guarantees; the local context makes that proposal familiar enough for review.
- Defer measurement until production for using wall-clock timestamps as version proof:: clock skew can order events; the team can monitor Operation Semantics and Session Guarantees after launch.
- Bound the M09 scoped measurement before approval.
- Approve the M09 shortcut for charlie now.

**Answer:** Bound the M09 scoped measurement before approval.

**Explanation:** M09-Q017 enacts mistake 3 from Operation Semantics and Session Guarantees; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M09-Q018

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Approve tTL bounds cache age only under for Operation Semantics and Session Guarantees; the local context makes that proposal familiar enough for review.
- Defer measurement until production for tTL bounds cache age only under; the team can monitor Operation Semantics and Session Guarantees after launch.
- Approve the M09 shortcut for delta now.
- Freeze the M09 scoped measurement and record the limiting assumption before approving the change.

**Answer:** Freeze the M09 scoped measurement and record the limiting assumption before approving the change.

**Explanation:** M09-Q018 enacts mistake 4 from Operation Semantics and Session Guarantees; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M09-Q019

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Preserve the M09 scoped measurement before approving the change.
- Approve returning an older version converts for Operation Semantics and Session Guarantees; the local context makes that proposal familiar enough for review.
- Defer measurement until production for returning an older version converts; the team can monitor Operation Semantics and Session Guarantees after launch.
- Approve the M09 shortcut for ember now.

**Answer:** Preserve the M09 scoped measurement before approving the change.

**Explanation:** M09-Q019 enacts mistake 5 from Operation Semantics and Session Guarantees; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M09-Q020

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Approve deletion, corruption, and operator error for Replication Topologies and Acknowledgement Boundaries; the local context makes that proposal familiar enough for review.
- Model the M09 scoped measurement before approval.
- Defer measurement until production for deletion, corruption, and operator error; the team can monitor Replication Topologies and Acknowledgement Boundaries after launch.
- Approve the M09 shortcut for fable now.

**Answer:** Model the M09 scoped measurement before approval.

**Explanation:** M09-Q020 enacts mistake 1 from Replication Topologies and Acknowledgement Boundaries; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M09-Q021

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Approve copies may share a failure domain for Replication Topologies and Acknowledgement Boundaries; the local context makes that proposal familiar enough for review.
- Defer measurement until production for copies may share a failure domain; the team can monitor Replication Topologies and Acknowledgement Boundaries after launch.
- Account the M09 scoped measurement and record the limiting assumption before approving the change.
- Approve the M09 shortcut for harbor now.

**Answer:** Account the M09 scoped measurement and record the limiting assumption before approving the change.

**Explanation:** M09-Q021 enacts mistake 2 from Replication Topologies and Acknowledgement Boundaries; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M09-Q022

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Approve latency improves while users for Replication Topologies and Acknowledgement Boundaries; the local context makes that proposal familiar enough for review.
- Defer measurement until production for latency improves while users; the team can monitor Replication Topologies and Acknowledgement Boundaries after launch.
- Approve the M09 shortcut for indigo now.
- Test the M09 scoped measurement before approving the change.

**Answer:** Test the M09 scoped measurement before approving the change.

**Explanation:** M09-Q022 enacts mistake 3 from Replication Topologies and Acknowledgement Boundaries; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M09-Q023

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Scope the M09 scoped measurement before approval.
- Approve adding multi-leader for availability without conflict ownership:: the for Replication Topologies and Acknowledgement Boundaries; the local context makes that proposal familiar enough for review.
- Defer measurement until production for adding multi-leader for availability without conflict ownership:: the; the team can monitor Replication Topologies and Acknowledgement Boundaries after launch.
- Approve the M09 shortcut for juniper now.

**Answer:** Scope the M09 scoped measurement before approval.

**Explanation:** M09-Q023 enacts mistake 4 from Replication Topologies and Acknowledgement Boundaries; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M09-Q024

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Approve safe authority change requires coordination for Replication Topologies and Acknowledgement Boundaries; the local context makes that proposal familiar enough for review.
- Measure the M09 scoped measurement and record the limiting assumption before approving the change.
- Defer measurement until production for safe authority change requires coordination; the team can monitor Replication Topologies and Acknowledgement Boundaries after launch.
- Approve the M09 shortcut for keystone now.

**Answer:** Measure the M09 scoped measurement and record the limiting assumption before approving the change.

**Explanation:** M09-Q024 enacts mistake 5 from Replication Topologies and Acknowledgement Boundaries; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M09-Q025

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** M09 Repair Bytes case 1: Bytes are 10,000 x 1024 = 10,240,000; that is 9.77 MiB.

**Explanation:** M09-Q025 uses repair bytes from Operation Semantics and Session Guarantees and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M09-Q026

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** M09 Key Movement case 2: Movement ratio is 2 / 8 = 0.25, or 25%.

**Explanation:** M09-Q026 uses key movement from Replication Topologies and Acknowledgement Boundaries and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M09-Q027

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** M09 Copy Time case 3: 200 GiB is 204800 MiB; 204800 / 40 = 5120 seconds, or 1.42 hours.

**Explanation:** M09-Q027 uses copy time from Quorums, Intersections, and Hidden Assumptions and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M09-Q028

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** M09 Skew Ratio case 4: Skew ratio is 120 / 40 = 3.0x.

**Explanation:** M09-Q028 uses skew ratio from Versions, Conflicts, Repair, and Convergence and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M09-Q029

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** M09 Serialization case 5: Serialization is 280 KiB x 8 / 900 Kbps = 2.49 seconds, ignoring protocol overhead.

**Explanation:** M09-Q029 uses serialization from Partitioning, Consistent Hashing, and Resharding and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M09-Q030

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** M09 Quorum case 6: It can lose 2 replicas and still collect 3 acknowledgements.

**Explanation:** M09-Q030 uses quorum from Hot Keys, Skew, Fairness, and Tenant Isolation and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M09-Q031

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** M09 diagnosis 1 identifies fault exposes the predicted invariant failure. The proving fields are acknowledgements.ambiguous and acknowledgements.attempted; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M09-Q031 comes from emitted trial fields rather than fixture identifiers; Operation Semantics and Session Guarantees is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M09-Q032

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** M09 diagnosis 2 identifies Replication Topologies and Acknowledgement Boundaries evidence scope. The proving fields are acknowledgements.ambiguous and acknowledgements.attempted; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M09-Q032 comes from emitted trial fields rather than fixture identifiers; Replication Topologies and Acknowledgement Boundaries is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M09-Q033

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** M09 diagnosis 3 identifies fault exposes the predicted invariant failure. The proving fields are acknowledgements.ambiguous and acknowledgements.attempted; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M09-Q033 comes from emitted trial fields rather than fixture identifiers; Quorums, Intersections, and Hidden Assumptions is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M09-Q034

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** M09 diagnosis 4 identifies Versions, Conflicts, Repair, and Convergence evidence scope. The proving fields are acknowledgements.ambiguous and acknowledgements.attempted; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M09-Q034 comes from emitted trial fields rather than fixture identifiers; Versions, Conflicts, Repair, and Convergence is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M09-Q035

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** M09 diagnosis 5 identifies fault exposes the predicted invariant failure. The proving fields are acknowledgements.ambiguous and acknowledgements.attempted; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M09-Q035 comes from emitted trial fields rather than fixture identifiers; Partitioning, Consistent Hashing, and Resharding is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M09-Q036

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** M09 diagnosis 6 identifies Hot Keys, Skew, Fairness, and Tenant Isolation evidence scope. The proving fields are acknowledgements.ambiguous and acknowledgements.attempted; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M09-Q036 comes from emitted trial fields rather than fixture identifiers; Hot Keys, Skew, Fairness, and Tenant Isolation is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M09-Q037

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** M09 diagnosis 7 identifies blind retry duplicates the logical write after an ambiguous acknowledgement. The proving fields are acknowledgements.ambiguous and acknowledgements.attempted; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M09-Q037 comes from emitted trial fields rather than fixture identifiers; CAP, PACELC, Regional Placement, Security, and Cost is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M09-Q038

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** M09 diagnosis 8 identifies Data-Placement Decisions, Migration, and Ownership evidence scope. The proving fields are acknowledgements.ambiguous and acknowledgements.attempted; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M09-Q038 comes from emitted trial fields rather than fixture identifiers; Data-Placement Decisions, Migration, and Ownership is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M09-Q039

**Type:** `design_judgment`
**Difficulty:** `recall`

**Answer:** For M09 decision 1, recommend against. The protected bound is 207 x 0.72 = 149.0/s, and the planned 182.2/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 182.2/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 33.2/s of lower-priority work.

**Explanation:** M09-Q039 turns on the forcing number from EX-01, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M09-Q040

**Type:** `design_judgment`
**Difficulty:** `application`

**Answer:** For M09 decision 2, recommend against. The protected bound is 224 x 0.72 = 161.3/s, and the planned 197.1/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 197.1/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 35.8/s of lower-priority work.

**Explanation:** M09-Q040 turns on the forcing number from EX-02, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M09-Q041

**Type:** `design_judgment`
**Difficulty:** `synthesis`

**Answer:** For M09 decision 3, recommend against. The protected bound is 241 x 0.72 = 173.5/s, and the planned 212.1/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 212.1/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 38.6/s of lower-priority work.

**Explanation:** M09-Q041 turns on the forcing number from EX-03, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M09-Q042

**Type:** `design_judgment`
**Difficulty:** `recall`

**Answer:** For M09 decision 4, recommend against. The protected bound is 258 x 0.72 = 185.8/s, and the planned 227.0/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 227.0/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 41.2/s of lower-priority work.

**Explanation:** M09-Q042 turns on the forcing number from EX-04, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M09-Q043

**Type:** `design_judgment`
**Difficulty:** `application`

**Answer:** For M09 decision 5, recommend against. The protected bound is 275 x 0.72 = 198.0/s, and the planned 242.0/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 242.0/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 44.0/s of lower-priority work.

**Explanation:** M09-Q043 turns on the forcing number from EX-05, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.
