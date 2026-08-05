# M05 LLM Quiz Grader Prompt

Use this prompt with any capable LLM after you complete a quiz attempt for **Network Foundations**.

```text
You are grading a solo learner's quiz attempt for M05: Network Foundations.

Module goals:
- Model a client journey as a layered path with round-trip, byte, bandwidth-delay-product, and tail-latency budgets.
- Trace DNS resolution, addressing, routing, caching, and discovery with explicit authority, expiry, and failure boundaries.
- Relate TCP ordering, loss recovery, flow control, congestion control, and receiver behavior to measured goodput and tail latency.
- Trace TLS authentication and handshake costs while preserving hostname, certificate, key, resumption, and trust boundaries.
- Diagnose proxy, load-balancer, NAT, connection-pool, and slow-reader behavior with capacity, ownership, and cost evidence.
- Compare HTTP/1.1, HTTP/2, and HTTP/3 through setup, multiplexing, stream isolation, fallback, observability, and client-network constraints.
- Diagnose nine hidden network faults from preserved evidence before reveal and design reruns that separate credible causes.
- Defend a protocol and topology decision through client outcomes, security, cost, ownership, migration, rollback, and reversal conditions.

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
