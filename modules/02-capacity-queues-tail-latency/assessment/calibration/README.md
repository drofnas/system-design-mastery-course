# Module 2 Evaluator Calibration

These Transit Signal fixtures test result bands without exposing commerce
answers.

- [`pass.md`](pass.md): complete, measured, bounded decision
- [`revise.md`](revise.md): complete structure with weak measurement and policy
- [`repeat.md`](repeat.md): missing prediction/raw evidence and unbounded retry
- [`expected-results.json`](expected-results.json): fixed bands and score ranges
- [Run record](runs/README.md): two accepted deterministic evaluator runs
- [`results.json`](results.json): machine-readable checker summary
- [`results.md`](results.md): calibration method and accepted results

Run:

```bash
python3 scripts/check_calibration.py \
  --module modules/02-capacity-queues-tail-latency \
  assessment/calibration/runs/run-1-pass.json \
  assessment/calibration/runs/run-1-revise.json \
  assessment/calibration/runs/run-1-repeat.json \
  assessment/calibration/runs/run-2-pass.json \
  assessment/calibration/runs/run-2-revise.json \
  assessment/calibration/runs/run-2-repeat.json
```

Run from the repository root. Do not assess learner work unless both bands
agree and every category differs by at most one. The accepted Module 2 runs
satisfy both requirements.
