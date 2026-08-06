# Security, Privacy, and Abuse Resistance Resource Guide

Local lessons are sufficient to complete the module. External sources reinforce
the instruction and provide a checkable primary or practitioner reference; they
never replace the local explanation, practice, or answer key.

## Required authoritative spine

The required records are RES-01, RES-02, RES-03, RES-10, RES-12, RES-14, RES-15.
Every required record is free and has a local written alternative. All other
records below are optional enrichment and do not consume required module time.

| Week | Required resources | Assigned minutes |
|---:|---|---:|
| 70 | RES-03, RES-12, RES-14, RES-15 | 200 |
| 71 | RES-01, RES-02, RES-10 | 205 |

For each assigned source, preserve the requested evidence, one transfer limit,
and one observation that would falsify the claim. A required source that is
temporarily unavailable is replaced by its local alternative and the same evidence
task; record the substitution.

## Resource records

### RES-01: Threat Modeling Cheat Sheet

- **Author/publisher:** OWASP Cheat Sheet Series
- **URL:** https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html
- **Type/status:** maintainer guidance; Required
- **Access:** free
- **Lesson/time:** the relevant lesson; 70 minutes assigned
- **Purpose:** Apply the four-question process to concrete assets, flows, boundaries, threats, and testable responses.
- **Boundary and evidence:** Read Overview through Review and Validation; submit one data-flow boundary, three contextual threats, responses, owners, and validation tests.
- **Local alternative:** [lessons/01-threat-models-abuse-cases.md](lessons/01-threat-models-abuse-cases.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-02: Application Security Verification Standard 5.0.0

- **Author/publisher:** OWASP Foundation
- **URL:** https://owasp.org/www-project-application-security-verification-standard/
- **Type/status:** open verification standard; Required
- **Access:** free
- **Lesson/time:** the relevant lesson; 60 minutes assigned
- **Purpose:** Turn threats into versioned verification requirements rather than generic control labels.
- **Boundary and evidence:** Read What is ASVS and How to Reference Requirements; select and version five requirements that test the Northstar model, explaining exclusions.
- **Local alternative:** [lessons/01-threat-models-abuse-cases.md](lessons/01-threat-models-abuse-cases.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-03: NIST SP 800-63B-4: Authentication and Authenticator Management

- **Author/publisher:** National Institute of Standards and Technology
- **URL:** https://pages.nist.gov/800-63-4/sp800-63b.html
- **Type/status:** standards-body guidance; Required
- **Access:** free
- **Lesson/time:** the relevant lesson; 90 minutes assigned
- **Purpose:** Separate authentication assurance, authenticator lifecycle, recovery, and session continuity.
- **Boundary and evidence:** Read Sections 2, 4, and 5; produce one assurance choice, recovery abuse case, session-binding contract, timeout, and revocation test.
- **Local alternative:** [lessons/02-identity-authentication-sessions.md](lessons/02-identity-authentication-sessions.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-10: NIST Privacy Framework 1.0

- **Author/publisher:** National Institute of Standards and Technology
- **URL:** https://www.nist.gov/privacy-framework/privacy-framework
- **Type/status:** standards-body framework; Required
- **Access:** free
- **Lesson/time:** the relevant lesson; 75 minutes assigned
- **Purpose:** Connect data processing, privacy outcomes, owners, and lifecycle verification without assuming one jurisdiction.
- **Boundary and evidence:** Read the Framework Core Identify-P, Govern-P, Control-P, Communicate-P, and Protect-P outcomes; produce a data-action inventory and deletion exception register.
- **Local alternative:** [lessons/06-audit-privacy-data-lifecycle.md](lessons/06-audit-privacy-data-lifecycle.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-12: LLM Prompt Injection Prevention Cheat Sheet

- **Author/publisher:** OWASP Cheat Sheet Series
- **URL:** https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html
- **Type/status:** maintainer guidance; Required
- **Access:** free
- **Lesson/time:** the relevant lesson; 70 minutes assigned
- **Purpose:** Treat instructions in retrieved content as adversarial data and preserve deterministic authorization.
- **Boundary and evidence:** Read Common Attack Types, Primary Defenses, Agent-Specific Defenses, and Testing; submit one indirect-injection test and deterministic denial trace.
- **Local alternative:** [lessons/08-prompt-injection-tool-authorization-decisions.md](lessons/08-prompt-injection-tool-authorization-decisions.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-04: Authorization Cheat Sheet

- **Author/publisher:** OWASP Cheat Sheet Series
- **URL:** https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html
- **Type/status:** maintainer guidance; Optional enrichment
- **Access:** free
- **Lesson/time:** the relevant lesson; 65 minutes optional
- **Purpose:** Design per-request, per-object, per-action authorization with explicit deny behavior and tests.
- **Boundary and evidence:** Read all Recommendations; submit an allow/deny matrix and four negative regression tests, including policy failure behavior.
- **Local alternative:** [lessons/03-authorization-models-enforcement.md](lessons/03-authorization-models-enforcement.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-05: Multi-Tenant Application Security Cheat Sheet

- **Author/publisher:** OWASP Cheat Sheet Series
- **URL:** https://cheatsheetseries.owasp.org/cheatsheets/Multi_Tenant_Security_Cheat_Sheet.html
- **Type/status:** maintainer guidance; Optional enrichment
- **Access:** free
- **Lesson/time:** the relevant lesson; 70 minutes optional
- **Purpose:** Trace tenant identity through every shared data and execution surface.
- **Boundary and evidence:** Read Key Risks, Best Practices, and Do's and Don'ts; audit API, database, cache, file, queue, search, and administrative paths.
- **Local alternative:** [lessons/04-tenant-isolation-scoped-access.md](lessons/04-tenant-isolation-scoped-access.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-06: Zanzibar: Google's Consistent, Global Authorization System

- **Author/publisher:** Ruoming Pang et al.; USENIX and Google
- **URL:** https://www.usenix.org/conference/atc19/presentation/pang
- **Type/status:** open paper and recorded practitioner presentation; Optional enrichment
- **Access:** free
- **Lesson/time:** the relevant lesson; 90 minutes optional
- **Purpose:** Evaluate relationship authorization, consistency, caching, and centralized policy as operated-system trade-offs.
- **Boundary and evidence:** Watch the presentation or read Sections 1-3 and 5-7 of the paper; record the data model, stale-decision risk, operating cost, and one simpler alternative.
- **Local alternative:** [lessons/03-authorization-models-enforcement.md](lessons/03-authorization-models-enforcement.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-07: Secrets Management Cheat Sheet

- **Author/publisher:** OWASP Cheat Sheet Series
- **URL:** https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html
- **Type/status:** maintainer guidance; Optional enrichment
- **Access:** free
- **Lesson/time:** the relevant lesson; 70 minutes optional
- **Purpose:** Design secret scope, custody, rotation, revocation, auditing, and exposure response.
- **Boundary and evidence:** Read General Secrets Management, CI/CD, Detection, and Incident Response; create one lifecycle and rotation-without-outage experiment.
- **Local alternative:** [lessons/05-secrets-keys-encryption.md](lessons/05-secrets-keys-encryption.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-08: NIST Key Management Guidelines

- **Author/publisher:** National Institute of Standards and Technology
- **URL:** https://csrc.nist.gov/projects/key-management/key-management-guidelines
- **Type/status:** standards-body guidance; Optional enrichment
- **Access:** free
- **Lesson/time:** the relevant lesson; 55 minutes optional
- **Purpose:** Distinguish key material, cryptoperiods, protection, compromise, recovery, and destruction.
- **Boundary and evidence:** Read the SP 800-57 Part 1 Rev. 5 overview and lifecycle guidance; map one key from generation through destruction and name its owner.
- **Local alternative:** [lessons/05-secrets-keys-encryption.md](lessons/05-secrets-keys-encryption.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-09: Logging Cheat Sheet

- **Author/publisher:** OWASP Cheat Sheet Series
- **URL:** https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html
- **Type/status:** maintainer guidance; Optional enrichment
- **Access:** free
- **Lesson/time:** the relevant lesson; 65 minutes optional
- **Purpose:** Make security events attributable and useful without logging secrets or unbounded sensitive data.
- **Boundary and evidence:** Read Event Data Sources through Verification; define an audit event, prohibited fields, tamper signal, logging-failure test, retention, and access rule.
- **Local alternative:** [lessons/06-audit-privacy-data-lifecycle.md](lessons/06-audit-privacy-data-lifecycle.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-11: SLSA Specification 1.2

- **Author/publisher:** OpenSSF SLSA project
- **URL:** https://slsa.dev/spec/v1.2/
- **Type/status:** open supply-chain specification; Optional enrichment
- **Access:** free
- **Lesson/time:** the relevant lesson; 65 minutes optional
- **Purpose:** Separate provenance evidence from trust decisions and verify source/build expectations.
- **Boundary and evidence:** Read About SLSA, Build Track Basics, Provenance, and Verifying Source; define one dependency acceptance policy and negative test.
- **Local alternative:** [lessons/07-supply-chain-abuse-security-response.md](lessons/07-supply-chain-abuse-security-response.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-13: AI Agent Security Cheat Sheet

- **Author/publisher:** OWASP Cheat Sheet Series
- **URL:** https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html
- **Type/status:** maintainer guidance; Optional enrichment
- **Access:** free
- **Lesson/time:** the relevant lesson; 65 minutes optional
- **Purpose:** Bound tool identity, privilege, approvals, memory, budgets, audit, and recovery independently of model behavior.
- **Boundary and evidence:** Read Threat Model, Least Privilege, Tool Authorization, Memory, Observability, and Adversarial Validation; produce a high-risk tool contract and failure matrix.
- **Local alternative:** [lessons/08-prompt-injection-tool-authorization-decisions.md](lessons/08-prompt-injection-tool-authorization-decisions.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

Do not copy articles, chapters, slides, or transcripts into learner artifacts.
Use short attributed quotations only when necessary and otherwise paraphrase with
the source ID, exact section boundary, and stated evidence limit.
