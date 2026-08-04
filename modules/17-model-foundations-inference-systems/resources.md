# Module 17 Resource Guide

Every required resource is free. The local lesson named in each row is the
complete text alternative; the external source supplies primary evidence or a
practitioner comparison. Verification records access, title, publisher, and the
assigned boundary on 2026-08-03, not permanent availability.

| ID | Resource and boundary | Week | Time | Required | Evidence to produce | Local fallback |
|---|---|---:|---:|---|---|---|
| RES-01 | Goodfellow, Bengio, and Courville, *Deep Learning*: Ch. 2 §2.1–2.5, Ch. 3 §3.1–3.4 and 3.13, Ch. 4 §4.1–4.3 | 65 | 90 min | Yes | Re-derive one matrix product, entropy example, and gradient approximation | Lesson 1 |
| RES-02 | Vaswani et al., *Attention Is All You Need*: §3.1–3.5 only | 65 | 60 min | Yes | Annotate shapes and derive the scale and causal mask | Lessons 2–3 |
| RES-03 | Stanford CS336 Spring 2026: lectures 1–5 and 10 materials only | 65–66 | 90 min | Yes | Separate token, operator, memory, hardware, and serving claims | Lessons 2–5 |
| RES-04 | Stanford Online CS336 Lecture 10, *Inference*: watch with captions | 66 | 75 min | Yes | Produce a prefill/decode/batching concept map and two transfer limits | Lessons 3–6 |
| RES-05 | Kwon et al., *Efficient Memory Management for Large Language Model Serving with PagedAttention*: §2–4 and §7 | 66 | 75 min | Yes | Reproduce the KV fragmentation argument and record assumptions | Lessons 4 and 6 |
| RES-06 | vLLM, *Optimization and Tuning*: preemption, chunked prefill, input processing | 67 | 45 min | Yes | Compare current controls with the module's portable scheduler | Lesson 6 |
| RES-07 | PyTorch, *Profiler recipe*: timing, shapes, memory, warm-up, trace export | 67 | 45 min | Yes | Write a measured-profile protocol and overhead limitations | Lesson 5 |
| RES-08 | Xiao et al., *SmoothQuant*: §1–4 and §5.3–5.5 | 67 | 60 min | Yes | Tie a precision change to both memory/performance and quality evidence | Lesson 7 |
| RES-09 | Meta Engineering, *Taming the tail utilization of ads inference at Meta scale* | 68 | 45 min | Yes | Separate measured intervention, outcome, scale, and non-transferable assumptions | Lesson 8 |

## Source records

- **RES-01:** Ian Goodfellow, Yoshua Bengio, and Aaron Courville; MIT Press;
  online book; <https://www.deeplearningbook.org/>; free; verified 2026-08-03.
- **RES-02:** Ashish Vaswani et al.; original paper;
  <https://arxiv.org/abs/1706.03762>; free; verified 2026-08-03.
- **RES-03:** Stanford University; course materials;
  <https://cs336.stanford.edu/>; free; verified 2026-08-03.
- **RES-04:** Stanford Online; captioned video;
  <https://www.youtube.com/watch?v=fcgPYo3OtV0>; free; verified 2026-08-03.
- **RES-05:** Woosuk Kwon et al.; SOSP paper;
  <https://arxiv.org/abs/2309.06180>; free; verified 2026-08-03.
- **RES-06:** vLLM project; maintainer documentation;
  <https://docs.vllm.ai/en/latest/configuration/optimization/>; free; verified 2026-08-03.
- **RES-07:** PyTorch project; maintainer tutorial;
  <https://docs.pytorch.org/tutorials/recipes/recipes/profiler_recipe.html>;
  free; verified 2026-08-03.
- **RES-08:** Guangxuan Xiao et al.; original quantization paper;
  <https://arxiv.org/abs/2211.10438>; free; verified 2026-08-03.
- **RES-09:** Meta Engineering; first-person practitioner case;
  <https://engineering.fb.com/2024/07/10/production-engineering/tail-utilization-ads-inference-meta/>;
  free; verified 2026-08-03.

## Reflection questions

1. Which source claim depends most strongly on model, hardware, or workload shape?
2. Which measurement would be invalid if queue time were excluded from TTFT?
3. Which cache optimization changes a correctness or privacy boundary?
4. What evidence would reverse the selected precision or provider decision?
