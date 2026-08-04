# Module 4 Anchored Rubric

Score every criterion from 0 to 4 using only submitted evidence. A score of 3 is
the expected passing quality; 4 requires unusually precise, adversarially tested,
teachable judgment.

## R01: Performance question and baseline

- **0:** no bounded question or preserved baseline.
- **1:** generic slowness claim or unscoped dashboard snapshot.
- **2:** journey and baseline exist but workload, useful work, or exclusions are
  incomplete.
- **3:** frozen user metric, workload, comparison, environment, useful-work
  checks, and uncertainty boundary support investigation.
- **4:** sensitivity and smallest meaningful effect are justified, with transfer
  limits that teach another team how to reuse the contract.

## R02: Hypotheses and controlled experiment

- **0:** a cause is asserted before evidence or work differs materially.
- **1:** one favored hypothesis with no falsifier.
- **2:** alternatives exist but predictions, variation levels, or controls are
  weak.
- **3:** competing mechanisms predict distinct evidence and falsifiers; order,
  repetitions, work, and environment are controlled or visible.
- **4:** discriminating experiments efficiently separate alternatives and expose
  remaining uncertainty across process/environment levels.

## R03: Trace context and correlation

- **0:** context is absent, fabricated, or used as authorization.
- **1:** identifiers appear without valid parentage or boundary handling.
- **2:** traces exist but invalid/missing context, log correlation, or exemplars
  are incomplete.
- **3:** valid context propagates across the process boundary; invalid context is
  safe; spans, logs, and exemplars correlate with bounded attributes.
- **4:** loss, sampling, clock, and trust limitations are tested and explained.

## R04: Metrics, logs, cardinality, and cost

- **0:** unbounded or sensitive labels create unsafe collection.
- **1:** signals are emitted without purpose, units, or dimensions.
- **2:** core signals exist but cardinality, overhead, retention, or ownership is
  incomplete.
- **3:** user, cause, and resource signals have units, bounds, cost/overhead
  evidence, redaction, retention, and owners.
- **4:** the learner proves a lower-cost correlation design without losing the
  decision evidence.

## R05: Profiles, dependencies, and query plans

- **0:** profile or plan claims contradict the evidence.
- **1:** screenshots or top lines are reported without collection boundaries.
- **2:** CPU/allocation/dependency evidence exists but attribution, equivalent
  results, or limitations are weak.
- **3:** profiles distinguish CPU, allocation, retention, and wait; dependency
  spans and query plans preserve result and data-shape boundaries.
- **4:** profile overhead and credible alternative access/resource explanations
  are experimentally separated.

## R06: Blind diagnosis and discriminating tests

Safety-critical because reading or changing the fault before freezing diagnosis
invalidates the evidence of diagnostic judgment.

- **0:** faults are inspected first, diagnoses lack raw evidence, or a materially
  false causal model drives the decision.
- **1:** symptoms are renamed as causes with no alternatives.
- **2:** most faults are located, but cause, confidence, or discriminating reruns
  are incomplete.
- **3:** all six diagnoses predate reveal, cite exact signals, separate observation
  from cause, and propose tests that distinguish credible alternatives.
- **4:** efficient reruns falsify strong alternatives and the learner teaches why
  initially plausible diagnoses failed.

## R07: Evidence integrity and telemetry safety

Safety-critical because altered evidence, leaked data, or unbounded collection
can invalidate decisions and harm users.

- **0:** raw data is missing/modified, secrets or sensitive payloads are exposed,
  bounds fail, or arithmetic contradicts detailed evidence.
- **1:** files exist without hashes, metadata, schema validation, or cleanup.
- **2:** preservation and safety are plausible but one material gap remains.
- **3:** raw evidence is immutable and hashed; schemas, redaction, cardinality,
  resource bounds, cleanup, and summary arithmetic agree.
- **4:** adversarial corruption/loss checks and independent reproduction confirm
  the evidence chain.

## R08: Benchmark and regression budget

- **0:** one convenient timing or changed work supports release.
- **1:** repeated values exist with no environment or action rule.
- **2:** interleaving and threshold exist but uncertainty or inconclusive handling
  is weak.
- **3:** raw interleaved repetitions, effect ratio, dispersion/uncertainty,
  meaningful threshold, and block/rerun/rollback action are reproducible; A11
  records the resulting policy decision without treating the report as an ADR.
- **4:** the budget is integrated into a stable release gate and validated against
  pass, regression, and inconclusive fixtures.

## R09: Decision, operations, and change ownership

- **0:** the recommendation ignores the user outcome or creates unsafe rollout.
- **1:** a patch preference lists no owners or reversal.
- **2:** trade-offs exist but cost, security, migration, failover, or rollback is
  incomplete.
- **3:** the decision follows causal evidence and covers telemetry cost/privacy,
  capacity, rollout, rollback, migration, owners, and reversal conditions.
- **4:** cross-team constraints and staged validation resolve a documented
  disagreement with quantified stopping conditions.

## R10: Communication and teach-back

- **0:** no review or defense evidence.
- **1:** vocabulary is recited without causal explanation.
- **2:** understandable summary with weak challenge handling or uncertainty.
- **3:** concise evidence chain withstands questions without changing workload or
  failure model; feedback and follow-up owners are recorded.
- **4:** another engineer can apply the method to a different stack and identify
  where the evidence would stop transferring.

## Result thresholds

- **Pass:** every gate passes, average at least 3.0, and R06/R07 are nonzero.
- **Revise:** no hard gate or safety-critical failure, but average is below 3.0 or
  remediable evidence/communication gaps remain.
- **Repeat:** G02–G05 fails or R06/R07 is zero.
