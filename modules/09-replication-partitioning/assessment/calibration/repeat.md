# Northstar Repeat Fixture

## Missing preserved baseline

Commit `fixture-m09-repeat` points to a Week 33 file edited after the results.
The F01 prediction changed from "both writes converge" to "one write is lost"
after the broken run. Assistance and original hashes are unavailable.

## Contradictory evidence

F01 broken and repaired scenarios use different operations and seeds, yet the
report calls them same-input. The submission claims N=3/R=1/W=1 is linearizable.
F03 raw versions are `[2,1]`, but it reports zero monotonic/read-your-writes
violations. F04 retries an ambiguous write and records two effects as one.

## Failed correctness

The repaired conflict policy silently chooses the last arrival and discards an
annotation sibling. Repair reports completion while intended replicas retain
different versions. Resharding cuts over with two missing keys and one duplicate
authority. Private metadata is copied to an ineligible node during repair.

## Unsupported decision and Gate 3

The ADR calls the whole database "AP," treats replicas as backups, omits
migration/rollback and owners, and claims the toy run proves regional durability
and legal residency. Gate 3 practical raw evidence is absent; the defense changes
the failure model after challenge. These failures require a new frozen baseline
and new trials, not prose remediation.
No controlled replica-partition postmortem is submitted; the learner treats the
unsupported ADR paragraph as both incident analysis and decision evidence.
