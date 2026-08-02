# Module 5 Evaluator Calibration

These Transit Signal fixtures test result bands without exposing commerce
answers. Evaluate Pass, Revise, and Repeat twice in separate deterministic
contexts with expected bands hidden. Preserve six raw JSON objects under
`runs/`, then run:

```bash
python3 scripts/check_calibration.py --module M05 \
  modules/05-network-foundations/assessment/calibration/runs/pass-run-1.json \
  modules/05-network-foundations/assessment/calibration/runs/revise-run-1.json \
  modules/05-network-foundations/assessment/calibration/runs/repeat-run-1.json \
  modules/05-network-foundations/assessment/calibration/runs/pass-run-2.json \
  modules/05-network-foundations/assessment/calibration/runs/revise-run-2.json \
  modules/05-network-foundations/assessment/calibration/runs/repeat-run-2.json
```

The checker validates schema parity, citations, finding classes, remediation,
arithmetic, safety outcomes, bands, and maximum one-point category drift.
