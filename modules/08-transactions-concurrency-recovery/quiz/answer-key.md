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

- Measure transaction acid data for review case one; limit the change.
- Measure putting network data for review case one; limit the change.
- Measure cache summary data for review case one; limit the change. with margin
- Measure widening every data for review case one; limit the change.

**Answer:** Measure transaction acid data for review case one; limit the change.

**Explanation:** M08-Q014 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects transaction acid as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M08-Q015

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Measure listing ansi data for review case two; limit the change. with margin
- Measure putting network data for review case two; limit the change.
- Measure repeatable read data for review case two; limit the change.
- Measure retrying only data for review case two; limit the change.

**Answer:** Measure putting network data for review case two; limit the change.

**Explanation:** M08-Q015 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects putting network as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M08-Q016

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Measure raising isolation data for review case three; limit the change.
- Measure lock timeout data for review case three; limit the change.
- Measure cache summary data for review case three; limit the change.
- Measure retrying last data for review case three; limit the change.

**Answer:** Measure cache summary data for review case three; limit the change.

**Explanation:** M08-Q016 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects cache summary as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M08-Q017

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Measure row locks data for review case four; limit the change. with margin
- Measure holding locks data for review case four; limit the change.
- Measure mvcc means data for review case four; limit the change.
- Measure widening every data for review case four; limit the change.

**Answer:** Measure widening every data for review case four; limit the change.

**Explanation:** M08-Q017 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects widening every as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M08-Q018

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Measure listing ansi data for review case five; limit the change.
- Measure validating only data for review case five; limit the change.
- Measure retrying high data for review case five; limit the change.
- Measure timestamps imply data for review case five; limit the change.

**Answer:** Measure listing ansi data for review case five; limit the change.

**Explanation:** M08-Q018 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects listing ansi as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M08-Q019

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Measure relying pre data for review case six; limit the change.
- Measure repeatable read data for review case six; limit the change.
- Measure audit log data for review case six; limit the change. with margin
- Measure dual writing data for review case six; limit the change.

**Answer:** Measure repeatable read data for review case six; limit the change.

**Explanation:** M08-Q019 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects repeatable read as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M08-Q020

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Measure keeping transaction data for review case seven; limit the change.
- Measure buffered write data for review case seven; limit the change.
- Measure retrying only data for review case seven; limit the change.
- Measure flushing data data for review case seven; limit the change.

**Answer:** Measure retrying only data for review case seven; limit the change.

**Explanation:** M08-Q020 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects retrying only as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M08-Q021

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Measure clean process data for review case eight; limit the change.
- Measure checkpoint completion data for review case eight; limit the change.
- Measure equating green data for review case eight; limit the change.
- Measure raising isolation data for review case eight; limit the change.

**Answer:** Measure raising isolation data for review case eight; limit the change.

**Explanation:** M08-Q021 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects raising isolation as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M08-Q022

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** Calculation for invariants and transaction boundaries, observable RPO is 20 - 7 = 13 minutes if the missing middle cannot be replayed.

**Explanation:** M08-Q022 uses RPO from Invariants and Transaction Boundaries and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M08-Q023

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** Calculation for histories, serializability, and isolation anomalies, observable RPO is 20 - 7 = 13 minutes if the missing middle cannot be replayed.

**Explanation:** M08-Q023 uses RPO from Histories, Serializability, and Isolation Anomalies and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M08-Q024

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** Calculation for locks, two-phase locking, deadlocks, and retries, the enumeration has 4 x 3 = 12 state cases.

**Explanation:** M08-Q024 uses recovery state enumeration from Locks, Two-Phase Locking, Deadlocks, and Retries and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M08-Q025

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** Diagnosis for invariants and transaction boundaries, initial_state.completed_exposures and control.atomic_workflow separate the mechanism. initial_state.completed_exposures = 0 while control.atomic_workflow = 1, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare initial_state.completed_exposures with control.atomic_workflow and connect that contrast to invariants and transaction boundaries.

**Grading notes:** Full credit names Invariants and Transaction Boundaries, cites initial_state.completed_exposures and control.atomic_workflow, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M08-Q026

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** Diagnosis for histories, serializability, and isolation anomalies, initial_state.completed_exposures and control.flush_before_ack separate the mechanism. initial_state.completed_exposures = 0 while control.flush_before_ack = 1, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare initial_state.completed_exposures with control.flush_before_ack and connect that contrast to histories, serializability, and isolation anomalies.

**Grading notes:** Full credit names Histories, Serializability, and Isolation Anomalies, cites initial_state.completed_exposures and control.flush_before_ack, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M08-Q027

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** Diagnosis for locks, two-phase locking, deadlocks, and retries, initial_state.certified_controllers and control.validate_restore separate the mechanism. initial_state.certified_controllers = 2 while control.validate_restore = 1, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare initial_state.certified_controllers with control.validate_restore and connect that contrast to locks, two-phase locking, deadlocks, and retries.

**Grading notes:** Full credit names Locks, Two-Phase Locking, Deadlocks, and Retries, cites initial_state.certified_controllers and control.validate_restore, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M08-Q028

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** Diagnosis for optimistic control, mvcc, snapshots, and write skew, initial_state.certified_controllers and control.rebuild_derived separate the mechanism. initial_state.certified_controllers = 2 while control.rebuild_derived = 1, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare initial_state.certified_controllers with control.rebuild_derived and connect that contrast to optimistic control, mvcc, snapshots, and write skew.

**Grading notes:** Full credit names Optimistic Control, MVCC, Snapshots, and Write Skew, cites initial_state.certified_controllers and control.rebuild_derived, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M08-Q029

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** Diagnosis for constraints, authority, and atomic workflows, invariants.0.value and control.atomic_workflow separate the mechanism. invariants.0.value = 2 while control.atomic_workflow = 1, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare invariants.0.value with control.atomic_workflow and connect that contrast to constraints, authority, and atomic workflows.

**Grading notes:** Full credit names Constraints, Authority, and Atomic Workflows, cites invariants.0.value and control.atomic_workflow, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M08-Q030

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** Diagnosis for wal, checkpoints, redo/undo, and group commit, invariants.0.value and control.flush_before_ack separate the mechanism. invariants.0.value = 2 while control.flush_before_ack = 1, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare invariants.0.value with control.flush_before_ack and connect that contrast to wal, checkpoints, redo/undo, and group commit.

**Grading notes:** Full credit names WAL, Checkpoints, Redo/Undo, and Group Commit, cites invariants.0.value and control.flush_before_ack, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M08-Q031

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** Diagnosis for backups, pitr, restore validation, and objectives, control.flush_before_ack and control.validate_restore separate the mechanism. control.flush_before_ack = 0 while control.validate_restore = 1, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare control.flush_before_ack with control.validate_restore and connect that contrast to backups, pitr, restore validation, and objectives.

**Grading notes:** Full credit names Backups, PITR, Restore Validation, and Objectives, cites control.flush_before_ack and control.validate_restore, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M08-Q032

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** Diagnosis for transaction and recovery decisions, initial_state.durable_exposure and control.validate_restore separate the mechanism. initial_state.durable_exposure = 0 while control.validate_restore = 1, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare initial_state.durable_exposure with control.validate_restore and connect that contrast to transaction and recovery decisions.

**Grading notes:** Full credit names Transaction and Recovery Decisions, cites initial_state.durable_exposure and control.validate_restore, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M08-Q033

**Type:** `design_judgment`
**Difficulty:** `recall`

**Answer:** Approve Invariant enforcement map at 134.9/s. The deciding number is 204 x 0.72 = 146.9/s, leaving 12/s before the reserve is consumed. Withdraw approval if a drill, trace, or workload sample shows invariant enforcement map demand above 146.9/s or proves the shed point cannot protect lower-priority work.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to invariant enforcement map demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 146.9/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M08-Q034

**Type:** `design_judgment`
**Difficulty:** `application`

**Answer:** Decline Minimal transaction boundary at 170.5/s. The deciding number is 221 x 0.72 = 159.1/s, so planned demand exceeds the usable region by 11.4/s. Approve later if repeated measurements lift usable capacity above 170.5/s or a named policy removes at least 11.4/s of deferrable work before saturation.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to minimal transaction boundary demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 159.1/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M08-Q035

**Type:** `design_judgment`
**Difficulty:** `synthesis`

**Answer:** Approve conditionally for Lost-update history. The deciding number is 238 x 0.72 = 171.4/s, and 166.4/s fits only while the fallback remains enforceable. Keep the condition until recovery traffic, priority demand, or fallback tests show less than 5/s of usable margin.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to lost-update history demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 171.4/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M08-Q036

**Type:** `design_judgment`
**Difficulty:** `recall`

**Answer:** Approve Write-skew graph at 166.5/s. The deciding number is 255 x 0.72 = 183.6/s, leaving 17.1/s before the reserve is consumed. Require redesign if a drill, trace, or workload sample shows write-skew graph demand above 183.6/s or proves the shed point cannot protect lower-priority work.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to write-skew graph demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 183.6/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M08-Q037

**Type:** `design_judgment`
**Difficulty:** `application`

**Answer:** Decline Lock compatibility at 211.4/s. The deciding number is 272 x 0.72 = 195.8/s, so planned demand exceeds the usable region by 15.6/s. Lift the decline if repeated measurements lift usable capacity above 211.4/s or a named policy removes at least 15.6/s of deferrable work before saturation.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to lock compatibility demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 195.8/s, compares it with planned demand, and names a scenario-specific reversal condition.
