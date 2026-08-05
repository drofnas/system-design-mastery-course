# Module 17 Explained Exercise Answers

These are reasoning checks for Atlas, not capstone answers. Other results are
acceptable when assumptions, arithmetic, evidence, and consequences are explicit.

## EX-01–EX-04

EX-01 should show a 2x2 output and six multiply-add terms per row pair; operations
and bytes depend on the stated counting convention and precision. EX-02 should
normalize before cosine comparison and reject the leap from vector similarity to
task equivalence. EX-03 should subtract the maximum logit, produce probabilities
that sum to one, report entropy units, and bound finite-difference error. EX-04
should apply `-infinity` conceptually to forbidden logits before softmax; removing
probability afterward without renormalization changes the distribution.

## EX-05–EX-07

The token contract must be versioned with normalization and prompt policy. The
attention ledger must show `Q`, `K`, and `V` shapes, scaled scores, a triangular
mask, normalized rows, and value aggregation. Prefill processes the existing
prompt while each decode step depends on the prior token and reuses stored keys
and values. Cancellation must be checked before admission, prefill chunks, and
decode steps.

## EX-08–EX-09

For a conventional cache, bytes scale with `2 * layers * kv_heads * head_dim *
tokens * batch * bytes_per_value`; architecture details can change the formula.
Capacity must reserve weights, runtime overhead, activations, and headroom before
using the remainder for KV. Cost divides total controlled cost by useful,
quality-passing output rather than attempted tokens.

## EX-10–EX-13

The protocol includes queue time in TTFT, records token timestamps, uses repeated
same-work trials, reports warm-up and timeouts, and separates profiler overhead.
A defensible scheduler caps tokens per round, prioritizes interactive decode,
chunks long prefill, and guarantees bounded batch progress. Admission happens
before allocation and checks memory, queue, deadline, quota, and identity.

## EX-14–EX-16

A safe cache key includes tenant and every value that can change authorization or
output semantics. Semantic reuse also records similarity method and threshold;
it is not inferred from text alone. A precision rollout passes the entire declared
corpus and stops on any protected threshold, not average error alone. Provider
failover shares one request identity and end-to-end deadline, checks response
compatibility, prevents overlapping attempts unless explicitly budgeted, and
counts only accepted output.

## EX-17–EX-18

Each pair preserves seed, input, workload, model, environment, and all controls
except one. The broken target must fail and repaired invariants must pass without
rewriting the raw evidence. An architecture defense compares the same drivers,
names owners and costs, separates measured from modeled claims, and gives an
executable migration, rollback, and evidence-based reversal condition.

## PESD 2.0 extension answer

A defensible answer covers an actual streaming tiny-transformer path with incremental KV state, token scheduling, byte-budget admission, tenant/version cache identity, bounded provider failure, profiling, and an AI System Dossier. It distinguishes the
requirement, enforcement mechanism, evidence, and owner; keeps modeled and
measured results separate; and names the failed condition that would reverse
the decision. Different architectures are acceptable when their invariants,
evidence boundaries, migration, and residual risk are explicit.
