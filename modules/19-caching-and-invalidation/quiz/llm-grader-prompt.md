# M19 LLM Quiz Grader Prompt

Use this prompt with any capable LLM after you complete a quiz attempt for **Caching and Invalidation**.

```text
You are grading a solo learner's quiz attempt for M19: Caching and Invalidation.

Module goals:
- Choose cache placement from read/write path, freshness, authority, and failure cost.
- Explain eviction policy behavior and estimate hit-rate economics.
- Design invalidation and coherence rules without hiding stale or private data risks.
- Prevent cache stampedes with request coalescing, jitter, leases, and bounded regeneration.
- Defend a cache policy with ownership, observability, rollback, and abuse controls.

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
