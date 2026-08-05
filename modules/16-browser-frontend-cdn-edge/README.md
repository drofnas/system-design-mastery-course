# Module 16: Browser, Frontend, CDN, and Edge Architecture

## Purpose

Trace tasks, microtasks, input dispatch, style, layout, paint, raster, and compositing from browser evidence.

This module is part of the solo Computer Science and System Design Mastery path. Study the local lessons first, reinforce the mechanisms with practice and labs, then use the quiz package to test recall, application, diagnosis, and design judgment.

## Prerequisites

- Familiarity with Modules 1-15, or willingness to review earlier lessons as needed.
- Python 3.11 or newer for the quiz tooling and most reinforcement labs.
- Comfort reading technical documentation, code snippets, diagrams, and answer explanations.

## Learning Outcomes

1. Trace tasks, microtasks, input dispatch, style, layout, paint, raster, and compositing from browser evidence.
2. Calculate route-level performance budgets and interpret controlled-lab and field evidence without conflating them.
3. Select and implement static, server, streaming, client, and island-hydration strategies per route from workload and interaction evidence.
4. Implement HTTP and CDN cache keys, freshness, validation, invalidation, and private-response isolation with explicit authority.
5. Build keyboard-complete, accessible, resilient interactions and explain the boundary between automated and manual evidence.
6. Diagnose long tasks, hydration mismatches, retained browser resources, and third-party failures from controlled evidence.
7. Preserve privacy-aware trace context across browser, edge, and origin while bounding telemetry cost and trust.
8. Defend frontend boundaries, BFF and microfrontend choices, edge consistency, ownership, cost, migration, and reversal conditions.

## Learn

1. [Browser Work and the Rendering Pipeline](lessons/01-browser-work-rendering-pipeline.md)
2. [Performance Budgets and Evidence](lessons/02-performance-budgets-evidence.md)
3. [Route Rendering and Hydration](lessons/03-route-rendering-hydration.md)
4. [HTTP and CDN Cache Safety](lessons/04-http-cdn-cache-safety.md)
5. [Accessibility and Resilient Interaction](lessons/05-accessibility-resilient-interaction.md)
6. [Memory, Third Parties, and Observability](lessons/06-memory-third-parties-observability.md)
7. [Northstar Browser-Edge Tutorial](lessons/07-northstar-browser-edge-tutorial.md)
8. [Frontend-Edge Decision and Teach-Back](lessons/08-frontend-edge-decision-teachback.md)

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
python3 scripts/generate_quiz.py --module M16 --count 20 --output quiz-m16.json
```

A module is complete when you can explain the lesson mechanisms, complete the practice, run or reason through the reinforcement lab, and score your quiz attempt with the answer key or LLM grader.

## Optional Project

Apply Browser, Frontend, CDN, and Edge Architecture to a small system you know. Write a short design note, experiment report, or implementation summary only if you want deeper practice.
