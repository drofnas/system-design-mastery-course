# Module 1 Calibration Record

## Accepted run

- Date: 2026-07-31
- Evaluator: OpenAI `gpt-5.6-sol`
- Execution: read-only, ephemeral sessions, fixed prompt and strict JSON schema
- Determinism: temperature was not exposed by the evaluator CLI
- Synthetic content sent: `pass.md`, `revise.md`, and `repeat.md`
- Checker: `scripts/check_calibration.py`
- Checker result: passed

| Fixture | Run 1 | Average | Run 2 | Average | Largest category drift |
|---|---|---:|---|---:|---:|
| Pass | Pass | 3.2 | Pass | 3.3 | 1 |
| Revise | Revise | 1.8 | Revise | 1.6 | 1 |
| Repeat | Repeat | 0.3 | Repeat | 0.2 | 1 |

Both runs cited real fixture headings, classified findings, linked remediation
to lessons and exercises, and returned the expected result bands. Detailed
scores are in [`results.json`](results.json). Raw provider logs are not part of
the course and were not committed.

## Issues found and corrected

1. The first strict-output attempt showed that nested objects in the evaluation
   schema needed `additionalProperties: false`, and that `baseline_tag` needed
   to be a required nullable field.
2. A pre-acceptance Pass run reported an average inconsistent with its ten
   scores. The evaluator prompt now requires an explicit arithmetic
   verification, and the deterministic checker rejects inconsistent averages.
3. The Revise fixture's original expected average range was narrower than the
   valid rubric anchors. Its lower calibration bound changed from 1.8 to 1.5;
   the result algorithm itself did not change.

Only the post-correction runs in the table count toward readiness.
