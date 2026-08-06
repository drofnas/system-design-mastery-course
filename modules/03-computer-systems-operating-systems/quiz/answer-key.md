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

- Measure timing unequal data for review case one; limit the change.
- Measure one iteration data for review case one; limit the change.
- Measure naming cache data for review case one; limit the change. with margin
- Measure reporting only data for review case one; limit the change.

**Answer:** Measure timing unequal data for review case one; limit the change.

**Explanation:** M03-Q015 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects timing unequal as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M03-Q016

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Measure generalizing across data for review case two; limit the change.
- Measure one iteration data for review case two; limit the change.
- Measure equating threads data for review case two; limit the change.
- Measure every context data for review case two; limit the change.

**Answer:** Measure one iteration data for review case two; limit the change.

**Explanation:** M03-Q016 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects one iteration as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M03-Q017

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Measure logical cpus data for review case three; limit the change.
- Measure syscall count data for review case three; limit the change.
- Measure naming cache data for review case three; limit the change.
- Measure throttled blocked data for review case three; limit the change.

**Answer:** Measure naming cache data for review case three; limit the change.

**Explanation:** M03-Q017 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects naming cache as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M03-Q018

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Measure every fault data for review case four; limit the change. with margin
- Measure rss allocated data for review case four; limit the change.
- Measure forcing host data for review case four; limit the change.
- Measure reporting only data for review case four; limit the change.

**Answer:** Measure reporting only data for review case four; limit the change.

**Explanation:** M03-Q018 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects reporting only as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M03-Q019

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Measure generalizing across data for review case five; limit the change.
- Measure different initialization data for review case five; limit the change.
- Measure oom exception data for review case five; limit the change.
- Measure away correctness data for review case five; limit the change.

**Answer:** Measure generalizing across data for review case five; limit the change.

**Explanation:** M03-Q019 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects generalizing across as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M03-Q020

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Measure any slow data for review case six; limit the change. with margin
- Measure equating threads data for review case six; limit the change.
- Measure running deadlock data for review case six; limit the change.
- Measure cache line data for review case six; limit the change.

**Answer:** Measure equating threads data for review case six; limit the change.

**Explanation:** M03-Q020 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects equating threads as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M03-Q021

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Measure asserting padded data for review case seven; limit the change.
- Measure close durability data for review case seven; limit the change.
- Measure every context data for review case seven; limit the change.
- Measure directory durability data for review case seven; limit the change.

**Answer:** Measure every context data for review case seven; limit the change.

**Explanation:** M03-Q021 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects every context as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M03-Q022

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Measure dev null data for review case eight; limit the change.
- Measure dropping caches data for review case eight; limit the change.
- Measure reporting average data for review case eight; limit the change.
- Measure logical cpus data for review case eight; limit the change.

**Answer:** Measure logical cpus data for review case eight; limit the change.

**Explanation:** M03-Q022 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects logical cpus as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M03-Q023

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Measure syscall count data for review case nine; limit the change.
- Measure all time data for review case nine; limit the change.
- Measure changing chunk data for review case nine; limit the change.
- Measure host wide data for review case nine; limit the change.

**Answer:** Measure syscall count data for review case nine; limit the change.

**Explanation:** M03-Q023 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects syscall count as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M03-Q024

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Measure cleanup abandoned data for review case ten; limit the change.
- Measure throttled blocked data for review case ten; limit the change.
- Measure latency losing data for review case ten; limit the change.
- Measure reading free data for review case ten; limit the change.

**Answer:** Measure throttled blocked data for review case ten; limit the change.

**Explanation:** M03-Q024 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects throttled blocked as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M03-Q025

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** Calculation for benchmark contracts, pipelines, caches, and locality, m03 Cache-Line Scan case 1: Packed records touch 10,040 x 64 / 64 = 10,040 cache lines.

**Explanation:** M03-Q025 uses cache-line scan from Benchmark Contracts, Pipelines, Caches, and Locality and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M03-Q026

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** Calculation for processes, scheduling, context switches, and system calls, 256 MiB is 262144 KiB; 262144 / 4 = 65,536 pages.

**Explanation:** M03-Q026 uses page first touches from Processes, Scheduling, Context Switches, and System Calls and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M03-Q027

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** Calculation for virtual memory, allocation, page faults, and rss, excess demand is 3.5 - 2.0 = 1.5 CPU-seconds during that second.

**Explanation:** M03-Q027 uses CPU quota from Virtual Memory, Allocation, Page Faults, and RSS and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M03-Q028

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** Calculation for locks, contention, deadlock, and false sharing, excess demand is 3.5 - 2.0 = 1.5 CPU-seconds during that second.

**Explanation:** M03-Q028 uses CPU quota from Locks, Contention, Deadlock, and False Sharing and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M03-Q029

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** Calculation for files, page cache, writeback, and durable writes, m03 Cache-Line Scan case 5: Packed records touch 10,080 x 64 / 64 = 10,080 cache lines.

**Explanation:** M03-Q029 uses cache-line scan from Files, Page Cache, Writeback, and Durable Writes and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M03-Q030

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** Diagnosis for benchmark contracts, pipelines, caches, and locality, parameters.iterations and warmup separate the mechanism. parameters.iterations = 4096 while warmup = 1, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare parameters.iterations with warmup and connect that contrast to benchmark contracts, pipelines, caches, and locality.

**Grading notes:** Full credit names Benchmark Contracts, Pipelines, Caches, and Locality, cites parameters.iterations and warmup, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M03-Q031

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** Diagnosis for processes, scheduling, context switches, and system calls, parameters.iterations and repetitions separate the mechanism. parameters.iterations = 4096 while repetitions = 3, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare parameters.iterations with repetitions and connect that contrast to processes, scheduling, context switches, and system calls.

**Grading notes:** Full credit names Processes, Scheduling, Context Switches, and System Calls, cites parameters.iterations and repetitions, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M03-Q032

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** Diagnosis for virtual memory, allocation, page faults, and rss, parameters.iterations and timeout_seconds separate the mechanism. parameters.iterations = 128 while timeout_seconds = 20, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare parameters.iterations with timeout_seconds and connect that contrast to virtual memory, allocation, page faults, and rss.

**Grading notes:** Full credit names Virtual Memory, Allocation, Page Faults, and RSS, cites parameters.iterations and timeout_seconds, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M03-Q033

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** Diagnosis for locks, contention, deadlock, and false sharing, parameters.bytes_per_iteration and warmup separate the mechanism. parameters.bytes_per_iteration = 1.04858e+06 while warmup = 0, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare parameters.bytes_per_iteration with warmup and connect that contrast to locks, contention, deadlock, and false sharing.

**Grading notes:** Full credit names Locks, Contention, Deadlock, and False Sharing, cites parameters.bytes_per_iteration and warmup, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M03-Q034

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** Diagnosis for files, page cache, writeback, and durable writes, parameters.bytes_per_iteration and repetitions separate the mechanism. parameters.bytes_per_iteration = 1.04858e+06 while repetitions = 3, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare parameters.bytes_per_iteration with repetitions and connect that contrast to files, page cache, writeback, and durable writes.

**Grading notes:** Full credit names Files, Page Cache, Writeback, and Durable Writes, cites parameters.bytes_per_iteration and repetitions, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M03-Q035

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** Diagnosis for device queues and i/o latency, parameters.bytes_per_iteration and timeout_seconds separate the mechanism. parameters.bytes_per_iteration = 1.04858e+06 while timeout_seconds = 20, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare parameters.bytes_per_iteration with timeout_seconds and connect that contrast to device queues and i/o latency.

**Grading notes:** Full credit names Device Queues and I/O Latency, cites parameters.bytes_per_iteration and timeout_seconds, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M03-Q036

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** Diagnosis for containers, quotas, throttling, and memory limits, warmup and timeout_seconds separate the mechanism. warmup = 1 while timeout_seconds = 10, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare warmup with timeout_seconds and connect that contrast to containers, quotas, throttling, and memory limits.

**Grading notes:** Full credit names Containers, Quotas, Throttling, and Memory Limits, cites warmup and timeout_seconds, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M03-Q037

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** Diagnosis for causal diagnosis and production decisions, repetitions and timeout_seconds separate the mechanism. repetitions = 3 while timeout_seconds = 10, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare repetitions with timeout_seconds and connect that contrast to causal diagnosis and production decisions.

**Grading notes:** Full credit names Causal Diagnosis and Production Decisions, cites repetitions and timeout_seconds, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M03-Q038

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** Diagnosis for benchmark contracts, pipelines, caches, and locality, parameters.workers and repetitions separate the mechanism. parameters.workers = 1 while repetitions = 3, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare parameters.workers with repetitions and connect that contrast to benchmark contracts, pipelines, caches, and locality.

**Grading notes:** Full credit names Benchmark Contracts, Pipelines, Caches, and Locality, cites parameters.workers and repetitions, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M03-Q039

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** Diagnosis for processes, scheduling, context switches, and system calls, parameters.workers and warmup separate the mechanism. parameters.workers = 16 while warmup = 1, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare parameters.workers with warmup and connect that contrast to processes, scheduling, context switches, and system calls.

**Grading notes:** Full credit names Processes, Scheduling, Context Switches, and System Calls, cites parameters.workers and warmup, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M03-Q040

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** Diagnosis for virtual memory, allocation, page faults, and rss, parameters.workers and repetitions separate the mechanism. parameters.workers = 8 while repetitions = 3, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare parameters.workers with repetitions and connect that contrast to virtual memory, allocation, page faults, and rss.

**Grading notes:** Full credit names Virtual Memory, Allocation, Page Faults, and RSS, cites parameters.workers and repetitions, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M03-Q041

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** Diagnosis for locks, contention, deadlock, and false sharing, parameters.iterations and repetitions separate the mechanism. parameters.iterations = 500000 while repetitions = 3, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare parameters.iterations with repetitions and connect that contrast to locks, contention, deadlock, and false sharing.

**Grading notes:** Full credit names Locks, Contention, Deadlock, and False Sharing, cites parameters.iterations and repetitions, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M03-Q042

**Type:** `design_judgment`
**Difficulty:** `recall`

**Answer:** Approve Freeze equivalent work at 124.1/s. The deciding number is 189 x 0.72 = 136.1/s, leaving 12/s before the reserve is consumed. Withdraw approval if a drill, trace, or workload sample shows freeze equivalent work demand above 136.1/s or proves the shed point cannot protect lower-priority work.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to freeze equivalent work demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 136.1/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M03-Q043

**Type:** `design_judgment`
**Difficulty:** `application`

**Answer:** Decline Locality and branch model at 159.7/s. The deciding number is 206 x 0.72 = 148.3/s, so planned demand exceeds the usable region by 11.4/s. Approve later if repeated measurements lift usable capacity above 159.7/s or a named policy removes at least 11.4/s of deferrable work before saturation.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to locality and branch model demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 148.3/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M03-Q044

**Type:** `design_judgment`
**Difficulty:** `synthesis`

**Answer:** Approve conditionally for Scheduler state table. The deciding number is 223 x 0.72 = 160.6/s, and 155.6/s fits only while the fallback remains enforceable. Keep the condition until recovery traffic, priority demand, or fallback tests show less than 5/s of usable margin.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to scheduler state table demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 160.6/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M03-Q045

**Type:** `design_judgment`
**Difficulty:** `recall`

**Answer:** Approve Syscall batching at 155.7/s. The deciding number is 240 x 0.72 = 172.8/s, leaving 17.1/s before the reserve is consumed. Require redesign if a drill, trace, or workload sample shows syscall batching demand above 172.8/s or proves the shed point cannot protect lower-priority work.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to syscall batching demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 172.8/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M03-Q046

**Type:** `design_judgment`
**Difficulty:** `application`

**Answer:** Decline First-touch estimate at 200.6/s. The deciding number is 257 x 0.72 = 185/s, so planned demand exceeds the usable region by 15.6/s. Lift the decline if repeated measurements lift usable capacity above 200.6/s or a named policy removes at least 15.6/s of deferrable work before saturation.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to first-touch estimate demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 185/s, compares it with planned demand, and names a scenario-specific reversal condition.
