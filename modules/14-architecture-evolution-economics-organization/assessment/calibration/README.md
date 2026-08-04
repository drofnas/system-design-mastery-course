# Module 14 Evaluator Calibration

The fixtures use Northstar only and differ in evidence quality, not preferred
architecture. Each fixture manifest freezes submission identity and assistance.
Run each fixture twice with deterministic settings, preserve all six raw JSON
responses, then run `scripts/check_calibration.py`.

- `pass.md` contains complete, consistent, adversarially tested evidence.
- `revise.md` preserves safety but lacks cost sensitivity and strategy traceability.
- `repeat.md` breaks chronology, compatibility, write authority, rollback, and ownership hard gates.

Result bands must agree across both runs and category scores may differ by at
most one point. The checker rejects mismatched averages, citations, finding
classes, safety flags, remediation references, or aggregate scores.
