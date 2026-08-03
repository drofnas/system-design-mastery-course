# Module 11 Evaluator Calibration

The fixtures use Northstar only and are not commerce answers. Evaluate
`pass.md`, `revise.md`, and `repeat.md` twice in isolated calls with the
published prompt, rubric, contract, remediation map, and shared schema.

Store six raw JSON responses under `runs/`, record unique isolation IDs, runtime
and deterministic settings, timestamps, and SHA-256 hashes. Then run:

```bash
python3 scripts/check_calibration.py --module M11 \
  assessment/calibration/runs/pass-run-1.json \
  assessment/calibration/runs/revise-run-1.json \
  assessment/calibration/runs/repeat-run-1.json \
  assessment/calibration/runs/pass-run-2.json \
  assessment/calibration/runs/revise-run-2.json \
  assessment/calibration/runs/repeat-run-2.json
```

Accept readiness only when bands match Pass/Revise/Repeat, detailed records
validate, and every category differs by at most one point.
