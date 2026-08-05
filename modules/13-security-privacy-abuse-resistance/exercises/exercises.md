# Module 13 Guided Exercises

Complete these with Northstar only. Freeze independent commerce work first.

## EX-01: Decompose a security target

Draw Northstar's publication path with actors, stores, processes, flows, trust
boundaries, classifications, administrative paths, and protected outcomes.

## EX-02: Convert abuse into requirements

Write three abuse cases using actor, precondition, path, property, impact. For
each choose treatment, PEP, negative test, detection, recovery, owner, and expiry.

## EX-03: Build an authentication state machine

Model login, active session, sensitive reauthentication, logout, expiry,
compromise, recovery, and authenticator replacement. Identify authoritative state.

## EX-04: Test replay and recovery

Predict and test expired session, revoked session, stale role claim, stolen
recovery code, and recovery-channel replacement.

## EX-05: Build an authorization matrix

Write at least twelve allow and deny cases across researcher, collaborator,
operator, service, assistant, and break-glass subjects.

## EX-06: Compare policy models

Compare RBAC-only, ABAC, and combined ABAC/ReBAC with the same domain cases,
consistency, latency, cache, operations, migration, and cost drivers.

## EX-07: Audit seven tenant surfaces

For API, database, cache, file, message, search/export, and administration, name
tenant authority, propagation, enforcement, denial, audit, repair, and test.

## EX-08: Design break glass

Specify trigger, requester, approver, tenant/object/action scope, authentication,
duration, visibility, audit, alert, automatic closure, and review.

## EX-09: Inventory credentials and keys

For five Northstar items, record purpose, scope, issuer, storage, plaintext
exposure, lifetime, rotation, revocation, recovery, destruction, and owner.

## EX-10: Rehearse rotation

Design a no-outage rotation for a 15-minute workload credential and prove the
exposed old version is rejected without using it as rollback.

## EX-11: Design an audit event

Define fields, prohibited values, source identity, integrity, access, retention,
tamper detection, logging failure, alert, and investigation use.

## EX-12: Build a data copy ledger

Trace researcher contact and private observations through active, derived,
export, log, and backup copies. Record purpose, owner, retention, and deletion.

## EX-13: Verify deletion and restore

Write predictions and queries proving active deletion, exception expiry, and
restore-time tombstone replay without erasing required audit attribution.

## EX-14: Verify dependency provenance

Define approved source, revision, digest, builder, provenance, inputs, policy,
quarantine, rollback, replacement, and owner. Test a wrong digest and wrong builder.

## EX-15: Bound economic abuse

Choose work/cost units and limits per subject, tenant, and system. Protect
incident and deletion work. Specify denial, fairness, telemetry, and recovery.

## EX-16: Specify a high-risk tool contract

Define typed arguments, subject, tenant, object, action, bounds, fresh approval,
credential scope, idempotency, budget, audit, denial, and ambiguous-effect repair.

## EX-17: Run adversarial assistant tests

Test direct and retrieved injection, encoded instructions, cross-tenant objects,
stale approval, duplicate effects, and exhausted budgets. Preserve denials.

## EX-18: Defend a security architecture

Compare three architectures using protected outcomes, threats, evidence,
operations, privacy, cost, migration, ownership, residual risk, and reversals.
Teach the causal model and answer hostile follow-up questions without AI.

## PESD 2.0 extension to the final exercise

Extend the final guided exercise with obligation-to-control-to-evidence mapping, privacy impact reasoning, secure SDLC, source-to-deployment identity, cryptographic inventory, crypto agility, and post-quantum migration planning. Produce an
obligation/control/evidence row, a named owner, a bounded cost or capacity
effect, a failure or policy-drift test, a migration step, and a reversal trigger.
Label every observation with an accepted evidence mode and do not use fixture
replay as independent Build, Break, Implement, or Measure evidence.
