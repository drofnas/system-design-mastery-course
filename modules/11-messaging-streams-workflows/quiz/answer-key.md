# M11 Quiz Answer Key

This key covers all 38 questions for **Messaging, Streams, and Workflows**. Use it after an attempt, or provide it with the LLM grading prompt for feedback.

## M11-Q001

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** Not safely; concurrent disagreement needs a named resolution authority and may violate invariants while unresolved.

**Explanation:** M11-Q001 uses self-check 1 from Authority, Events, Queues, Logs, and Streams; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M11-Q002

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** No. An event is a domain claim with authority and identity; retention is a transport property.

**Explanation:** M11-Q002 uses self-check 2 from Authority, Events, Queues, Logs, and Streams; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M11-Q003

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** A tested procedure starting from authoritative identities/versions, with comparison oracles and bounded repair, not a diagram label.

**Explanation:** M11-Q003 uses self-check 3 from Authority, Events, Queues, Logs, and Streams; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M11-Q004

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** It avoids silent loss when retry plus idempotency is available; it does not make duplicates harmless by itself.

**Explanation:** M11-Q004 uses self-check 1 from Delivery Semantics, Identities, and Exactly-Once Boundaries; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M11-Q005

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** When an effect occurs outside the inbox transaction or dedupe retention is shorter than replay/retry exposure.

**Explanation:** M11-Q005 uses self-check 2 from Delivery Semantics, Identities, and Exactly-Once Boundaries; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M11-Q006

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** No. It proves only local uniqueness; the effect owner needs a stable key, receipt, or reconciliation query.

**Explanation:** M11-Q006 uses self-check 3 from Delivery Semantics, Identities, and Exactly-Once Boundaries; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M11-Q007

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** No. Consumers beyond partition count are idle; a hot partition or shared dependency remains the bottleneck.

**Explanation:** M11-Q007 uses self-check 1 from Ordering, Partition Keys, and Consumer Groups; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M11-Q008

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** It gives a log order under its producer contract, not proof of causal or authoritative order from every source.

**Explanation:** M11-Q008 uses self-check 2 from Ordering, Partition Keys, and Consumer Groups; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M11-Q009

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** Only under a published version/repair contract that preserves required transitions and records the skip; otherwise it may hide missing state.

**Explanation:** M11-Q009 uses self-check 3 from Ordering, Partition Keys, and Consumer Groups; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M11-Q010

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** No. It prevents the fact/publication-intent gap; publication remains retryable and potentially duplicated.

**Explanation:** M11-Q010 uses self-check 1 from Transactional Outbox, Inbox, and Change Data Capture; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M11-Q011

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** Redelivery after local commit but before broker acknowledgement, provided the inbox and local effect committed together.

**Explanation:** M11-Q011 uses self-check 2 from Transactional Outbox, Inbox, and Change Data Capture; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M11-Q012

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** It resolves to a database commit position with compatible schema/snapshot state and enough retained log to resume.

**Explanation:** M11-Q012 uses self-check 3 from Transactional Outbox, Inbox, and Change Data Capture; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M11-Q013

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Measure treat log data for review case one; limit the change. with margin
- Measure publish intent data for review case one; limit the change. with margin
- Measure copy entire data for review case one; limit the change.
- Measure choose event data for review case one; limit the change.

**Answer:** Measure treat log data for review case one; limit the change. with margin

**Explanation:** M11-Q013 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects treat log as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M11-Q014

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Measure generate new data for review case two; limit the change.
- Measure publish intent data for review case two; limit the change.
- Measure payload equality data for review case two; limit the change.
- Measure commit offset data for review case two; limit the change.

**Answer:** Measure publish intent data for review case two; limit the change.

**Explanation:** M11-Q014 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects publish intent as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M11-Q015

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Measure call broker data for review case three; limit the change.
- Measure require global data for review case three; limit the change.
- Measure copy entire data for review case three; limit the change.
- Measure key randomly data for review case three; limit the change.

**Answer:** Measure copy entire data for review case three; limit the change.

**Explanation:** M11-Q015 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects copy entire as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M11-Q016

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Measure assume partitions data for review case four; limit the change. with margin
- Measure ignore rebalance data for review case four; limit the change.
- Measure mark published data for review case four; limit the change.
- Measure choose event data for review case four; limit the change. with margin

**Answer:** Measure choose event data for review case four; limit the change. with margin

**Explanation:** M11-Q016 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects choose event as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M11-Q017

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Measure generate new data for review case five; limit the change.
- Measure delete immediately data for review case five; limit the change.
- Measure treat cdc data for review case five; limit the change.
- Measure store inbox data for review case five; limit the change.

**Answer:** Measure generate new data for review case five; limit the change.

**Explanation:** M11-Q017 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects generate new as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M11-Q018

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Measure replay live data for review case six; limit the change. with margin
- Measure payload equality data for review case six; limit the change.
- Measure skip poison data for review case six; limit the change.
- Measure trust counts data for review case six; limit the change.

**Answer:** Measure payload equality data for review case six; limit the change.

**Explanation:** M11-Q018 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects payload equality as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M11-Q019

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Measure repair authority data for review case seven; limit the change. with margin
- Measure event presence data for review case seven; limit the change.
- Measure commit offset data for review case seven; limit the change. with margin
- Measure compensate deleting data for review case seven; limit the change.

**Answer:** Measure commit offset data for review case seven; limit the change. with margin

**Explanation:** M11-Q019 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects commit offset as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M11-Q020

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Measure retry all data for review case eight; limit the change.
- Measure hide state data for review case eight; limit the change.
- Measure call watermark data for review case eight; limit the change.
- Measure call broker data for review case eight; limit the change.

**Answer:** Measure call broker data for review case eight; limit the change.

**Explanation:** M11-Q020 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects call broker as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M11-Q021

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** Calculation for authority, events, queues, logs, and streams, non-hot share is 1 - 0.35 = 0.65; 12 x 0.65 = 7.8 partition-equivalents remain.

**Explanation:** M11-Q021 uses partition parallelism from Authority, Events, Queues, Logs, and Streams and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M11-Q022

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** Calculation for delivery semantics, identities, and exactly-once boundaries, net drain is (240 - 150) / 1.25 = 72.0/s, so drain time is 54,000 / 72.0 = 750.0 seconds.

**Explanation:** M11-Q022 uses backlog drain from Delivery Semantics, Identities, and Exactly-Once Boundaries and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M11-Q023

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** Calculation for ordering, partition keys, and consumer groups, net drain is 240 - 150 = 90/s; 54,000 / 90 = 600.0 seconds.

**Explanation:** M11-Q023 uses stream drain from Ordering, Partition Keys, and Consumer Groups and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M11-Q024

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** Calculation for transactional outbox, inbox, and change data capture, net drain is 240 - 150 = 90/s; 54,000 / 90 = 600.0 seconds.

**Explanation:** M11-Q024 uses stream drain from Transactional Outbox, Inbox, and Change Data Capture and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M11-Q025

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** Diagnosis for authority, events, queues, logs, and streams, authority.facts.0.version and broker.duplicates separate the mechanism. authority.facts.0.version = 3 while broker.duplicates = 0, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare authority.facts.0.version with broker.duplicates and connect that contrast to authority, events, queues, logs, and streams.

**Grading notes:** Full credit names Authority, Events, Queues, Logs, and Streams, cites authority.facts.0.version and broker.duplicates, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M11-Q026

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** Diagnosis for delivery semantics, identities, and exactly-once boundaries, authority.facts.0.version and broker.records.0.position separate the mechanism. authority.facts.0.version = 3 while broker.records.0.position = 0, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare authority.facts.0.version with broker.records.0.position and connect that contrast to delivery semantics, identities, and exactly-once boundaries.

**Grading notes:** Full credit names Delivery Semantics, Identities, and Exactly-Once Boundaries, cites authority.facts.0.version and broker.records.0.position, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M11-Q027

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** Diagnosis for ordering, partition keys, and consumer groups, authority.facts.0.version and broker.records.1.position separate the mechanism. authority.facts.0.version = 3 while broker.records.1.position = 1, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare authority.facts.0.version with broker.records.1.position and connect that contrast to ordering, partition keys, and consumer groups.

**Grading notes:** Full credit names Ordering, Partition Keys, and Consumer Groups, cites authority.facts.0.version and broker.records.1.position, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M11-Q028

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** Diagnosis for transactional outbox, inbox, and change data capture, authority.version and broker.duplicates separate the mechanism. authority.version = 3 while broker.duplicates = 1, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare authority.version with broker.duplicates and connect that contrast to transactional outbox, inbox, and change data capture.

**Grading notes:** Full credit names Transactional Outbox, Inbox, and Change Data Capture, cites authority.version and broker.duplicates, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M11-Q029

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** Diagnosis for replay, poison records, and reconciliation, authority.version and broker.records.0.position separate the mechanism. authority.version = 3 while broker.records.0.position = 0, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare authority.version with broker.records.0.position and connect that contrast to replay, poison records, and reconciliation.

**Grading notes:** Full credit names Replay, Poison Records, and Reconciliation, cites authority.version and broker.records.0.position, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M11-Q030

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** Diagnosis for workflow state, sagas, and compensation, authority.version and consumer.applications separate the mechanism. authority.version = 3 while consumer.applications = 1, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare authority.version with consumer.applications and connect that contrast to workflow state, sagas, and compensation.

**Grading notes:** Full credit names Workflow State, Sagas, and Compensation, cites authority.version and consumer.applications, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M11-Q031

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** Diagnosis for event time, watermarks, lag, and bounded recovery, broker.duplicates and broker.records.0.version separate the mechanism. broker.duplicates = 0 while broker.records.0.version = 3, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare broker.duplicates with broker.records.0.version and connect that contrast to event time, watermarks, lag, and bounded recovery.

**Grading notes:** Full credit names Event Time, Watermarks, Lag, and Bounded Recovery, cites broker.duplicates and broker.records.0.version, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M11-Q032

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** Diagnosis for asynchronous architecture decisions, broker.duplicates and consumer.applications separate the mechanism. broker.duplicates = 0 while consumer.applications = 1, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare broker.duplicates with consumer.applications and connect that contrast to asynchronous architecture decisions.

**Grading notes:** Full credit names Asynchronous Architecture Decisions, cites broker.duplicates and consumer.applications, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M11-Q033

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** Diagnosis for authority, events, queues, logs, and streams, broker.records.0.position and broker.records.0.version separate the mechanism. broker.records.0.position = 0 while broker.records.0.version = 3, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare broker.records.0.position with broker.records.0.version and connect that contrast to authority, events, queues, logs, and streams.

**Grading notes:** Full credit names Authority, Events, Queues, Logs, and Streams, cites broker.records.0.position and broker.records.0.version, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M11-Q034

**Type:** `design_judgment`
**Difficulty:** `application`

**Answer:** Approve Authority and derived state at 141.4/s. The deciding number is 213 x 0.72 = 153.4/s, leaving 12/s before the reserve is consumed. Withdraw approval if a drill, trace, or workload sample shows authority and derived state demand above 153.4/s or proves the shed point cannot protect lower-priority work.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to authority and derived state demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 153.4/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M11-Q035

**Type:** `design_judgment`
**Difficulty:** `synthesis`

**Answer:** Decline Event envelope review at 177/s. The deciding number is 230 x 0.72 = 165.6/s, so planned demand exceeds the usable region by 11.4/s. Approve later if repeated measurements lift usable capacity above 177/s or a named policy removes at least 11.4/s of deferrable work before saturation.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to event envelope review demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 165.6/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M11-Q036

**Type:** `design_judgment`
**Difficulty:** `recall`

**Answer:** Approve conditionally for Crash-window derivation. The deciding number is 247 x 0.72 = 177.8/s, and 172.8/s fits only while the fallback remains enforceable. Keep the condition until recovery traffic, priority demand, or fallback tests show less than 5/s of usable margin.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to crash-window derivation demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 177.8/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M11-Q037

**Type:** `design_judgment`
**Difficulty:** `application`

**Answer:** Approve Exactly-once claim audit at 173/s. The deciding number is 264 x 0.72 = 190.1/s, leaving 17.1/s before the reserve is consumed. Require redesign if a drill, trace, or workload sample shows exactly-once claim audit demand above 190.1/s or proves the shed point cannot protect lower-priority work.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to exactly-once claim audit demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 190.1/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M11-Q038

**Type:** `design_judgment`
**Difficulty:** `synthesis`

**Answer:** Decline Partition-key comparison at 217.9/s. The deciding number is 281 x 0.72 = 202.3/s, so planned demand exceeds the usable region by 15.6/s. Lift the decline if repeated measurements lift usable capacity above 217.9/s or a named policy removes at least 15.6/s of deferrable work before saturation.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to partition-key comparison demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 202.3/s, compares it with planned demand, and names a scenario-specific reversal condition.
