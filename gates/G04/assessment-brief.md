# G04 Assessment Brief

This is the learner-facing prompt set for the standalone Week 68 gate over
M10, M11, M12. The exact time boxes and hard floors in [gate.json](gate.json)
control. The 30-minute freeze and final scoring/closure block are managed from
the [gate overview](README.md); this brief contains the four scored parts.

Gate 4 runs in Week 68. Complete it after freezing Module 12 evidence. Freeze
each part before feedback. The practical uses an unpublished Northstar variant
and does not expose a commerce answer. Scored-part time: 5.5 hours.

Use the [sealed-local gate workflow](../../SOLO_GATE_GUIDE.md). Human review
is optional and stronger portfolio evidence, but it is not required.

## Part 1: Written examination — 75 minutes

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

## Part 2: Hidden Northstar workflow-recovery practical — 150 minutes

Run `scripts/solo_gate.py prepare --gate G04` to select one of three synthetic
cross-module variants. Before reveal,
freeze the invariant, predictions, journey/SLO impact, diagnostic plan, recovery
order, and evidence limits. Preserve raw evidence; identify two causal alternatives;
reveal the faults; apply one isolated repair per cause; rerun equivalent work.

Required evidence includes term/epoch and fencing, stable event/effect/workflow
identity, authority and derived versions, alert/incident timing, backup/replay,
RPO/RTO, regional capacity, degraded admissions, reconciliation, hashes,
operator approvals, and uncertainty. The model cannot prove production or regional guarantees.

## Part 3: Architecture defense — 60 minutes

Defend independent commerce reliability and DR decisions against frozen
solo-review questions for product, on-call, data/security, and finance roles.
An optional human panel may ask adaptive follow-ups. Derive journeys/SLOs, degradation,
incident ownership, recovery tiers, capacity, security, cost, migration,
rollback, dissent, and reversal evidence. Do not copy Northstar or change the
failure model to evade a challenge.

## Part 4: Portfolio review — 45 minutes

Index Modules 10–12 evidence by exact file heading and commit: predictions,
builds/tests, failure experiments, incident/recovery records, decisions,
evaluations, learning logs, assistance disclosures, Gate 4, and the Week 68 gate freeze; accepted findings belong in the later
Week 69 capstone delta. Sample one item per class and have the
independent post-freeze evaluator verify chronology.

## Result

Pass only when all structural gates, scored parts, three module-domain
subscores, safety-critical rows, and the overall average meet their published
floors. Revise applies only when evidence and chronology are complete and a
non-safety floor is missed. Repeat applies when an invariant fails, chronology
is invalid, evidence is fabricated or mismatched, or the causal model is
materially incorrect. A Pass creates no required remediation artifact.
