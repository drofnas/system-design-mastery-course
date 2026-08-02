# Module 10 Calibration Results

Two isolated evaluator passes produced stable expected bands:

| Fixture | Run 1 | Run 2 | Averages | Maximum category drift |
|---|---|---|---|---:|
| Pass | Pass | Pass | 3.2 / 3.3 | 1 |
| Revise | Revise | Revise | 2.2 / 2.4 | 1 |
| Repeat | Repeat | Repeat | 0.1 / 0.1 | 1 |

The deterministic checker validated schema fields, manifest identity, heading
citations, structural gates, averages, result rules, R08/R09 safety handling,
finding classes, remediation references, and cross-run drift. Raw records and
SHA-256 provenance are preserved under `runs/` and `run-metadata.json`.
