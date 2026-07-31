# Independent evaluator run record

This directory preserves six accepted structured evaluator outputs:

- `run-1-pass.json`, `run-1-revise.json`, and `run-1-repeat.json`
- `run-2-pass.json`, `run-2-revise.json`, and `run-2-repeat.json`

Do not fabricate these files or infer them from the expected score bands. Each
must be an independent deterministic evaluation of the matching Transit Signal
fixture using the published evaluator prompt, rubric, and shared schema.

`scripts/check_calibration.py --module
modules/02-capacity-queues-tail-latency` accepts all six files. See the
[calibration results](../results.md) for the method and score summary.
