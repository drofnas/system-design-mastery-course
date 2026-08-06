# M10 Quiz Answer Key

This key covers all 38 questions for **Time, Coordination, and Consensus**. Use it after an attempt, or provide it with the LLM grading prompt for feedback.

## M10-Q001

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** It has no shared origin or bounded relationship with another host's clock.

**Explanation:** M10-Q001 uses self-check 1 from Physical Clocks, Drift, Skew, and Uncertainty; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M10-Q002

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** Correctness-critical authority must fail closed or use a non-time proof; silently extending the bound changes the failure model.

**Explanation:** M10-Q002 uses self-check 2 from Physical Clocks, Drift, Skew, and Uncertainty; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M10-Q003

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** No. Overlap means the clock evidence is insufficient to order them; a causal message path could still order the events. The practice radius is `2 ms + 40×300/1,000,000 = 14 ms`; pairwise skew is 28 ms. An 18 ms difference is insufficient.

**Explanation:** M10-Q003 uses self-check 3 from Physical Clocks, Drift, Skew, and Uncertainty; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M10-Q004

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** Only that the scalar order is compatible with possible causality; it does not prove `a → b`.

**Explanation:** M10-Q004 uses self-check 1 from Logical Clocks, Vector Clocks, and Causal Order; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M10-Q005

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** When neither vector is componentwise less than the other.

**Explanation:** M10-Q005 uses self-check 2 from Logical Clocks, Vector Clocks, and Causal Order; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M10-Q006

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** Separate nodes can sort only the events they know. Without agreement on the accepted set/prefix, they may authorize different commands. One valid trace is `a1 L1/[1,0]`, send `L2/[2,0]`, `a2 L3/[3,0]`; `b1 L1/[0,1]`, receive `L3/[2,2]`, `b2 L4/[2,3]`. `a2` and `b1` are concurrent; `b1 → b2`; neither `a2 → b2` nor `b2 → a2` follows.

**Explanation:** M10-Q006 uses self-check 3 from Logical Clocks, Vector Clocks, and Causal Order; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M10-Q007

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** Yes. A safe system may reject every write during quorum loss.

**Explanation:** M10-Q007 uses self-check 1 from Safety, Liveness, Failure Detectors, and Consensus Boundaries; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M10-Q008

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** Only that the heartbeat was not observed before the local deadline under the observer's clock/scheduler/network conditions.

**Explanation:** M10-Q008 uses self-check 2 from Safety, Liveness, Failure Detectors, and Consensus Boundaries; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M10-Q009

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** An operation-level invariant, a failure model requiring automatic agreement, and a comparison showing simpler authority/reconciliation choices are insufficient.

**Explanation:** M10-Q009 uses self-check 3 from Safety, Liveness, Failure Detectors, and Consensus Boundaries; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M10-Q010

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** It provides a shared witness; protocol state/selection rules make that witness constrain later decisions.

**Explanation:** M10-Q010 uses self-check 1 from Paxos, Raft, and Replicated-State-Machine Foundations; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M10-Q011

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** Consensus agrees on commands, not arbitrary local side effects. Different application results would violate replicated-state-machine equivalence.

**Explanation:** M10-Q011 uses self-check 2 from Paxos, Raft, and Replicated-State-Machine Foundations; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M10-Q012

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** No. Failover needs a new agreed epoch and an eligible log; the old leader may remain alive but partitioned. The proposer must choose X, the highest-numbered accepted value among its quorum. At a log index, the analogous obligation is that later leadership cannot choose a conflicting command after the earlier command is committed.

**Explanation:** M10-Q012 uses self-check 3 from Paxos, Raft, and Replicated-State-Machine Foundations; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M10-Q013

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Test the M10 scoped measurement and record the limiting assumption before approving the change.
- Approve synchronization has error, age, and for Physical Clocks, Drift, Skew, and Uncertainty; the local context makes that proposal familiar enough for review.
- Defer measurement until production for synchronization has error, age, and; the team can monitor Physical Clocks, Drift, Skew, and Uncertainty after launch.
- Approve the M10 shortcut for alpha now.

**Answer:** Test the M10 scoped measurement and record the limiting assumption before approving the change.

**Explanation:** M10-Q013 enacts mistake 1 from Physical Clocks, Drift, Skew, and Uncertainty; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M10-Q014

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Approve confusing monotonic duration with global order.: A monotonic local clock is for Physical Clocks, Drift, Skew, and Uncertainty; the local context makes that proposal familiar enough for review.
- Scope the M10 scoped measurement before approving the change.
- Defer measurement until production for confusing monotonic duration with global order.: A monotonic local clock is; the team can monitor Physical Clocks, Drift, Skew, and Uncertainty after launch.
- Approve the M10 shortcut for bravo now.

**Answer:** Scope the M10 scoped measurement before approving the change.

**Explanation:** M10-Q014 enacts mistake 2 from Physical Clocks, Drift, Skew, and Uncertainty; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M10-Q015

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Approve using a lease without process-pause bounds.: A client may stop executing for Physical Clocks, Drift, Skew, and Uncertainty; the local context makes that proposal familiar enough for review.
- Defer measurement until production for using a lease without process-pause bounds.: A client may stop executing; the team can monitor Physical Clocks, Drift, Skew, and Uncertainty after launch.
- Measure the M10 scoped measurement before approval.
- Approve the M10 shortcut for charlie now.

**Answer:** Measure the M10 scoped measurement before approval.

**Explanation:** M10-Q015 enacts mistake 3 from Physical Clocks, Drift, Skew, and Uncertainty; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M10-Q016

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Approve a resource needs a strictly ordered for Physical Clocks, Drift, Skew, and Uncertainty; the local context makes that proposal familiar enough for review.
- Defer measurement until production for a resource needs a strictly ordered; the team can monitor Physical Clocks, Drift, Skew, and Uncertainty after launch.
- Approve the M10 shortcut for delta now.
- Bound the M10 scoped measurement and record the limiting assumption before approving the change.

**Answer:** Bound the M10 scoped measurement and record the limiting assumption before approving the change.

**Explanation:** M10-Q016 enacts mistake 4 from Physical Clocks, Drift, Skew, and Uncertainty; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M10-Q017

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Freeze the M10 scoped measurement before approving the change.
- Approve `L(a) < L(b)` can hold for concurrent for Logical Clocks, Vector Clocks, and Causal Order; the local context makes that proposal familiar enough for review.
- Defer measurement until production for `L(a) < L(b)` can hold for concurrent; the team can monitor Logical Clocks, Vector Clocks, and Causal Order after launch.
- Approve the M10 shortcut for ember now.

**Answer:** Freeze the M10 scoped measurement before approving the change.

**Explanation:** M10-Q017 enacts mistake 1 from Logical Clocks, Vector Clocks, and Causal Order; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M10-Q018

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Approve it means no observed causal path for Logical Clocks, Vector Clocks, and Causal Order; the local context makes that proposal familiar enough for review.
- Preserve the M10 scoped measurement before approval.
- Defer measurement until production for it means no observed causal path; the team can monitor Logical Clocks, Vector Clocks, and Causal Order after launch.
- Approve the M10 shortcut for fable now.

**Answer:** Preserve the M10 scoped measurement before approval.

**Explanation:** M10-Q018 enacts mistake 2 from Logical Clocks, Vector Clocks, and Causal Order; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M10-Q019

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Approve dynamic membership needs versioned for Logical Clocks, Vector Clocks, and Causal Order; the local context makes that proposal familiar enough for review.
- Defer measurement until production for dynamic membership needs versioned; the team can monitor Logical Clocks, Vector Clocks, and Causal Order after launch.
- Model the M10 scoped measurement and record the limiting assumption before approving the change.
- Approve the M10 shortcut for harbor now.

**Answer:** Model the M10 scoped measurement and record the limiting assumption before approving the change.

**Explanation:** M10-Q019 enacts mistake 3 from Logical Clocks, Vector Clocks, and Causal Order; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M10-Q020

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Approve using a total tie-breaker as an invariant.: Stable display order cannot for Logical Clocks, Vector Clocks, and Causal Order; the local context makes that proposal familiar enough for review.
- Defer measurement until production for using a total tie-breaker as an invariant.: Stable display order cannot; the team can monitor Logical Clocks, Vector Clocks, and Causal Order after launch.
- Approve the M10 shortcut for indigo now.
- Account the M10 scoped measurement before approving the change.

**Answer:** Account the M10 scoped measurement before approving the change.

**Explanation:** M10-Q020 enacts mistake 4 from Logical Clocks, Vector Clocks, and Causal Order; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M10-Q021

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** M10 Clock Interval case 1: Pairwise uncertainty radius is 2 + 2 = 4 ms.

**Explanation:** M10-Q021 uses clock interval from Physical Clocks, Drift, Skew, and Uncertainty and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M10-Q022

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** M10 Clock Drift case 2: Drift is 40/1,000,000 x 300 s x 1000 = 12.0 ms.

**Explanation:** M10-Q022 uses clock drift from Logical Clocks, Vector Clocks, and Causal Order and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M10-Q023

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** M10 Skew Ratio case 3: Skew ratio is 120 / 40 = 3.0x.

**Explanation:** M10-Q023 uses skew ratio from Safety, Liveness, Failure Detectors, and Consensus Boundaries and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M10-Q024

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** M10 Raft Vote case 4: No. Terms tie at 4, so index decides; 18 < 20, so the voter should reject the vote.

**Explanation:** M10-Q024 uses Raft vote from Paxos, Raft, and Replicated-State-Machine Foundations and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M10-Q025

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** M10 diagnosis 1 identifies leader completeness. The proving fields are events.0.tick and events.1.tick; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M10-Q025 comes from emitted trial fields rather than fixture identifiers; Physical Clocks, Drift, Skew, and Uncertainty is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M10-Q026

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** M10 diagnosis 2 identifies Logical Clocks, Vector Clocks, and Causal Order evidence scope. The proving fields are events.0.tick and events.1.tick; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M10-Q026 comes from emitted trial fields rather than fixture identifiers; Logical Clocks, Vector Clocks, and Causal Order is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M10-Q027

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** M10 diagnosis 3 identifies stale-owner fencing. The proving fields are events.0.tick and events.1.tick; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M10-Q027 comes from emitted trial fields rather than fixture identifiers; Safety, Liveness, Failure Detectors, and Consensus Boundaries is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M10-Q028

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** M10 diagnosis 4 identifies Paxos, Raft, and Replicated-State-Machine Foundations evidence scope. The proving fields are events.0.tick and events.1.tick; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M10-Q028 comes from emitted trial fields rather than fixture identifiers; Paxos, Raft, and Replicated-State-Machine Foundations is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M10-Q029

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** M10 diagnosis 5 identifies election safety. The proving fields are events.0.tick and events.1.tick; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M10-Q029 comes from emitted trial fields rather than fixture identifiers; Raft Leader Election and Persistent Hard State is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M10-Q030

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** M10 diagnosis 6 identifies Raft Log Replication, Commitment, and Application evidence scope. The proving fields are events.0.tick and events.1.tick; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M10-Q030 comes from emitted trial fields rather than fixture identifiers; Raft Log Replication, Commitment, and Application is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M10-Q031

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** M10 diagnosis 7 identifies one logical client effect. The proving fields are client_results.0.logical_effects and client_results.0.result; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M10-Q031 comes from emitted trial fields rather than fixture identifiers; Clients, Linearizable Reads, Snapshots, and Compaction is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M10-Q032

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** M10 diagnosis 8 identifies Membership, Leases, Fencing, and Coordination Decisions evidence scope. The proving fields are client_results.0.logical_effects and client_results.0.result; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M10-Q032 comes from emitted trial fields rather than fixture identifiers; Membership, Leases, Fencing, and Coordination Decisions is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M10-Q033

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** M10 diagnosis 9 identifies linearizable authority read barrier. The proving fields are events.0.tick and events.1.tick; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M10-Q033 comes from emitted trial fields rather than fixture identifiers; Physical Clocks, Drift, Skew, and Uncertainty is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M10-Q034

**Type:** `design_judgment`
**Difficulty:** `application`

**Answer:** For M10 decision 1, recommend against. The protected bound is 210 x 0.72 = 151.2/s, and the planned 184.8/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 184.8/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 33.6/s of lower-priority work.

**Explanation:** M10-Q034 turns on the forcing number from EX-01, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M10-Q035

**Type:** `design_judgment`
**Difficulty:** `synthesis`

**Answer:** For M10 decision 2, recommend against. The protected bound is 227 x 0.72 = 163.4/s, and the planned 199.8/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 199.8/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 36.4/s of lower-priority work.

**Explanation:** M10-Q035 turns on the forcing number from EX-02, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M10-Q036

**Type:** `design_judgment`
**Difficulty:** `recall`

**Answer:** For M10 decision 3, recommend against. The protected bound is 244 x 0.72 = 175.7/s, and the planned 214.7/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 214.7/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 39.0/s of lower-priority work.

**Explanation:** M10-Q036 turns on the forcing number from EX-03, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M10-Q037

**Type:** `design_judgment`
**Difficulty:** `application`

**Answer:** For M10 decision 4, recommend against. The protected bound is 261 x 0.72 = 187.9/s, and the planned 229.7/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 229.7/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 41.8/s of lower-priority work.

**Explanation:** M10-Q037 turns on the forcing number from EX-04, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M10-Q038

**Type:** `design_judgment`
**Difficulty:** `synthesis`

**Answer:** For M10 decision 5, recommend against. The protected bound is 278 x 0.72 = 200.2/s, and the planned 244.6/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 244.6/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 44.4/s of lower-priority work.

**Explanation:** M10-Q038 turns on the forcing number from EX-05, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.
