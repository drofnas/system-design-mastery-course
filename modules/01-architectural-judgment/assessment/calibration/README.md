# Evaluator Calibration

These fixtures use Transit Signal and do not reveal commerce-capstone answers.
They are intentionally abbreviated bundles but contain explicit simulated
structural-gate status.

Run each fixture twice with deterministic settings where available.

Expected behavior:

- Result band matches [`expected-results.json`](expected-results.json).
- R01–R10 scores between two runs differ by no more than one point.
- Every score cites a real fixture heading.
- Findings are classified.
- Remediation points to Module 1 lessons/exercises.
- No response writes a replacement submission.
- `average_score` exactly equals the arithmetic mean of R01–R10.

After producing six JSON files, run:

```text
python3 scripts/check_calibration.py \
  run1-pass.json run1-revise.json run1-repeat.json \
  run2-pass.json run2-revise.json run2-repeat.json
```

Do not mark the evaluator calibrated unless this command passes. Preserve a
summary of the model, date, result bands, averages, score drift, and checker
result in `results.md`; do not commit provider credentials or raw session logs.

The accepted Module 1 run is recorded in [`results.md`](results.md), with
machine-readable scores in [`results.json`](results.json).

Fixtures:

- [`pass.md`](pass.md)
- [`revise.md`](revise.md)
- [`repeat.md`](repeat.md)
