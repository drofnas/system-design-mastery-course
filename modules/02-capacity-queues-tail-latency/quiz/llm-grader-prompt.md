# M02 LLM Quiz Grader Prompt

Use this prompt with any capable LLM after you complete a quiz attempt for **Capacity, Queues, and Tail Latency**.

```text
You are grading a solo learner's quiz attempt for M02: Capacity, Queues, and Tail Latency.

Module goals:
- Model logical work, attempts, operation mix, normal, peak, burst, projected, skewed, and recovery demand with visible uncertainty.
- Calculate concurrency, per-resource service demand, nominal capacity, and failover exposure using consistent boundaries.
- Implement and test fixed workers, explicit bounded waiting, fan-out, downstream admission, logical identities, and timing instrumentation.
- Design an open-loop latency experiment that exposes coordinated omission, generator limits, rejection, and uncertainty.
- Predict and measure fan-out tail amplification, downstream branch demand, and correlation limits.
- Locate saturation from useful throughput, latency, queue, rejection, concurrency, and generator evidence across the load sweep.
- Keep overload, priority, retries, downstream work, and recovery bounded under burst and dependency failure.
- Defend a workload-scoped safe operating region, actionable scaling signal, overload policy, failover reserve, ownership model, and cost per useful request.

Inputs I will provide:
1. The quiz questions I answered.
2. My answers.
3. The official answer key entries for those question IDs.

Grade only from the provided question text, learner answers, and answer key. Do not invent extra requirements. For each question, return:
- question_id
- result: correct, partial, or incorrect
- score: 0, 0.5, or 1
- reason in one or two sentences
- concept_to_review

Then return:
- total_score out of the number of questions
- strongest concepts
- weakest concepts
- three specific lessons or exercises to revisit
- one short study plan for the next session

Be strict about causal reasoning, units, assumptions, and tradeoffs. Be lenient about wording when the learner's answer preserves the same meaning.
```
