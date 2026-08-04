# Module 9 Calibration Results

Two evaluator passes produced stable expected bands:

| Fixture | Run 1 | Run 2 | Averages | Maximum category drift |
|---|---|---|---|---:|
| Pass | Pass | Pass | 3.1 / 3.1 | 1 |
| Revise | Revise | Revise | 2.4 / 2.5 | 1 |
| Repeat | Repeat | Repeat | 0.2 / 0.1 | 1 |

The deterministic checker validated schema fields, manifest identity, heading
citations, structural gates, averages, result rules, R07/R08 safety handling,
finding classes, remediation references, and cross-run drift. Raw records and
SHA-256 provenance are preserved under `runs/` and `run-metadata.json`.
