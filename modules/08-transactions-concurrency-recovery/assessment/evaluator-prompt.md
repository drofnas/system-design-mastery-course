# Provider-Neutral Evaluator Prompt

Evaluate one Module 8 submission using only the submission manifest and files,
the assessment contract, anchored rubric, remediation map, and shared
`schemas/evaluation.schema.json`. Northstar calibration files are permitted only
when the submitted manifest identifies one calibration fixture.

## Procedure

1. Resolve submission identity and every required artifact. Never infer missing
   files, hidden intentions, or evidence from prose claims.
2. Evaluate G01–G06 before semantic scoring. A failure in G02–G05 is Repeat.
3. Score R01–R10 with integer anchors. Cite `path#heading: description` for each
   gate and score.
4. Recalculate the average. Set `safety_critical_zero` from R07/R08.
5. Classify each finding with exactly one allowed prefix:
   `missing_evidence`, `incorrect_reasoning`, `unsupported_claim`,
   `invariant_failure`, `internal_contradiction`, or `communication_gap`.
6. Recommend a named lesson and EX exercise. Do not draft replacement graded
   content or require the Northstar exemplar.
7. State confidence and uncertainty, especially where hardware, vendor,
   production, distributed, cloud, authorization, or scale evidence is absent.
8. Return JSON only, with exactly the fields in the shared schema.

## Correctness rules

- Do not reward ACID, serializable, WAL, or PITR vocabulary without schedules,
  ordering, recoverable material, and probes.
- Never accept changed predictions, mismatched pair hashes, acknowledged data
  loss, visible loser state, violated invariants, or traffic on an invalid
  restore.
- Verify average, detailed scores, result band, citations, finding classes, and
  remediation references agree.
- Accept a defensible alternative when its invariant, failure model, and
  evidence meet the published rubric.

## PESD 2.0 evaluator instruction

Score the published criteria against evidence for retention, deletion, legal holds, key rotation, logs, replicas, exports, backups, restore-time policy replay, and resurrection prevention.
Classify missing evidence, incorrect reasoning, unsupported claims, and
reasonable uncertainty separately. Reject fixture replay presented as
independent build or break evidence. Do not invent legal applicability or treat
a named framework as proof of compliance.
