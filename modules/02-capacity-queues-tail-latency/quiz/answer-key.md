# M02 Quiz Answer Key

This key covers all 41 questions for **Capacity, Queues, and Tail Latency**. Use it after an attempt, or provide it with the LLM grading prompt for feedback.

## M02-Q001

**Type:** `short_answer`  
**Difficulty:** `recall`

**Answer:** Concurrency depends on rate and time in the boundary; a daily total provides neither short-window rate nor service time

**Explanation:** The cited self-check in L01 tests whether the learner can connect Workload and Useful Work to the module mechanism without replacing evidence with labels. This explanation is specific to M02-Q001 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M02-Q002

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** No. It may recover one logical operation, but it remains another attempt for the same identity

**Explanation:** The cited self-check in L01 tests whether the learner can connect Workload and Useful Work to the module mechanism without replacing evidence with labels. This explanation is specific to M02-Q002 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M02-Q003

**Type:** `short_answer`  
**Difficulty:** `synthesis`

**Answer:** Key or tenant skew, including the rate and concentration window

**Explanation:** The cited self-check in L01 tests whether the learner can connect Workload and Useful Work to the module mechanism without replacing evidence with labels. This explanation is specific to M02-Q003 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M02-Q004

**Type:** `short_answer`  
**Difficulty:** `recall`

**Answer:** Recovery often overlaps new demand. Ignoring it produces a design that can serve normally but cannot catch up

**Explanation:** The cited self-check in L01 tests whether the learner can connect Workload and Useful Work to the module mechanism without replacing evidence with labels. This explanation is specific to M02-Q004 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M02-Q005

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** Only when attempted work enters the chosen boundary; cheap pre-admission rejection belongs outside it

**Explanation:** The cited self-check in L02 tests whether the learner can connect Little’s Law and Saturation to the module mechanism without replacing evidence with labels. This explanation is specific to M02-Q005 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M02-Q006

**Type:** `short_answer`  
**Difficulty:** `synthesis`

**Answer:** No. The identity assumes suitable long-run averages; queue trend and completion evidence establish stability

**Explanation:** The cited self-check in L02 tests whether the learner can connect Little’s Law and Saturation to the module mechanism without replacing evidence with labels. This explanation is specific to M02-Q006 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M02-Q007

**Type:** `short_answer`  
**Difficulty:** `recall`

**Answer:** It leaves no room for variance, bursts, interruptions, recovery, or model error

**Explanation:** The cited self-check in L02 tests whether the learner can connect Little’s Law and Saturation to the module mechanism without replacing evidence with labels. This explanation is specific to M02-Q007 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M02-Q008

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** Downstream concurrency reaches its bound and rejection or waiting appears while service workers remain below their own bound. For the practice: in-system L = 120 × 0.08 = 9.6; in-service demand is 120 × 0.05 = 6, so six workers are modeled at 100%

**Explanation:** The cited self-check in L02 tests whether the learner can connect Little’s Law and Saturation to the module mechanism without replacing evidence with labels. This explanation is specific to M02-Q008 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M02-Q009

**Type:** `short_answer`  
**Difficulty:** `synthesis`

**Answer:** The missing observations were never collected; sorting the remaining values cannot reconstruct their experience without an explicit correction model

**Explanation:** The cited self-check in L03 tests whether the learner can connect Latency Measurement to the module mechanism without replacing evidence with labels. This explanation is specific to M02-Q009 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M02-Q010

**Type:** `short_answer`  
**Difficulty:** `recall`

**Answer:** The generator did not deliver the requested schedule, so system-capacity conclusions are confounded

**Explanation:** The cited self-check in L03 tests whether the learner can connect Latency Measurement to the module mechanism without replacing evidence with labels. This explanation is specific to M02-Q010 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M02-Q011

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** Yes, in the attempted-user population. Record rejection latency and outcome separately rather than mixing it with successful-service latency

**Explanation:** The cited self-check in L03 tests whether the learner can connect Latency Measurement to the module mechanism without replacing evidence with labels. This explanation is specific to M02-Q011 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M02-Q012

**Type:** `short_answer`  
**Difficulty:** `synthesis`

**Answer:** Maximum exposes extreme observations and timeout censoring, although it is not stable enough to replace percentiles

**Explanation:** The cited self-check in L03 tests whether the learner can connect Latency Measurement to the module mechanism without replacing evidence with labels. This explanation is specific to M02-Q012 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M02-Q013

**Type:** `short_answer`  
**Difficulty:** `recall`

**Answer:** It cannot be determined from the branch p99 alone; the full distribution, fan-out, correlation, and response rule matter

**Explanation:** The cited self-check in L04 tests whether the learner can connect Fan-out and Tail Amplification to the module mechanism without replacing evidence with labels. This explanation is specific to M02-Q013 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M02-Q014

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** Averages hide long journeys or hot keys that create disproportionate branch work

**Explanation:** The cited self-check in L04 tests whether the learner can connect Fan-out and Tail Amplification to the module mechanism without replacing evidence with labels. This explanation is specific to M02-Q014 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M02-Q015

**Type:** `multiple_choice`  
**Difficulty:** `application`

**Choices:**

- Keep Workload and Useful Work scoped to its stated evidence and boundary.
- Make the documented mistake: Start from host count: host count is supply, not demand
- Treat Start from host count: host count is supply, not demand as complete proof without the lesson boundary
- Choose the familiar tool before checking whether Start from host count: host count is supply, not demand applies

**Answer:** Keep Workload and Useful Work scoped to its stated evidence and boundary.

**Explanation:** The distractors are anchored in the mistake list for L01; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M02-Q015 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M02-Q016

**Type:** `multiple_choice`  
**Difficulty:** `synthesis`

**Choices:**

- Choose the familiar tool before checking whether Average a whole day: it erases burst duration and recovery debt appl.
- Keep Workload and Useful Work scoped to its stated evidence and boundary.
- Treat Average a whole day: it erases burst duration and recovery debt as complete proof without the lesson boundary
- Make the documented mistake: Average a whole day: it erases burst duration and recovery debt

**Answer:** Keep Workload and Useful Work scoped to its stated evidence and boundary.

**Explanation:** The distractors are anchored in the mistake list for L01; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M02-Q016 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M02-Q017

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Choices:**

- Choose the familiar tool before checking whether Mix requests and attempts: retries appear as successful scaling appl.
- Treat Mix requests and attempts: retries appear as successful scaling as complete proof without the lesson boundary
- Keep Workload and Useful Work scoped to its stated evidence and boundary.
- Make the documented mistake: Mix requests and attempts: retries appear as successful scaling

**Answer:** Keep Workload and Useful Work scoped to its stated evidence and boundary.

**Explanation:** The distractors are anchored in the mistake list for L01; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M02-Q017 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M02-Q018

**Type:** `multiple_choice`  
**Difficulty:** `application`

**Choices:**

- Choose the familiar tool before checking whether Model only foreground work: reconciliation and backlog drain consume.
- Make the documented mistake: Model only foreground work: reconciliation and backlog drain consu
- Treat Model only foreground work: reconciliation and backlog drain consume as complete proof without the lesson bound.
- Keep Workload and Useful Work scoped to its stated evidence and boundary.

**Answer:** Keep Workload and Useful Work scoped to its stated evidence and boundary.

**Explanation:** The distractors are anchored in the mistake list for L01; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M02-Q018 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M02-Q019

**Type:** `multiple_choice`  
**Difficulty:** `synthesis`

**Choices:**

- Keep Workload and Useful Work scoped to its stated evidence and boundary.
- Choose the familiar tool before checking whether Treat projections as measurements: false precision hides the sensiti.
- Treat Treat projections as measurements: false precision hides the sensitiv as complete proof without the lesson boun.
- Make the documented mistake: Treat projections as measurements: false precision hides the sensi

**Answer:** Keep Workload and Useful Work scoped to its stated evidence and boundary.

**Explanation:** The distractors are anchored in the mistake list for L01; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M02-Q019 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M02-Q020

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Choices:**

- Choose the familiar tool before checking whether Combine different boundaries: server concurrency with client end-to-.
- Keep Little’s Law and Saturation scoped to its stated evidence and boundary.
- Treat Combine different boundaries: server concurrency with client end-to-e as complete proof without the lesson boun.
- Make the documented mistake: Combine different boundaries: server concurrency with client end-t

**Answer:** Keep Little’s Law and Saturation scoped to its stated evidence and boundary.

**Explanation:** The distractors are anchored in the mistake list for L02; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M02-Q020 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M02-Q021

**Type:** `multiple_choice`  
**Difficulty:** `application`

**Choices:**

- Choose the familiar tool before checking whether Use attempted rate after rejection: rejected work did not occupy the.
- Treat Use attempted rate after rejection: rejected work did not occupy the as complete proof without the lesson bound.
- Keep Little’s Law and Saturation scoped to its stated evidence and boundary.
- Make the documented mistake: Use attempted rate after rejection: rejected work did not occupy t

**Answer:** Keep Little’s Law and Saturation scoped to its stated evidence and boundary.

**Explanation:** The distractors are anchored in the mistake list for L02; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M02-Q021 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M02-Q022

**Type:** `multiple_choice`  
**Difficulty:** `synthesis`

**Choices:**

- Choose the familiar tool before checking whether Call the nominal limit safe capacity: the calculation has no varianc.
- Treat Call the nominal limit safe capacity: the calculation has no variance, as complete proof without the lesson bou.
- Make the documented mistake: Call the nominal limit safe capacity: the calculation has no varia
- Keep Little’s Law and Saturation scoped to its stated evidence and boundary.

**Answer:** Keep Little’s Law and Saturation scoped to its stated evidence and boundary.

**Explanation:** The distractors are anchored in the mistake list for L02; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M02-Q022 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M02-Q023

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Choices:**

- Keep Little’s Law and Saturation scoped to its stated evidence and boundary.
- Treat Infer percentiles from a mean: Little’s Law relates long-run averages as complete proof without the lesson boun.
- Make the documented mistake: Infer percentiles from a mean: Little’s Law relates long-run avera
- Choose the familiar tool before checking whether Infer percentiles from a mean: Little’s Law relates long-run average.

**Answer:** Keep Little’s Law and Saturation scoped to its stated evidence and boundary.

**Explanation:** The distractors are anchored in the mistake list for L02; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M02-Q023 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M02-Q024

**Type:** `multiple_choice`  
**Difficulty:** `application`

**Choices:**

- Choose the familiar tool before checking whether Assume every worker is interchangeable: shared downstreams can bind.
- Keep Little’s Law and Saturation scoped to its stated evidence and boundary.
- Treat Assume every worker is interchangeable: shared downstreams can bind f as complete proof without the lesson boun.
- Make the documented mistake: Assume every worker is interchangeable: shared downstreams can bin

**Answer:** Keep Little’s Law and Saturation scoped to its stated evidence and boundary.

**Explanation:** The distractors are anchored in the mistake list for L02; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M02-Q024 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M02-Q025

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Original concurrency = 140 x 0.045 = 6.30 operations. Revised rate = 140 x 1.25 = 175.0/s, so revised concurrency = 175.0 x 0.045 = 7.88 operations.

**Explanation:** This perturbs the numeric practice around Workload and Useful Work: keep the same boundary, align milliseconds to seconds, then apply rate times scoped work. This explanation is specific to M02-Q025 and its cited source.

**Grading notes:** Full credit requires both concurrency values, unit conversion from ms to seconds, and a statement that the boundary stayed unchanged.

## M02-Q026

**Type:** `calculation`  
**Difficulty:** `recall`

**Answer:** Original concurrency = 150 x 0.055 = 8.25 operations. Revised rate = 150 x 1.30 = 195.0/s, so revised concurrency = 195.0 x 0.055 = 10.72 operations.

**Explanation:** This perturbs the numeric practice around Little’s Law and Saturation: keep the same boundary, align milliseconds to seconds, then apply rate times scoped work. This explanation is specific to M02-Q026 and its cited source.

**Grading notes:** Full credit requires both concurrency values, unit conversion from ms to seconds, and a statement that the boundary stayed unchanged.

## M02-Q027

**Type:** `calculation`  
**Difficulty:** `application`

**Answer:** Original concurrency = 160 x 0.065 = 10.40 operations. Revised rate = 160 x 1.35 = 216.0/s, so revised concurrency = 216.0 x 0.065 = 14.04 operations.

**Explanation:** This perturbs the numeric practice around Latency Measurement: keep the same boundary, align milliseconds to seconds, then apply rate times scoped work. This explanation is specific to M02-Q027 and its cited source.

**Grading notes:** Full credit requires both concurrency values, unit conversion from ms to seconds, and a statement that the boundary stayed unchanged.

## M02-Q028

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Original concurrency = 170 x 0.075 = 12.75 operations. Revised rate = 170 x 1.40 = 238.0/s, so revised concurrency = 238.0 x 0.075 = 17.85 operations.

**Explanation:** This perturbs the numeric practice around Fan-out and Tail Amplification: keep the same boundary, align milliseconds to seconds, then apply rate times scoped work. This explanation is specific to M02-Q028 and its cited source.

**Grading notes:** Full credit requires both concurrency values, unit conversion from ms to seconds, and a statement that the boundary stayed unchanged.

## M02-Q029

**Type:** `calculation`  
**Difficulty:** `recall`

**Answer:** Original concurrency = 180 x 0.035 = 6.30 operations. Revised rate = 180 x 1.45 = 261.0/s, so revised concurrency = 261.0 x 0.035 = 9.13 operations.

**Explanation:** This perturbs the numeric practice around Bounded Overload Control: keep the same boundary, align milliseconds to seconds, then apply rate times scoped work. This explanation is specific to M02-Q029 and its cited source.

**Grading notes:** Full credit requires both concurrency values, unit conversion from ms to seconds, and a statement that the boundary stayed unchanged.

## M02-Q030

**Type:** `calculation`  
**Difficulty:** `application`

**Answer:** Original concurrency = 190 x 0.045 = 8.55 operations. Revised rate = 190 x 1.10 = 209.0/s, so revised concurrency = 209.0 x 0.045 = 9.41 operations.

**Explanation:** This perturbs the numeric practice around Retries and Downstream Protection: keep the same boundary, align milliseconds to seconds, then apply rate times scoped work. This explanation is specific to M02-Q030 and its cited source.

**Grading notes:** Full credit requires both concurrency values, unit conversion from ms to seconds, and a statement that the boundary stayed unchanged.

## M02-Q031

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** The fixture tests fixture-closed-loop-stall (closed), with closed as the expected target. The strongest discriminator is the field that changes the mechanism under test, such as id=fixture-closed-loop-stall, rather than the general presence of a lab run.

**Explanation:** The cited fixture is machine-readable source material for M02; diagnosis should start from the emitted fields and connect them to Latency Measurement. This explanation is specific to M02-Q031 and its cited source.

**Grading notes:** Full credit requires naming the mechanism or failure mode and citing one concrete field from the fixture. Partial credit is appropriate for a plausible mechanism without a discriminator.

## M02-Q032

**Type:** `scenario_diagnosis`  
**Difficulty:** `synthesis`

**Answer:** The fixture tests fixture-failover-loss (open), with open as the expected target. The strongest discriminator is the field that changes the mechanism under test, such as id=fixture-failover-loss, rather than the general presence of a lab run.

**Explanation:** The cited fixture is machine-readable source material for M02; diagnosis should start from the emitted fields and connect them to Fan-out and Tail Amplification. This explanation is specific to M02-Q032 and its cited source.

**Grading notes:** Full credit requires naming the mechanism or failure mode and citing one concrete field from the fixture. Partial credit is appropriate for a plausible mechanism without a discriminator.

## M02-Q033

**Type:** `scenario_diagnosis`  
**Difficulty:** `recall`

**Answer:** The fixture tests fixture-failover-normal (open), with open as the expected target. The strongest discriminator is the field that changes the mechanism under test, such as id=fixture-failover-normal, rather than the general presence of a lab run.

**Explanation:** The cited fixture is machine-readable source material for M02; diagnosis should start from the emitted fields and connect them to Bounded Overload Control. This explanation is specific to M02-Q033 and its cited source.

**Grading notes:** Full credit requires naming the mechanism or failure mode and citing one concrete field from the fixture. Partial credit is appropriate for a plausible mechanism without a discriminator.

## M02-Q034

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** The fixture tests fixture-open-loop-stall (open), with open as the expected target. The strongest discriminator is the field that changes the mechanism under test, such as id=fixture-open-loop-stall, rather than the general presence of a lab run.

**Explanation:** The cited fixture is machine-readable source material for M02; diagnosis should start from the emitted fields and connect them to Retries and Downstream Protection. This explanation is specific to M02-Q034 and its cited source.

**Grading notes:** Full credit requires naming the mechanism or failure mode and citing one concrete field from the fixture. Partial credit is appropriate for a plausible mechanism without a discriminator.

## M02-Q035

**Type:** `scenario_diagnosis`  
**Difficulty:** `synthesis`

**Answer:** The fixture tests fixture-retry-amplification (open), with open as the expected target. The strongest discriminator is the field that changes the mechanism under test, such as id=fixture-retry-amplification, rather than the general presence of a lab run.

**Explanation:** The cited fixture is machine-readable source material for M02; diagnosis should start from the emitted fields and connect them to Failover Headroom and Unit Cost. This explanation is specific to M02-Q035 and its cited source.

**Grading notes:** Full credit requires naming the mechanism or failure mode and citing one concrete field from the fixture. Partial credit is appropriate for a plausible mechanism without a discriminator.

## M02-Q036

**Type:** `scenario_diagnosis`  
**Difficulty:** `recall`

**Answer:** The fixture tests fixture-saturation (open), with open as the expected target. The strongest discriminator is the field that changes the mechanism under test, such as id=fixture-saturation, rather than the general presence of a lab run.

**Explanation:** The cited fixture is machine-readable source material for M02; diagnosis should start from the emitted fields and connect them to Capacity Decisions and Defense. This explanation is specific to M02-Q036 and its cited source.

**Grading notes:** Full credit requires naming the mechanism or failure mode and citing one concrete field from the fixture. Partial credit is appropriate for a plausible mechanism without a discriminator.

## M02-Q037

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Recommend the option that preserves the Fan-out and Tail Amplification mechanism under the exercise constraints: At peak, Transit Signal receives 170 rider lookups/s. Two percent receive one retry. Each lookup has three route legs. 1 The decision should be reversed if a repeated measurement or review shows the named constraint is false, the safer alternative meets the same outcome at lower operational cost, or the protected invariant is no longer owned by this boundary.

**Explanation:** The exercise asks for a defensible decision, not a preference. The answer must keep evidence and reversal conditions visible so the learner can change course when facts change. This explanation is specific to M02-Q037 and its cited source.

**Grading notes:** Full credit requires a clear recommendation, cited exercise evidence, and a falsifiable reversal condition. Half credit for a reasonable recommendation with no reversal condition.

## M02-Q038

**Type:** `design_judgment`  
**Difficulty:** `recall`

**Answer:** Recommend the option that preserves the Bounded Overload Control mechanism under the exercise constraints: Compare the five-minute 800/s burst with 800/s sustained for one hour. Calculate logical requests in both periods The decision should be reversed if a repeated measurement or review shows the named constraint is false, the safer alternative meets the same outcome at lower operational cost, or the protected invariant is no longer owned by this boundary.

**Explanation:** The exercise asks for a defensible decision, not a preference. The answer must keep evidence and reversal conditions visible so the learner can change course when facts change. This explanation is specific to M02-Q038 and its cited source.

**Grading notes:** Full credit requires a clear recommendation, cited exercise evidence, and a falsifiable reversal condition. Half credit for a reasonable recommendation with no reversal condition.

## M02-Q039

**Type:** `design_judgment`  
**Difficulty:** `application`

**Answer:** Recommend the option that preserves the Retries and Downstream Protection mechanism under the exercise constraints: At 170 admitted requests/s, mean in-system time is 80 ms and mean service time is 25 ms. 1. Calculate in-system concurrency. 2. Calculate service concurrency. 3 The decision should be reversed if a repeated measurement or review shows the named constraint is false, the safer alternative meets the same outcome at lower operational cost, or the protected invariant is no longer owned by this boundary.

**Explanation:** The exercise asks for a defensible decision, not a preference. The answer must keep evidence and reversal conditions visible so the learner can change course when facts change. This explanation is specific to M02-Q039 and its cited source.

**Grading notes:** Full credit requires a clear recommendation, cited exercise evidence, and a falsifiable reversal condition. Half credit for a reasonable recommendation with no reversal condition.

## M02-Q040

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Recommend the option that preserves the Failover Headroom and Unit Cost mechanism under the exercise constraints: Draw an event timeline for 50 open-loop arrivals/s during a two-second service stall. Compare it with one closed-loop participant The decision should be reversed if a repeated measurement or review shows the named constraint is false, the safer alternative meets the same outcome at lower operational cost, or the protected invariant is no longer owned by this boundary.

**Explanation:** The exercise asks for a defensible decision, not a preference. The answer must keep evidence and reversal conditions visible so the learner can change course when facts change. This explanation is specific to M02-Q040 and its cited source.

**Grading notes:** Full credit requires a clear recommendation, cited exercise evidence, and a falsifiable reversal condition. Half credit for a reasonable recommendation with no reversal condition.

## M02-Q041

**Type:** `design_judgment`  
**Difficulty:** `recall`

**Answer:** Recommend the option that preserves the Capacity Decisions and Defense mechanism under the exercise constraints: Write a trial contract for the Transit baseline: population, boundary, workload, warm-up, duration, repetitions, outcomes, percentiles, rejection treatment, clock, generator check,. The decision should be reversed if a repeated measurement or review shows the named constraint is false, the safer alternative meets the same outcome at lower operational cost, or the protected invariant is no longer owned by this boundary.

**Explanation:** The exercise asks for a defensible decision, not a preference. The answer must keep evidence and reversal conditions visible so the learner can change course when facts change. This explanation is specific to M02-Q041 and its cited source.

**Grading notes:** Full credit requires a clear recommendation, cited exercise evidence, and a falsifiable reversal condition. Half credit for a reasonable recommendation with no reversal condition.
