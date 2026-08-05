# Module 2 Anchored Rubric

## Scoring

Use integer scores 0–4. Every score cites the submitted file and heading.

| Score | General meaning |
|---:|---|
| 0 | Missing, unsafe, fabricated, or materially false |
| 1 | Terms or fragments without an operable causal model |
| 2 | Plausible happy path with important evidence gaps |
| 3 | Defensible, scoped decision with adequate evidence |
| 4 | Quantified, adversarially tested, reproducible, and teachable judgment |

## R01: Workload shape and uncertainty

- **0:** No logical-work boundary or unusable units.
- **1:** User totals or average rate without operation identity or time shape.
- **2:** Normal and peak exist, but burst, mix, skew, projection, recovery work,
  or evidence classification is incomplete.
- **3:** Logical versus attempt work, normal/peak/burst/projected demand,
  operation mix, skew, growth, and evidence status are explicit.
- **4:** Sensitivity identifies decision-changing uncertainty and traces it to
  branch demand, recovery, cost, and an owned evidence plan.

Remediation: Lesson 1; EX-01–EX-02.

## R02: Capacity calculations and Little’s Law

- **0:** Calculations use incompatible boundaries or materially false units.
- **1:** Formula names appear without substituted values or model limits.
- **2:** Basic concurrency and capacity exist, but service demand, resource
  minimum, rejection boundary, or exclusions are weak.
- **3:** Little’s Law boundaries align; per-resource demand, nominal capacity,
  predicted bottleneck, failover arithmetic, and limitations are correct.
- **4:** Independent calculations reconcile, sensitivity changes option ranking,
  and measured disagreement is explained without rewriting the prediction.

Remediation: Lesson 2; EX-03.

## R03: Implementation and instrumentation

- **0:** No runnable mechanism or output cannot support the claim.
- **1:** Happy-path code hides queue, concurrency, identities, or timing.
- **2:** Service runs but one material bound, timestamp, outcome, or test is
  missing.
- **3:** Fixed workers, explicit queue, fan-out, downstream limit, retry bounds,
  logical identities, timing, outcomes, and automated tests are observable.
- **4:** Interfaces are reproducible and bounded; tests challenge limits,
  invalid configuration, cancellation/error boundaries, and evidence schemas.

Remediation: Lessons 3–6; EX-04–EX-09.

## R04: Measurement validity

- **0:** Fabricated/altered data, no raw evidence, or a method that cannot offer
  the claimed load.
- **1:** Percentiles without population, count, boundary, or generator evidence.
- **2:** Open-loop or raw data exists, but warm-up, repetitions, rejected work,
  host, timeout, generator lag, or uncertainty is incomplete.
- **3:** Open-loop scheduling, monotonic boundaries, generator lag, counts,
  outcomes, percentiles, raw evidence, configuration, and limitations support
  the claim.
- **4:** Closed-loop bias is demonstrated, repetitions expose variance, and
  competing measurement explanations are falsified.

Remediation: Lesson 3; EX-04–EX-05.

## R05: Tail and fan-out analysis

- **0:** Tail claims contradict the submitted distribution or fan-out behavior.
- **1:** Reports p99 without a branch-to-journey causal model.
- **2:** Fan-out probability or branch demand is calculated, but correlation,
  variable fan-out, or measured comparison is absent.
- **3:** Branch distribution, fan-out, request maximum, downstream demand, and
  observed journey tail are connected with scoped assumptions.
- **4:** Correlation and workload classes are tested; alternatives quantify
  latency, correctness, cost, and duplicate-work trade-offs.

Remediation: Lesson 4; EX-06.

## R06: Overload containment — safety critical

- **0:** Work can grow without a bound, protected work can starve, or overload
  causes an unaddressed invariant failure.
- **1:** Mentions backpressure or shedding without explicit bounds and outcomes.
- **2:** A finite queue or rejection exists, but deadlines, priority,
  authorization, fairness, degraded mode, or recovery is incomplete.
- **3:** Every material wait is bounded; admission is cheap; priority is
  authorized; rejection/degradation and recovery are tested and observable.
- **4:** Combined burst and slowdown tests preserve invariant-protecting work,
  configuration failure is safe, and policy changes are staged and auditable.

Remediation: Lesson 5; EX-07–EX-08.

## R07: Retry and downstream containment — safety critical

- **0:** Retries or fan-out can amplify without a bound or duplicate an unsafe
  effect.
- **1:** Backoff exists without eligibility, identity, attempt, or shared budget.
- **2:** Local attempts are bounded, but fleet budget, downstream limit,
  deadlines, repeat safety, or amplification evidence is incomplete.
- **3:** Retry eligibility, identity, local attempts, shared budget, jitter,
  downstream concurrency, denial, and recovered useful work are explicit.
- **4:** Multi-layer amplification and combined downstream failure are tested;
  cancellation/unknown outcomes remain bounded and owned.

Remediation: Lesson 6; EX-09.

## R08: Failover, operations, ownership, and cost

- **0:** Normal-state capacity is presented as failover-safe or cost has no
  defensible denominator.
- **1:** Adds a generic reserve or infrastructure total.
- **2:** Failover or cost arithmetic exists, but recovery demand, clearance,
  lead time, ownership, or sensitivity is incomplete.
- **3:** Declared loss, retained capacity, concurrent recovery, backlog
  clearance, scaling lead time, cost/useful request, and owners are explicit.
- **4:** Correlated loss and low/base/high sensitivity change a staged operating
  decision with cross-team commitments.

Remediation: Lesson 7; EX-10.

## R09: Causal diagnosis and evidence discipline

- **0:** Conclusions contradict raw evidence or raw observations were replaced.
- **1:** Charts symptoms without a bottleneck hypothesis.
- **2:** Finds the saturation knee but weakly separates observation,
  interpretation, competing causes, or failed predictions.
- **3:** The nine-point sweep and failure matrix connect resource bounds to
  useful throughput, queue, rejection, latency, and prediction error.
- **4:** Repeated falsification rules out generator and alternative bottlenecks;
  limitations and follow-up are prioritized and reproducible.

Remediation: Lessons 2–7; EX-10–EX-11.

## R10: Decision quality, rollout, and teach-back

- **0:** No decision, unsafe rollout, or defense changes assumptions to evade
  critique.
- **1:** Recommends a percentage or tool without driver/evidence chain.
- **2:** Safe region and policy exist, but exclusions, signal lead time, cost,
  owner, rollback, disagreement, or reversal is weak.
- **3:** Report and ADR define a scoped safe region, actionable signal, overload
  policy, failover, cost, owners, staged rollout, rollback, and reversal.
- **4:** Defense teaches the causal model, resolves stakeholder conflict through
  evidence, and records how failed predictions changed the decision.

Remediation: Lesson 8; EX-12.

## Result

- Pass: all structural gates, average ≥ 3.0, no zero in R06 or R07.
- Revise: complete set but insufficient evidence for a defensible decision.
- Repeat: prediction/artifact integrity fails, evidence is fabricated, a safety
  bound fails, or the model is materially false.

## PESD 2.0 cross-cutting anchors

Apply these anchors inside the published module-specific criteria; they do not
create a generic substitute rubric.

- **0–1:** ignores or merely names per-tenant allocation, forecast variance, useful-outcome economics, shared-cost policy, and modeled energy/carbon sensitivity without an enforceable
  causal model, evidence boundary, or owner.
- **2:** covers the happy path but leaves a material tenant, governance,
  recovery, supplier, cost, migration, or evidence gap.
- **3:** connects the requirement to a mechanism, failure evidence, ownership,
  cost, migration, and a scoped residual risk.
- **4:** additionally tests policy drift or isolation failure, quantifies useful
  outcome and uncertainty, preserves lineage, and gives teachable reversal and
  decommissioning triggers.
