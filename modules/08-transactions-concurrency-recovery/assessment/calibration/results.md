# Module 8 Calibration Results

Two evaluator passes produced stable expected bands:

| Fixture | Run 1 | Run 2 | Averages | Maximum category drift |
|---|---|---|---|---:|
| Pass | Pass | Pass | 3.8 / 3.7 | 1 |
| Revise | Revise | Revise | 2.3 / 2.2 | 1 |
| Repeat | Repeat | Repeat | 0.1 / 0.1 | 0 |

The deterministic checker passed after validating shared-schema fields,
manifest identity, headings/citations, structural gates, averages, result
rules, safety-critical R07/R08, finding classes, remediation references, and
cross-run drift. Raw records and SHA-256 provenance are preserved under `runs/`
and `run-metadata.json`.
