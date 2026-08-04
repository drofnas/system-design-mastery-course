lesson_id: L07

# Caches, Quantization, and Provider Failure

## Outcomes

- Define safe prefix and semantic cache identities and invalidation.
- Gate precision changes on performance, memory, and protected quality evidence.
- Bound provider failover by identity, compatibility, cost, and one deadline.

## Prerequisites

Use Modules 6 and 13 plus Lessons 1–6.

## Mechanism: optimizations change correctness boundaries

A prefix cache may reuse KV state only when the entire computation prefix is
compatible. A semantic cache is riskier: a similarity rule chooses reuse for
non-identical input. Its model, threshold, corpus, tenant scope, authorization,
and output contract are correctness inputs. Cache identity includes tenant,
model, tokenizer, prompt policy, precision where it changes state, normalized
input, cache algorithm/version, and semantic threshold. Invalidation is triggered
by relevant version or authorization change, not only time.

Quantization changes representation. Measure stored bytes and execution, then
compare against a fixed reference corpus using declared maximum logit error,
top-k agreement, and task checks. Average agreement cannot waive a protected
example. Roll out by shadow, canary, stop threshold, and reversible version.

Provider failover is a remote-call policy. Preserve request identity and one
end-to-end deadline. Verify tokenizer, model behavior, response schema, privacy,
region, and quality compatibility. Prevent overlapping attempts unless their
duplicate work and cost are explicitly budgeted. A fallback that returns a
different contract is degradation, not transparent success.

## Worked example

Atlas initially keys cache entries by normalized prompt and model name. Museum B
receives Museum A's private style result after both use the same prompt; a prompt-
policy update also serves stale wording. The repaired key and invalidation policy
include tenant, authenticated scope, exact versions, precision, cache type, and
threshold. The test uses pseudonymous tenants and records zero cross-tenant hits.

A reduced-precision version saves modeled memory but changes a protected date
token in one case. Its average top-k agreement is high, yet it fails the declared
task gate and never reaches the canary. Provider loss then rejects requests whose
remaining deadline cannot support a compatible fallback instead of launching
unbounded retries.

## Common expert mistakes

- Treating a cache as a performance-only component.
- Using model family names where exact model/tokenizer versions are required.
- Claiming quantization is lossless from average benchmark movement.
- Failing over across data residency or privacy boundaries.
- Counting duplicated provider output as useful throughput.

## Guided practice

Complete EX-14–EX-16. Attempt a two-tenant cache collision, a precision change,
and a provider outage with the same request and deadline.

## Self-check

1. Why does precision sometimes belong in cache identity?
2. What extra contract does semantic caching require?
3. When must a quantized candidate stop before canary?
4. Why is a second provider not automatically resilience?

## Explained answers

1. Cached model state or output can depend on representation and kernel behavior.
2. A versioned similarity method, threshold, evaluation corpus, allowed scope,
   authorization, and consequences of a false hit.
3. When any published quality or safety threshold fails, even if averages improve.
4. It may violate compatibility, data boundary, deadline, cost, or duplicate-work limits.

## Sources and next work

Study RES-05, RES-06, and RES-08. Complete EX-14–EX-16 before running F04–F06.
