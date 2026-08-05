# M10 Quiz Answer Key

This key covers all 100 questions for **Time, Coordination, and Consensus**. Use it after an attempt, or provide it with the LLM grading prompt for feedback.

## M10-Q001

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to calculate physical-clock drift, skew, and uncertainty and diagnose conclusions that exceed the available clock contract.

**Explanation:** Use Physical Clocks, Drift, Skew, and Uncertainty to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M10-Q002

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Logical Clocks, Vector Clocks, and Causal Order', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Logical Clocks, Vector Clocks, and Causal Order to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M10-Q003

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. - Write falsifiable safety and conditional liveness properties.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M10-Q004

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **“Majorities overlap, therefore safe.”** The intersection must retain and

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M10-Q005

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for implement client deduplication and linearizable reads with explicit ambiguous-outcome and quorum barriers..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - Ongaro and Ousterhout, Sections 5.2 and 5.4.1.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M10-Q006

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to protect snapshots, membership changes, leases, and external resources with atomic state, overlapping quorums, and fencing.

**Explanation:** Use Raft Log Replication, Commitment, and Application to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M10-Q007

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Clients, Linearizable Reads, Snapshots, and Compaction', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Clients, Linearizable Reads, Snapshots, and Compaction to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M10-Q008

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. - Prove quorum overlap through a membership transition.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M10-Q009

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Treating NTP success as perfect time.** Synchronization has error, age, and

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M10-Q010

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for derive happened-before, lamport-clock, and vector-clock relationships without treating display order as causality..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - Lamport, Time, Clocks, and the Ordering of Events, pages 558–563.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M10-Q011

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to separate safety, liveness, and failure-detector assumptions and select consensus only for properties that require agreement.

**Explanation:** Use Safety, Liveness, Failure Detectors, and Consensus Boundaries to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M10-Q012

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Paxos, Raft, and Replicated-State-Machine Foundations', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Paxos, Raft, and Replicated-State-Machine Foundations to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M10-Q013

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. - Trace follower, candidate, and leader transitions across terms.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M10-Q014

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Equating majority storage with commitment in every term.** The current-term

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M10-Q015

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for diagnose eight coordination failures from immutable same-input evidence and scoped safety oracles..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - Ongaro and Ousterhout, Sections 6–7.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M10-Q016

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to defend a coordination architecture covering alternatives, operating limits, security, cost, migration, ownership, dissent, and reversal evidence.

**Explanation:** Use Membership, Leases, Fencing, and Coordination Decisions to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M10-Q017

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Physical Clocks, Drift, Skew, and Uncertainty', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Physical Clocks, Drift, Skew, and Uncertainty to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M10-Q018

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. - Derive happened-before from process and message events.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M10-Q019

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Writing “the system is consistent.”** Properties apply to operations and

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M10-Q020

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for implement and diagnose raft elections, persistent hard state, log matching, commitment, and state-machine application..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - Lamport, Paxos Made Simple.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M10-Q021

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to implement client deduplication and linearizable reads with explicit ambiguous-outcome and quorum barriers.

**Explanation:** Use Raft Leader Election and Persistent Hard State to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M10-Q022

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Raft Log Replication, Commitment, and Application', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Raft Log Replication, Commitment, and Application to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M10-Q023

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. - Make duplicate delivery produce one logical state-machine effect.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M10-Q024

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Changing local config files independently.** Consensus quorums may no longer

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M10-Q025

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for calculate physical-clock drift, skew, and uncertainty and diagnose conclusions that exceed the available clock contract..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - Corbett et al., Spanner, Sections 3 and 4.1–4.2.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M10-Q026

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to derive happened-before, lamport-clock, and vector-clock relationships without treating display order as causality.

**Explanation:** Use Logical Clocks, Vector Clocks, and Causal Order to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M10-Q027

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Safety, Liveness, Failure Detectors, and Consensus Boundaries', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Safety, Liveness, Failure Detectors, and Consensus Boundaries to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M10-Q028

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. - Explain quorum agreement as an intersection plus value-selection rules.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M10-Q029

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Treating randomized timeout as safety.** Vote persistence and quorum

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M10-Q030

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for protect snapshots, membership changes, leases, and external resources with atomic state, overlapping quorums, and fencing..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - Ongaro and Ousterhout, Sections 5.3–5.4 and Figure 2.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M10-Q031

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to diagnose eight coordination failures from immutable same-input evidence and scoped safety oracles.

**Explanation:** Use Clients, Linearizable Reads, Snapshots, and Compaction to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M10-Q032

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Membership, Leases, Fencing, and Coordination Decisions', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Membership, Leases, Fencing, and Coordination Decisions to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M10-Q033

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. - Calculate worst-case drift and pairwise skew over a stated interval.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M10-Q034

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Reading causality from scalar order.** `L(a) < L(b)` can hold for concurrent

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M10-Q035

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for separate safety, liveness, and failure-detector assumptions and select consensus only for properties that require agreement..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - Ongaro and Ousterhout, In Search of an Understandable Consensus Algorithm.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M10-Q036

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to implement and diagnose raft elections, persistent hard state, log matching, commitment, and state-machine application.

**Explanation:** Use Paxos, Raft, and Replicated-State-Machine Foundations to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M10-Q037

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Raft Leader Election and Persistent Hard State', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Raft Leader Election and Persistent Hard State to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M10-Q038

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. - Execute AppendEntries predecessor checks and safe suffix repair.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M10-Q039

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Claiming exactly-once transport.** The contract is one logical effect for a

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M10-Q040

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for defend a coordination architecture covering alternatives, operating limits, security, cost, migration, ownership, dissent, and reversal evidence..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - Ongaro and Ousterhout, Section 6 and dissertation membership extension.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M10-Q041

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to calculate physical-clock drift, skew, and uncertainty and diagnose conclusions that exceed the available clock contract.

**Explanation:** Use Physical Clocks, Drift, Skew, and Uncertainty to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M10-Q042

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Logical Clocks, Vector Clocks, and Causal Order', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Logical Clocks, Vector Clocks, and Causal Order to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M10-Q043

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. - Write falsifiable safety and conditional liveness properties.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M10-Q044

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **“Majorities overlap, therefore safe.”** The intersection must retain and

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M10-Q045

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for implement client deduplication and linearizable reads with explicit ambiguous-outcome and quorum barriers..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - Ongaro and Ousterhout, Sections 5.2 and 5.4.1.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M10-Q046

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to protect snapshots, membership changes, leases, and external resources with atomic state, overlapping quorums, and fencing.

**Explanation:** Use Raft Log Replication, Commitment, and Application to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M10-Q047

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Clients, Linearizable Reads, Snapshots, and Compaction', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Clients, Linearizable Reads, Snapshots, and Compaction to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M10-Q048

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. - Prove quorum overlap through a membership transition.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M10-Q049

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Treating NTP success as perfect time.** Synchronization has error, age, and

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M10-Q050

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for derive happened-before, lamport-clock, and vector-clock relationships without treating display order as causality..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - Lamport, Time, Clocks, and the Ordering of Events, pages 558–563.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M10-Q051

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to separate safety, liveness, and failure-detector assumptions and select consensus only for properties that require agreement.

**Explanation:** Use Safety, Liveness, Failure Detectors, and Consensus Boundaries to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M10-Q052

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Paxos, Raft, and Replicated-State-Machine Foundations', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Paxos, Raft, and Replicated-State-Machine Foundations to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M10-Q053

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. - Trace follower, candidate, and leader transitions across terms.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M10-Q054

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Equating majority storage with commitment in every term.** The current-term

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M10-Q055

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for diagnose eight coordination failures from immutable same-input evidence and scoped safety oracles..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - Ongaro and Ousterhout, Sections 6–7.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M10-Q056

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to defend a coordination architecture covering alternatives, operating limits, security, cost, migration, ownership, dissent, and reversal evidence.

**Explanation:** Use Membership, Leases, Fencing, and Coordination Decisions to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M10-Q057

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Physical Clocks, Drift, Skew, and Uncertainty', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Physical Clocks, Drift, Skew, and Uncertainty to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M10-Q058

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. - Derive happened-before from process and message events.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M10-Q059

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Writing “the system is consistent.”** Properties apply to operations and

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M10-Q060

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for implement and diagnose raft elections, persistent hard state, log matching, commitment, and state-machine application..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - Lamport, Paxos Made Simple.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M10-Q061

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to implement client deduplication and linearizable reads with explicit ambiguous-outcome and quorum barriers.

**Explanation:** Use Raft Leader Election and Persistent Hard State to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M10-Q062

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Raft Log Replication, Commitment, and Application', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Raft Log Replication, Commitment, and Application to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M10-Q063

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. - Make duplicate delivery produce one logical state-machine effect.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M10-Q064

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Changing local config files independently.** Consensus quorums may no longer

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M10-Q065

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for calculate physical-clock drift, skew, and uncertainty and diagnose conclusions that exceed the available clock contract..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - Corbett et al., Spanner, Sections 3 and 4.1–4.2.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M10-Q066

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to derive happened-before, lamport-clock, and vector-clock relationships without treating display order as causality.

**Explanation:** Use Logical Clocks, Vector Clocks, and Causal Order to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M10-Q067

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Safety, Liveness, Failure Detectors, and Consensus Boundaries', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Safety, Liveness, Failure Detectors, and Consensus Boundaries to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M10-Q068

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. - Explain quorum agreement as an intersection plus value-selection rules.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M10-Q069

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Treating randomized timeout as safety.** Vote persistence and quorum

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M10-Q070

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for protect snapshots, membership changes, leases, and external resources with atomic state, overlapping quorums, and fencing..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - Ongaro and Ousterhout, Sections 5.3–5.4 and Figure 2.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M10-Q071

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to diagnose eight coordination failures from immutable same-input evidence and scoped safety oracles.

**Explanation:** Use Clients, Linearizable Reads, Snapshots, and Compaction to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M10-Q072

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Membership, Leases, Fencing, and Coordination Decisions', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Membership, Leases, Fencing, and Coordination Decisions to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M10-Q073

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. - Calculate worst-case drift and pairwise skew over a stated interval.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M10-Q074

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Reading causality from scalar order.** `L(a) < L(b)` can hold for concurrent

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M10-Q075

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for separate safety, liveness, and failure-detector assumptions and select consensus only for properties that require agreement..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - Ongaro and Ousterhout, In Search of an Understandable Consensus Algorithm.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M10-Q076

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to implement and diagnose raft elections, persistent hard state, log matching, commitment, and state-machine application.

**Explanation:** Use Paxos, Raft, and Replicated-State-Machine Foundations to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M10-Q077

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Raft Leader Election and Persistent Hard State', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Raft Leader Election and Persistent Hard State to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M10-Q078

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. - Execute AppendEntries predecessor checks and safe suffix repair.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M10-Q079

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Claiming exactly-once transport.** The contract is one logical effect for a

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M10-Q080

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for defend a coordination architecture covering alternatives, operating limits, security, cost, migration, ownership, dissent, and reversal evidence..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - Ongaro and Ousterhout, Section 6 and dissertation membership extension.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M10-Q081

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to calculate physical-clock drift, skew, and uncertainty and diagnose conclusions that exceed the available clock contract.

**Explanation:** Use Physical Clocks, Drift, Skew, and Uncertainty to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M10-Q082

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Logical Clocks, Vector Clocks, and Causal Order', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Logical Clocks, Vector Clocks, and Causal Order to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M10-Q083

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. - Write falsifiable safety and conditional liveness properties.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M10-Q084

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **“Majorities overlap, therefore safe.”** The intersection must retain and

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M10-Q085

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for implement client deduplication and linearizable reads with explicit ambiguous-outcome and quorum barriers..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - Ongaro and Ousterhout, Sections 5.2 and 5.4.1.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M10-Q086

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to protect snapshots, membership changes, leases, and external resources with atomic state, overlapping quorums, and fencing.

**Explanation:** Use Raft Log Replication, Commitment, and Application to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M10-Q087

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Clients, Linearizable Reads, Snapshots, and Compaction', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Clients, Linearizable Reads, Snapshots, and Compaction to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M10-Q088

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. - Prove quorum overlap through a membership transition.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M10-Q089

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Treating NTP success as perfect time.** Synchronization has error, age, and

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M10-Q090

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for derive happened-before, lamport-clock, and vector-clock relationships without treating display order as causality..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - Lamport, Time, Clocks, and the Ordering of Events, pages 558–563.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M10-Q091

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to separate safety, liveness, and failure-detector assumptions and select consensus only for properties that require agreement.

**Explanation:** Use Safety, Liveness, Failure Detectors, and Consensus Boundaries to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M10-Q092

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Paxos, Raft, and Replicated-State-Machine Foundations', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Paxos, Raft, and Replicated-State-Machine Foundations to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M10-Q093

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. - Trace follower, candidate, and leader transitions across terms.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M10-Q094

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Equating majority storage with commitment in every term.** The current-term

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M10-Q095

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for diagnose eight coordination failures from immutable same-input evidence and scoped safety oracles..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - Ongaro and Ousterhout, Sections 6–7.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M10-Q096

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to defend a coordination architecture covering alternatives, operating limits, security, cost, migration, ownership, dissent, and reversal evidence.

**Explanation:** Use Membership, Leases, Fencing, and Coordination Decisions to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M10-Q097

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Physical Clocks, Drift, Skew, and Uncertainty', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Physical Clocks, Drift, Skew, and Uncertainty to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M10-Q098

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. - Derive happened-before from process and message events.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M10-Q099

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Writing “the system is consistent.”** Properties apply to operations and

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M10-Q100

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for implement and diagnose raft elections, persistent hard state, log matching, commitment, and state-machine application..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - Lamport, Paxos Made Simple.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.
