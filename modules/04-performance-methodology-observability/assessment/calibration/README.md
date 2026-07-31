# Module 4 Evaluator Calibration

These fictional submissions use only Transit Signal. Expected bands remain
hidden from each evaluator invocation.

Run each fixture twice in an isolated context with the evaluator prompt, rubric,
remediation map, and shared schema. Preserve all six raw JSON outputs, then run:

```bash
python3 scripts/check_calibration.py --module M04 \
  modules/04-performance-methodology-observability/assessment/calibration/runs/run-1-pass.json \
  modules/04-performance-methodology-observability/assessment/calibration/runs/run-1-revise.json \
  modules/04-performance-methodology-observability/assessment/calibration/runs/run-1-repeat.json \
  modules/04-performance-methodology-observability/assessment/calibration/runs/run-2-pass.json \
  modules/04-performance-methodology-observability/assessment/calibration/runs/run-2-revise.json \
  modules/04-performance-methodology-observability/assessment/calibration/runs/run-2-repeat.json
```

Acceptance requires the expected result for every fixture, all citations to real
fixture headings, correct finding classes and remediation, exact arithmetic,
and no criterion drifting by more than one point between runs.
