# M08 Quiz Answer Key

This key covers all 37 questions for **Transactions, Concurrency, and Recovery**. Use it after an attempt, or provide it with the LLM grading prompt for feedback.

## M08-Q001

**Type:** `short_answer`  
**Difficulty:** `recall`

**Answer:** It has no falsifiable condition or named authority. 2. The constraint is evaluated at the commit/write boundary against concurrent database state; pre-checks can become stale. 3. Coupling it enlarges contention and recovery scope while adding no authoritative correctness if it can be reconstructed

**Explanation:** The cited self-check in L01 tests whether the learner can connect Invariants and Transaction Boundaries to the module mechanism without replacing evidence with labels. This explanation is specific to M08-Q001 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M08-Q002

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** Map an invariant to authority, writers, a minimal atomic boundary, an enforcement point, and a falsifiable proof. Distinguish database consistency from application correctness

**Explanation:** The cited self-check in L01 tests whether the learner can connect Invariants and Transaction Boundaries to the module mechanism without replacing evidence with labels. This explanation is specific to M08-Q002 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M08-Q003

**Type:** `short_answer`  
**Difficulty:** `synthesis`

**Answer:** Map an invariant to authority, writers, a minimal atomic boundary, an enforcement point, and a falsifiable proof. Distinguish database consistency from application correctness

**Explanation:** The cited self-check in L01 tests whether the learner can connect Invariants and Transaction Boundaries to the module mechanism without replacing evidence with labels. This explanation is specific to M08-Q003 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M08-Q004

**Type:** `short_answer`  
**Difficulty:** `recall`

**Answer:** Yes; write skew uses committed snapshots. 2. Lost update overwrites the same logical value; write skew uses disjoint writes whose combined effect violates a predicate. 3. Roll back and retry the entire transaction from fresh state, subject to bounded eligibility and deadline rules

**Explanation:** The cited self-check in L02 tests whether the learner can connect Histories, Serializability, and Isolation Anomalies to the module mechanism without replacing evidence with labels. This explanation is specific to M08-Q004 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M08-Q005

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** Read a history, construct dependencies, identify lost update and write skew, and select an isolation claim per operation rather than per product

**Explanation:** The cited self-check in L02 tests whether the learner can connect Histories, Serializability, and Isolation Anomalies to the module mechanism without replacing evidence with labels. This explanation is specific to M08-Q005 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M08-Q006

**Type:** `short_answer`  
**Difficulty:** `synthesis`

**Answer:** Read a history, construct dependencies, identify lost update and write skew, and select an isolation claim per operation rather than per product

**Explanation:** The cited self-check in L02 tests whether the learner can connect Histories, Serializability, and Isolation Anomalies to the module mechanism without replacing evidence with labels. This explanation is specific to M08-Q006 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M08-Q007

**Type:** `short_answer`  
**Difficulty:** `recall`

**Answer:** Other code paths, database internals, and lock upgrades can introduce new orders. 2. The whole transaction, snapshot, locks, authorization decision, and deadline-derived work. 3. A concurrent row may appear after the check; a constraint or protected predicate decides against commit-time state

**Explanation:** The cited self-check in L03 tests whether the learner can connect Locks, Two-Phase Locking, Deadlocks, and Retries to the module mechanism without replacing evidence with labels. This explanation is specific to M08-Q007 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M08-Q008

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** Derive lock compatibility and wait-for graphs, explain strict 2PL, recover from deadlock, and implement bounded whole-transaction retry

**Explanation:** The cited self-check in L03 tests whether the learner can connect Locks, Two-Phase Locking, Deadlocks, and Retries to the module mechanism without replacing evidence with labels. This explanation is specific to M08-Q008 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M08-Q009

**Type:** `short_answer`  
**Difficulty:** `synthesis`

**Answer:** Derive lock compatibility and wait-for graphs, explain strict 2PL, recover from deadlock, and implement bounded whole-transaction retry

**Explanation:** The cited self-check in L03 tests whether the learner can connect Locks, Two-Phase Locking, Deadlocks, and Retries to the module mechanism without replacing evidence with labels. This explanation is specific to M08-Q009 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M08-Q010

**Type:** `short_answer`  
**Difficulty:** `recall`

**Answer:** They can jointly falsify a predicate read by both transactions. 2. Work is discarded after reads/computation, then repeated under continued contention

**Explanation:** The cited self-check in L04 tests whether the learner can connect Optimistic Control, MVCC, Snapshots, and Write Skew to the module mechanism without replacing evidence with labels. This explanation is specific to M08-Q010 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M08-Q011

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** Oldest active snapshot/version-retention age and retained bytes, paired with cleanup lag and transaction age

**Explanation:** The cited self-check in L04 tests whether the learner can connect Optimistic Control, MVCC, Snapshots, and Write Skew to the module mechanism without replacing evidence with labels. This explanation is specific to M08-Q011 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M08-Q012

**Type:** `multiple_choice`  
**Difficulty:** `application`

**Choices:**

- Keep Invariants and Transaction Boundaries scoped to its stated evidence and boundary.
- Make the documented mistake: Calling a transaction “ACID” without naming the admitted histories
- Choose the familiar tool before checking whether Calling a transaction “ACID” without naming the admitted histories a.
- Treat Calling a transaction “ACID” without naming the admitted histories as complete proof without the lesson boundary

**Answer:** Keep Invariants and Transaction Boundaries scoped to its stated evidence and boundary.

**Explanation:** The distractors are anchored in the mistake list for L01; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M08-Q012 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M08-Q013

**Type:** `multiple_choice`  
**Difficulty:** `synthesis`

**Choices:**

- Make the documented mistake: Putting network calls inside a transaction and assuming atomicity
- Keep Invariants and Transaction Boundaries scoped to its stated evidence and boundary.
- Choose the familiar tool before checking whether Putting network calls inside a transaction and assuming atomicity cr.
- Treat Putting network calls inside a transaction and assuming atomicity cro as complete proof without the lesson boun.

**Answer:** Keep Invariants and Transaction Boundaries scoped to its stated evidence and boundary.

**Explanation:** The distractors are anchored in the mistake list for L01; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M08-Q013 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M08-Q014

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Choices:**

- Make the documented mistake: Treating a cache or summary as authority because it is convenient
- Choose the familiar tool before checking whether Treating a cache or summary as authority because it is convenient to.
- Keep Invariants and Transaction Boundaries scoped to its stated evidence and boundary.
- Treat Treating a cache or summary as authority because it is convenient to as complete proof without the lesson bound.

**Answer:** Keep Invariants and Transaction Boundaries scoped to its stated evidence and boundary.

**Explanation:** The distractors are anchored in the mistake list for L01; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M08-Q014 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M08-Q015

**Type:** `multiple_choice`  
**Difficulty:** `application`

**Choices:**

- Make the documented mistake: Widening every boundary “for safety,” increasing lock duration and
- Treat Widening every boundary “for safety,” increasing lock duration and re as complete proof without the lesson boun.
- Choose the familiar tool before checking whether Widening every boundary “for safety,” increasing lock duration and r.
- Keep Invariants and Transaction Boundaries scoped to its stated evidence and boundary.

**Answer:** Keep Invariants and Transaction Boundaries scoped to its stated evidence and boundary.

**Explanation:** The distractors are anchored in the mistake list for L01; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M08-Q015 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M08-Q016

**Type:** `multiple_choice`  
**Difficulty:** `synthesis`

**Choices:**

- Keep Histories, Serializability, and Isolation Anomalies scoped to its stated evidence and boun.
- Make the documented mistake: Listing ANSI anomaly names without drawing the violating schedule. with extra conf
- Treat Listing ANSI anomaly names without drawing the violating schedule as complete proof without the lesson boundary
- Choose the familiar tool before checking whether Listing ANSI anomaly names without drawing the violating schedule ap.

**Answer:** Keep Histories, Serializability, and Isolation Anomalies scoped to its stated evidence and boun.

**Explanation:** The distractors are anchored in the mistake list for L02; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M08-Q016 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M08-Q017

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Choices:**

- Treat Assuming repeatable read or snapshot means serializable in every data as complete proof without the lesson boun.
- Keep Histories, Serializability, and Isolation Anomalies scoped to its stated evidence and boun.
- Choose the familiar tool before checking whether Assuming repeatable read or snapshot means serializable in every dat.
- Make the documented mistake: Assuming repeatable read or snapshot means serializable in every d. with extra con

**Answer:** Keep Histories, Serializability, and Isolation Anomalies scoped to its stated evidence and boun.

**Explanation:** The distractors are anchored in the mistake list for L02; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M08-Q017 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M08-Q018

**Type:** `multiple_choice`  
**Difficulty:** `application`

**Choices:**

- Choose the familiar tool before checking whether Retrying only the failed statement after the transaction snapshot is.
- Make the documented mistake: Retrying only the failed statement after the transaction snapshot. with extra conf
- Keep Histories, Serializability, and Isolation Anomalies scoped to its stated evidence and boun.
- Treat Retrying only the failed statement after the transaction snapshot is as complete proof without the lesson bound.

**Answer:** Keep Histories, Serializability, and Isolation Anomalies scoped to its stated evidence and boun.

**Explanation:** The distractors are anchored in the mistake list for L02; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M08-Q018 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M08-Q019

**Type:** `multiple_choice`  
**Difficulty:** `synthesis`

**Choices:**

- Choose the familiar tool before checking whether Raising isolation globally without measuring abort and latency costs.
- Make the documented mistake: Raising isolation globally without measuring abort and latency cos. with extra con
- Treat Raising isolation globally without measuring abort and latency costs as complete proof without the lesson bound.
- Keep Histories, Serializability, and Isolation Anomalies scoped to its stated evidence and boun.

**Answer:** Keep Histories, Serializability, and Isolation Anomalies scoped to its stated evidence and boun.

**Explanation:** The distractors are anchored in the mistake list for L02; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M08-Q019 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M08-Q020

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Original concurrency = 200 x 0.075 = 15.00 operations. Revised rate = 200 x 1.25 = 250.0/s, so revised concurrency = 250.0 x 0.075 = 18.75 operations.

**Explanation:** This perturbs the numeric practice around Invariants and Transaction Boundaries: keep the same boundary, align milliseconds to seconds, then apply rate times scoped work. This explanation is specific to M08-Q020 and its cited source.

**Grading notes:** Full credit requires both concurrency values, unit conversion from ms to seconds, and a statement that the boundary stayed unchanged.

## M08-Q021

**Type:** `calculation`  
**Difficulty:** `recall`

**Answer:** Original concurrency = 120 x 0.035 = 4.20 operations. Revised rate = 120 x 1.30 = 156.0/s, so revised concurrency = 156.0 x 0.035 = 5.46 operations.

**Explanation:** This perturbs the numeric practice around Histories, Serializability, and Isolation Anomalies: keep the same boundary, align milliseconds to seconds, then apply rate times scoped work. This explanation is specific to M08-Q021 and its cited source.

**Grading notes:** Full credit requires both concurrency values, unit conversion from ms to seconds, and a statement that the boundary stayed unchanged.

## M08-Q022

**Type:** `calculation`  
**Difficulty:** `application`

**Answer:** Original concurrency = 130 x 0.045 = 5.85 operations. Revised rate = 130 x 1.35 = 175.5/s, so revised concurrency = 175.5 x 0.045 = 7.90 operations.

**Explanation:** This perturbs the numeric practice around Locks, Two-Phase Locking, Deadlocks, and Retries: keep the same boundary, align milliseconds to seconds, then apply rate times scoped work. This explanation is specific to M08-Q022 and its cited source.

**Grading notes:** Full credit requires both concurrency values, unit conversion from ms to seconds, and a statement that the boundary stayed unchanged.

## M08-Q023

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Original concurrency = 140 x 0.055 = 7.70 operations. Revised rate = 140 x 1.40 = 196.0/s, so revised concurrency = 196.0 x 0.055 = 10.78 operations.

**Explanation:** This perturbs the numeric practice around Optimistic Control, MVCC, Snapshots, and Write Skew: keep the same boundary, align milliseconds to seconds, then apply rate times scoped work. This explanation is specific to M08-Q023 and its cited source.

**Grading notes:** Full credit requires both concurrency values, unit conversion from ms to seconds, and a statement that the boundary stayed unchanged.

## M08-Q024

**Type:** `calculation`  
**Difficulty:** `recall`

**Answer:** Original concurrency = 150 x 0.065 = 9.75 operations. Revised rate = 150 x 1.45 = 217.5/s, so revised concurrency = 217.5 x 0.065 = 14.14 operations.

**Explanation:** This perturbs the numeric practice around Constraints, Authority, and Atomic Workflows: keep the same boundary, align milliseconds to seconds, then apply rate times scoped work. This explanation is specific to M08-Q024 and its cited source.

**Grading notes:** Full credit requires both concurrency values, unit conversion from ms to seconds, and a statement that the boundary stayed unchanged.

## M08-Q025

**Type:** `calculation`  
**Difficulty:** `application`

**Answer:** Original concurrency = 160 x 0.075 = 12.00 operations. Revised rate = 160 x 1.10 = 176.0/s, so revised concurrency = 176.0 x 0.075 = 13.20 operations.

**Explanation:** This perturbs the numeric practice around WAL, Checkpoints, Redo/Undo, and Group Commit: keep the same boundary, align milliseconds to seconds, then apply rate times scoped work. This explanation is specific to M08-Q025 and its cited source.

**Grading notes:** Full credit requires both concurrency values, unit conversion from ms to seconds, and a statement that the boundary stayed unchanged.

## M08-Q026

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Original concurrency = 170 x 0.035 = 5.95 operations. Revised rate = 170 x 1.15 = 195.5/s, so revised concurrency = 195.5 x 0.035 = 6.84 operations.

**Explanation:** This perturbs the numeric practice around Backups, PITR, Restore Validation, and Objectives: keep the same boundary, align milliseconds to seconds, then apply rate times scoped work. This explanation is specific to M08-Q026 and its cited source.

**Grading notes:** Full credit requires both concurrency values, unit conversion from ms to seconds, and a statement that the boundary stayed unchanged.

## M08-Q027

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** The fixture tests f01-lost-update-broken (broken), with broken as the expected target. The strongest discriminator is the field that changes the mechanism under test, such as scenario_id=f01-lost-update-broken, rather than the general presence of a lab run.

**Explanation:** The cited fixture is machine-readable source material for M08; diagnosis should start from the emitted fields and connect them to Locks, Two-Phase Locking, Deadlocks, and Retries. This explanation is specific to M08-Q027 and its cited source.

**Grading notes:** Full credit requires naming the mechanism or failure mode and citing one concrete field from the fixture. Partial credit is appropriate for a plausible mechanism without a discriminator.

## M08-Q028

**Type:** `scenario_diagnosis`  
**Difficulty:** `synthesis`

**Answer:** The fixture tests f01-lost-update-repaired (repaired), with repaired as the expected target. The strongest discriminator is the field that changes the mechanism under test, such as scenario_id=f01-lost-update-repaired, rather than the general presence of a lab run.

**Explanation:** The cited fixture is machine-readable source material for M08; diagnosis should start from the emitted fields and connect them to Optimistic Control, MVCC, Snapshots, and Write Skew. This explanation is specific to M08-Q028 and its cited source.

**Grading notes:** Full credit requires naming the mechanism or failure mode and citing one concrete field from the fixture. Partial credit is appropriate for a plausible mechanism without a discriminator.

## M08-Q029

**Type:** `scenario_diagnosis`  
**Difficulty:** `recall`

**Answer:** The fixture tests f02-write-skew-broken (broken), with broken as the expected target. The strongest discriminator is the field that changes the mechanism under test, such as scenario_id=f02-write-skew-broken, rather than the general presence of a lab run.

**Explanation:** The cited fixture is machine-readable source material for M08; diagnosis should start from the emitted fields and connect them to Constraints, Authority, and Atomic Workflows. This explanation is specific to M08-Q029 and its cited source.

**Grading notes:** Full credit requires naming the mechanism or failure mode and citing one concrete field from the fixture. Partial credit is appropriate for a plausible mechanism without a discriminator.

## M08-Q030

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** The fixture tests f02-write-skew-repaired (repaired), with repaired as the expected target. The strongest discriminator is the field that changes the mechanism under test, such as scenario_id=f02-write-skew-repaired, rather than the general presence of a lab run.

**Explanation:** The cited fixture is machine-readable source material for M08; diagnosis should start from the emitted fields and connect them to WAL, Checkpoints, Redo/Undo, and Group Commit. This explanation is specific to M08-Q030 and its cited source.

**Grading notes:** Full credit requires naming the mechanism or failure mode and citing one concrete field from the fixture. Partial credit is appropriate for a plausible mechanism without a discriminator.

## M08-Q031

**Type:** `scenario_diagnosis`  
**Difficulty:** `synthesis`

**Answer:** The fixture tests f03-deadlock-broken (broken), with broken as the expected target. The strongest discriminator is the field that changes the mechanism under test, such as scenario_id=f03-deadlock-broken, rather than the general presence of a lab run.

**Explanation:** The cited fixture is machine-readable source material for M08; diagnosis should start from the emitted fields and connect them to Backups, PITR, Restore Validation, and Objectives. This explanation is specific to M08-Q031 and its cited source.

**Grading notes:** Full credit requires naming the mechanism or failure mode and citing one concrete field from the fixture. Partial credit is appropriate for a plausible mechanism without a discriminator.

## M08-Q032

**Type:** `scenario_diagnosis`  
**Difficulty:** `recall`

**Answer:** The fixture tests f03-deadlock-repaired (repaired), with repaired as the expected target. The strongest discriminator is the field that changes the mechanism under test, such as scenario_id=f03-deadlock-repaired, rather than the general presence of a lab run.

**Explanation:** The cited fixture is machine-readable source material for M08; diagnosis should start from the emitted fields and connect them to Transaction and Recovery Decisions. This explanation is specific to M08-Q032 and its cited source.

**Grading notes:** Full credit requires naming the mechanism or failure mode and citing one concrete field from the fixture. Partial credit is appropriate for a plausible mechanism without a discriminator.

## M08-Q033

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Recommend the option that preserves the Optimistic Control, MVCC, Snapshots, and Write Skew mechanism under the exercise constraints: Map N-01–N-06 to authority, writers, boundary, constraint, oracle, and owner. The decision should be reversed if a repeated measurement or review shows the named constraint is false, the safer alternative meets the same outcome at lower operational cost, or the protected invariant is no longer owned by this boundary.

**Explanation:** The exercise asks for a defensible decision, not a preference. The answer must keep evidence and reversal conditions visible so the learner can change course when facts change. This explanation is specific to M08-Q033 and its cited source.

**Grading notes:** Full credit requires a clear recommendation, cited exercise evidence, and a falsifiable reversal condition. Half credit for a reasonable recommendation with no reversal condition.

## M08-Q034

**Type:** `design_judgment`  
**Difficulty:** `recall`

**Answer:** Recommend the option that preserves the Constraints, Authority, and Atomic Workflows mechanism under the exercise constraints: Classify result, audit, summary, notification, and telescope command as authoritative, derived, or external; draw commit and repair boundaries. The decision should be reversed if a repeated measurement or review shows the named constraint is false, the safer alternative meets the same outcome at lower operational cost, or the protected invariant is no longer owned by this boundary.

**Explanation:** The exercise asks for a defensible decision, not a preference. The answer must keep evidence and reversal conditions visible so the learner can change course when facts change. This explanation is specific to M08-Q034 and its cited source.

**Grading notes:** Full credit requires a clear recommendation, cited exercise evidence, and a falsifiable reversal condition. Half credit for a reasonable recommendation with no reversal condition.

## M08-Q035

**Type:** `design_judgment`  
**Difficulty:** `application`

**Answer:** Recommend the option that preserves the WAL, Checkpoints, Redo/Undo, and Group Commit mechanism under the exercise constraints: Write F01 as ordered reads/writes/commits, calculate expected and observed counts, and identify the dependency that makes one update disappear. The decision should be reversed if a repeated measurement or review shows the named constraint is false, the safer alternative meets the same outcome at lower operational cost, or the protected invariant is no longer owned by this boundary.

**Explanation:** The exercise asks for a defensible decision, not a preference. The answer must keep evidence and reversal conditions visible so the learner can change course when facts change. This explanation is specific to M08-Q035 and its cited source.

**Grading notes:** Full credit requires a clear recommendation, cited exercise evidence, and a falsifiable reversal condition. Half credit for a reasonable recommendation with no reversal condition.

## M08-Q036

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Recommend the option that preserves the Backups, PITR, Restore Validation, and Objectives mechanism under the exercise constraints: Draw F02 snapshots and serialization edges. Explain why same-row write-conflict detection is insufficient and compare two repairs. The decision should be reversed if a repeated measurement or review shows the named constraint is false, the safer alternative meets the same outcome at lower operational cost, or the protected invariant is no longer owned by this boundary.

**Explanation:** The exercise asks for a defensible decision, not a preference. The answer must keep evidence and reversal conditions visible so the learner can change course when facts change. This explanation is specific to M08-Q036 and its cited source.

**Grading notes:** Full credit requires a clear recommendation, cited exercise evidence, and a falsifiable reversal condition. Half credit for a reasonable recommendation with no reversal condition.

## M08-Q037

**Type:** `design_judgment`  
**Difficulty:** `recall`

**Answer:** Recommend the option that preserves the Transaction and Recovery Decisions mechanism under the exercise constraints: Create a compatibility table for shared, exclusive, and update-intent locks; apply it to an exclusive telescope window. The decision should be reversed if a repeated measurement or review shows the named constraint is false, the safer alternative meets the same outcome at lower operational cost, or the protected invariant is no longer owned by this boundary.

**Explanation:** The exercise asks for a defensible decision, not a preference. The answer must keep evidence and reversal conditions visible so the learner can change course when facts change. This explanation is specific to M08-Q037 and its cited source.

**Grading notes:** Full credit requires a clear recommendation, cited exercise evidence, and a falsifiable reversal condition. Half credit for a reasonable recommendation with no reversal condition.
