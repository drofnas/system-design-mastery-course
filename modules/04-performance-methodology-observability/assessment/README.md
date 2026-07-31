# Module 4 Assessment

This assessment scores a learner's independent commerce investigation. The
Transit fixtures calibrate the evaluator and are never capstone exemplars.

## Submission bundle

Submit file paths and immutable commit identifiers for:

1. Frozen Week 13 investigation plan and baseline.
2. Instrumented Module 2 service, tests, schemas, and build review.
3. Raw telemetry bundles and hashes for baseline plus six hidden faults.
4. Blind diagnosis matrix frozen before fixture reveal.
5. Query-plan comparison, profiles, and instrumentation-overhead evidence.
6. Raw interleaved benchmark samples and regression-budget result.
7. Performance review and recorded teach-back.
8. Weekly learning logs, evaluator output, and separate remediation if needed.

## Structural gates

- **G01 — Identity:** commits, workload, environment, and assistance disclosure
  are present.
- **G02 — Preservation:** the baseline and blind diagnoses are frozen; revisions
  are separate.
- **G03 — Evidence contract:** raw signals, metadata, hashes, and schemas are
  present and internally consistent.
- **G04 — Blind fault work:** all six diagnoses cite evidence and predate reveal.
- **G05 — Validation:** equivalent-work checks, controlled candidate validation,
  and regression-budget arithmetic are reproducible.
- **G06 — Defense:** review, teach-back, feedback, ownership, and remediation
  records are present.

G02–G05 are hard gates. Their failure produces Repeat.

## Scoring and result

Use the [Module 4 rubric](rubric.md). Pass requires:

- every structural gate;
- average R01–R10 of at least 3.0;
- no zero in R06 or R07;
- stable workload and failure model during defense.

Revise addresses remediable evidence or reasoning gaps. Repeat is required when
preservation, raw evidence, blind diagnosis, equivalent work, or telemetry
safety fails. Follow the [remediation map](remediation-map.md) without replacing
the learner's graded answer.

## Evaluator use

The [provider-neutral prompt](evaluator-prompt.md) accepts only submitted files,
the rubric, and the shared evaluation schema. It must cite a submitted file and
heading for every gate and score, classify findings, express uncertainty, and
recommend lessons/exercises rather than authoring replacement work.
