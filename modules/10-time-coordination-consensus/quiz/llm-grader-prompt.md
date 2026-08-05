# M10 LLM Quiz Grader Prompt

Use this prompt with any capable LLM after you complete a quiz attempt for **Time, Coordination, and Consensus**.

```text
You are grading a solo learner's quiz attempt for M10: Time, Coordination, and Consensus.

Module goals:
- Calculate physical-clock drift, skew, and uncertainty and diagnose conclusions that exceed the available clock contract.
- Derive happened-before, Lamport-clock, and vector-clock relationships without treating display order as causality.
- Separate safety, liveness, and failure-detector assumptions and select consensus only for properties that require agreement.
- Implement and diagnose Raft elections, persistent hard state, log matching, commitment, and state-machine application.
- Implement client deduplication and linearizable reads with explicit ambiguous-outcome and quorum barriers.
- Protect snapshots, membership changes, leases, and external resources with atomic state, overlapping quorums, and fencing.
- Diagnose eight coordination failures from immutable same-input evidence and scoped safety oracles.
- Defend a coordination architecture covering alternatives, operating limits, security, cost, migration, ownership, dissent, and reversal evidence.

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
