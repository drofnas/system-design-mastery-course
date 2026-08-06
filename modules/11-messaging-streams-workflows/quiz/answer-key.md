# M11 Quiz Answer Key

This key covers all 37 questions for **Messaging, Streams, and Workflows**. Use it after an attempt, or provide it with the LLM grading prompt for feedback.

## M11-Q001

**Type:** `short_answer`  
**Difficulty:** `recall`

**Answer:** Not safely; concurrent disagreement needs a named resolution authority and may violate invariants while unresolved

**Explanation:** The cited self-check in L01 tests whether the learner can connect Authority, Events, Queues, Logs, and Streams to the module mechanism without replacing evidence with labels. This explanation is specific to M11-Q001 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M11-Q002

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** No. An event is a domain claim with authority and identity; retention is a transport property

**Explanation:** The cited self-check in L01 tests whether the learner can connect Authority, Events, Queues, Logs, and Streams to the module mechanism without replacing evidence with labels. This explanation is specific to M11-Q002 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M11-Q003

**Type:** `short_answer`  
**Difficulty:** `synthesis`

**Answer:** A tested procedure starting from authoritative identities/versions, with comparison oracles and bounded repair, not a diagram label

**Explanation:** The cited self-check in L01 tests whether the learner can connect Authority, Events, Queues, Logs, and Streams to the module mechanism without replacing evidence with labels. This explanation is specific to M11-Q003 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M11-Q004

**Type:** `short_answer`  
**Difficulty:** `recall`

**Answer:** It avoids silent loss when retry plus idempotency is available; it does not make duplicates harmless by itself

**Explanation:** The cited self-check in L02 tests whether the learner can connect Delivery Semantics, Identities, and Exactly-Once Boundaries to the module mechanism without replacing evidence with labels. This explanation is specific to M11-Q004 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M11-Q005

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** When an effect occurs outside the inbox transaction or dedupe retention is shorter than replay/retry exposure

**Explanation:** The cited self-check in L02 tests whether the learner can connect Delivery Semantics, Identities, and Exactly-Once Boundaries to the module mechanism without replacing evidence with labels. This explanation is specific to M11-Q005 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M11-Q006

**Type:** `short_answer`  
**Difficulty:** `synthesis`

**Answer:** No. It proves only local uniqueness; the effect owner needs a stable key, receipt, or reconciliation query

**Explanation:** The cited self-check in L02 tests whether the learner can connect Delivery Semantics, Identities, and Exactly-Once Boundaries to the module mechanism without replacing evidence with labels. This explanation is specific to M11-Q006 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M11-Q007

**Type:** `short_answer`  
**Difficulty:** `recall`

**Answer:** No. Consumers beyond partition count are idle; a hot partition or shared dependency remains the bottleneck

**Explanation:** The cited self-check in L03 tests whether the learner can connect Ordering, Partition Keys, and Consumer Groups to the module mechanism without replacing evidence with labels. This explanation is specific to M11-Q007 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M11-Q008

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** It gives a log order under its producer contract, not proof of causal or authoritative order from every source

**Explanation:** The cited self-check in L03 tests whether the learner can connect Ordering, Partition Keys, and Consumer Groups to the module mechanism without replacing evidence with labels. This explanation is specific to M11-Q008 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M11-Q009

**Type:** `short_answer`  
**Difficulty:** `synthesis`

**Answer:** Only under a published version/repair contract that preserves required transitions and records the skip; otherwise it may hide missing state

**Explanation:** The cited self-check in L03 tests whether the learner can connect Ordering, Partition Keys, and Consumer Groups to the module mechanism without replacing evidence with labels. This explanation is specific to M11-Q009 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M11-Q010

**Type:** `short_answer`  
**Difficulty:** `recall`

**Answer:** No. It prevents the fact/publication-intent gap; publication remains retryable and potentially duplicated

**Explanation:** The cited self-check in L04 tests whether the learner can connect Transactional Outbox, Inbox, and Change Data Capture to the module mechanism without replacing evidence with labels. This explanation is specific to M11-Q010 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M11-Q011

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** Redelivery after local commit but before broker acknowledgement, provided the inbox and local effect committed together

**Explanation:** The cited self-check in L04 tests whether the learner can connect Transactional Outbox, Inbox, and Change Data Capture to the module mechanism without replacing evidence with labels. This explanation is specific to M11-Q011 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M11-Q012

**Type:** `multiple_choice`  
**Difficulty:** `application`

**Choices:**

- Keep Authority, Events, Queues, Logs, and Streams scoped to its stated evidence and boundary.
- Choose the familiar tool before checking whether Treat the log as authority: it may omit a CDC change or retain an ob.
- Make the documented mistake: Treat the log as authority: it may omit a CDC change or retain an
- Treat Treat the log as authority: it may omit a CDC change or retain an obs as complete proof without the lesson boun.

**Answer:** Keep Authority, Events, Queues, Logs, and Streams scoped to its stated evidence and boundary.

**Explanation:** The distractors are anchored in the mistake list for L01; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M11-Q012 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M11-Q013

**Type:** `multiple_choice`  
**Difficulty:** `synthesis`

**Choices:**

- Treat Publish intent as fact: SendBulletinRequested is not evidence that a as complete proof without the lesson bound.
- Keep Authority, Events, Queues, Logs, and Streams scoped to its stated evidence and boundary.
- Make the documented mistake: Publish intent as fact: SendBulletinRequested is not evidence that
- Choose the familiar tool before checking whether Publish intent as fact: SendBulletinRequested is not evidence that a.

**Answer:** Keep Authority, Events, Queues, Logs, and Streams scoped to its stated evidence and boundary.

**Explanation:** The distractors are anchored in the mistake list for L01; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M11-Q013 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M11-Q014

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Choices:**

- Make the documented mistake: Copy entire rows: this leaks data and couples consumers to private
- Treat Copy entire rows: this leaks data and couples consumers to private st as complete proof without the lesson boun.
- Keep Authority, Events, Queues, Logs, and Streams scoped to its stated evidence and boundary.
- Choose the familiar tool before checking whether Copy entire rows: this leaks data and couples consumers to private s.

**Answer:** Keep Authority, Events, Queues, Logs, and Streams scoped to its stated evidence and boundary.

**Explanation:** The distractors are anchored in the mistake list for L01; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M11-Q014 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M11-Q015

**Type:** `multiple_choice`  
**Difficulty:** `application`

**Choices:**

- Choose the familiar tool before checking whether Choose event-driven boundaries first: extra deployables create owner.
- Treat Choose event-driven boundaries first: extra deployables create owners as complete proof without the lesson boun.
- Make the documented mistake: Choose event-driven boundaries first: extra deployables create own
- Keep Authority, Events, Queues, Logs, and Streams scoped to its stated evidence and boundary.

**Answer:** Keep Authority, Events, Queues, Logs, and Streams scoped to its stated evidence and boundary.

**Explanation:** The distractors are anchored in the mistake list for L01; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M11-Q015 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M11-Q016

**Type:** `multiple_choice`  
**Difficulty:** `synthesis`

**Choices:**

- Keep Delivery Semantics, Identities, and Exactly-Once Boundaries scoped to its stated evidence.
- Choose the familiar tool before checking whether Generate a new ID on retry: deduplication cannot recognize sameness.
- Make the documented mistake: Generate a new ID on retry: deduplication cannot recognize samenes
- Treat Generate a new ID on retry: deduplication cannot recognize sameness as complete proof without the lesson bounda.

**Answer:** Keep Delivery Semantics, Identities, and Exactly-Once Boundaries scoped to its stated evidence.

**Explanation:** The distractors are anchored in the mistake list for L02; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M11-Q016 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M11-Q017

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Choices:**

- Make the documented mistake: Use payload equality: legitimate equal events and serialization ch
- Keep Delivery Semantics, Identities, and Exactly-Once Boundaries scoped to its stated evidence.
- Treat Use payload equality: legitimate equal events and serialization chang as complete proof without the lesson boun.
- Choose the familiar tool before checking whether Use payload equality: legitimate equal events and serialization chan.

**Answer:** Keep Delivery Semantics, Identities, and Exactly-Once Boundaries scoped to its stated evidence.

**Explanation:** The distractors are anchored in the mistake list for L02; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M11-Q017 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M11-Q018

**Type:** `multiple_choice`  
**Difficulty:** `application`

**Choices:**

- Make the documented mistake: Commit offset before local state: a crash loses accepted work
- Choose the familiar tool before checking whether Commit offset before local state: a crash loses accepted work applies
- Keep Delivery Semantics, Identities, and Exactly-Once Boundaries scoped to its stated evidence.
- Treat Commit offset before local state: a crash loses accepted work as complete proof without the lesson boundary

**Answer:** Keep Delivery Semantics, Identities, and Exactly-Once Boundaries scoped to its stated evidence.

**Explanation:** The distractors are anchored in the mistake list for L02; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M11-Q018 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M11-Q019

**Type:** `multiple_choice`  
**Difficulty:** `synthesis`

**Choices:**

- Treat Call broker transactions end-to-end exactly once: external databases as complete proof without the lesson bound.
- Make the documented mistake: Call broker transactions end-to-end exactly once: external databas
- Choose the familiar tool before checking whether Call broker transactions end-to-end exactly once: external databases.
- Keep Delivery Semantics, Identities, and Exactly-Once Boundaries scoped to its stated evidence.

**Answer:** Keep Delivery Semantics, Identities, and Exactly-Once Boundaries scoped to its stated evidence.

**Explanation:** The distractors are anchored in the mistake list for L02; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M11-Q019 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M11-Q020

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Original concurrency = 140 x 0.040 = 5.60 operations. Revised rate = 140 x 1.25 = 175.0/s, so revised concurrency = 175.0 x 0.040 = 7.00 operations.

**Explanation:** This perturbs the numeric practice around Authority, Events, Queues, Logs, and Streams: keep the same boundary, align milliseconds to seconds, then apply rate times scoped work. This explanation is specific to M11-Q020 and its cited source.

**Grading notes:** Full credit requires both concurrency values, unit conversion from ms to seconds, and a statement that the boundary stayed unchanged.

## M11-Q021

**Type:** `calculation`  
**Difficulty:** `recall`

**Answer:** Original concurrency = 150 x 0.050 = 7.50 operations. Revised rate = 150 x 1.30 = 195.0/s, so revised concurrency = 195.0 x 0.050 = 9.75 operations.

**Explanation:** This perturbs the numeric practice around Delivery Semantics, Identities, and Exactly-Once Boundaries: keep the same boundary, align milliseconds to seconds, then apply rate times scoped work. This explanation is specific to M11-Q021 and its cited source.

**Grading notes:** Full credit requires both concurrency values, unit conversion from ms to seconds, and a statement that the boundary stayed unchanged.

## M11-Q022

**Type:** `calculation`  
**Difficulty:** `application`

**Answer:** Original concurrency = 160 x 0.060 = 9.60 operations. Revised rate = 160 x 1.35 = 216.0/s, so revised concurrency = 216.0 x 0.060 = 12.96 operations.

**Explanation:** This perturbs the numeric practice around Ordering, Partition Keys, and Consumer Groups: keep the same boundary, align milliseconds to seconds, then apply rate times scoped work. This explanation is specific to M11-Q022 and its cited source.

**Grading notes:** Full credit requires both concurrency values, unit conversion from ms to seconds, and a statement that the boundary stayed unchanged.

## M11-Q023

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Original concurrency = 170 x 0.070 = 11.90 operations. Revised rate = 170 x 1.40 = 238.0/s, so revised concurrency = 238.0 x 0.070 = 16.66 operations.

**Explanation:** This perturbs the numeric practice around Transactional Outbox, Inbox, and Change Data Capture: keep the same boundary, align milliseconds to seconds, then apply rate times scoped work. This explanation is specific to M11-Q023 and its cited source.

**Grading notes:** Full credit requires both concurrency values, unit conversion from ms to seconds, and a statement that the boundary stayed unchanged.

## M11-Q024

**Type:** `calculation`  
**Difficulty:** `recall`

**Answer:** Original concurrency = 180 x 0.080 = 14.40 operations. Revised rate = 180 x 1.45 = 261.0/s, so revised concurrency = 261.0 x 0.080 = 20.88 operations.

**Explanation:** This perturbs the numeric practice around Replay, Poison Records, and Reconciliation: keep the same boundary, align milliseconds to seconds, then apply rate times scoped work. This explanation is specific to M11-Q024 and its cited source.

**Grading notes:** Full credit requires both concurrency values, unit conversion from ms to seconds, and a statement that the boundary stayed unchanged.

## M11-Q025

**Type:** `calculation`  
**Difficulty:** `application`

**Answer:** Original concurrency = 190 x 0.040 = 7.60 operations. Revised rate = 190 x 1.10 = 209.0/s, so revised concurrency = 209.0 x 0.040 = 8.36 operations.

**Explanation:** This perturbs the numeric practice around Workflow State, Sagas, and Compensation: keep the same boundary, align milliseconds to seconds, then apply rate times scoped work. This explanation is specific to M11-Q025 and its cited source.

**Grading notes:** Full credit requires both concurrency values, unit conversion from ms to seconds, and a statement that the boundary stayed unchanged.

## M11-Q026

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Original concurrency = 200 x 0.050 = 10.00 operations. Revised rate = 200 x 1.15 = 230.0/s, so revised concurrency = 230.0 x 0.050 = 11.50 operations.

**Explanation:** This perturbs the numeric practice around Event Time, Watermarks, Lag, and Bounded Recovery: keep the same boundary, align milliseconds to seconds, then apply rate times scoped work. This explanation is specific to M11-Q026 and its cited source.

**Grading notes:** Full credit requires both concurrency values, unit conversion from ms to seconds, and a statement that the boundary stayed unchanged.

## M11-Q027

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** The fixture tests f01-atomic-outbox-broken (broken), with I01 as the expected target. The strongest discriminator is the field that changes the mechanism under test, such as scenario_id=f01-atomic-outbox-broken, rather than the general presence of a lab run.

**Explanation:** The cited fixture is machine-readable source material for M11; diagnosis should start from the emitted fields and connect them to Ordering, Partition Keys, and Consumer Groups. This explanation is specific to M11-Q027 and its cited source.

**Grading notes:** Full credit requires naming the mechanism or failure mode and citing one concrete field from the fixture. Partial credit is appropriate for a plausible mechanism without a discriminator.

## M11-Q028

**Type:** `scenario_diagnosis`  
**Difficulty:** `synthesis`

**Answer:** The fixture tests f01-atomic-outbox-repaired (repaired), with I01 as the expected target. The strongest discriminator is the field that changes the mechanism under test, such as scenario_id=f01-atomic-outbox-repaired, rather than the general presence of a lab run.

**Explanation:** The cited fixture is machine-readable source material for M11; diagnosis should start from the emitted fields and connect them to Transactional Outbox, Inbox, and Change Data Capture. This explanation is specific to M11-Q028 and its cited source.

**Grading notes:** Full credit requires naming the mechanism or failure mode and citing one concrete field from the fixture. Partial credit is appropriate for a plausible mechanism without a discriminator.

## M11-Q029

**Type:** `scenario_diagnosis`  
**Difficulty:** `recall`

**Answer:** The fixture tests f02-duplicate-delivery-broken (broken), with I03 as the expected target. The strongest discriminator is the field that changes the mechanism under test, such as scenario_id=f02-duplicate-delivery-broken, rather than the general presence of a lab run.

**Explanation:** The cited fixture is machine-readable source material for M11; diagnosis should start from the emitted fields and connect them to Replay, Poison Records, and Reconciliation. This explanation is specific to M11-Q029 and its cited source.

**Grading notes:** Full credit requires naming the mechanism or failure mode and citing one concrete field from the fixture. Partial credit is appropriate for a plausible mechanism without a discriminator.

## M11-Q030

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** The fixture tests f02-duplicate-delivery-repaired (repaired), with I03 as the expected target. The strongest discriminator is the field that changes the mechanism under test, such as scenario_id=f02-duplicate-delivery-repaired, rather than the general presence of a lab run.

**Explanation:** The cited fixture is machine-readable source material for M11; diagnosis should start from the emitted fields and connect them to Workflow State, Sagas, and Compensation. This explanation is specific to M11-Q030 and its cited source.

**Grading notes:** Full credit requires naming the mechanism or failure mode and citing one concrete field from the fixture. Partial credit is appropriate for a plausible mechanism without a discriminator.

## M11-Q031

**Type:** `scenario_diagnosis`  
**Difficulty:** `synthesis`

**Answer:** The fixture tests f03-effect-ambiguity-broken (broken), with I04 as the expected target. The strongest discriminator is the field that changes the mechanism under test, such as scenario_id=f03-effect-ambiguity-broken, rather than the general presence of a lab run.

**Explanation:** The cited fixture is machine-readable source material for M11; diagnosis should start from the emitted fields and connect them to Event Time, Watermarks, Lag, and Bounded Recovery. This explanation is specific to M11-Q031 and its cited source.

**Grading notes:** Full credit requires naming the mechanism or failure mode and citing one concrete field from the fixture. Partial credit is appropriate for a plausible mechanism without a discriminator.

## M11-Q032

**Type:** `scenario_diagnosis`  
**Difficulty:** `recall`

**Answer:** The fixture tests f03-effect-ambiguity-repaired (repaired), with I04 as the expected target. The strongest discriminator is the field that changes the mechanism under test, such as scenario_id=f03-effect-ambiguity-repaired, rather than the general presence of a lab run.

**Explanation:** The cited fixture is machine-readable source material for M11; diagnosis should start from the emitted fields and connect them to Asynchronous Architecture Decisions. This explanation is specific to M11-Q032 and its cited source.

**Grading notes:** Full credit requires naming the mechanism or failure mode and citing one concrete field from the fixture. Partial credit is appropriate for a plausible mechanism without a discriminator.

## M11-Q033

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Recommend the option that preserves the Transactional Outbox, Inbox, and Change Data Capture mechanism under the exercise constraints: Classify Northstar registry, outbox, broker record, catalog, bulletin receipt, and workflow history. Name authority and rebuild/repair. The decision should be reversed if a repeated measurement or review shows the named constraint is false, the safer alternative meets the same outcome at lower operational cost, or the protected invariant is no longer owned by this boundary.

**Explanation:** The exercise asks for a defensible decision, not a preference. The answer must keep evidence and reversal conditions visible so the learner can change course when facts change. This explanation is specific to M11-Q033 and its cited source.

**Grading notes:** Full credit requires a clear recommendation, cited exercise evidence, and a falsifiable reversal condition. Half credit for a reasonable recommendation with no reversal condition.

## M11-Q034

**Type:** `design_judgment`  
**Difficulty:** `recall`

**Answer:** Recommend the option that preserves the Replay, Poison Records, and Reconciliation mechanism under the exercise constraints: Draft ObservationPublished; justify identity, aggregate version, schema, time, payload, trace, and excluded private fields. The decision should be reversed if a repeated measurement or review shows the named constraint is false, the safer alternative meets the same outcome at lower operational cost, or the protected invariant is no longer owned by this boundary.

**Explanation:** The exercise asks for a defensible decision, not a preference. The answer must keep evidence and reversal conditions visible so the learner can change course when facts change. This explanation is specific to M11-Q034 and its cited source.

**Grading notes:** Full credit requires a clear recommendation, cited exercise evidence, and a falsifiable reversal condition. Half credit for a reasonable recommendation with no reversal condition.

## M11-Q035

**Type:** `design_judgment`  
**Difficulty:** `application`

**Answer:** Recommend the option that preserves the Workflow State, Sagas, and Compensation mechanism under the exercise constraints: Draw process/acknowledge orderings and identify loss, duplicate, and ambiguous outcomes. The decision should be reversed if a repeated measurement or review shows the named constraint is false, the safer alternative meets the same outcome at lower operational cost, or the protected invariant is no longer owned by this boundary.

**Explanation:** The exercise asks for a defensible decision, not a preference. The answer must keep evidence and reversal conditions visible so the learner can change course when facts change. This explanation is specific to M11-Q035 and its cited source.

**Grading notes:** Full credit requires a clear recommendation, cited exercise evidence, and a falsifiable reversal condition. Half credit for a reasonable recommendation with no reversal condition.

## M11-Q036

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Recommend the option that preserves the Event Time, Watermarks, Lag, and Bounded Recovery mechanism under the exercise constraints: Audit "the bulletin pipeline is exactly once." Name every participating state, transaction, and external effect. The decision should be reversed if a repeated measurement or review shows the named constraint is false, the safer alternative meets the same outcome at lower operational cost, or the protected invariant is no longer owned by this boundary.

**Explanation:** The exercise asks for a defensible decision, not a preference. The answer must keep evidence and reversal conditions visible so the learner can change course when facts change. This explanation is specific to M11-Q036 and its cited source.

**Grading notes:** Full credit requires a clear recommendation, cited exercise evidence, and a falsifiable reversal condition. Half credit for a reasonable recommendation with no reversal condition.

## M11-Q037

**Type:** `design_judgment`  
**Difficulty:** `recall`

**Answer:** Recommend the option that preserves the Asynchronous Architecture Decisions mechanism under the exercise constraints: Compare observation, institution, and random keys for ordering, skew, fairness, privacy, and parallelism. The decision should be reversed if a repeated measurement or review shows the named constraint is false, the safer alternative meets the same outcome at lower operational cost, or the protected invariant is no longer owned by this boundary.

**Explanation:** The exercise asks for a defensible decision, not a preference. The answer must keep evidence and reversal conditions visible so the learner can change course when facts change. This explanation is specific to M11-Q037 and its cited source.

**Grading notes:** Full credit requires a clear recommendation, cited exercise evidence, and a falsifiable reversal condition. Half credit for a reasonable recommendation with no reversal condition.
