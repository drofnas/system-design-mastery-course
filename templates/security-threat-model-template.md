# Security Threat Model

Use this artifact to connect product behavior to testable security and privacy
requirements. Replace every prompt. A list of generic attacks is not a threat
model.

## Submission identity

- System and version:
- Author and reviewers:
- Created at:
- Evidence commit:
- AI assistance and verification:

## Scope and protected outcomes

Name the user and business outcomes that security controls protect. State
explicit non-goals, excluded environments, and the authority that accepts each
exclusion.

## Assets and data classification

| Asset or data class | Security or privacy property | Owner | Retention/residency | Loss or misuse consequence |
|---|---|---|---|---|
| | | | | |

## Actors, identities, and capabilities

| Actor | Proven identity | Allowed capabilities | Forbidden capabilities | Credential/session lifecycle |
|---|---|---|---|---|
| | | | | |

## System and trust boundaries

Draw data flows, stores, processes, external actors, administrative paths, and
every point where trust or authority changes. Label data classification and the
identity propagated across each boundary.

```mermaid
flowchart LR
    A["<actor>"] -->|"<identity, data, action>"| B["<trust boundary>"]
```

## Security and privacy invariants

| ID | Invariant | Violating event | Preventive control | Detective evidence | Recovery action |
|---|---|---|---|---|---|
| SEC-01 | | | | | |

## Threat and abuse-case register

| ID | Actor and precondition | Abuse path | Asset/property at risk | Observable impact | Response | Owner |
|---|---|---|---|---|---|---|
| T-01 | | | | | Mitigate / eliminate / transfer / accept | |

For accepted and transferred risks, name the accountable person, review date,
expiry condition, and evidence that would reverse the decision.

## Authorization matrix

Record decisions for specific subjects, objects, relationships, actions, and
contexts. Include deny cases, administrative access, break-glass access, and
policy-change consistency.

| Subject/context | Object | Action | Decision | Enforcement point | Test |
|---|---|---|---|---|---|
| | | | Allow / deny | | |

## Tenant and data-lifecycle controls

Trace tenant context and classified data through authoritative storage, caches,
files, messages, search or retrieval indexes, logs, exports, and backups. State
how deletion, retention, legal holds, and residency are verified rather than
assumed.

## Credentials, keys, and dependencies

| Item | Scope | Issuance/provenance | Storage | Rotation/revocation | Failure and recovery evidence |
|---|---|---|---|---|---|
| | | | | | |

## Audit, detection, and response

Define attributable security events, sensitive fields that must not be logged,
tamper detection, access controls, retention, alerts, response ownership, and
how logging failure is detected.

## Adversarial validation

| Experiment | Frozen prediction | Raw evidence | Invariant result | Discriminating rerun |
|---|---|---|---|---|
| | | | | |

## Residual risk, cost, and ownership

| Residual risk | Exposure | Current owner | Operating cost | Review/reversal condition |
|---|---|---|---|---|
| | | | | |

## Review and revisions

Preserve the submitted model. Put corrections, reviewer dissent, and changed
decisions in dated addenda with citations to new evidence.

