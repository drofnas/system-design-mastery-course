# Module 4 Resource Guide

Every required source is free. Local lessons contain the required teaching; the
sources provide standards text, maintainer contracts, and production experience.

## RES-01: The USE Method

- Author/publisher: Brendan Gregg
- URL: https://www.brendangregg.com/usemethod.html
- Type/status: practitioner methodology; required
- Boundary: read Summary, Metrics, In Practice, and Other Methodologies
- Time/week: 35 minutes, Week 13
- Access: free
- Purpose: start from resource questions rather than available dashboards
- Evidence: build a utilization/saturation/errors table and name two gaps
- Local alternative: Lesson 1
- Reflection: Which user symptom cannot be diagnosed by USE alone?
- Last verified: 2026-07-31

## RES-02: Monitoring Systems with Advanced Analytics

- Authors/publisher: Jess Frame, Anthony Lenton, Steven Thurgood, Anton
  Tolchanov, Nejc Trdin, and Carmela Quinito; Google SRE Workbook
- URL: https://sre.google/workbook/monitoring/
- Type/status: practitioner handbook chapter; required
- Boundary: read Desirable Features, Sources of Monitoring Data, and Metrics
  with Purpose through Saturation
- Time/week: 45 minutes, Week 13
- Access: free
- Purpose: connect user symptoms, diagnostic signals, and operating cost
- Evidence: classify five proposed signals by user, cause, and capacity purpose
- Local alternative: Lessons 1 and 4
- Reflection: Which signal is useful for diagnosis but unsafe for paging?
- Last verified: 2026-07-31

## RES-03: Trace Context

- Author/publisher: W3C Distributed Tracing Working Group
- URL: https://www.w3.org/TR/trace-context/
- Type/status: W3C Recommendation; required
- Boundary: read Abstract, Trace Context HTTP Headers Format, Processing Model,
  and Privacy Considerations
- Time/week: 40 minutes, Week 14
- Access: free
- Purpose: define interoperable trace identity and safe propagation behavior
- Evidence: validate three `traceparent` examples and document one trust boundary
- Local alternative: Lesson 3
- Reflection: Why must an inbound trace identifier not grant authorization?
- Last verified: 2026-07-31

## RES-04: OpenTelemetry Specification Overview

- Author/publisher: OpenTelemetry maintainers, Cloud Native Computing Foundation
- URL: https://opentelemetry.io/docs/specs/otel/overview/
- Type/status: maintainer specification; required
- Boundary: read Client Architecture, Tracing Signal, Metric Signal, Log Signal,
  Resources, Context Propagation, and Propagators
- Time/week: 45 minutes, Week 14
- Access: free
- Purpose: map the lab's provider-neutral records to common signal semantics
- Evidence: map each lab field to resource, scope, context, span, metric, or log
- Local alternative: Lessons 3 and 4
- Reflection: Which correlation survives aggregation, and which detail does not?
- Last verified: 2026-07-31

## RES-05: Rigorous Benchmarking in Reasonable Time

- Authors/publisher: Tomas Kalibera and Richard E. Jones; ACM ISMM, accepted
  manuscript hosted by the University of Kent
- URL: https://kar.kent.ac.uk/33611/
- Type/status: original research paper; required
- Boundary: read the abstract, experimental-dimension model, repetition guidance,
  and reporting recommendations; skip formal derivations on first pass
- Time/week: 55 minutes, Week 16
- Access: free
- Purpose: treat multiple sources of performance variation explicitly
- Evidence: identify process-, iteration-, and environment-level variation in
  the learner's benchmark
- Local alternative: Lessons 2 and 7
- Reflection: Which repetition level would a single long run miss?
- Last verified: 2026-07-31

## RES-06: The Art of Performance Monitoring

- Author/publisher: Brian Smith, Facebook; USENIX Association
- URL: https://www.usenix.org/conference/srecon16/program/presentation/smith
- Type/status: conference video, audio, and slides; required
- Boundary: watch the complete talk or use all slides plus the local written
  alternative
- Time/week: 35 minutes, Week 14
- Access: free
- Purpose: examine production performance monitoring as a designed system
- Evidence: record one monitoring design rule, its cost, and one counterexample
- Local alternative: Lesson 4 and the Transit case
- Reflection: Which useful production signal should not become a metric label?
- Last verified: 2026-07-31

## Optional enrichment

- Python Software Foundation, `cProfile` and `tracemalloc` documentation:
  https://docs.python.org/3/library/debug.html — inspect exact profiler
  limitations while implementing a non-Python production equivalent.
