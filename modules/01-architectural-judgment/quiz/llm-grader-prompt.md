# M01 LLM Quiz Grader Prompt

Use this prompt with any capable LLM after you complete a quiz attempt for **Architectural Judgment**.

```text
You are grading a solo learner's quiz attempt for M01: Architectural Judgment.

Module goals:
- Translate an ambiguous product request into users, outcomes, scope, constraints, and measurable acceptance conditions.
- Build a workload model with normal, peak, burst, projected, skew, and uncertainty dimensions.
- Express business, data, security, and operational invariants and assign authoritative state ownership.
- Write measurable quality-attribute scenarios tied to user journeys and evidence collection.
- Communicate system context, boundaries, flows, trust, and ownership without prematurely choosing deployable services.
- Compare simple, moderate, and distributed designs using shared drivers, cost boundaries, evidence, and reversal conditions.
- State a scoped failure and overload model and expose unsupported claims through adversarial review.
- Write and defend an evidence-based RFC, resolve disagreement through decision drivers, and teach the causal model.

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
