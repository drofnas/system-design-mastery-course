# Worked Case Study: Transit Signal Observability

## Case boundary

Transit Signal's route-impact endpoint receives a rider journey with three
route legs. It fans out to one approved-impact lookup per leg and returns only
after every branch completes. Module 2 established its queue and concurrency
bounds. Module 4 keeps those semantics and adds evidence collection.

This is a method demonstration, not a commerce architecture answer.

## User effect and baseline

The rider target remains p95 below 300 ms and p99 below one second. Useful
throughput counts distinct successful journey lookups. The local baseline uses
30 requests per second for five seconds, eight workers, an eight-entry queue,
three-way fan-out, and 24 downstream slots.

Before a run, Transit Signal freezes this question:

> Why did p95 journey latency rise while offered work and successful request
> count remained stable?

The team refuses to start with "CPU is high" or "the database is slow." Those
are candidate observations, not questions tied to the rider outcome.

## Hypothesis ledger

| ID | Candidate cause | Predicted evidence | Falsifier |
|---|---|---|---|
| H1 | extra CPU work in request processing | wall and process CPU rise; profile concentrates in one stack; dependency spans stay stable | process CPU and profile share do not move |
| H2 | allocation pressure | traced bytes and peak memory rise; allocation sites identify retained or transient objects | allocation snapshots and retained bytes remain equivalent |
| H3 | serialized critical section | lock-wait spans and wait counter rise as concurrency increases | wait remains flat while service time rises elsewhere |
| H4 | slow local dependency | one child span and dependency histogram move; CPU remains near baseline | child timing remains stable |
| H5 | unclosed connections | active-connection gauge and descriptor delta climb after completed requests | both return to baseline after each request |
| H6 | high-cardinality metric label | unique metric series and estimated telemetry bytes grow with requests | series count remains bounded by the declared dimensions |

Each hypothesis predicts a *combination* of signals. One correlated graph cannot
establish the cause.

## Instrumentation design

One request produces a client span, a server span, branch spans, and a SQLite
lookup span. Structured log records carry the active trace and span identifiers.
Metrics use bounded dimensions such as outcome and operation; request identity
is allowed in traces and logs but prohibited as a normal metric attribute.

The lab records:

- journey and branch duration distributions;
- queue, worker, downstream, connection, and lock-wait state;
- process CPU, memory, allocation, and file-I/O observations;
- structured lifecycle events with trace correlation;
- CPU and allocation profile summaries;
- SQLite query plan and dependency timing;
- unique metric series and an explicit telemetry-byte estimate.

The collection plan also records overhead. A profiler that changes the measured
path can explain a result only after its own effect is bounded.

## First controlled comparison

Transit Signal runs an interleaved sequence:

```text
baseline, candidate, candidate, baseline, baseline, candidate
```

Every run preserves scenario, seed, planned arrivals, useful-work definition,
and machine metadata. The raw order remains visible. The review reports the
ratio and dispersion rather than selecting the most convenient run.

For independent diagnosis, a partner runs the lab's `blind-prepare` command and
keeps its reveal mapping outside the learner-visible directory. Opaque bundle
IDs are randomized on every preparation. The learner commits the Week 15 matrix
before the partner runs `blind-reveal`; that reveal record hashes the frozen
matrix. Named lab scenarios remain guided source-work inputs, not blind fixtures.

Suppose the candidate has a higher p95 and the server span widens. The SQLite
child span is unchanged, process CPU rises, and the CPU profile attributes most
new samples to impact normalization. That pattern weakens H3–H5 and supports
H1. It still does not prove that removing normalization is safe.

## Discriminating test

The team introduces an equivalent precomputed normalization result while
preserving response checksum and branches. Prediction: if normalization caused
the regression, process CPU and server-span duration should return toward the
baseline while dependency timing remains stable.

If latency improves but the checksum changes, the test is invalid. It removed
work rather than optimizing equivalent work.

## Query-plan example

The route-impact lookup is tested with and without an index on
`impact(route_id, approved_at)`. The plan is captured beside timing evidence.
"Uses an index" is not enough: the review must name the access path, row-count
assumption, result equivalence, and whether the tested data resembles the
decision workload.

## Telemetry failure example

Adding `request_id` to a latency metric produces one series per request. It
appears convenient for investigation, but it transfers request-level detail
into the most expensive aggregation path. Transit Signal removes that label,
keeps request identity in sampled traces and logs, and links an exemplar from a
latency bucket to a trace.

The change reduces series growth without discarding request-level evidence.

## Completed decision shape

The worked review recommends the candidate only when:

- equivalent-work checks pass;
- the effect exceeds the declared regression/noise budget;
- the predicted causal signals move together;
- a discriminating test weakens credible alternatives;
- telemetry cost and sensitive-data rules remain within policy;
- rollout, rollback, owner, and production validation are named.

Reverse the decision if production traffic changes the hot path, collection
overhead exceeds its budget, the query distribution invalidates the local plan,
or user-journey latency fails to improve.

Other conclusions remain valid when their workload, evidence, and uncertainty
are explicit.
