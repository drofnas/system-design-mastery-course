# Module 15 Anchored Rubric

## R01: Equivalent work and conformance

- **0:** variants change required work or count invalid outcomes as success.
- **1:** similar code without a semantic contract, hashes, or four-runtime evidence.
- **2:** baseline conforms but retries, payload, limits, or denominator differ.
- **3:** logical work, limits, success, hashes, schemas, and all runtimes align.
- **4:** negative and compatibility fixtures expose subtle non-equivalence.

## R02: Memory lifetime and management

- **0:** ownership/release model permits known corruption or unbounded retention.
- **1:** stack/heap/GC/ownership vocabulary without values and resources.
- **2:** main lifetimes exist but aliases, cycles, external resources, or measurement are weak.
- **3:** placement, owners, aliases, release triggers, pressure, and limits align.
- **4:** retainer/release evidence changes design without overgeneralizing a model.

## R03: Scheduler and concurrency model

- **0:** blocking or queued work is materially unbounded.
- **1:** async/thread labels without scheduler, queue, or capacity.
- **2:** main scheduler mapped but worker, fairness, or overload evidence is weak.
- **3:** producers, queues, schedulers, work class, bounds, and overload align.
- **4:** runnable/blocked evidence and falsification explain counterintuitive tails.

## R04: Types, serialization, and validation

- **0:** untrusted bytes gain typed meaning or authority without validation.
- **1:** generated/interface types are treated as runtime checks.
- **2:** shape validation exists but semantic, authorization, or compatibility checks are weak.
- **3:** syntax, shape, semantics, authorization, bounds, errors, and evolution agree.
- **4:** negative mixed-version fixtures validate meaning across all runtimes.

## R05: Bounded fan-out correctness

Safety-critical because unbounded or late child work can exhaust capacity or act
after the caller's authority expires.

- **0:** repaired evidence still expands deadlines, creates unbounded work, or loses required semantics.
- **1:** parallel calls without global bounds, one deadline, ownership, or overload.
- **2:** happy path works but optional/required, admission placement, or cleanup is weak.
- **3:** admission, deadlines, classification, cancellation, join, assembly, and overload agree.
- **4:** burst, partial, timeout, and shutdown variants retain every invariant.

## R06: Visibility and race safety

Safety-critical because repeated correct observations can hide undefined or
language-permitted stale behavior.

- **0:** repaired evidence contains a race or false happens-before claim.
- **1:** detector/lock vocabulary without conflicting accesses or invariant oracle.
- **2:** tool is clean but schedule coverage, edge proof, or business correctness is weak.
- **3:** graph, synchronization, detector/static evidence, oracle, and limits agree.
- **4:** alternate schedules and implementations preserve protocol and quantify contention.

## R07: Cancellation, cleanup, and resource safety

Safety-critical because orphan work and leaked resources outlive request scope.

- **0:** repaired task/effect/resource remains after cleanup grace.
- **1:** timeout/RAII/defer labels without identity or post-grace evidence.
- **2:** main cleanup works but parse, error, shutdown, or cancellation paths are weak.
- **3:** ownership, stable identities, acknowledgement, matched release, and zero deltas agree.
- **4:** repeated cancellation and exception variants validate cleanup under saturation.

## R08: Failure diagnosis and evidence integrity

Safety-critical because changed work or rewritten trials can manufacture a runtime conclusion.

- **0:** chronology/evidence is altered or a repaired target remains failed.
- **1:** conclusions without predictions, hashes, pairs, or causal alternatives.
- **2:** most pairs work but one-control isolation, host identity, or uncertainty is weak.
- **3:** F01–F09 predictions, pairs, targets, repairs, invariants, and limits agree.
- **4:** additional falsification narrows causal claims while preserving all evidence.

## R09: Operations, security, cost, migration, and ownership

- **0:** decision leaves a critical security/operational failure or unowned runtime.
- **1:** ecosystem/team preference without lifecycle obligations.
- **2:** useful comparison with weak patching, telemetry, cost, migration, or succession.
- **3:** operations, security, cost, dependencies, owners, migration, rollback, and stops align.
- **4:** exercised adoption/exit evidence and cross-team dissent change scope or sequencing.

## R10: Decision and teach-back

- **0:** universal ranking, unsafe adoption, or inability to explain causal model.
- **1:** preferred language without alternatives, evidence, or reversal.
- **2:** decision exists but uncertainty, no-change, bounded adoption, or teaching transfer is weak.
- **3:** drivers, alternatives, evidence, dissent, choice, reversals, defense, and revision align.
- **4:** the frozen role-based transfer exercise applies the method to a
  different workload and improves it. Optional human application upgrades
  attestation, not score.

## Thresholds

Pass requires every gate, average ≥3.0, and no zero in R05–R08. Revise preserves
safety but repairs gaps. Repeat follows G02–G05 failure or a safety-critical zero.
