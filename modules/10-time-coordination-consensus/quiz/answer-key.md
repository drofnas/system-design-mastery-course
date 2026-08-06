# M10 Quiz Answer Key

This key covers all 16 questions for **Time, Coordination, and Consensus**. Use it after an attempt, or provide it with the LLM grading prompt for feedback.

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

## M10-Q021

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** Pairwise uncertainty radius is 2 + 2 = 4 ms.

**Explanation:** M10-Q021 uses clock interval from Physical Clocks, Drift, Skew, and Uncertainty and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M10-Q022

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** Drift is 40/1,000,000 x 300 s x 1000 = 12.0 ms.

**Explanation:** M10-Q022 uses clock drift from Logical Clocks, Vector Clocks, and Causal Order and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M10-Q023

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** Skew ratio is 120 / 40 = 3.0x.

**Explanation:** M10-Q023 uses skew ratio from Safety, Liveness, Failure Detectors, and Consensus Boundaries and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M10-Q024

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** No. Terms tie at 4, so index decides; 18 < 20, so the voter should reject the vote.

**Explanation:** M10-Q024 uses Raft vote from Paxos, Raft, and Replicated-State-Machine Foundations and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.
