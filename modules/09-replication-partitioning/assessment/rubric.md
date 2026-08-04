# Module 9 Anchored Rubric

## R01: Operation semantics and session guarantees

- **0:** an admitted history violates an important operation invariant or semantics are materially false.
- **1:** labels without histories, ordering, failure response, threshold, or oracle.
- **2:** useful table with material scope, token, staleness, causal, or falsification gaps.
- **3:** each operation maps outcome, authority, violating history, weakest sufficient contract, failure response, threshold, and oracle.
- **4:** adversarial histories and sensitivity establish when a stronger/weaker contract changes user, cost, or operating outcomes.

## R02: Replication and acknowledgement boundaries

- **0:** success is acknowledged beyond the stated durable authority or unsafe follower/multi-writer behavior is accepted.
- **1:** topology names without event order or durability/visibility boundaries.
- **2:** plausible topology with weak acknowledgement, lag, conflict, failure-domain, or ownership detail.
- **3:** leader/follower, multi-leader, and leaderless alternatives have explicit accept/replicate/durable/ack/visible order and scoped trade-offs.
- **4:** failure and cost sensitivity prove the chosen boundary and reversal thresholds across operation classes.

## R03: Quorums and partition assumptions

- **0:** invalid quorum arithmetic or an intersection is claimed to prove linearizability/safety despite contradictory evidence.
- **1:** N/R/W vocabulary without separate intersections or assumptions.
- **2:** arithmetic works but membership, durability, version selection, concurrency, sloppy quorum, or availability definition is incomplete.
- **3:** read/write and write/write intersections, maps, responses, durability, versions, partition behavior, and repair assumptions agree.
- **4:** counterexamples across membership/failure variants teach exactly which property each assumption supports.

## R04: Versions, conflicts, repair, and convergence

- **0:** concurrent valid state is silently lost or repair publishes incorrect authority.
- **1:** version/repair terms without supersession, siblings, merge, coverage, or oracle.
- **2:** basic conflicts and repair work with weak provenance, cold-key coverage, cost, authorization, or convergence proof.
- **3:** supersession, sibling preservation, domain resolution, read repair, anti-entropy, resource bounds, and independent convergence evidence agree.
- **4:** repeated/reordered repairs and adversarial conflicts prove idempotence, safety, cost limits, and reversal conditions.

## R05: Partitioning and resharding

- **0:** migration loses a key, admits duplicate authority, violates placement, or destroys rollback.
- **1:** hash/range terms without ownership, movement, load, or migration sequence.
- **2:** placement works with weak skew, replica, routing, catch-up, verification, mixed-version, or rollback evidence.
- **3:** hash/range/consistent-hash comparison, movement/load calculations, copy/catch-up/verify/cutover/rollback/decommission gates, and owners agree.
- **4:** workload and membership sensitivity prove safe capacity, transfer, compatibility, and reversal thresholds.

## R06: Hotspots, fairness, tenant isolation, and residency

- **0:** one tenant can read forbidden data, corrupt another tenant, or exhaust safety-critical capacity without control.
- **1:** hotspot/security labels without per-key/tenant/resource evidence or placement inventory.
- **2:** useful mitigation with weak semantics, scarce-resource enforcement, repair traffic, derived-copy, exception, or cost coverage.
- **3:** per-key/node/tenant evidence drives safe mitigation, capacity reserves, eligible placement, access/deletion proof, cost, and owners.
- **4:** adversarial skew and policy exceptions prove isolation and recovery under budget and regional constraints.

## R07: Evidence integrity and causal diagnosis

Safety-critical because changed predictions, mismatched pairs, fabricated trials,
or contradictory arithmetic invalidate every distributed-systems conclusion.

- **0:** baseline/raw evidence changed, pair inputs differ, or claims contradict schema-valid trial evidence.
- **1:** fault labels restate symptoms without hashes, histories, alternatives, or uncertainty.
- **2:** most pairs exist but ordering, same-input proof, ratios, causal alternatives, or evidence boundary is incomplete.
- **3:** F01–F06 preserve predictions, scenarios, raw pairs, hashes, calculations, isolated repairs, reruns, alternatives, and uncertainty.
- A passing evidence chain also links A11 to the unchanged F01 pair and keeps
  postmortem causality distinct from the cross-trial failure matrix.
- **4:** discriminating variants falsify strong alternatives and explain failed predictions across implementation boundaries.

## R08: Distributed correctness and convergence

Safety-critical because stale authority, lost conflicts, session regression,
non-convergence, missing keys, or duplicate owners can cause irreversible harm.

- **0:** a repaired invariant fails, conflict is lost, required session regresses, repair diverges, or resharding loses/duplicates authority.
- **1:** safety asserted without histories, versions, acknowledgement, repair, and placement oracles.
- **2:** happy paths pass but partition, leader, lag, ambiguous outcome, conflict, convergence, reshard, or isolation coverage is weak.
- **3:** all six repairs preserve scoped invariants with explicit unavailability, version/session evidence, convergence, placement integrity, and exclusions.
- **4:** independent oracles and adversarial schedules reproduce the contract in a second environment without overclaiming consensus or durability.

## R09: ADR, migration, security, operations, and cost

- **0:** unsafe authority/cutover, forbidden placement, unowned repair, or false production claim.
- **1:** preference without shared drivers, evidence, owners, or migration.
- **2:** decision exists but operation scope, telemetry, security, cost, compatibility, rollback, dissent, or decommissioning is weak.
- **3:** evidence-driven ADR covers alternatives, per-operation policy, security/residency, cost, telemetry, owners, staged migration, rollback, dissent, and reversal.
- **4:** mixed-version and partition rehearsals resolve cross-team disagreement under failure, latency, and budget pressure.

## R10: Gate 3, defense, teach-back, and remediation

- **0:** Gate 3/defense is missing or explanation depends on materially false behavior.
- **1:** vocabulary recited without storage, transaction, replica, partition, or evidence derivation.
- **2:** understandable defense with weak hidden practical, portfolio traceability, challenge, dissent, uncertainty, or remediation linkage.
- **3:** all four Gate 3 parts pass; teach-back derives Modules 7–9 mechanisms, handles four stakeholder views, records changed belief/dissent, and preserves dated remediation.
- **4:** another team applies the method to a different stack and resolves a cross-module data decision with evidence.

## Result thresholds

- **Pass:** every gate passes, average at least 3.0, and R07/R08 are nonzero.
- **Revise:** no hard/safety failure, but average is below 3.0 or material gaps remain.
- **Repeat:** G02–G05 fails or R07/R08 is zero.
