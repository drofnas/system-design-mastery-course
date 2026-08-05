# M15 Quiz Answer Key

This key covers all 100 questions for **Execution Models Across Languages**. Use it after an attempt, or provide it with the LLM grading prompt for feedback.

## M15-Q001

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to explain and compare stack, heap, allocation, escape, manual lifetime, raii, ownership, reference counting, and tracing collection from workload evidence.

**Explanation:** Use Memory Lifetime and Management to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M15-Q002

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Schedulers, Event Loops, and Tasks', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Schedulers, Event Loops, and Tasks to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M15-Q003

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. Derive admission, deadline, cancellation, and cleanup contracts for child work, then implement them without changing request semantics across runtimes.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M15-Q004

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: Calling a race detector a proof; it observes executed schedules and supported code.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M15-Q005

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for diagnose memory-visibility and data-race failures with happens-before reasoning, detector evidence, and explicit detector limits..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. Use RES-05 and the public schemas.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M15-Q006

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to preserve contracts across static, dynamic, process, and serialization boundaries through explicit validation and scoped authority.

**Explanation:** Use Equivalent-work Runtime Measurement to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M15-Q007

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Northstar Polyglot Fan-out Tutorial', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Northstar Polyglot Fan-out Tutorial to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M15-Q008

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. Choose a runtime from evidence, plan adoption or no-change safely, and teach the method without presenting a language ranking.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M15-Q009

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: Treating heap allocation as inherently slow while ignoring allocation rate,

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M15-Q010

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for trace work through operating-system threads, event loops, worker pools, goroutines, async tasks, virtual threads, and runtime schedulers..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. Use RES-01, RES-04, and RES-07.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M15-Q011

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to implement the same bounded fan-out contract in typescript, go, rust, and java with bounded admission, deadlines, cancellation, validation, and cleanup.

**Explanation:** Use Bounded Fan-out and Structured Cleanup to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M15-Q012

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Memory Visibility and Races', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Memory Visibility and Races to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M15-Q013

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. Compare static/dynamic and nominal/structural typing, then restore guarantees lost at JSON, process, persistence, and authorization boundaries.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M15-Q014

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: Mixing cold compilation/startup with steady request service without labeling it.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M15-Q015

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for diagnose nine execution-model failures while bounding operational, security, cost, migration, and ownership consequences..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. Use the lab reference../lab/README.md and completed case study../case-study/northstar-observation-enrichment.md.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M15-Q016

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to defend and teach a runtime choice from workload behavior, safety, operability, ecosystem, cost, migration, ownership, and team evidence.

**Explanation:** Use Runtime Decision and Teach-back to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M15-Q017

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Memory Lifetime and Management', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Memory Lifetime and Management to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M15-Q018

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. Trace runnable, blocked, queued, and executing work from request to runtime task to OS thread; choose a bound for each finite scheduler.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M15-Q019

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: Using a semaphore after spawning tasks, which bounds execution but not queued

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M15-Q020

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for measure latency, useful throughput, queueing, memory, allocation, and garbage collection under equivalent work without treating host noise as a language property..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. Use RES-02, RES-08, RES-09, and RES-10.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M15-Q021

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to diagnose memory-visibility and data-race failures with happens-before reasoning, detector evidence, and explicit detector limits.

**Explanation:** Use Types, Serialization, and Validation to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M15-Q022

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Equivalent-work Runtime Measurement', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Equivalent-work Runtime Measurement to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M15-Q023

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. Run the reference contract, inspect a visible result in three steps, and trace the same control through TypeScript, Go, Rust, and Java.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M15-Q024

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: Turning one benchmark into a universal “fastest language” claim.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M15-Q025

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for explain and compare stack, heap, allocation, escape, manual lifetime, raii, ownership, reference counting, and tracing collection from workload evidence..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. Use RES-03 and local lab code.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M15-Q026

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to trace work through operating-system threads, event loops, worker pools, goroutines, async tasks, virtual threads, and runtime schedulers.

**Explanation:** Use Schedulers, Event Loops, and Tasks to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M15-Q027

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Bounded Fan-out and Structured Cleanup', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Bounded Fan-out and Structured Cleanup to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M15-Q028

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. Build a happens-before graph, distinguish race freedom from business correctness, and use detectors without overstating their coverage.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M15-Q029

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: Treating a generated type as a wire validator.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M15-Q030

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for preserve contracts across static, dynamic, process, and serialization boundaries through explicit validation and scoped authority..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. Use RES-11, reuse Module 4 measurement rules, and continue to Lesson 707-northstar-polyglot-tutorial.md.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M15-Q031

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to diagnose nine execution-model failures while bounding operational, security, cost, migration, and ownership consequences.

**Explanation:** Use Northstar Polyglot Fan-out Tutorial to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M15-Q032

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Runtime Decision and Teach-back', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Runtime Decision and Teach-back to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M15-Q033

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. Explain stack and heap placement, compare manual release, RAII, ownership, reference counting, and tracing collection, and predict workload-visible costs.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M15-Q034

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: Calling all Node work single-threaded or all Go/Rust/Java work parallel.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M15-Q035

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for implement the same bounded fan-out contract in typescript, go, rust, and java with bounded admission, deadlines, cancellation, validation, and cleanup..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. Revisit Module 6 deadline derivation and continue to Lesson 404-memory-visibility-races.md.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M15-Q036

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to measure latency, useful throughput, queueing, memory, allocation, and garbage collection under equivalent work without treating host noise as a language property.

**Explanation:** Use Memory Visibility and Races to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M15-Q037

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Types, Serialization, and Validation', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Types, Serialization, and Validation to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M15-Q038

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. Design a fair cross-runtime experiment, calculate useful throughput and latency, and distinguish protocol facts from empirical host observations.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M15-Q039

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: Editing Northstar thresholds into the independent commerce build.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M15-Q040

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for defend and teach a runtime choice from workload behavior, safety, operability, ecosystem, cost, migration, ownership, and team evidence..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. Use RES-06 only with its historical boundary.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M15-Q041

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to explain and compare stack, heap, allocation, escape, manual lifetime, raii, ownership, reference counting, and tracing collection from workload evidence.

**Explanation:** Use Memory Lifetime and Management to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M15-Q042

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Schedulers, Event Loops, and Tasks', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Schedulers, Event Loops, and Tasks to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M15-Q043

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. Derive admission, deadline, cancellation, and cleanup contracts for child work, then implement them without changing request semantics across runtimes.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M15-Q044

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: Calling a race detector a proof; it observes executed schedules and supported code.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M15-Q045

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for diagnose memory-visibility and data-race failures with happens-before reasoning, detector evidence, and explicit detector limits..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. Use RES-05 and the public schemas.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M15-Q046

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to preserve contracts across static, dynamic, process, and serialization boundaries through explicit validation and scoped authority.

**Explanation:** Use Equivalent-work Runtime Measurement to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M15-Q047

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Northstar Polyglot Fan-out Tutorial', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Northstar Polyglot Fan-out Tutorial to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M15-Q048

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. Choose a runtime from evidence, plan adoption or no-change safely, and teach the method without presenting a language ranking.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M15-Q049

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: Treating heap allocation as inherently slow while ignoring allocation rate,

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M15-Q050

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for trace work through operating-system threads, event loops, worker pools, goroutines, async tasks, virtual threads, and runtime schedulers..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. Use RES-01, RES-04, and RES-07.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M15-Q051

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to implement the same bounded fan-out contract in typescript, go, rust, and java with bounded admission, deadlines, cancellation, validation, and cleanup.

**Explanation:** Use Bounded Fan-out and Structured Cleanup to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M15-Q052

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Memory Visibility and Races', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Memory Visibility and Races to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M15-Q053

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. Compare static/dynamic and nominal/structural typing, then restore guarantees lost at JSON, process, persistence, and authorization boundaries.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M15-Q054

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: Mixing cold compilation/startup with steady request service without labeling it.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M15-Q055

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for diagnose nine execution-model failures while bounding operational, security, cost, migration, and ownership consequences..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. Use the lab reference../lab/README.md and completed case study../case-study/northstar-observation-enrichment.md.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M15-Q056

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to defend and teach a runtime choice from workload behavior, safety, operability, ecosystem, cost, migration, ownership, and team evidence.

**Explanation:** Use Runtime Decision and Teach-back to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M15-Q057

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Memory Lifetime and Management', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Memory Lifetime and Management to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M15-Q058

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. Trace runnable, blocked, queued, and executing work from request to runtime task to OS thread; choose a bound for each finite scheduler.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M15-Q059

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: Using a semaphore after spawning tasks, which bounds execution but not queued

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M15-Q060

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for measure latency, useful throughput, queueing, memory, allocation, and garbage collection under equivalent work without treating host noise as a language property..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. Use RES-02, RES-08, RES-09, and RES-10.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M15-Q061

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to diagnose memory-visibility and data-race failures with happens-before reasoning, detector evidence, and explicit detector limits.

**Explanation:** Use Types, Serialization, and Validation to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M15-Q062

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Equivalent-work Runtime Measurement', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Equivalent-work Runtime Measurement to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M15-Q063

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. Run the reference contract, inspect a visible result in three steps, and trace the same control through TypeScript, Go, Rust, and Java.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M15-Q064

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: Turning one benchmark into a universal “fastest language” claim.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M15-Q065

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for explain and compare stack, heap, allocation, escape, manual lifetime, raii, ownership, reference counting, and tracing collection from workload evidence..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. Use RES-03 and local lab code.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M15-Q066

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to trace work through operating-system threads, event loops, worker pools, goroutines, async tasks, virtual threads, and runtime schedulers.

**Explanation:** Use Schedulers, Event Loops, and Tasks to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M15-Q067

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Bounded Fan-out and Structured Cleanup', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Bounded Fan-out and Structured Cleanup to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M15-Q068

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. Build a happens-before graph, distinguish race freedom from business correctness, and use detectors without overstating their coverage.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M15-Q069

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: Treating a generated type as a wire validator.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M15-Q070

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for preserve contracts across static, dynamic, process, and serialization boundaries through explicit validation and scoped authority..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. Use RES-11, reuse Module 4 measurement rules, and continue to Lesson 707-northstar-polyglot-tutorial.md.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M15-Q071

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to diagnose nine execution-model failures while bounding operational, security, cost, migration, and ownership consequences.

**Explanation:** Use Northstar Polyglot Fan-out Tutorial to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M15-Q072

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Runtime Decision and Teach-back', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Runtime Decision and Teach-back to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M15-Q073

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. Explain stack and heap placement, compare manual release, RAII, ownership, reference counting, and tracing collection, and predict workload-visible costs.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M15-Q074

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: Calling all Node work single-threaded or all Go/Rust/Java work parallel.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M15-Q075

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for implement the same bounded fan-out contract in typescript, go, rust, and java with bounded admission, deadlines, cancellation, validation, and cleanup..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. Revisit Module 6 deadline derivation and continue to Lesson 404-memory-visibility-races.md.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M15-Q076

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to measure latency, useful throughput, queueing, memory, allocation, and garbage collection under equivalent work without treating host noise as a language property.

**Explanation:** Use Memory Visibility and Races to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M15-Q077

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Types, Serialization, and Validation', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Types, Serialization, and Validation to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M15-Q078

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. Design a fair cross-runtime experiment, calculate useful throughput and latency, and distinguish protocol facts from empirical host observations.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M15-Q079

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: Editing Northstar thresholds into the independent commerce build.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M15-Q080

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for defend and teach a runtime choice from workload behavior, safety, operability, ecosystem, cost, migration, ownership, and team evidence..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. Use RES-06 only with its historical boundary.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M15-Q081

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to explain and compare stack, heap, allocation, escape, manual lifetime, raii, ownership, reference counting, and tracing collection from workload evidence.

**Explanation:** Use Memory Lifetime and Management to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M15-Q082

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Schedulers, Event Loops, and Tasks', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Schedulers, Event Loops, and Tasks to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M15-Q083

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. Derive admission, deadline, cancellation, and cleanup contracts for child work, then implement them without changing request semantics across runtimes.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M15-Q084

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: Calling a race detector a proof; it observes executed schedules and supported code.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M15-Q085

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for diagnose memory-visibility and data-race failures with happens-before reasoning, detector evidence, and explicit detector limits..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. Use RES-05 and the public schemas.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M15-Q086

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to preserve contracts across static, dynamic, process, and serialization boundaries through explicit validation and scoped authority.

**Explanation:** Use Equivalent-work Runtime Measurement to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M15-Q087

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Northstar Polyglot Fan-out Tutorial', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Northstar Polyglot Fan-out Tutorial to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M15-Q088

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. Choose a runtime from evidence, plan adoption or no-change safely, and teach the method without presenting a language ranking.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M15-Q089

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: Treating heap allocation as inherently slow while ignoring allocation rate,

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M15-Q090

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for trace work through operating-system threads, event loops, worker pools, goroutines, async tasks, virtual threads, and runtime schedulers..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. Use RES-01, RES-04, and RES-07.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M15-Q091

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to implement the same bounded fan-out contract in typescript, go, rust, and java with bounded admission, deadlines, cancellation, validation, and cleanup.

**Explanation:** Use Bounded Fan-out and Structured Cleanup to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M15-Q092

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Memory Visibility and Races', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Memory Visibility and Races to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M15-Q093

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. Compare static/dynamic and nominal/structural typing, then restore guarantees lost at JSON, process, persistence, and authorization boundaries.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M15-Q094

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: Mixing cold compilation/startup with steady request service without labeling it.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M15-Q095

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for diagnose nine execution-model failures while bounding operational, security, cost, migration, and ownership consequences..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. Use the lab reference../lab/README.md and completed case study../case-study/northstar-observation-enrichment.md.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M15-Q096

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to defend and teach a runtime choice from workload behavior, safety, operability, ecosystem, cost, migration, ownership, and team evidence.

**Explanation:** Use Runtime Decision and Teach-back to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M15-Q097

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Memory Lifetime and Management', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Memory Lifetime and Management to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M15-Q098

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. Trace runnable, blocked, queued, and executing work from request to runtime task to OS thread; choose a bound for each finite scheduler.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M15-Q099

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: Using a semaphore after spawning tasks, which bounds execution but not queued

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M15-Q100

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for measure latency, useful throughput, queueing, memory, allocation, and garbage collection under equivalent work without treating host noise as a language property..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. Use RES-02, RES-08, RES-09, and RES-10.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.
