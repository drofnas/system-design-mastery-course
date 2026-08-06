---
lesson_id: L06
title: "I/O, Dependency Timing, and Query Plans"
---

# I/O, Dependency Timing, and Query Plans

## Outcomes

- Decompose queue, service, dependency, and local I/O time.
- Capture a query plan beside result-equivalence and timing evidence.
- Design a discriminating test for CPU, lock, and dependency alternatives.

## Prerequisites

Lesson 5 and basic SQL/index knowledge.

## Mechanism and method

End-to-end latency is a path, not a single timer:

```text
arrival lag + queue wait + service CPU/wait + dependency work + response
```

Child spans expose timing boundaries, but their names and clocks must be stable.
Local file I/O can complete into a cache rather than durable storage; this
module claims timing only, not durability.

A query plan is a prediction from schema, indexes, statistics, parameters, and
data distribution. Capture it with:

- query text or stable operation identity;
- schema and index definition;
- representative row counts/selectivity;
- parameters or parameter class;
- result checksum;
- cold/warm boundary and repeated timing.

Change one factor, then check whether the predicted access path and user effect
move together.

## Worked example

Transit uses SQLite for approved route impacts. `EXPLAIN QUERY PLAN` reports a
scan without the composite index and an index search with it. The lab preserves
the returned impact IDs and records the child span. If the plan changes but
journey latency does not, the index is not yet a user-visible optimization under
that workload.

## Common expert mistakes

- **Call every wait I/O:** locks, queues, timers, and scheduler delay also wait.
- **Treat an index name as proof:** selectivity and result equivalence remain
  unknown.
- **Compare cold baseline to warm candidate:** cache boundary explains the
  result.
- **Infer durability from file-write latency:** completion boundary is different.

## Guided practice

Complete EX-11 and EX-12. Write one rerun that distinguishes a wider SQLite
span from extra CPU performed around the call.

## Self-check

1. What evidence connects a query plan to a journey regression?
2. Why preserve a result checksum?
3. Can a child span prove the dependency is the root cause?

## Explained answers

1. A representative plan, repeated dependency timing, stable surrounding spans,
   result equivalence, and movement in the user metric.
2. To prove the faster variant returned the same required information.
3. No. It locates elapsed time; a discriminating change must test why the
   dependency widened and whether fixing it changes the journey.

## Failure-mode bridge to the lab

Dependency and query-plan evidence often looks deceptively authoritative. A slow
child span can mean the dependency is slow, the caller is sending a worse query,
the pool is exhausted, or the trace starts after queueing has already happened.
A query plan can show a scan, but the decision still depends on rows examined,
rows returned, index selectivity, cache state, and whether the query changed.

In the lab, treat every dependency diagnosis as a contract question. What did
the caller ask for? How many attempts happened? Was connection reuse preserved?
Did the same logical work run in baseline and candidate? For database-like
evidence, state the access path and the cardinality assumption before proposing
an index. The repair should target the causal mechanism, not merely the most
visible slow box in the trace.

## Second worked example

A query changes from indexed lookup to full scan after a filter is added. Before
adding a new index, check whether the filter is selective, whether the planner
has current statistics, and whether the result ordering also changed. If the
query returns 40 rows after examining 4 million, an index may help. If it returns
3.8 million rows, the scan may be the honest cost of the requested work. The
decision should name the access path, write amplification, storage cost, and the
rollback plan if the index fails to improve the target journey.

## Decision checklist

Name caller request shape, dependency contract, attempts, timeout, pool state,
query access path, rows examined, rows returned, and write cost. A fix should
target the first causal break in that chain.

## Sources and next work

- SQLite, EXPLAIN QUERY PLAN (RES-09).
- Python Software Foundation, sqlite3 (RES-15).
- Next: turn comparisons into a release gate in Lesson 7.
