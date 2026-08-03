# Incremental Architecture Migration Plan

## Outcomes, invariants, and authority

- Product outcome:
- Authoritative state before, during, and after:
- Invariants and service objectives:
- Compatibility population and window:

## States and transitions

| State | Entry evidence | Allowed writes | Read path | Exit gate | Rollback |
|---|---|---|---|---|---|
| Baseline | | | | | |
| Expand | | | | | |
| Backfill | | | | | |
| Shadow | | | | | |
| Cutover | | | | | |
| Contract | | | | | |
| Decommission | | | | | |

## Compatibility and data movement

Define producer/consumer compatibility, schema expansion, deprecation,
idempotency, checkpointing, reconciliation, divergence handling, and the rule
that prevents unverified dual authority.

## Promotion and stop conditions

Name measurable thresholds for mismatches, errors, latency, freshness, cost,
and operator control. Promotion requires evidence; crossing a stop threshold
halts or rolls back the migration.

## Ownership and communication

Name a primary owner, secondary owner, decision authority, affected consumers,
support path, runbook, and handoff evidence for every phase.

## Decommission proof

List old writers, readers, data, credentials, infrastructure, dashboards,
runbooks, and cost allocations. Do not remove them until their absence is
measured and rollback obligations have expired.
