# M06 Quiz Answer Key

This key covers all 17 questions for **Deadlines and Resilient Remote Calls**. Use it after an attempt, or provide it with the LLM grading prompt for feedback.

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

## M06-Q022

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** Usable budget is 900 - 180 = 720 ms; per stage is 240 ms.

**Explanation:** M06-Q022 uses deadline allocation from End-to-End Deadlines and Allocation and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M06-Q023

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** Worst count is 2^3 = 8 attempts for one original operation.

**Explanation:** M06-Q023 uses attempt count from Cancellation and Useful-Work Boundaries and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M06-Q024

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** Mean dependency concurrency is 180 x 0.060 = 10.8 active calls.

**Explanation:** M06-Q024 uses dependency concurrency from Retry Classification, Budgets, Backoff, and Jitter and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M06-Q025

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** Idempotency still sizes the held calls as 180 x 0.060 = 10.8 active calls.

**Explanation:** M06-Q025 uses dependency concurrency from Idempotency and Deduplication and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M06-Q026

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** Bulkhead capacity should expect 180 x 0.060 = 10.8 active dependency calls.

**Explanation:** M06-Q026 uses dependency concurrency from Bulkheads, Pools, Health, and Bounded Fan-Out and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M06-Q027

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** Breaker math still starts from 180 x 0.060 = 10.8 active calls before hedge amplification.

**Explanation:** M06-Q027 uses dependency concurrency from Circuit Breakers, Hedges, and Partial Results and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.
