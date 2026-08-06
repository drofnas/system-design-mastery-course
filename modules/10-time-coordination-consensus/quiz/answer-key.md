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

- Measure ntp success data for review case one; limit the change.
- Measure monotonic duration data for review case one; limit the change.
- Measure lease process data for review case one; limit the change.
- Measure timestamps fencing data for review case one; limit the change.

**Answer:** Measure ntp success data for review case one; limit the change.

**Explanation:** M10-Q013 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects ntp success as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M10-Q014

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Measure reading causality data for review case two; limit the change.
- Measure monotonic duration data for review case two; limit the change.
- Measure concurrency simultaneous data for review case two; limit the change.
- Measure identity lifecycle data for review case two; limit the change.

**Answer:** Measure monotonic duration data for review case two; limit the change.

**Explanation:** M10-Q014 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects monotonic duration as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M10-Q015

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Measure total tie data for review case three; limit the change.
- Measure writing system data for review case three; limit the change.
- Measure lease process data for review case three; limit the change.
- Measure timeout crash data for review case three; limit the change.

**Answer:** Measure lease process data for review case three; limit the change.

**Explanation:** M10-Q015 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects lease process as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M10-Q016

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Measure mixing safety data for review case four; limit the change.
- Measure putting all data for review case four; limit the change.
- Measure majorities overlap data for review case four; limit the change.
- Measure timestamps fencing data for review case four; limit the change.

**Answer:** Measure timestamps fencing data for review case four; limit the change.

**Explanation:** M10-Q016 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects timestamps fencing as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M10-Q017

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Measure reading causality data for review case five; limit the change.
- Measure equating replication data for review case five; limit the change.
- Measure deterministic application data for review case five; limit the change.
- Measure algorithm slogans data for review case five; limit the change.

**Answer:** Measure reading causality data for review case five; limit the change.

**Explanation:** M10-Q017 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects reading causality as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M10-Q018

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Measure randomized timeout data for review case six; limit the change.
- Measure concurrency simultaneous data for review case six; limit the change.
- Measure persisting eventually data for review case six; limit the change.
- Measure electing highest data for review case six; limit the change. with margin

**Answer:** Measure concurrency simultaneous data for review case six; limit the change.

**Explanation:** M10-Q018 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects concurrency simultaneous as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M10-Q019

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Measure resetting term data for review case seven; limit the change.
- Measure equating majority data for review case seven; limit the change.
- Measure identity lifecycle data for review case seven; limit the change.
- Measure applying commitment data for review case seven; limit the change.

**Answer:** Measure identity lifecycle data for review case seven; limit the change.

**Explanation:** M10-Q019 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects identity lifecycle as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M10-Q020

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Measure deleting entire data for review case eight; limit the change.
- Measure test coverage data for review case eight; limit the change.
- Measure exactly once data for review case eight; limit the change.
- Measure total tie data for review case eight; limit the change.

**Answer:** Measure total tie data for review case eight; limit the change.

**Explanation:** M10-Q020 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects total tie as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M10-Q021

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** Calculation for physical clocks, drift, skew, and uncertainty, pairwise uncertainty radius is 2 + 2 = 4 ms.

**Explanation:** M10-Q021 uses clock interval from Physical Clocks, Drift, Skew, and Uncertainty and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M10-Q022

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** Calculation for logical clocks, vector clocks, and causal order, drift is 40/1,000,000 x 300 s x 1000 = 12.0 ms.

**Explanation:** M10-Q022 uses clock drift from Logical Clocks, Vector Clocks, and Causal Order and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M10-Q023

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** Calculation for safety, liveness, failure detectors, and consensus boundaries, skew ratio is 120 / 40 = 3.0x.

**Explanation:** M10-Q023 uses skew ratio from Safety, Liveness, Failure Detectors, and Consensus Boundaries and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M10-Q024

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** Calculation for paxos, raft, and replicated-state-machine foundations, no. Terms tie at 4, so index decides; 18 < 20, so the voter should reject the vote.

**Explanation:** M10-Q024 uses Raft vote from Paxos, Raft, and Replicated-State-Machine Foundations and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M10-Q025

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** Diagnosis for physical clocks, drift, skew, and uncertainty, events.0.tick and events.2.tick separate the mechanism. events.0.tick = 1 while events.2.tick = 2, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare events.0.tick with events.2.tick and connect that contrast to physical clocks, drift, skew, and uncertainty.

**Grading notes:** Full credit names Physical Clocks, Drift, Skew, and Uncertainty, cites events.0.tick and events.2.tick, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M10-Q026

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** Diagnosis for logical clocks, vector clocks, and causal order, events.0.tick and generated_schedule_count separate the mechanism. events.0.tick = 1 while generated_schedule_count = 8, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare events.0.tick with generated_schedule_count and connect that contrast to logical clocks, vector clocks, and causal order.

**Grading notes:** Full credit names Logical Clocks, Vector Clocks, and Causal Order, cites events.0.tick and generated_schedule_count, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M10-Q027

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** Diagnosis for safety, liveness, failure detectors, and consensus boundaries, events.1.tick and events.2.tick separate the mechanism. events.1.tick = 1 while events.2.tick = 2, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare events.1.tick with events.2.tick and connect that contrast to safety, liveness, failure detectors, and consensus boundaries.

**Grading notes:** Full credit names Safety, Liveness, Failure Detectors, and Consensus Boundaries, cites events.1.tick and events.2.tick, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M10-Q028

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** Diagnosis for paxos, raft, and replicated-state-machine foundations, events.1.tick and generated_schedule_count separate the mechanism. events.1.tick = 1 while generated_schedule_count = 8, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare events.1.tick with generated_schedule_count and connect that contrast to paxos, raft, and replicated-state-machine foundations.

**Grading notes:** Full credit names Paxos, Raft, and Replicated-State-Machine Foundations, cites events.1.tick and generated_schedule_count, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M10-Q029

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** Diagnosis for raft leader election and persistent hard state, events.1.tick and events.2.persisted separate the mechanism. events.1.tick = 1 while events.2.persisted = 0, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare events.1.tick with events.2.persisted and connect that contrast to raft leader election and persistent hard state.

**Grading notes:** Full credit names Raft Leader Election and Persistent Hard State, cites events.1.tick and events.2.persisted, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M10-Q030

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** Diagnosis for raft log replication, commitment, and application, events.2.persisted and generated_schedule_count separate the mechanism. events.2.persisted = 1 while generated_schedule_count = 8, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare events.2.persisted with generated_schedule_count and connect that contrast to raft log replication, commitment, and application.

**Grading notes:** Full credit names Raft Log Replication, Commitment, and Application, cites events.2.persisted and generated_schedule_count, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M10-Q031

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** Diagnosis for clients, linearizable reads, snapshots, and compaction, client_results.0.sequence and client_results.1.logical_effects separate the mechanism. client_results.0.sequence = 12 while client_results.1.logical_effects = 1, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare client_results.0.sequence with client_results.1.logical_effects and connect that contrast to clients, linearizable reads, snapshots, and compaction.

**Grading notes:** Full credit names Clients, Linearizable Reads, Snapshots, and Compaction, cites client_results.0.sequence and client_results.1.logical_effects, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M10-Q032

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** Diagnosis for membership, leases, fencing, and coordination decisions, client_results.0.sequence and client_results.1.result separate the mechanism. client_results.0.sequence = 12 while client_results.1.result = 1, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare client_results.0.sequence with client_results.1.result and connect that contrast to membership, leases, fencing, and coordination decisions.

**Grading notes:** Full credit names Membership, Leases, Fencing, and Coordination Decisions, cites client_results.0.sequence and client_results.1.result, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M10-Q033

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** Diagnosis for physical clocks, drift, skew, and uncertainty, events.2.tick and generated_schedule_count separate the mechanism. events.2.tick = 6 while generated_schedule_count = 8, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare events.2.tick with generated_schedule_count and connect that contrast to physical clocks, drift, skew, and uncertainty.

**Grading notes:** Full credit names Physical Clocks, Drift, Skew, and Uncertainty, cites events.2.tick and generated_schedule_count, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M10-Q034

**Type:** `design_judgment`
**Difficulty:** `application`

**Answer:** Approve Clock-bound calculation at 139.2/s. The deciding number is 210 x 0.72 = 151.2/s, leaving 12/s before the reserve is consumed. Withdraw approval if a drill, trace, or workload sample shows clock-bound calculation demand above 151.2/s or proves the shed point cannot protect lower-priority work.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to clock-bound calculation demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 151.2/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M10-Q035

**Type:** `design_judgment`
**Difficulty:** `synthesis`

**Answer:** Decline Lease assumption audit at 174.8/s. The deciding number is 227 x 0.72 = 163.4/s, so planned demand exceeds the usable region by 11.4/s. Approve later if repeated measurements lift usable capacity above 174.8/s or a named policy removes at least 11.4/s of deferrable work before saturation.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to lease assumption audit demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 163.4/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M10-Q036

**Type:** `design_judgment`
**Difficulty:** `recall`

**Answer:** Approve conditionally for Happened-before trace. The deciding number is 244 x 0.72 = 175.7/s, and 170.7/s fits only while the fallback remains enforceable. Keep the condition until recovery traffic, priority demand, or fallback tests show less than 5/s of usable margin.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to happened-before trace demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 175.7/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M10-Q037

**Type:** `design_judgment`
**Difficulty:** `application`

**Answer:** Approve Lamport and vector clocks at 170.8/s. The deciding number is 261 x 0.72 = 187.9/s, leaving 17.1/s before the reserve is consumed. Require redesign if a drill, trace, or workload sample shows lamport and vector clocks demand above 187.9/s or proves the shed point cannot protect lower-priority work.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to lamport and vector clocks demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 187.9/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M10-Q038

**Type:** `design_judgment`
**Difficulty:** `synthesis`

**Answer:** Decline Safety and liveness specification at 215.8/s. The deciding number is 278 x 0.72 = 200.2/s, so planned demand exceeds the usable region by 15.6/s. Lift the decline if repeated measurements lift usable capacity above 215.8/s or a named policy removes at least 15.6/s of deferrable work before saturation.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to safety and liveness specification demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 200.2/s, compares it with planned demand, and names a scenario-specific reversal condition.
