# M02 Quiz Answer Key

This key covers all 20 questions for **Capacity, Queues, and Tail Latency**. Use it after an attempt, or provide it with the LLM grading prompt for feedback.

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

## M02-Q024

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** Attempts are 120 x (1 + 0.25) = 150.0/s; useful throughput is still bounded by the 120/s logical identities.

**Explanation:** M02-Q024 uses retry amplification from Workload and Useful Work and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M02-Q025

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** L = 124/s x 0.080 s = 9.92 requests inside the boundary.

**Explanation:** M02-Q025 uses Little's Law from Little’s Law and Saturation and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M02-Q026

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** At least one slow branch = 1 - (1 - 0.020)^4 = 0.0776, or 7.76%.

**Explanation:** M02-Q026 uses fan-out tail probability from Latency Measurement and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M02-Q027

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** Drain time is 54,000 / 240/s = 225.0 seconds before overhead or new arrivals.

**Explanation:** M02-Q027 uses queue drain bound from Fan-out and Tail Amplification and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M02-Q028

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** The multiplier is 3^4 = 81 attempts at the deepest dependency for one original request.

**Explanation:** M02-Q028 uses layered retry attempts from Bounded Overload Control and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M02-Q029

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** Failover-adjusted capacity is 315.6 x 0.75 = 236.7/s, so steady state must stay at or below about 236.7/s.

**Explanation:** M02-Q029 uses failover headroom from Retries and Downstream Protection and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M02-Q030

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** Net drain is (240 - 150) / 1.25 = 72.0/s, so drain time is 54,000 / 72.0 = 750.0 seconds.

**Explanation:** M02-Q030 uses backlog drain from Failover Headroom and Unit Cost and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.
