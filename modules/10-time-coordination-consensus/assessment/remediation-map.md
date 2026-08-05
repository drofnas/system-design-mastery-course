# Module 10 Remediation Map

Use a new dated artifact. Never edit frozen predictions, raw trials, the first
RFC, defense record, or evaluation.

| Finding | Revisit | Practice | New evidence |
|---|---|---|---|
| Clock bound or causality error | Lessons 1–2 | EX-01–EX-04 | corrected calculation/event graph plus counterexample |
| Safety/liveness or consensus-boundary gap | Lesson 3 | EX-05–EX-06 | revised property table and alternative comparison |
| Paxos/Raft conceptual error | Lesson 4 | EX-07 | acceptor/log trace with violated shortcut |
| Election or persistence failure | Lesson 5 | EX-08 | new restart/election trace with durable-state evidence |
| Log/commit/application failure | Lesson 6 | EX-09–EX-10 | discriminating conflict/commit rerun and proof ledger |
| Client/read/snapshot failure | Lesson 7 | EX-11–EX-12 | duplicate/read-barrier/snapshot interruption rerun |
| Lease/fencing/membership failure | Lesson 8 | EX-13–EX-14 | resource rejection and joint-quorum evidence |
| Weak causal diagnosis | Lessons 5–8 | EX-15 | preserved addendum with first divergence and alternative test |
| Weak RFC/defense/ownership | Lesson 8 | EX-16 | revised RFC section and new defense challenge record |

Repeat work is required when repaired safety fails or evidence integrity is
lost. Revise is sufficient for bounded omissions that can be repaired without
changing immutable evidence.

## PESD 2.0 remediation

When a cross-cutting floor is missed, return to Lesson 8's PESD 2.0 extension
and the final exercise. Create a separate dated revision containing the missing
requirement/control/evidence mapping, owner, evidence boundary, failure check,
cost consequence, migration, and reversal trigger. Never edit the frozen
baseline or raw trial. A Pass creates no required remediation artifact.
