# M10 Quiz Answer Key

This key covers all 37 questions for **Time, Coordination, and Consensus**. Use it after an attempt, or provide it with the LLM grading prompt for feedback.

## M10-Q001

**Type:** `short_answer`  
**Difficulty:** `recall`

**Answer:** It has no shared origin or bounded relationship with another host's clock

**Explanation:** The cited self-check in L01 tests whether the learner can connect Physical Clocks, Drift, Skew, and Uncertainty to the module mechanism without replacing evidence with labels. This explanation is specific to M10-Q001 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M10-Q002

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** Correctness-critical authority must fail closed or use a non-time proof; silently extending the bound changes the failure model

**Explanation:** The cited self-check in L01 tests whether the learner can connect Physical Clocks, Drift, Skew, and Uncertainty to the module mechanism without replacing evidence with labels. This explanation is specific to M10-Q002 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M10-Q003

**Type:** `short_answer`  
**Difficulty:** `synthesis`

**Answer:** No. Overlap means the clock evidence is insufficient to order them; a causal message path could still order the events. The practice radius is 2 ms + 40×300/1,000,000 = 14 ms; pairwise skew is 28 ms. An 18 ms difference is insufficient

**Explanation:** The cited self-check in L01 tests whether the learner can connect Physical Clocks, Drift, Skew, and Uncertainty to the module mechanism without replacing evidence with labels. This explanation is specific to M10-Q003 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M10-Q004

**Type:** `short_answer`  
**Difficulty:** `recall`

**Answer:** Only that the scalar order is compatible with possible causality; it does not prove a → b

**Explanation:** The cited self-check in L02 tests whether the learner can connect Logical Clocks, Vector Clocks, and Causal Order to the module mechanism without replacing evidence with labels. This explanation is specific to M10-Q004 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M10-Q005

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** When neither vector is componentwise less than the other

**Explanation:** The cited self-check in L02 tests whether the learner can connect Logical Clocks, Vector Clocks, and Causal Order to the module mechanism without replacing evidence with labels. This explanation is specific to M10-Q005 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M10-Q006

**Type:** `short_answer`  
**Difficulty:** `synthesis`

**Answer:** Separate nodes can sort only the events they know. Without agreement on the accepted set/prefix, they may authorize different commands. One valid trace is a1 L1/[1,0], send L2/[2,0], a2 L3/[3,0]; b1 L1/[0,1], receive L3/[2,2], b2 L4/[2,3]. a2 and b1 are concurrent; b1 → b2; neither a2 → b2 nor b2 → a2 follows

**Explanation:** The cited self-check in L02 tests whether the learner can connect Logical Clocks, Vector Clocks, and Causal Order to the module mechanism without replacing evidence with labels. This explanation is specific to M10-Q006 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M10-Q007

**Type:** `short_answer`  
**Difficulty:** `recall`

**Answer:** Yes. A safe system may reject every write during quorum loss

**Explanation:** The cited self-check in L03 tests whether the learner can connect Safety, Liveness, Failure Detectors, and Consensus Boundaries to the module mechanism without replacing evidence with labels. This explanation is specific to M10-Q007 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M10-Q008

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** Only that the heartbeat was not observed before the local deadline under the observer's clock/scheduler/network conditions

**Explanation:** The cited self-check in L03 tests whether the learner can connect Safety, Liveness, Failure Detectors, and Consensus Boundaries to the module mechanism without replacing evidence with labels. This explanation is specific to M10-Q008 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M10-Q009

**Type:** `short_answer`  
**Difficulty:** `synthesis`

**Answer:** An operation-level invariant, a failure model requiring automatic agreement, and a comparison showing simpler authority/reconciliation choices are insufficient

**Explanation:** The cited self-check in L03 tests whether the learner can connect Safety, Liveness, Failure Detectors, and Consensus Boundaries to the module mechanism without replacing evidence with labels. This explanation is specific to M10-Q009 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M10-Q010

**Type:** `short_answer`  
**Difficulty:** `recall`

**Answer:** It provides a shared witness; protocol state/selection rules make that witness constrain later decisions

**Explanation:** The cited self-check in L04 tests whether the learner can connect Paxos, Raft, and Replicated-State-Machine Foundations to the module mechanism without replacing evidence with labels. This explanation is specific to M10-Q010 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M10-Q011

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** Consensus agrees on commands, not arbitrary local side effects. Different application results would violate replicated-state-machine equivalence

**Explanation:** The cited self-check in L04 tests whether the learner can connect Paxos, Raft, and Replicated-State-Machine Foundations to the module mechanism without replacing evidence with labels. This explanation is specific to M10-Q011 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M10-Q012

**Type:** `multiple_choice`  
**Difficulty:** `application`

**Choices:**

- Keep Physical Clocks, Drift, Skew, and Uncertainty scoped to its stated evidence and boundary.
- Choose the familiar tool before checking whether Treating NTP success as perfect time. Synchronization has error, age.
- Treat Treating NTP success as perfect time. Synchronization has error, age as complete proof without the lesson bound.
- Make the documented mistake: Treating NTP success as perfect time. Synchronization has error, a

**Answer:** Keep Physical Clocks, Drift, Skew, and Uncertainty scoped to its stated evidence and boundary.

**Explanation:** The distractors are anchored in the mistake list for L01; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M10-Q012 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M10-Q013

**Type:** `multiple_choice`  
**Difficulty:** `synthesis`

**Choices:**

- Make the documented mistake: Confusing monotonic duration with global order. A monotonic local
- Keep Physical Clocks, Drift, Skew, and Uncertainty scoped to its stated evidence and boundary.
- Treat Confusing monotonic duration with global order. A monotonic local clo as complete proof without the lesson boun.
- Choose the familiar tool before checking whether Confusing monotonic duration with global order. A monotonic local cl.

**Answer:** Keep Physical Clocks, Drift, Skew, and Uncertainty scoped to its stated evidence and boundary.

**Explanation:** The distractors are anchored in the mistake list for L01; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M10-Q013 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M10-Q014

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Choices:**

- Treat Using a lease without process-pause bounds. A client may stop executi as complete proof without the lesson boun.
- Make the documented mistake: Using a lease without process-pause bounds. A client may stop exec
- Keep Physical Clocks, Drift, Skew, and Uncertainty scoped to its stated evidence and boundary.
- Choose the familiar tool before checking whether Using a lease without process-pause bounds. A client may stop execut.

**Answer:** Keep Physical Clocks, Drift, Skew, and Uncertainty scoped to its stated evidence and boundary.

**Explanation:** The distractors are anchored in the mistake list for L01; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M10-Q014 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M10-Q015

**Type:** `multiple_choice`  
**Difficulty:** `application`

**Choices:**

- Choose the familiar tool before checking whether Using timestamps as fencing tokens. A resource needs a strictly orde.
- Treat Using timestamps as fencing tokens. A resource needs a strictly order as complete proof without the lesson boun.
- Make the documented mistake: Using timestamps as fencing tokens. A resource needs a strictly or
- Keep Physical Clocks, Drift, Skew, and Uncertainty scoped to its stated evidence and boundary.

**Answer:** Keep Physical Clocks, Drift, Skew, and Uncertainty scoped to its stated evidence and boundary.

**Explanation:** The distractors are anchored in the mistake list for L01; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M10-Q015 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M10-Q016

**Type:** `multiple_choice`  
**Difficulty:** `synthesis`

**Choices:**

- Keep Logical Clocks, Vector Clocks, and Causal Order scoped to its stated evidence and boundary.
- Treat Reading causality from scalar order. L(a) < L(b) can hold for concurr as complete proof without the lesson boun.
- Make the documented mistake: Reading causality from scalar order. L(a) < L(b) can hold for conc. with extra con
- Choose the familiar tool before checking whether Reading causality from scalar order. L(a) < L(b) can hold for concur.

**Answer:** Keep Logical Clocks, Vector Clocks, and Causal Order scoped to its stated evidence and boundary.

**Explanation:** The distractors are anchored in the mistake list for L02; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M10-Q016 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M10-Q017

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Choices:**

- Treat Calling concurrency simultaneous time. It means no observed causal pa as complete proof without the lesson boun.
- Keep Logical Clocks, Vector Clocks, and Causal Order scoped to its stated evidence and boundary.
- Choose the familiar tool before checking whether Calling concurrency simultaneous time. It means no observed causal p.
- Make the documented mistake: Calling concurrency simultaneous time. It means no observed causal. with extra con

**Answer:** Keep Logical Clocks, Vector Clocks, and Causal Order scoped to its stated evidence and boundary.

**Explanation:** The distractors are anchored in the mistake list for L02; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M10-Q017 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M10-Q018

**Type:** `multiple_choice`  
**Difficulty:** `application`

**Choices:**

- Choose the familiar tool before checking whether Ignoring identity lifecycle in vectors. Dynamic membership needs ver.
- Treat Ignoring identity lifecycle in vectors. Dynamic membership needs vers as complete proof without the lesson boun.
- Keep Logical Clocks, Vector Clocks, and Causal Order scoped to its stated evidence and boundary.
- Make the documented mistake: Ignoring identity lifecycle in vectors. Dynamic membership needs v. with extra con

**Answer:** Keep Logical Clocks, Vector Clocks, and Causal Order scoped to its stated evidence and boundary.

**Explanation:** The distractors are anchored in the mistake list for L02; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M10-Q018 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M10-Q019

**Type:** `multiple_choice`  
**Difficulty:** `synthesis`

**Choices:**

- Choose the familiar tool before checking whether Using a total tie-breaker as an invariant. Stable display order cann.
- Make the documented mistake: Using a total tie-breaker as an invariant. Stable display order ca. with extra con
- Treat Using a total tie-breaker as an invariant. Stable display order cannot as complete proof without the lesson bou.
- Keep Logical Clocks, Vector Clocks, and Causal Order scoped to its stated evidence and boundary.

**Answer:** Keep Logical Clocks, Vector Clocks, and Causal Order scoped to its stated evidence and boundary.

**Explanation:** The distractors are anchored in the mistake list for L02; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M10-Q019 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M10-Q020

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Original concurrency = 130 x 0.035 = 4.55 operations. Revised rate = 130 x 1.25 = 162.5/s, so revised concurrency = 162.5 x 0.035 = 5.69 operations.

**Explanation:** This perturbs the numeric practice around Physical Clocks, Drift, Skew, and Uncertainty: keep the same boundary, align milliseconds to seconds, then apply rate times scoped work. This explanation is specific to M10-Q020 and its cited source.

**Grading notes:** Full credit requires both concurrency values, unit conversion from ms to seconds, and a statement that the boundary stayed unchanged.

## M10-Q021

**Type:** `calculation`  
**Difficulty:** `recall`

**Answer:** Original concurrency = 140 x 0.045 = 6.30 operations. Revised rate = 140 x 1.30 = 182.0/s, so revised concurrency = 182.0 x 0.045 = 8.19 operations.

**Explanation:** This perturbs the numeric practice around Logical Clocks, Vector Clocks, and Causal Order: keep the same boundary, align milliseconds to seconds, then apply rate times scoped work. This explanation is specific to M10-Q021 and its cited source.

**Grading notes:** Full credit requires both concurrency values, unit conversion from ms to seconds, and a statement that the boundary stayed unchanged.

## M10-Q022

**Type:** `calculation`  
**Difficulty:** `application`

**Answer:** Original concurrency = 150 x 0.055 = 8.25 operations. Revised rate = 150 x 1.35 = 202.5/s, so revised concurrency = 202.5 x 0.055 = 11.14 operations.

**Explanation:** This perturbs the numeric practice around Safety, Liveness, Failure Detectors, and Consensus Boundaries: keep the same boundary, align milliseconds to seconds, then apply rate times scoped work. This explanation is specific to M10-Q022 and its cited source.

**Grading notes:** Full credit requires both concurrency values, unit conversion from ms to seconds, and a statement that the boundary stayed unchanged.

## M10-Q023

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Original concurrency = 160 x 0.065 = 10.40 operations. Revised rate = 160 x 1.40 = 224.0/s, so revised concurrency = 224.0 x 0.065 = 14.56 operations.

**Explanation:** This perturbs the numeric practice around Paxos, Raft, and Replicated-State-Machine Foundations: keep the same boundary, align milliseconds to seconds, then apply rate times scoped work. This explanation is specific to M10-Q023 and its cited source.

**Grading notes:** Full credit requires both concurrency values, unit conversion from ms to seconds, and a statement that the boundary stayed unchanged.

## M10-Q024

**Type:** `calculation`  
**Difficulty:** `recall`

**Answer:** Original concurrency = 170 x 0.075 = 12.75 operations. Revised rate = 170 x 1.45 = 246.5/s, so revised concurrency = 246.5 x 0.075 = 18.49 operations.

**Explanation:** This perturbs the numeric practice around Raft Leader Election and Persistent Hard State: keep the same boundary, align milliseconds to seconds, then apply rate times scoped work. This explanation is specific to M10-Q024 and its cited source.

**Grading notes:** Full credit requires both concurrency values, unit conversion from ms to seconds, and a statement that the boundary stayed unchanged.

## M10-Q025

**Type:** `calculation`  
**Difficulty:** `application`

**Answer:** Original concurrency = 180 x 0.035 = 6.30 operations. Revised rate = 180 x 1.10 = 198.0/s, so revised concurrency = 198.0 x 0.035 = 6.93 operations.

**Explanation:** This perturbs the numeric practice around Raft Log Replication, Commitment, and Application: keep the same boundary, align milliseconds to seconds, then apply rate times scoped work. This explanation is specific to M10-Q025 and its cited source.

**Grading notes:** Full credit requires both concurrency values, unit conversion from ms to seconds, and a statement that the boundary stayed unchanged.

## M10-Q026

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Original concurrency = 190 x 0.045 = 8.55 operations. Revised rate = 190 x 1.15 = 218.5/s, so revised concurrency = 218.5 x 0.045 = 9.83 operations.

**Explanation:** This perturbs the numeric practice around Clients, Linearizable Reads, Snapshots, and Compaction: keep the same boundary, align milliseconds to seconds, then apply rate times scoped work. This explanation is specific to M10-Q026 and its cited source.

**Grading notes:** Full credit requires both concurrency values, unit conversion from ms to seconds, and a statement that the boundary stayed unchanged.

## M10-Q027

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** The fixture tests f01-leader-termination-broken (broken), with C05 as the expected target. The strongest discriminator is the field that changes the mechanism under test, such as scenario_id=f01-leader-termination-broken, rather than the general presence of a lab run.

**Explanation:** The cited fixture is machine-readable source material for M10; diagnosis should start from the emitted fields and connect them to Safety, Liveness, Failure Detectors, and Consensus Boundaries. This explanation is specific to M10-Q027 and its cited source.

**Grading notes:** Full credit requires naming the mechanism or failure mode and citing one concrete field from the fixture. Partial credit is appropriate for a plausible mechanism without a discriminator.

## M10-Q028

**Type:** `scenario_diagnosis`  
**Difficulty:** `synthesis`

**Answer:** The fixture tests f01-leader-termination-repaired (repaired), with C05 as the expected target. The strongest discriminator is the field that changes the mechanism under test, such as scenario_id=f01-leader-termination-repaired, rather than the general presence of a lab run.

**Explanation:** The cited fixture is machine-readable source material for M10; diagnosis should start from the emitted fields and connect them to Paxos, Raft, and Replicated-State-Machine Foundations. This explanation is specific to M10-Q028 and its cited source.

**Grading notes:** Full credit requires naming the mechanism or failure mode and citing one concrete field from the fixture. Partial credit is appropriate for a plausible mechanism without a discriminator.

## M10-Q029

**Type:** `scenario_diagnosis`  
**Difficulty:** `recall`

**Answer:** The fixture tests f02-stale-partitioned-leader-broken (broken), with C08 as the expected target. The strongest discriminator is the field that changes the mechanism under test, such as scenario_id=f02-stale-partitioned-leader-broken, rather than the general presence of a lab run.

**Explanation:** The cited fixture is machine-readable source material for M10; diagnosis should start from the emitted fields and connect them to Raft Leader Election and Persistent Hard State. This explanation is specific to M10-Q029 and its cited source.

**Grading notes:** Full credit requires naming the mechanism or failure mode and citing one concrete field from the fixture. Partial credit is appropriate for a plausible mechanism without a discriminator.

## M10-Q030

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** The fixture tests f02-stale-partitioned-leader-repaired (repaired), with C08 as the expected target. The strongest discriminator is the field that changes the mechanism under test, such as scenario_id=f02-stale-partitioned-leader-repaired, rather than the general presence of a lab run.

**Explanation:** The cited fixture is machine-readable source material for M10; diagnosis should start from the emitted fields and connect them to Raft Log Replication, Commitment, and Application. This explanation is specific to M10-Q030 and its cited source.

**Grading notes:** Full credit requires naming the mechanism or failure mode and citing one concrete field from the fixture. Partial credit is appropriate for a plausible mechanism without a discriminator.

## M10-Q031

**Type:** `scenario_diagnosis`  
**Difficulty:** `synthesis`

**Answer:** The fixture tests f03-restart-persistence-broken (broken), with C01 as the expected target. The strongest discriminator is the field that changes the mechanism under test, such as scenario_id=f03-restart-persistence-broken, rather than the general presence of a lab run.

**Explanation:** The cited fixture is machine-readable source material for M10; diagnosis should start from the emitted fields and connect them to Clients, Linearizable Reads, Snapshots, and Compaction. This explanation is specific to M10-Q031 and its cited source.

**Grading notes:** Full credit requires naming the mechanism or failure mode and citing one concrete field from the fixture. Partial credit is appropriate for a plausible mechanism without a discriminator.

## M10-Q032

**Type:** `scenario_diagnosis`  
**Difficulty:** `recall`

**Answer:** The fixture tests f03-restart-persistence-repaired (repaired), with C01 as the expected target. The strongest discriminator is the field that changes the mechanism under test, such as scenario_id=f03-restart-persistence-repaired, rather than the general presence of a lab run.

**Explanation:** The cited fixture is machine-readable source material for M10; diagnosis should start from the emitted fields and connect them to Membership, Leases, Fencing, and Coordination Decisions. This explanation is specific to M10-Q032 and its cited source.

**Grading notes:** Full credit requires naming the mechanism or failure mode and citing one concrete field from the fixture. Partial credit is appropriate for a plausible mechanism without a discriminator.

## M10-Q033

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Recommend the option that preserves the Paxos, Raft, and Replicated-State-Machine Foundations mechanism under the exercise constraints: Two controllers synchronize within ±3 ms, drift at most 30 ppm, and have not synchronized for 200 seconds. Calculate each uncertainty radius and maximum pairwise skew The decision should be reversed if a repeated measurement or review shows the named constraint is false, the safer alternative meets the same outcome at lower operational cost, or the protected invariant is no longer owned by this boundary.

**Explanation:** The exercise asks for a defensible decision, not a preference. The answer must keep evidence and reversal conditions visible so the learner can change course when facts change. This explanation is specific to M10-Q033 and its cited source.

**Grading notes:** Full credit requires a clear recommendation, cited exercise evidence, and a falsifiable reversal condition. Half credit for a reasonable recommendation with no reversal condition.

## M10-Q034

**Type:** `design_judgment`  
**Difficulty:** `recall`

**Answer:** Recommend the option that preserves the Raft Leader Election and Persistent Hard State mechanism under the exercise constraints: Northstar proposes a 5-second mount lease renewed every second The decision should be reversed if a repeated measurement or review shows the named constraint is false, the safer alternative meets the same outcome at lower operational cost, or the protected invariant is no longer owned by this boundary.

**Explanation:** The exercise asks for a defensible decision, not a preference. The answer must keep evidence and reversal conditions visible so the learner can change course when facts change. This explanation is specific to M10-Q034 and its cited source.

**Grading notes:** Full credit requires a clear recommendation, cited exercise evidence, and a falsifiable reversal condition. Half credit for a reasonable recommendation with no reversal condition.

## M10-Q035

**Type:** `design_judgment`  
**Difficulty:** `application`

**Answer:** Recommend the option that preserves the Raft Log Replication, Commitment, and Application mechanism under the exercise constraints: Draw three processes. n1 sends configuration C to n2; n3 independently creates note N; n2 acknowledges C and later receives N. Mark every causal edge and identify concurrent pairs. The decision should be reversed if a repeated measurement or review shows the named constraint is false, the safer alternative meets the same outcome at lower operational cost, or the protected invariant is no longer owned by this boundary.

**Explanation:** The exercise asks for a defensible decision, not a preference. The answer must keep evidence and reversal conditions visible so the learner can change course when facts change. This explanation is specific to M10-Q035 and its cited source.

**Grading notes:** Full credit requires a clear recommendation, cited exercise evidence, and a falsifiable reversal condition. Half credit for a reasonable recommendation with no reversal condition.

## M10-Q036

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Recommend the option that preserves the Clients, Linearizable Reads, Snapshots, and Compaction mechanism under the exercise constraints: Assign Lamport and three-component vector clocks to EX-03. Add a stable display tie-breaker and explain why it does not make N causally precede C. The decision should be reversed if a repeated measurement or review shows the named constraint is false, the safer alternative meets the same outcome at lower operational cost, or the protected invariant is no longer owned by this boundary.

**Explanation:** The exercise asks for a defensible decision, not a preference. The answer must keep evidence and reversal conditions visible so the learner can change course when facts change. This explanation is specific to M10-Q036 and its cited source.

**Grading notes:** Full credit requires a clear recommendation, cited exercise evidence, and a falsifiable reversal condition. Half credit for a reasonable recommendation with no reversal condition.

## M10-Q037

**Type:** `design_judgment`  
**Difficulty:** `recall`

**Answer:** Recommend the option that preserves the Membership, Leases, Fencing, and Coordination Decisions mechanism under the exercise constraints: Write two falsifiable safety properties and one conditional liveness property for telescope controller failover The decision should be reversed if a repeated measurement or review shows the named constraint is false, the safer alternative meets the same outcome at lower operational cost, or the protected invariant is no longer owned by this boundary.

**Explanation:** The exercise asks for a defensible decision, not a preference. The answer must keep evidence and reversal conditions visible so the learner can change course when facts change. This explanation is specific to M10-Q037 and its cited source.

**Grading notes:** Full credit requires a clear recommendation, cited exercise evidence, and a falsifiable reversal condition. Half credit for a reasonable recommendation with no reversal condition.
