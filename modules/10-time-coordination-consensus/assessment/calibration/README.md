# Module 10 Evaluator Calibration

The fixtures use Northstar only and are not commerce answers. `pass.md`,
`revise.md`, and `repeat.md` each have a fixture manifest. Evaluate each fixture
twice in isolated calls with the published prompt, rubric, contract, remediation
map, and shared schema.

Store six raw JSON responses under `runs/`, record unique isolation IDs, runtime
and deterministic settings, timestamps, and SHA-256 hashes. Then run:

```bash
python3 scripts/check_calibration.py --module M10 \
  pass-run-1.json revise-run-1.json repeat-run-1.json \
  pass-run-2.json revise-run-2.json repeat-run-2.json
```

Accept readiness only when bands match Pass/Revise/Repeat, all detailed records
validate, and each category differs by at most one point between runs.
