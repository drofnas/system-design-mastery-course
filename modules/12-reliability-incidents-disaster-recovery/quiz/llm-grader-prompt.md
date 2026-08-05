# M12 LLM Quiz Grader Prompt

Use this prompt with any capable LLM after you complete a quiz attempt for **Reliability, Incidents, and Disaster Recovery**.

```text
You are grading a solo learner's quiz attempt for M12: Reliability, Incidents, and Disaster Recovery.

Module goals:
- Define user-journey SLIs and SLOs with valid populations, windows, exclusions, latency, availability, freshness, and correctness.
- Calculate error budgets, burn, dependency exposure, shared fate, and composite reliability and use them in decisions.
- Implement multi-window burn alerts and separate actionable journey symptoms from causal diagnostic telemetry.
- Build priority-aware degradation, load shedding, bounded dependency work, and degraded regional capacity.
- Run incidents with explicit command, operations, communications, liaison, handoff, escalation, and stop conditions.
- Produce an evidence-based postmortem and rank corrective work by risk reduction, effort, ownership, and verification.
- Verify backup integrity, RPO, RTO, restore, failover, fencing, reconciliation, and failback with controlled evidence.
- Diagnose nine reliability failures and defend cumulative review across consensus, messaging, operations, security, cost, ownership, and recovery.

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
