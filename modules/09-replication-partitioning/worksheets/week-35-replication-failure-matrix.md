# Week 35 Replication Failure Matrix

For F01–F06 preserve the frozen prediction, scenario, raw broken trial, isolated
repair, raw repaired trial, and hashes. Record:

| Pair | Availability | Versions/session | Conflict/repair | Movement/load | Invariant | Alternative explanation |
|---|---|---|---|---|---|---|
| F01 | | | | | | |
| F02 | | | | | | |
| F03 | | | | | | |
| F04 | | | | | | |
| F05 | | | | | | |
| F06 | | | | | | |

Recalculate every ratio. Explain failed predictions, evidence boundaries, cost,
security/tenant impact, operating owner, and the next discriminating test.

## A11: Replica-partition controlled postmortem — 45 minutes

Select the frozen F01 replica-partition pair and create
`reports/module-09-replica-partition-postmortem.md`. The matrix compares all
faults; the postmortem explains one controlled incident's user/data impact,
timeline, acknowledgement and version boundaries, first divergence, contributing
conditions, detection/repair gaps, uncertainty, and owned corrective actions.
Do not rewrite raw trials or present a modeled result as production evidence.
