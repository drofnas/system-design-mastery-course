# Module 10 Anchored Rubric

## R01: Clock uncertainty and causal order

- **0:** wall-clock or scalar timestamp is used as proof of authority/causality despite contradictory evidence.
- **1:** clock terms without calculations, event graph, assumptions, or failure response.
- **2:** useful drift/order analysis with material interval, vector, identity, or oracle gaps.
- **3:** drift/skew/uncertainty calculations, happened-before, Lamport/vector traces, limits, and fail-closed rules agree.
- **4:** adversarial clock/identity variants teach exactly when physical, logical, causal, and total orders support different decisions.

## R02: Safety, liveness, failure detection, and consensus boundary

- **0:** unsafe competing authority is admitted or liveness is claimed without required quorum/fairness.
- **1:** vocabulary without forbidden histories, conditional progress, failure model, or alternatives.
- **2:** plausible properties with weak operation scope, detector assumptions, quorum-loss behavior, or simpler choices.
- **3:** falsifiable safety/liveness, suspicion semantics, operation boundaries, alternatives, and failure responses align.
- **4:** discriminating histories prove where consensus changes outcomes and where it only adds cost/operational risk.

## R03: Leader election, terms, votes, and persistence

- **0:** two repaired leaders can exist in one term or a dependent response precedes required persistence.
- **1:** election labels without event order, log eligibility, majority, or restart state.
- **2:** happy election works with weak higher-term, split-vote, persistence, or liveness evidence.
- **3:** state transitions, one durable vote, up-to-date checks, quorum certificates, demotion, and recovery agree.
- **4:** adversarial restart/partition schedules and independent oracles establish election safety while scoping progress assumptions.

## R04: Replicated-log commitment and state-machine application

- **0:** committed state is overwritten/lost or different commands apply at one index.
- **1:** replicated-log terms without predecessor checks, commit rule, or applied history.
- **2:** common path works with weak conflict repair, current-term commitment, determinism, or recovery coverage.
- **3:** log matching, safe truncation, commitment, leader completeness, ordered application, and proof ledger agree.
- **4:** counterexample schedules connect implementation state to abstract invariants and falsify incorrect commit shortcuts.

## R05: Client identity and linearizable reads

- **0:** duplicate delivery repeats an irreversible effect or an authority read is served by known-stale leadership.
- **1:** idempotency/linearizability labels without identities, response state, barrier, or ambiguity.
- **2:** basic dedup/read path with weak retention, snapshot, leader-change, apply-lag, or deadline behavior.
- **3:** replicated client result state and quorum/apply read barrier handle duplicates, ambiguity, and leadership change.
- **4:** adversarial retries, sequence gaps, expiry, snapshots, and concurrent reads prove the scoped client contract.

## R06: Snapshots, compaction, and membership

- **0:** snapshot/reconfiguration loses committed state, dedup/fence data, or permits disjoint decisions.
- **1:** mechanism names without metadata, atomic activation, quorum transition, or recovery.
- **2:** useful path with weak interruption, checksum, learner catch-up, joint quorum, rollback, or mixed-version evidence.
- **3:** snapshot contents/activation/restart and old-joint-new membership preserve committed prefix and overlap.
- **4:** repeated interruptions and partitioned reconfiguration establish safe recovery, capacity limits, compatibility, and reversal gates.

## R07: Leases, epochs, fencing, and protected resources

- **0:** a stale authenticated owner can mutate the protected resource.
- **1:** lease/fence vocabulary without timing ledger, monotonic allocation, resource check, or exception path.
- **2:** nominal fencing works with weak pause, renewal, every-write enforcement, credential, audit, or recovery coverage.
- **3:** explicit lease assumptions plus authoritative epochs and resource-side monotonic checks reject every modeled stale owner.
- **4:** adversarial clock/pause/delay/credential variants prove failure behavior and define when the lease optimization must disable.

## R08: Evidence integrity and causal diagnosis

Safety-critical because changed predictions, mismatched pair inputs, fabricated
trials, or contradictory arithmetic invalidate every conclusion.

- **0:** baseline/raw evidence changed, pair hashes differ, or conclusions contradict schema-valid events.
- **1:** symptoms restated without hashes, first divergence, isolated controls, alternatives, or uncertainty.
- **2:** most pairs exist but provenance, calculations, reruns, causal alternatives, or evidence boundaries are weak.
- **3:** F01–F08 preserve predictions/raw pairs, prove shared inputs/changed controls, recalculate traces, and isolate repairs.
- **4:** discriminating variants falsify strong alternatives and reproduce the observable contract in a second environment.

## R09: Consensus and stale-authority safety

Safety-critical because duplicate leaders, conflicting applied logs, stale
authority, corrupt snapshots, or disjoint membership can cause irreversible harm.

- **0:** any repaired core invariant fails.
- **1:** safety asserted without terms, votes, logs, indexes, client state, fences, snapshots, and membership evidence.
- **2:** happy paths pass but one named failure family or oracle is materially weak.
- **3:** all eight repaired pairs preserve election, log, application, client, fencing, snapshot, and membership invariants.
- **4:** independent or formal-model oracles cover adversarial schedules without overclaiming untested production properties.

## R10: RFC, operations, security, cost, migration, defense, and remediation

- **0:** unsafe cutover/ownership or materially false production claim.
- **1:** preference without shared drivers, operated contract, alternatives, or owners.
- **2:** decision exists but cost, security, telemetry, quorum loss, migration, rollback, dissent, or reversal is weak.
- **3:** evidence-driven RFC and defense cover properties, alternatives, operation, security, cost, migration, owners, dissent, and remediation.
- **4:** the frozen role-based transfer exercise resolves disagreement and
  applies the method to a different stack with measured reversal thresholds.
  Optional team review upgrades attestation, not score.

## Result thresholds

- **Pass:** every gate passes, average at least 3.0, and R08/R09 are nonzero.
- **Revise:** no hard/safety failure, but average is below 3.0 or material gaps remain.
- **Repeat:** G02–G05 fails or R08/R09 is zero.
