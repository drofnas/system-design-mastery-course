# M09 LLM Quiz Grader Prompt

Use this prompt with any capable LLM after you complete a quiz attempt for **Replication and Partitioning**.

```text
You are grading a solo learner's quiz attempt for M09: Replication and Partitioning.

Module goals:
- Specify fresh, bounded-stale, read-your-writes, monotonic, causal, and linearizable requirements per operation.
- Compare leader/follower, multi-leader, and leaderless replication with explicit synchronous and asynchronous acknowledgement boundaries.
- Calculate quorum intersections and diagnose failures in membership, durability, concurrent-version, and sloppy-quorum assumptions.
- Implement selectable version metadata, conflict preservation, read repair, and anti-entropy with convergence evidence.
- Compare hash, range, and consistent-hash partitioning using balance, movement, routing, and safe reshard evidence.
- Diagnose replica partition, leader loss, lag, lost acknowledgement, hot key, and reshard failures from immutable same-input evidence.
- Design tenant isolation, regional placement, residency controls, capacity, repair ownership, migration, rollback, and cost.
- Synthesize the module mechanisms across earlier topics and explain the decision tradeoffs from evidence.

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
