# M06 LLM Quiz Grader Prompt

Use this prompt with any capable LLM after you complete a quiz attempt for **Deadlines and Resilient Remote Calls**.

```text
You are grading a solo learner's quiz attempt for M06: Deadlines and Resilient Remote Calls.

Module goals:
- Allocate and propagate an end-to-end deadline through serial and parallel work with response and cleanup reserves.
- Prove cancellation stops queued, active, and child work within a declared bound.
- Classify retry eligibility and enforce bounded randomized retries using attempt and cost budgets.
- Make ambiguous remote outcomes safe using scoped idempotency records, atomic effects, and deduplication retention.
- Bound fan-out, pools, tenants, and health traffic with explicit admission, fairness, and overload behavior.
- Compare breakers, hedges, partial results, and fail-fast behavior by failure model and useful-work economics.
- Diagnose and repair retry storm, pool exhaustion, slowdown, partial response, duplicate effect, and cancellation leak from preserved evidence.
- Defend a remote-call policy through user outcomes, security, cost, ownership, exceptions, migration, rollback, and reversal evidence.

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
