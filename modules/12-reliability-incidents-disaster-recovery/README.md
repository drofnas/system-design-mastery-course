# Module 12: Reliability, Incidents, and Disaster Recovery

> **Authoring status:** Review. PESD 2.0 content and machine-readable contracts are migrated. Refreshed evaluator calibration, full platform matrices, offline reruns, cleanup checks, and timed learner pilots remain required before Ready.

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

The 10–12 hour weekly figure is a capacity envelope. Core work is deliberately
budgeted below that ceiling; unused time is recovery buffer, not hidden work.

### Week 63: Model and derive — 8.5 hours

| Work | Time |
|---|---:|
| Bounded authoritative resources | 130 min |
| Local mechanism instruction | 120 min |
| Guided practice | 60 min |
| Model and derive core work | 200 min |

Optional contingency capacity: 210 minutes. It is not core work, carries no required evidence, and may remain unused.

### Week 64: Guided build and prediction freeze — 9 hours

| Work | Time |
|---|---:|
| Bounded authoritative resources | 145 min |
| Local mechanism instruction | 120 min |
| Guided practice | 60 min |
| Required evidence components | 120 min |
| Guided build and prediction freeze core work | 95 min |

Optional contingency capacity: 180 minutes. It is not core work, carries no required evidence, and may remain unused.

### Week 65: Independent build and integration — 10 hours

| Work | Time |
|---|---:|
| Independent build and integration core work | 540 min |
| Independent build and integration verification checkpoint | 60 min |

Optional contingency capacity: 120 minutes. It is not core work, carries no required evidence, and may remain unused.

### Week 66: Break, repair, measure, and diagnose — 10 hours

| Work | Time |
|---|---:|
| Required evidence components | 90 min |
| Break, repair, measure, and diagnose core work | 510 min |

Optional contingency capacity: 120 minutes. It is not core work, carries no required evidence, and may remain unused.

### Week 67: Decide, teach, assess, and freeze — 9.5 hours

| Work | Time |
|---|---:|
| Required evidence components | 90 min |
| Decide, teach, assess, and freeze core work | 420 min |
| Module teach-back | 30 min |
| Learning log and freeze check | 30 min |

Optional contingency capacity: 150 minutes. It is not core work, carries no required evidence, and may remain unused.
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
submission, one recovery-tier ADR, one Week 68 gate freeze and separate Week 69 capstone delta, and one
recorded teach-back.

## Assessment and completion

- Read the [assessment contract](assessment/README.md), [anchored rubric](assessment/rubric.md),
  [Gate 4](../../gates/G04/assessment-brief.md), [evaluator prompt](assessment/evaluator-prompt.md),
  and [remediation map](assessment/remediation-map.md) before independent work.
- Pass G01–G06, average at least 3.0, and avoid a zero in R04, R07, R08, or R09.
- Complete the four Gate 4 parts only after freezing Module 12 evidence. Preserve
  the Week 68 gate freeze and Week 69 capstone delta separately from the Week 1 baseline and earlier
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

A frozen self-evaluation may establish **Solo Complete**; independent human or LLM review may establish **Independently Validated**. Synthetic lab values are not production measurements.

## PESD 2.0 scope addition

This 5-week module schedules 47 core hours. Its primary
decision is ADR A12. The added graded scope is
cyber recovery, corrupted-backup recovery, provider concentration, control-plane outages, clean-room assumptions, evidence preservation, and notification ownership. See Lesson 8, the final guided exercise, final worksheet,
rubric anchors, and remediation map for the integrated evidence contract.

## PESD 2.0 evaluation ownership

Gate G04 invokes this module's rubric and provider-neutral
evaluator once for its domain score. Do not create a second module semantic
evaluation report. The gate result is authoritative; remediation remains a
separate dated artifact only for Revise or Repeat.
