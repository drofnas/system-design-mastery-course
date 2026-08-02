# Harbor Pass Calibration Submission

## Submission identity

Artifact commit `fixture-m07-pass` and baseline tag
`fixture-m07-pass-baseline` resolve through the immutable manifest. The
submission lists A01–A09 paths, SHA-256 hashes, Python 3.13.2/macOS environment,
scenario schema v1, trial schema v1, evidence kind
`measured-python-filesystem-clean-close`, and synthetic-fixture assistance. No
restricted coordinates, learner data, device evidence, or production claims
are present.

## Frozen workload and access-path model

The baseline predates all results. It quantifies normal 2,000/s and peak
8,000/s ingest, a 55% hot-station concentration, value sizes, growth,
retention, exact/latest/range/search/export operations, result bounds, and SLOs.
It maps unique observation identity, scan order, no resurrection, restricted
coordinates, and rollup lineage to authoritative state. Relational catalog,
ordered telemetry, inverted notes, derived columnar rollups, document, graph,
and managed alternatives are compared with owners and reversal evidence.

## Page and B+ tree build

The page derivation includes header, key, value, slot, fill, fragmentation, and
overflow uncertainty. Cold, warm, and post-scan trials report page requests,
hits, misses, evictions, writes, and the OS/device-cache boundary. The fixed
page file implements recursive leaf/interior/root splits, separator routing,
linked ranges, overwrite, simplified delete with underfull-page reporting, and
clean close/reopen. Tests verify sorted unique keys, child counts, equal depth,
linked-leaf completeness, point/range agreement, 60-key adversarial splits,
delete, overwrite, page alignment, and reopen.

## LSM Bloom and compaction build

The LSM implements ordered memtable flush, length-framed SSTables, sparse fence
offsets, persisted Bloom metadata, newest-first point visibility, sorted range
merge, tombstones, atomic manifest replacement, and size-tiered compaction.
Tests prove no Bloom false negatives, newest overwrite wins, tombstones suppress
older values before and after compaction, and clean reopen matches the live map.
The report explicitly excludes WAL acknowledgement, fsync crash durability,
concurrency, backup, and restore.

## Amplification and query-plan evidence

The frozen denominator includes logical key/value/tombstone bytes. One trial
reports 10,000 logical bytes, 28,000 engine bytes, 100 logical reads, 180 page or
table probes, 15,600 disk bytes, and 12,000 live bytes: write amplification
2.8, read amplification 1.8, and space amplification 1.30. Capacity sensitivity
includes peak ingest, compaction reserve, temporary space, recovery time, and
engine-versus-device write boundaries. Query-plan evidence compares estimated
and actual rows, composite index order, correlated station/region predicates,
statistics, covering/partial costs, and a derived columnar path.

## Workload matrix and six-fault diagnosis

Both engines have immutable read-, write-, range-, skew-, and delete-heavy raw
trials. F01 cache, F02 backlog, F03 Bloom, F04 overlapping runs, F05 hot-cache,
and F06 tombstone pairs each preserve the pre-result prediction, seed, logical
operation sequence, environment, and pair-shared hash. Only the named config
field changes; full config hashes differ. For every pair the report separates
observation from cause, ranks at least two alternatives, checks correctness
first, and records recovery. A discriminating rerun rejected the initial claim
that F05 latency was caused only by tree height: post-scan cache misses changed
while height did not.

## Correctness deletion and evidence safety

All 22 trials validate and report reference-map equality, ordered ranges, clean
reopen, zero resurrections, zero engine validation errors, and closed cleanup.
F06 retains a tombstone while older runs remain and drops it only when all older
versions participate in compaction. Point, range, and reopen all keep the key
absent. Restricted coordinates are excluded from keys, values, scenarios,
trials, logs, indexes, and calibration evidence; roles and deletion propagation
are documented.

## Alternatives ADR migration and cost

The ADR compares B+ tree, LSM, current relational, and managed alternatives
under shared workload, security, cost, operations, recovery, skill, and change
drivers. It selects a bounded-compaction LSM telemetry path, retains relational
authority and derived indexes, and states range-tail, compaction-cost, and
recovery thresholds that reverse the choice. Owners cover application,
database, capacity, security, backup/recovery, and on-call. Migration uses the
old store as single authority, ordered replay, sliced backfill, count/hash and
sample comparison, shadow reads, per-operation cutover, rollback, compatibility
window, and decommission gates. Unit cost and temporary-space sensitivity are
included without inventing cloud prices.

## Teach-back and remediation

The recorded defense derives page, tree, LSM, Bloom, tombstone, amplification,
and query-plan behavior. Database, application, security, finance, and on-call
reviewers challenge the decision. The record preserves one dissent about
compaction operations, assigns a sustained-load follow-up owner/date, and names
a changed belief about scan-driven cache pollution. The baseline, raw trials,
ADR, defense, and evaluation remain immutable; optional score-four work uses
dated addenda linked to Lessons 1–8 and EX-01–EX-16.
