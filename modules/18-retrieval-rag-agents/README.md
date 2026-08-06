# Module 18: Retrieval, RAG, and Agent Systems

## Purpose

Retrieval, RAG, tool authorization, workflow durability, grounding, and agent failure modes.

This module is part of the solo Computer Science and System Design Mastery path. Study the local lessons first, reinforce the mechanisms with practice and labs, then use the quiz package to test recall, application, diagnosis, and design judgment.

## Prerequisites

- Familiarity with Modules 1-17, or willingness to review earlier lessons as needed.
- Python 3.11 or newer for the quiz tooling and most reinforcement labs.
- Comfort reading technical documentation, code snippets, diagrams, and answer explanations.

## Learning Outcomes

1. Model exact and approximate nearest-neighbor retrieval and tune HNSW from measured recall, visited work, latency, memory, and index cost.
2. Build and compare chunked lexical, vector, filtered, hybrid, and reranked retrieval paths using one evaluation set.
3. Select retrieval, grounding, refusal, latency, and cost measures that connect to a declared user outcome and release criterion.
4. Preserve evidence authorization, exact version, freshness, revocation, claim support, citations, and justified abstention.
5. Enforce versioned tool schemas, scoped credentials, deterministic authorization, bound human approval, and secret-free audit outside model output.
6. Resume, replay, deduplicate, cancel, compensate, and budget an agent workflow without repeating irreversible side effects.
7. Diagnose F01-F08 from immutable equivalent trials and connect each repair to user, security, operating, and cost consequences.
8. Synthesize retrieval, agent, product, security, operating, cost, ownership, migration, and reversal tradeoffs.

## Learn

1. [Retrieval Contracts, Outcomes, and Evaluation](lessons/01-retrieval-contracts-evaluation.md)
2. [Chunking, Lexical and Vector Retrieval, and Access Filters](lessons/02-chunking-lexical-vector-filters.md)
3. [Exact Search, HNSW, and Index Economics](lessons/03-exact-ann-hnsw.md)
4. [Hybrid Retrieval, Reranking, and Release Criteria](lessons/04-hybrid-reranking-release-gates.md)
5. [Evidence provenance, grounding, freshness, and abstention](lessons/05-provenance-grounding-freshness.md)
6. [Structured tools, authorization, approval, and hostile context](lessons/06-tools-authorization-prompt-injection.md)
7. [Durable agent workflows, replay, cancellation, and budgets](lessons/07-durable-agent-workflows.md)
8. [CivicAid Decision Tutorial and Synthesis Review](lessons/08-civicaid-decision-defense.md)

- Glossary: [glossary.md](glossary.md).

## Practice And Lab

- Guided exercises: [exercises/exercises.md](exercises/exercises.md).
- Explained practice answers: [exercises/answer-key.md](exercises/answer-key.md).
- Reinforcement lab: [lab/README.md](lab/README.md). Run the portable retrieval/agent lab for reinforcement; build a larger assistant only as an optional synthesis project.
- Resource guide: [resources.md](resources.md).

## Quiz And Review

- Question bank: [quiz/question-bank.json](quiz/question-bank.json).
- Answer key: [quiz/answer-key.md](quiz/answer-key.md).
- LLM grading prompt: [quiz/llm-grader-prompt.md](quiz/llm-grader-prompt.md).

Generate a 20-question quiz from the repository root:

```bash
python3 scripts/generate_quiz.py --module M18 --count 20 --output quiz-m18.json
```

A module is complete when you can explain the lesson mechanisms, complete the practice, run or reason through the reinforcement lab, and score your quiz attempt with the answer key or LLM grader.

## Optional Project

Build an optional final synthesis project that uses retrieval and tool workflows safely. No synthesis review or locked first attempt is required.
