# Module 17 Glossary

- **Admission control:** Decide whether new work may enter before it consumes a
  scarce queue, memory reservation, or compute slot.
- **Arithmetic intensity:** Operations performed per byte transferred across a
  named memory boundary.
- **Attention:** Weighted aggregation of value vectors using query-key scores.
- **Continuous batching:** Add and remove sequences while decoding instead of
  waiting for a fixed batch to finish as a unit.
- **Decode:** Autoregressive production of new tokens after prompt processing.
- **Embedding:** Dense vector selected or produced for a discrete token.
- **Entropy:** Expected information under a probability distribution,
  `-sum(p * log p)` for discrete outcomes.
- **Inter-token latency (ITL):** Time between consecutive emitted output tokens.
- **KV cache:** Stored attention keys and values reused during autoregressive decode.
- **Prefill:** Parallel processing of prompt tokens to establish initial model state.
- **Prefix cache:** Reuse of model state for an identical, fully versioned prompt prefix.
- **Quantization:** Represent values with fewer or different numerical levels.
- **Semantic cache:** Reuse based on a similarity decision rather than exact identity;
  its threshold and scope are part of correctness.
- **Softmax:** Stable normalization of scores into a probability distribution.
- **Time to first token (TTFT):** Admission-to-first-output latency, including
  queueing and prefill under this module's contract.
- **Useful output throughput:** Accepted output tokens that satisfy the declared
  quality and completion contract per unit time; retries and discarded output do not count.
