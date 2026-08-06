# M09 Quiz Answer Key

This key covers all 43 questions for **Replication and Partitioning**. Use it after an attempt, or provide it with the LLM grading prompt for feedback.

## M09-Q001

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** No. It is scoped to one session unless a stronger contract is also present.

**Explanation:** M09-Q001 uses self-check 1 from Operation Semantics and Session Guarantees; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M09-Q002

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** Yes. A session can observe versions 5, 5, 6 while authority is already at 9.

**Explanation:** M09-Q002 uses self-check 2 from Operation Semantics and Session Guarantees; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M09-Q003

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** A unit and bound, reference version/time, measurement point, failure action, and oracle.

**Explanation:** M09-Q003 uses self-check 3 from Operation Semantics and Session Guarantees; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M09-Q004

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** Eventual convergence permits a window where conflicting owners can act; the invariant is violated before convergence repairs state.

**Explanation:** M09-Q004 uses self-check 4 from Operation Semantics and Session Guarantees; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M09-Q005

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** No. The acknowledgement and placement contracts must prove durability and independence.

**Explanation:** M09-Q005 uses self-check 1 from Replication Topologies and Acknowledgement Boundaries; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M09-Q006

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** Detect concurrent versions and define who or what resolves them without violating the business invariant.

**Explanation:** M09-Q006 uses self-check 2 from Replication Topologies and Acknowledgement Boundaries; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M09-Q007

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** Followers can lag and the router may select one without a minimum-version rule.

**Explanation:** M09-Q007 uses self-check 3 from Replication Topologies and Acknowledgement Boundaries; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M09-Q008

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** Explicitly reject authority-changing writes or recover the known authority; do not invent an unproved election.

**Explanation:** M09-Q008 uses self-check 4 from Replication Topologies and Acknowledgement Boundaries; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M09-Q009

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** Both: 3+3>5 and 2×3>5.

**Explanation:** M09-Q009 uses self-check 1 from Quorums, Intersections, and Hidden Assumptions; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M09-Q010

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** Write/write intersection fails because 4 is not greater than 5.

**Explanation:** M09-Q010 uses self-check 2 from Quorums, Intersections, and Hidden Assumptions; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M09-Q011

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** Not from arithmetic alone; it may need to compare versions and meet the operation's freshness rule.

**Explanation:** M09-Q011 uses self-check 3 from Quorums, Intersections, and Hidden Assumptions; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M09-Q012

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** The formal CAP definition and a product's bounded success SLO measure different outcomes; mixing them produces false claims.

**Explanation:** M09-Q012 uses self-check 4 from Quorums, Intersections, and Hidden Assumptions; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M09-Q013

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** No. Clock error and concurrent writers can make timestamps misleading.

**Explanation:** M09-Q013 uses self-check 1 from Versions, Conflicts, Repair, and Convergence; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M09-Q014

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** A key that is never read is never compared.

**Explanation:** M09-Q014 uses self-check 2 from Versions, Conflicts, Repair, and Convergence; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M09-Q015

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Measure one label data for review case one; limit the change.
- Measure equating acknowledgement data for review case one; limit the change.
- Measure wall clock data for review case one; limit the change.
- Measure cache ttl data for review case one; limit the change.

**Answer:** Measure one label data for review case one; limit the change.

**Explanation:** M09-Q015 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects one label as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M09-Q016

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Measure failing open data for review case two; limit the change. with margin with margin
- Measure equating acknowledgement data for review case two; limit the change.
- Measure replication backup data for review case two; limit the change.
- Measure promising durability data for review case two; limit the change.

**Answer:** Measure equating acknowledgement data for review case two; limit the change.

**Explanation:** M09-Q016 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects equating acknowledgement as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M09-Q017

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Measure serving followers data for review case three; limit the change.
- Measure multi leader data for review case three; limit the change.
- Measure wall clock data for review case three; limit the change.
- Measure failover routing data for review case three; limit the change.

**Answer:** Measure wall clock data for review case three; limit the change.

**Explanation:** M09-Q017 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects wall clock as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M09-Q018

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Measure quoting linearizability data for review case four; limit the change.
- Measure write intersection data for review case four; limit the change.
- Measure hinted replicas data for review case four; limit the change.
- Measure cache ttl data for review case four; limit the change.

**Answer:** Measure cache ttl data for review case four; limit the change.

**Explanation:** M09-Q018 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects cache ttl as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M09-Q019

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Measure failing open data for review case five; limit the change.
- Measure equating timeout data for review case five; limit the change.
- Measure changing during data for review case five; limit the change.
- Measure last write data for review case five; limit the change.

**Answer:** Measure failing open data for review case five; limit the change.

**Explanation:** M09-Q019 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects failing open as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M09-Q020

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Measure retries conflict data for review case six; limit the change.
- Measure replication backup data for review case six; limit the change.
- Measure depending only data for review case six; limit the change.
- Measure merkle tree data for review case six; limit the change. with margin

**Answer:** Measure replication backup data for review case six; limit the change.

**Explanation:** M09-Q020 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects replication backup as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M09-Q021

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Measure repairing derived data for review case seven; limit the change.
- Measure averages declare data for review case seven; limit the change. with margin
- Measure promising durability data for review case seven; limit the change.
- Measure expecting consistent data for review case seven; limit the change.

**Answer:** Measure promising durability data for review case seven; limit the change.

**Explanation:** M09-Q021 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects promising durability as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M09-Q022

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Measure cutting routing data for review case eight; limit the change.
- Measure dual writing data for review case eight; limit the change. with margin
- Measure deleting old data for review case eight; limit the change.
- Measure serving followers data for review case eight; limit the change.

**Answer:** Measure serving followers data for review case eight; limit the change.

**Explanation:** M09-Q022 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects serving followers as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M09-Q023

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Measure multi leader data for review case nine; limit the change.
- Measure keys instead data for review case nine; limit the change.
- Measure replicas write data for review case nine; limit the change.
- Measure rate limiting data for review case nine; limit the change.

**Answer:** Measure multi leader data for review case nine; limit the change.

**Explanation:** M09-Q023 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects multi leader as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M09-Q024

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Measure letting background data for review case ten; limit the change.
- Measure failover routing data for review case ten; limit the change.
- Measure isolation authentication data for review case ten; limit the change.
- Measure labeling database data for review case ten; limit the change.

**Answer:** Measure failover routing data for review case ten; limit the change.

**Explanation:** M09-Q024 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects failover routing as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M09-Q025

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** Calculation for operation semantics and session guarantees, bytes are 10,000 x 1024 = 10,240,000; that is 9.77 MiB.

**Explanation:** M09-Q025 uses repair bytes from Operation Semantics and Session Guarantees and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M09-Q026

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** Calculation for replication topologies and acknowledgement boundaries, movement ratio is 2 / 8 = 0.25, or 25%.

**Explanation:** M09-Q026 uses key movement from Replication Topologies and Acknowledgement Boundaries and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M09-Q027

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** Calculation for quorums, intersections, and hidden assumptions, 200 GiB is 204800 MiB; 204800 / 40 = 5120 seconds, or 1.42 hours.

**Explanation:** M09-Q027 uses copy time from Quorums, Intersections, and Hidden Assumptions and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M09-Q028

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** Calculation for versions, conflicts, repair, and convergence, skew ratio is 120 / 40 = 3.0x.

**Explanation:** M09-Q028 uses skew ratio from Versions, Conflicts, Repair, and Convergence and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M09-Q029

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** Calculation for partitioning, consistent hashing, and resharding, serialization is 280 KiB x 8 / 900 Kbps = 2.49 seconds, ignoring protocol overhead.

**Explanation:** M09-Q029 uses serialization from Partitioning, Consistent Hashing, and Resharding and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M09-Q030

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** Calculation for hot keys, skew, fairness, and tenant isolation, it can lose 2 replicas and still collect 3 acknowledgements.

**Explanation:** M09-Q030 uses quorum from Hot Keys, Skew, Fairness, and Tenant Isolation and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M09-Q031

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** Diagnosis for operation semantics and session guarantees, acknowledgements.ambiguous and acknowledgements.successful separate the mechanism. acknowledgements.ambiguous = 0 while acknowledgements.successful = 4, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare acknowledgements.ambiguous with acknowledgements.successful and connect that contrast to operation semantics and session guarantees.

**Grading notes:** Full credit names Operation Semantics and Session Guarantees, cites acknowledgements.ambiguous and acknowledgements.successful, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M09-Q032

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** Diagnosis for replication topologies and acknowledgement boundaries, acknowledgements.ambiguous and availability.accepted separate the mechanism. acknowledgements.ambiguous = 0 while availability.accepted = 2, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare acknowledgements.ambiguous with availability.accepted and connect that contrast to replication topologies and acknowledgement boundaries.

**Grading notes:** Full credit names Replication Topologies and Acknowledgement Boundaries, cites acknowledgements.ambiguous and availability.accepted, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M09-Q033

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** Diagnosis for quorums, intersections, and hidden assumptions, acknowledgements.ambiguous and availability.ratio separate the mechanism. acknowledgements.ambiguous = 0 while availability.ratio = 1, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare acknowledgements.ambiguous with availability.ratio and connect that contrast to quorums, intersections, and hidden assumptions.

**Grading notes:** Full credit names Quorums, Intersections, and Hidden Assumptions, cites acknowledgements.ambiguous and availability.ratio, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M09-Q034

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** Diagnosis for versions, conflicts, repair, and convergence, acknowledgements.ambiguous and availability.total separate the mechanism. acknowledgements.ambiguous = 0 while availability.total = 3, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare acknowledgements.ambiguous with availability.total and connect that contrast to versions, conflicts, repair, and convergence.

**Grading notes:** Full credit names Versions, Conflicts, Repair, and Convergence, cites acknowledgements.ambiguous and availability.total, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M09-Q035

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** Diagnosis for partitioning, consistent hashing, and resharding, acknowledgements.attempted and availability.ratio separate the mechanism. acknowledgements.attempted = 3 while availability.ratio = 1, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare acknowledgements.attempted with availability.ratio and connect that contrast to partitioning, consistent hashing, and resharding.

**Grading notes:** Full credit names Partitioning, Consistent Hashing, and Resharding, cites acknowledgements.attempted and availability.ratio, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M09-Q036

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** Diagnosis for hot keys, skew, fairness, and tenant isolation, acknowledgements.successful and availability.ratio separate the mechanism. acknowledgements.successful = 3 while availability.ratio = 1, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare acknowledgements.successful with availability.ratio and connect that contrast to hot keys, skew, fairness, and tenant isolation.

**Grading notes:** Full credit names Hot Keys, Skew, Fairness, and Tenant Isolation, cites acknowledgements.successful and availability.ratio, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M09-Q037

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** Diagnosis for cap, pacelc, regional placement, security, and cost, acknowledgements.successful and availability.ratio separate the mechanism. acknowledgements.successful = 2 while availability.ratio = 1, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare acknowledgements.successful with availability.ratio and connect that contrast to cap, pacelc, regional placement, security, and cost.

**Grading notes:** Full credit names CAP, PACELC, Regional Placement, Security, and Cost, cites acknowledgements.successful and availability.ratio, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M09-Q038

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** Diagnosis for data-placement decisions, migration, and ownership, acknowledgements.successful and availability.total separate the mechanism. acknowledgements.successful = 2 while availability.total = 3, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare acknowledgements.successful with availability.total and connect that contrast to data-placement decisions, migration, and ownership.

**Grading notes:** Full credit names Data-Placement Decisions, Migration, and Ownership, cites acknowledgements.successful and availability.total, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M09-Q039

**Type:** `design_judgment`
**Difficulty:** `recall`

**Answer:** Approve Operation histories at 137/s. The deciding number is 207 x 0.72 = 149/s, leaving 12/s before the reserve is consumed. Withdraw approval if a drill, trace, or workload sample shows operation histories demand above 149/s or proves the shed point cannot protect lower-priority work.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to operation histories demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 149/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M09-Q040

**Type:** `design_judgment`
**Difficulty:** `application`

**Answer:** Decline Weakest sufficient contract at 172.7/s. The deciding number is 224 x 0.72 = 161.3/s, so planned demand exceeds the usable region by 11.4/s. Approve later if repeated measurements lift usable capacity above 172.7/s or a named policy removes at least 11.4/s of deferrable work before saturation.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to weakest sufficient contract demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 161.3/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M09-Q041

**Type:** `design_judgment`
**Difficulty:** `synthesis`

**Answer:** Approve conditionally for Acknowledgement trace. The deciding number is 241 x 0.72 = 173.5/s, and 168.5/s fits only while the fallback remains enforceable. Keep the condition until recovery traffic, priority demand, or fallback tests show less than 5/s of usable margin.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to acknowledgement trace demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 173.5/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M09-Q042

**Type:** `design_judgment`
**Difficulty:** `recall`

**Answer:** Approve Topology comparison at 168.7/s. The deciding number is 258 x 0.72 = 185.8/s, leaving 17.1/s before the reserve is consumed. Require redesign if a drill, trace, or workload sample shows topology comparison demand above 185.8/s or proves the shed point cannot protect lower-priority work.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to topology comparison demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 185.8/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M09-Q043

**Type:** `design_judgment`
**Difficulty:** `application`

**Answer:** Decline Quorum arithmetic at 213.6/s. The deciding number is 275 x 0.72 = 198/s, so planned demand exceeds the usable region by 15.6/s. Lift the decline if repeated measurements lift usable capacity above 213.6/s or a named policy removes at least 15.6/s of deferrable work before saturation.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to quorum arithmetic demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 198/s, compares it with planned demand, and names a scenario-specific reversal condition.
