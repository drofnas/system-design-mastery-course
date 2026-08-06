# M08 Quiz Answer Key

This key covers all 16 questions for **Transactions, Concurrency, and Recovery**. Use it after an attempt, or provide it with the LLM grading prompt for feedback.

## M08-Q001

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** It has no falsifiable condition or named authority. 2. The constraint is evaluated at the commit/write boundary against concurrent database state; pre-checks can become stale. 3. Coupling it enlarges contention and recovery scope while adding no authoritative correctness if it can be reconstructed.

**Explanation:** M08-Q001 uses self-check 1 from Invariants and Transaction Boundaries; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M08-Q002

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** A schema constraint is stronger when it is evaluated at the commit or write boundary against concurrent database state; an application pre-check can become stale.

**Explanation:** M08-Q002 uses self-check 2 from Invariants and Transaction Boundaries; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M08-Q003

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** Keep rebuildable summaries outside the authoritative transaction because coupling them enlarges contention and recovery scope without adding authoritative correctness.

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

**Answer:** Lost update overwrites the same logical value; write skew uses disjoint writes whose combined effect violates a predicate.

**Explanation:** M08-Q005 uses self-check 2 from Histories, Serializability, and Isolation Anomalies; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M08-Q006

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** Roll back and retry the entire transaction from fresh state, subject to bounded eligibility and deadline rules.

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

**Answer:** Reset the whole transaction, snapshot, locks, authorization decision, and deadline-derived work before retry.

**Explanation:** M08-Q008 uses self-check 2 from Locks, Two-Phase Locking, Deadlocks, and Retries; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M08-Q009

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** A concurrent row may appear after the check; a constraint or protected predicate decides against commit-time state.

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

## M08-Q022

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** Observable RPO is 20 - 7 = 13 minutes if the missing middle cannot be replayed.

**Explanation:** M08-Q022 uses RPO from Invariants and Transaction Boundaries and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M08-Q023

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** PITR-visible RPO is 20 - 7 = 13 minutes if the missing middle cannot be replayed.

**Explanation:** M08-Q023 uses RPO from Histories, Serializability, and Isolation Anomalies and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M08-Q024

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** The enumeration has 4 x 3 = 12 state cases.

**Explanation:** M08-Q024 uses recovery state enumeration from Locks, Two-Phase Locking, Deadlocks, and Retries and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.
