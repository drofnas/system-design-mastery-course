# Module 1 Assessment

## Purpose

Assessment determines whether the learner can frame, compare, challenge, and
defend an architecture decision. It does not compare the submission with one
canonical design.

## Files

- [Rubric](rubric.md): module-specific 0–4 anchors and remediation
- [Evaluator prompt](evaluator-prompt.md): provider-neutral review contract
- [Report template](report-template.md): human-readable saved result
- [Remediation map](remediation-map.md): new evidence paths that preserve frozen work
- [Evaluation schema](../../../schemas/evaluation.schema.json): structured result
- [Calibration fixtures](calibration/README.md): Pass, Revise, and Repeat cases

## Required input bundle

- Frozen Week 1 baseline and `week-01-baseline` tag
- Week 2 candidate-design report
- Practice ADR
- Week 3 failure review and evidence ledger
- Baseline review
- Week 4 RFC
- Defense record and revision log
- Four learning logs
- Git commit identifiers for every graded artifact

## Evaluation sequence

1. Run repository validation.
2. Verify the baseline tag and artifact immutability.
3. Run structural gates.
4. Score semantic criteria using cited submission evidence.
5. Apply the fixed result rules.
6. Save JSON conforming to the evaluation schema.
7. Save a Markdown report from the report template.
8. Perform remediation in a new artifact.

## Result rules

- **Pass:** all structural gates pass, average score is at least 3.0, no
  safety-critical criterion is 0, and defense answers preserve submitted
  assumptions.
- **Revise:** artifacts exist but evidence, causal reasoning, measurement, or
  communication prevents a defensible decision.
- **Repeat:** a required artifact or freeze gate is missing, a safety property
  fails, or the design depends on a materially false model.

An experienced human reviewer is encouraged. The LLM evaluator is sufficient
for formal self-study only when it follows the prompt and produces cited,
schema-conforming output.

## Evaluation packaging and independence

Use the [provider-neutral bundle and validation workflow](../../../EVALUATION_GUIDE.md). The evaluator returns JSON only; the validator renders the report. An independent LLM or human critique after the freeze is required for formal Pass. Self-scoring remains provisional.
