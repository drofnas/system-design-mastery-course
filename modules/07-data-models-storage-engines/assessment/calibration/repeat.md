# Harbor Repeat Calibration Submission

## Submission identity

Artifact commit `fixture-m07-repeat` has no baseline tag, immutable submission
manifest, raw trial hashes, runtime, schema version, evidence-kind boundary, or
assistance disclosure. A screenshot is the only performance evidence.

## Overwritten baseline and inconsistent evidence

The workload “baseline” was rewritten after results to say LSM was always the
choice. It lists average throughput only and no operations, distributions,
invariants, access paths, retention, security boundary, or alternatives. It
claims 10,000 logical bytes and 20,000 physical bytes produce write
amplification 1.5; 40 reads plus 30 scans are reported as 50 total reads.

## Broken B+ tree and missing LSM build

The tree is an in-memory binary search tree serialized as one JSON object. It
has no fixed pages, interior/leaf distinction, linked range, cache, split
validation, delete test, or reopen comparison. A 20-key range returns 17 keys
out of order. No LSM implementation, Bloom filter, tombstone, compaction,
manifest, or clean-reopen evidence is submitted.

## Missing workload and fault evidence

There are no immutable read-, write-, range-, skew-, or delete-heavy raw
trials and no F01–F06 pairs. Seeds, logical operation sequences, pair hashes,
config hashes, counters, environment labels, alternatives, recovery evidence,
and uncertainty are absent. The screenshot's p99 has no underlying samples.

## Resurrection restricted-data leak and false durability

After deleting `H12|09:00`, reopen returns the old value from a stale file. A
Bloom-like cache returns negative for one present key. Restricted station
coordinates appear in keys and logs available to the general operator role.
The report calls a successful `close()` “crash-proof exactly-once durability,”
but provides no WAL, sync, crash, backup, or restore evidence. The file handle
remains open after the test.

## Technology preference without decision

The decision says “NoSQL scales, so use LSM” without workload evidence,
alternatives, query plans, cost, security, recovery requirements, owners,
migration authority, validation, rollback, compatibility, decommissioning,
dissent, or reversal conditions.

## Missing defense and remediation

No teach-back, cross-functional challenge, evaluation report, learning logs, or
separate remediation exists. The learner replaced the original code and report
with the claimed repair, so the failed evidence cannot be reconstructed.
