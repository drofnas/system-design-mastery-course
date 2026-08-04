# Module 12: Reliability, Incidents, and Disaster Recovery

> **Authoring status:** Ready. Teaching, practice, lab, assessment, calibration,
> semantic review, resource verification, and course validation passed on
> 2026-08-02.

## What this module changes

Reliability is not a component uptime percentage. It is the fraction of a named
user journey that meets a measurable contract over a stated population and
window. This module connects that contract to error-budget decisions, actionable
alerts, bounded degradation, incident coordination, and tested recovery.

The continuing non-capstone case is **Northstar Observatory Reliability and
Recovery**. It extends the observatory registry, public catalog, and publication
workflow from Modules 8–11. It contains no products, merchants, inventory,
checkout, payments, orders, or capstone architecture. Freeze independent
commerce decisions before opening the worked case or answer key.

## Prerequisites

- Modules 1–11, especially capacity, observability, deadlines, transaction
  recovery, fencing, consensus, durable workflows, and reconciliation
- Python 3.11 or newer; the reference lab uses only the standard library
- Preserved Module 10 and 11 decisions and immutable evidence
- Comfort reading time series, incident timelines, recovery logs, and JSON

## Learning outcomes

By the end of the module, you can:

1. Define user-journey SLIs and SLOs with valid-event populations, windows,
   exclusions, latency, availability, freshness, and correctness.
2. Calculate error budgets, burn rates, dependency exposure, shared fate, and
   composite reliability without multiplying unrelated percentages blindly.
3. Implement multi-window burn alerts and separate mitigation signals from
   diagnostic telemetry.
4. Build priority-aware degraded modes, load shedding, dependency bounds, and
   enough reserve to operate after zone or regional loss.
5. Run an incident with explicit command, operations, communications, liaison,
   handoff, escalation, and stop conditions.
6. Produce an evidence-based postmortem and rank corrective work by expected
   risk reduction, effort, ownership, and verification.
7. Verify backup integrity, RPO, RTO, restore, failover, fencing,
   reconciliation, and failback using controlled recovery evidence.
8. Diagnose nine reliability failures and defend Gate 4 across consensus,
   messaging, reliability, security, cost, ownership, and recovery.

## Schedule

### Week 45: Model user-visible reliability — 10.5 hours

| Work | Time |
|---|---:|
| Lessons 1–3 and bounded sources | 3 h |
| EX-01–EX-07 and Northstar tutorial | 2 h |
| Independent journey, SLO, budget, alert, and recovery baseline | 4 h |
| Self-check and learning log | 1.5 h |

Use the [Week 45 worksheet](worksheets/week-45-reliability-model.md).

### Week 46: Build operational controls — 11.5 hours

| Work | Time |
|---|---:|
| Lesson 4 and bounded sources | 2.5 h |
| EX-08–EX-09 and lab walkthrough | 2.5 h |
| Independent SLO, alert, degraded-mode, runbook, and recovery build | 5.5 h |
| Implementation review and learning log | 1 h |

Use the [Week 46 worksheet](worksheets/week-46-reliability-controls.md).

### Week 47: Run incidents and recovery exercises — 11.5 hours

| Work | Time |
|---|---:|
| Lessons 5–7 and bounded sources | 2.5 h |
| EX-10–EX-15 and game-day rehearsal | 2 h |
| Nine broken/repaired pairs and immutable evidence | 5 h |
| Incident postmortem, recovery notes, and learning log | 2 h |

Use the [Week 47 worksheet](worksheets/week-47-incident-recovery-experiments.md).

### Week 48: Decide, teach, and complete Gate 4 — 10 hours

| Work | Time |
|---|---:|
| Lesson 8, bounded sources, and EX-16 | 1.5 h |
| Final postmortem, disaster-recovery review, and recovery-tier ADR | 2.5 h |
| Recorded defense and module evaluation | 1.5 h |
| Four-part Gate 4 | 3.5 h |
| Remediation and learning log | 1 h |

Use the [Week 48 worksheet](worksheets/week-48-reliability-decision-gate-04.md).

## Learn

1. [User journeys, SLIs, and SLOs](lessons/01-user-journeys-slis-slos.md)
2. [Error budgets, dependencies, and composite reliability](lessons/02-error-budgets-dependencies.md)
3. [Burn rates and actionable alerting](lessons/03-burn-rates-actionable-alerting.md)
4. [Graceful degradation and degraded capacity](lessons/04-graceful-degradation-capacity.md)
5. [Incident command, communication, and runbooks](lessons/05-incident-command-runbooks.md)
6. [Postmortems and corrective work](lessons/06-postmortems-corrective-work.md)
7. [Backups, restore, failover, and failback](lessons/07-backups-restore-failover.md)
8. [Chaos, game days, and reliability decisions](lessons/08-game-days-reliability-decisions.md)

Use the [glossary](glossary.md) as reference after studying the mechanisms.

## Practice and independent evidence

- Freeze Week 45 commerce decisions before studying the completed
  [Northstar case](case-study/northstar-reliability-recovery.md).
- Complete the [guided exercises](exercises/exercises.md) before opening the
  [explained answers](exercises/answer-key.md).
- Run the [reliability lab](lab/README.md), preserve hashes and raw output, then
  reproduce the observable contract in the learner's chosen stack or safe
  operated environment.
- Preserve predictions, incident timelines, and raw recovery evidence.
  Corrections belong in dated addenda; never rewrite a failed first attempt.
- Do not copy Northstar's journeys, thresholds, burn windows, roles, topology,
  backup schedule, or recovery design into the commerce capstone.

This module contributes one controlled-incident postmortem, one
disaster-recovery exercise report, one reliability investigation, one Gate 4
submission, one recovery-tier ADR, one Week 48 capstone revision, and one
recorded teach-back.

## Assessment and completion

- Read the [assessment contract](assessment/README.md), [anchored rubric](assessment/rubric.md),
  [Gate 4](assessment/gate-04.md), [evaluator prompt](assessment/evaluator-prompt.md),
  and [remediation map](assessment/remediation-map.md) before independent work.
- Pass G01–G06, average at least 3.0, and avoid a zero in R04, R07, R08, or R09.
- Complete the four Gate 4 parts only after freezing Module 12 evidence. Preserve
  the Week 48 capstone revision separately from the Week 1 baseline and earlier
  revisions.

## Evidence boundary and AI use

The deterministic model exposes journey accounting, budget arithmetic, alert
decisions, bounded degradation, incident records, backups, recovery sequencing,
fencing, and reconciliation. It does not prove physical media durability,
production availability or latency, control-plane independence, real regional
isolation, human performance under stress, security enforcement, or compliance.

AI may challenge calculations, hypotheses, failure coverage, and alternatives.
It may not choose the graded design, invent incident or recovery evidence,
modify frozen artifacts, write replacement graded answers, or answer during the
defense. Disclose assistance and verify generated claims.

## Course-wide completion contracts

- The machine-readable `module.json` time blocks are the canonical required-work budget.
- The [factual-claims ledger](assessment/factual-claims.json) maps each local lesson to its authoritative source boundary.
- Use the [provider-neutral evaluation workflow](../../EVALUATION_GUIDE.md) only after learner evidence is committed.
- Use the [sealed local gate workflow](../../SOLO_GATE_GUIDE.md) when a course gate applies. Human review is optional.

Self-scoring is provisional and cannot establish Pass. Synthetic lab values are not production measurements.
