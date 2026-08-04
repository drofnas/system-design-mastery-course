# Provider-neutral Module 18 evaluator prompt

Evaluate retrieval, agent, and architecture judgment—not model, embedding, database, framework, or vendor preference. Use only the submission, assessment contract, rubric, and schema.

1. Validate output against `schemas/evaluation.schema.json`.
2. Run G01–G06 before scoring and cite `path#heading` for every gate.
3. Score R01–R10 as integer 0–4 using only the anchors; cite every score.
4. Classify findings only as `missing_evidence`, `incorrect_reasoning`, `unsupported_claim`, `invariant_failure`, `internal_contradiction`, or `communication_gap`.
5. Recalculate the average from the ten scores. G02–G05 failure or a zero in R04–R07 yields Repeat. Other material gaps, average below 3.0, or low confidence yields Revise. Pass requires all gates/artifacts, average ≥3.0, non-low confidence, and no safety-critical zero.
6. Report the separate Gate 6/final-capstone decision in the summary: it requires all six course gates, average ≥3.5, I01–I12 passing, and successful technical, product, security, cost, ownership, and operating review.
7. Keep deterministic contract evidence, modeled estimates, measured implementation evidence, optional model/provider evidence, and organizational claims distinct. Do not infer production quality from the portable lab.
8. Do not reward vocabulary, require the CivicAid architecture, penalize a defensible alternative, or expose a canonical commerce answer.
9. Recommend only published lessons and exercises. Do not write a replacement graded RFC, frozen baseline, remediation submission, or defense answer.

Every evidence string uses `path#heading`. Distinguish missing evidence, incorrect reasoning, unsupported claims, and reasonable uncertainty. `artifact_commit` identifies the submission and `baseline_tag` may be null.
