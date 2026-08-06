# M15 Quiz Answer Key

This key covers all 16 questions for **Execution Models Across Languages**. Use it after an attempt, or provide it with the LLM grading prompt for feedback.

## M15-Q001

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** No. Borrow rules cover memory access; external-resource lifetime still needs an owned close path and observed cleanup.

**Explanation:** M15-Q001 uses self-check 1 from Memory Lifetime and Management; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M15-Q002

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** The runtime or allocator may keep reclaimed regions for reuse; object reachability, heap commitment, and RSS are different measures.

**Explanation:** M15-Q002 uses self-check 2 from Memory Lifetime and Management; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M15-Q003

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** Retainer paths or owner identities show continuing reachability; collector events plus falling live-set size suggest delayed reclamation instead.

**Explanation:** M15-Q003 uses self-check 3 from Memory Lifetime and Management; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M15-Q004

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** One core or executor thread may be saturated while the host has idle cores; throttling or a blocked scheduler can also hide behind aggregate CPU.

**Explanation:** M15-Q004 uses self-check 1 from Schedulers, Event Loops, and Tasks; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M15-Q005

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** It reduces the cost and coupling of one Java task to one OS thread. It does not add CPU, memory, connections, downstream capacity, deadlines, or bounds.

**Explanation:** M15-Q005 uses self-check 2 from Schedulers, Event Loops, and Tasks; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M15-Q006

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** When offered children are unbounded or cancellation/cleanup does not own their lifetime, task count and external work can grow beyond the budget.

**Explanation:** M15-Q006 uses self-check 3 from Schedulers, Event Loops, and Tasks; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M15-Q007

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** Orphan work consumes resources, may perform effects after authority expires, and can leak request or tenant context.

**Explanation:** M15-Q007 uses self-check 1 from Bounded Fan-out and Structured Cleanup; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M15-Q008

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** Validate a small bounded envelope, then admit before large allocation or child creation. Otherwise rejected work can still exhaust the service.

**Explanation:** M15-Q008 uses self-check 2 from Bounded Fan-out and Structured Cleanup; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M15-Q009

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** Stable task/resource identities, cancellation acknowledgement, zero owned active tasks and open resources after grace, plus matched acquisition/release.

**Explanation:** M15-Q009 uses self-check 3 from Bounded Fan-out and Structured Cleanup; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M15-Q010

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** No. The executed schedules may not expose the conflict and observations do not create a language-defined ordering.

**Explanation:** M15-Q010 uses self-check 1 from Memory Visibility and Races; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M15-Q011

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** No. The counter and list need one coherent protocol and completion boundary.

**Explanation:** M15-Q011 uses self-check 2 from Memory Visibility and Races; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M15-Q012

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** Workload and schedule coverage, tool/runtime identity, invariant checks, unsupported-code limits, and a separate static or causal argument.

**Explanation:** M15-Q012 uses self-check 3 from Memory Visibility and Races; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M15-Q013

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** Nothing at runtime; it only changes the compiler's assumed type.

**Explanation:** M15-Q013 uses self-check 1 from Types, Serialization, and Validation; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M15-Q022

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** Retained memory is 1800 x 12 KiB = 21600 KiB = 21.1 MiB.

**Explanation:** M15-Q022 uses retained memory from Memory Lifetime and Management and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M15-Q023

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** Report 930/1000 = 93.0% against the same equivalent-work denominator.

**Explanation:** M15-Q023 uses success denominator from Schedulers, Event Loops, and Tasks and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M15-Q024

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** 12 - 8 = 4 tasks wait before any scheduling overhead.

**Explanation:** M15-Q024 uses runtime slots from Bounded Fan-out and Structured Cleanup and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.
