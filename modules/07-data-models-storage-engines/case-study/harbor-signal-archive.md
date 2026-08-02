# Harbor Signal Archive Worked Case

## Problem and isolation

Harbor Signal Archive supports a municipal coastal-operations team. Sensors at
240 stations publish water level, wind, visibility, and equipment-health
observations. Operators query the latest status, scan a station's time range,
search incident notes, export regional analytics, and delete expired raw
samples. Exact coordinates for critical infrastructure are restricted.

Harbor has no commerce state. Its keys, workload, retention rules, index
choices, and decision are examples only. The learner freezes a separate
commerce baseline before using this case.

## Workload and invariants

Normal ingest is 2,000 observations/s, peak is 8,000/s for 20 minutes, and one
storm can send 55% of writes to 12 stations. Values average 240 bytes. The
system retains 30 days of raw observations, one year of hourly rollups, and
seven years of signed incident reports.

| Operation | Share or rate | Required order/access | Target |
|---|---:|---|---|
| append observation | 60% | station and observation time | p99 acknowledgement ≤40 ms |
| exact observation | 10% | exact composite key | p99 ≤30 ms |
| latest station state | 12% | greatest time within station | p99 ≤40 ms |
| station time range | 10% | ordered range | p99 ≤200 ms for 10,000 rows |
| absent-key probe | 3% | exact non-member | p99 ≤25 ms |
| note search | 3% | token to report IDs | p99 ≤300 ms |
| retention delete | background | time cutoff | complete within 24 h |
| regional export | background | column projection and time window | no interactive-SLO breach |

Required invariants include unique `(station_id, observed_at, sequence)`, no
resurrection after an accepted retention deletion, chronological scan order,
restricted coordinates absent from general telemetry indexes, and traceable
transformation from raw observation to rollup.

## Data-model reasoning

The completed Harbor model uses a relational catalog for station identity,
authorization, and retention policy; an ordered key/value representation for
telemetry; an inverted index for incident-note tokens; and columnar derived
files for regional analytics. A graph model was considered for equipment
dependencies but rejected initially because the required traversal is shallow
and changes rarely. A document representation remains valid for schematically
variable sensor payloads if it preserves typed access keys and evolution rules.

The primary telemetry key is:

```text
station_id | observed_at_utc | sequence
```

This layout makes one station's time range contiguous. It does not make a
region-wide time scan contiguous, so Harbor maintains a derived regional
rollup. Duplicating that access path is a conscious write/storage cost, not a
free query optimization.

## B+ tree walkthrough

With 4 KiB pages, 32-byte keys, 240-byte values, and 24 bytes of per-entry
overhead, a leaf fits approximately `floor((4096 - header) / 296)` entries.
The worked example uses much smaller pages so splits are visible. Inserts find
one leaf, place the key in order, split a full leaf, link its successor, and
copy a separator into the parent. An interior split can create a new root.

Point lookup traverses separators. Range lookup traverses once and then follows
linked leaves. A small buffer pool turns repeated hot-station traversals into
cache hits, but a scan larger than the pool can evict useful upper pages. The
lab's simplified delete keeps search correct and records underfull pages; it
does not claim production-grade merge, concurrency, or crash safety.

## LSM walkthrough

Harbor writes enter an ordered memtable. At its configured threshold the lab
writes one immutable sorted table containing length-framed entries, a sparse
index, and a Bloom filter. Reads check the memtable and then tables newest-first.
Ranges merge visible versions in key order. A delete writes a tombstone, which
must mask every older value until compaction proves that discarding both is
safe.

Four similarly sized tables trigger size-tiered compaction in the repaired
configuration. Disabling that work initially lowers foreground write cost, but
run count, negative-lookup probes, tombstone space, and later merge work grow.
Harbor therefore measures useful ingest and compaction capacity separately and
admits writes only within a recoverable region.

## Amplification example

Suppose a trial accepts 10 MiB of keys and values, writes 34 MiB across flushes
and compactions, probes 18 blocks for 6 logical reads, and occupies 16 MiB for
12 MiB of live data:

```text
write amplification = 34 / 10 = 3.4
read amplification  = 18 / 6  = 3.0 probes/read
space amplification = 16 / 12 = 1.33
```

These are engine-level measurements. Device firmware may add more writes, and
the Python/file-system lab cannot observe them.

## Failure matrix and visible reasoning

| Experiment | Broken hypothesis | Repaired evidence sought |
|---|---|---|
| small cache | a tree needs one I/O per level forever | repeated hot reads reuse pages without hiding range-scan pollution |
| compaction backlog | background work can always catch up later | run count and pending bytes stay bounded in steady state |
| Bloom disabled | negative lookups are cheap because files are sorted | no false negatives and fewer table probes with the filter |
| overlapping runs | sorted files make range scans free | compaction reduces merge sources while preserving order/results |
| hot-key skew | average throughput predicts every station | per-key concentration changes cache, split, and stall behavior |
| tombstone debt | deletion immediately frees storage | deleted values never reappear; compaction later reclaims safe bytes |

## Decision and alternatives

Harbor chooses an LSM-style primary telemetry store because sustained ingest
and sequential flushing dominate, while bounded compaction and Bloom filters
keep negative lookups within target. The relational catalog and inverted note
index remain separate access paths. A B+ tree is still defensible if range-read
latency, simpler space reclamation, or operational familiarity outweighs
measured write cost.

The decision includes per-role coordinate authorization, encrypted storage,
redacted telemetry, capacity and compaction owners, disk/run-count alerts, a
dual-read migration, hash/count comparison, fallback, rollback before old-path
decommissioning, and explicit recovery requirements. It does not claim that
clean-close persistence is crash durability. The choice reverses if measured
range/read tails or compaction cost exceed their budgets under the projected
storm workload.
