---
lesson_id: L07
title: Supply chains, economic abuse, and security response
---

# Supply chains, economic abuse, and security response

## Outcomes

- Form dependency expectations and verify identity, digest, provenance, and policy.
- Bound resource and monetary abuse per actor, tenant, operation, and time window.
- Connect preventive failure to detection, containment, recovery, and ownership.

## Prerequisites

Module 2 overload controls, Module 12 incident response, and L05 credentials.

## Mechanism and repeatable method

Software provenance says where an artifact came from and how it was produced.
It does not decide whether the source, builder, inputs, or process are acceptable.
Verification compares signed or otherwise protected evidence with an explicit
expectation: repository, revision, builder, dependencies, review state, and
allowed exceptions.

For each dependency record owner, version/digest, source, provenance, privilege,
reachable data, update policy, vulnerability response, quarantine, rollback,
and replacement seam. A manifest without enforcement or response is inventory.

Economic abuse uses valid-looking features to consume costly work. Rate limits
must identify the scarce resource and fairness domain. Use units such as bytes
scanned, jobs admitted, model tokens, export CPU-seconds, messages, or dollars,
not only requests. Enforce per subject and tenant as well as global capacity;
otherwise one tenant can remain under a global threshold while exhausting others.

Every preventive control needs a failure plan:

`signal -> triage owner -> containment -> credential/dependency/data scope -> recovery -> verification -> review`

Security incident response shares command discipline with reliability incidents
but adds evidence preservation, exposure scoping, credential containment,
notification owners, and adversary-aware communications.

## Worked example

Northstar approves the `image-decoder` digest and its build provenance. F07
provides a different digest with no verified provenance. The repaired control
quarantines it before deployment, records the expectation mismatch, retains the
last approved artifact, and opens an owner-scoped investigation. A provenance
document from an unapproved builder would also fail.

Northstar bulk exports consume storage reads and worker minutes. F08 sends many
exports from one researcher and consortium. The repaired policy enforces
subject, tenant, and global budgets; rejects optional work before enqueue;
reports consumed units and estimated cost; and preserves operator and recovery work.

## Common expert mistakes

- **Treating an SBOM as prevention:** inventory does not verify or block an artifact.
- **Trusting any signed provenance:** a valid signature from the wrong builder is
  still outside policy.
- **Counting only requests:** one request can cause unbounded fan-out or cost.
- **IP-only limits:** shared addresses punish innocent users while distributed
  attackers evade the limit.
- **Response without recovery proof:** containment can break service or leave old
  credentials and artifacts active.

## Guided practice

Define Northstar expectations for one library and one build artifact. Include
identity, digest, builder, source, review, transitive inputs, verification,
quarantine, rollback, and owner. Then design export budgets across subject,
tenant, and system scopes using work and cost units. Add an alert and a safe
recovery test for each control failure.

## Self-check

1. Why is provenance not trust?
2. What must a dependency acceptance policy contain?
3. Why are request counts often the wrong abuse unit?
4. What changes in security incident response?

## Explained answers

1. Provenance supplies evidence; policy decides whether its identities and process are acceptable.
2. Expected source, revision/digest, builder/process, inputs, verification, exceptions, response, and owner.
3. Requests vary in fan-out, bytes, compute, money, and downstream effects.
4. Preserve evidence, scope exposure, contain credentials and artifacts, account
   for an adaptive actor, and involve notification/legal owners where applicable.

## Sources and next work

- [SLSA Specification 1.2](https://slsa.dev/spec/v1.2/)

Complete EX-14 and EX-15, then run F07 and F08 from frozen predictions.
