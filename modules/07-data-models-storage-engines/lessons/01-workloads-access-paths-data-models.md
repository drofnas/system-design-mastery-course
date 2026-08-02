lesson_id: L01

# Workloads, Access Paths, and Data Models

## Outcomes

- Convert user operations into an access-path matrix with rates, selectivity,
  order, result size, freshness, and growth.
- Separate logical modeling from physical placement and index choice.
- Choose a data model by invariant and access-path fit, including the cost of
  duplicated representations.

## Prerequisites

Module 1 workload/invariant framing and Module 2 capacity estimates. You should
already distinguish normal, peak, burst, and projected load.

## Mechanism and method

A data model states identities, relationships, constraints, and evolution. A
physical design states record layout, partition/order key, index, compression,
and maintenance. Mixing the two too early produces technology-shaped
requirements.

Use this procedure:

1. Name each operation from the user's perspective.
2. Quantify arrival rate, concurrency, key distribution, result cardinality,
   predicate/selectivity, required order, freshness, and retention.
3. Map every invariant to the authoritative state and enforcement point.
4. Propose the minimal access path for each dominant operation.
5. Count write, storage, migration, consistency, and ownership costs for every
   duplicate representation.
6. Compare models only after this matrix exists; record evidence that would
   reverse the choice.

Relational models make constraints and joins explicit. Documents can preserve
aggregate locality and schema variation. Key/value models expose direct key
access. Graph models prioritize relationship traversal. Time-series layouts
organize ordered measurements and retention. Columnar layouts reduce work for
large projections and aggregates. None eliminates physical access paths.

## Worked example

Harbor's latest-state and time-range operations both begin with `station_id`,
then order by time. The primary telemetry key is therefore
`station_id|observed_at|sequence`. A region-wide export does not share that
prefix. Instead of weakening the interactive layout, Harbor builds a derived
regional rollup with freshness and lineage contracts.

Restricted coordinates live in the authorized station catalog rather than the
general telemetry value. This is a security boundary and reduces accidental
index leakage. Incident-note tokens use an inverted index because substring
scans would make work proportional to all reports.

## Common expert mistakes

- **Choosing from nouns:** “telemetry means time-series database” omits actual
  access paths, retention, and operating constraints.
- **Treating denormalization as free:** duplicated data needs consistency,
  rebuild, access-control, and decommission contracts.
- **Optimizing averages:** a small set of hot stations can dominate page and
  compaction behavior.
- **Using one model for every operation:** authoritative write and analytical
  read models can differ if lineage and freshness are explicit.
- **Equating schema flexibility with no schema:** readers still depend on field
  meaning, type, version, and absence semantics.

## Guided practice

For Harbor, fill one access-path row for exact observation, latest state,
station range, absent lookup, note search, and retention delete. For each, name
the candidate model and one physical path. Then answer: which single added
index increases write work most during a storm, and which owner accepts it?

Compare with EX-01 and EX-02 only after freezing the table.

## Self-check

1. Why is “document database” insufficient as a physical design?
2. When is a derived columnar representation safer than changing the primary
   row order?
3. What evidence can disqualify an otherwise natural graph model?

## Explained answers

1. It does not define partition/order keys, indexes, record size, consistency,
   maintenance, or the physical work of an operation.
2. When interactive access and analytical scans require incompatible locality;
   the derived path is safe only with lineage, freshness, rebuild, and access
   controls.
3. Shallow/stable traversals, low relationship update rate, or a simpler
   indexed join meeting the measured target can outweigh graph flexibility.

## Sources and next work

- CMU 15-445/645 Spring 2026 storage-model materials, bounded in RES-03.
- PostgreSQL index documentation, RES-08, for later access-path comparison.
- Continue to Lesson 2 and EX-01–EX-02; freeze the independent matrix before
  reading the Harbor completed decision.
