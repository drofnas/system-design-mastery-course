# Atlas Museum Exhibit Label Service: Completed Case

Open this only after freezing A01. It is a worked non-optional project case, not a
canonical architecture for the the external commerce example.

## Context and workload

Atlas serves four museums. Curators submit public object metadata and private
draft notes to produce 80–120 word label drafts. Interactive preview targets a
750 ms p95 TTFT and 120 ms p95 ITL; overnight batch work has no interactive
latency objective. Peak demand is 18 interactive and 45 batch arrivals per
second. Prompts range from 64 to 2,048 tokens; outputs are capped at 160 tokens.

## Frozen model

The team records model, tokenizer, prompt-policy, precision, and cache versions.
It estimates weights, activations, KV bytes per token, queue capacity, per-class
concurrency, and cost per accepted quality-passing 1,000 output tokens. Quality
is a fixed 24-item synthetic corpus with top-k agreement and task checks. The
case does not claim that this corpus represents every museum collection.

## Candidate designs

1. One FIFO server with fixed batches is simplest, but long batch prefills delay
   interactive work and memory is allocated after admission.
2. One bounded server with interactive and batch classes, token-budget batches,
   chunked prefill, memory reservations, and versioned tenant caches meets the
   controlled workload with the fewest operational boundaries.
3. Separate interactive and batch deployments improve isolation but double
   rollout, cache, and capacity ownership before Atlas has evidence that the
   shared bounded scheduler is insufficient.

Atlas selects option 2. It reserves memory before queue admission, rejects work
that cannot finish within its deadline, caps batch-token work per scheduling
round, and reports queue time in TTFT. Cache identity includes tenant, model,
tokenizer, prompt-policy, precision, normalized prompt, and cache kind. A model
or policy change invalidates entries rather than relying only on time expiry.

## Failure findings

- F01 proves that admitting from request count alone can overrun KV headroom.
- F02 proves a long prefill can violate interactive TTFT while aggregate token
  throughput looks healthy.
- F03 proves an unbounded queue converts overload into stale, expensive work.
- F04 proves incomplete cache identity can cross tenant and version boundaries.
- F05 proves lower numerical error on average does not guarantee the declared
  top-k and task tolerance for every protected example.
- F06 proves naive provider retries spend the same deadline and cost more than once.

## Decision, owners, and reversal

The serving owner owns admission, scheduler, rollout, and provider failover. The
museum platform owner owns tenant identity and prompt-policy versions. The model
owner owns the quality corpus and precision gate. FinOps owns rate verification,
not the architectural choice. Security reviews cache and telemetry fields.

Migration shadows the bounded scheduler, compares same-request hashes and
quality, canaries one museum, then expands. Rollback disables new admission and
drains old work before routing to the prior version. Split deployments become
preferred if a four-week production sample shows either class cannot meet its
objective without reserving more than 70% of capacity away from the other.

## Acceptable alternatives

A separate batch deployment or managed provider can be defensible when its
measurements, data boundary, capacity, cost, compatibility, and exit plan are
explicit. Copying Atlas thresholds or components into the optional project without
independent workload evidence is not defensible.
