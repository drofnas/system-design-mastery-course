# Module 2: Capacity, Queues, and Tail Latency

## Purpose

Model logical work, attempts, operation mix, normal, peak, burst, projected, skewed, and recovery demand with visible uncertainty.

This module is part of the solo Computer Science and System Design Mastery path. Study the local lessons first, reinforce the mechanisms with practice and labs, then use the quiz package to test recall, application, diagnosis, and design judgment.

## Prerequisites

- Familiarity with Modules 1-1, or willingness to review earlier lessons as needed.
- Python 3.11 or newer for the quiz tooling and most reinforcement labs.
- Comfort reading technical documentation, code snippets, diagrams, and answer explanations.

## Learning Outcomes

1. Model logical work, attempts, operation mix, normal, peak, burst, projected, skewed, and recovery demand with visible uncertainty.
2. Calculate concurrency, per-resource service demand, nominal capacity, and failover exposure using consistent boundaries.
3. Implement and test fixed workers, explicit bounded waiting, fan-out, downstream admission, logical identities, and timing instrumentation.
4. Design an open-loop latency experiment that exposes coordinated omission, generator limits, rejection, and uncertainty.
5. Predict and measure fan-out tail amplification, downstream branch demand, and correlation limits.
6. Locate saturation from useful throughput, latency, queue, rejection, concurrency, and generator evidence across the required load sweep.
7. Keep overload, priority, retries, downstream work, and recovery bounded under burst and dependency failure.
8. Defend a workload-scoped safe operating region, actionable scaling signal, overload policy, failover reserve, ownership model, and cost per useful request.

## Learn

1. [Workload and Useful Work](lessons/01-workload-and-useful-work.md)
2. [Little’s Law and Saturation](lessons/02-littles-law-and-saturation.md)
3. [Latency Measurement](lessons/03-latency-measurement.md)
4. [Fan-out and Tail Amplification](lessons/04-fanout-and-tail-amplification.md)
5. [Bounded Overload Control](lessons/05-bounded-overload-control.md)
6. [Retries and Downstream Protection](lessons/06-retries-and-downstream-protection.md)
7. [Failover Headroom and Unit Cost](lessons/07-failover-headroom-and-unit-cost.md)
8. [Capacity Decisions and Defense](lessons/08-capacity-decisions-and-defense.md)

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
python3 scripts/generate_quiz.py --module M02 --count 20 --output quiz-m02.json
```

A module is complete when you can explain the lesson mechanisms, complete the practice, run or reason through the reinforcement lab, and score your quiz attempt with the answer key or LLM grader.

## Optional Project

Apply Capacity, Queues, and Tail Latency to a small system you know. Write a short design note, experiment report, or implementation summary only if you want deeper practice.
