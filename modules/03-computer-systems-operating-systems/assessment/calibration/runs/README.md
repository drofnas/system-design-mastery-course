# Independent evaluator run record

This directory preserves six accepted structured evaluator outputs:

- `run-1-pass.json`, `run-1-revise.json`, and `run-1-repeat.json`
- `run-2-pass.json`, `run-2-revise.json`, and `run-2-repeat.json`

Each file is the unmodified output from an isolated read-only `gpt-5.6-sol`
evaluation of one Transit Signal fixture. The evaluator received the published
prompt, rubric, schema, and only the named fixture; expected bands were hidden.

`scripts/check_calibration.py --module M03` accepts all six files. See the
[calibration results](../results.md) for the method and score summary.
