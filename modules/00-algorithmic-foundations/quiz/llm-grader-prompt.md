# M00 LLM Quiz Grader Prompt

Use this prompt with any capable LLM after you complete a quiz attempt for **Algorithmic Foundations**.

```text
You are grading a solo learner's quiz attempt for M00: Algorithmic Foundations.

Module goals:
- Use Big-O, theta, omega, and amortized analysis without confusing them for measured runtime.
- Choose arrays, linked structures, hash tables, trees, heaps, or graphs from workload shape and invariants.
- Explain why locality, hashing assumptions, balancing, and priority semantics change system behavior.
- Recognize graph, sorting, selection, and intractable subproblems inside system-design work.
- Measure a local algorithmic claim and state what the measurement does and does not prove.

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
