# Module 4 Glossary

- **Baseline:** the preserved reference distribution and environment against
  which a candidate is compared.
- **Causal model:** a mechanism-level account connecting a change to resource
  behavior and a user-visible outcome.
- **Cardinality:** the number of distinct attribute combinations that create
  separate metric time series.
- **Continuous profile:** repeated stack sampling used to attribute resource
  consumption over time; the lab uses bounded captures to teach the contract.
- **Controlled experiment:** a comparison that changes one intended factor and
  preserves relevant work, workload, environment, and measurement boundaries.
- **Discriminating test:** an experiment whose possible outcomes separate two
  or more credible hypotheses.
- **Exemplar:** a trace-linked observation attached to an aggregated metric
  point or bucket.
- **Falsifier:** an observation that would materially weaken a hypothesis.
- **Metric series:** one metric name plus one unique set of attribute values.
- **Profile:** an attribution of CPU time, allocations, or another resource to
  code locations or stacks.
- **Regression budget:** the maximum tolerated performance change for a stated
  workload, metric, uncertainty rule, and action.
- **Span:** a timed operation within a trace, with identifiers, parentage,
  status, and bounded attributes.
- **Structured log:** an event with named, typed fields rather than a message
  that must be parsed from prose.
- **Telemetry bundle:** the scenario, metadata, raw signals, profiles, and
  summary needed to reproduce or challenge one trial.
- **Trace context:** identifiers and flags propagated across execution and
  process boundaries so work can be correlated.
- **Useful work:** distinct successful user outcomes, excluding retry or
  instrumentation activity that creates no additional user value.
