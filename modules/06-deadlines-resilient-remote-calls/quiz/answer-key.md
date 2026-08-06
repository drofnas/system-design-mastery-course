# M06 Quiz Answer Key

This key covers all 40 questions for **Deadlines and Resilient Remote Calls**. Use it after an attempt, or provide it with the LLM grading prompt for feedback.

## M06-Q001

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** The absolute deadline preserves elapsed time across hops and prevents nested work from extending the user promise.

**Explanation:** M06-Q001 uses self-check 1 from End-to-End Deadlines and Allocation; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M06-Q002

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** Parallel completion follows the slowest required child, while attempts, slots, CPU, and dependency load still accumulate across all children.

**Explanation:** M06-Q002 uses self-check 2 from End-to-End Deadlines and Allocation; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M06-Q003

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** Reject, degrade, or use an approved fallback before dispatch; record the budget decision rather than starting predictably late work.

**Explanation:** M06-Q003 uses self-check 3 from End-to-End Deadlines and Allocation; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M06-Q004

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** Only that an owner was asked to stop; observation and cleanup need evidence.

**Explanation:** M06-Q004 uses self-check 1 from Cancellation and Useful-Work Boundaries; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M06-Q005

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** Completing an already-started atomic effect plus its durable outcome can preserve correctness better than creating an unknown partial state.

**Explanation:** M06-Q005 uses self-check 2 from Cancellation and Useful-Work Boundaries; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M06-Q006

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** A time series of queued/active children, permits, handles, and effect starts through `t_drained`, correlated to `t_signal`.

**Explanation:** M06-Q006 uses self-check 3 from Cancellation and Useful-Work Boundaries; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M06-Q007

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** No. It changes timing; attempt count needs a separate cap or budget.

**Explanation:** M06-Q007 uses self-check 1 from Retry Classification, Budgets, Backoff, and Jitter; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M06-Q008

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** Singular ownership prevents multiplicative retries and makes cost visible.

**Explanation:** M06-Q008 uses self-check 2 from Retry Classification, Budgets, Backoff, and Jitter; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M06-Q009

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** More dependency work is producing fewer logical outcomes, a possible positive feedback loop rather than a harmless transient symptom.

**Explanation:** M06-Q009 uses self-check 3 from Retry Classification, Budgets, Backoff, and Jitter; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M06-Q010

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** Nothing conclusive; the outcome is ambiguous until authoritative state or a durable idempotency result is consulted.

**Explanation:** M06-Q010 uses self-check 1 from Idempotency and Deduplication; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M06-Q011

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** It prevents one key from silently representing two different intentions.

**Explanation:** M06-Q011 uses self-check 2 from Idempotency and Deduplication; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M06-Q012

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Measure resetting each data for review case one; limit the change.
- Measure parallel budgets data for review case one; limit the change.
- Measure mean latency data for review case one; limit the change.
- Measure giving every data for review case one; limit the change.

**Answer:** Measure resetting each data for review case one; limit the change.

**Explanation:** M06-Q012 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects resetting each as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M06-Q013

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Measure deadline proof data for review case two; limit the change. with margin
- Measure parallel budgets data for review case two; limit the change.
- Measure canceling only data for review case two; limit the change.
- Measure releasing permit data for review case two; limit the change.

**Answer:** Measure parallel budgets data for review case two; limit the change.

**Explanation:** M06-Q013 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects parallel budgets as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M06-Q014

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Measure queue cancellation data for review case three; limit the change.
- Measure interrupting atomic data for review case three; limit the change.
- Measure mean latency data for review case three; limit the change.
- Measure error response data for review case three; limit the change.

**Answer:** Measure mean latency data for review case three; limit the change.

**Explanation:** M06-Q014 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects mean latency as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M06-Q015

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Measure retrying every data for review case four; limit the change.
- Measure retries every data for review case four; limit the change.
- Measure jitter budget data for review case four; limit the change.
- Measure giving every data for review case four; limit the change.

**Answer:** Measure giving every data for review case four; limit the change.

**Explanation:** M06-Q015 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects giving every as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M06-Q016

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Measure deadline proof data for review case five; limit the change.
- Measure budgeting per data for review case five; limit the change.
- Measure retrying after data for review case five; limit the change.
- Measure post not data for review case five; limit the change. with margin

**Answer:** Measure deadline proof data for review case five; limit the change.

**Explanation:** M06-Q016 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects deadline proof as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M06-Q017

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Measure key fingerprint data for review case six; limit the change.
- Measure canceling only data for review case six; limit the change.
- Measure dedup cache data for review case six; limit the change.
- Measure short retention data for review case six; limit the change.

**Answer:** Measure canceling only data for review case six; limit the change.

**Explanation:** M06-Q017 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects canceling only as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M06-Q018

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Measure guessable global data for review case seven; limit the change.
- Measure one global data for review case seven; limit the change.
- Measure releasing permit data for review case seven; limit the change.
- Measure large queue data for review case seven; limit the change.

**Answer:** Measure releasing permit data for review case seven; limit the change.

**Explanation:** M06-Q018 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects releasing permit as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M06-Q019

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Measure increasing pool data for review case eight; limit the change.
- Measure deep liveness data for review case eight; limit the change.
- Measure drain test data for review case eight; limit the change. with margin
- Measure queue cancellation data for review case eight; limit the change.

**Answer:** Measure queue cancellation data for review case eight; limit the change.

**Explanation:** M06-Q019 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects queue cancellation as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M06-Q020

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Measure interrupting atomic data for review case nine; limit the change.
- Measure breaker universal data for review case nine; limit the change.
- Measure hedging unconditionally data for review case nine; limit the change.
- Measure not canceling data for review case nine; limit the change.

**Answer:** Measure interrupting atomic data for review case nine; limit the change.

**Explanation:** M06-Q020 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects interrupting atomic as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M06-Q021

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Measure partial success data for review case ten; limit the change.
- Measure error response data for review case ten; limit the change.
- Measure stale fallback data for review case ten; limit the change.
- Measure rate limit data for review case ten; limit the change.

**Answer:** Measure error response data for review case ten; limit the change.

**Explanation:** M06-Q021 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects error response as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M06-Q022

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** Calculation for end-to-end deadlines and allocation, usable budget is 900 - 180 = 720 ms; per stage is 240 ms.

**Explanation:** M06-Q022 uses deadline allocation from End-to-End Deadlines and Allocation and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M06-Q023

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** Calculation for cancellation and useful-work boundaries, worst count is 2^3 = 8 attempts for one original operation.

**Explanation:** M06-Q023 uses attempt count from Cancellation and Useful-Work Boundaries and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M06-Q024

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** Calculation for retry classification, budgets, backoff, and jitter, mean dependency concurrency is 180 x 0.060 = 10.8 active calls.

**Explanation:** M06-Q024 uses dependency concurrency from Retry Classification, Budgets, Backoff, and Jitter and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M06-Q025

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** Calculation for idempotency and deduplication, mean dependency concurrency is 180 x 0.060 = 10.8 active calls.

**Explanation:** M06-Q025 uses dependency concurrency from Idempotency and Deduplication and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M06-Q026

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** Calculation for bulkheads, pools, health, and bounded fan-out, mean dependency concurrency is 180 x 0.060 = 10.8 active calls.

**Explanation:** M06-Q026 uses dependency concurrency from Bulkheads, Pools, Health, and Bounded Fan-Out and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M06-Q027

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** Calculation for circuit breakers, hedges, and partial results, mean dependency concurrency is 180 x 0.060 = 10.8 active calls.

**Explanation:** M06-Q027 uses dependency concurrency from Circuit Breakers, Hedges, and Partial Results and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M06-Q028

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** Diagnosis for end-to-end deadlines and allocation, attempts.initial and attempts.per_dependency.unit separate the mechanism. attempts.initial = 24 while attempts.per_dependency.unit = 8, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare attempts.initial with attempts.per_dependency.unit and connect that contrast to end-to-end deadlines and allocation.

**Grading notes:** Full credit names End-to-End Deadlines and Allocation, cites attempts.initial and attempts.per_dependency.unit, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M06-Q029

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** Diagnosis for cancellation and useful-work boundaries, attempts.backoff_logical_ms.0 and attempts.per_dependency.road separate the mechanism. attempts.backoff_logical_ms.0 = 5 while attempts.per_dependency.road = 40, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare attempts.backoff_logical_ms.0 with attempts.per_dependency.road and connect that contrast to cancellation and useful-work boundaries.

**Grading notes:** Full credit names Cancellation and Useful-Work Boundaries, cites attempts.backoff_logical_ms.0 and attempts.per_dependency.road, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M06-Q030

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** Diagnosis for retry classification, budgets, backoff, and jitter, attempts.backoff_logical_ms.0 and attempts.per_dependency.road separate the mechanism. attempts.backoff_logical_ms.0 = 0.963 while attempts.per_dependency.road = 24, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare attempts.backoff_logical_ms.0 with attempts.per_dependency.road and connect that contrast to retry classification, budgets, backoff, and jitter.

**Grading notes:** Full credit names Retry Classification, Budgets, Backoff, and Jitter, cites attempts.backoff_logical_ms.0 and attempts.per_dependency.road, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M06-Q031

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** Diagnosis for idempotency and deduplication, attempts.initial and attempts.start_logical_ms.0 separate the mechanism. attempts.initial = 6 while attempts.start_logical_ms.0 = 3.242, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare attempts.initial with attempts.start_logical_ms.0 and connect that contrast to idempotency and deduplication.

**Grading notes:** Full credit names Idempotency and Deduplication, cites attempts.initial and attempts.start_logical_ms.0, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M06-Q032

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** Diagnosis for bulkheads, pools, health, and bounded fan-out, attempts.per_dependency.road and attempts.retries separate the mechanism. attempts.per_dependency.road = 2 while attempts.retries = 0, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare attempts.per_dependency.road with attempts.retries and connect that contrast to bulkheads, pools, health, and bounded fan-out.

**Grading notes:** Full credit names Bulkheads, Pools, Health, and Bounded Fan-Out, cites attempts.per_dependency.road and attempts.retries, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M06-Q033

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** Diagnosis for circuit breakers, hedges, and partial results, attempts.per_dependency.road and attempts.per_dependency.weather separate the mechanism. attempts.per_dependency.road = 2 while attempts.per_dependency.weather = 4, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare attempts.per_dependency.road with attempts.per_dependency.weather and connect that contrast to circuit breakers, hedges, and partial results.

**Grading notes:** Full credit names Circuit Breakers, Hedges, and Partial Results, cites attempts.per_dependency.road and attempts.per_dependency.weather, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M06-Q034

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** Diagnosis for rate limits, quotas, and fairness, attempts.per_dependency.road and attempts.retries separate the mechanism. attempts.per_dependency.road = 2 while attempts.retries = 0, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare attempts.per_dependency.road with attempts.retries and connect that contrast to rate limits, quotas, and fairness.

**Grading notes:** Full credit names Rate Limits, Quotas, and Fairness, cites attempts.per_dependency.road and attempts.retries, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M06-Q035

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** Diagnosis for remote-call policy, migration, and ownership, attempts.per_dependency.unit and attempts.start_logical_ms.0 separate the mechanism. attempts.per_dependency.unit = 8 while attempts.start_logical_ms.0 = 2.079, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare attempts.per_dependency.unit with attempts.start_logical_ms.0 and connect that contrast to remote-call policy, migration, and ownership.

**Grading notes:** Full credit names Remote-Call Policy, Migration, and Ownership, cites attempts.per_dependency.unit and attempts.start_logical_ms.0, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M06-Q036

**Type:** `design_judgment`
**Difficulty:** `recall`

**Answer:** Approve Deadline allocation at 130.6/s. The deciding number is 198 x 0.72 = 142.6/s, leaving 12/s before the reserve is consumed. Withdraw approval if a drill, trace, or workload sample shows deadline allocation demand above 142.6/s or proves the shed point cannot protect lower-priority work.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to deadline allocation demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 142.6/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M06-Q037

**Type:** `design_judgment`
**Difficulty:** `application`

**Answer:** Decline Serial and parallel call graph at 166.2/s. The deciding number is 215 x 0.72 = 154.8/s, so planned demand exceeds the usable region by 11.4/s. Approve later if repeated measurements lift usable capacity above 166.2/s or a named policy removes at least 11.4/s of deferrable work before saturation.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to serial and parallel call graph demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 154.8/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M06-Q038

**Type:** `design_judgment`
**Difficulty:** `synthesis`

**Answer:** Approve conditionally for Cancellation timeline. The deciding number is 232 x 0.72 = 167/s, and 162/s fits only while the fallback remains enforceable. Keep the condition until recovery traffic, priority demand, or fallback tests show less than 5/s of usable margin.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to cancellation timeline demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 167/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M06-Q039

**Type:** `design_judgment`
**Difficulty:** `recall`

**Answer:** Approve Atomic exception at 162.2/s. The deciding number is 249 x 0.72 = 179.3/s, leaving 17.1/s before the reserve is consumed. Require redesign if a drill, trace, or workload sample shows atomic exception demand above 179.3/s or proves the shed point cannot protect lower-priority work.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to atomic exception demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 179.3/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M06-Q040

**Type:** `design_judgment`
**Difficulty:** `application`

**Answer:** Decline Layered amplification at 207.1/s. The deciding number is 266 x 0.72 = 191.5/s, so planned demand exceeds the usable region by 15.6/s. Lift the decline if repeated measurements lift usable capacity above 207.1/s or a named policy removes at least 15.6/s of deferrable work before saturation.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to layered amplification demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 191.5/s, compares it with planned demand, and names a scenario-specific reversal condition.
