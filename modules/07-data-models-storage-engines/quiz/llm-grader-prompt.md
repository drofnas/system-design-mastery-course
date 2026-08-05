# M07 LLM Quiz Grader Prompt

Use this prompt with any capable LLM after you complete a quiz attempt for **Data Models and Storage Engines**.

```text
You are grading a solo learner's quiz attempt for M07: Data Models and Storage Engines.

Module goals:
- Derive logical and physical data models from quantified access paths, invariants, retention, growth, and ownership.
- Explain and measure how pages, records, buffer pools, locality, and cache policy shape physical work.
- Implement and validate a persistent paged B+ tree with point lookup, range scan, splits, cache behavior, deletion, and clean reopen.
- Implement and validate an LSM store with memtable, SSTables, sparse indexes, Bloom filters, tombstones, and compaction.
- Calculate read, write, and space amplification and connect them to tail latency, capacity, cost, and SSD endurance.
- Choose indexes and diagnose query plans whose estimates, statistics, or access paths do not match the workload.
- Diagnose read, write, range, skew, delete, cache, Bloom, compaction, and tombstone behavior from preserved same-input evidence.
- Defend a storage-engine decision covering security, operations, cost, ownership, migration, rollback, recovery requirements, and reversal evidence.

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
