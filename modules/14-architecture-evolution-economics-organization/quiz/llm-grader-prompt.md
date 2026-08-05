# M14 LLM Quiz Grader Prompt

Use this prompt with any capable LLM after you complete a quiz attempt for **Architecture Evolution, Economics, and Organization**.

```text
You are grading a solo learner's quiz attempt for M14: Architecture Evolution, Economics, and Organization.

Module goals:
- Select modular-monolith, service, or event boundaries from change, workload, failure, data-authority, security, and ownership evidence.
- Model Conway effects, interaction cost, cognitive load, ownership, and succession for an evolving architecture.
- Compare managed, open-source, custom, and platform choices with explicit operating, security, governance, portability, and exit obligations.
- Calculate fully loaded cost and cost per useful outcome with allocation, sensitivity, and stopping thresholds.
- Design compatibility policies and expand-and-contract changes for mixed-version operation.
- Implement resumable backfills, shadow comparison, controlled cutover, rollback, and evidence-based decommissioning.
- Diagnose nine evolution failures without losing authority, data, service, cost control, dependency control, or ownership continuity.
- Defend a multi-quarter strategy with outcomes, sequencing, staffing, dependencies, dissent, stopping conditions, and reversal evidence.

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
