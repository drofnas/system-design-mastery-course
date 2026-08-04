# Module 17 Anchored Rubric

## R01: Mathematical model and numerical reasoning

- **0:** tensor shapes, masking, probability, or numerical reasoning is materially false.
- **1:** formulas or vocabulary appear without derivation, units, or decision use.
- **2:** basic calculations work but shape, stability, error, or sensitivity is weak.
- **3:** operations, shapes, stable probability, gradients, tolerances, and limits align.
- **4:** counterexamples and sensitivity distinguish numerical error from task quality.

## R02: Transformer implementation

- **0:** causal behavior is violated or implementation output cannot be reproduced.
- **1:** framework calls or fragments without an inspectable inference path.
- **2:** tokenizer and attention run but version, tests, prefill/decode, or lifecycle gaps remain.
- **3:** versioned tokens, embeddings, causal attention, generation, tests, and limitations agree.
- **4:** independent hand references and perturbation tests falsify plausible implementation errors.

## R03: Capacity and cost accounting

- **0:** admitted work can exceed known memory or the cost denominator is deceptive.
- **1:** parameter count or tokens/s is presented as a capacity model.
- **2:** main weights/KV/work estimates exist but headroom, skew, sensitivity, or useful cost is weak.
- **3:** weights, runtime, activations, KV, compute, bandwidth, queue, headroom, skew, and useful cost reconcile.
- **4:** repeated evidence validates the binding constraint and changes admission or sourcing.

## R04: Measurement and diagnosis

- **0:** fabricated data or modeled values are presented as hardware measurements.
- **1:** one latency or throughput number lacks timestamps, workload, environment, or outcomes.
- **2:** useful measurements exist but queue time, tails, repetitions, overhead, or causal alternatives are weak.
- **3:** TTFT, ITL, prefill/decode, outcomes, throughput, memory, environment, repetition, and limits align.
- **4:** interleaved same-work experiments falsify alternatives and revise the capacity model.

## R05: Scheduling, admission, and fairness

Safety-critical because late admission or unbounded work can exhaust memory and
turn overload into fleet-wide failure.

- **0:** repaired work can overrun memory/queue/deadline or trusts caller priority.
- **1:** batching labels without token, byte, queue, deadline, tenant, or class bounds.
- **2:** normal load is bounded but skew, rejection, starvation, or authorization evidence is weak.
- **3:** pre-admission reservation, token budgets, chunking, class shares, quotas, shedding, and recovery agree.
- **4:** adversarial length/tenant mixes preserve safety and quantify useful-work trade-offs.

## R06: Cache isolation and invalidation

Safety-critical because an incomplete identity can disclose private drafts or
serve incompatible output.

- **0:** repaired evidence crosses tenant/authorization or serves a stale incompatible entry.
- **1:** caching is asserted without key, scope, version, threshold, or invalidation evidence.
- **2:** exact cache identity works but semantic threshold, policy change, telemetry, or purge gaps remain.
- **3:** tenant, authorization, versions, precision, algorithm, threshold, invalidation, and two-tenant evidence agree.
- **4:** collision, revocation, mixed-version, and false-hit tests preserve the boundary and quantify cost.

## R07: Precision and quality decision

- **0:** a candidate that fails a declared protected quality threshold is deployed.
- **1:** reduced bytes or average benchmark change is the only evidence.
- **2:** numerical and task checks exist but corpus identity, worst case, rollout, or rollback is weak.
- **3:** reference hash, numerical error, top-k/task thresholds, performance, shadow, canary, stop, and rollback align.
- **4:** sensitivity across inputs and devices narrows the safe precision envelope.

## R08: Provider and failure containment

Safety-critical because unbounded failover can exceed deadlines, duplicate cost,
or cross privacy and compatibility boundaries.

- **0:** repaired provider loss amplifies attempts, crosses a boundary, or returns incompatible success.
- **1:** a second provider is named without identity, deadline, data, quality, or cost contracts.
- **2:** fallback works normally but partial response, cancellation, compatibility, or capacity gaps remain.
- **3:** one identity/deadline, bounded attempts, compatibility, data boundary, degradation, capacity, and cost agree.
- **4:** simultaneous overload/outage evidence validates failover and rollback without double-counting useful work.

## R09: Failure-evidence integrity

Safety-critical because changed inputs or rewritten trials can manufacture an
inference conclusion.

- **0:** chronology/evidence is altered or any repaired target remains failed.
- **1:** conclusions lack predictions, hashes, pairs, evidence kind, or limitations.
- **2:** most pairs work but one-control isolation, repetitions, raw identity, or alternatives are weak.
- **3:** F01–F06 predictions, hashes, targets, repairs, invariants, raw trials, and limitations agree.
- **4:** independent repetitions and falsification narrow claims while preserving every frozen artifact.

## R10: Architecture leadership

- **0:** a critical boundary is unowned or migration is unsafe and irreversible.
- **1:** model/vendor preference without shared drivers or obligations.
- **2:** useful RFC with weak operations, security, cost, ownership, migration, dissent, or reversal.
- **3:** decision, alternatives, evidence, owners, cost, migration, rollback, stops, defense, and revision align.
- **4:** another team applies the method and resulting dissent materially improves the decision.

## Thresholds

Pass requires every G01–G06 gate, every A01–A11 artifact, average ≥3.0, and no
zero in R05, R06, R08, or R09. G02–G05 failure or a safety-critical zero yields
Repeat; other material gaps yield Revise.
