# Module 17 Guided Exercises

Complete these with Atlas only. Freeze independent commerce decisions before
opening the answer key.

## EX-01: Vector and matrix ledger

Multiply a 2x3 token matrix by a 3x2 projection. Record every shape, multiply,
addition, and byte assumption; identify which dimensions can batch.

## EX-02: Norms and projections

Calculate the L2 norm and cosine similarity for two exhibit vectors. Explain why
similar direction does not prove interchangeable generated output.

## EX-03: Probability, entropy, and gradient

Apply stable softmax to three logits, calculate entropy, then use a centered
finite difference to estimate one derivative. State numerical limitations.

## EX-04: Stable softmax and masking

Show why subtracting the row maximum preserves softmax probabilities. Apply a
causal mask before normalization and explain why masking afterward is wrong.

## EX-05: Token and embedding contract

Define Atlas vocabulary, unknown-token, normalization, model-version, and prompt
policy behavior. Trace four tokens into embedding rows.

## EX-06: Attention by hand

Calculate `QK^T / sqrt(d_k)`, causal masking, row softmax, and weighted values for
three positions. Check shapes and row sums.

## EX-07: Prefill and decode trace

Trace one 96-token prompt and four output tokens. Identify reused state, serial
dependencies, emitted timestamps, and cancellation points.

## EX-08: KV-memory calculation

For given layers, KV heads, head dimension, bytes per value, batch, and sequence
length, calculate KV bytes and sensitivity to each input.

## EX-09: Capacity and cost model

Combine weight, activation, KV, headroom, token throughput, arrival mix, and
useful-output rate. Identify the binding constraint and reversal evidence.

## EX-10: Measurement protocol

Define warm-up, repetitions, open-loop arrivals, timeouts, profiler overhead,
host identity, percentiles, and raw evidence for TTFT and ITL.

## EX-11: Scheduler comparison

Compare FIFO fixed batching with token-budget continuous batching for six short
interactive requests and two long batch requests. Show both throughput and tails.

## EX-12: Admission and memory reservation

Design a pre-admission calculation that rejects a request before model or KV
allocation. Include deadline, queue, tenant, and traffic-class bounds.

## EX-13: Fairness and quota

Specify a scheduling round that prevents batch starvation without allowing batch
prefill to violate interactive objectives. Name the authorization source.

## EX-14: Cache identity

Construct prefix and semantic cache keys. Include tenant, model, tokenizer,
prompt policy, precision, normalized input, threshold, and invalidation event.

## EX-15: Quantization gate

Compare reference and reduced-precision logits on a fixed corpus. Define maximum
error, top-k agreement, task threshold, rollout, stop, and rollback rules.

## EX-16: Provider-loss pair

Design equivalent broken/repaired trials for provider loss. Bound attempts by one
deadline, preserve request identity, verify compatibility, and count useful work.

## EX-17: Failure evidence audit

For F01–F06, list fields that must match, the one control that may differ, raw
records to freeze, target invariant, limitations, and same-work repair evidence.

## EX-18: Architecture defense

Compare a managed provider, one bounded self-hosted deployment, and split
interactive/batch deployments. Defend one with quality, capacity, cost, security,
ownership, migration, rollback, dissent, stop, and reversal conditions.

## PESD 2.0 extension to the final exercise

Extend the final guided exercise with an actual streaming tiny-transformer path with incremental KV state, token scheduling, byte-budget admission, tenant/version cache identity, bounded provider failure, profiling, and an AI System Dossier. Produce an
obligation/control/evidence row, a named owner, a bounded cost or capacity
effect, a failure or policy-drift test, a migration step, and a reversal trigger.
Label every observation with an accepted evidence mode and do not use fixture
replay as independent Build, Break, Implement, or Measure evidence.
