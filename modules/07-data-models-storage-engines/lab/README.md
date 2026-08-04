# Harbor Persistent Storage Lab

Before setup, run the repository [Home Lab Guide](../../../HOME_LAB_GUIDE.md)
preflight for `M07`.

This standard-library lab executes two educational storage engines:

- a fixed-size page file with B+ tree interior/leaf pages, linked leaves,
  splits, a small LRU buffer pool, clean close, and reopen;
- an LSM directory with an ordered memtable, framed sorted tables, sparse
  indexes, persisted Bloom filters, tombstones, manifest, and size-tiered
  compaction.

Both expose `put`, `get`, ordered `scan`, `delete`, `close`, and `reopen`.

## Run

From this directory:

```bash
python3 -m storage_lab scenarios/base-btree-read.json
python3 -m unittest discover -s tests -v
```

The CLI accepts exactly one strict scenario and emits one strict JSON trial.
Every result includes a full configuration hash and a pair-shared workload
hash, measured Python/file-system evidence, operation latency, deterministic
work counters, amplification, maintenance, correctness, and cleanup.

## Evidence procedure

1. Freeze the scenario and causal prediction before running it.
2. Preserve raw JSON, runtime label, and both hashes.
3. Check reference-map, range-order, reopen, and non-resurrection safety first.
4. Explain deterministic page/table/byte counters before wall-clock latency.
5. Compare pair files only when `shared_input_sha256` agrees.
6. Preserve the broken result; remediation is a separate rerun/addendum.

## Scenario inventory

- Ten bases: B+ tree and LSM under read-, write-, range-, skew-, and
  delete-heavy workloads.
- F01: tiny versus workload-shaped B+ tree cache.
- F02: disabled versus bounded LSM compaction.
- F03: Bloom filters disabled versus enabled for negative lookups.
- F04: overlapping runs versus compacted range-read state.
- F05: hot-key workload under tiny versus measured B+ tree cache.
- F06: LSM tombstone debt versus compaction with non-resurrection checks.

## Measurement boundary

The engines are single-process teaching implementations. B+ tree delete omits
production merge/rebalance and records underfull pages. LSM acknowledgement has
no WAL/fsync crash contract. Clean close and reopen prove only that the emitted
file image can be read back. Python timing cannot prove device media I/O,
kernel cache state, concurrency, crash recovery, cloud cost, or production SLOs.
