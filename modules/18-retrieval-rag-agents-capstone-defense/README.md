# Module 18: Retrieval, RAG, Agents, and Capstone Defense

> **Authoring status:** Ready. The portable lab, F01–F08 pairs, six isolated
> evaluator records, deterministic calibration, semantic/resource review, and
> focused/full validation all pass.

## What this module changes

A retrieval-augmented assistant is a probabilistic distributed system with
deterministic obligations. Retrieval may miss the right evidence. Generated
claims may outpace their citations. Derived indexes may lag revocation. Model
output may propose an action, but it cannot grant authority. A workflow may
restart after a side effect and see the same result twice. This module teaches
you to measure those boundaries and enforce the safety properties in code.

The continuing non-capstone case is the **CivicAid Municipal Permit Assistant**.
Residents search versioned public rules, access their private drafts, and may
approve an official permit submission. CivicAid contains no products,
inventory, checkout, payment, merchant, or shopping-assistant answer. Freeze
your independent commerce decisions before opening the completed case or answer
key.

## Prerequisites

- Modules 1–17, especially retrieval-adjacent storage, deadlines, messaging,
  security, browser/edge, and inference evidence
- Python 3.11+; the required lab uses only the standard library
- Frozen Week 1 baseline, Week 12/24/48 revisions, Gate 5 evidence, and
  independent Module 16–17 capstone evidence
- No model download, account, API key, accelerator, or network for required work

## Learning outcomes

By the end of the module, you can:

1. Model exact and approximate retrieval and tune HNSW from measured recall and work.
2. Build and compare lexical, vector, hybrid, filtered, and reranked retrieval.
3. Select retrieval and answer metrics that predict a declared product outcome.
4. Preserve evidence scope, version, freshness, revocation, citation, and abstention.
5. Enforce typed tools, scoped credentials, authorization, approval, and audit outside a model.
6. Resume, replay, deduplicate, cancel, compensate, and budget agent workflows.
7. Diagnose stale, low-quality, adversarial, timeout, replay, budget, and authorization failures.
8. Defend the complete capstone across product, technical, security, operations,
   cost, ownership, migration, reversal, and organizational concerns.

## Schedule

### Week 69: Model retrieval and freeze predictions — 11 hours

| Work | Time |
|---|---:|
| Lessons 1–4 and bounded sources | 4 h |
| EX-01–EX-10 with CivicAid calculations | 2 h |
| Independent dataset, retrieval contract, and F01–F08 predictions | 3.5 h |
| Freeze, source review, and learning log | 1.5 h |

Use the [Week 69 worksheet](worksheets/week-69-retrieval-model.md).

### Week 70: Build retrieval, grounding, and durable tools — 12 hours

| Work | Time |
|---|---:|
| Lessons 5–7 and CivicAid tutorial | 3 h |
| EX-08–EX-16 and lab rehearsal | 2 h |
| Independent commerce assistant implementation and tests | 6 h |
| Implementation review and learning log | 1 h |

Use the [Week 70 worksheet](worksheets/week-70-assistant-build.md).

### Week 71: Break and measure system claims — 12 hours

| Work | Time |
|---|---:|
| Lessons 5–8 and bounded sources | 1.5 h |
| F01–F08 rehearsal and diagnostic plan | 2 h |
| Sixteen immutable broken/repaired trials | 6 h |
| Failure matrix, incident, threat, cost, and learning log | 2.5 h |

Use the [Week 71 worksheet](worksheets/week-71-retrieval-agent-failures.md).

### Week 72: Decide, defend, assess, and plan — 11 hours

| Work | Time |
|---|---:|
| Lesson 8, resource synthesis, and EX-17–EX-20 | 1 h |
| Final RFC, operations, migration, and Week 72 revision | 3 h |
| Gate 6 examination, hidden practical, defense, and portfolio review | 3.5 h |
| Module evaluation, remediation, teach-back, log, and practice plan | 3.5 h |

Use the [Week 72 worksheet](worksheets/week-72-capstone-defense.md).

## Learn

1. [Retrieval contracts, outcomes, and evaluation](lessons/01-retrieval-contracts-evaluation.md)
2. [Chunking, lexical and vector retrieval, and access filters](lessons/02-chunking-lexical-vector-filters.md)
3. [Exact search, HNSW, and index economics](lessons/03-exact-ann-hnsw.md)
4. [Hybrid retrieval, reranking, and release gates](lessons/04-hybrid-reranking-release-gates.md)
5. [Evidence provenance, freshness, grounding, and abstention](lessons/05-provenance-grounding-freshness.md)
6. [Structured tools, authorization, approvals, and adversarial content](lessons/06-tools-authorization-prompt-injection.md)
7. [Durable agent state, replay, cancellation, and budgets](lessons/07-durable-agent-workflows.md)
8. [CivicAid decision, capstone integration, and final defense](lessons/08-civicaid-capstone-defense.md)

Use the [navigation guide](navigation.md), [artifact contracts](artifact-contracts.md),
[glossary](glossary.md), [resource guide](resources.md), and [lab reference](lab/README.md)
after studying the local explanation.

## Practice and independent evidence

- Freeze A01 before the completed [CivicAid case](case-study/civicaid-permit-assistant.md).
- Complete the [guided exercises](exercises/exercises.md) before opening the
  [explained answers](exercises/answer-key.md).
- Run all eight pairs in the portable lab. Preserve predictions, scenario and
  trial hashes, source/evaluation identities, toolchain, raw output, and limits.
- Build the commerce assistant independently. CivicAid thresholds, tool names,
  topology, and answers are not capstone defaults.
- Store corrections in dated addenda. Never rewrite a frozen baseline or raw trial.

This module closes the portfolio with the complete capstone, a substantial final
RFC, threat and cost evidence, migration and operating plans, a controlled
incident, a failure matrix, a recorded defense, and the next-year practice plan.

## Assessment and completion

- Read the [assessment contract](assessment/README.md), [anchored rubric](assessment/rubric.md),
  [evaluator prompt](assessment/evaluator-prompt.md), [remediation map](assessment/remediation-map.md),
  and [Gate 6 contract](assessment/gate-06.md).
- Module Pass requires G01–G06, every A01–A17 artifact, average at least 3.0,
  and no zero in R04–R07.
- Gate 6 and the final capstone require all six course gates, average at least
  3.5, no failed capstone invariant, and no safety-critical zero.

## Evidence boundary and AI use

The deterministic lab proves repository contracts and exposes causal controls.
It does not prove production relevance, language-model factuality, HNSW scale,
hardware latency, provider equivalence, legal compliance, or team readiness.

AI may challenge hypotheses, tests, alternatives, and review questions. It may
not choose the graded architecture, invent judgments or measurements, alter
frozen work, write replacement graded answers, or answer during Gate 6.
