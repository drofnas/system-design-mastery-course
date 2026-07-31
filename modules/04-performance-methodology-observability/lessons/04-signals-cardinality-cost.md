lesson_id: L04

# Metrics, Logs, Cardinality, and Cost

## Outcomes

- Select signals for user health, diagnosis, capacity, and change validation.
- Calculate a metric-series upper bound and telemetry byte estimate.
- Apply redaction, access, retention, and ownership decisions.

## Prerequisites

Lesson 3 and Module 2 latency distributions.

## Mechanism and method

Metrics aggregate repeated measurements. Logs preserve event detail. Traces
preserve a sampled causal path. Profiles attribute resource use to code. Each
signal loses information differently, so correlation is designed rather than
assumed.

For a metric with dimensions `operation`, `outcome`, and `region`, the worst
case series count is the product of distinct values. Add dimensions before
deployment only when their bound, use, owner, and retention are known.

Estimate collection cost as:

```text
records × average encoded bytes + index/series overhead
```

The exact backend cost varies, but unbounded growth is visible before choosing a
vendor. Keep user/request identity in controlled traces or logs, redact payloads
and secrets, and apply least-privilege access and deletion rules.

## Worked example

Transit exposes three operations, four outcomes, and one local region: at most
12 normal series per metric. Adding `request_id` creates up to one series per
request. The lab counts unique series, estimates bytes, and marks the cardinality
budget exceeded without exporting anything.

## Common expert mistakes

- **Log everything:** volume, sensitive data, and investigation noise increase.
- **Put errors only in logs:** aggregate rates and alerting become expensive to
  reconstruct.
- **Use unbounded route or tenant labels:** normal product growth becomes a
  telemetry incident.
- **Ignore instrumentation ownership:** obsolete signals remain forever.

## Guided practice

Complete EX-07 and EX-08. Give each signal a purpose, cardinality bound,
retention, privacy class, and deletion owner.

## Self-check

1. Why can a low event rate still create high metric cardinality?
2. Where should request identity normally live?
3. What is telemetry overhead evidence?

## Explained answers

1. Cardinality depends on unique attribute combinations, not only observation
   frequency.
2. In bounded traces and structured logs, with redaction and access controls;
   not as a normal metric dimension.
3. A controlled comparison of collection disabled/enabled covering user latency,
   process resources, bytes, series, and loss.

## Sources and next work

- OpenTelemetry, [Metrics specification](https://opentelemetry.io/docs/specs/otel/metrics/).
- OpenTelemetry, [Logging specification](https://opentelemetry.io/docs/specs/otel/logs/).
- Google SRE Workbook, [Monitoring](https://sre.google/workbook/monitoring/).
- Next: attribute resources to code in Lesson 5.
