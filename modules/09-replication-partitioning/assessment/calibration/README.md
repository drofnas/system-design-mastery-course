# Module 9 Evaluator Calibration

The Pass, Revise, and Repeat fixtures use Northstar and cannot be submitted as a
commerce answer. Each fixture has an immutable manifest. Run each twice with
identical supported settings, preserve raw JSON and SHA-256, then run:

```bash
python3 scripts/check_calibration.py --module M09 \
  pass-run-1.json pass-run-2.json revise-run-1.json revise-run-2.json \
  repeat-run-1.json repeat-run-2.json
```

Expected bands must agree and category scores may differ by at most one point.
The checker also verifies averages, gates, safety zero, citations, finding
classes, remediation references, confidence, and result logic.
