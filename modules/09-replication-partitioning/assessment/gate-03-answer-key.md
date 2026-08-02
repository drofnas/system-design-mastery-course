# Gate 3 Assessor Notes and Explained Boundaries

Use only after all four parts are frozen. These notes describe acceptable
reasoning, not one architecture.

## Written examination

1. Credit workload-specific access paths, read/write/space amplification,
   compaction/cache/tail effects, durability boundaries, and how replica count
   multiplies storage and background work.
2. A write-skew history with two snapshot readers and disjoint writes is valid;
   the explanation must show dependencies and whole-transaction abort/retry or
   an enforceable restructuring.
3. Read/write intersects because 6>5; write/write does not because 4 is not >5.
   Membership, version comparison, real-time order, and durable responses remain
   separate protocol obligations.
4. Read-your-writes and monotonic reads fail. A minimum-version token routes,
   waits, or explicitly rejects; telemetry records required/observed versions.
5. Accept alternative partitioners when movement is measured and migration has
   copy, concurrent-change capture, independent verification, staged routing,
   rollback authority, reconciliation, capacity, and hotspot controls.

## Hidden practical

Correct fault names after reveal cannot repair changed predictions or mismatched
work. Pass evidence must keep transaction authority, replica histories, hashes,
and invariant oracles consistent while acknowledging the toy-model boundary.

## Defense and portfolio

Accept designs different from Northstar when per-operation semantics follow
drivers and evidence. Look for cross-module causal reasoning, residency and
tenant controls, cost per useful operation, operational ownership, mixed-version
migration, rollback, dissent, and exact commit/heading traceability.
