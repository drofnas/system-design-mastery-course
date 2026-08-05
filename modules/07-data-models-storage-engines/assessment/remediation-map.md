# Module 7 Remediation Map

Keep the original baseline, scenarios, raw trials, first ADR, defense, and
evaluation immutable. Put corrections in dated addenda and rerun only the
smallest evidence needed.

| Finding area | Lessons | Exercises | New evidence |
|---|---|---|---|
| Workload/model/access paths | Lesson 1 | EX-01–EX-02 | bounded workload/model addendum |
| Pages/cache/locality | Lesson 2 | EX-03–EX-04 | occupancy and warm/cold/pollution rerun |
| B+ tree mechanism | Lesson 3 | EX-05–EX-07 | split/delete/reopen evidence |
| LSM/Bloom/compaction | Lesson 4 | EX-08–EX-09 | version/tombstone/filter/merge rerun |
| Amplification/capacity/cost | Lesson 5 | EX-10 | reconciled counters and sensitivity |
| Query plan/index | Lesson 6 | EX-11–EX-12 | estimate/actual and alternative diagnosis |
| Failure evidence integrity | Lesson 7 | EX-13–EX-14 | new immutable trial and discriminating rerun |
| Storage correctness/safety | Lessons 3–4, 7 | EX-06, EX-08, EX-14 | reference/reopen/non-resurrection evidence |
| ADR/migration/ownership | Lesson 8 | EX-15 | dated ADR and rollback rehearsal |
| Defense/teach-back | Lesson 8 | EX-16 | follow-up defense and dissent record |

Repeat requires a new independent baseline and new raw trials only when the
original ordering or evidence integrity is invalid. Never reconstruct missing
raw data.

## PESD 2.0 remediation

When a cross-cutting floor is missed, return to Lesson 8's PESD 2.0 extension
and the final exercise. Create a separate dated revision containing the missing
requirement/control/evidence mapping, owner, evidence boundary, failure check,
cost consequence, migration, and reversal trigger. Never edit the frozen
baseline or raw trial. A Pass creates no required remediation artifact.
