# M03 Quiz Answer Key

This key covers all 46 questions for **Computer Systems and Operating Systems**. Use it after an attempt, or provide it with the LLM grading prompt for feedback.

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

## M03-Q015

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Scope the M03 scoped measurement and record the limiting assumption before approving the change.
- Approve a faster wrong checksum is not an optimization for Benchmark Contracts, Pipelines, Caches, and Locality; the local context makes that proposal familiar enough for review.
- Defer measurement until production for a faster wrong checksum is not an optimization; the team can monitor Benchmark Contracts, Pipelines, Caches, and Locality after launch.
- Approve the M03 shortcut for alpha now.

**Answer:** Scope the M03 scoped measurement and record the limiting assumption before approving the change.

**Explanation:** M03-Q015 enacts mistake 1 from Benchmark Contracts, Pipelines, Caches, and Locality; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M03-Q016

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Approve startup, interrupts, and frequency state dominate for Benchmark Contracts, Pipelines, Caches, and Locality; the local context makes that proposal familiar enough for review.
- Measure the M03 scoped measurement before approving the change.
- Defer measurement until production for startup, interrupts, and frequency state dominate; the team can monitor Benchmark Contracts, Pipelines, Caches, and Locality after launch.
- Approve the M03 shortcut for bravo now.

**Answer:** Measure the M03 scoped measurement before approving the change.

**Explanation:** M03-Q016 enacts mistake 2 from Benchmark Contracts, Pipelines, Caches, and Locality; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M03-Q017

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Approve layout, vectorization, or copying for Benchmark Contracts, Pipelines, Caches, and Locality; the local context makes that proposal familiar enough for review.
- Defer measurement until production for layout, vectorization, or copying; the team can monitor Benchmark Contracts, Pipelines, Caches, and Locality after launch.
- Bound the M03 scoped measurement before approval.
- Approve the M03 shortcut for charlie now.

**Answer:** Bound the M03 scoped measurement before approval.

**Explanation:** M03-Q017 enacts mistake 3 from Benchmark Contracts, Pipelines, Caches, and Locality; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M03-Q018

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Approve it selects favorable noise and hides variance for Benchmark Contracts, Pipelines, Caches, and Locality; the local context makes that proposal familiar enough for review.
- Defer measurement until production for it selects favorable noise and hides variance; the team can monitor Benchmark Contracts, Pipelines, Caches, and Locality after launch.
- Approve the M03 shortcut for delta now.
- Freeze the M03 scoped measurement and record the limiting assumption before approving the change.

**Answer:** Freeze the M03 scoped measurement and record the limiting assumption before approving the change.

**Explanation:** M03-Q018 enacts mistake 4 from Benchmark Contracts, Pipelines, Caches, and Locality; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M03-Q019

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Preserve the M03 scoped measurement before approving the change.
- Approve cache and branch behavior are not API contracts for Benchmark Contracts, Pipelines, Caches, and Locality; the local context makes that proposal familiar enough for review.
- Defer measurement until production for cache and branch behavior are not API contracts; the team can monitor Benchmark Contracts, Pipelines, Caches, and Locality after launch.
- Approve the M03 shortcut for ember now.

**Answer:** Preserve the M03 scoped measurement before approving the change.

**Explanation:** M03-Q019 enacts mistake 5 from Benchmark Contracts, Pipelines, Caches, and Locality; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M03-Q020

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Approve runnable threads still need CPU capacity for Processes, Scheduling, Context Switches, and System Cal; the local context makes that proposal familiar enough for review.
- Model the M03 scoped measurement before approval.
- Defer measurement until production for runnable threads still need CPU capacity; the team can monitor Processes, Scheduling, Context Switches, and System Cal after launch.
- Approve the M03 shortcut for fable now.

**Answer:** Model the M03 scoped measurement before approval.

**Explanation:** M03-Q020 enacts mistake 1 from Processes, Scheduling, Context Switches, and System Calls; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M03-Q021

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Approve blocking is required for many correct waits for Processes, Scheduling, Context Switches, and System Cal; the local context makes that proposal familiar enough for review.
- Defer measurement until production for blocking is required for many correct waits; the team can monitor Processes, Scheduling, Context Switches, and System Cal after launch.
- Account the M03 scoped measurement and record the limiting assumption before approving the change.
- Approve the M03 shortcut for harbor now.

**Answer:** Account the M03 scoped measurement and record the limiting assumption before approving the change.

**Explanation:** M03-Q021 enacts mistake 2 from Processes, Scheduling, Context Switches, and System Calls; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M03-Q022

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Approve treating logical CPUs as identical physical cores:: SMT and heterogeneous for Processes, Scheduling, Context Switches, and System Cal; the local context makes that proposal familiar enough for review.
- Defer measurement until production for treating logical CPUs as identical physical cores:: SMT and heterogeneous; the team can monitor Processes, Scheduling, Context Switches, and System Cal after launch.
- Approve the M03 shortcut for indigo now.
- Test the M03 scoped measurement before approving the change.

**Answer:** Test the M03 scoped measurement before approving the change.

**Explanation:** M03-Q022 enacts mistake 3 from Processes, Scheduling, Context Switches, and System Calls; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M03-Q023

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Scope the M03 scoped measurement before approval.
- Approve request size and kernel work also change cost for Processes, Scheduling, Context Switches, and System Cal; the local context makes that proposal familiar enough for review.
- Defer measurement until production for request size and kernel work also change cost; the team can monitor Processes, Scheduling, Context Switches, and System Cal after launch.
- Approve the M03 shortcut for juniper now.

**Answer:** Scope the M03 scoped measurement before approval.

**Explanation:** M03-Q023 enacts mistake 4 from Processes, Scheduling, Context Switches, and System Calls; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M03-Q024

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Approve the remediation and owner differ for Processes, Scheduling, Context Switches, and System Cal; the local context makes that proposal familiar enough for review.
- Measure the M03 scoped measurement and record the limiting assumption before approving the change.
- Defer measurement until production for the remediation and owner differ; the team can monitor Processes, Scheduling, Context Switches, and System Cal after launch.
- Approve the M03 shortcut for keystone now.

**Answer:** Measure the M03 scoped measurement and record the limiting assumption before approving the change.

**Explanation:** M03-Q024 enacts mistake 5 from Processes, Scheduling, Context Switches, and System Calls; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M03-Q025

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** M03 Cache-Line Scan case 1: Packed records touch 10,040 x 64 / 64 = 10,040 cache lines.

**Explanation:** M03-Q025 uses cache-line scan from Benchmark Contracts, Pipelines, Caches, and Locality and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M03-Q026

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** M03 Page First Touches case 2: 256 MiB is 262144 KiB; 262144 / 4 = 65,536 pages.

**Explanation:** M03-Q026 uses page first touches from Processes, Scheduling, Context Switches, and System Calls and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M03-Q027

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** M03 Cpu Quota case 3: Excess demand is 3.5 - 2.0 = 1.5 CPU-seconds during that second.

**Explanation:** M03-Q027 uses CPU quota from Virtual Memory, Allocation, Page Faults, and RSS and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M03-Q028

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** M03 Cpu Quota case 4: Excess demand is 3.5 - 2.0 = 1.5 CPU-seconds during that second.

**Explanation:** M03-Q028 uses CPU quota from Locks, Contention, Deadlock, and False Sharing and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M03-Q029

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** M03 Cache-Line Scan case 5: Packed records touch 10,080 x 64 / 64 = 10,080 cache lines.

**Explanation:** M03-Q029 uses cache-line scan from Files, Page Cache, Writeback, and Durable Writes and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M03-Q030

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** M03 diagnosis 1 identifies Benchmark Contracts, Pipelines, Caches, and Locality evidence scope. The proving fields are parameters.iterations and parameters.bytes_per_iteration; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M03-Q030 comes from emitted trial fields rather than fixture identifiers; Benchmark Contracts, Pipelines, Caches, and Locality is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M03-Q031

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** M03 diagnosis 2 identifies Processes, Scheduling, Context Switches, and System Calls evidence scope. The proving fields are parameters.iterations and parameters.bytes_per_iteration; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M03-Q031 comes from emitted trial fields rather than fixture identifiers; Processes, Scheduling, Context Switches, and System Calls is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M03-Q032

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** M03 diagnosis 3 identifies Virtual Memory, Allocation, Page Faults, and RSS evidence scope. The proving fields are parameters.iterations and parameters.bytes_per_iteration; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M03-Q032 comes from emitted trial fields rather than fixture identifiers; Virtual Memory, Allocation, Page Faults, and RSS is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M03-Q033

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** M03 diagnosis 4 identifies Locks, Contention, Deadlock, and False Sharing evidence scope. The proving fields are parameters.iterations and parameters.bytes_per_iteration; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M03-Q033 comes from emitted trial fields rather than fixture identifiers; Locks, Contention, Deadlock, and False Sharing is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M03-Q034

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** M03 diagnosis 5 identifies Files, Page Cache, Writeback, and Durable Writes evidence scope. The proving fields are parameters.iterations and parameters.bytes_per_iteration; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M03-Q034 comes from emitted trial fields rather than fixture identifiers; Files, Page Cache, Writeback, and Durable Writes is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M03-Q035

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** M03 diagnosis 6 identifies Device Queues and I/O Latency evidence scope. The proving fields are parameters.iterations and parameters.bytes_per_iteration; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M03-Q035 comes from emitted trial fields rather than fixture identifiers; Device Queues and I/O Latency is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M03-Q036

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** M03 diagnosis 7 identifies Containers, Quotas, Throttling, and Memory Limits evidence scope. The proving fields are parameters.elements and parameters.stride; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M03-Q036 comes from emitted trial fields rather than fixture identifiers; Containers, Quotas, Throttling, and Memory Limits is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M03-Q037

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** M03 diagnosis 8 identifies Causal Diagnosis and Production Decisions evidence scope. The proving fields are parameters.elements and parameters.stride; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M03-Q037 comes from emitted trial fields rather than fixture identifiers; Causal Diagnosis and Production Decisions is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M03-Q038

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** M03 diagnosis 9 identifies Benchmark Contracts, Pipelines, Caches, and Locality evidence scope. The proving fields are parameters.workers and parameters.iterations; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M03-Q038 comes from emitted trial fields rather than fixture identifiers; Benchmark Contracts, Pipelines, Caches, and Locality is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M03-Q039

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** M03 diagnosis 10 identifies Processes, Scheduling, Context Switches, and System Calls evidence scope. The proving fields are parameters.workers and parameters.iterations; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M03-Q039 comes from emitted trial fields rather than fixture identifiers; Processes, Scheduling, Context Switches, and System Calls is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M03-Q040

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** M03 diagnosis 11 identifies Virtual Memory, Allocation, Page Faults, and RSS evidence scope. The proving fields are parameters.workers and parameters.iterations; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M03-Q040 comes from emitted trial fields rather than fixture identifiers; Virtual Memory, Allocation, Page Faults, and RSS is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M03-Q041

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** M03 diagnosis 12 identifies Locks, Contention, Deadlock, and False Sharing evidence scope. The proving fields are parameters.workers and parameters.iterations; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M03-Q041 comes from emitted trial fields rather than fixture identifiers; Locks, Contention, Deadlock, and False Sharing is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M03-Q042

**Type:** `design_judgment`
**Difficulty:** `recall`

**Answer:** For M03 decision 1, recommend against. The protected bound is 189 x 0.72 = 136.1/s, and the planned 166.3/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 166.3/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 30.2/s of lower-priority work.

**Explanation:** M03-Q042 turns on the forcing number from EX-01, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M03-Q043

**Type:** `design_judgment`
**Difficulty:** `application`

**Answer:** For M03 decision 2, recommend against. The protected bound is 206 x 0.72 = 148.3/s, and the planned 181.3/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 181.3/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 33.0/s of lower-priority work.

**Explanation:** M03-Q043 turns on the forcing number from EX-02, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M03-Q044

**Type:** `design_judgment`
**Difficulty:** `synthesis`

**Answer:** For M03 decision 3, recommend against. The protected bound is 223 x 0.72 = 160.6/s, and the planned 196.2/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 196.2/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 35.6/s of lower-priority work.

**Explanation:** M03-Q044 turns on the forcing number from EX-03, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M03-Q045

**Type:** `design_judgment`
**Difficulty:** `recall`

**Answer:** For M03 decision 4, recommend against. The protected bound is 240 x 0.72 = 172.8/s, and the planned 211.2/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 211.2/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 38.4/s of lower-priority work.

**Explanation:** M03-Q045 turns on the forcing number from EX-04, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M03-Q046

**Type:** `design_judgment`
**Difficulty:** `application`

**Answer:** For M03 decision 5, recommend against. The protected bound is 257 x 0.72 = 185.0/s, and the planned 226.2/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 226.2/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 41.2/s of lower-priority work.

**Explanation:** M03-Q046 turns on the forcing number from EX-05, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.
