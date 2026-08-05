# M03 LLM Quiz Grader Prompt

Use this prompt with any capable LLM after you complete a quiz attempt for **Computer Systems and Operating Systems**.

```text
You are grading a solo learner's quiz attempt for M03: Computer Systems and Operating Systems.

Module goals:
- save a falsifiable benchmark contract with equivalent work, machine boundaries, measurement limits, and production-transfer uncertainty.
- Explain and measure how access patterns, branches, copying, pipelines, and caches shape equivalent application work.
- Relate runnable work, processes, threads, syscalls, context switches, quotas, and oversubscription to useful throughput.
- Diagnose allocation lifetime, page touching, faults, residency, reclaim pressure, and memory-limit outcomes without conflating their counters.
- Implement and safely test lock contention, bounded deadlock, shared-state invariants, and false sharing.
- Distinguish buffered completion, page-cache writeback, device queues, file sync, directory durability, and recoverable acknowledgement.
- Apply unprivileged CPU, memory, PID, and I/O constraints and transfer container evidence with explicit operational limits and owners.
- Defend and teach a systems-performance decision from a counterintuitive result with cost, security, operations, ownership, migration, rollback, and reversal evidence.

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
