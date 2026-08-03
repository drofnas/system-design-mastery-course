# Week 46 Reliability Controls Build

## Build contract

Implement in the learner's chosen stack:

1. valid/good journey event evaluation and coverage handling;
2. SLO budget and multi-window burn calculations;
3. page/ticket routing with immediate action and ownership;
4. priority admission, degraded output, deadlines, queues, and concurrency bounds;
5. incident role/runbook records;
6. backup manifest, isolated restore verification, authority epoch, and reconciliation;
7. schema-valid deterministic output or an equivalent documented interface.

## Test matrix

Test boundary events, missing telemetry, low traffic, fast/slow burn, overlapping
alerts, dependency slowdown, burst, stale cache, regional loss, corrupt backup,
log gap, stale authority, failback, wrong target, and denied approval.

## Observable interface

Record command/API, input schema, output schema, versions, defaults, constraints,
error behavior, hashes, environment, and limitations. Run the Northstar lab once
before reproducing only its observable contract, not its thresholds or design.

## Implementation review

- Journey contract and anti-gaming review
- Arithmetic and deterministic tests
- Resource and work bounds
- Security, secret, audit, and deletion/retention boundaries
- Recovery authority and rollback
- Cost, owner, migration, and decommission plan
- Claims the environment cannot prove

## Week 46 learning log

Preserve failed tests and explain the repair in a new commit or dated addendum.
