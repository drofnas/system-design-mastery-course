# M02 Quiz Answer Key

This key covers all 41 questions for **Capacity, Queues, and Tail Latency**. Use it after an attempt, or provide it with the LLM grading prompt for feedback.

## M02-Q001

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** Concurrency depends on rate and time in the boundary; a daily total provides neither short-window rate nor service time.

**Explanation:** M02-Q001 uses self-check 1 from Workload and Useful Work; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M02-Q002

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** No. It may recover one logical operation, but it remains another attempt for the same identity.

**Explanation:** M02-Q002 uses self-check 2 from Workload and Useful Work; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M02-Q003

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** Key or tenant skew, including the rate and concentration window.

**Explanation:** M02-Q003 uses self-check 3 from Workload and Useful Work; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M02-Q004

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** Recovery often overlaps new demand. Ignoring it produces a design that can serve normally but cannot catch up.

**Explanation:** M02-Q004 uses self-check 4 from Workload and Useful Work; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M02-Q005

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** Only when attempted work enters the chosen boundary; cheap pre-admission rejection belongs outside it.

**Explanation:** M02-Q005 uses self-check 1 from Little’s Law and Saturation; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M02-Q006

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** No. The identity assumes suitable long-run averages; queue trend and completion evidence establish stability.

**Explanation:** M02-Q006 uses self-check 2 from Little’s Law and Saturation; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M02-Q007

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** It leaves no room for variance, bursts, interruptions, recovery, or model error.

**Explanation:** M02-Q007 uses self-check 3 from Little’s Law and Saturation; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M02-Q008

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** Downstream concurrency reaches its bound and rejection or waiting appears while service workers remain below their own bound.

**Explanation:** M02-Q008 uses self-check 4 from Little’s Law and Saturation; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M02-Q009

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** The missing observations were never collected; sorting the remaining values cannot reconstruct their experience without an explicit correction model.

**Explanation:** M02-Q009 uses self-check 1 from Latency Measurement; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M02-Q010

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** The generator did not deliver the requested schedule, so system-capacity conclusions are confounded.

**Explanation:** M02-Q010 uses self-check 2 from Latency Measurement; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M02-Q011

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** Yes, in the attempted-user population. Record rejection latency and outcome separately rather than mixing it with successful-service latency.

**Explanation:** M02-Q011 uses self-check 3 from Latency Measurement; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M02-Q012

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** Maximum exposes extreme observations and timeout censoring, although it is not stable enough to replace percentiles.

**Explanation:** M02-Q012 uses self-check 4 from Latency Measurement; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M02-Q013

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** It cannot be determined from the branch p99 alone; the full distribution, fan-out, correlation, and response rule matter.

**Explanation:** M02-Q013 uses self-check 1 from Fan-out and Tail Amplification; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M02-Q014

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Measure host count data for review case one; limit the change.
- Measure average whole data for review case one; limit the change.
- Measure mix requests data for review case one; limit the change.
- Measure model only data for review case one; limit the change.

**Answer:** Measure host count data for review case one; limit the change.

**Explanation:** M02-Q014 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects host count as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M02-Q015

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Measure treat projections data for review case two; limit the change.
- Measure average whole data for review case two; limit the change.
- Measure combine different data for review case two; limit the change.
- Measure attempted rate data for review case two; limit the change.

**Answer:** Measure average whole data for review case two; limit the change.

**Explanation:** M02-Q015 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects average whole as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M02-Q016

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Measure call nominal data for review case three; limit the change.
- Measure infer percentiles data for review case three; limit the change.
- Measure mix requests data for review case three; limit the change.
- Measure assume every data for review case three; limit the change.

**Answer:** Measure mix requests data for review case three; limit the change.

**Explanation:** M02-Q016 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects mix requests as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M02-Q017

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Measure report only data for review case four; limit the change.
- Measure drop rejected data for review case four; limit the change.
- Measure wall clock data for review case four; limit the change.
- Measure model only data for review case four; limit the change.

**Answer:** Measure model only data for review case four; limit the change.

**Explanation:** M02-Q017 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects model only as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M02-Q018

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Measure treat projections data for review case five; limit the change.
- Measure ignore generator data for review case five; limit the change.
- Measure compare unmatched data for review case five; limit the change.
- Measure multiply branch data for review case five; limit the change. with margin

**Answer:** Measure treat projections data for review case five; limit the change.

**Explanation:** M02-Q018 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects treat projections as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M02-Q019

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Measure assume independence data for review case six; limit the change.
- Measure combine different data for review case six; limit the change.
- Measure ignore variable data for review case six; limit the change.
- Measure optimize only data for review case six; limit the change.

**Answer:** Measure combine different data for review case six; limit the change.

**Explanation:** M02-Q019 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects combine different as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M02-Q020

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Measure add hedges data for review case seven; limit the change. with margin
- Measure treat queue data for review case seven; limit the change.
- Measure attempted rate data for review case seven; limit the change.
- Measure hide queues data for review case seven; limit the change.

**Answer:** Measure attempted rate data for review case seven; limit the change.

**Explanation:** M02-Q020 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects attempted rate as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M02-Q021

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Measure reject too data for review case eight; limit the change.
- Measure prioritize caller data for review case eight; limit the change.
- Measure never exercise data for review case eight; limit the change.
- Measure call nominal data for review case eight; limit the change.

**Answer:** Measure call nominal data for review case eight; limit the change.

**Explanation:** M02-Q021 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects call nominal as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M02-Q022

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Measure infer percentiles data for review case nine; limit the change.
- Measure retry every data for review case nine; limit the change.
- Measure exponential backoff data for review case nine; limit the change.
- Measure omit logical data for review case nine; limit the change.

**Answer:** Measure infer percentiles data for review case nine; limit the change.

**Explanation:** M02-Q022 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects infer percentiles as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M02-Q023

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Measure protect caller data for review case ten; limit the change.
- Measure assume every data for review case ten; limit the change.
- Measure reserve capacity data for review case ten; limit the change.
- Measure ignore recovery data for review case ten; limit the change.

**Answer:** Measure assume every data for review case ten; limit the change.

**Explanation:** M02-Q023 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects assume every as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M02-Q024

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** Calculation for workload and useful work, attempts are 120 x (1 + 0.25) = 150.0/s; useful throughput is still bounded by the 120/s logical identities.

**Explanation:** M02-Q024 uses retry amplification from Workload and Useful Work and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M02-Q025

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** Calculation for littles law and saturation, m02 Little'S Law case 2: L = 124/s x 0.080 s = 9.92 requests inside the boundary.

**Explanation:** M02-Q025 uses Little's Law from Little’s Law and Saturation and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M02-Q026

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** Calculation for latency measurement, m02 Fan-Out Tail Probability case 3: At least one slow branch = 1 - (1 - 0.020)^4 = 0.0776, or 7.76%.

**Explanation:** M02-Q026 uses fan-out tail probability from Latency Measurement and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M02-Q027

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** Calculation for fan-out and tail amplification, drain time is 54,000 / 240/s = 225.0 seconds before overhead or new arrivals.

**Explanation:** M02-Q027 uses queue drain bound from Fan-out and Tail Amplification and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M02-Q028

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** Calculation for bounded overload control, the multiplier is 3^4 = 81 attempts at the deepest dependency for one original request.

**Explanation:** M02-Q028 uses layered retry attempts from Bounded Overload Control and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M02-Q029

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** Calculation for retries and downstream protection, failover-adjusted capacity is 315.6 x 0.75 = 236.7/s, so steady state must stay at or below about 236.7/s.

**Explanation:** M02-Q029 uses failover headroom from Retries and Downstream Protection and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M02-Q030

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** Calculation for failover headroom and unit cost, net drain is (240 - 150) / 1.25 = 72.0/s, so drain time is 54,000 / 72.0 = 750.0 seconds.

**Explanation:** M02-Q030 uses backlog drain from Failover Headroom and Unit Cost and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M02-Q031

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** Diagnosis for workload and useful work, arrival.rate_per_second and arrival.max_in_flight separate the mechanism. arrival.rate_per_second = 100 while arrival.max_in_flight = 1, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare arrival.rate_per_second with arrival.max_in_flight and connect that contrast to workload and useful work.

**Grading notes:** Full credit names Workload and Useful Work, cites arrival.rate_per_second and arrival.max_in_flight, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M02-Q032

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** Diagnosis for littles law and saturation, arrival.rate_per_second and service.workers separate the mechanism. arrival.rate_per_second = 100 while service.workers = 1, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare arrival.rate_per_second with service.workers and connect that contrast to littles law and saturation.

**Grading notes:** Full credit names Littles Law and Saturation, cites arrival.rate_per_second and service.workers, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M02-Q033

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** Diagnosis for latency measurement, arrival.rate_per_second and service.queue_capacity separate the mechanism. arrival.rate_per_second = 100 while service.queue_capacity = 4, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare arrival.rate_per_second with service.queue_capacity and connect that contrast to latency measurement.

**Grading notes:** Full credit names Latency Measurement, cites arrival.rate_per_second and service.queue_capacity, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M02-Q034

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** Diagnosis for fan-out and tail amplification, arrival.rate_per_second and service.base_service_ms separate the mechanism. arrival.rate_per_second = 100 while service.base_service_ms = 20, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare arrival.rate_per_second with service.base_service_ms and connect that contrast to fan-out and tail amplification.

**Grading notes:** Full credit names Fan-out and Tail Amplification, cites arrival.rate_per_second and service.base_service_ms, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M02-Q035

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** Diagnosis for bounded overload control, arrival.duration_seconds and arrival.max_in_flight separate the mechanism. arrival.duration_seconds = 0.4 while arrival.max_in_flight = 4, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare arrival.duration_seconds with arrival.max_in_flight and connect that contrast to bounded overload control.

**Grading notes:** Full credit names Bounded Overload Control, cites arrival.duration_seconds and arrival.max_in_flight, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M02-Q036

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** Diagnosis for retries and downstream protection, arrival.duration_seconds and service.workers separate the mechanism. arrival.duration_seconds = 0.3 while service.workers = 1, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare arrival.duration_seconds with service.workers and connect that contrast to retries and downstream protection.

**Grading notes:** Full credit names Retries and Downstream Protection, cites arrival.duration_seconds and service.workers, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M02-Q037

**Type:** `design_judgment`
**Difficulty:** `application`

**Answer:** Approve Define useful work at 121.9/s. The deciding number is 186 x 0.72 = 133.9/s, leaving 12/s before the reserve is consumed. Withdraw approval if a drill, trace, or workload sample shows define useful work demand above 133.9/s or proves the shed point cannot protect lower-priority work.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to define useful work demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 133.9/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M02-Q038

**Type:** `design_judgment`
**Difficulty:** `synthesis`

**Answer:** Decline Shape and sensitivity at 157.6/s. The deciding number is 203 x 0.72 = 146.2/s, so planned demand exceeds the usable region by 11.4/s. Approve later if repeated measurements lift usable capacity above 157.6/s or a named policy removes at least 11.4/s of deferrable work before saturation.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to shape and sensitivity demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 146.2/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M02-Q039

**Type:** `design_judgment`
**Difficulty:** `recall`

**Answer:** Approve conditionally for Apply Little’s Law. The deciding number is 220 x 0.72 = 158.4/s, and 153.4/s fits only while the fallback remains enforceable. Keep the condition until recovery traffic, priority demand, or fallback tests show less than 5/s of usable margin.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to apply little’s law demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 158.4/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M02-Q040

**Type:** `design_judgment`
**Difficulty:** `application`

**Answer:** Approve Expose coordinated omission at 153.5/s. The deciding number is 237 x 0.72 = 170.6/s, leaving 17.1/s before the reserve is consumed. Require redesign if a drill, trace, or workload sample shows expose coordinated omission demand above 170.6/s or proves the shed point cannot protect lower-priority work.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to expose coordinated omission demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 170.6/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M02-Q041

**Type:** `design_judgment`
**Difficulty:** `synthesis`

**Answer:** Decline Design a valid trial at 198.5/s. The deciding number is 254 x 0.72 = 182.9/s, so planned demand exceeds the usable region by 15.6/s. Lift the decline if repeated measurements lift usable capacity above 198.5/s or a named policy removes at least 15.6/s of deferrable work before saturation.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to design a valid trial demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 182.9/s, compares it with planned demand, and names a scenario-specific reversal condition.
