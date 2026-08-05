# M04 LLM Quiz Grader Prompt

Use this prompt with any capable LLM after you complete a quiz attempt for **Performance Methodology and Observability**.

```text
You are grading a solo learner's quiz attempt for M04: Performance Methodology and Observability.

Module goals:
- save a user-scoped performance question, equivalent-work baseline, competing hypotheses, falsifiers, and bounded collection plan before inspecting a fault.
- Design controlled, interleaved experiments that expose process and environment variation while preserving useful work and raw samples.
- Propagate safe trace context across a process boundary and correlate request traces, structured logs, metrics, and exemplars.
- Choose metrics and logs with explicit units, purpose, cardinality, overhead, privacy, retention, access, cost, and ownership bounds.
- Use CPU, allocation, lock-wait, dependency-span, local-I/O, and query-plan evidence without overstating profiler or cache boundaries.
- Diagnose CPU work, allocation pressure, lock contention, slow I/O, connection retention, and metric-cardinality faults before reveal, then design discriminating reruns.
- Build a reproducible benchmark and enforce a workload-scoped regression budget with pass, regression, and inconclusive outcomes.
- Defend a performance change through user outcome, causal evidence, validation, telemetry safety and cost, ownership, migration, rollout, rollback, and reversal conditions.

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
