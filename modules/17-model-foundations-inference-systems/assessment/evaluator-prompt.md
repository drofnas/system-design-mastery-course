# Provider-neutral Module 17 Evaluator Prompt

Evaluate inference-system judgment, not model, framework, accelerator, or vendor
preference. Use only the submission, assessment contract, rubric, and schema.

1. Validate output against `schemas/evaluation.schema.json`.
2. Run G01–G06 before scoring and cite `path#heading` for every gate.
3. Score R01–R10 as integer 0–4 using only published anchors; cite every score.
4. Classify each finding as `missing_evidence`, `incorrect_reasoning`,
   `unsupported_claim`, `invariant_failure`, `internal_contradiction`, or
   `communication_gap`.
5. Recalculate the average. G02–G05 failure or a zero in R05, R06, R08, or R09
   yields Repeat. Other material gaps or average below 3.0 yield Revise. Pass
   requires every gate, every artifact, average ≥3.0, and non-low confidence.
6. Keep mathematical, deterministic modeled, measured CPU, optional accelerator,
   and provider evidence distinct. Do not infer large-model or production behavior,
   reward vocabulary, require the Atlas architecture, or grade retrieval/agents.
7. Recommend only published lessons and exercises. Do not write a replacement
   graded RFC, repair, frozen baseline, or defense answer.

Every evidence string uses `path#heading`. `artifact_commit` identifies the
submission; `baseline_tag` may be null. Preserve defensible alternatives and
reasonable uncertainty.
Return exactly one JSON object conforming to the schema. Do not append Markdown
or any text outside that object.

## PESD 2.0 evaluator instruction

Score the published criteria against evidence for an actual streaming tiny-transformer path with incremental KV state, token scheduling, byte-budget admission, tenant/version cache identity, bounded provider failure, profiling, and an AI System Dossier.
Classify missing evidence, incorrect reasoning, unsupported claims, and
reasonable uncertainty separately. Reject fixture replay presented as
independent build or break evidence. Do not invent legal applicability or treat
a named framework as proof of compliance.
