# Module 18 Readiness Review

## Result

**Ready on 2026-08-03.** Module 18 satisfies the syllabus, module standard,
manifest, teaching, portable retrieval/agent lab, paired-failure, capstone-
defense, assessment, calibration, resource, navigation, evidence-safety,
focused-validation, and full-course contracts.

## Verified gates

- Identity: M18, Weeks 69–72, 46 scheduled hours.
- Instruction and practice: eight lessons, separate CivicAid case, twenty
  guided exercises with explained answers, and four weekly worksheets.
- Lab: eleven Python tests pass. Retrieval oracles, seeded HNSW, grounding,
  versioning, authorization, approval, idempotency, replay, cancellation, and
  all F01–F08 repairs restore I01–I12 deterministically.
- Assessment: G01–G06, R01–R10, provider-neutral evaluator, structured report,
  remediation map, and three CivicAid calibration fixtures resolve.
- Calibration: six raw records pass deterministic checking; bands are stable,
  criterion drift is zero, and SHA-256 provenance matches.
- Resources: required free authoritative sources resolved on 2026-08-03 with
  bounded assignments and local alternatives.
- Safety: no commerce capstone answer leakage, production RAG or agent
  overclaim, secret, private data, fabricated citation, frozen-artifact
  overwrite, unresolved authorization/replay failure, or syllabus drift.

## Commands passed

```text
python3 -m unittest discover -s tests -v
python3 scripts/check_calibration.py --module M18 <six raw records>
python3 scripts/validate_course.py --module M18
python3 scripts/validate_course.py
git diff --check
```

## Evidence boundary

Module readiness means the package can teach and assess the final module. It
does not mean a learner has passed Module 18, Gate 6, or the capstone defense.
The deterministic CivicAid lab also does not prove production relevance,
provider quality, legal compliance, or organizational adoption.
