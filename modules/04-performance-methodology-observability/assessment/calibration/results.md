# Module 4 Evaluator Calibration Results

Calibration passed on 2026-07-31 using two independent isolated OpenAI
`gpt-5.6-sol` invocations per fictional Transit Signal fixture. Evaluators
received fixed inputs and one fixture at a time; expected bands were hidden.

## Execution

- Provider/model: OpenAI `gpt-5.6-sol`
- Temperature: not exposed by the evaluator runtime
- Input boundary: isolated invocation restricted to the manifest-listed files
- Session persistence: ephemeral, isolated invocation per fixture and run
- Structured output: `schemas/evaluation.schema.json`
- Deterministic checker: `scripts/check_calibration.py --module M04`

## Accepted results

| Fixture | Run 1 | Average | Run 2 | Average | Maximum criterion drift |
|---|---|---:|---|---:|---:|
| Pass | Pass | 3.7 | Pass | 3.6 | 1 |
| Revise | Revise | 1.9 | Revise | 2.0 | 1 |
| Repeat | Repeat | 0.0 | Repeat | 0.0 | 0 |

The checker confirmed exact gate and rubric coverage, result arithmetic,
safety-critical reporting, citations to real fixture headings, approved finding
classes, lesson/exercise remediation, expected bands, and no category drift
greater than one point. The six unmodified outputs are preserved in the
[run record](runs/README.md).

## Readiness conclusion

The evaluator separates strong causal evidence, remediable investigation gaps,
and hard baseline, blind-diagnosis, evidence-integrity, and validation failures.
It does not reward observability vocabulary without a causal model or require a
single architecture. Calibration is accepted for Module 4.
