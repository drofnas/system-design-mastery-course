# Module 15 Semantic and Resource Readiness Review

> **PESD 2.0 status: Review.** This pre-migration readiness record is historical, not a current Ready decision. Fresh evaluator repetitions, platform/offline/cleanup matrices, and timed learner pilots remain pending.

Review date: 2026-08-04
Historical decision (superseded): **Ready**

## Teaching and evidence review

- O1–O8 each map to local instruction, guided practice, independent evidence,
  and module-specific R01–R10 anchors.
- The Northstar case is non-capstone and contains no commerce architecture,
  thresholds, or canonical commerce answer. Learners freeze A01 before opening
  completed case material or explained answers.
- Weeks 57–60 total 46 hours. The package includes a worked example, guided and
  independent work, F01–F09 failure pairs, two comparison reports, an internals
  review, an ADR, a teach-back, module evaluation, remediation, and Gate 5.
- The runtime decision procedure covers security, operations, cost, ecosystem,
  ownership, migration, rollback, stopping conditions, and reversal evidence.
- Gate 5 reviews frozen Modules 13–15 evidence and creates no Week 60 capstone
  revision.

## Contract and implementation review

- All four services bind loopback and expose `/health`, `/fanout`, and
  `/telemetry/snapshot`.
- Strict request contracts reject unknown fields, invalid identifier shapes,
  invalid modes, excessive children, excessive payloads, and invalid deadlines
  before fan-out.
- Behavior tests cover ordered responses, bounded admission, non-expanding
  deadlines, cleanup counters, and TypeScript's erased-type boundary.
- Go runs under `-race`; Rust includes Send/Sync contrast material. Detector and
  compiler evidence are explicitly bounded and do not claim protocol proof.
- The measured scenario layer drives F01–F09 through actual loopback services.
  Each broken/repaired pair preserves runtime, seed, workload, limits, and
  shared-input hash while changing one test-only process control. Broken cases
  expose the named target and repaired cases restore it.
- Node.js 24.18.0, Go 1.26.5, Rust 1.97.1, and OpenJDK 25 image digests are
  recorded. TypeScript 7.0.2 replaces the planned unavailable 6.0 package; the
  language boundary and explicit runtime-validation objective are unchanged.

## Resource and integrity review

- RES-01–RES-17 were opened successfully on 2026-08-04. Required sources are
  free, bounded to named sections, assigned a purpose, time, week, evidence
  prompt, and local alternative. The scheduler video has captions and Lesson 2
  is its written alternative.
- Primary specifications and maintainer documentation support memory,
  scheduling, validation, virtual-thread, GC, release, and detector claims.
  Discord's case is explicitly historical and workload-specific.
- Review found no copied long-form source text, private learner data, secrets,
  capstone answer leakage, or title/promotion guarantee.

## Passing local gates

- `python3 -m unittest discover modules/15-execution-models-across-languages/lab/tests`
- `python3 modules/15-execution-models-across-languages/lab/run_conformance.py --mode all --runtime all --scenario all --output NEW_DIRECTORY`
- TypeScript build and behavior tests in Node.js 24.18.0
- Go tests with race detection in Go 1.26.5
- Rust locked tests in Rust 1.97.1
- Java compile and behavior tests in OpenJDK 25
- 22/22 clean-checkout measured outputs, with three excluded warmups, five
  measured repetitions, verified hashes, successful cleanup, and no remaining
  Module 15 containers
- `python3 scripts/validate_factual_readiness.py --module M15`
- `python3 scripts/validate_course.py --module M15`

## Calibration and readiness result

Pass, Revise, and Repeat were each evaluated twice in isolated, ephemeral,
read-only invocations after explicit authorization. The deterministic checker
accepted all six schema-valid records: Pass scored 3.0/3.0, Revise 2.5/2.5,
and Repeat 0.1/0.1. Result bands agree, maximum per-criterion drift is one,
and response, fixture, contract, prompt, and schema hashes are preserved in
`assessment/calibration/run-metadata.json`.

Focused and full-course validation pass. Semantic and resource review therefore
passes, and the historical review found the module ready for learners within its published evidence
boundary.
