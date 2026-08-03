# Module 12 Evaluator Calibration

The fixtures use Northstar only. They intentionally differ in evidence quality,
not architecture preference. Each fixture manifest freezes submission identity
and assistance. Run every fixture twice with deterministic settings, preserve
all six raw JSON outputs, then run `scripts/check_calibration.py`.

- `pass.md` contains complete, consistent, adversarially tested evidence.
- `revise.md` has no hard/safety failure but lacks enough traceability and depth.
- `repeat.md` fails chronology, recovery safety, and hard gates.

The result band must agree across both runs and each criterion may differ by at
most one point. Structured output is rejected when averages, gates, citations,
finding classes, safety flags, or remediation contradict detailed scores.
