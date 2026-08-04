# Module 3 Evaluator Calibration Results

Calibration passed on 2026-07-31 using two independent isolated OpenAI
`gpt-5.6-sol` sessions per fictional Transit Signal fixture. Evaluators received
the fixed prompt, rubric, shared output schema, and one fixture at a time. The
expected result bands were hidden during scoring.

## Execution

- Provider/model: OpenAI `gpt-5.6-sol`
- Temperature: not exposed by the evaluator runtime
- Filesystem: read-only evaluation context
- Session persistence: isolated session per fixture and run
- Structured output: `schemas/evaluation.schema.json`
- Deterministic checker: `scripts/check_calibration.py --module M03`

## Accepted results

| Fixture | Run 1 | Average | Run 2 | Average | Maximum criterion drift |
|---|---|---:|---|---:|---:|
| Pass | Pass | 3.4 | Pass | 3.8 | 1 |
| Revise | Revise | 2.3 | Revise | 2.1 | 1 |
| Repeat | Repeat | 0.0 | Repeat | 0.0 | 0 |

The checker confirmed exact rubric coverage, gate/result consistency, arithmetic,
safety-critical reporting, citations to real fixture headings, approved finding
classes, lesson/exercise remediation, expected bands, and category drift no
greater than one point. The six unmodified structured outputs are preserved in
[the run record](runs/README.md).

## Readiness conclusion

The evaluator distinguishes reproducible evidence, remediable causal and
decision gaps, and hard prediction, evidence, concurrency, and durability
failures. It neither rewards mechanism vocabulary alone nor requires a single
architecture. Calibration is accepted for Module 3.
