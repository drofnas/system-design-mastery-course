# Module 13 Explained Answers

These are reasoning checks, not optional project answers. Other designs are acceptable
when their properties and evidence are defensible.

## EX-01

A complete model includes researcher, operator, service and attacker identities;
API, authoritative state, publication worker, catalog, index, assistant, tool
gate, audit, build and administrative paths; and labels for tenant, data class,
identity, authority, and trust changes. Missing restore or support paths is a
material gap because both can bypass normal controls.

## EX-02

“Researcher changes tenant ID and receives another tenant's observation” is
testable. “Cross-tenant attack” is not. A strong answer places enforcement before
disclosure, expects zero objects, records a safe denial event, names repair and
owner, and expires any accepted gap.

## EX-03

Authentication and session states must include recovery and replacement. The
server or identity authority owns expiry/revocation; a client clock or hidden UI
cannot. Sensitive publication uses fresh reauthentication rather than assuming
the original login proves current presence.

## EX-04

Every stale or revoked credential is denied server-side before protected work.
Recovery material is one-time, expiry-bound, and invalidated after use; replacing
the recovery channel requires stronger evidence and notification. A stale role
claim is handled by bounded token life or an authoritative check appropriate to risk.

## EX-05

The matrix must distinguish object and action. Researcher read-own and read-other
are separate. Publish, delete, export, policy change, and break glass are separate.
Each deny case identifies the PEP and avoids leaking object existence.

## EX-06

RBAC is simple for stable job functions but strains under tenant, ownership, and
temporary collaboration. ABAC expresses context; ReBAC expresses delegations.
The combined model is justified only if policy consistency, cache invalidation,
operations, and migration are owned. Centralization is not automatically required.

## EX-07

Tenant identity comes from verified membership. Every surface must bind or
verify it. Cache keys and search filters are common omissions. Administrative
and restore paths require the same invariant, not a permanent internal bypass.

## EX-08

Break glass is specific, approved, fresh-authenticated, short-lived, visible,
attributed, alerted, auto-closed, and reviewed. A standing support-admin role is
not break glass because it lacks exceptional state and bounded authority.

## EX-09

Strong inventories distinguish human session secrets, workload tokens, TLS
keys, data keys, and signing identities. Each has different consumers and
recovery. “Stored in secret manager” is incomplete without scope, plaintext
exposure, access, rotation, revocation, and evidence.

## EX-10

The repaired sequence distributes new authority, observes consumers, switches
issuance, rejects old authority, monitors attempts, and removes copies. Rollback
restores code compatibility without accepting an exposed secret.

## EX-11

Useful events include actor, tenant, object class/safe ID, action, outcome,
policy, PEP, time, and correlation. Secrets and raw private content are excluded.
Tamper detection, access audit, logging-failure behavior, and an investigation
consumer are required; append-only marketing language is insufficient.

## EX-12

The ledger includes authoritative state, caches, indexes, messages, exports,
logs, replicas, backups, and derived analytics. Each copy needs purpose, owner,
retention, access, deletion/exception, and rebuild/restore behavior.

## EX-13

Evidence combines request identity, per-copy status, normal and direct queries,
exception expiry, and a restore test that replays deletion before service.
Removing audit attribution can reduce accountability and is not automatically correct.

## EX-14

Provenance is compared with approved source, revision, builder, process, and
inputs. A matching signature from the wrong builder fails. Quarantine blocks
admission, preserves the last good artifact, and creates an owned response path.

## EX-15

Bytes scanned and worker-seconds better represent exports than request count.
Subject, tenant, and global budgets prevent one identity or tenant from consuming
the pool. Denial occurs before enqueue and preserves recovery/security work.

## EX-16

The tool gate receives authenticated context and a structured proposal, validates
exact arguments and object, performs external authorization, requires exact
approval, and supplies a scoped credential and idempotency key. Model text has no authority.

## EX-17

A strong matrix shows every malicious input reaching a deterministic denial or a
bounded harmless output. It records original intent, policy and reason without
copying sensitive or adversarial text into long-lived logs. Duplicate effects
use reconciliation, not blind retry.

## EX-18

No-tools, proposal-only, and bounded-tools are compared with the same drivers.
Northstar chooses proposal-only because current demand does not justify the
authority and operating cost. Another answer can pass with stronger need,
evidence, approval, containment, incident response, and reversal conditions.
