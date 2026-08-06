# M08 Quiz Answer Key

This key covers all 37 questions for **Transactions, Concurrency, and Recovery**. Use it after an attempt, or provide it with the LLM grading prompt for feedback.

## M08-Q001

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** It has no falsifiable condition or named authority. 2. The constraint is evaluated at the commit/write boundary against concurrent database state; pre-checks can become stale. 3. Coupling it enlarges contention and recovery scope while adding no authoritative correctness if it can be reconstructed.

**Explanation:** M08-Q001 uses self-check 1 from Invariants and Transaction Boundaries; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M08-Q002

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** M08 L01 answer: preserve the Invariants and Transaction Boundaries mechanism and its evidence scope.

**Explanation:** M08-Q002 uses self-check 2 from Invariants and Transaction Boundaries; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M08-Q003

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** M08 L01 answer: preserve the Invariants and Transaction Boundaries mechanism and its evidence scope.

**Explanation:** M08-Q003 uses self-check 3 from Invariants and Transaction Boundaries; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M08-Q004

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** Yes; write skew uses committed snapshots. 2. Lost update overwrites the same logical value; write skew uses disjoint writes whose combined effect violates a predicate. 3. Roll back and retry the entire transaction from fresh state, subject to bounded eligibility and deadline rules.

**Explanation:** M08-Q004 uses self-check 1 from Histories, Serializability, and Isolation Anomalies; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M08-Q005

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** M08 L02 answer: preserve the Histories, Serializability, and Isolation Anomalies mechanism and its evidence scope.

**Explanation:** M08-Q005 uses self-check 2 from Histories, Serializability, and Isolation Anomalies; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M08-Q006

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** M08 L02 answer: preserve the Histories, Serializability, and Isolation Anomalies mechanism and its evidence scope.

**Explanation:** M08-Q006 uses self-check 3 from Histories, Serializability, and Isolation Anomalies; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M08-Q007

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** Other code paths, database internals, and lock upgrades can introduce new orders. 2. The whole transaction, snapshot, locks, authorization decision, and deadline-derived work. 3. A concurrent row may appear after the check; a constraint or protected predicate decides against commit-time state.

**Explanation:** M08-Q007 uses self-check 1 from Locks, Two-Phase Locking, Deadlocks, and Retries; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M08-Q008

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** M08 L03 answer: preserve the Locks, Two-Phase Locking, Deadlocks, and Retries mechanism and its evidence scope.

**Explanation:** M08-Q008 uses self-check 2 from Locks, Two-Phase Locking, Deadlocks, and Retries; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M08-Q009

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** M08 L03 answer: preserve the Locks, Two-Phase Locking, Deadlocks, and Retries mechanism and its evidence scope.

**Explanation:** M08-Q009 uses self-check 3 from Locks, Two-Phase Locking, Deadlocks, and Retries; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M08-Q010

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** They can jointly falsify a predicate read by both transactions. 2. Work is discarded after reads/computation, then repeated under continued contention.

**Explanation:** M08-Q010 uses self-check 1 from Optimistic Control, MVCC, Snapshots, and Write Skew; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M08-Q011

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** Oldest active snapshot/version-retention age and retained bytes, paired with cleanup lag and transaction age.

**Explanation:** M08-Q011 uses self-check 2 from Optimistic Control, MVCC, Snapshots, and Write Skew; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M08-Q012

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** M08 L04 answer: preserve the Optimistic Control, MVCC, Snapshots, and Write Skew mechanism and its evidence scope.

**Explanation:** M08-Q012 uses self-check 3 from Optimistic Control, MVCC, Snapshots, and Write Skew; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M08-Q013

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** It improves authorization and feedback, while the constraint remains the concurrency-safe final guard. 2. No; it creates a durable intent and a retriable/reconcilable workflow. 3. Authority identity/version or LSN, rebuild rule, and freshness/validity state.

**Explanation:** M08-Q013 uses self-check 1 from Constraints, Authority, and Atomic Workflows; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M08-Q014

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Calculate the M08 scoped measurement and record the limiting assumption before approving the change.
- Approve calling a transaction “ACID” without naming the admitted histories for Invariants and Transaction Boundaries; the local context makes that proposal familiar enough for review.
- Defer measurement until production for calling a transaction “ACID” without naming the admitted histories; the team can monitor Invariants and Transaction Boundaries after launch.
- Approve the M08 shortcut for alpha now.

**Answer:** Calculate the M08 scoped measurement and record the limiting assumption before approving the change.

**Explanation:** M08-Q014 enacts mistake 1 from Invariants and Transaction Boundaries; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M08-Q015

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Approve putting network calls inside a transaction and assuming atomicity crosses the for Invariants and Transaction Boundaries; the local context makes that proposal familiar enough for review.
- Draw the M08 scoped measurement before approving the change.
- Defer measurement until production for putting network calls inside a transaction and assuming atomicity crosses the; the team can monitor Invariants and Transaction Boundaries after launch.
- Approve the M08 shortcut for bravo now.

**Answer:** Draw the M08 scoped measurement before approving the change.

**Explanation:** M08-Q015 enacts mistake 2 from Invariants and Transaction Boundaries; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M08-Q016

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Approve treating a cache or summary as authority because it is convenient to query for Invariants and Transaction Boundaries; the local context makes that proposal familiar enough for review.
- Defer measurement until production for treating a cache or summary as authority because it is convenient to query; the team can monitor Invariants and Transaction Boundaries after launch.
- Separate the M08 scoped measurement before approval.
- Approve the M08 shortcut for charlie now.

**Answer:** Separate the M08 scoped measurement before approval.

**Explanation:** M08-Q016 enacts mistake 3 from Invariants and Transaction Boundaries; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M08-Q017

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Approve widening every boundary “for safety,” increasing lock duration and recovery for Invariants and Transaction Boundaries; the local context makes that proposal familiar enough for review.
- Defer measurement until production for widening every boundary “for safety,” increasing lock duration and recovery; the team can monitor Invariants and Transaction Boundaries after launch.
- Approve the M08 shortcut for delta now.
- Verify the M08 scoped measurement and record the limiting assumption before approving the change.

**Answer:** Verify the M08 scoped measurement and record the limiting assumption before approving the change.

**Explanation:** M08-Q017 enacts mistake 4 from Invariants and Transaction Boundaries; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M08-Q018

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Compare the M08 scoped measurement before approving the change.
- Approve listing ANSI anomaly names without drawing the violating schedule for Histories, Serializability, and Isolation Anomalies; the local context makes that proposal familiar enough for review.
- Defer measurement until production for listing ANSI anomaly names without drawing the violating schedule; the team can monitor Histories, Serializability, and Isolation Anomalies after launch.
- Approve the M08 shortcut for ember now.

**Answer:** Compare the M08 scoped measurement before approving the change.

**Explanation:** M08-Q018 enacts mistake 1 from Histories, Serializability, and Isolation Anomalies; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M08-Q019

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Approve assuming repeatable read or snapshot means serializable in every database for Histories, Serializability, and Isolation Anomalies; the local context makes that proposal familiar enough for review.
- Reject the M08 scoped measurement before approval.
- Defer measurement until production for assuming repeatable read or snapshot means serializable in every database; the team can monitor Histories, Serializability, and Isolation Anomalies after launch.
- Approve the M08 shortcut for fable now.

**Answer:** Reject the M08 scoped measurement before approval.

**Explanation:** M08-Q019 enacts mistake 2 from Histories, Serializability, and Isolation Anomalies; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M08-Q020

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Approve retrying only the failed statement after the transaction snapshot is invalid for Histories, Serializability, and Isolation Anomalies; the local context makes that proposal familiar enough for review.
- Defer measurement until production for retrying only the failed statement after the transaction snapshot is invalid; the team can monitor Histories, Serializability, and Isolation Anomalies after launch.
- Trace the M08 scoped measurement and record the limiting assumption before approving the change.
- Approve the M08 shortcut for harbor now.

**Answer:** Trace the M08 scoped measurement and record the limiting assumption before approving the change.

**Explanation:** M08-Q020 enacts mistake 3 from Histories, Serializability, and Isolation Anomalies; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M08-Q021

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Approve raising isolation globally without measuring abort and latency costs for Histories, Serializability, and Isolation Anomalies; the local context makes that proposal familiar enough for review.
- Defer measurement until production for raising isolation globally without measuring abort and latency costs; the team can monitor Histories, Serializability, and Isolation Anomalies after launch.
- Approve the M08 shortcut for indigo now.
- Require the M08 scoped measurement before approving the change.

**Answer:** Require the M08 scoped measurement before approving the change.

**Explanation:** M08-Q021 enacts mistake 4 from Histories, Serializability, and Isolation Anomalies; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M08-Q022

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** M08 Rpo case 1: Observable RPO is 20 - 7 = 13 minutes if the missing middle cannot be replayed.

**Explanation:** M08-Q022 uses RPO from Invariants and Transaction Boundaries and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M08-Q023

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** M08 Rpo case 2: Observable RPO is 20 - 7 = 13 minutes if the missing middle cannot be replayed.

**Explanation:** M08-Q023 uses RPO from Histories, Serializability, and Isolation Anomalies and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M08-Q024

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** M08 Recovery State Enumeration case 3: The enumeration has 4 x 3 = 12 state cases.

**Explanation:** M08-Q024 uses recovery state enumeration from Locks, Two-Phase Locking, Deadlocks, and Retries and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M08-Q025

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** M08 diagnosis 1 identifies Invariants and Transaction Boundaries evidence scope. The proving fields are initial_state.completed_exposures and invariants.0.value; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M08-Q025 comes from emitted trial fields rather than fixture identifiers; Invariants and Transaction Boundaries is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M08-Q026

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** M08 diagnosis 2 identifies Histories, Serializability, and Isolation Anomalies evidence scope. The proving fields are initial_state.completed_exposures and invariants.0.value; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M08-Q026 comes from emitted trial fields rather than fixture identifiers; Histories, Serializability, and Isolation Anomalies is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M08-Q027

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** M08 diagnosis 3 identifies Locks, Two-Phase Locking, Deadlocks, and Retries evidence scope. The proving fields are initial_state.certified_controllers and invariants.0.value; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M08-Q027 comes from emitted trial fields rather than fixture identifiers; Locks, Two-Phase Locking, Deadlocks, and Retries is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M08-Q028

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** M08 diagnosis 4 identifies Optimistic Control, MVCC, Snapshots, and Write Skew evidence scope. The proving fields are initial_state.certified_controllers and invariants.0.value; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M08-Q028 comes from emitted trial fields rather than fixture identifiers; Optimistic Control, MVCC, Snapshots, and Write Skew is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M08-Q029

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** M08 diagnosis 5 identifies Constraints, Authority, and Atomic Workflows evidence scope. The proving fields are initial_state.completed_transfers and invariants.0.value; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M08-Q029 comes from emitted trial fields rather than fixture identifiers; Constraints, Authority, and Atomic Workflows is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M08-Q030

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** M08 diagnosis 6 identifies WAL, Checkpoints, Redo/Undo, and Group Commit evidence scope. The proving fields are initial_state.completed_transfers and invariants.0.value; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M08-Q030 comes from emitted trial fields rather than fixture identifiers; WAL, Checkpoints, Redo/Undo, and Group Commit is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M08-Q031

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** M08 diagnosis 7 identifies Backups, PITR, Restore Validation, and Objectives evidence scope. The proving fields are initial_state.durable_exposure and invariants.0.value; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M08-Q031 comes from emitted trial fields rather than fixture identifiers; Backups, PITR, Restore Validation, and Objectives is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M08-Q032

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** M08 diagnosis 8 identifies Transaction and Recovery Decisions evidence scope. The proving fields are initial_state.durable_exposure and invariants.0.value; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M08-Q032 comes from emitted trial fields rather than fixture identifiers; Transaction and Recovery Decisions is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M08-Q033

**Type:** `design_judgment`
**Difficulty:** `recall`

**Answer:** For M08 decision 1, recommend against. The protected bound is 204 x 0.72 = 146.9/s, and the planned 179.5/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 179.5/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 32.6/s of lower-priority work.

**Explanation:** M08-Q033 turns on the forcing number from EX-01, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M08-Q034

**Type:** `design_judgment`
**Difficulty:** `application`

**Answer:** For M08 decision 2, recommend against. The protected bound is 221 x 0.72 = 159.1/s, and the planned 194.5/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 194.5/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 35.4/s of lower-priority work.

**Explanation:** M08-Q034 turns on the forcing number from EX-02, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M08-Q035

**Type:** `design_judgment`
**Difficulty:** `synthesis`

**Answer:** For M08 decision 3, recommend against. The protected bound is 238 x 0.72 = 171.4/s, and the planned 209.4/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 209.4/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 38.0/s of lower-priority work.

**Explanation:** M08-Q035 turns on the forcing number from EX-03, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M08-Q036

**Type:** `design_judgment`
**Difficulty:** `recall`

**Answer:** For M08 decision 4, recommend against. The protected bound is 255 x 0.72 = 183.6/s, and the planned 224.4/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 224.4/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 40.8/s of lower-priority work.

**Explanation:** M08-Q036 turns on the forcing number from EX-04, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M08-Q037

**Type:** `design_judgment`
**Difficulty:** `application`

**Answer:** For M08 decision 5, recommend against. The protected bound is 272 x 0.72 = 195.8/s, and the planned 239.4/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 239.4/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 43.6/s of lower-priority work.

**Explanation:** M08-Q037 turns on the forcing number from EX-05, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.
