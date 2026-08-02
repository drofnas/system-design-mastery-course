# Module 6 Evaluator Calibration

Beacon Dispatch provides Pass, Revise, and Repeat fixtures. Each fixture is
evaluated twice in a separate ephemeral evaluator context with the closest
available deterministic setting. Expected bands and earlier responses are
withheld from each evaluator. Exact raw responses and per-invocation provenance
are retained under `runs/`.

Run the deterministic verifier with:

```bash
python3 scripts/check_calibration.py --module M06 \
  modules/06-deadlines-resilient-remote-calls/assessment/calibration/runs/pass-run-1.json \
  modules/06-deadlines-resilient-remote-calls/assessment/calibration/runs/revise-run-1.json \
  modules/06-deadlines-resilient-remote-calls/assessment/calibration/runs/repeat-run-1.json \
  modules/06-deadlines-resilient-remote-calls/assessment/calibration/runs/pass-run-2.json \
  modules/06-deadlines-resilient-remote-calls/assessment/calibration/runs/revise-run-2.json \
  modules/06-deadlines-resilient-remote-calls/assessment/calibration/runs/repeat-run-2.json
```

Fixtures are deliberately non-commerce and cannot serve as capstone answers.
