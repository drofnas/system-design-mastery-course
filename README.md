# Principal Engineer and Systems Design Mastery

This repository is the working record for the 72-week
**Principal Engineer and Systems Design Mastery** course. The authoritative
course requirements are in [`00_COURSE_SYLLABUS.md`](00_COURSE_SYLLABUS.md).

## Current milestone

The course is at **Week 1: Architectural Judgment**.

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
5. Continue Module 1 through its Week 4 RFC, defense, and assessment.

The baseline is evidence of initial judgment. Once tagged, it must never be
edited. Revised designs belong in new Week 24, Week 48, and Week 72 files.

## Standard cadence

- Duration: 72 weeks
- Weekly effort: 10–12 hours
- Module length: four weeks

| Week in module | Focus | Evidence |
|---:|---|---|
| 1 | Model | Vocabulary, assumptions, diagrams, estimates, source review |
| 2 | Build | Minimal implementation exposing the mechanism |
| 3 | Break and measure | Failure injection, load, and measurement |
| 4 | Decide and teach | ADR or RFC, review, feedback, and revision |

A normal week allocates 2–3 hours to reading and notes, 3–4 hours to
implementation, 2 hours to experiments, 1–2 hours to decision writing, and
1 hour to review and the learning log.

## Assessment gates

| Gate | Week | Focus |
|---:|---:|---|
| 1 | 12 | Judgment, capacity, and computer systems |
| 2 | 24 | Performance, networks, and remote calls |
| 3 | 36 | Storage, transactions, replication, and partitioning |
| 4 | 48 | Consensus, messaging, reliability, and recovery |
| 5 | 60 | Security, evolution, economics, and runtimes |
| 6 | 72 | Browser, edge, AI systems, and capstone |

Each gate requires a written examination, practical exercise, architecture
defense, and portfolio review. The passing average is 3 out of 4, with no zero
on a safety-critical artifact. The final capstone requires 3.5 out of 4.

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
modules/        Complete four-week teaching and assessment packages
schemas/        Machine-readable module and evaluation contracts
scripts/        Course validation tools
```

## Module catalog

| Module | Weeks | Status | Entry point |
|---:|---:|---|---|
| 1. Architectural Judgment | 1–4 | Ready | [Start Module 1](modules/01-architectural-judgment/README.md) |
| 2. Capacity, Queues, and Tail Latency | 5–8 | Ready | [Start Module 2](modules/02-capacity-queues-tail-latency/README.md) |
| 3. Computer Systems and Operating Systems | 9–12 | Ready | [Start Module 3](modules/03-computer-systems-operating-systems/README.md) |
| 4. Performance Methodology and Observability | 13–16 | Ready | [Start Module 4](modules/04-performance-methodology-observability/README.md) |
| 5. Network Foundations | 17–20 | Ready | [Start Module 5](modules/05-network-foundations/README.md) |
| 6. Deadlines and Resilient Remote Calls | 21–24 | Ready | [Start Module 6](modules/06-deadlines-resilient-remote-calls/README.md) |
| 7. Data Models and Storage Engines | 25–28 | Ready | [Start Module 7](modules/07-data-models-storage-engines/README.md) |
| 8. Transactions, Concurrency, and Recovery | 29–32 | Ready | [Start Module 8](modules/08-transactions-concurrency-recovery/README.md) |
| 9–18 | 33–72 | Syllabus-defined; teaching packages not yet authored | [Course syllabus](00_COURSE_SYLLABUS.md) |

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
local Markdown links. Use `--module M01` through `--module M08` to validate a
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

## Templates

- [`templates/learning-log-template.md`](templates/learning-log-template.md)
- [`templates/adr-template.md`](templates/adr-template.md)
- [`templates/rfc-template.md`](templates/rfc-template.md)
- [`templates/experiment-report-template.md`](templates/experiment-report-template.md)
- [`templates/systems-performance-report-template.md`](templates/systems-performance-report-template.md)
- [`templates/review-template.md`](templates/review-template.md)
- [`templates/rubric-scorecard-template.md`](templates/rubric-scorecard-template.md)
- [`templates/protocol-topology-decision-template.md`](templates/protocol-topology-decision-template.md)
