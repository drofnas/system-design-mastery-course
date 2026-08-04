# Atlas Pass Calibration Fixture

## Identity and frozen chronology

The manifest resolves A01–A11 and four learning logs. A01 and all F01–F06
predictions predate execution. Twelve raw trials are immutable; pair hashes,
source commit, evidence kind, Python/toolchain, host, and assistance are recorded.

## Mathematics, model, and capacity

Shape ledgers, hand attention, stable softmax, entropy, and gradient checks agree
with the tested tokenizer and one-block model. The capacity model includes
weights, runtime, activations, KV, 20% justified headroom, prompt/output skew,
queue/deadline limits, provider-loss reserve, and cost per quality-passing 1,000
output tokens. Sensitivity identifies maximum sequence length as the binding input.

## Measurement and serving controls

Repeated CPU runs pin warm-up, workload, runtime, host, timestamps, timeouts, and
profiler overhead. Queue-inclusive TTFT, ITL, prefill/decode, outcomes, memory,
and useful throughput remain separate from deterministic modeled evidence. Token-
budget admission reserves memory before allocation; chunked prefill, interactive
decode priority, a bounded batch share, authenticated tenant quota, and shedding
preserve both safety and liveness under skew.

## Cache, precision, and provider safety

Two pseudonymous tenants prove no cross-tenant prefix or semantic hit. Keys and
invalidation include tenant/authorization, exact model/tokenizer/prompt-policy/
precision, algorithm, threshold, normalized input, and cache kind. The fixed
quality corpus records its hash, worst logit error, top-k agreement, task checks,
shadow/canary stops, and rollback. Provider loss shares one identity and deadline,
verifies compatibility/data boundary/capacity, and records zero duplicate work.

## Failures and architecture leadership

F01–F06 broken targets fail and repaired trials restore I01–I10 with same work,
one changed control, limitations, alternatives, and immutable raw evidence. The
RFC compares no-change, managed, bounded shared, and split deployments using the
same drivers. Named owners, cost sensitivity, shadow/canary migration, drain,
rollback, decommission, dissent, and a quantified reversal condition align with
the defense, evaluation, and separate remediation revision.

## Inference deployment-policy ADR

The distinct A12 ADR selects a bounded inference deployment policy, preserves
the RFC as option exploration, and records quality and data stops, capacity and
unit cost, owners, migration, rollback, decommission, dissent, exception expiry,
and quantified reversal evidence.
