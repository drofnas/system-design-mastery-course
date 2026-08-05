# M11 LLM Quiz Grader Prompt

Use this prompt with any capable LLM after you complete a quiz attempt for **Messaging, Streams, and Workflows**.

```text
You are grading a solo learner's quiz attempt for M11: Messaging, Streams, and Workflows.

Module goals:
- Separate authoritative facts, commands, events, queues, logs, streams, and derived state, with explicit owners and rebuild contracts.
- Derive delivery failure windows, stable identities, ordering scope, and defensible exactly-once boundaries.
- Select partition keys and consumer-group topology from workload, fairness, and per-aggregate invariants.
- Implement an atomic outbox, stable envelope, publisher, idempotent inbox, derived view, and CDC checkpoint boundary.
- Design safe replay, poison handling, schema evolution, derived-state rebuild, and reconciliation.
- Model durable workflows, orchestration or choreography, idempotent compensation, and explicit points of no return.
- Calculate lag and drain time and apply explicit event-time, watermark, late-data, backpressure, and recovery policies.
- Diagnose nine asynchronous failures and defend an RFC covering semantics, operations, security, cost, migration, ownership, dissent, and reversal evidence.

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
