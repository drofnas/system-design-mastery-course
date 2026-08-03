---
lesson_id: L01
title: Threat models, trust boundaries, and abuse cases
---

# Threat models, trust boundaries, and abuse cases

## Outcomes

- Decompose a system into assets, actors, processes, stores, flows, and trust boundaries.
- Turn plausible abuse paths into testable security and privacy requirements.
- Assign treatment, owner, evidence, review date, and reversal conditions to every material threat.

## Prerequisites

Module 1 invariants and quality scenarios, Module 5 network boundaries, and
Module 12 incident and recovery ownership.

## Mechanism and repeatable method

A threat model is a maintained decision artifact, not a catalog of famous
attacks. Use four passes:

1. **Model:** name protected outcomes and assets; draw actors, processes, stores,
   data flows, administrative paths, and each trust change.
2. **Challenge:** for each boundary ask how identity can be spoofed, state or
   evidence tampered with, action denied, data disclosed, work amplified, or
   privilege raised. Add domain abuse cases instead of forcing every risk into a mnemonic.
3. **Respond:** eliminate, mitigate, transfer, or explicitly accept the threat.
   Translate mitigation into an enforcement point and a negative test.
4. **Validate:** cite evidence, residual exposure, owner, review date, and the
   observation that would require a different response.

Write abuse cases as `actor + precondition + path + affected property + observable
impact`. “An attacker hacks us” cannot produce a test. “An authenticated Northstar
researcher changes the tenant in an observation URL and receives a private record
owned by another consortium” can.

Risk ranking is a sequencing aid, not arithmetic truth. Record confidence and
uncertainty separately from impact. A low-frequency event that violates a hard
tenant invariant cannot be averaged away by a speculative likelihood score.

## Worked example

Northstar accepts private telescope observations, publishes selected results,
and indexes operating notes for search. The first diagram reveals a boundary
between a consortium researcher and the catalog API, another between the API
and an asynchronous publication worker, and a third between retrieved notes and
an assistant that can propose operator actions.

Threat N-T01 is: an authenticated researcher supplies a different consortium ID
when reading a private observation. The property at risk is confidentiality and
tenant isolation. Northstar responds with identity-bound tenant context at the
request boundary, object-level authorization at the read, tenant-scoped cache
keys, a denial audit event, and a negative integration test. The security owner
accepts residual risk from misconfigured analytical exports until the separate
export path passes the same test; the acceptance expires before external launch.

This is stronger than writing “use RBAC” because it identifies the object,
action, boundaries, evidence, owner, and unfinished risk.

## Common expert mistakes

- **Starting from controls:** a list of MFA, encryption, and firewalls can miss
  the actual business abuse path and misplaced enforcement point.
- **Modeling only diagrams:** a diagram without threats, responses, tests, and
  owners is system documentation, not a threat model.
- **Treating STRIDE as coverage proof:** prompts help discovery; they do not
  guarantee domain abuse, privacy, supply-chain, or economic risks are complete.
- **Collapsing risk into one number:** multiplying invented likelihood and impact
  hides confidence and can demote invariant failures.
- **Accepting risk forever:** an ownerless acceptance with no expiry is an
  undocumented control failure.

## Guided practice

For Northstar's publication path, draw researcher, catalog API, authoritative
store, outbox, worker, public catalog, audit store, and operator. Mark identity,
classification, and authority on each flow. Write one spoofing threat, one
business-logic abuse case, and one privacy lifecycle threat. For each, name a
PEP, negative test, detective evidence, recovery action, owner, and review date.

## Self-check

1. Why is an asset list alone insufficient?
2. What makes an abuse case testable?
3. When can an accepted risk be defensible?
4. Why should confidence be separate from impact?

## Explained answers

1. Assets do not show actors, flows, trust changes, misuse paths, or where a
   decision must be enforced.
2. It names actor, precondition, concrete path, protected property, and observable outcome.
3. When exposure is explicit, an accountable owner approves it, expiry and
   review conditions exist, and evidence can trigger a different decision.
4. A severe risk with weak likelihood data should remain visible; one combined
   score can falsely imply precision and hide uncertainty.

## Sources and next work

- [OWASP Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html)
- [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/)

Complete EX-01 and EX-02, then freeze the Week 49 model before opening the case.
