# Module 3 Assessment

> **PESD 2.0 evaluation ownership:** G01 invokes this module-specific rubric and evaluator exactly once as its domain score. Do not run or submit a separate module semantic evaluation report.

## Purpose

Assessment determines whether the learner can connect measured systems
behavior to a bounded production decision. It does not reward a particular
processor, operating system, filesystem, container runtime, or faster result.

## Files

- [Rubric](rubric.md): Module 3 score anchors and remediation
- [Evaluator prompt](evaluator-prompt.md): evidence-bound review contract
- [Report template](report-template.md): saved human-readable result
- [Remediation map](remediation-map.md): new evidence paths that preserve frozen work
- [Gate 1](../../../gates/G01/assessment-brief.md): written exam, Transit practical, architecture defense,
  and portfolio review
- [Evaluation schema](../../../schemas/evaluation.schema.json): JSON contract
- [Calibration fixtures](calibration/README.md): Transit Signal Pass, Revise,
  and Repeat cases

## Required input bundle

- Frozen Week 12 benchmark prediction and its commit
- Machine inventory, source, build flags, scenarios, and automated tests
- Raw `systems-trial` JSON for the required matrix and repetition summaries
- Equivalent-work, safety, timeout, and sanitizer evidence
- Failure matrix and counterintuitive-result report
- Systems-performance decision artifact with rollout, rollback, cost, owners,
  and reversal conditions
- Recorded teach-back, challenge record, evaluation target, and separate revision
- Weeks 11–15 learning logs
- Gate 1 artifacts when Gate 1 is being assessed
- Commit identifiers for all graded artifacts

## Evaluation sequence

1. Run course validation, native tests, sanitizer checks, and the required
   Linux-container checks.
2. Verify the prediction predates raw experiment evidence.
3. Verify the complete artifact set and raw-data integrity.
4. Apply the six structural gates.
5. Score only submitted evidence against R01–R10.
6. Apply the fixed result algorithm.
7. Save schema-conforming JSON and the Markdown report.
8. Remediate in a new artifact; never replace the frozen prediction or raw data.

## Results

- **Pass:** every gate passes, mean score is at least 3.0, and R06 and R07 are
  not zero.
- **Revise:** the complete artifact set exists, but weak evidence, causal
  diagnosis, or decision reasoning prevents a defensible systems claim.
- **Repeat:** prediction or required evidence is missing, raw evidence is
  altered or invented, concurrency or durability safety fails, required work is
  unbounded, or the machine model is materially false.

## Evaluation packaging and independence

Use the [provider-neutral bundle and validation workflow](../../../EVALUATION_GUIDE.md). The evaluator returns JSON only; the validator renders the report. A frozen self-evaluated Pass establishes **Solo Complete** and remains explicitly self-attested. A passing independent human or LLM review of the same bundle establishes **Independently Validated**.
