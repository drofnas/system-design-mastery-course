# Module 8 Readiness Review

> **PESD 2.0 status: Review.** This pre-migration readiness record is historical, not a current Ready decision. Fresh evaluator repetitions, platform/offline/cleanup matrices, and timed learner pilots remain pending.

## Historical result (superseded)

**Ready on 2026-08-02.** Module 8 satisfies the syllabus, authoring standard,
manifest, teaching, lab, failure, decision, assessment, calibration, resource,
navigation, evidence-safety, focused-validation, and full-course gates.

## Verified gates

- Module identity: M08, Weeks 29–32, 43.5 scheduled hours.
- Instruction/practice: eight complete lessons, Northstar tutorial, sixteen
  guided exercises with explained answers, four independent worksheets.
- Lab: nine tests pass; fourteen strict F01–F07 scenarios validate; every pair
  has identical shared input and a distinct repair control.
- Interfaces: transaction scenario/trial schemas load; CLI run/restore paths,
  hashes, LSN/ack arithmetic, checksums, and recovery fields validate.
- Assessment: G01–G06, R01–R10, provider-neutral prompt, shared schema,
  remediation map, report template, and Pass/Revise/Repeat fixtures resolve.
- Calibration: six raw records pass deterministic checking; bands are stable;
  category drift is at most one; provenance hashes match.
- Resources: eight required free authoritative/practitioner records were opened
  successfully on 2026-08-02 and have bounded assignments/local alternatives.
- Safety: semantic review confirms no answer leakage, fabricated production
  claims, secrets, learner-artifact overwrite, or syllabus weakening.

## Commands passed

```text
python3 -m unittest discover -s tests -v
python3 scripts/check_calibration.py --module M08 <six raw records>
python3 scripts/validate_course.py --module M08
python3 scripts/validate_course.py
git diff --check
```

## Evidence boundary

Readiness means this is a complete teaching and assessment package. It does not
promote the toy engine into a production database or turn local timings into a
production recovery promise. Learners must verify chosen database, hardware,
security, workload, and operating assumptions.
