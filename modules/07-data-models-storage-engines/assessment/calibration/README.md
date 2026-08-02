# Module 7 Evaluator Calibration

Harbor Signal Archive provides Pass, Revise, and Repeat fixtures. Evaluate each
fixture twice in a separate isolated evaluator context using the closest
deterministic setting. Withhold expected bands, other fixtures, and previous
responses. Preserve exact raw responses and invocation provenance under `runs/`.

Run the deterministic verifier with:

```bash
python3 scripts/check_calibration.py --module M07 \
  modules/07-data-models-storage-engines/assessment/calibration/runs/pass-run-1.json \
  modules/07-data-models-storage-engines/assessment/calibration/runs/revise-run-1.json \
  modules/07-data-models-storage-engines/assessment/calibration/runs/repeat-run-1.json \
  modules/07-data-models-storage-engines/assessment/calibration/runs/pass-run-2.json \
  modules/07-data-models-storage-engines/assessment/calibration/runs/revise-run-2.json \
  modules/07-data-models-storage-engines/assessment/calibration/runs/repeat-run-2.json
```

Fixtures are deliberately municipal and cannot serve as commerce answers.
