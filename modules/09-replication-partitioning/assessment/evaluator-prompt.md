# Provider-Neutral Evaluator Prompt

Evaluate one Module 9 submission using only the submission manifest/files,
assessment contract, anchored rubric, remediation map, and shared
`schemas/evaluation.schema.json`. Northstar calibration files are permitted only
when the submitted manifest identifies one calibration fixture.

## Procedure

1. Resolve submission identity and A01–A10. Never infer missing evidence or hidden intent.
2. Evaluate G01–G06 before semantic scoring. G02–G05 failure is Repeat.
3. Score R01–R10 with integer anchors. Cite `path#heading: description` for every gate and score.
4. Recalculate the average and set `safety_critical_zero` from R07/R08.
5. Prefix every finding with exactly one allowed class: `missing_evidence`,
   `incorrect_reasoning`, `unsupported_claim`, `invariant_failure`,
   `internal_contradiction`, or `communication_gap`.
6. Recommend a named Lesson and EX exercise. Do not draft replacement graded content.
7. State confidence and uncertainty, especially where production, durability,
   consensus, legal, security, regional, or scale evidence is absent.
8. Return JSON only with exactly the shared-schema fields.

## Correctness rules

- Do not reward consistency, quorum, CAP, repair, or sharding vocabulary without
  histories, sets, versions, traces, movement/load calculations, and oracles.
- Never accept changed predictions, mismatched pair hashes, invalid arithmetic,
  lost concurrent state, session regression, non-convergence, missing keys,
  duplicate authority, or forbidden placement.
- Verify average, result band, citations, finding classes, and remediation agree.
- Accept a defensible alternative when its invariant, failure model, and evidence
  meet the rubric; never require Northstar's topology or thresholds.
