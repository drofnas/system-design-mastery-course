# Module 12: Reliability, Incidents, and Disaster Recovery

## Purpose

Define user-journey SLIs and SLOs with valid populations, windows, exclusions, latency, availability, freshness, and correctness.

This module is part of the solo Computer Science and System Design Mastery path. Study the local lessons first, reinforce the mechanisms with practice and labs, then use the quiz package to test recall, application, diagnosis, and design judgment.

## Prerequisites

- Familiarity with Modules 1-11, or willingness to review earlier lessons as needed.
- Python 3.11 or newer for the quiz tooling and most reinforcement labs.
- Comfort reading technical documentation, code snippets, diagrams, and answer explanations.

## Learning Outcomes

1. Define user-journey SLIs and SLOs with valid populations, windows, exclusions, latency, availability, freshness, and correctness.
2. Calculate error budgets, burn, dependency exposure, shared fate, and composite reliability and use them in decisions.
3. Implement multi-window burn alerts and separate actionable journey symptoms from causal diagnostic telemetry.
4. Build priority-aware degradation, load shedding, bounded dependency work, and degraded regional capacity.
5. Run incidents with explicit command, operations, communications, liaison, handoff, escalation, and stop conditions.
6. Produce an evidence-based postmortem and rank corrective work by risk reduction, effort, ownership, and verification.
7. Verify backup integrity, RPO, RTO, restore, failover, fencing, reconciliation, and failback with controlled evidence.
8. Diagnose nine reliability failures and defend cumulative review across consensus, messaging, operations, security, cost, ownership, and recovery.

## Learn

1. [User Journeys, SLIs, and SLOs](lessons/01-user-journeys-slis-slos.md)
2. [Error Budgets, Dependencies, and Composite Reliability](lessons/02-error-budgets-dependencies.md)
3. [Burn Rates and Actionable Alerting](lessons/03-burn-rates-actionable-alerting.md)
4. [Graceful Degradation and Degraded Capacity](lessons/04-graceful-degradation-capacity.md)
5. [Incident Command, Communication, and Runbooks](lessons/05-incident-command-runbooks.md)
6. [Postmortems and Corrective Work](lessons/06-postmortems-corrective-work.md)
7. [Backups, Restore, Failover, and Failback](lessons/07-backups-restore-failover.md)
8. [Chaos, Game Days, and Reliability Decisions](lessons/08-game-days-reliability-decisions.md)

- Glossary: [glossary.md](glossary.md).

## Practice And Lab

- Guided exercises: [exercises/exercises.md](exercises/exercises.md).
- Explained practice answers: [exercises/answer-key.md](exercises/answer-key.md).
- Reinforcement lab: [lab/README.md](lab/README.md). Use the lab to reinforce the local mechanism; treat expanded matrices and platform-specific evidence as optional deep-dive work.
- Resource guide: [resources.md](resources.md).

## Quiz And Review

- Question bank: [quiz/question-bank.json](quiz/question-bank.json).
- Answer key: [quiz/answer-key.md](quiz/answer-key.md).
- LLM grading prompt: [quiz/llm-grader-prompt.md](quiz/llm-grader-prompt.md).

Generate a 20-question quiz from the repository root:

```bash
python3 scripts/generate_quiz.py --module M12 --count 20 --output quiz-m12.json
```

A module is complete when you can explain the lesson mechanisms, complete the practice, run or reason through the reinforcement lab, and score your quiz attempt with the answer key or LLM grader.

## Optional Project

Apply Reliability, Incidents, and Disaster Recovery to a small system you know. Write a short design note, experiment report, or implementation summary only if you want deeper practice.
