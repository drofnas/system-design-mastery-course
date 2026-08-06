# M03 Quiz Answer Key

This key covers all 18 questions for **Computer Systems and Operating Systems**. Use it after an attempt, or provide it with the LLM grading prompt for feedback.

## M03-Q001

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** It prevents dead-code elimination and establishes equivalent output without adding output I/O to the timed region.

**Explanation:** M03-Q001 uses self-check 1 from Benchmark Contracts, Pipelines, Caches, and Locality; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M03-Q002

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** It proves only that the complete measured variant finished sooner under the recorded conditions. It does not isolate a cache or branch mechanism.

**Explanation:** M03-Q002 uses self-check 2 from Benchmark Contracts, Pipelines, Caches, and Locality; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M03-Q003

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** When production repeatedly reuses the same working set and the claim is about steady-state behavior. The contract must say so.

**Explanation:** M03-Q003 uses self-check 3 from Benchmark Contracts, Pipelines, Caches, and Locality; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M03-Q004

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** It may execute more instructions or create longer data dependencies than a well-predicted branch.

**Explanation:** M03-Q004 uses self-check 4 from Benchmark Contracts, Pipelines, Caches, and Locality; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M03-Q005

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** When copy/allocation cost is outside the measurement, reuse is too low to cross `C / Δ`, or ownership, freshness, and memory requirements make the extra representation unsafe. Measure the complete boundary the decision will pay.

**Explanation:** M03-Q005 uses self-check 5 from Benchmark Contracts, Pipelines, Caches, and Locality; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M03-Q006

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** Yes. Runnable work can wait in a scheduler queue or be quota-throttled.

**Explanation:** M03-Q006 uses self-check 1 from Processes, Scheduling, Context Switches, and System Calls; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M03-Q007

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** A thread can voluntarily block on a lock, condition, sleep, or other resource.

**Explanation:** M03-Q007 uses self-check 2 from Processes, Scheduling, Context Switches, and System Calls; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M03-Q008

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** Scheduling displacement increased under the recorded conditions; the cause still needs controlled variation.

**Explanation:** M03-Q008 uses self-check 3 from Processes, Scheduling, Context Switches, and System Calls; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M03-Q009

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** It changes when data becomes visible, when failures surface, and which records share an error or durability boundary.

**Explanation:** M03-Q009 uses self-check 4 from Processes, Scheduling, Context Switches, and System Calls; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M03-Q010

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** No. Reservation and lazy allocation can precede page touching and residency.

**Explanation:** M03-Q010 uses self-check 1 from Virtual Memory, Allocation, Page Faults, and RSS; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M03-Q011

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** A reported major fault required I/O; a minor fault was serviced without I/O.

**Explanation:** M03-Q011 uses self-check 2 from Virtual Memory, Allocation, Page Faults, and RSS; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M03-Q012

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** Current memory can fall before sampling, while peak shows maximum exposure; both still need platform definitions.

**Explanation:** M03-Q012 uses self-check 3 from Virtual Memory, Allocation, Page Faults, and RSS; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M03-Q013

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** The service and platform owners jointly define limits, termination/restart, observability, and capacity response.

**Explanation:** M03-Q013 uses self-check 4 from Virtual Memory, Allocation, Page Faults, and RSS; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M03-Q014

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** Contended actors eventually progress; a deadlocked wait cycle cannot progress without outside change.

**Explanation:** M03-Q014 uses self-check 1 from Locks, Contention, Deadlock, and False Sharing; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M03-Q025

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** Packed records touch 10,040 x 64 / 64 = 10,040 cache lines.

**Explanation:** M03-Q025 uses cache-line scan from Benchmark Contracts, Pipelines, Caches, and Locality and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M03-Q026

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** 256 MiB is 262144 KiB; 262144 / 4 = 65,536 pages.

**Explanation:** M03-Q026 uses page first touches from Processes, Scheduling, Context Switches, and System Calls and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M03-Q027

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** Excess demand is 3.5 - 2.0 = 1.5 CPU-seconds during that second.

**Explanation:** M03-Q027 uses CPU quota from Virtual Memory, Allocation, Page Faults, and RSS and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M03-Q028

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** Excess demand is 3.5 - 2.0 = 1.5 CPU-seconds during that second.

**Explanation:** M03-Q028 uses CPU quota from Locks, Contention, Deadlock, and False Sharing and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.
