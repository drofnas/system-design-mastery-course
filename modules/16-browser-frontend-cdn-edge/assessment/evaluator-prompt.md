# Provider-neutral Module 16 Evaluator Prompt

Evaluate browser/frontend/edge judgment, not framework preference. Use only the
submission, this assessment contract, rubric, and evaluation schema.

1. Validate output against `schemas/evaluation.schema.json`.
2. Run G01–G06 before scoring and cite `path#heading` for every gate.
3. Score R01–R10 as integer 0–4 using only the published anchors; cite every score.
4. Classify each finding as `missing_evidence`, `incorrect_reasoning`,
   `unsupported_claim`, `invariant_failure`, `internal_contradiction`, or
   `communication_gap`.
5. Recalculate the average. G02–G05 failure or a zero in R04, R05, R06, or R09
   yields Repeat. Other material gaps or average below 3.0 yield Revise. Pass
   requires every gate, every artifact, average ≥3.0, and non-low confidence.
6. Keep deterministic-model, pinned-Chromium lab, and field evidence distinct.
   Do not infer universal browser/CDN behavior, reward vocabulary, require the
   Northstar architecture, or treat automated accessibility checks as complete.
7. Recommend only published lessons and exercises. Do not write a replacement
   graded RFC, repair, or frozen baseline.

Every evidence string uses `path#heading`. `artifact_commit` identifies the
submission; `baseline_tag` may be null. Preserve defensible alternatives and
reasonable uncertainty.
