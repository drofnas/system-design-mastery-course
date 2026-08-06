---
lesson_id: L04
title: "Metrics, Logs, Cardinality, and Cost"
---

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

## Failure-mode bridge to the lab

Metrics, logs, and traces each lose information in different ways. Metrics are
cheap to aggregate but can hide the single request that explains a failure. Logs
can preserve details but explode in volume or leak sensitive values. Traces can
connect causality but become hard to store when every user, query, or payload
becomes a dimension.

The lab asks you to notice when observability itself becomes part of the failure.
A cardinality fault is not merely a bill problem; it can drop the exact signal
you need during the incident. A disabled collection path is not proof that the
system behaved well; it is a measurement gap. When writing a diagnosis, include
the cost and retention limit that made a signal trustworthy enough to use. If a
signal was sampled, capped, or suppressed, say how that affects the claim.

## Second worked example

A team adds `user_id`, `query_text`, and `session_id` to a metric label set so
they can debug one customer's complaint. The first dashboard looks wonderful:
every request is distinguishable. A day later the metrics backend drops series,
cost rises, and aggregates become unreliable. The better design keeps bounded
labels such as route, status class, dependency, and tenant tier, then sends
request-specific detail to logs or traces with retention controls. The question
is not "can we attach the field?" but "which signal can afford this dimension?"

## Decision checklist

For every proposed signal, name its owner, retention period, sensitive fields,
cardinality limit, sampling rule, and expected action. A signal with no action
is documentation, not observability.

## Sources and next work

- OpenTelemetry, Metrics specification (RES-12).
- OpenTelemetry, Logging specification (RES-13).
- Google SRE Workbook, Monitoring (RES-02).
- Next: attribute resources to code in Lesson 5.
