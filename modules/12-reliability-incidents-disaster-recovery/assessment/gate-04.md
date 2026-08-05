# Gate 4: Consensus, Messaging, Reliability, and Recovery

> **PESD V1 historical contract:** Preserve this file for V1 learners and immutable evidence. PESD 2.0 uses [gates/G04/README.md](../../../gates/G04/README.md).

Gate 4 closes Week 48. Complete it after freezing Module 12 evidence. Freeze
each part before feedback. The practical uses an unpublished Northstar variant
and does not expose a commerce answer. Total learner time: 3.5 hours.

Use the [sealed-local gate workflow](../../../SOLO_GATE_GUIDE.md). Human review
is optional and stronger portfolio evidence, but it is not required.

## Part 1: Written examination — 60 minutes

1. Define a user-journey SLI whose denominator cannot exclude dependency
   failures; calculate budget and burn for a supplied workload.
2. Explain when a component reliability product is invalid because of optional
   paths, fallbacks, correlation, or shared fate.
3. Design a multi-window page and separate diagnostics for a slow dependency
   plus load-growth incident; name the first safe mitigation.
4. Recover a durable workflow after lost acknowledgement and regional failure;
   connect event/effect identity, consensus epoch, fencing, and reconciliation.
5. Given backup/log versions and timestamps, calculate RPO/RTO and design
   verified failover/failback with degraded capacity and operator controls.

## Part 2: Hidden Northstar workflow-recovery practical — 90 minutes

Run `scripts/solo_gate.py prepare --gate G04` to select one of three synthetic
cross-module variants. Before reveal,
freeze the invariant, predictions, journey/SLO impact, diagnostic plan, recovery
order, and evidence limits. Preserve raw evidence; identify two causal alternatives;
reveal the faults; apply one isolated repair per cause; rerun equivalent work.

Required evidence includes term/epoch and fencing, stable event/effect/workflow
identity, authority and derived versions, alert/incident timing, backup/replay,
RPO/RTO, regional capacity, degraded admissions, reconciliation, hashes,
operator approvals, and uncertainty. The model cannot prove production or regional guarantees.

## Part 3: Architecture defense — 30 minutes

Defend independent commerce reliability and DR decisions against frozen
solo-review questions for product, on-call, data/security, and finance roles.
An optional human panel may ask adaptive follow-ups. Derive journeys/SLOs, degradation,
incident ownership, recovery tiers, capacity, security, cost, migration,
rollback, dissent, and reversal evidence. Do not copy Northstar or change the
failure model to evade a challenge.

## Part 4: Portfolio review — 30 minutes

Index Modules 10–12 evidence by exact file heading and commit: predictions,
builds/tests, failure experiments, incident/recovery records, decisions,
evaluations, learning logs, assistance disclosures, Gate 4, and the separately
frozen Week 48 capstone revision. Sample one item per class and have the
independent post-freeze evaluator verify chronology.

## Result algorithm

Repeat if chronology is broken, raw evidence is fabricated/altered, G02–G05
fails, a safety invariant fails, or R04/R07/R08/R09 is zero. Revise if every
part exists but a section or average is below 3.0 or traceability is incomplete.
Pass only when every part and gate passes, average is at least 3.0, and
confidence is not low. Revisions are dated addenda; repeats use new hidden seeds.
