# Module 2 Evaluator Calibration Results

Calibration passed on 2026-07-31 using two independent ephemeral OpenAI Codex
sessions per fictional Transit Signal fixture. Evaluators received the fixed
prompt, rubric, shared output schema, and one fixture at a time. Expected bands
were not included in evaluator inputs.

## Execution

- Provider/model: OpenAI `gpt-5.6-sol`
- Temperature: not exposed by the evaluator CLI
- Filesystem: read-only temporary directory containing only authorized
  calibration material
- Session persistence: ephemeral
- Structured output: `schemas/evaluation.schema.json`
- Deterministic checker: `scripts/check_calibration.py --module M02`

## Accepted results

| Fixture | Run 1 | Average | Run 2 | Average | Maximum criterion drift |
|---|---|---:|---|---:|---:|
| Pass | Pass | 3.4 | Pass | 3.6 | 1 |
| Revise | Revise | 2.0 | Revise | 1.9 | 1 |
| Repeat | Repeat | 0.2 | Repeat | 0.2 | 1 |

The checker confirmed exact rubric coverage, gate/result consistency, arithmetic,
safety-critical reporting, real fixture headings, approved finding classes,
lesson/exercise remediation, expected bands, and category drift no greater than
one point. The six unmodified structured outputs are preserved in
[the run record](runs/README.md).

## Calibration correction

The first draft of the Revise fixture explicitly omitted required measurement
fields and the failover experiment. The published gate algorithm therefore
correctly returned Repeat. The fixture was corrected before the accepted runs so
that all structural evidence exists while its semantic reasoning remains weak.
No evaluator result was edited to obtain the expected band.

## Readiness conclusion

The evaluator distinguishes complete evidence, remediable judgment gaps, and
hard integrity or safety failures without rewarding vocabulary alone or
requiring one canonical architecture. Calibration is accepted for Module 2.
