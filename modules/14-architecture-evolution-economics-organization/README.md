# Module 14: Architecture Evolution, Economics, and Organization

> **Authoring status:** Ready. Deterministic lab tests, six isolated evaluator
> runs, calibration checking, semantic and resource review, and focused and
> full-course validation passed on 2026-08-03.

## What this module changes

Architecture evolution is a controlled change to a live technical and social
system. A boundary is valuable only when it improves an outcome enough to pay
for new coordination, compatibility, operational, security, and economic work.
This module teaches learners to select a boundary, quantify its total cost,
migrate without losing authority or service, and make ownership survivable.

The continuing non-capstone case is the **Northstar Observatory Catalog
Evolution Program**. The operations registry remains authoritative for accepted
observations and publication approval. Northstar extracts only the public
catalog projection and bulletin delivery after comparing a modular monolith,
synchronous service, and event-driven projection. Freeze independent commerce
decisions before opening the case or answer key.

## Prerequisites

- Modules 1–13, especially architecture drivers, cost, transactions,
  replication, messaging, recovery, and security ownership
- Python 3.11 or newer; the reference lab uses only the standard library
- Preserved Week 1 baseline and Week 48 revision; neither may be edited
- Ability to read JSON contracts, cost tables, deployment sequences, and
  evidence-backed technical decisions

## Learning outcomes

By the end of the module, you can:

1. Select modular-monolith, service, or event boundaries from measured change,
   workload, failure, data-authority, security, and ownership drivers.
2. Model Conway effects, interaction cost, cognitive load, ownership, and
   succession without treating an org chart as an architecture command.
3. Compare managed, open-source, custom, and platform choices with operating,
   governance, security, portability, and exit obligations.
4. Calculate fully loaded cost and cost per useful outcome with allocation,
   sensitivity, and explicit stopping thresholds.
5. Design compatibility policies and expand-and-contract changes for
   mixed-version operation.
6. Implement resumable backfills, shadow comparison, controlled cutover,
   rollback, and evidence-based decommissioning.
7. Diagnose nine evolution failures without losing authority, data, service,
   cost control, dependency control, or ownership continuity.
8. Defend a multi-quarter strategy with outcomes, sequencing, staffing,
   dependencies, dissent, stopping conditions, and reversal evidence.

## Schedule

### Week 53: Model boundaries, ownership, sourcing, and economics — 10.5 hours

| Work | Time |
|---|---:|
| Lessons 1–4 and bounded sources | 3 h |
| EX-01–EX-08 and Northstar modeling tutorial | 2 h |
| Independent baseline, boundary, ownership, sourcing, and cost model | 4 h |
| Freeze, self-check, and learning log | 1.5 h |

Use the [Week 53 worksheet](worksheets/week-53-evolution-model.md).

### Week 54: Build compatibility and migration controls — 11.5 hours

| Work | Time |
|---|---:|
| Lessons 5–6 and bounded sources | 3 h |
| EX-09–EX-12 and lab walkthrough | 2.5 h |
| Independent compatibility, backfill, cost, and migration build | 5 h |
| Implementation review and learning log | 1 h |

Use the [Week 54 worksheet](worksheets/week-54-migration-build.md).

### Week 55: Break migration, cost, dependency, and ownership controls — 11.5 hours

| Work | Time |
|---|---:|
| Lesson 7 and bounded sources | 2.5 h |
| EX-13–EX-16 and experiment rehearsal | 2 h |
| Nine broken/repaired pairs and immutable raw evidence | 5 h |
| Failure matrix, reconciliation report, and learning log | 2 h |

Use the [Week 55 worksheet](worksheets/week-55-evolution-failure-matrix.md).

### Week 56: Decide, teach, assess, and remediate — 10 hours

| Work | Time |
|---|---:|
| Lesson 8, bounded sources, and EX-17–EX-18 | 2 h |
| Technical-strategy memo | 3 h |
| Recorded defense and evaluator run | 2 h |
| Remediation, separate revision, and learning log | 3 h |

Use the [Week 56 worksheet](worksheets/week-56-strategy-defense.md).

## Learn

1. [Boundaries from outcomes and coupling](lessons/01-boundaries-outcomes-coupling.md)
2. [Social architecture, ownership, and cognitive load](lessons/02-social-architecture-ownership.md)
3. [Sourcing, platforms, and governance](lessons/03-sourcing-platforms-governance.md)
4. [Total cost and unit economics](lessons/04-total-cost-unit-economics.md)
5. [Compatibility, versioning, and schema evolution](lessons/05-compatibility-schema-evolution.md)
6. [Incremental migration and backfills](lessons/06-incremental-migration-backfills.md)
7. [Shadowing, cutover, rollback, and decommissioning](lessons/07-shadow-cutover-rollback.md)
8. [Technical strategy and teach-back](lessons/08-technical-strategy-teach-back.md)

Use the [glossary](glossary.md) as reference after studying the mechanisms.

## Practice and independent evidence

- Freeze the commerce evolution baseline before studying the completed
  [Northstar case](case-study/northstar-catalog-evolution.md).
- Complete the [guided exercises](exercises/exercises.md) before opening the
  [explained answers](exercises/answer-key.md).
- Run the [evolution lab](lab/README.md), preserve scenario and raw-output
  hashes, then reproduce the observable controls in the chosen stack or a safe
  operated environment.
- Preserve failed trials and uncertainty. Corrections belong in dated addenda;
  never rewrite frozen baselines or raw evidence.
- Do not copy Northstar boundaries, costs, staffing, thresholds, contracts, or
  target architecture into the commerce capstone.

This module contributes one cost model, one migration plan, one substantial
technical-strategy memo, one failure matrix, and one recorded teach-back.

## Assessment and completion

- Read the [assessment contract](assessment/README.md),
  [anchored rubric](assessment/rubric.md),
  [evaluator prompt](assessment/evaluator-prompt.md), and
  [remediation map](assessment/remediation-map.md) before independent work.
- Pass G01–G06, average at least 3.0, and avoid a zero in R05–R09.
- Gate 5 remains at Week 60. Week 56 does not create or edit a capstone gate
  revision; Module 14 evidence feeds the later assessment.

## Evidence boundary and AI use

The deterministic model exposes compatibility, migration state, hashes, cost
arithmetic, decisions, and invariant results. It does not prove production
compatibility, provider portability, accounting accuracy, safe migration at
scale, or real human staffing resilience.

AI may challenge options, arithmetic, experiments, and evidence. It may not
choose the graded strategy, invent measurements, alter frozen artifacts, write
replacement graded answers, or answer during the defense.

## Course-wide completion contracts

- The machine-readable `module.json` time blocks are the canonical required-work budget.
- The [factual-claims ledger](assessment/factual-claims.json) maps each local lesson to its authoritative source boundary.
- Use the [provider-neutral evaluation workflow](../../EVALUATION_GUIDE.md) only after learner evidence is committed.
- Use the [sealed local gate workflow](../../SOLO_GATE_GUIDE.md) when a course gate applies. Human review is optional.

A frozen self-evaluation may establish **Solo Complete**; independent human or LLM review may establish **Independently Validated**. Synthetic lab values are not production measurements.
