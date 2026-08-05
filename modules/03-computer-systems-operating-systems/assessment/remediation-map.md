# Module 3 Remediation Map

Remediation preserves the pre-experiment prediction and every raw native trial.
Corrections belong in a new dated artifact.

| Finding | Revisit | Practice | New evidence |
|---|---|---|---|
| Equivalent-work identity is missing | Lesson 1 | EX-01 | Frozen workload/checksum rerun |
| Locality or branch claim lacks mechanism | Lesson 2 | EX-02 | Counter-backed locality comparison |
| Scheduler/syscall explanation is weak | Lessons 3–4 | EX-03–EX-04 | State trace or batching trial |
| Memory placement claim is unsupported | Lesson 5 | EX-05 | First-touch measurement addendum |
| Race/lock reasoning is unsafe | Lesson 6 | EX-06–EX-08 | Sanitizer/race evidence and lock graph |
| Durability or I/O boundary is false | Lesson 7 | EX-09–EX-10 | Repaired timeline and controlled I/O trial |
| Cross-platform decision overgeneralizes | Lesson 8 | EX-11–EX-12 | Constraint matrix and new defense |

An evaluator may identify a lesson and exercise but may not write the repaired
systems explanation or alter evidence that already failed.

## PESD 2.0 remediation

When a cross-cutting floor is missed, return to Lesson 8's PESD 2.0 extension
and the final exercise. Create a separate dated revision containing the missing
requirement/control/evidence mapping, owner, evidence boundary, failure check,
cost consequence, migration, and reversal trigger. Never edit the frozen
baseline or raw trial. A Pass creates no required remediation artifact.
