# Module 4 Evaluator Calibration

These fictional submissions use only Transit Signal. Expected bands remain
hidden from each evaluator invocation.

Run each fixture twice in an isolated context with the evaluator prompt, rubric,
remediation map, and shared schema. Preserve all six raw JSON outputs, then run:

```bash
python3 scripts/check_calibration.py --module M04 \
  modules/04-performance-methodology-observability/assessment/calibration/runs/pass-run-1.json \
  modules/04-performance-methodology-observability/assessment/calibration/runs/revise-run-1.json \
  modules/04-performance-methodology-observability/assessment/calibration/runs/repeat-run-1.json \
  modules/04-performance-methodology-observability/assessment/calibration/runs/pass-run-2.json \
  modules/04-performance-methodology-observability/assessment/calibration/runs/revise-run-2.json \
  modules/04-performance-methodology-observability/assessment/calibration/runs/repeat-run-2.json
```

Acceptance requires the expected result for every fixture, all citations to real
fixture headings, correct finding classes and remediation, exact arithmetic,
and no criterion drifting by more than one point between runs.

The accepted [summary](results.md), machine-readable
[results](results.json), and [six-run record](runs/README.md) were verified on
2026-07-31.
