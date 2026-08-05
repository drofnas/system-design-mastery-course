# M18 LLM Quiz Grader Prompt

Use this prompt with any capable LLM after you complete a quiz attempt for **Retrieval, RAG, and Agent Systems**.

```text
You are grading a solo learner's quiz attempt for M18: Retrieval, RAG, and Agent Systems.

Module goals:
- Model exact and approximate nearest-neighbor retrieval and tune HNSW from measured recall, visited work, latency, memory, and index cost.
- Build and compare chunked lexical, vector, filtered, hybrid, and reranked retrieval paths using one evaluation set.
- Select retrieval, grounding, refusal, latency, and cost measures that connect to a declared user outcome and release criterion.
- Preserve evidence authorization, exact version, freshness, revocation, claim support, citations, and justified abstention.
- Enforce versioned tool schemas, scoped credentials, deterministic authorization, bound human approval, and secret-free audit outside model output.
- Resume, replay, deduplicate, cancel, compensate, and budget an agent workflow without repeating irreversible side effects.
- Diagnose F01-F08 from immutable equivalent trials and connect each repair to user, security, operating, and cost consequences.
- Synthesize retrieval, agent, product, security, operating, cost, ownership, migration, and reversal tradeoffs.

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
