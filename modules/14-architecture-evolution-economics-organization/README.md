# Module 14: Architecture Evolution, Economics, and Organization

> **Authoring status:** Review. PESD 2.0 content and machine-readable contracts are migrated. Refreshed evaluator calibration, full platform matrices, offline reruns, cleanup checks, and timed learner pilots remain required before Ready.

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
- Preserved Week 1 baseline, Week 68 Gate 4 freeze, and Week 69 delta; neither may be edited
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

The 10–12 hour weekly figure is a capacity envelope. Core work is deliberately
budgeted below that ceiling; unused time is recovery buffer, not hidden work.

### Week 75: Model and derive — 8.5 hours

| Work | Time |
|---|---:|
| Bounded authoritative resources | 160 min |
| Local mechanism instruction | 120 min |
| Guided practice | 60 min |
| Model and derive core work | 170 min |

Optional contingency capacity: 210 minutes. It is not core work, carries no required evidence, and may remain unused.

### Week 76: Guided build and prediction freeze — 9 hours

| Work | Time |
|---|---:|
| Bounded authoritative resources | 150 min |
| Local mechanism instruction | 120 min |
| Guided practice | 60 min |
| Required evidence components | 60 min |
| Guided build and prediction freeze core work | 150 min |

Optional contingency capacity: 180 minutes. It is not core work, carries no required evidence, and may remain unused.

### Week 77: Independent build and integration — 10 hours

| Work | Time |
|---|---:|
| Independent build and integration core work | 540 min |
| Independent build and integration verification checkpoint | 60 min |

Optional contingency capacity: 120 minutes. It is not core work, carries no required evidence, and may remain unused.

### Week 78: Break, repair, measure, and diagnose — 10 hours

| Work | Time |
|---|---:|
| Required evidence components | 90 min |
| Break, repair, measure, and diagnose core work | 510 min |

Optional contingency capacity: 120 minutes. It is not core work, carries no required evidence, and may remain unused.

### Week 79: Decide, teach, assess, and freeze — 9.5 hours

| Work | Time |
|---|---:|
| Required evidence components | 150 min |
| Decide, teach, assess, and freeze core work | 360 min |
| Module teach-back | 30 min |
| Learning log and freeze check | 30 min |

Optional contingency capacity: 150 minutes. It is not core work, carries no required evidence, and may remain unused.
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
- Gate 5 runs in Week 85. Module 14 evidence feeds that later assessment; accepted findings belong in the separate Week 86 delta.

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

## PESD 2.0 scope addition

This 5-week module schedules 47 core hours. Its primary
decision is ADR A07. The added graded scope is
a thin local platform product with a service catalog, self-service interface, golden path, policy guardrails, exception path, ownership metadata, platform SLO, adoption and support metrics, FinOps allocation, and an exit plan. See Lesson 8, the final guided exercise, final worksheet,
rubric anchors, and remediation map for the integrated evidence contract.
