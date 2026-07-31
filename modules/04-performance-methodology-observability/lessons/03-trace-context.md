lesson_id: L03

# Trace Context and Causal Request Paths

## Outcomes

- Validate and propagate trace identity across a process boundary.
- Model parent/child work without turning trace data into authorization.
- Correlate logs and exemplars with request paths.

## Prerequisites

Lessons 1–2 and familiarity with client/server boundaries.

## Mechanism and method

A trace identifier groups related work. A span identifier names one operation;
parentage records the causal path. The W3C `traceparent` format carries version,
trace ID, parent ID, and flags. Version `00` identifiers cannot be all zero and
must have exact lengths.

At an inbound boundary:

1. Parse the carrier without trusting it as authority.
2. Continue valid context or start a new root for missing/invalid context.
3. Create a server span and child spans around causal operations.
4. Put trace/span IDs in structured logs.
5. Attach an exemplar selectively to aggregated latency evidence.
6. Avoid payload, credentials, or unrestricted baggage.

Use monotonic clocks for durations and wall-clock timestamps for cross-record
navigation. Record both clock meanings.

## Worked example

The Transit load driver creates a client span and sends `traceparent` in the
JSON carrier. The service validates it, creates a server child, then creates
three branch spans and one SQLite span. A completion log carries the active
server span. A p95 histogram exemplar links one observation back to its trace.

## Common expert mistakes

- **Use trace ID for authorization:** inbound context is caller-controlled.
- **Reuse one span for all work:** dependency and queue time cannot be separated.
- **Put identity in every span attribute:** sensitive data and storage cost grow.
- **Assume every span arrives:** sampling and exporter loss require tolerant
  analysis.

## Guided practice

Complete EX-05 and EX-06. Draw the expected Transit trace tree and classify
every attribute by bounded, high-cardinality, or sensitive.

## Self-check

1. What happens when inbound context is invalid?
2. Why keep trace identity out of normal metrics?
3. What is the difference between correlation and authorization?

## Explained answers

1. Continue the user request with a new local root and record bounded diagnostic
   evidence; do not accept the malformed identity.
2. It creates one series per identity, defeating metric aggregation and cost
   bounds.
3. Correlation joins evidence about work. Authorization decides whether an actor
   may perform an action; trace data cannot grant that permission.

## Sources and next work

- W3C, [Trace Context](https://www.w3.org/TR/trace-context/).
- OpenTelemetry, [Tracing API](https://opentelemetry.io/docs/specs/otel/trace/api/).
- Next: bound aggregated signals in Lesson 4.
