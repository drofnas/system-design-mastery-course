# Module 7 Guided Exercises

Complete these with Harbor Signal Archive. Freeze answers before opening the
answer key. Each exercise prepares a distinct piece of independent evidence;
the numbers are not capstone defaults.

## EX-01: Access-path matrix

For exact observation, latest station state, station range, note search,
retention delete, and regional export, record rate, key distribution,
predicate/selectivity, order, result size, freshness, retention, and SLO.

## EX-02: Model and invariant placement

Compare relational, document, key/value, graph, time-series, and columnar
representations. Assign authoritative state and enforcement for uniqueness,
non-resurrection, coordinate restriction, scan order, and rollup lineage.

## EX-03: Page-capacity derivation

Calculate optimistic and 75%-fill leaf capacity for 4 KiB pages, a 32-byte
header, 32-byte key, 8-byte slot, and values of 128, 240, and 900 bytes. List
omitted factors.

## EX-04: Buffer-pool trace

Trace `R,A,B,A,C,D,A` under three LRU frames. Record hit/miss/eviction and
explain why a database miss is not necessarily a device read.

## EX-05: B+ tree split trace

For order four, insert `10,20,30,40,25,5,15`. Draw leaves, links, separators,
and root changes after every split.

## EX-06: Tree invariant review

Write checks for key order, unique page IDs, valid children, separator routing,
equal leaf depth, linked-leaf completeness, and agreement between point/range
results.

## EX-07: Index selection

Choose B+ tree, hash, or inverted index for four Harbor operations. For each,
state one benefit and one write/storage/security cost.

## EX-08: LSM visibility

Resolve point and full-range results for newest-to-oldest runs
`R3={a:T,c:7}`, `R2={a:5,b:6}`, `R1={a:2,c:4}`. State when `a:T` can be
discarded.

## EX-09: Bloom-filter budget

For 100 keys, 1,000 bits, and seven hashes, estimate false-positive
probability. Explain the correctness response to a negative and positive result.

## EX-10: Amplification arithmetic

Given 12 MiB logical writes, 30 MiB engine writes, 24 probes for 12 reads,
18 MiB disk, and 15 MiB live data, compute all ratios and state the evidence
boundary.

## EX-11: Composite-index order

Compare `(station_id, observed_at)` and `(observed_at, station_id)` for exact,
latest, station-range, and region-time operations. Name the leading-prefix
constraint and one derived path.

## EX-12: Query-plan diagnosis

A plan estimates 20 rows but observes 20,000 at the first scan. Produce three
ranked causes and one discriminating check for each before proposing an index.

## EX-13: Workload predictions

Predict the direction of page probes, table probes, bytes written, cache hits,
run count, tombstones, and space for read-, write-, range-, skew-, and
delete-heavy scenarios. State an alternative explanation for each.

## EX-14: Same-input failure design

For the six published pairs, identify the one intended variable and every field
that must remain identical. Define correctness and recovery checks before
running them.

## EX-15: Storage decision table

Compare B+ tree, LSM, current relational storage, and a managed alternative
under shared user, workload, security, cost, operations, recovery, ownership,
migration, and reversal drivers.

## EX-16: Defense and dissent

Conduct a recorded defense. Have five roles challenge the decision: database,
application, security/privacy, finance, and on-call/recovery. Record changed
belief, unresolved dissent, owner, follow-up evidence, and any dated addendum.
