---
lesson_id: L06
title: "Audit, privacy, and data lifecycles"
---

# Audit, privacy, and data lifecycles

## Outcomes

- Design attributable, privacy-aware, tamper-detectable security events.
- Trace classified data through collection, use, copies, retention, deletion, and recovery.
- Verify lifecycle claims and record legal, contractual, and operational exceptions.

## Prerequisites

Module 11 derived-state repair, Module 12 backup/recovery, and L01 protected assets.

## Mechanism and repeatable method

Audit evidence answers who or what attempted which action on which object, under
which authority and policy, at what time, with what outcome. It must be useful
for investigation without becoming a second sensitive database.

An audit event needs event identity, actor and authentication context, tenant,
object class and safe identifier, action, decision/outcome, policy/control
version, enforcement point, time source, correlation, and reason category.
Never log credentials, raw session secrets, unnecessary personal data, or
untrusted text without encoding and size limits.

Tamper evident means modification or deletion can be detected. Techniques can
include append-only permissions, remote copies, sequence/hash links, signatures,
access audit, and independent reconciliation. None proves the event itself was
truthful; source identity and clock quality remain assumptions.

For data lifecycle, use a copy ledger:

`data class -> purpose -> authority -> transformations/copies -> access -> retention -> deletion/exception -> verification -> owner`

Deletion is a workflow across authoritative storage, caches, indexes, messages,
exports, logs, replicas, and backups. A backup exception needs a stated expiry,
access restriction, restore-time deletion replay, owner, and test. Do not invent
universal retention periods; applicable legal and contractual owners decide them.

## Worked example

Northstar classifies public catalog entries, consortium-private observations,
researcher contact data, credentials, and audit metadata separately. Private
observations feed a tenant-scoped search index; contact data never enters it.

F06 deletes a researcher profile from authoritative state but finds copies in a
cache, index, and backup. The repaired workflow records the request, deletes
active copies, proves normal and direct queries return none, records the backup
exception and expiry, and ensures restore automation reapplies tombstones before
service. F05 modifies an audit event; a sequence discontinuity triggers an alert
and the independent copy supports investigation.

## Common expert mistakes

- **Logging everything:** sensitive data, cost, noise, and access risk grow while
  investigation quality may fall.
- **Calling append-only immutable:** privileged operators, retention jobs, and
  source forgery still need controls and evidence.
- **Deleting only the primary row:** derived stores and restore paths resurrect data.
- **One retention period for all data:** purpose and obligations differ by class and copy.
- **Claiming compliance from a framework:** technical controls cannot determine
  jurisdiction, contracts, or lawful purpose by themselves.

## Guided practice

Design a Northstar denial event for cross-tenant access and an approval event for
break glass. Mark required and prohibited fields, integrity, access, retention,
failure detection, and response. Then trace researcher contact data and private
observations through every copy, including backup restore, and specify deletion
evidence and exceptions.

## Self-check

1. What is the difference between tamper-proof and tamper-evident?
2. Why can an audit log violate privacy?
3. What makes a backup deletion exception credible?
4. Why must restore participate in deletion?

## Explained answers

1. Tamper-evident designs detect change; “tamper-proof” overstates what privileged
   actors, source compromise, or destructive failures cannot do.
2. It can centralize identifiers, behavior, secrets, and long-lived personal data.
3. Scope, restricted access, expiry, owner, restore-time enforcement, and tested evidence.
4. Restoring an older snapshot can recreate records deleted after that snapshot.

## Sources and next work

- OWASP Logging Cheat Sheet (RES-09)
- NIST Privacy Framework (RES-10)

Complete EX-11-EX-13 and freeze the copy ledger before running deletion tests.
