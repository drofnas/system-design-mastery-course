# Harbor Revise Calibration Submission

## Submission identity

Artifact commit `fixture-m07-revise` and baseline tag
`fixture-m07-revise-baseline` resolve. A01–A09 paths, hashes, Python/OS label,
schema versions, clean-close evidence kind, and assistance disclosure exist.

## Frozen workload and access-path model

The baseline predates results and lists all Harbor operations and invariants.
Rates and order are present, but burst duration, hot-station concentration,
result sizes, derived-copy ownership, and model reversal evidence are vague.

## Page and B+ tree build

Point, range, insert, split, delete, and reopen tests pass. The report gives page
size and cache hits/misses but omits fill sensitivity, post-scan pollution,
interior split stress, and a precise explanation of simplified delete limits.
No key loss or false durability claim is reported.

## LSM Bloom and compaction build

Memtable, SSTable, Bloom, newest-value, tombstone, range merge, compaction, and
reopen exist and pass reference checks. Sparse-index evidence, manifest
publication reasoning, false-positive measurement, and compaction-policy
sensitivity are incomplete. The report correctly excludes WAL crash durability.

## Amplification and query-plan evidence

Ratios reconcile: 10,000 logical bytes, 24,000 engine bytes, 100 reads, 220
probes, 18,000 disk bytes, and 12,000 live bytes yield 2.4, 2.2, and 1.5.
However, temporary space, recovery after peak, device boundary, unit-cost
sensitivity, actual-versus-estimated query rows, correlation, and alternative
index cost receive only brief treatment.

## Workload matrix and six-fault diagnosis

Ten base trials and F01–F06 pairs exist, validate, retain predictions, and use
matching pair hashes with one named setting changed. The report mostly restates
counter direction. Alternate causes, recovery windows, cold/warm distinction,
and discriminating reruns are missing for four pairs. Raw evidence is preserved
and arithmetic is consistent.

## Correctness deletion and evidence safety

All submitted trials report reference and reopen match, sorted ranges, zero
resurrection, no Bloom false negatives, no validation errors, and clean close.
Restricted coordinates are absent. Boundary tests for empty pages, wide values,
multiple overwrite/delete cycles, and corrupted input are missing, but no
safety failure appears in submitted evidence.

## Alternatives ADR migration and cost

The ADR compares B+ tree, LSM, relational, and managed options and chooses LSM.
It names security, operations, owners, ordered replay, backfill, validation,
cutover, and rollback. Quantified recovery requirements, compatibility window,
decommission criteria, exception ownership, unit-cost sensitivity, and
measurable reversal thresholds need revision.

## Teach-back and remediation

The defense explains core mechanisms and includes database and application
questions. Security, finance, and recovery challenges, dissent, changed belief,
another-team application, and a dated remediation addendum are missing. The
original artifacts remain immutable.
