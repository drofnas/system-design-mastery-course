---
lesson_id: L05
title: "Secrets, keys, certificates, and encryption"
---

# Secrets, keys, certificates, and encryption

## Outcomes

- Inventory credentials and key material by purpose, scope, custodian, and consumer.
- Design issuance, distribution, use, rotation, revocation, recovery, and destruction.
- Distinguish encrypted transport/storage from authorization and data-lifecycle guarantees.

## Prerequisites

L03 least privilege, L04 tenant boundaries, and Module 5 transport security.

## Mechanism and repeatable method

A secret is a bearer of authority or confidentiality. Its risk is determined by
what it authorizes, where plaintext exists, how long it remains valid, who can
retrieve it, and whether compromise can be contained.

Build a lifecycle table for every secret, certificate, and key:

1. purpose and protected property;
2. principal, tenant, environment, audience, and operation scope;
3. generation or issuance authority and provenance;
4. storage, delivery, in-memory exposure, and prohibited sinks;
5. validity, cryptoperiod, rotation trigger, overlap, and consumer rollout;
6. revocation, compromise detection, emergency replacement, and rollback;
7. archival, recovery, destruction, audit, and owner.

Prefer short-lived, workload-bound credentials over shared static secrets.
Rotation is a distributed migration: create a new version, make consumers accept
it, switch issuance, observe, reject the old version, and verify removal. A
rotation that leaves the old version accepted has changed inventory, not risk.

Encryption in transit protects a channel; encryption at rest protects selected
storage threats. Neither authorizes a read, deletes data, validates a dependency,
or prevents a privileged process from seeing plaintext. Use reviewed protocols
and libraries. Record key hierarchy and custody instead of designing algorithms.

## Worked example

Northstar's ingest worker receives a 15-minute credential scoped to one tenant
and `feeds:write`. It cannot read observations or administer policies. The
credential is issued to a workload identity, never stored in source, and its
retrieval and use are audited without logging the value.

F04 assumes version 2 was exposed while version 3 is active. The repaired
rotation distributes version 3, confirms every consumer, stops version 2
issuance, rejects version 2 at the service, monitors attempts, and retires it.
Rollback restores compatible application code without reauthorizing the exposed
version. This distinguishes service rollback from credential rollback.

## Common expert mistakes

- **One high-value shared secret:** attribution and containment become impossible.
- **Scheduled rotation without revocation:** an exposed old value may remain valid.
- **Logging values for debugging:** central logs expand the blast radius and retention.
- **Confusing encryption with access control:** an authorized service still sees plaintext.
- **Deleting keys without recovery analysis:** premature destruction can make
  required data unrecoverable; indefinite retention can defeat deletion promises.

## Guided practice

Inventory Northstar human sessions, workload credentials, TLS certificates,
data-encryption keys, backup keys, and signing identities. For one workload
credential and one data key, write state transitions, evidence, overlap,
revocation, recovery, destruction, owner, and a no-outage rotation test. Name
what encryption does not protect.

## Self-check

1. Why is rotation a migration?
2. What proves an exposed version is contained?
3. Why does encryption not provide tenant authorization?
4. What is the danger of a shared service credential?

## Explained answers

1. Issuers and all consumers must move through compatible versions before old
   authority can be safely rejected.
2. Rejection tests at every accepting boundary plus monitoring for attempted use.
3. Decryption occurs before business authorization; a process with the key may
   still request or return the wrong tenant's data.
4. It broadens scope, prevents attribution, couples rotation, and expands compromise impact.

## Sources and next work

- OWASP Secrets Management Cheat Sheet (RES-07)
- NIST Key Management Guidelines (RES-08)

Complete EX-09 and EX-10 and preserve rotation evidence rather than screenshots alone.
