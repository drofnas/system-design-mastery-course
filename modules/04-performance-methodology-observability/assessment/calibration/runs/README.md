# Module 4 Calibration Run Record

These six files are the structured outputs from independent, ephemeral
`gpt-5.6-sol` evaluator invocations on 2026-07-31. Each invocation was restricted
to the evaluator prompt, assessment gate contract, rubric, remediation map,
output schema, one submission manifest, and exactly one Transit Signal fixture.
It did not receive expected bands, another fixture, or a prior result.

| Run | Pass | Revise | Repeat |
|---:|---|---|---|
| 1 | [pass-run-1.json](pass-run-1.json) | [revise-run-1.json](revise-run-1.json) | [repeat-run-1.json](repeat-run-1.json) |
| 2 | [pass-run-2.json](pass-run-2.json) | [revise-run-2.json](revise-run-2.json) | [repeat-run-2.json](repeat-run-2.json) |

The repository checker validates result bands, arithmetic, fixture-only
citations, finding classes, remediation references, safety-critical reporting,
and per-criterion drift.
