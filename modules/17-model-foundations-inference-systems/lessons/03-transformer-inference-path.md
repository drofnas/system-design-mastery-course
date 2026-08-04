lesson_id: L03

# Transformer Inference from Prefill to Decode

## Outcomes

- Trace a decoder block and autoregressive generation loop.
- Separate prefill work from decode work and KV reuse.
- Locate cancellation, sampling, version, and output boundaries.

## Prerequisites

Complete Lessons 1–2 and understand bounded remote calls from Module 6.

## Mechanism: one parallel phase followed by a serial dependency chain

A decoder block combines normalized hidden state, masked self-attention,
residual connections, and a feed-forward network. A final projection produces
vocabulary logits. Training and inference use the same parameters but different
workflows: inference fixes weights and repeatedly chooses the next token.

**Prefill** processes prompt tokens, produces the first logits, and creates key
and value state. It usually exposes more parallel work. **Decode** adds one token
at a time; each new token depends on the prior result and reads stored weights
and KV state. A KV cache trades memory for avoided recomputation.

Trace procedure:

1. Validate request identity, tenant, versions, token limits, and deadline.
2. Reserve worst-case bounded resources before admission.
3. Tokenize and prefill, recording queue and compute time separately.
4. Emit the first token and define TTFT from request acceptance, including queue.
5. For each decode step, check cancellation/deadline, extend KV state, select and
   emit a token, and record its timestamp.
6. End with a terminal status, model identity, cache identity, counts, and cost.

Greedy selection makes the lab deterministic. Sampling requires a recorded seed,
algorithm, temperature, truncation policy, and runtime because nominally equal
settings can still diverge across implementations.

## Worked example

Atlas accepts a 96-token prompt capped at four output tokens. Queue time is 90 ms,
prefill is 210 ms, and the first decode step is 45 ms, so TTFT is 345 ms under
the module definition. Later tokens arrive after 42, 46, and 44 ms; report the
three ITL observations, not `total/4`. Cancelling after token two prevents later
decode and releases the reservation; it does not retroactively erase emitted text.

## Common expert mistakes

- Reporting model execution time as TTFT while excluding queue and tokenization.
- Counting prompt processing and decode as one uniform tokens-per-second number.
- Treating KV reuse as free despite memory, fragmentation, identity, and eviction.
- Retrying generation without shared request identity or a remaining deadline.
- Claiming deterministic output without pinning algorithm, seed, and runtime.

## Guided practice

Complete EX-07. Trace the lab server's `accepted`, `token`, and terminal events.
Mark what must happen if the deadline expires before admission, during prefill,
and after two tokens.

## Self-check

1. Why can prefill and decode have different bottlenecks?
2. What exactly does a KV cache avoid?
3. When does an accepted request become billable useful work?
4. Why must every stream terminate explicitly?

## Explained answers

1. Prefill exposes matrix work across prompt tokens; decode is sequential and
   repeatedly moves weights and growing KV state.
2. It avoids recomputing prior-token keys and values, not current-token work or
   all attention reads.
3. The course counts only output that satisfies the declared completion and
   quality contract; the commercial policy may differ and must be stated.
4. Clients and operators need to distinguish success, rejection, cancellation,
   deadline, and provider failure rather than infer completion from a closed socket.

## Sources and next work

Study RES-02 and RES-04. Complete EX-07, then calculate the resource envelope in
Lesson 4 before choosing concurrency.
