# Module 15 Evaluator Calibration

Fixtures use Northstar only and differ in evidence quality, not preferred
runtime. Run each fixture twice with deterministic settings, preserve all six
raw JSON responses, and run `scripts/check_calibration.py`.

- `pass.md` has four-runtime conformance, safe pairs, and a reversible decision.
- `revise.md` preserves safety but weakens equivalence, cost, and decision traceability.
- `repeat.md` breaks chronology, bounds, race, cancellation, cleanup, and validation gates.

Bands must agree and category scores may drift by at most one. The checker
rejects inconsistent averages, citations, finding classes, safety flags,
remediation references, aggregate scores, or manifest identity.
