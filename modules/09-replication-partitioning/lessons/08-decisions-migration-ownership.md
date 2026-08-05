lesson_id: L08

# Data-Placement Decisions, Migration, and Ownership

## Outcomes

- Produce an evidence-driven data-placement and consistency ADR.
- Plan mixed-version migration, rollback, repair, and decommissioning.
- Defend the decision across product, data, security, finance, and operations.

## Prerequisites

Lessons 1–7, all six paired experiments, and Module 1 ADR/RFC methods.

## Mechanism and decision procedure

The ADR must let another team operate and reverse the design. Organize it by
operation, not by vendor feature:

1. **Drivers:** user outcome, invariant, workload/skew, latency/staleness,
   partition model, recovery, residency, budget, and team capacity.
2. **Evidence:** frozen predictions, schema-valid trials, production/maintainer
   sources, calculations, and explicit transfer gaps.
3. **Alternatives:** at least leader/follower, multi-leader, leaderless, and a
   simpler single-authority option where credible.
4. **Decision table:** authority, topology, N/R/W or acknowledgement, read/session
   rule, partition response, conflict/repair, partition key, hotspot control,
   placement eligibility, and telemetry per operation.
5. **Ownership:** application, data platform, security/privacy, on-call, finance,
   and policy decision rights.
6. **Migration:** compatibility, shadow/copy, verification, canary, cutover,
   rollback, reconciliation, and decommission gates.
7. **Reversal:** quantified evidence that changes topology, semantics, placement,
   or managed/custom choice.

Mixed versions are a first-class failure model. Old clients may omit session
tokens; old routers may hold stale maps; new replicas may understand metadata
old code discards. Define read/write compatibility and prevent an older path
from silently erasing siblings or residency tags. A rollback is safe only while
the old representation can consume every new committed state or a verified
reverse transform exists.

Telemetry must follow promises: accepted/error/ambiguous outcomes, version lag,
session violations, conflict age, repair backlog/rate, divergent ranges,
hot-key/tenant shares, moved bytes/keys, routing-map age, residency violations,
unit cost, and human pages. Name thresholds and owners.

## Worked example

Northstar chooses one authority for controller windows, asynchronous followers
for bounded-stale public browse, and conflict-preserving multi-site annotation
writes. Private metadata uses an eligible-node set before hashing. Migration
first writes version and residency metadata while old readers ignore but retain
unknown fields, shadows reads, copies and verifies, canaries one public tenant,
then shifts writes. Any missing key, erased sibling, session regression, or
ineligible placement stops cutover. Old state remains for the rollback window.

The defense records a finance request to reduce remote copies, a security
objection about repair destinations, and an on-call concern about backlog. The
ADR resolves what evidence would reopen each issue rather than declaring
consensus by authority.

## Common expert mistakes

- **Feature inventory instead of decision:** lists do not connect mechanisms to
  operation requirements.
- **One global consistency setting:** it hides overpayment and unsafe exceptions.
- **Rollback as deploy reversal:** state written under the new semantics may be
  unreadable or unsafe for old code.
- **Unowned repair and residency exceptions:** background correctness work fails
  silently between teams.
- **Vocabulary-only defense:** reviewers need histories, arithmetic, trials,
  uncertainty, and reversal evidence.

## Guided practice

Draft Northstar's per-operation table, compare three alternatives under the
same drivers, and build a migration gate table. Role-play data platform,
security, finance, and on-call challenges. Complete EX-16, then freeze the
independent ADR and defense before evaluation.

## Self-check

1. Why must alternatives use shared drivers?
2. What makes rollback a data problem?
3. Which telemetry detects a session guarantee failure?
4. How should unresolved disagreement appear in the ADR?

## Explained answers

1. Otherwise the comparison is rhetoric: each option can be made to win by
   changing requirements.
2. New committed metadata, versions, conflicts, or placement may not be
   representable or safe in the old system.
3. Required minimum version and observed version in session order, with routing
   and failure response.
4. As explicit dissent, owner, experiment, decision deadline, residual risk,
   and evidence threshold—not silently removed.

## Sources and next work

Use the DynamoDB and Meta cases for operated trade-offs, but retain Northstar's
own workload and failure model. Complete the ADR, defense, Module 9 assessment,
and Gate 3. Module 10 will establish time, coordination, and consensus proofs
that this module deliberately leaves open.

## PESD 2.0 extension: modern constraints and ownership

PESD 2.0 adds **tenant onboarding, suspension, export, offboarding, region movement, cells, control-plane/data-plane separation, tenant keys, quotas, SLOs, and cost attribution**.

### Repeatable decision procedure

1. Inventory the affected data, tenants, identities, providers, jurisdictions,
   control planes, evidence owners, and cost owners before selecting a mechanism.
2. State the invariant and the authority that may change it. Separate a claimed
   policy from the enforcement point and from the evidence that proves execution.
3. Freeze a prediction, implement or model the named mechanism, and record the
   accepted evidence mode and runtime boundary.
4. Inject one policy, isolation, recovery, or supplier failure in addition to the
   module's mechanism failure. Preserve raw evidence before interpretation.
5. Compare at least two options across product outcome, technical mechanism,
   security and governance, operations and recovery, economics, ownership,
   migration, and reversal triggers.

### Non-capstone extension

Apply the procedure to the module's continuing case. Add one tenant or governed
data class, one supplier or control-plane dependency, and one deletion, recovery,
or exit obligation. The completed case may demonstrate the method, but its
topology, thresholds, policy choices, and answer are not defaults for Global
Commerce.

### Evidence boundary

Use `derived`, `executed_deterministic`, `measured_loopback`,
`measured_container`, `modeled_capacity`, `fixture_replay`, or
`measured_accelerator` exactly as defined by the course. Fixture replay supports
practice and remediation only. Modeled remote scale is not local measurement.
Every trial records commit and input/configuration hashes, runtime and resource
limits, clock, warm-up/repetition policy, raw outcomes, and limitations.

### Source boundary

Use the module's bounded primary sources and preserve the local evidence boundary.
