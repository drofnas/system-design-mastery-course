# Week 47 Incident and Recovery Experiments

Use only an authorized isolated environment. Preserve every scenario, seed,
input, configuration, raw trial, timestamp, hash, and approval.

## Game-day safety charter

- Hypothesis and fault boundary:
- Protected users/data and maximum blast radius:
- Command, operations, communications, liaison, and observers:
- Required access and break-glass expiry:
- Abort, rollback, cleanup, and escalation:
- Start-state verification and exercise authorization:

## Paired-trial method

For F01–F09, run broken and repaired variants with identical workload, fault
events, and seed. Change one named control. Preserve the broken target failure
and require every published invariant to pass in the repaired trial.

| Pair | Shared-input hash | Changed control | Broken first divergence | Repaired proof | Remaining limit |
|---|---|---|---|---|---|
| F01 | | | | | |
| F02 | | | | | |
| F03 | | | | | |
| F04 | | | | | |
| F05 | | | | | |
| F06 | | | | | |
| F07 | | | | | |
| F08 | | | | | |
| F09 | | | | | |

## Controlled incident

Run F01 while workload grows. Measure journey impact, budget burn, detection,
declaration, mitigation, communication, handoff, recovery, and normalization.
Complete the incident-postmortem template from immutable evidence.

## Recovery exercises

Run F05/F06 for corrupt backup and point-in-time loss, F07/F08 for regional
failover/failback, and F09 for operator error. Measure RPO/RTO, versions, epochs,
capacity, shed work, reconciliation, approvals, audit, and rollback.

## Independent reproduction

Reproduce one pair in a second implementation or safe operated system. Explain
which observations match and which production claims remain unsupported.

## Week 47 learning log

Record one disproved prediction, one changed runbook, and one cross-team lesson.
