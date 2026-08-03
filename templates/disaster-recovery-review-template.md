# Disaster-Recovery Review

## Submission identity and authority

- System, authoritative data, owner, evidence commit:
- Exercise environment and authorization:
- Tool and AI assistance disclosure:

## Business impact and recovery priorities

| Journey/data | Maximum tolerable outage | RPO | RTO | Minimum service | Owner |
|---|---:|---:|---:|---|---|
| | | | | | |

## Failure model and dependencies

Name process, host, zone, region, network, dependency, corruption, credential,
operator, and control-plane faults in and out of scope. Include shared fate.

## Backup and restore contract

Record backup source, frequency, retention, encryption, deletion/retention
interaction, integrity checks, restore isolation, credentials, and last test.

## Recovery sequence and evidence

| Step | Preconditions | Authority/epoch | Action | Verification | Elapsed | Abort/rollback |
|---|---|---|---|---|---:|---|
| | | | | | | |

Calculate observed RPO and RTO from immutable evidence. Explain gaps rather
than rounding them away.

## Failover, degraded capacity, and failback

Define priority traffic, reserve, load shedding, fencing, data catch-up,
reconciliation, staged routing, observation window, and rollback authority.

## Security and operator safety

Cover break-glass approval, least privilege, audit, destructive target checks,
secret/key availability, restored security controls, and post-exercise review.

## Options, cost, ownership, and decision

Compare at least three recovery tiers using the same user, data, staffing,
cost, and failure drivers. State the decision, dissent, migration, stopping
conditions, and reversal evidence.
