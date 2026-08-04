# Module 2 Assessment

## Purpose

Assessment determines whether the learner can predict, measure, diagnose, and
govern a finite-capacity system. It does not reward a particular utilization
percentage, programming style, or cloud architecture.

## Files

- [Rubric](rubric.md): Module 2 score anchors and remediation
- [Evaluator prompt](evaluator-prompt.md): evidence-bound review contract
- [Report template](report-template.md): saved human-readable result
- [Remediation map](remediation-map.md): new evidence paths that preserve frozen work
- [Evaluation schema](../../../schemas/evaluation.schema.json): JSON contract
- [Calibration fixtures](calibration/README.md): Transit Signal Pass, Revise,
  and Repeat cases

## Required input bundle

- Frozen Week 5 capacity prediction and its commit
- Capacity-planning output
- Service, load driver, configurations, and automated tests
- Raw request-attempt JSONL and trial summaries
- Required nine-point load sweep
- Slow, burst, queue, retry, downstream-limit, and failover experiments
- Failure matrix and experiment report
- Capacity report and overload-policy ADR
- Defense record, evaluation target, and separate revision
- Weeks 5–8 learning logs
- Commit identifiers for all graded artifacts

## Evaluation sequence

1. Run course and lab validation.
2. Verify the prediction predates raw experiment evidence.
3. Verify the complete artifact set and raw-data integrity.
4. Apply the structural gates.
5. Score only submitted evidence against R01–R10.
6. Apply the fixed result algorithm.
7. Save schema-conforming JSON and the Markdown report.
8. Remediate in a new artifact.

## Results

- **Pass:** every gate passes, mean score is at least 3.0, R06 and R07 are not
  zero, and the defense preserves the submitted workload and failure model.
- **Revise:** the artifact set exists, but weak measurement, diagnosis, or
  decision evidence prevents a defensible capacity claim.
- **Repeat:** prediction or required evidence is missing, overload/retry safety
  fails, raw evidence is altered or invented, or the model is materially false.

## Evaluation packaging and independence

Use the [provider-neutral bundle and validation workflow](../../../EVALUATION_GUIDE.md). The evaluator returns JSON only; the validator renders the report. An independent LLM or human critique after the freeze is required for formal Pass. Self-scoring remains provisional.
