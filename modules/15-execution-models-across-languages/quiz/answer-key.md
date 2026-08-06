# M15 Quiz Answer Key

This key covers all 38 questions for **Execution Models Across Languages**. Use it after an attempt, or provide it with the LLM grading prompt for feedback.

## M15-Q001

**Type:** `short_answer`  
**Difficulty:** `recall`

**Answer:** No. Borrow rules cover memory access; external-resource lifetime still needs an owned close path and observed cleanup

**Explanation:** The cited self-check in L01 tests whether the learner can connect Memory Lifetime and Management to the module mechanism without replacing evidence with labels. This explanation is specific to M15-Q001 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M15-Q002

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** The runtime or allocator may keep reclaimed regions for reuse; object reachability, heap commitment, and RSS are different measures

**Explanation:** The cited self-check in L01 tests whether the learner can connect Memory Lifetime and Management to the module mechanism without replacing evidence with labels. This explanation is specific to M15-Q002 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M15-Q003

**Type:** `short_answer`  
**Difficulty:** `synthesis`

**Answer:** Retainer paths or owner identities show continuing reachability; collector events plus falling live-set size suggest delayed reclamation instead

**Explanation:** The cited self-check in L01 tests whether the learner can connect Memory Lifetime and Management to the module mechanism without replacing evidence with labels. This explanation is specific to M15-Q003 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M15-Q004

**Type:** `short_answer`  
**Difficulty:** `recall`

**Answer:** One core or executor thread may be saturated while the host has idle cores; throttling or a blocked scheduler can also hide behind aggregate CPU

**Explanation:** The cited self-check in L02 tests whether the learner can connect Schedulers, Event Loops, and Tasks to the module mechanism without replacing evidence with labels. This explanation is specific to M15-Q004 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M15-Q005

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** It reduces the cost and coupling of one Java task to one OS thread. It does not add CPU, memory, connections, downstream capacity, deadlines, or bounds

**Explanation:** The cited self-check in L02 tests whether the learner can connect Schedulers, Event Loops, and Tasks to the module mechanism without replacing evidence with labels. This explanation is specific to M15-Q005 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M15-Q006

**Type:** `short_answer`  
**Difficulty:** `synthesis`

**Answer:** When offered children are unbounded or cancellation/cleanup does not own their lifetime, task count and external work can grow beyond the budget

**Explanation:** The cited self-check in L02 tests whether the learner can connect Schedulers, Event Loops, and Tasks to the module mechanism without replacing evidence with labels. This explanation is specific to M15-Q006 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M15-Q007

**Type:** `short_answer`  
**Difficulty:** `recall`

**Answer:** Orphan work consumes resources, may perform effects after authority expires, and can leak request or tenant context

**Explanation:** The cited self-check in L03 tests whether the learner can connect Bounded Fan-out and Structured Cleanup to the module mechanism without replacing evidence with labels. This explanation is specific to M15-Q007 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M15-Q008

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** Validate a small bounded envelope, then admit before large allocation or child creation. Otherwise rejected work can still exhaust the service

**Explanation:** The cited self-check in L03 tests whether the learner can connect Bounded Fan-out and Structured Cleanup to the module mechanism without replacing evidence with labels. This explanation is specific to M15-Q008 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M15-Q009

**Type:** `short_answer`  
**Difficulty:** `synthesis`

**Answer:** Stable task/resource identities, cancellation acknowledgement, zero owned active tasks and open resources after grace, plus matched acquisition/release

**Explanation:** The cited self-check in L03 tests whether the learner can connect Bounded Fan-out and Structured Cleanup to the module mechanism without replacing evidence with labels. This explanation is specific to M15-Q009 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M15-Q010

**Type:** `short_answer`  
**Difficulty:** `recall`

**Answer:** No. The executed schedules may not expose the conflict and observations do not create a language-defined ordering

**Explanation:** The cited self-check in L04 tests whether the learner can connect Memory Visibility and Races to the module mechanism without replacing evidence with labels. This explanation is specific to M15-Q010 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M15-Q011

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** No. The counter and list need one coherent protocol and completion boundary

**Explanation:** The cited self-check in L04 tests whether the learner can connect Memory Visibility and Races to the module mechanism without replacing evidence with labels. This explanation is specific to M15-Q011 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M15-Q012

**Type:** `multiple_choice`  
**Difficulty:** `application`

**Choices:**

- Keep Memory Lifetime and Management scoped to its stated evidence and boundary.
- Treat Treating heap allocation as inherently slow while ignoring allocation as complete proof without the lesson boun.
- Choose the familiar tool before checking whether Treating heap allocation as inherently slow while ignoring allocatio.
- Make the documented mistake: Treating heap allocation as inherently slow while ignoring allocat

**Answer:** Keep Memory Lifetime and Management scoped to its stated evidence and boundary.

**Explanation:** The distractors are anchored in the mistake list for L01; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M15-Q012 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M15-Q013

**Type:** `multiple_choice`  
**Difficulty:** `synthesis`

**Choices:**

- Make the documented mistake: Treating low RSS as proof of release; allocators may retain pages
- Keep Memory Lifetime and Management scoped to its stated evidence and boundary.
- Choose the familiar tool before checking whether Treating low RSS as proof of release; allocators may retain pages an.
- Treat Treating low RSS as proof of release; allocators may retain pages and as complete proof without the lesson boun.

**Answer:** Keep Memory Lifetime and Management scoped to its stated evidence and boundary.

**Explanation:** The distractors are anchored in the mistake list for L01; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M15-Q013 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M15-Q014

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Choices:**

- Treat Claiming RAII closes asynchronous child work automatically. The scope as complete proof without the lesson boun.
- Choose the familiar tool before checking whether Claiming RAII closes asynchronous child work automatically. The scop.
- Keep Memory Lifetime and Management scoped to its stated evidence and boundary.
- Make the documented mistake: Claiming RAII closes asynchronous child work automatically. The sc

**Answer:** Keep Memory Lifetime and Management scoped to its stated evidence and boundary.

**Explanation:** The distractors are anchored in the mistake list for L01; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M15-Q014 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M15-Q015

**Type:** `multiple_choice`  
**Difficulty:** `application`

**Choices:**

- Make the documented mistake: Comparing GC pauses without heap size, allocation rate, flags, war
- Treat Comparing GC pauses without heap size, allocation rate, flags, warm-u as complete proof without the lesson boun.
- Choose the familiar tool before checking whether Comparing GC pauses without heap size, allocation rate, flags, warm-.
- Keep Memory Lifetime and Management scoped to its stated evidence and boundary.

**Answer:** Keep Memory Lifetime and Management scoped to its stated evidence and boundary.

**Explanation:** The distractors are anchored in the mistake list for L01; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M15-Q015 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M15-Q016

**Type:** `multiple_choice`  
**Difficulty:** `synthesis`

**Choices:**

- Keep Schedulers, Event Loops, and Tasks scoped to its stated evidence and boundary.
- Make the documented mistake: Calling all Node work single-threaded or all Go/Rust/Java work par
- Choose the familiar tool before checking whether Calling all Node work single-threaded or all Go/Rust/Java work paral.
- Treat Calling all Node work single-threaded or all Go/Rust/Java work parall as complete proof without the lesson boun.

**Answer:** Keep Schedulers, Event Loops, and Tasks scoped to its stated evidence and boundary.

**Explanation:** The distractors are anchored in the mistake list for L02; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M15-Q016 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M15-Q017

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Choices:**

- Treat Measuring CPU utilization without runnable queue, throttling, and per as complete proof without the lesson boun.
- Keep Schedulers, Event Loops, and Tasks scoped to its stated evidence and boundary.
- Choose the familiar tool before checking whether Measuring CPU utilization without runnable queue, throttling, and pe.
- Make the documented mistake: Measuring CPU utilization without runnable queue, throttling, and

**Answer:** Keep Schedulers, Event Loops, and Tasks scoped to its stated evidence and boundary.

**Explanation:** The distractors are anchored in the mistake list for L02; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M15-Q017 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M15-Q018

**Type:** `multiple_choice`  
**Difficulty:** `application`

**Choices:**

- Make the documented mistake: Replacing a small thread pool with unbounded tasks and moving fail
- Treat Replacing a small thread pool with unbounded tasks and moving failure as complete proof without the lesson boun.
- Keep Schedulers, Event Loops, and Tasks scoped to its stated evidence and boundary.
- Choose the familiar tool before checking whether Replacing a small thread pool with unbounded tasks and moving failur.

**Answer:** Keep Schedulers, Event Loops, and Tasks scoped to its stated evidence and boundary.

**Explanation:** The distractors are anchored in the mistake list for L02; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M15-Q018 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M15-Q019

**Type:** `multiple_choice`  
**Difficulty:** `synthesis`

**Choices:**

- Choose the familiar tool before checking whether Assuming async syntax proves non-blocking behavior applies
- Treat Assuming async syntax proves non-blocking behavior as complete proof without the lesson boundary
- Make the documented mistake: Assuming async syntax proves non-blocking behavior
- Keep Schedulers, Event Loops, and Tasks scoped to its stated evidence and boundary.

**Answer:** Keep Schedulers, Event Loops, and Tasks scoped to its stated evidence and boundary.

**Explanation:** The distractors are anchored in the mistake list for L02; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M15-Q019 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M15-Q020

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Original concurrency = 180 x 0.060 = 10.80 operations. Revised rate = 180 x 1.25 = 225.0/s, so revised concurrency = 225.0 x 0.060 = 13.50 operations.

**Explanation:** This perturbs the numeric practice around Memory Lifetime and Management: keep the same boundary, align milliseconds to seconds, then apply rate times scoped work. This explanation is specific to M15-Q020 and its cited source.

**Grading notes:** Full credit requires both concurrency values, unit conversion from ms to seconds, and a statement that the boundary stayed unchanged.

## M15-Q021

**Type:** `calculation`  
**Difficulty:** `recall`

**Answer:** Original concurrency = 190 x 0.070 = 13.30 operations. Revised rate = 190 x 1.30 = 247.0/s, so revised concurrency = 247.0 x 0.070 = 17.29 operations.

**Explanation:** This perturbs the numeric practice around Schedulers, Event Loops, and Tasks: keep the same boundary, align milliseconds to seconds, then apply rate times scoped work. This explanation is specific to M15-Q021 and its cited source.

**Grading notes:** Full credit requires both concurrency values, unit conversion from ms to seconds, and a statement that the boundary stayed unchanged.

## M15-Q022

**Type:** `calculation`  
**Difficulty:** `application`

**Answer:** Original concurrency = 200 x 0.080 = 16.00 operations. Revised rate = 200 x 1.35 = 270.0/s, so revised concurrency = 270.0 x 0.080 = 21.60 operations.

**Explanation:** This perturbs the numeric practice around Bounded Fan-out and Structured Cleanup: keep the same boundary, align milliseconds to seconds, then apply rate times scoped work. This explanation is specific to M15-Q022 and its cited source.

**Grading notes:** Full credit requires both concurrency values, unit conversion from ms to seconds, and a statement that the boundary stayed unchanged.

## M15-Q023

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Original concurrency = 120 x 0.040 = 4.80 operations. Revised rate = 120 x 1.40 = 168.0/s, so revised concurrency = 168.0 x 0.040 = 6.72 operations.

**Explanation:** This perturbs the numeric practice around Memory Visibility and Races: keep the same boundary, align milliseconds to seconds, then apply rate times scoped work. This explanation is specific to M15-Q023 and its cited source.

**Grading notes:** Full credit requires both concurrency values, unit conversion from ms to seconds, and a statement that the boundary stayed unchanged.

## M15-Q024

**Type:** `calculation`  
**Difficulty:** `recall`

**Answer:** Original concurrency = 130 x 0.050 = 6.50 operations. Revised rate = 130 x 1.45 = 188.5/s, so revised concurrency = 188.5 x 0.050 = 9.43 operations.

**Explanation:** This perturbs the numeric practice around Types, Serialization, and Validation: keep the same boundary, align milliseconds to seconds, then apply rate times scoped work. This explanation is specific to M15-Q024 and its cited source.

**Grading notes:** Full credit requires both concurrency values, unit conversion from ms to seconds, and a statement that the boundary stayed unchanged.

## M15-Q025

**Type:** `calculation`  
**Difficulty:** `application`

**Answer:** Original concurrency = 140 x 0.060 = 8.40 operations. Revised rate = 140 x 1.10 = 154.0/s, so revised concurrency = 154.0 x 0.060 = 9.24 operations.

**Explanation:** This perturbs the numeric practice around Equivalent-work Runtime Measurement: keep the same boundary, align milliseconds to seconds, then apply rate times scoped work. This explanation is specific to M15-Q025 and its cited source.

**Grading notes:** Full credit requires both concurrency values, unit conversion from ms to seconds, and a statement that the boundary stayed unchanged.

## M15-Q026

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Original concurrency = 150 x 0.070 = 10.50 operations. Revised rate = 150 x 1.15 = 172.5/s, so revised concurrency = 172.5 x 0.070 = 12.07 operations.

**Explanation:** This perturbs the numeric practice around Northstar Polyglot Fan-out Tutorial: keep the same boundary, align milliseconds to seconds, then apply rate times scoped work. This explanation is specific to M15-Q026 and its cited source.

**Grading notes:** Full credit requires both concurrency values, unit conversion from ms to seconds, and a statement that the boundary stayed unchanged.

## M15-Q027

**Type:** `calculation`  
**Difficulty:** `recall`

**Answer:** Original concurrency = 160 x 0.080 = 12.80 operations. Revised rate = 160 x 1.20 = 192.0/s, so revised concurrency = 192.0 x 0.080 = 15.36 operations.

**Explanation:** This perturbs the numeric practice around Runtime Decision and Teach-back: keep the same boundary, align milliseconds to seconds, then apply rate times scoped work. This explanation is specific to M15-Q027 and its cited source.

**Grading notes:** Full credit requires both concurrency values, unit conversion from ms to seconds, and a statement that the boundary stayed unchanged.

## M15-Q028

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** The fixture tests f01-event-loop-block-broken (broken), with I03 as the expected target. The strongest discriminator is the field that changes the mechanism under test, such as scenario_id=f01-event-loop-block-broken, rather than the general presence of a lab run.

**Explanation:** The cited fixture is machine-readable source material for M15; diagnosis should start from the emitted fields and connect them to Bounded Fan-out and Structured Cleanup. This explanation is specific to M15-Q028 and its cited source.

**Grading notes:** Full credit requires naming the mechanism or failure mode and citing one concrete field from the fixture. Partial credit is appropriate for a plausible mechanism without a discriminator.

## M15-Q029

**Type:** `scenario_diagnosis`  
**Difficulty:** `synthesis`

**Answer:** The fixture tests f01-event-loop-block-repaired (repaired), with I03 as the expected target. The strongest discriminator is the field that changes the mechanism under test, such as scenario_id=f01-event-loop-block-repaired, rather than the general presence of a lab run.

**Explanation:** The cited fixture is machine-readable source material for M15; diagnosis should start from the emitted fields and connect them to Memory Visibility and Races. This explanation is specific to M15-Q029 and its cited source.

**Grading notes:** Full credit requires naming the mechanism or failure mode and citing one concrete field from the fixture. Partial credit is appropriate for a plausible mechanism without a discriminator.

## M15-Q030

**Type:** `scenario_diagnosis`  
**Difficulty:** `recall`

**Answer:** The fixture tests f02-worker-exhaustion-broken (broken), with I02 as the expected target. The strongest discriminator is the field that changes the mechanism under test, such as scenario_id=f02-worker-exhaustion-broken, rather than the general presence of a lab run.

**Explanation:** The cited fixture is machine-readable source material for M15; diagnosis should start from the emitted fields and connect them to Types, Serialization, and Validation. This explanation is specific to M15-Q030 and its cited source.

**Grading notes:** Full credit requires naming the mechanism or failure mode and citing one concrete field from the fixture. Partial credit is appropriate for a plausible mechanism without a discriminator.

## M15-Q031

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** The fixture tests f02-worker-exhaustion-repaired (repaired), with I02 as the expected target. The strongest discriminator is the field that changes the mechanism under test, such as scenario_id=f02-worker-exhaustion-repaired, rather than the general presence of a lab run.

**Explanation:** The cited fixture is machine-readable source material for M15; diagnosis should start from the emitted fields and connect them to Equivalent-work Runtime Measurement. This explanation is specific to M15-Q031 and its cited source.

**Grading notes:** Full credit requires naming the mechanism or failure mode and citing one concrete field from the fixture. Partial credit is appropriate for a plausible mechanism without a discriminator.

## M15-Q032

**Type:** `scenario_diagnosis`  
**Difficulty:** `synthesis`

**Answer:** The fixture tests f03-task-leak-broken (broken), with I04 as the expected target. The strongest discriminator is the field that changes the mechanism under test, such as scenario_id=f03-task-leak-broken, rather than the general presence of a lab run.

**Explanation:** The cited fixture is machine-readable source material for M15; diagnosis should start from the emitted fields and connect them to Northstar Polyglot Fan-out Tutorial. This explanation is specific to M15-Q032 and its cited source.

**Grading notes:** Full credit requires naming the mechanism or failure mode and citing one concrete field from the fixture. Partial credit is appropriate for a plausible mechanism without a discriminator.

## M15-Q033

**Type:** `scenario_diagnosis`  
**Difficulty:** `recall`

**Answer:** The fixture tests f03-task-leak-repaired (repaired), with I04 as the expected target. The strongest discriminator is the field that changes the mechanism under test, such as scenario_id=f03-task-leak-repaired, rather than the general presence of a lab run.

**Explanation:** The cited fixture is machine-readable source material for M15; diagnosis should start from the emitted fields and connect them to Runtime Decision and Teach-back. This explanation is specific to M15-Q033 and its cited source.

**Grading notes:** Full credit requires naming the mechanism or failure mode and citing one concrete field from the fixture. Partial credit is appropriate for a plausible mechanism without a discriminator.

## M15-Q034

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Recommend the option that preserves the Memory Visibility and Races mechanism under the exercise constraints: Trace one request's descriptors, buffers, responses, aggregate, tasks, and files. For each record placement, owner, aliases, release trigger, and leak evidence. The decision should be reversed if a repeated measurement or review shows the named constraint is false, the safer alternative meets the same outcome at lower operational cost, or the protected invariant is no longer owned by this boundary.

**Explanation:** The exercise asks for a defensible decision, not a preference. The answer must keep evidence and reversal conditions visible so the learner can change course when facts change. This explanation is specific to M15-Q034 and its cited source.

**Grading notes:** Full credit requires a clear recommendation, cited exercise evidence, and a falsifiable reversal condition. Half credit for a reasonable recommendation with no reversal condition.

## M15-Q035

**Type:** `design_judgment`  
**Difficulty:** `recall`

**Answer:** Recommend the option that preserves the Types, Serialization, and Validation mechanism under the exercise constraints: Four children return 256 KiB each. Decode makes one equal-size copy and assembly makes a 128 KiB summary. Calculate minimum request-attributable bytes before runtime overhead The decision should be reversed if a repeated measurement or review shows the named constraint is false, the safer alternative meets the same outcome at lower operational cost, or the protected invariant is no longer owned by this boundary.

**Explanation:** The exercise asks for a defensible decision, not a preference. The answer must keep evidence and reversal conditions visible so the learner can change course when facts change. This explanation is specific to M15-Q035 and its cited source.

**Grading notes:** Full credit requires a clear recommendation, cited exercise evidence, and a falsifiable reversal condition. Half credit for a reasonable recommendation with no reversal condition.

## M15-Q036

**Type:** `design_judgment`  
**Difficulty:** `application`

**Answer:** Recommend the option that preserves the Equivalent-work Runtime Measurement mechanism under the exercise constraints: Map accept, JSON decode, DNS, socket wait, 20 ms hash, logging, and assembly to event loop/runtime task/worker/OS thread for each runtime. Name every queue. The decision should be reversed if a repeated measurement or review shows the named constraint is false, the safer alternative meets the same outcome at lower operational cost, or the protected invariant is no longer owned by this boundary.

**Explanation:** The exercise asks for a defensible decision, not a preference. The answer must keep evidence and reversal conditions visible so the learner can change course when facts change. This explanation is specific to M15-Q036 and its cited source.

**Grading notes:** Full credit requires a clear recommendation, cited exercise evidence, and a falsifiable reversal condition. Half credit for a reasonable recommendation with no reversal condition.

## M15-Q037

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Recommend the option that preserves the Northstar Polyglot Fan-out Tutorial mechanism under the exercise constraints: Given 8 CPU cores, dependency capacity 64, fan-out 4, and 16 MiB per active request, propose request/child bounds under a 512 MiB service budget. The decision should be reversed if a repeated measurement or review shows the named constraint is false, the safer alternative meets the same outcome at lower operational cost, or the protected invariant is no longer owned by this boundary.

**Explanation:** The exercise asks for a defensible decision, not a preference. The answer must keep evidence and reversal conditions visible so the learner can change course when facts change. This explanation is specific to M15-Q037 and its cited source.

**Grading notes:** Full credit requires a clear recommendation, cited exercise evidence, and a falsifiable reversal condition. Half credit for a reasonable recommendation with no reversal condition.

## M15-Q038

**Type:** `design_judgment`  
**Difficulty:** `recall`

**Answer:** Recommend the option that preserves the Runtime Decision and Teach-back mechanism under the exercise constraints: Validate IDs, deadline, limit, children, required flags, payload, fault mode, unknown fields, and cross-field rules before admission. The decision should be reversed if a repeated measurement or review shows the named constraint is false, the safer alternative meets the same outcome at lower operational cost, or the protected invariant is no longer owned by this boundary.

**Explanation:** The exercise asks for a defensible decision, not a preference. The answer must keep evidence and reversal conditions visible so the learner can change course when facts change. This explanation is specific to M15-Q038 and its cited source.

**Grading notes:** Full credit requires a clear recommendation, cited exercise evidence, and a falsifiable reversal condition. Half credit for a reasonable recommendation with no reversal condition.
