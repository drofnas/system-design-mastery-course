# M08 Quiz Answer Key

This key covers all 100 questions for **Transactions, Concurrency, and Recovery**. Use it after an attempt, or provide it with the LLM grading prompt for feedback.

## M08-Q001

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to map business invariants to transaction boundaries, authoritative state, and enforceable constraints.

**Explanation:** Use Invariants and Transaction Boundaries to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M08-Q002

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Histories, Serializability, and Isolation Anomalies', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Histories, Serializability, and Isolation Anomalies to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M08-Q003

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. Derive lock compatibility and wait-for graphs, explain strict 2PL, recover from deadlock, and implement bounded whole-transaction retry.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M08-Q004

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: Saying MVCC means “readers never block” without vacuum/version limits.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M08-Q005

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for explain and test wal ordering, checkpoints, redo/undo, group commit, and durable acknowledgement..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - PostgreSQL, DDL Constraintshttps://www.postgresql.org/docs/current/ddl-constraints.html.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M08-Q006

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to automate and validate backup, point-in-time recovery, integrity checks, and measured rto/rpo while distinguishing replicas from backups.

**Explanation:** Use WAL, Checkpoints, Redo/Undo, and Group Commit to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M08-Q007

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Backups, PITR, Restore Validation, and Objectives', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Backups, PITR, Restore Validation, and Objectives to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M08-Q008

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. Defend per-invariant isolation, constraint, retry, acknowledgement, backup, and tested recovery choices with ownership, cost, security, migration, and reversal evidence.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M08-Q009

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: Calling a transaction “ACID” without naming the admitted histories.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M08-Q010

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for derive isolation anomalies from histories, visibility rules, and serialization dependencies..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - PostgreSQL, Transaction Isolationhttps://www.postgresql.org/docs/current/transaction-iso.html.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M08-Q011

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to implement and compare locking, optimistic validation, mvcc, deadlock handling, and bounded transaction retries.

**Explanation:** Use Locks, Two-Phase Locking, Deadlocks, and Retries to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M08-Q012

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Optimistic Control, MVCC, Snapshots, and Write Skew', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Optimistic Control, MVCC, Snapshots, and Write Skew to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M08-Q013

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. Choose enforceable constraints, keep required authoritative writes atomic, and separate reconstructable state and external effects from the transaction.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M08-Q014

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: Calling a buffered write durable because the language write call returned.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M08-Q015

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for diagnose seven concurrency and recovery failures from immutable same-input evidence..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - PostgreSQL, Continuous Archiving and PITRhttps://www.postgresql.org/docs/current/continuous-archiving.html.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M08-Q016

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to defend a transaction and recovery strategy covering security, cost, operations, ownership, migration, rollback, and reversal evidence.

**Explanation:** Use Transaction and Recovery Decisions to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M08-Q017

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Invariants and Transaction Boundaries', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Invariants and Transaction Boundaries to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M08-Q018

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. Read a history, construct dependencies, identify lost update and write skew, and select an isolation claim per operation rather than per product.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M08-Q019

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: Treating a lock timeout as a deadlock detector.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M08-Q020

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for enforce atomic authoritative workflows with schema constraints and rebuildable derived state..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - CMU 15-445, MVCC lectures and noteshttps://15445.courses.cs.cmu.edu/spring2026/schedule.html.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M08-Q021

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to explain and test wal ordering, checkpoints, redo/undo, group commit, and durable acknowledgement.

**Explanation:** Use Constraints, Authority, and Atomic Workflows to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M08-Q022

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'WAL, Checkpoints, Redo/Undo, and Group Commit', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use WAL, Checkpoints, Redo/Undo, and Group Commit to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M08-Q023

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. Build a recoverable base-plus-log set, distinguish replicas from backups, measure RTO/RPO, and gate traffic on restore integrity and application probes.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M08-Q024

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: Choosing one isolation level for the whole architecture.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M08-Q025

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for map business invariants to transaction boundaries, authoritative state, and enforceable constraints..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - PostgreSQL, Constraintshttps://www.postgresql.org/docs/current/ddl-constraints.html.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M08-Q026

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to derive isolation anomalies from histories, visibility rules, and serialization dependencies.

**Explanation:** Use Histories, Serializability, and Isolation Anomalies to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M08-Q027

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Locks, Two-Phase Locking, Deadlocks, and Retries', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Locks, Two-Phase Locking, Deadlocks, and Retries to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M08-Q028

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. Explain version visibility, implement optimistic validation, diagnose snapshot write skew, and bound conflict/garbage-collection costs.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M08-Q029

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: Relying on a pre-insert existence check instead of uniqueness.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M08-Q030

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for automate and validate backup, point-in-time recovery, integrity checks, and measured rto/rpo while distinguishing replicas from backups..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - PostgreSQL, Write-Ahead Logginghttps://www.postgresql.org/docs/current/wal-intro.html.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M08-Q031

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to diagnose seven concurrency and recovery failures from immutable same-input evidence.

**Explanation:** Use Backups, PITR, Restore Validation, and Objectives to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M08-Q032

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Transaction and Recovery Decisions', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Transaction and Recovery Decisions to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M08-Q033

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. Map an invariant to authority, writers, a minimal atomic boundary, an enforcement point, and a falsifiable proof.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M08-Q034

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: Listing ANSI anomaly names without drawing the violating schedule.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M08-Q035

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for implement and compare locking, optimistic validation, mvcc, deadlock handling, and bounded transaction retries..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - PostgreSQL, Explicit Lockinghttps://www.postgresql.org/docs/current/explicit-locking.html.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M08-Q036

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to enforce atomic authoritative workflows with schema constraints and rebuildable derived state.

**Explanation:** Use Optimistic Control, MVCC, Snapshots, and Write Skew to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M08-Q037

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Constraints, Authority, and Atomic Workflows', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Constraints, Authority, and Atomic Workflows to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M08-Q038

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. Order WAL, data, flush, commit, and acknowledgement events; recover committed and loser transactions; explain checkpoints and group commit; bound durability claims.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M08-Q039

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: Equating green backup jobs with recoverability.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M08-Q040

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for defend a transaction and recovery strategy covering security, cost, operations, ownership, migration, rollback, and reversal evidence..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - GitHub, October 21 post-incident analysishttps://github.blog/news-insights/company-news/oct21-post-incident-analysis/.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M08-Q041

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to map business invariants to transaction boundaries, authoritative state, and enforceable constraints.

**Explanation:** Use Invariants and Transaction Boundaries to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M08-Q042

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Histories, Serializability, and Isolation Anomalies', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Histories, Serializability, and Isolation Anomalies to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M08-Q043

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. Derive lock compatibility and wait-for graphs, explain strict 2PL, recover from deadlock, and implement bounded whole-transaction retry.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M08-Q044

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: Saying MVCC means “readers never block” without vacuum/version limits.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M08-Q045

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for explain and test wal ordering, checkpoints, redo/undo, group commit, and durable acknowledgement..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - PostgreSQL, DDL Constraintshttps://www.postgresql.org/docs/current/ddl-constraints.html.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M08-Q046

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to automate and validate backup, point-in-time recovery, integrity checks, and measured rto/rpo while distinguishing replicas from backups.

**Explanation:** Use WAL, Checkpoints, Redo/Undo, and Group Commit to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M08-Q047

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Backups, PITR, Restore Validation, and Objectives', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Backups, PITR, Restore Validation, and Objectives to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M08-Q048

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. Defend per-invariant isolation, constraint, retry, acknowledgement, backup, and tested recovery choices with ownership, cost, security, migration, and reversal evidence.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M08-Q049

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: Calling a transaction “ACID” without naming the admitted histories.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M08-Q050

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for derive isolation anomalies from histories, visibility rules, and serialization dependencies..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - PostgreSQL, Transaction Isolationhttps://www.postgresql.org/docs/current/transaction-iso.html.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M08-Q051

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to implement and compare locking, optimistic validation, mvcc, deadlock handling, and bounded transaction retries.

**Explanation:** Use Locks, Two-Phase Locking, Deadlocks, and Retries to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M08-Q052

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Optimistic Control, MVCC, Snapshots, and Write Skew', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Optimistic Control, MVCC, Snapshots, and Write Skew to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M08-Q053

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. Choose enforceable constraints, keep required authoritative writes atomic, and separate reconstructable state and external effects from the transaction.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M08-Q054

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: Calling a buffered write durable because the language write call returned.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M08-Q055

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for diagnose seven concurrency and recovery failures from immutable same-input evidence..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - PostgreSQL, Continuous Archiving and PITRhttps://www.postgresql.org/docs/current/continuous-archiving.html.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M08-Q056

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to defend a transaction and recovery strategy covering security, cost, operations, ownership, migration, rollback, and reversal evidence.

**Explanation:** Use Transaction and Recovery Decisions to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M08-Q057

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Invariants and Transaction Boundaries', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Invariants and Transaction Boundaries to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M08-Q058

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. Read a history, construct dependencies, identify lost update and write skew, and select an isolation claim per operation rather than per product.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M08-Q059

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: Treating a lock timeout as a deadlock detector.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M08-Q060

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for enforce atomic authoritative workflows with schema constraints and rebuildable derived state..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - CMU 15-445, MVCC lectures and noteshttps://15445.courses.cs.cmu.edu/spring2026/schedule.html.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M08-Q061

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to explain and test wal ordering, checkpoints, redo/undo, group commit, and durable acknowledgement.

**Explanation:** Use Constraints, Authority, and Atomic Workflows to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M08-Q062

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'WAL, Checkpoints, Redo/Undo, and Group Commit', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use WAL, Checkpoints, Redo/Undo, and Group Commit to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M08-Q063

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. Build a recoverable base-plus-log set, distinguish replicas from backups, measure RTO/RPO, and gate traffic on restore integrity and application probes.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M08-Q064

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: Choosing one isolation level for the whole architecture.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M08-Q065

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for map business invariants to transaction boundaries, authoritative state, and enforceable constraints..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - PostgreSQL, Constraintshttps://www.postgresql.org/docs/current/ddl-constraints.html.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M08-Q066

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to derive isolation anomalies from histories, visibility rules, and serialization dependencies.

**Explanation:** Use Histories, Serializability, and Isolation Anomalies to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M08-Q067

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Locks, Two-Phase Locking, Deadlocks, and Retries', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Locks, Two-Phase Locking, Deadlocks, and Retries to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M08-Q068

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. Explain version visibility, implement optimistic validation, diagnose snapshot write skew, and bound conflict/garbage-collection costs.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M08-Q069

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: Relying on a pre-insert existence check instead of uniqueness.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M08-Q070

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for automate and validate backup, point-in-time recovery, integrity checks, and measured rto/rpo while distinguishing replicas from backups..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - PostgreSQL, Write-Ahead Logginghttps://www.postgresql.org/docs/current/wal-intro.html.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M08-Q071

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to diagnose seven concurrency and recovery failures from immutable same-input evidence.

**Explanation:** Use Backups, PITR, Restore Validation, and Objectives to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M08-Q072

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Transaction and Recovery Decisions', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Transaction and Recovery Decisions to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M08-Q073

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. Map an invariant to authority, writers, a minimal atomic boundary, an enforcement point, and a falsifiable proof.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M08-Q074

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: Listing ANSI anomaly names without drawing the violating schedule.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M08-Q075

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for implement and compare locking, optimistic validation, mvcc, deadlock handling, and bounded transaction retries..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - PostgreSQL, Explicit Lockinghttps://www.postgresql.org/docs/current/explicit-locking.html.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M08-Q076

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to enforce atomic authoritative workflows with schema constraints and rebuildable derived state.

**Explanation:** Use Optimistic Control, MVCC, Snapshots, and Write Skew to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M08-Q077

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Constraints, Authority, and Atomic Workflows', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Constraints, Authority, and Atomic Workflows to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M08-Q078

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. Order WAL, data, flush, commit, and acknowledgement events; recover committed and loser transactions; explain checkpoints and group commit; bound durability claims.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M08-Q079

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: Equating green backup jobs with recoverability.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M08-Q080

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for defend a transaction and recovery strategy covering security, cost, operations, ownership, migration, rollback, and reversal evidence..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - GitHub, October 21 post-incident analysishttps://github.blog/news-insights/company-news/oct21-post-incident-analysis/.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M08-Q081

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to map business invariants to transaction boundaries, authoritative state, and enforceable constraints.

**Explanation:** Use Invariants and Transaction Boundaries to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M08-Q082

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Histories, Serializability, and Isolation Anomalies', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Histories, Serializability, and Isolation Anomalies to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M08-Q083

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. Derive lock compatibility and wait-for graphs, explain strict 2PL, recover from deadlock, and implement bounded whole-transaction retry.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M08-Q084

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: Saying MVCC means “readers never block” without vacuum/version limits.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M08-Q085

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for explain and test wal ordering, checkpoints, redo/undo, group commit, and durable acknowledgement..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - PostgreSQL, DDL Constraintshttps://www.postgresql.org/docs/current/ddl-constraints.html.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M08-Q086

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to automate and validate backup, point-in-time recovery, integrity checks, and measured rto/rpo while distinguishing replicas from backups.

**Explanation:** Use WAL, Checkpoints, Redo/Undo, and Group Commit to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M08-Q087

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Backups, PITR, Restore Validation, and Objectives', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Backups, PITR, Restore Validation, and Objectives to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M08-Q088

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. Defend per-invariant isolation, constraint, retry, acknowledgement, backup, and tested recovery choices with ownership, cost, security, migration, and reversal evidence.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M08-Q089

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: Calling a transaction “ACID” without naming the admitted histories.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M08-Q090

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for derive isolation anomalies from histories, visibility rules, and serialization dependencies..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - PostgreSQL, Transaction Isolationhttps://www.postgresql.org/docs/current/transaction-iso.html.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M08-Q091

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to implement and compare locking, optimistic validation, mvcc, deadlock handling, and bounded transaction retries.

**Explanation:** Use Locks, Two-Phase Locking, Deadlocks, and Retries to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M08-Q092

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Optimistic Control, MVCC, Snapshots, and Write Skew', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Optimistic Control, MVCC, Snapshots, and Write Skew to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M08-Q093

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. Choose enforceable constraints, keep required authoritative writes atomic, and separate reconstructable state and external effects from the transaction.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M08-Q094

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: Calling a buffered write durable because the language write call returned.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M08-Q095

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for diagnose seven concurrency and recovery failures from immutable same-input evidence..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - PostgreSQL, Continuous Archiving and PITRhttps://www.postgresql.org/docs/current/continuous-archiving.html.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M08-Q096

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to defend a transaction and recovery strategy covering security, cost, operations, ownership, migration, rollback, and reversal evidence.

**Explanation:** Use Transaction and Recovery Decisions to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M08-Q097

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Invariants and Transaction Boundaries', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Invariants and Transaction Boundaries to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M08-Q098

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. Read a history, construct dependencies, identify lost update and write skew, and select an isolation claim per operation rather than per product.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M08-Q099

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: Treating a lock timeout as a deadlock detector.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M08-Q100

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for enforce atomic authoritative workflows with schema constraints and rebuildable derived state..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - CMU 15-445, MVCC lectures and noteshttps://15445.courses.cs.cmu.edu/spring2026/schedule.html.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.
