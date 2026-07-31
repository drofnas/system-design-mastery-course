# Module 3 Anchored Rubric

## Scoring

Use integer scores 0–4. Every score cites the submitted file and heading.

| Score | General meaning |
|---:|---|
| 0 | Missing, unsafe, fabricated, or materially false |
| 1 | Vocabulary without an operable causal model |
| 2 | Plausible happy path with important evidence gaps |
| 3 | Defensible, scoped decision with adequate evidence |
| 4 | Quantified, adversarially tested, reproducible, and teachable judgment |

## R01: Machine and workload model

- **0:** The measured work or machine boundary is absent or materially false.
- **1:** Names hardware or workload totals without logical-work identity,
  constraints, or production boundary.
- **2:** Work, host, and runtime exist, but operation mix, data shape, compiler,
  filesystem, constraints, or claim boundary is incomplete.
- **3:** Logical work, equivalent-work checksum, machine/kernel/architecture,
  compiler flags, data shape, runtime, filesystem, and constraints are explicit.
- **4:** Sensitivity identifies which uncertain machine or workload assumption
  changes the decision and assigns an evidence owner and follow-up.

Remediation: Lesson 1; EX-01–EX-02.

## R02: Benchmark validity

- **0:** Results are invented, altered, incomparable, or cannot support the claim.
- **1:** Reports elapsed time without work equivalence or a measurement boundary.
- **2:** Repetitions and timing exist, but warm-up, CPU time, host noise,
  confidence, scenario identity, or limitations are weak.
- **3:** Frozen prediction, equivalent work, monotonic timing, repetitions,
  scenario/commit identity, counters, environment, and limitations support the claim.
- **4:** Competing measurement explanations are falsified and observed variance
  sets a decision-relevant effect threshold.

Remediation: Lesson 1; EX-01–EX-03.

## R03: Locality and processor reasoning

- **0:** The conclusion contradicts the work or attributes every change to cache.
- **1:** Uses pipeline/cache vocabulary without an access or branch model.
- **2:** Locality or branch variants exist, but copying, compiler behavior,
  prefetch, equivalent work, or counterevidence is incomplete.
- **3:** Access pattern, branch predictability, copying, working set, checksum,
  and observed behavior form a scoped causal chain.
- **4:** A counterintuitive result is reproduced and separated from compiler,
  frequency, prefetch, NUMA, and measurement alternatives.

Remediation: Lesson 1; EX-02–EX-03.

## R04: Scheduling and syscall reasoning

- **0:** Concurrency is unbounded or scheduling claims contradict observed work.
- **1:** Treats thread count, context switches, or syscall count as performance by itself.
- **2:** Oversubscription or batching is measured, but runnable work, quota,
  blocking, useful throughput, or scheduler evidence is incomplete.
- **3:** Runnable work, thread/process boundaries, system calls, user/system CPU,
  context switches, quota, throttling, and useful throughput support the diagnosis.
- **4:** Controlled variants separate scheduler, syscall, lock, and device-queue
  explanations and define where the result transfers to production.

Remediation: Lesson 2; EX-04–EX-05.

## R05: Memory behavior and containment

- **0:** Required memory can grow without a bound or memory claims are materially false.
- **1:** Equates allocation, virtual size, RSS, or page faults without a mechanism.
- **2:** Page-touch/allocation tests exist, but lifetime, reclaim, faults, limit,
  OOM outcome, or accounting boundary is incomplete.
- **3:** Allocation lifetime, page touching, RSS, major/minor faults, reclaim
  pressure, container limit, outcome, and workload checksum are connected.
- **4:** Repeated pressure tests distinguish allocator, page cache, reclaim, and
  cgroup explanations while defining a conservative operating response.

Remediation: Lesson 3; EX-05–EX-06.

## R06: Concurrency safety — safety critical

- **0:** Data races, unsafe effects, unbounded waits, or an uncontained deadlock remain.
- **1:** Uses locks or atomics without invariants, ownership, or progress bounds.
- **2:** Correct final counts exist, but contention, timeout, cancellation,
  lock ordering, false sharing, or failure cleanup is incomplete.
- **3:** Shared-state invariants, lock ownership/order, bounded waits, watchdog,
  equivalent work, contention evidence, and cleanup are explicit and tested.
- **4:** Adversarial schedules and configuration failures preserve correctness,
  bounded termination, observability, and an auditable rollout path.

Remediation: Lesson 4; EX-07–EX-08.

## R07: Durability safety — safety critical

- **0:** Acknowledgement can falsely claim durability or corruption/loss lacks containment.
- **1:** Mentions flush or `fsync` without defining data, metadata, and failure boundary.
- **2:** Buffered and durable variants exist, but acknowledgement point,
  directory durability, partial writes, error handling, or recovery is incomplete.
- **3:** Buffered completion, writeback, file sync, rename/directory boundary,
  acknowledgement, errors, recovery, and retained evidence are explicit.
- **4:** Bounded fault experiments challenge partial progress and crash windows;
  the decision quantifies latency, loss window, recovery, and ownership trade-offs.

Remediation: Lessons 5–6; EX-09–EX-10.

## R08: Resource containment and operational transfer

- **0:** Experiments require unsafe privilege/global changes or container results
  are represented as bare-metal guarantees.
- **1:** Names a CPU/memory limit without controller evidence or ownership.
- **2:** Limits are bounded, but throttling, OOM, PID, I/O, runtime overhead,
  monitoring, or host-versus-container scope is incomplete.
- **3:** Unprivileged CPU/memory/PID/I/O bounds, controller evidence, outcomes,
  runtime/filesystem limitations, production signals, and owners are explicit.
- **4:** Combined limits and noisy-neighbor cases drive staged operations,
  alerting, rollback, capacity, and cross-team commitments.

Remediation: Lesson 7; EX-10–EX-11.

## R09: Causal diagnosis

- **0:** Conclusions contradict raw evidence or observations were overwritten.
- **1:** Charts symptoms and selects a familiar mechanism without alternatives.
- **2:** A hypothesis and comparison exist, but falsification, repetitions,
  limitations, or contradictory evidence is weak.
- **3:** Observation, interpretation, alternatives, discriminating tests,
  repetitions, limitations, and a preserved failed prediction form a causal chain.
- **4:** Multiple independent counters and interventions rule out plausible
  alternatives and prioritize the next decision-changing experiment.

Remediation: Lesson 8; EX-11–EX-12.

## R10: Decision and teach-back quality

- **0:** No decision, unsafe rollout, or defense changes assumptions to evade critique.
- **1:** Recommends a tool or faster variant without a driver/evidence chain.
- **2:** A choice exists, but scope, correctness, cost, owner, migration,
  rollback, residual risk, or reversal is weak.
- **3:** Report and defense connect mechanism to a scoped choice, correctness,
  security, cost, operations, ownership, migration, rollback, and reversal.
- **4:** The teach-back makes a counterintuitive result reusable, resolves a
  stakeholder conflict with evidence, and records how uncertainty changes policy.

Remediation: Lesson 8; EX-12.

## Result

- Pass: all structural gates, average ≥ 3.0, no zero in R06 or R07.
- Revise: complete set but insufficient evidence for a defensible decision.
- Repeat: prediction/artifact integrity fails, evidence is fabricated, required
  work is unbounded, concurrency/durability safety fails, or the machine model
  is materially false.
