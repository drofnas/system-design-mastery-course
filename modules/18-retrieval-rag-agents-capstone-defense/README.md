# Module 18: Retrieval, RAG, Agents, and Capstone Defense

> **Authoring status:** Review. PESD 2.0 content and machine-readable contracts are migrated. Refreshed evaluator calibration, full platform matrices, offline reruns, cleanup checks, and timed learner pilots remain required before Ready.

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
- Frozen Week 1 baseline; Gate freezes from Weeks 16, 33, 50, 68, and 85; their separate flex-week deltas; and independent Module 16–17 evidence
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

The 10–12 hour weekly figure is a capacity envelope. Core work is deliberately
budgeted below that ceiling; unused time is recovery buffer, not hidden work.

### Week 98: Model and derive — 8.5 hours

| Work | Time |
|---|---:|
| Bounded authoritative resources | 160 min |
| Local mechanism instruction | 120 min |
| Guided practice | 60 min |
| Model and derive core work | 170 min |

Optional contingency capacity: 210 minutes. It is not core work, carries no required evidence, and may remain unused.

### Week 99: Guided build and prediction freeze — 9 hours

| Work | Time |
|---|---:|
| Bounded authoritative resources | 155 min |
| Local mechanism instruction | 120 min |
| Guided practice | 60 min |
| Required evidence components | 120 min |
| Guided build and prediction freeze core work | 85 min |

Optional contingency capacity: 180 minutes. It is not core work, carries no required evidence, and may remain unused.

### Week 100: Independent build and integration — 10 hours

| Work | Time |
|---|---:|
| Independent build and integration core work | 540 min |
| Independent build and integration verification checkpoint | 60 min |

Optional contingency capacity: 120 minutes. It is not core work, carries no required evidence, and may remain unused.

### Week 101: Break, repair, measure, and diagnose — 10 hours

| Work | Time |
|---|---:|
| Required evidence components | 150 min |
| Break, repair, measure, and diagnose core work | 450 min |

Optional contingency capacity: 120 minutes. It is not core work, carries no required evidence, and may remain unused.

### Week 102: Decide, teach, assess, and freeze — 9.5 hours

| Work | Time |
|---|---:|
| Required evidence components | 120 min |
| Decide, teach, assess, and freeze core work | 390 min |
| Module teach-back | 30 min |
| Learning log and freeze check | 30 min |

Optional contingency capacity: 150 minutes. It is not core work, carries no required evidence, and may remain unused.
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
  and [Gate 6 contract](../../gates/G06/assessment-brief.md).
- Module Pass requires G01–G06, every required artifact in `module.json`, average at least 3.0,
  and no zero in R04–R07.
- Gate 6 and the final capstone require all six course gates, average at least
  3.5, passing C01–C10 and AI01–AI12 evidence, and at least 3.0 in every safety-critical dimension.

## Evidence boundary and AI use

The deterministic lab proves repository contracts and exposes causal controls.
It does not prove production relevance, language-model factuality, HNSW scale,
hardware latency, provider equivalence, legal compliance, or team readiness.

AI may challenge hypotheses, tests, alternatives, and review questions. It may
not choose the graded architecture, invent judgments or measurements, alter
frozen work, write replacement graded answers, or answer during Gate 6.

## Course-wide completion contracts

- The machine-readable `module.json` time blocks are the canonical required-work budget.
- The [factual-claims ledger](assessment/factual-claims.json) maps each local lesson to its authoritative source boundary.
- Use the [provider-neutral evaluation workflow](../../EVALUATION_GUIDE.md) only after learner evidence is committed.
- Use the [sealed local gate workflow](../../SOLO_GATE_GUIDE.md) when a course gate applies. Human review is optional.

A frozen self-evaluation may establish **Solo Complete**; independent human or LLM review may establish **Independently Validated**. Synthetic lab values are not production measurements.

## PESD 2.0 scope addition

This 5-week module schedules 47 core hours. Its primary
decision is RFC A10. The added graded scope is
a complete AI assurance case covering tool/model inventory, provider supply chain, ongoing evaluation, human-approval efficacy, transparency, deletion, incident response, policy drift, rollback, and retirement. See Lesson 8, the final guided exercise, final worksheet,
rubric anchors, and remediation map for the integrated evidence contract.

## PESD 2.0 evaluation ownership

Gate G06 invokes this module's rubric and provider-neutral
evaluator once for its domain score. Do not create a second module semantic
evaluation report. The gate result is authoritative; remediation remains a
separate dated artifact only for Revise or Repeat.
