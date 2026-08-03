# Module 13 Anchored Rubric

## R01: Threat modeling and abuse cases

- **0:** protected assets or critical trust boundaries are missing, or a known hard threat has no response.
- **1:** attack labels without actors, paths, properties, impacts, tests, or owners.
- **2:** useful model with material administrative, recovery, privacy, or residual-risk gaps.
- **3:** assets, actors, flows, boundaries, abuse cases, treatments, PEPs, tests, owners, and reversals align.
- **4:** cross-team adversarial review and new evidence update the model without erasing prior decisions.

## R02: Identity, authentication, recovery, and sessions

Safety-critical because stale, replayed, or weakly recovered identity can bypass every later control.

- **0:** repaired evidence accepts an expired/revoked credential or recovery bypasses the required assurance.
- **1:** authentication labels without lifecycle, binding, expiry, revocation, recovery, or negative tests.
- **2:** ordinary login works but replacement, propagation, federation, or sensitive reauthentication is weak.
- **3:** assurance, authenticators, sessions, recovery, revocation, propagation, audit, and replay tests agree.
- **4:** compromise and role-change variants validate timing, containment, and user/operational consequences.

## R03: Object/action authorization

Safety-critical because a missing or stale decision can disclose data or cause an irreversible effect.

- **0:** a repaired unauthorized object/action succeeds or the PEP fails open.
- **1:** roles or permissions listed without object, action, context, policy identity, or denial evidence.
- **2:** main paths work but delayed effects, cache freshness, policy failure, or negative coverage is weak.
- **3:** model choice, allow/deny matrix, authoritative inputs, PEPs, freshness, traces, and tests agree.
- **4:** policy-change races and alternate-stack tests validate consistency and migration thresholds.

## R04: Tenant isolation and scoped access

Safety-critical because one cross-tenant disclosure or mutation violates the course invariant.

- **0:** repaired evidence returns or mutates another tenant's protected object.
- **1:** tenant filter claims without trusted context, surfaces, denial, audit, or tests.
- **2:** API/database isolation works but cache, file, message, search, admin, restore, or break glass is weak.
- **3:** all seven surfaces bind tenant authority, deny safely, record evidence, repair, and pass negative tests.
- **4:** isolation tiers and operator-error variants validate blast radius, cost, migration, and reversal conditions.

## R05: Secrets, keys, certificates, and encryption

Safety-critical because over-scoped or still-valid exposed authority expands compromise.

- **0:** repaired evidence accepts an exposed version, logs secret material, or invents unsafe cryptography.
- **1:** storage labels without scope, issuance, plaintext exposure, rotation, revocation, recovery, or owner.
- **2:** lifecycle exists but overlap, consumer rollout, old-version rejection, key custody, or rollback is weak.
- **3:** scope, custody, cryptoperiod, rotation, revocation, recovery, destruction, audit, and tests agree.
- **4:** compromise and no-outage variants validate containment and teach encryption's explicit limits.

## R06: Audit, detection, and security response

- **0:** evidence is altered, secrets are logged, or a material security event is unattributable.
- **1:** event names without actor, object/action, outcome, policy, integrity, access, or response.
- **2:** useful events with weak minimization, logging failure, tamper detection, correlation, or ownership.
- **3:** event schema, prohibited fields, source confidence, tamper signal, access, retention, alerts, and response align.
- **4:** failed-source, clock, storage, and privileged-tamper variants validate investigation and recovery.

## R07: Privacy and data lifecycle

Safety-critical because false deletion or restore resurrection can expose protected data while reporting success.

- **0:** repaired evidence leaves an active copy or restore silently resurrects deleted protected data.
- **1:** classification or retention labels without purpose, copy inventory, exception, verification, or owner.
- **2:** primary deletion works but derived copies, backups, restore, minimization, or residency decisions are weak.
- **3:** classes, purposes, copies, access, retention, deletion, exceptions, restore replay, queries, and owners agree.
- **4:** repeated delete/restore and policy-change variants validate exposure bounds and reversal evidence.

## R08: Dependency, supply-chain, economic-abuse, and response controls

- **0:** a mismatched artifact is accepted or abusive work remains unbounded after repair.
- **1:** SBOM/rate-limit labels without expectations, verification, work units, scopes, denial, or response.
- **2:** one control works but transitive inputs, builder trust, tenant fairness, cost, quarantine, or recovery is weak.
- **3:** dependency policy/provenance and subject/tenant/global budgets produce bounded decisions, evidence, and recovery.
- **4:** alternate builder, coordinated abuse, and rollback variants validate trust and cost thresholds.

## R09: Prompt injection and tool authorization

Safety-critical because model-controlled authority can turn untrusted text into an irreversible action.

- **0:** retrieved content grants authority or a repaired unauthorized high-risk tool produces an effect.
- **1:** prompt filters without trust labels, external authorization, approval, scope, idempotency, budget, or audit.
- **2:** main attack is denied but indirect content, stale approval, duplicate effects, or recovery is weak.
- **3:** intent, trust, schema, arguments, tenant, authorization, approval, credentials, idempotency, budgets, and audit agree.
- **4:** adaptive and cross-provider tests validate capability limits and a safer no-tool alternative.

## R10: Security architecture, ownership, and teach-back

- **0:** ownerless critical risk, unsafe migration, false compliance claim, or defense cannot explain a safety property.
- **1:** preferred controls without shared drivers, alternatives, evidence, or owners.
- **2:** decision exists but cost, privacy, operations, migration, dissent, residual risk, or reversal is weak.
- **3:** threat model, verification, RFC, defense, alternatives, owners, costs, dissent, remediation, and reversals align.
- **4:** cross-team review resolves disagreement and transfers the reasoning to another stack or domain.

## Result thresholds

- **Pass:** every gate passes, average at least 3.0, and R02/R03/R04/R05/R07/R09 are nonzero.
- **Revise:** no hard/safety failure, but average is below 3.0 or material evidence gaps remain.
- **Repeat:** G02-G05 fails or a safety-critical criterion is zero.
