# M15 Quiz Answer Key

This key covers all 38 questions for **Execution Models Across Languages**. Use it after an attempt, or provide it with the LLM grading prompt for feedback.

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

## M15-Q014

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Measure heap allocation data for review case one; limit the change.
- Measure low rss data for review case one; limit the change. with margin
- Measure raii closes data for review case one; limit the change.
- Measure pauses heap data for review case one; limit the change.

**Answer:** Measure heap allocation data for review case one; limit the change.

**Explanation:** M15-Q014 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects heap allocation as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M15-Q015

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Measure all node data for review case two; limit the change. with margin
- Measure low rss data for review case two; limit the change. with margin
- Measure measuring cpu data for review case two; limit the change.
- Measure replacing small data for review case two; limit the change.

**Answer:** Measure low rss data for review case two; limit the change. with margin

**Explanation:** M15-Q015 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects low rss as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M15-Q016

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Measure async syntax data for review case three; limit the change. with margin
- Measure semaphore after data for review case three; limit the change.
- Measure raii closes data for review case three; limit the change. with margin
- Measure returning after data for review case three; limit the change.

**Answer:** Measure raii closes data for review case three; limit the change. with margin

**Explanation:** M15-Q016 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects raii closes as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M15-Q017

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Measure timeout exception data for review case four; limit the change. with margin
- Measure giving optional data for review case four; limit the change.
- Measure race detector data for review case four; limit the change.
- Measure pauses heap data for review case four; limit the change. with margin

**Answer:** Measure pauses heap data for review case four; limit the change. with margin

**Explanation:** M15-Q017 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects pauses heap as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M15-Q018

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Measure all node data for review case five; limit the change. with margin
- Measure volatile general data for review case five; limit the change. with margin
- Measure fixing race data for review case five; limit the change.
- Measure race freedom data for review case five; limit the change.

**Answer:** Measure all node data for review case five; limit the change. with margin

**Explanation:** M15-Q018 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects all node as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M15-Q019

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Measure generated type data for review case six; limit the change. with margin
- Measure measuring cpu data for review case six; limit the change. with margin
- Measure returning library data for review case six; limit the change.
- Measure validating shape data for review case six; limit the change.

**Answer:** Measure measuring cpu data for review case six; limit the change. with margin

**Explanation:** M15-Q019 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects measuring cpu as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M15-Q020

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Measure allowing unknown data for review case seven; limit the change.
- Measure mixing cold data for review case seven; limit the change.
- Measure replacing small data for review case seven; limit the change.
- Measure fixing concurrency data for review case seven; limit the change.

**Answer:** Measure replacing small data for review case seven; limit the change.

**Explanation:** M15-Q020 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects replacing small as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M15-Q021

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Measure rss heap data for review case eight; limit the change.
- Measure removing outliers data for review case eight; limit the change.
- Measure editing northstar data for review case eight; limit the change.
- Measure async syntax data for review case eight; limit the change.

**Answer:** Measure async syntax data for review case eight; limit the change.

**Explanation:** M15-Q021 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects async syntax as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M15-Q022

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** Calculation for memory lifetime and management, retained memory is 1800 x 12 KiB = 21600 KiB = 21.1 MiB.

**Explanation:** M15-Q022 uses retained memory from Memory Lifetime and Management and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M15-Q023

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** Calculation for schedulers, event loops, and tasks, report 930/1000 = 93.0% against the same equivalent-work denominator.

**Explanation:** M15-Q023 uses success denominator from Schedulers, Event Loops, and Tasks and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M15-Q024

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** Calculation for bounded fan-out and structured cleanup, 12 - 8 = 4 tasks wait before any scheduling overhead.

**Explanation:** M15-Q024 uses runtime slots from Bounded Fan-out and Structured Cleanup and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M15-Q025

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** Diagnosis for memory lifetime and management, cancellation.joined and invariants.2.passed separate the mechanism. cancellation.joined = 1 while invariants.2.passed = 0, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare cancellation.joined with invariants.2.passed and connect that contrast to memory lifetime and management.

**Grading notes:** Full credit names Memory Lifetime and Management, cites cancellation.joined and invariants.2.passed, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M15-Q026

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** Diagnosis for schedulers, event loops, and tasks, cancellation.propagated and invariants.2.passed separate the mechanism. cancellation.propagated = 1 while invariants.2.passed = 0, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare cancellation.propagated with invariants.2.passed and connect that contrast to schedulers, event loops, and tasks.

**Grading notes:** Full credit names Schedulers, Event Loops, and Tasks, cites cancellation.propagated and invariants.2.passed, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M15-Q027

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** Diagnosis for bounded fan-out and structured cleanup, invariants.0.passed and invariants.2.passed separate the mechanism. invariants.0.passed = 1 while invariants.2.passed = 0, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare invariants.0.passed with invariants.2.passed and connect that contrast to bounded fan-out and structured cleanup.

**Grading notes:** Full credit names Bounded Fan-out and Structured Cleanup, cites invariants.0.passed and invariants.2.passed, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M15-Q028

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** Diagnosis for memory visibility and races, invariants.1.passed and invariants.2.passed separate the mechanism. invariants.1.passed = 1 while invariants.2.passed = 0, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare invariants.1.passed with invariants.2.passed and connect that contrast to memory visibility and races.

**Grading notes:** Full credit names Memory Visibility and Races, cites invariants.1.passed and invariants.2.passed, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M15-Q029

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** Diagnosis for types, serialization, and validation, invariants.2.passed and memory.bounded separate the mechanism. invariants.2.passed = 0 while memory.bounded = 1, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare invariants.2.passed with memory.bounded and connect that contrast to types, serialization, and validation.

**Grading notes:** Full credit names Types, Serialization, and Validation, cites invariants.2.passed and memory.bounded, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M15-Q030

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** Diagnosis for equivalent-work runtime measurement, cancellation.joined and invariants.2.passed separate the mechanism. cancellation.joined = 1 while invariants.2.passed = 0, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare cancellation.joined with invariants.2.passed and connect that contrast to equivalent-work runtime measurement.

**Grading notes:** Full credit names Equivalent-work Runtime Measurement, cites cancellation.joined and invariants.2.passed, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M15-Q031

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** Diagnosis for northstar polyglot fan-out tutorial, cancellation.propagated and invariants.2.passed separate the mechanism. cancellation.propagated = 1 while invariants.2.passed = 0, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare cancellation.propagated with invariants.2.passed and connect that contrast to northstar polyglot fan-out tutorial.

**Grading notes:** Full credit names Northstar Polyglot Fan-out Tutorial, cites cancellation.propagated and invariants.2.passed, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M15-Q032

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** Diagnosis for runtime decision and teach-back, invariants.0.passed and invariants.2.passed separate the mechanism. invariants.0.passed = 1 while invariants.2.passed = 0, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare invariants.0.passed with invariants.2.passed and connect that contrast to runtime decision and teach-back.

**Grading notes:** Full credit names Runtime Decision and Teach-back, cites invariants.0.passed and invariants.2.passed, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M15-Q033

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** Diagnosis for memory lifetime and management, invariants.1.passed and invariants.2.passed separate the mechanism. invariants.1.passed = 1 while invariants.2.passed = 0, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare invariants.1.passed with invariants.2.passed and connect that contrast to memory lifetime and management.

**Grading notes:** Full credit names Memory Lifetime and Management, cites invariants.1.passed and invariants.2.passed, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M15-Q034

**Type:** `design_judgment`
**Difficulty:** `application`

**Answer:** Approve Lifetime inventory at 150/s. The deciding number is 225 x 0.72 = 162/s, leaving 12/s before the reserve is consumed. Withdraw approval if a drill, trace, or workload sample shows lifetime inventory demand above 162/s or proves the shed point cannot protect lower-priority work.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to lifetime inventory demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 162/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M15-Q035

**Type:** `design_judgment`
**Difficulty:** `synthesis`

**Answer:** Decline Allocation calculation at 185.6/s. The deciding number is 242 x 0.72 = 174.2/s, so planned demand exceeds the usable region by 11.4/s. Approve later if repeated measurements lift usable capacity above 185.6/s or a named policy removes at least 11.4/s of deferrable work before saturation.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to allocation calculation demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 174.2/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M15-Q036

**Type:** `design_judgment`
**Difficulty:** `recall`

**Answer:** Approve conditionally for Scheduler placement. The deciding number is 259 x 0.72 = 186.5/s, and 181.5/s fits only while the fallback remains enforceable. Keep the condition until recovery traffic, priority demand, or fallback tests show less than 5/s of usable margin.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to scheduler placement demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 186.5/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M15-Q037

**Type:** `design_judgment`
**Difficulty:** `application`

**Answer:** Approve Bound derivation at 181.6/s. The deciding number is 276 x 0.72 = 198.7/s, leaving 17.1/s before the reserve is consumed. Require redesign if a drill, trace, or workload sample shows bound derivation demand above 198.7/s or proves the shed point cannot protect lower-priority work.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to bound derivation demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 198.7/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M15-Q038

**Type:** `design_judgment`
**Difficulty:** `synthesis`

**Answer:** Decline Request contract at 226.6/s. The deciding number is 293 x 0.72 = 211/s, so planned demand exceeds the usable region by 15.6/s. Lift the decline if repeated measurements lift usable capacity above 226.6/s or a named policy removes at least 15.6/s of deferrable work before saturation.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to request contract demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 211/s, compares it with planned demand, and names a scenario-specific reversal condition.
