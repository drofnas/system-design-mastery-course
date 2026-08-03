# Northstar Pass Calibration Submission

## Submission chronology and integrity

The Week 49 baseline commit `m13-pass-baseline` contains assets, trust boundaries,
N-T01-N-T09, and predictions before trial output. A04 contains eighteen immutable
raw JSON results. Pair manifests show one shared-input hash and exactly one
control change per pair. All repaired I01-I12 results pass. Assistance is disclosed.

## Threat model and protected outcomes

The model covers private observations, researcher contacts, publication
authority, credentials, audit evidence, dependencies, budgets, retrieved notes,
support, restore, and break glass. Each threat has treatment, PEP, negative test,
detection, recovery, owner, expiry, and reversal evidence. Analytical exports
remain an accepted risk with an owner and pre-launch expiry.

## Identity and sessions

Researcher sessions expire at 60 minutes; publication requires authentication no
older than five minutes. Server-side revocation is authoritative. Recovery uses
a registered channel, delay, notification, old-material invalidation, and session
revocation. F03 denies the revoked 90-minute session before object access.

## Authorization and tenant isolation

The policy tuple records subject, object, action, tenant, relationships, context,
and policy version. The API and publication worker are PEPs. F02 denies observer
approval. The seven-surface audit covers database, cache, files, messages,
search/exports, administration, and restore. F01 returns no cross-tenant object.
Break glass is tenant/action scoped, approved, alerted, expires in 15 minutes,
and receives post-use review.

## Secrets, keys, and encryption

The credential ledger records scope, issuer, storage, plaintext exposure,
lifetime, rotation, revocation, recovery, destruction, and owner. F04 moves to
version 3 and proves version 2 rejection without using it for rollback. Encryption
limits explicitly state that authorized processes see plaintext and keys do not authorize tenants.

## Audit and privacy lifecycle

Events contain safe actor, tenant, object, action, outcome, policy, PEP, time, and
correlation fields and prohibit credentials and private content. F05 detects a
sequence break against an independent copy. The copy ledger covers active store,
cache, index, queues, exports, logs, replicas, and backups. F06 proves active
deletion and restore-time tombstone replay while recording a restricted backup exception.

## Dependency, abuse, and security response

F07 rejects the wrong digest and unverified provenance, quarantines the artifact,
keeps last good, and assigns investigation. F08 enforces bytes-scanned and
worker-second budgets per subject, tenant, and system before enqueue while
reserving incident/deletion work. Both have alerts, recovery, and owners.

## Prompt injection and tools

Retrieved notes are untrusted data. The assistant has read-only credentials and
can produce proposals only. F09 denies `array.reconfigure` without operator
identity, fresh exact approval, scope, and policy even though the malicious note
requests it. Idempotency, budget, audit, and ambiguous-effect reconciliation are defined.

## Security architecture and defense

The RFC compares no-tools, proposal-only, and bounded-tools options plus shared
versus dedicated authorization/isolation. It selects proposal-only and layered
shared isolation from current evidence. Residual risks, operating cost, privacy,
migration, owners, dissent, and measurable reversals are recorded. Product,
security/privacy, operations, finance, and platform reviewers challenged the
decision; the recorded defense resolved two issues and assigned one experiment.

## Evidence boundaries and remediation

The report states the lab does not prove production isolation, cryptography,
physical deletion, provenance, legal compliance, or adaptive-adversary resistance.
All corrections are dated addenda. No Northstar design appears in commerce work.
