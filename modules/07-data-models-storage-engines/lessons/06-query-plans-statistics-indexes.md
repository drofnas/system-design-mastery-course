---
lesson_id: L06
title: "Query Plans, Statistics, and Index Design"
---

# Query Plans, Statistics, and Index Design

## Outcomes

- Trace a query plan from estimates to actual work and results.
- Diagnose selectivity and correlation errors before adding an index.
- Design equality, ordered, composite, partial, and covering access paths from
  operation contracts.

## Prerequisites

Lessons 1–5 and familiarity with SQL. The lesson does not teach SQL syntax.

## Mechanism and method

A planner enumerates legal physical plans, estimates their rows and cost, and
chooses the least estimated cost. A plan is a tree of scans, joins, sorts, and
aggregates. Statistics approximate distribution; estimates can be wrong
because data changed, sampling missed skew, or predicates are correlated.

Use this diagnosis procedure:

1. Preserve query text, parameters, schema/index definitions, statistics age,
   environment, and plan.
2. Compare estimated rows with actual rows at the earliest divergent node.
3. Separate estimate error from execution-cost error and resource saturation.
4. Form at least two causes: stale statistics, correlation, parameter skew,
   missing access path, cache state, or operator cost.
5. Run the smallest discriminating check before changing schema.
6. Evaluate the proposed index against every write, storage, migration,
   privacy, and ownership cost.

Composite B+ tree indexes normally support the ordered left prefix. Equality
on leading columns plus a range on the next can be effective. A covering index
can avoid base-table fetches but duplicates more bytes. Partial indexes reduce
scope only when the operation's predicate implies their condition.

## Worked example

Harbor queries a station and a 20-minute time range. An index ordered
`(station_id, observed_at)` supports direct seek plus ordered iteration. An
index ordered `(observed_at, station_id)` makes the station predicate scattered
inside the time window. A regional export may prefer the latter or a derived
columnar path; one index does not optimize both workloads.

For `station_class='storm' AND region='north'`, independent statistics may
multiply selectivities even though storm stations are concentrated in the
north. Harbor first compares estimated/actual rows and statistics before
declaring the tree itself slow.

## Common expert mistakes

- **Reading only the top plan node:** the first cardinality error is often
  lower in the tree.
- **Adding an index after one slow trace:** cache, parameters, blocking, and
  saturation may be the cause.
- **Ignoring order direction and prefix:** the right columns in the wrong order
  still miss the access path.
- **Treating planner cost as milliseconds:** it is a comparison model unless
  the implementation documents otherwise.
- **Leaking sensitive fields into an index:** indexes duplicate data under
  separate access, backup, and deletion paths.

## Guided practice

Design indexes for Harbor exact observation, latest station state, station
range, and retention cutoff. For each, state the leading columns, required
order, estimated selectivity, and write/space/security cost. Complete EX-11 and
EX-12 using `EXPLAIN` evidence from a local database if available.

## Self-check

1. What does an estimated/actual row ratio of 1,000 at a scan suggest?
2. Why can a covering index make the system slower overall?
3. When do extended statistics help?

## Explained answers

1. A major selectivity/model error at or before that node; investigate data
   distribution, parameters, and statistics before operator tuning.
2. It increases write work, cache pressure, storage, maintenance, and migration
   even if one read avoids base-row fetches.
3. When predicates on multiple columns are correlated or functionally
   dependent and independent estimates are materially wrong.

## Sources and next work

- PostgreSQL Indexes, EXPLAIN, and Planner Statistics, RES-08–RES-10.
- Continue to Lesson 7 and include plan evidence in EX-11–EX-12.
