# Module 11 Readiness Review

## Result

**Ready on 2026-08-02.** Module 11 satisfies the syllabus, authoring standard,
manifest, teaching, lab, failure, decision, assessment, calibration, resource,
navigation, evidence-safety, focused-validation, and full-course gates.

## Verified gates

- Identity: M11, Weeks 41–44, 43.5 scheduled hours.
- Instruction/practice: eight complete lessons, Northstar tutorial, sixteen
  guided exercises with explained answers, and four independent worksheets.
- Lab: eight tests pass; eighteen F01–F09 scenarios validate; pairs share input,
  differ by one repair control, and rerun deterministically.
- Interfaces: messaging scenario/trial schemas load; SQLite authority/outbox and
  inbox/projection state, log positions, effects, workflows, poison, time,
  reconciliation, hashes, metrics, and I01–I12 validate.
- Assessment: G01–G06, R01–R10, provider-neutral prompt, remediation, report,
  defense, and three calibration fixtures resolve.
- Calibration: six raw records pass deterministic checking; result bands are
  stable; category drift is zero; SHA-256 provenance matches.
- Resources: seven required free sources resolve with bounded assignments and
  local alternatives; the required talk has slides and local written teaching.
- Safety: semantic review confirms no capstone answer leakage, production
  overclaim, secret, learner-artifact overwrite, Gate 4 shift, or Module 12 scope theft.

## Commands passed

```text
python3 -m unittest discover -s modules/11-messaging-streams-workflows/lab/tests -v
python3 scripts/check_calibration.py --module M11 <six raw records>
python3 scripts/validate_course.py --module M11
python3 scripts/validate_course.py
git diff --check
```

## Evidence boundary

Readiness means the package can teach and assess the syllabus module. The local
model is not a production broker or workflow engine and cannot prove physical
durability, real-time availability, production performance, regional survival,
universal exactly-once effects, or security enforcement.
