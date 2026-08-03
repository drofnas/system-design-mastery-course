---
lesson_id: L03
title: Authorization models and enforcement
---

# Authorization models and enforcement

## Outcomes

- Express authorization as a decision over subject, object, action, context, and policy version.
- Select role, attribute, relationship, or combined policy from domain needs.
- Place and test policy decision and enforcement points, including failure behavior.

## Prerequisites

L01 threats, L02 identity evidence, Module 9 consistency, and Module 10 stale-owner protection.

## Mechanism and repeatable method

Authorization evaluates a complete tuple:

`decision = policy(subject, object, action, context, policy_version)`

RBAC groups permissions by role. ABAC evaluates properties such as tenant,
classification, device, time, or incident state. ReBAC follows relationships
such as member-of, owns, delegated-by, or parent-of. Choose the simplest model
that expresses the domain without role explosion or hidden application rules.

Use this procedure:

1. inventory objects and meaningful actions, including reads, exports, searches,
   policy changes, and indirect effects;
2. write allow and deny examples before choosing the model;
3. identify authoritative attributes and relationships and their freshness needs;
4. define default deny and behavior when policy data or the PDP is unavailable;
5. place the PEP before disclosure or effect, not only in the UI or router;
6. return a decision trace safe enough for audit and debugging;
7. test subject x object x action x context, with role removal and policy change races.

Caching an allow decision creates a consistency contract. The cache key must
include every decision input and the validity window must match the tolerated
staleness. High-risk writes may require a fresher policy read than public reads.

## Worked example

Northstar uses roles for broad job function, tenant and classification
attributes for ordinary observation access, and relationships for temporary
collaboration grants. A researcher may read an observation when the authenticated
tenant matches the object's tenant and either owns the observation or has a live
delegation. Only an operator with fresh authentication may publish it.

The API is the PEP for reads and writes; the worker rechecks authorization for
delayed high-risk effects instead of trusting the enqueueing UI. A cached
relationship decision includes subject, relation, object, policy version, and
expiry. F02 attempts `approve` as an observer. The repaired trace denies the
specific action before workflow state changes.

## Common expert mistakes

- **One “admin” escape hatch:** broad roles hide object and action distinctions
  and make review, expiry, and least privilege difficult.
- **UI authorization:** hiding a button does not protect the API, queue, or worker.
- **Checking object type, not object:** permission to read one observation does
  not grant every observation.
- **Failing open:** availability pressure cannot silently convert missing policy
  data into permission.
- **Caching without policy identity:** stale decisions survive revocation or relationship changes.

## Guided practice

Write twelve Northstar cases covering researcher, collaborator, operator,
service, and break-glass subjects across read, search, export, edit, publish,
delete, and policy-change actions. Mark allow and deny outcomes, authoritative
inputs, freshness, PEP, audit fields, and failure behavior. Compare RBAC-only,
ABAC, and combined ABAC/ReBAC designs using complexity, consistency, latency,
operability, and migration cost.

## Self-check

1. Which fields belong in an authorization decision?
2. When is RBAC insufficient?
3. Why must an asynchronous worker sometimes reauthorize?
4. What must an authorization cache key contain?

## Explained answers

1. Subject, object, action, context, and the evaluated policy identity/version.
2. When permissions depend on tenant, object ownership, delegation, classification,
   or other contextual relationships that cause role explosion.
3. Identity, relationship, policy, or approval may change between enqueue and effect.
4. Every input that can change the decision, plus a bounded policy validity period.

## Sources and next work

- [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)
- [Zanzibar paper and presentation](https://www.usenix.org/conference/atc19/presentation/pang)

Complete EX-05 and EX-06 before implementing the authorization matrix.
