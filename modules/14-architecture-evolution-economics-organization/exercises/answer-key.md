# Module 14 Explained Exercise Answers

These are reasoned Northstar answers, not capstone answers. Other choices are
valid when they preserve authority, compatibility, service, cost, security, and
ownership with evidence.

## EX-01 explained answer

- Catalog code and registry release is change coupling: eight of twelve recent
  releases coordinated.
- Synchronous publication-to-catalog work would be runtime coupling: a derived
  outage could delay authority.
- Shared publication tables create data coupling: derived readers depend on
  private authoritative schema.
- Broad registry credentials create security coupling: public reads inherit
  privileges they do not need.
- Registry-only replay knowledge is ownership coupling: recovery depends on two
  people. The classes overlap; naming the dominant mechanism keeps repairs precise.

## EX-02 explained answer

The modular option wins on correctness, cost, and reversibility. The synchronous
service can win when low-latency request/response behavior is required and the
registry does not depend on it to commit. The event projection wins when derived
freshness tolerance, burst isolation, replay, and a stable owner are present.
Thresholds must be measurable, such as three coordination delays beyond ten
days, not “teams feel slow.”

## EX-03 explained answer

The current path crosses research access, registry product ownership, registry
implementation, security/privacy review, one release train, registry on-call,
and support. The target still requires contract communication, but routine
catalog presentation changes remain within research access. Contract changes
are service interactions; temporary migration work is collaboration with an
exit test.

## EX-04 explained answer

Two secondary operators receive least-privilege access and an immutable scenario
identity. Without the experts, they diagnose lag, pause consumption, replay a
bounded range, reconcile counts/versions/hashes, roll back routing, communicate
status, and complete a handoff. Pass requires correct outcomes within the target,
not merely reading the runbook.

## EX-05 explained answer

The platform lane is defensible because recovery and telemetry are already
staffed and its quota covers the 20× burst. It is not automatically best. The
matrix must expose managed price/limit risk, open-source upgrade/on-call work,
polling lag/load, and platform support/adoption cost. Every option needs a data
export, replacement path, owner, and estimated exit duration.

## EX-06 explained answer

A thin offer includes versioned event publication/consumption, tenant-scoped
credentials, idempotency, replay, lag telemetry, schema checks, a tested recovery
runbook, self-service provisioning, bounded support, and exceptions with an
owner. Measure time to first safe event and support load. Retire features with
no users or outcome rather than growing a universal platform.

## EX-07 explained answer

Modular: $9,000 + $16,000 + $5,000 = $30,000; $30,000 / 530,000 × 1,000 =
$56.60. Candidate: $15,000 + $24,000 + $3,000 + $12,000 = $54,000;
$54,000 / 538,000 × 1,000 = $100.37. Failed, stale, or slow reads consumed
resources without delivering the defined outcome, so counting them would reward
quality loss.

## EX-08 explained answer

Price shock yields $72,000 total and $133.83 per 1,000 at 538,000 good reads,
crossing $105. Five percent fewer good reads makes the original candidate
$105.65, also crossing. Doubling transition amortization yields $66,000 and
$122.68. Each case stops expansion; the price shock is the largest modeled
effect, but all three require review.

## EX-09 explained answer

During expansion, v1 consumers must accept v2 envelopes because the old field
remains and unknown optional fields are ignored. V2 consumers accept v1 through
the documented default. A v2-only contracted producer with a v1 consumer is
unsupported and must be prevented or rejected before effect. Replay fixtures
cover both stored versions. “Same major version” alone does not establish this.

## EX-10 explained answer

Deploy tolerant readers and replay fixtures; expand schema; emit both fields;
backfill and reconcile; inventory live, delayed, and replay consumers; observe
zero v1-only use for the retention window; expire rollback dependence; announce
and test the major change; then remove `public`. Contracting earlier makes
rollback or an old consumer unsafe.

## EX-11 explained answer

Authority remains the registry in every state. Candidate reads become
authoritative only for catalog delivery, never publication approval. Every state
has an evidence gate: compatibility, reconciliation, shadow comparison, bounded
cutover, absence, or removal. If a row cannot name safe rollback or roll-forward,
the preceding state must not promote.

## EX-12 explained answer

The cursor cannot distinguish completed from uncertain work. Correct ordering is
derive stable batch → write idempotently with source version → durably record
results → advance checkpoint. Restart repeats batch 42. Reconciliation of IDs,
versions, and hashes proves completeness; row count alone is insufficient.

## EX-13 explained answer

Sort results by stable observation ID, compare source versions and tenant/public
scope exactly, round only declared display precision, and exclude request IDs and
timestamps that have no contract meaning. Missing, extra, wrong-scope, stale, or
different authoritative content is semantic. Presentation ordering may be
harmless only when the public contract does not promise order.

## EX-14 explained answer

Crashes can occur before the database, after it but before the call, after the
remote write but before acknowledgement, or during retry. These produce missing
projection, duplicate call, or ambiguous success. Commit registry state and an
outbox atomically; publish and apply idempotently; reconcile the projection from
the authoritative version.

## EX-15 explained answer

Use 5%, 25%, 50%, then 100% segmented traffic with a full peak observation at
each material step. Require zero authority/tenant mismatch, bounded explained
presentation mismatch, freshness and p95 targets, unit cost ≤$105, and exercised
operators. Rollback is safe only while the old path preserves all post-cutover
state; otherwise stop earlier or prepare roll-forward.

## EX-16 explained answer

Each broken pair should fail its named I03–I11 invariant while holding shared
inputs constant. Contain before repair: halt rollout/backfill/cutover, fence the
second writer, restore authoritative routing, enforce budget, activate exit, or
escalate ownership. Preserve the first output and rerun only as a new repaired
trial.

## EX-17 explained answer

A defensible sequence is instrument; modularize and introduce a seam; expand,
backfill, and shadow; bounded cutover, contract, and decommission. The first two
steps improve evidence and structure even if extraction stops. Each later step
is conditional on compatibility, cost, owner, security, and rollback gates.

## EX-18 explained answer

Resolve title-based disagreement with the ledger. Immediate extraction lacks
comparison and ownership evidence; permanent modularity ignores measured delay
and failure distraction. Choose modular seam first, then condition extraction on
flow, shadow, cost, and ownership results. Preserve finance's concern that the
transition premium may not expire as a dated risk with an owner and threshold.

## PESD 2.0 extension answer

A defensible answer covers a thin local platform product with a service catalog, self-service interface, golden path, policy guardrails, exception path, ownership metadata, platform SLO, adoption and support metrics, FinOps allocation, and an exit plan. It distinguishes the
requirement, enforcement mechanism, evidence, and owner; keeps modeled and
measured results separate; and names the failed condition that would reverse
the decision. Different architectures are acceptable when their invariants,
evidence boundaries, migration, and residual risk are explicit.
