# M15 LLM Quiz Grader Prompt

Use this prompt with any capable LLM after you complete a quiz attempt for **Execution Models Across Languages**.

```text
You are grading a solo learner's quiz attempt for M15: Execution Models Across Languages.

Module goals:
- Explain and compare stack, heap, allocation, escape, manual lifetime, RAII, ownership, reference counting, and tracing collection from workload evidence.
- Trace work through operating-system threads, event loops, worker pools, goroutines, async tasks, virtual threads, and runtime schedulers.
- Implement the same bounded fan-out contract in TypeScript, Go, Rust, and Java with bounded admission, deadlines, cancellation, validation, and cleanup.
- Measure latency, useful throughput, queueing, memory, allocation, and garbage collection under equivalent work without treating host noise as a language property.
- Diagnose memory-visibility and data-race failures with happens-before reasoning, detector evidence, and explicit detector limits.
- Preserve contracts across static, dynamic, process, and serialization boundaries through explicit validation and scoped authority.
- Diagnose nine execution-model failures while bounding operational, security, cost, migration, and ownership consequences.
- Defend and teach a runtime choice from workload behavior, safety, operability, ecosystem, cost, migration, ownership, and team evidence.

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
