# Principal Engineer and Systems Design Mastery

Course-wide learner contracts:

- [Supported one-computer setup](HOME_LAB_GUIDE.md)
- [Sealed local course gates](SOLO_GATE_GUIDE.md)
- [Provider-neutral evaluation workflow](EVALUATION_GUIDE.md)
- [Module authoring and readiness standard](MODULE_STANDARD.md)
- [PESD 2.0 readiness register](PESD_V2_READINESS.md)

This repository contains the teaching materials for the 104-week PESD 2.0
**Principal Engineer and Systems Design Mastery** course. It is also designed
to become each learner's version-controlled record of coursework: notes, labs,
experiments, architecture decisions, reviews, and capstone evidence. The
authoritative course requirements are in
[`00_COURSE_SYLLABUS.md`](00_COURSE_SYLLABUS.md).

Before running any executable lab, use the cross-platform
[`HOME_LAB_GUIDE.md`](HOME_LAB_GUIDE.md) and its non-installing preflight. The course
supports one ordinary macOS or Ubuntu computer, and Windows through Ubuntu on
WSL2; no discrete GPU or second learner is required.

## Make your own course repository

The recommended setup is a GitHub fork with two long-lived branches:

- Keep `main` free of personal coursework so it can track this repository.
- Do all coursework on `coursework`, including answers, experiments, reports,
  and capstone artifacts.

Fork this repository on GitHub, then clone your fork and create the coursework
branch:

```bash
git clone https://github.com/YOUR-USERNAME/system-design-mastery-course.git
cd system-design-mastery-course
git remote add upstream https://github.com/drofnas/system-design-mastery-course.git
git switch -c coursework
git push -u origin coursework
```

Commit your work to `coursework`. When this course publishes an update, bring
it into your fork with:

```bash
git switch main
git fetch upstream
git merge --ff-only upstream/main
git push origin main
git switch coursework
git merge main
git push origin coursework
```

Keeping coursework off `main` prevents course updates from being mixed with
your commits. It cannot prevent every merge conflict: if both you and the
course change the same worksheet, resolve that conflict on `coursework` and
preserve your completed evidence.

### Public and private coursework

A fork of this public repository is also public. Its branches and Git history
are visible to others, and commits may remain accessible even after a fork or
branch is deleted. Never commit secrets, proprietary employer material, private
data, or other sensitive information.

If your coursework must remain private, create an empty private repository and
use a clone of this course instead of a GitHub fork:

```bash
git clone https://github.com/drofnas/system-design-mastery-course.git
cd system-design-mastery-course
git remote rename origin upstream
git remote add origin https://github.com/YOUR-USERNAME/YOUR-PRIVATE-REPOSITORY.git
git push -u origin main
git switch -c coursework
git push -u origin coursework
```

Use the same update sequence shown above. This private copy will not retain
GitHub's fork relationship, but the `upstream` remote still provides course
updates.

## Start here: Week 1

Your first milestone is **Week 1: Architectural Judgment**.

Start with the complete
[`Module 1: Architectural Judgment`](modules/01-architectural-judgment/README.md).
Its local lessons teach the methods using a non-commerce transit case before
you apply them independently.

1. Study Module 1 Lessons 1–5 and complete the guided exercises without using
   the commerce capstone.
2. Complete [`capstone/baselines/week-01-baseline.md`](capstone/baselines/week-01-baseline.md)
   independently, without requesting AI architecture recommendations.
3. Commit and tag the completed baseline as `week-01-baseline`.
4. Record criticism only in
   [`reviews/week-01-baseline-review.md`](reviews/week-01-baseline-review.md).
5. Continue Module 1 through its Week 5 RFC, defense, and assessment.

The baseline is evidence of initial judgment. Once tagged, it must never be
edited. Freeze capstone submissions at Weeks 16, 33, 50, 68, 85, and 103. Write
separate delta revisions during Weeks 17, 34, 51, 69, 86, and 104.

## Standard cadence

- Duration: 104 weeks
- Weekly capacity: 10–12 hours
- Scheduled core work: 8.5–10 hours in instructional weeks
- Module length: five weeks; six for Modules 10 and 17

| Week in module | Focus | Core hours |
|---:|---|---:|
| 1 | Model and derive | 8.5 |
| 2 | Guided build and prediction freeze | 9 |
| 3 | Independent build and integration | 10 |
| 4 | Break, repair, measure, and diagnose | 10 |
| 5 | Decide, teach, assess, and freeze | 9.5 |

Modules 10 and 17 insert a second 10-hour independent build/integration week.
The difference between core work and 10–12-hour capacity is intentional buffer.

## Assessment gates

| Gate | Week | Focus |
|---:|---:|---|
| 1 | 16 | Judgment, capacity, and computer systems |
| 2 | 33 | Performance, networks, and remote calls |
| 3 | 50 | Storage, transactions, replication, and partitioning |
| 4 | 68 | Consensus, messaging, reliability, and recovery |
| 5 | 85 | Security, evolution, economics, and runtimes |
| 6 | 103 | Web edge, AI systems, and capstone |

Gates are standalone weeks with no new teaching or build work. Every scored
part, module-domain subscore, and safety-critical row must reach 3.0. Gate 6
also requires a 3.5 longitudinal capstone and overall average. See the
[gate manifests](gates/) for exact minutes, domain matrices, invariants, and
Pass/Revise/Repeat rules.

## Portfolio inventory

Track progress against the syllabus minimums:

| Artifact | Required |
|---|---:|
| Architecture Decision Records | 12 |
| Substantial RFCs | 6 |
| Capacity and cost models | 3 |
| Performance investigation reports | 6 |
| Controlled-incident postmortems | 4 |
| Failure matrices | 6 |
| Source-code internals reviews | 3 |
| Runtime comparison reports | 2 |
| Major security threat models | 1 |
| Disaster-recovery exercise reports | 2 |
| Migration plans | 2 |
| Recorded teach-backs or reviews | 6 |
| Complete capstone | 1 |
| Data Governance Dossier lineage | 1 |
| Assurance Case | 1 |
| Platform Product Experiment | 1 |
| AI System Dossier lineage | 1 |

The machine-readable [portfolio registry](portfolio-items.json) assigns each
featured credit once. See the [V1-to-V2 migration guide](V1_TO_V2_MIGRATION.md)
if you began the 72-week release.

## Repository map

```text
notes/          Concept and source notes
labs/           Mechanism implementations
experiments/    Experiment definitions and raw evidence
adr/            Architecture Decision Records
rfc/            Substantial design proposals
reports/        Capacity, performance, incident, and recovery reports
reviews/        Artifact reviews and assessment feedback
capstone/       Global Commerce Platform artifacts and implementation
learning-log/   Weekly reflection and teach-back records
templates/      Reusable artifact contracts
modules/        Complete five-/six-week teaching and assessment packages
gates/          Standalone course-gate manifests and schedules
schemas/        Machine-readable module and evaluation contracts
scripts/        Course validation tools
```

## Module catalog

| Module | Weeks | Status | Entry point |
|---:|---:|---|---|
| 1. Architectural Judgment | 1–5 | Review | [Start Module 1](modules/01-architectural-judgment/README.md) |
| 2. Capacity, Queues, and Tail Latency | 6–10 | Review | [Start Module 2](modules/02-capacity-queues-tail-latency/README.md) |
| 3. Computer Systems and Operating Systems | 11–15 | Review | [Start Module 3](modules/03-computer-systems-operating-systems/README.md) |
| 4. Performance Methodology and Observability | 18–22 | Review | [Start Module 4](modules/04-performance-methodology-observability/README.md) |
| 5. Network Foundations | 23–27 | Review | [Start Module 5](modules/05-network-foundations/README.md) |
| 6. Deadlines and Resilient Remote Calls | 28–32 | Review | [Start Module 6](modules/06-deadlines-resilient-remote-calls/README.md) |
| 7. Data Models and Storage Engines | 35–39 | Review | [Start Module 7](modules/07-data-models-storage-engines/README.md) |
| 8. Transactions, Concurrency, and Recovery | 40–44 | Review | [Start Module 8](modules/08-transactions-concurrency-recovery/README.md) |
| 9. Replication and Partitioning | 45–49 | Review | [Start Module 9](modules/09-replication-partitioning/README.md) |
| 10. Time, Coordination, and Consensus | 52–57 | Review | [Start Module 10](modules/10-time-coordination-consensus/README.md) |
| 11. Messaging, Streams, and Workflows | 58–62 | Review | [Start Module 11](modules/11-messaging-streams-workflows/README.md) |
| 12. Reliability, Incidents, and Disaster Recovery | 63–67 | Review | [Start Module 12](modules/12-reliability-incidents-disaster-recovery/README.md) |
| 13. Security, Privacy, and Abuse Resistance | 70–74 | Review | [Start Module 13](modules/13-security-privacy-abuse-resistance/README.md) |
| 14. Architecture Evolution, Economics, and Organization | 75–79 | Review | [Start Module 14](modules/14-architecture-evolution-economics-organization/README.md) |
| 15. Execution Models Across Languages | 80–84 | Review | [Start Module 15](modules/15-execution-models-across-languages/README.md) |
| 16. Browser, Frontend, CDN, and Edge Architecture | 87–91 | Review | [Start Module 16](modules/16-browser-frontend-cdn-edge/README.md) |
| 17. Model Foundations and Inference Systems | 92–97 | Review | [Start Module 17](modules/17-model-foundations-inference-systems/README.md) |
| 18. Retrieval, RAG, Agents, and Capstone Defense | 98–102 | Review | [Start Module 18](modules/18-retrieval-rag-agents-capstone-defense/README.md) |

Future modules must satisfy
[`MODULE_STANDARD.md`](MODULE_STANDARD.md). Course-authoring agents must also
follow [`AGENTS.md`](AGENTS.md).

## Validate the course

Run:

```bash
python3 scripts/validate_course.py
```

The validator discovers every module manifest and checks hour budgets, outcome
mappings, lesson and resource contracts, required teaching and assessment
files, calibration state, the frozen baseline contract, JSON interfaces, and
local Markdown links. Use `--module M01` through `--module M18` to validate a
single module.

## Evidence and AI rules

- Quantify architectural claims and identify how they will be measured.
- State the workload, invariants, failure model, ownership, and reversal evidence.
- Keep raw observations separate from interpretation.
- Disclose AI assistance on graded artifacts.
- Verify AI-generated claims against primary sources, code, or experiments.
- Read and explain generated code before accepting it.
- Keep secrets, private data, and proprietary material out of unapproved tools.
- Preserve an independent first design before requesting AI critique.
- Never rely on AI during an architecture defense.

## License

Copyright © 2026 drofnas.

- Course content, including lessons, exercises, assessments, documentation, and
  templates, is licensed under
  [Creative Commons Attribution 4.0 International](LICENSE-CONTENT).
- Software, including source code, executable labs, tests, scripts, schemas,
  and machine-readable fixtures, is licensed under the
  [Apache License 2.0](LICENSE-CODE).

The repository-wide scope and exceptions are defined in [`LICENSE`](LICENSE).
Linked or quoted third-party resources remain subject to their original
copyright and license terms.

You retain copyright in original coursework that you add to your copy. The
licenses above continue to govern course material that you copy, modify, or
redistribute as part of that work.

## Templates

- [`templates/learning-log-template.md`](templates/learning-log-template.md)
- [`templates/adr-template.md`](templates/adr-template.md)
- [`templates/rfc-template.md`](templates/rfc-template.md)
- [`templates/experiment-report-template.md`](templates/experiment-report-template.md)
- [`templates/systems-performance-report-template.md`](templates/systems-performance-report-template.md)
- [`templates/review-template.md`](templates/review-template.md)
- [`templates/rubric-scorecard-template.md`](templates/rubric-scorecard-template.md)
- [`templates/protocol-topology-decision-template.md`](templates/protocol-topology-decision-template.md)
- [`templates/slo-reliability-policy-template.md`](templates/slo-reliability-policy-template.md)
- [`templates/incident-postmortem-template.md`](templates/incident-postmortem-template.md)
- [`templates/disaster-recovery-review-template.md`](templates/disaster-recovery-review-template.md)
- [`templates/architecture-cost-model-template.md`](templates/architecture-cost-model-template.md)
- [`templates/migration-plan-template.md`](templates/migration-plan-template.md)
- [`templates/technical-strategy-memo-template.md`](templates/technical-strategy-memo-template.md)
- [`templates/runtime-comparison-report-template.md`](templates/runtime-comparison-report-template.md)
