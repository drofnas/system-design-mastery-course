# M02 Quiz Answer Key

This key covers all 100 questions for **Capacity, Queues, and Tail Latency**. Use it after an attempt, or provide it with the LLM grading prompt for feedback.

## M02-Q001

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to model logical work, attempts, operation mix, normal, peak, burst, projected, skewed, and recovery demand with visible uncertainty.

**Explanation:** A capacity model begins with work crossing a named boundary. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M02-Q002

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Little’s Law and Saturation', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** For a stable long-run boundary: text L = λW L is average work in the boundary, λ is the rate that enters and eventually leaves that boundary, and W is average time in it.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M02-Q003

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. You can design an open-loop latency experiment, identify coordinated omission, report generator error, and interpret percentile evidence with scope.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M02-Q004

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Multiply branch p99 by fan-out:** parallel maximum is not a sequential sum.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M02-Q005

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for predict and measure fan-out tail amplification, downstream branch demand, and correlation limits..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - Google SRE, Addressing Cascading Failureshttps://sre.google/sre-book/addressing-cascading-failures/ - David Yanacek, Avoiding Insurmountable Queue Backlogshttps://aws.amazon.com/builders-library/avoiding-insurmountable-queue-backlogs/ Complete EX-07 and EX-0

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M02-Q006

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to locate saturation from useful throughput, latency, queue, rejection, concurrency, and generator evidence across the load sweep.

**Explanation:** A retry is additional load created during a failure. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M02-Q007

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Failover Headroom and Unit Cost', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Normal-state success does not prove failover safety.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M02-Q008

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. You can turn predictions and experiments into a scoped capacity decision with a safe region, scaling signal, overload policy, owners, rollout, and reversal conditions.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M02-Q009

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Start from host count:** host count is supply, not demand.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M02-Q010

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for calculate concurrency, per-resource service demand, nominal capacity, and failover exposure using consistent boundaries..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - MIT OpenCourseWare, Queueing Systems lecture noteshttps://ocw.mit.edu/courses/1-203j-logistical-and-transportation-planning-methods-fall-2006/resources/lec5/ - Julius Plenz, How to Trade off Server Utilization and Tail Latencyhttps://www.usenix.org/conferenc

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M02-Q011

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to implement and test fixed workers, explicit bounded waiting, fan-out, downstream admission, logical identities, and timing instrumentation.

**Explanation:** A latency distribution needs: - population and operation - start and stop boundary - workload and environment - observation window and sample count - warm-up and repetitions - treatment of timeouts, rejection, and missing observations - measurement location an The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M02-Q012

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Fan-out and Tail Amplification', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** If one branch completes within threshold t with probability Ft, and n parallel branches are independent, a request that waits for all branches completes within t with probability: text Pmax branch ≤ t = Ft^n Pany branch t = 1 - Ft^n For a branch-tail probabili

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M02-Q013

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. You can locate every place work waits, choose explicit queue and concurrency bounds, and define admission, priority, degradation, and recovery behavior.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M02-Q014

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Retry every error:** permanent and overload errors consume more capacity.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M02-Q015

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for keep overload, priority, retries, downstream work, and recovery bounded under burst and dependency failure..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - David Yanacek, Avoiding Insurmountable Queue Backlogshttps://aws.amazon.com/builders-library/avoiding-insurmountable-queue-backlogs/ - Julius Plenz, How to Trade off Server Utilization and Tail Latencyhttps://www.usenix.org/conference/srecon19asia/presentati

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M02-Q016

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to defend a workload-scoped safe operating region, actionable scaling signal, overload policy, failover reserve, ownership model, and cost per useful request.

**Explanation:** A capacity report is a decision artifact, not a benchmark dump. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M02-Q017

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Workload and Useful Work', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** A capacity model begins with work crossing a named boundary.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M02-Q018

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. You can apply Little’s Law to consistent boundaries, calculate service-demand limits, distinguish utilization from latency, and state the limits of the model.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M02-Q019

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Report only averages:** a small slow population can dominate user journeys.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M02-Q020

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for design an open-loop latency experiment that exposes coordinated omission, generator limits, rejection, and uncertainty..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - Jeffrey Dean and Luiz André Barroso, The Tail at Scalehttps://research.google/pubs/the-tail-at-scale/ Complete EX-06 and run the Transit baseline before Lesson 5.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M02-Q021

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to predict and measure fan-out tail amplification, downstream branch demand, and correlation limits.

**Explanation:** When arrivals exceed completions, one of four things happens: 1. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M02-Q022

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Retries and Downstream Protection', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** A retry is additional load created during a failure.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M02-Q023

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. You can calculate degraded-state capacity, backlog clearance, and cost per useful request, then run sensitivity without declaring a universal utilization target.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M02-Q024

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Select the prettiest chart:** a decision needs falsifying and failure

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M02-Q025

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for model logical work, attempts, operation mix, normal, peak, burst, projected, skewed, and recovery demand with visible uncertainty..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - MIT OpenCourseWare, Queueing Systems lecture noteshttps://ocw.mit.edu/courses/1-203j-logistical-and-transportation-planning-methods-fall-2006/resources/lec5/ - Google SRE, Addressing Cascading Failureshttps://sre.google/sre-book/addressing-cascading-failures

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M02-Q026

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to calculate concurrency, per-resource service demand, nominal capacity, and failover exposure using consistent boundaries.

**Explanation:** For a stable long-run boundary: text L = λW L is average work in the boundary, λ is the rate that enters and eventually leaves that boundary, and W is average time in it. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M02-Q027

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Latency Measurement', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** A latency distribution needs: - population and operation - start and stop boundary - workload and environment - observation window and sample count - warm-up and repetitions - treatment of timeouts, rejection, and missing observations - measurement location an

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M02-Q028

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. You can derive the probability of at least one slow branch, connect branch service demand to journey latency, and state when independence assumptions fail.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M02-Q029

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Treat a queue as capacity:** it changes when work fails, not how fast work

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M02-Q030

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for locate saturation from useful throughput, latency, queue, rejection, concurrency, and generator evidence across the load sweep..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - Google SRE, Addressing Cascading Failureshttps://sre.google/sre-book/addressing-cascading-failures/ - Marc Brooker, Timeouts, retries, and backoff with jitterhttps://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/ Complete EX-09, th

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M02-Q031

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to keep overload, priority, retries, downstream work, and recovery bounded under burst and dependency failure.

**Explanation:** Normal-state success does not prove failover safety. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M02-Q032

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Capacity Decisions and Defense', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** A capacity report is a decision artifact, not a benchmark dump.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M02-Q033

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. You can define a workload boundary, distinguish logical work from attempts, and model normal, peak, burst, projected, and skewed demand with visible uncertainty.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M02-Q034

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Combine different boundaries:** server concurrency with client end-to-end

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M02-Q035

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for implement and test fixed workers, explicit bounded waiting, fan-out, downstream admission, logical identities, and timing instrumentation..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - HdrHistogram maintainers, Corrected vs.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M02-Q036

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to design an open-loop latency experiment that exposes coordinated omission, generator limits, rejection, and uncertainty.

**Explanation:** If one branch completes within threshold t with probability Ft, and n parallel branches are independent, a request that waits for all branches completes within t with probability: text Pmax branch ≤ t = Ft^n Pany branch t = 1 - Ft^n For a branch-tail probabili The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M02-Q037

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Bounded Overload Control', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** When arrivals exceed completions, one of four things happens: 1.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M02-Q038

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. You can calculate retry amplification, define local and shared retry bounds, and protect a smaller downstream with deadlines, concurrency, and admission.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M02-Q039

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Reserve capacity only at the first tier:** a shared downstream still fails.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M02-Q040

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for defend a workload-scoped safe operating region, actionable scaling signal, overload policy, failover reserve, ownership model, and cost per useful request..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - Google SRE, Addressing Cascading Failureshttps://sre.google/sre-book/addressing-cascading-failures/ - Google Research, The Tail at Scalehttps://research.google/pubs/the-tail-at-scale/ Complete EX-12, the capacity report, ADR, and defense.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M02-Q041

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to model logical work, attempts, operation mix, normal, peak, burst, projected, skewed, and recovery demand with visible uncertainty.

**Explanation:** A capacity model begins with work crossing a named boundary. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M02-Q042

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Little’s Law and Saturation', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** For a stable long-run boundary: text L = λW L is average work in the boundary, λ is the rate that enters and eventually leaves that boundary, and W is average time in it.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M02-Q043

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. You can design an open-loop latency experiment, identify coordinated omission, report generator error, and interpret percentile evidence with scope.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M02-Q044

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Multiply branch p99 by fan-out:** parallel maximum is not a sequential sum.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M02-Q045

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for predict and measure fan-out tail amplification, downstream branch demand, and correlation limits..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - Google SRE, Addressing Cascading Failureshttps://sre.google/sre-book/addressing-cascading-failures/ - David Yanacek, Avoiding Insurmountable Queue Backlogshttps://aws.amazon.com/builders-library/avoiding-insurmountable-queue-backlogs/ Complete EX-07 and EX-0

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M02-Q046

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to locate saturation from useful throughput, latency, queue, rejection, concurrency, and generator evidence across the load sweep.

**Explanation:** A retry is additional load created during a failure. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M02-Q047

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Failover Headroom and Unit Cost', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Normal-state success does not prove failover safety.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M02-Q048

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. You can turn predictions and experiments into a scoped capacity decision with a safe region, scaling signal, overload policy, owners, rollout, and reversal conditions.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M02-Q049

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Start from host count:** host count is supply, not demand.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M02-Q050

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for calculate concurrency, per-resource service demand, nominal capacity, and failover exposure using consistent boundaries..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - MIT OpenCourseWare, Queueing Systems lecture noteshttps://ocw.mit.edu/courses/1-203j-logistical-and-transportation-planning-methods-fall-2006/resources/lec5/ - Julius Plenz, How to Trade off Server Utilization and Tail Latencyhttps://www.usenix.org/conferenc

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M02-Q051

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to implement and test fixed workers, explicit bounded waiting, fan-out, downstream admission, logical identities, and timing instrumentation.

**Explanation:** A latency distribution needs: - population and operation - start and stop boundary - workload and environment - observation window and sample count - warm-up and repetitions - treatment of timeouts, rejection, and missing observations - measurement location an The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M02-Q052

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Fan-out and Tail Amplification', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** If one branch completes within threshold t with probability Ft, and n parallel branches are independent, a request that waits for all branches completes within t with probability: text Pmax branch ≤ t = Ft^n Pany branch t = 1 - Ft^n For a branch-tail probabili

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M02-Q053

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. You can locate every place work waits, choose explicit queue and concurrency bounds, and define admission, priority, degradation, and recovery behavior.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M02-Q054

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Retry every error:** permanent and overload errors consume more capacity.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M02-Q055

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for keep overload, priority, retries, downstream work, and recovery bounded under burst and dependency failure..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - David Yanacek, Avoiding Insurmountable Queue Backlogshttps://aws.amazon.com/builders-library/avoiding-insurmountable-queue-backlogs/ - Julius Plenz, How to Trade off Server Utilization and Tail Latencyhttps://www.usenix.org/conference/srecon19asia/presentati

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M02-Q056

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to defend a workload-scoped safe operating region, actionable scaling signal, overload policy, failover reserve, ownership model, and cost per useful request.

**Explanation:** A capacity report is a decision artifact, not a benchmark dump. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M02-Q057

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Workload and Useful Work', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** A capacity model begins with work crossing a named boundary.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M02-Q058

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. You can apply Little’s Law to consistent boundaries, calculate service-demand limits, distinguish utilization from latency, and state the limits of the model.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M02-Q059

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Report only averages:** a small slow population can dominate user journeys.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M02-Q060

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for design an open-loop latency experiment that exposes coordinated omission, generator limits, rejection, and uncertainty..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - Jeffrey Dean and Luiz André Barroso, The Tail at Scalehttps://research.google/pubs/the-tail-at-scale/ Complete EX-06 and run the Transit baseline before Lesson 5.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M02-Q061

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to predict and measure fan-out tail amplification, downstream branch demand, and correlation limits.

**Explanation:** When arrivals exceed completions, one of four things happens: 1. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M02-Q062

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Retries and Downstream Protection', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** A retry is additional load created during a failure.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M02-Q063

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. You can calculate degraded-state capacity, backlog clearance, and cost per useful request, then run sensitivity without declaring a universal utilization target.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M02-Q064

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Select the prettiest chart:** a decision needs falsifying and failure

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M02-Q065

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for model logical work, attempts, operation mix, normal, peak, burst, projected, skewed, and recovery demand with visible uncertainty..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - MIT OpenCourseWare, Queueing Systems lecture noteshttps://ocw.mit.edu/courses/1-203j-logistical-and-transportation-planning-methods-fall-2006/resources/lec5/ - Google SRE, Addressing Cascading Failureshttps://sre.google/sre-book/addressing-cascading-failures

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M02-Q066

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to calculate concurrency, per-resource service demand, nominal capacity, and failover exposure using consistent boundaries.

**Explanation:** For a stable long-run boundary: text L = λW L is average work in the boundary, λ is the rate that enters and eventually leaves that boundary, and W is average time in it. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M02-Q067

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Latency Measurement', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** A latency distribution needs: - population and operation - start and stop boundary - workload and environment - observation window and sample count - warm-up and repetitions - treatment of timeouts, rejection, and missing observations - measurement location an

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M02-Q068

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. You can derive the probability of at least one slow branch, connect branch service demand to journey latency, and state when independence assumptions fail.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M02-Q069

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Treat a queue as capacity:** it changes when work fails, not how fast work

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M02-Q070

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for locate saturation from useful throughput, latency, queue, rejection, concurrency, and generator evidence across the load sweep..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - Google SRE, Addressing Cascading Failureshttps://sre.google/sre-book/addressing-cascading-failures/ - Marc Brooker, Timeouts, retries, and backoff with jitterhttps://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/ Complete EX-09, th

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M02-Q071

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to keep overload, priority, retries, downstream work, and recovery bounded under burst and dependency failure.

**Explanation:** Normal-state success does not prove failover safety. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M02-Q072

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Capacity Decisions and Defense', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** A capacity report is a decision artifact, not a benchmark dump.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M02-Q073

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. You can define a workload boundary, distinguish logical work from attempts, and model normal, peak, burst, projected, and skewed demand with visible uncertainty.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M02-Q074

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Combine different boundaries:** server concurrency with client end-to-end

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M02-Q075

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for implement and test fixed workers, explicit bounded waiting, fan-out, downstream admission, logical identities, and timing instrumentation..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - HdrHistogram maintainers, Corrected vs.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M02-Q076

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to design an open-loop latency experiment that exposes coordinated omission, generator limits, rejection, and uncertainty.

**Explanation:** If one branch completes within threshold t with probability Ft, and n parallel branches are independent, a request that waits for all branches completes within t with probability: text Pmax branch ≤ t = Ft^n Pany branch t = 1 - Ft^n For a branch-tail probabili The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M02-Q077

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Bounded Overload Control', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** When arrivals exceed completions, one of four things happens: 1.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M02-Q078

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. You can calculate retry amplification, define local and shared retry bounds, and protect a smaller downstream with deadlines, concurrency, and admission.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M02-Q079

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Reserve capacity only at the first tier:** a shared downstream still fails.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M02-Q080

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for defend a workload-scoped safe operating region, actionable scaling signal, overload policy, failover reserve, ownership model, and cost per useful request..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - Google SRE, Addressing Cascading Failureshttps://sre.google/sre-book/addressing-cascading-failures/ - Google Research, The Tail at Scalehttps://research.google/pubs/the-tail-at-scale/ Complete EX-12, the capacity report, ADR, and defense.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M02-Q081

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to model logical work, attempts, operation mix, normal, peak, burst, projected, skewed, and recovery demand with visible uncertainty.

**Explanation:** A capacity model begins with work crossing a named boundary. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M02-Q082

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Little’s Law and Saturation', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** For a stable long-run boundary: text L = λW L is average work in the boundary, λ is the rate that enters and eventually leaves that boundary, and W is average time in it.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M02-Q083

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. You can design an open-loop latency experiment, identify coordinated omission, report generator error, and interpret percentile evidence with scope.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M02-Q084

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Multiply branch p99 by fan-out:** parallel maximum is not a sequential sum.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M02-Q085

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for predict and measure fan-out tail amplification, downstream branch demand, and correlation limits..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - Google SRE, Addressing Cascading Failureshttps://sre.google/sre-book/addressing-cascading-failures/ - David Yanacek, Avoiding Insurmountable Queue Backlogshttps://aws.amazon.com/builders-library/avoiding-insurmountable-queue-backlogs/ Complete EX-07 and EX-0

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M02-Q086

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to locate saturation from useful throughput, latency, queue, rejection, concurrency, and generator evidence across the load sweep.

**Explanation:** A retry is additional load created during a failure. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M02-Q087

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Failover Headroom and Unit Cost', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Normal-state success does not prove failover safety.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M02-Q088

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. You can turn predictions and experiments into a scoped capacity decision with a safe region, scaling signal, overload policy, owners, rollout, and reversal conditions.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M02-Q089

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Start from host count:** host count is supply, not demand.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M02-Q090

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for calculate concurrency, per-resource service demand, nominal capacity, and failover exposure using consistent boundaries..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - MIT OpenCourseWare, Queueing Systems lecture noteshttps://ocw.mit.edu/courses/1-203j-logistical-and-transportation-planning-methods-fall-2006/resources/lec5/ - Julius Plenz, How to Trade off Server Utilization and Tail Latencyhttps://www.usenix.org/conferenc

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M02-Q091

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to implement and test fixed workers, explicit bounded waiting, fan-out, downstream admission, logical identities, and timing instrumentation.

**Explanation:** A latency distribution needs: - population and operation - start and stop boundary - workload and environment - observation window and sample count - warm-up and repetitions - treatment of timeouts, rejection, and missing observations - measurement location an The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M02-Q092

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Fan-out and Tail Amplification', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** If one branch completes within threshold t with probability Ft, and n parallel branches are independent, a request that waits for all branches completes within t with probability: text Pmax branch ≤ t = Ft^n Pany branch t = 1 - Ft^n For a branch-tail probabili

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M02-Q093

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. You can locate every place work waits, choose explicit queue and concurrency bounds, and define admission, priority, degradation, and recovery behavior.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M02-Q094

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Retry every error:** permanent and overload errors consume more capacity.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M02-Q095

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for keep overload, priority, retries, downstream work, and recovery bounded under burst and dependency failure..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - David Yanacek, Avoiding Insurmountable Queue Backlogshttps://aws.amazon.com/builders-library/avoiding-insurmountable-queue-backlogs/ - Julius Plenz, How to Trade off Server Utilization and Tail Latencyhttps://www.usenix.org/conference/srecon19asia/presentati

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M02-Q096

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to defend a workload-scoped safe operating region, actionable scaling signal, overload policy, failover reserve, ownership model, and cost per useful request.

**Explanation:** A capacity report is a decision artifact, not a benchmark dump. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M02-Q097

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Workload and Useful Work', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** A capacity model begins with work crossing a named boundary.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M02-Q098

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. You can apply Little’s Law to consistent boundaries, calculate service-demand limits, distinguish utilization from latency, and state the limits of the model.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M02-Q099

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Report only averages:** a small slow population can dominate user journeys.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M02-Q100

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for design an open-loop latency experiment that exposes coordinated omission, generator limits, rejection, and uncertainty..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - Jeffrey Dean and Luiz André Barroso, The Tail at Scalehttps://research.google/pubs/the-tail-at-scale/ Complete EX-06 and run the Transit baseline before Lesson 5.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.
