# Performance Methodology and Observability Resource Guide

Local lessons are sufficient to complete the module. External sources reinforce
the instruction and provide a checkable primary or practitioner reference; they
never replace the local explanation, practice, or answer key.

## Required authoritative spine

The required records are RES-01, RES-02, RES-03, RES-04, RES-05, RES-06.
Every required record is free and has a local written alternative. All other
records below are optional enrichment and do not consume required module time.

| Week | Required resources | Assigned minutes |
|---:|---|---:|
| 18 | RES-03, RES-05, RES-06 | 130 |
| 19 | RES-01, RES-02, RES-04 | 125 |

For each assigned source, preserve the requested evidence, one transfer limit,
and one observation that would falsify the claim. A required source that is
temporarily unavailable is replaced by its local alternative and the same evidence
task; record the substitution.

## Resource records

### RES-01: The USE Method

- **Author/publisher:** Brendan Gregg
- **URL:** https://www.brendangregg.com/usemethod.html
- **Type/status:** practitioner performance methodology; Required
- **Access:** free
- **Lesson/time:** network; 35 minutes assigned
- **Purpose:** Start investigation from resource questions rather than available dashboards.
- **Boundary and evidence:** Read Summary, Metrics, In Practice, and Other Methodologies; build a USE table and name two gaps.
- **Local alternative:** [lessons/01-question-first-investigations.md](lessons/01-question-first-investigations.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-07-31
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-02: Monitoring Systems with Advanced Analytics

- **Author/publisher:** Google SRE Workbook contributors
- **URL:** https://sre.google/workbook/monitoring/
- **Type/status:** practitioner handbook chapter; Required
- **Access:** free
- **Lesson/time:** network; 45 minutes assigned
- **Purpose:** Connect user symptoms, diagnostic signals, and operating cost.
- **Boundary and evidence:** Read Desirable Features, Sources of Monitoring Data, and Metrics with Purpose through Saturation; classify five signals.
- **Local alternative:** [lessons/04-signals-cardinality-cost.md](lessons/04-signals-cardinality-cost.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-07-31
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-03: Trace Context

- **Author/publisher:** W3C Distributed Tracing Working Group
- **URL:** https://www.w3.org/TR/trace-context/
- **Type/status:** W3C Recommendation; Required
- **Access:** free
- **Lesson/time:** the relevant lesson; 40 minutes assigned
- **Purpose:** Define interoperable trace identity, parsing, and privacy behavior.
- **Boundary and evidence:** Read Abstract, header format, processing model, and privacy considerations; validate three contexts and identify one trust boundary.
- **Local alternative:** [lessons/03-trace-context.md](lessons/03-trace-context.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-07-31
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-04: OpenTelemetry Specification Overview

- **Author/publisher:** OpenTelemetry maintainers and CNCF
- **URL:** https://opentelemetry.io/docs/specs/otel/overview/
- **Type/status:** maintainer specification; Required
- **Access:** free
- **Lesson/time:** network; 45 minutes assigned
- **Purpose:** Map provider-neutral lab records to trace, metric, log, resource, and context semantics.
- **Boundary and evidence:** Read the named signal, resource, context, and propagator sections; map every lab record field.
- **Local alternative:** [lessons/03-trace-context.md](lessons/03-trace-context.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-07-31
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-05: Rigorous Benchmarking in Reasonable Time

- **Author/publisher:** Tomas Kalibera and Richard E. Jones; ACM ISMM and University of Kent
- **URL:** https://kar.kent.ac.uk/33611/
- **Type/status:** original research paper; Required
- **Access:** free
- **Lesson/time:** the relevant lesson; 55 minutes assigned
- **Purpose:** Model multiple sources of benchmark variation and efficient repetition.
- **Boundary and evidence:** Read the abstract, experimental dimensions, repetition guidance, and reporting recommendations; identify three variation levels.
- **Local alternative:** [lessons/07-benchmarks-regression-budgets.md](lessons/07-benchmarks-regression-budgets.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-07-31
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-06: The Art of Performance Monitoring

- **Author/publisher:** Brian Smith, Facebook; USENIX Association
- **URL:** https://www.usenix.org/conference/srecon16/program/presentation/smith
- **Type/status:** conference video, audio, and slides; Required
- **Access:** free
- **Lesson/time:** the relevant lesson; 35 minutes assigned
- **Purpose:** Examine production performance monitoring as a designed and owned system.
- **Boundary and evidence:** Watch the complete talk or use all slides with the local alternative; record one design rule, its cost, and a counterexample.
- **Local alternative:** [lessons/04-signals-cardinality-cost.md](lessons/04-signals-cardinality-cost.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-07-31
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-07: The Python Profilers

- **Author/publisher:** Python Software Foundation
- **URL:** https://docs.python.org/3/library/profile.html
- **Type/status:** official documentation; Optional enrichment
- **Access:** free
- **Lesson/time:** the relevant lesson; 30 minutes optional
- **Purpose:** Distinguish deterministic call profiling, cumulative time, and instrumentation overhead in the portable lab.
- **Boundary and evidence:** Read the introduction, instant user manual, and limitations; record what deterministic profiling measures and how its overhead changes the evidence limit.
- **Local alternative:** [lessons/05-profiling.md](lessons/05-profiling.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-04
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-08: tracemalloc — Trace memory allocations

- **Author/publisher:** Python Software Foundation
- **URL:** https://docs.python.org/3/library/tracemalloc.html
- **Type/status:** official documentation; Optional enrichment
- **Access:** free
- **Lesson/time:** the relevant lesson; 25 minutes optional
- **Purpose:** Interpret allocation snapshots and retained differences without equating total allocation with a leak.
- **Boundary and evidence:** Read tracing allocations, snapshots, and comparing snapshots; state what the tool can attribute and what it cannot establish about object liveness.
- **Local alternative:** [lessons/05-profiling.md](lessons/05-profiling.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-04
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-09: EXPLAIN QUERY PLAN

- **Author/publisher:** SQLite project
- **URL:** https://www.sqlite.org/eqp.html
- **Type/status:** official documentation; Optional enrichment
- **Access:** free
- **Lesson/time:** the relevant lesson; 25 minutes optional
- **Purpose:** Interpret scan, search, index, join-order, and temporary-structure evidence in the dependency lab.
- **Boundary and evidence:** Read the warning and Sections 1.1–1.3; identify the chosen access path and explain why output formatting is not a stable application API.
- **Local alternative:** [lessons/06-dependencies-query-plans.md](lessons/06-dependencies-query-plans.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-04
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

Do not copy articles, chapters, slides, or transcripts into learner artifacts.
Use short attributed quotations only when necessary and otherwise paraphrase with
the source ID, exact section boundary, and stated evidence limit.
