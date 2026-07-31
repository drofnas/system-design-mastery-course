# Module 3 Evaluator Calibration

## Contract

The fixtures use only the Transit replay-and-checkpoint case. They are evaluator
tests, not capstone exemplars. Keep expected bands hidden from the evaluator.

Run Pass, Revise, and Repeat twice in isolated read-only sessions with the same
rubric, evaluator prompt, schema, and deterministic settings where supported.
Preserve the six raw JSON objects in `runs/`, then run:

```text
python3 scripts/check_calibration.py --module modules/03-computer-systems-operating-systems
```

Both runs must match the expected band. Per-criterion scores may differ by at
most one point. The checker also rejects arithmetic, citation, finding-class,
safety, and remediation contradictions.

## Fixtures

- [Pass](pass.md): reproducible, bounded, causally defended evidence
- [Revise](revise.md): complete artifacts with insufficient causal and
  operational support
- [Repeat](repeat.md): broken prediction integrity and unsafe durability

These files intentionally summarize a submission bundle. Evaluators score only
their headings and must not import claims from lessons or answer keys.
