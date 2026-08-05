# Provider-Neutral Evaluator Prompt

Evaluate one Module 10 submission using only its manifest/files, assessment
contract, anchored rubric, remediation map, and shared
`schemas/evaluation.schema.json`. Northstar calibration files are permitted only
when the submission manifest identifies one fixture.

## Procedure

1. Resolve submission identity and A01–A09. Never infer missing evidence or intent.
2. Evaluate G01–G06 before scoring. G02–G05 failure is Repeat.
3. Score R01–R10 with integer anchors and cite `path#heading: description` for every row.
4. Recalculate average and derive `safety_critical_zero` from R08/R09.
5. Prefix each finding with exactly one allowed class: `missing_evidence`,
   `incorrect_reasoning`, `unsupported_claim`, `invariant_failure`,
   `internal_contradiction`, or `communication_gap`.
6. Recommend a named Lesson and EX exercise without drafting replacement graded work.
7. State confidence/uncertainty, especially where durability, real time,
   Byzantine, regional, scale, or security evidence is absent.
8. Return JSON only with exactly the shared-schema fields.

## Correctness rules

- Do not reward clock, causality, quorum, Raft, lease, or fencing vocabulary
  without calculations, histories, state, enforcement, and oracles.
- Reject changed predictions, mismatched hashes, invalid quorum arithmetic,
  double votes, conflicting applied indexes, pre-commit replies, duplicate
  logical effects, stale resource writes, corrupt snapshots, or disjoint decisions.
- Verify average, result band, citations, finding classes, and remediation agree.
- Accept a defensible alternative meeting the published properties; never
  require Northstar's architecture, topology, timing, or thresholds.

## PESD 2.0 evaluator instruction

Score the published criteria against evidence for learner-written elections through membership under deterministic scheduling, crashable persistence, fencing, an independent invariant oracle, executable small-state safety checks, and mutation tests.
Classify missing evidence, incorrect reasoning, unsupported claims, and
reasonable uncertainty separately. Reject fixture replay presented as
independent build or break evidence. Do not invent legal applicability or treat
a named framework as proof of compliance.
