# Module 7 Explained Answer Key

These answers demonstrate reasoning, not one required architecture. Alternatives
are valid when they preserve the same contracts and support claims with evidence.

## EX-01 explanation

Exact lookup needs an equality key and one row; station range needs the same
station prefix plus ordered time and up to 10,000 rows. Note search maps tokens
to postings. Regional export projects many rows and few columns. Retention is a
background cutoff operation whose completion window matters more than one-row
latency. The full matrix prevents one “database type” from hiding incompatible
paths.

## EX-02 explanation

Harbor can use relational authority for stations/permissions, ordered key/value
telemetry, an inverted note index, and derived columnar rollups. A document or
time-series primary is also defensible. The key is that uniqueness and deletion
have an authoritative enforcement point, coordinate authorization applies to
every copy, and derived data has lineage/rebuild semantics.

## EX-03 explanation

Usable bytes are `4096-32=4064`. Per-entry sizes are 168, 280, and 940 bytes,
giving optimistic capacities 24, 14, and 4. At 75% target fill, plan roughly
18, 10, and 3. Headers can grow; variable framing, fragmentation, prefixes,
compression, checksums, and overflow change these estimates.

## EX-04 explanation

`R,A,B` fill the frames with misses; the next `A` hits; `C` evicts the least
recent `R`; `D` evicts `B`; final `A` hits. There are five misses, two hits, and
two evictions after initial fill. OS/device caches may satisfy engine misses.

## EX-05 explanation

A correct trace keeps leaves globally ordered, promotes the first key of a new
right leaf, and creates a new root when the old root cannot accept another
separator. Exact grouping can vary with the published split convention; point
and linked range traversal must still produce `5,10,15,20,25,30,40`.

## EX-06 explanation

Check every page once, track visited IDs, require strictly increasing keys,
verify child count is separator count plus one, compute all leaf depths, compare
each separator with the right child's minimum, traverse the leaf chain without
cycles, and compare that sequence with point lookups for every live key.

## EX-07 explanation

B+ tree fits exact plus ordered station ranges; hash fits equality without
ordered scans; inverted fits note tokens. Each additional structure consumes
write bandwidth, storage/cache, migration time, deletion propagation, and an
authorization surface.

## EX-08 explanation

`a` is absent because the newest version is a tombstone, `b=6`, and `c=7`.
The visible range is `b=6,c=7`. Drop `a:T` only when compaction includes every
older run that may contain `a` or when lower-level metadata proves none can.

## EX-09 explanation

`p≈(1-e^-0.7)^7≈0.0082`, about 0.82%. A negative safely skips the table when
the filter was built correctly. A positive requires a table/index probe and may
be false.

## EX-10 explanation

Write amplification is `30/12=2.5`; read amplification is `24/12=2.0`; space
amplification is `18/15=1.2`. These are lab engine/file counters, not device
firmware writes, production latency, or cloud cost.

## EX-11 explanation

`(station_id, observed_at)` supports station equality then ordered time range
and latest-by-station. `(observed_at, station_id)` supports global time order
but scatters a station's readings. A regional/time columnar rollup can serve
exports without compromising the primary interactive path.

## EX-12 explanation

Plausible causes include stale samples, cross-column correlation, and parameter
or hot-key skew. Checks are refresh/inspect statistics, compare extended versus
independent estimates, and run representative parameter classes. A missing
index is a candidate only after the access path and total costs are explicit.

## EX-13 explanation

Direction depends on configuration: write-heavy LSM may reduce foreground
random writes but grow runs/compaction; range-heavy B+ trees may exploit linked
leaves; skew can improve cache locality while increasing overlapping versions;
deletes initially add tombstones and space. Answers that assert universal
magnitudes without trials are unsupported.

## EX-14 explanation

Seed, logical operation sequence, engine, key/value set, environment label, and
all non-target settings remain identical. The pair fingerprint covers them.
Correctness includes reference-map equality and no resurrection; recovery adds
bounded run/debt/space state after the trigger.

## EX-15 explanation

The decision table must use shared drivers. Harbor's worked choice favors LSM
ingest with bounded compaction, but a B+ tree or managed relational path can win
when range tails, recovery maturity, team skill, or total cost dominates.

## EX-16 explanation

A complete defense cites raw evidence, separates lab and production claims,
handles restricted-data and recovery questions, records dissent without forcing
consensus, assigns follow-up owners/dates, and preserves the original ADR before
any revision.

## PESD 2.0 extension answer

A defensible answer covers analytical projections, versioned data contracts, quality SLOs, lineage, stewardship, rebuild and backfill, deletion propagation, and ownership while preserving B+ tree and LSM mechanisms. It distinguishes the
requirement, enforcement mechanism, evidence, and owner; keeps modeled and
measured results separate; and names the failed condition that would reverse
the decision. Different architectures are acceptable when their invariants,
evidence boundaries, migration, and residual risk are explicit.
