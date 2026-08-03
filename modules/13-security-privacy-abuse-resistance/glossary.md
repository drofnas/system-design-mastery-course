# Module 13 Glossary

- **Abuse case:** an actor, precondition, action path, and impact describing
  unintended or malicious use of a real feature.
- **Authentication:** evidence that a subject controls an identity or
  authenticator; it does not grant access by itself.
- **Authorization:** a decision about whether a subject may perform an action on
  a particular object in a stated context.
- **Policy decision point (PDP):** the component that evaluates an authorization
  policy. It is distinct from the enforcement point that blocks or permits work.
- **Policy enforcement point (PEP):** the boundary that must obtain and enforce
  a complete authorization decision before an effect or disclosure.
- **RBAC / ABAC / ReBAC:** authorization based primarily on roles, attributes,
  or relationships. Real policies may combine them.
- **Tenant context:** the trusted tenant identity bound to a subject and carried
  through data and execution paths; an attacker-supplied tenant ID is input.
- **Break glass:** exceptional, time-limited privileged access with approval,
  scope, attribution, monitoring, expiry, and post-use review.
- **Authenticator:** something a claimant controls to prove an identity.
- **Session binding:** evidence that continuing requests belong to a prior
  authentication event and remain within its assurance and lifetime.
- **Secret:** confidential credential material such as a token, password, or
  private key. A resource identifier is not a secret.
- **Cryptoperiod:** the approved time or usage interval for a key.
- **Envelope encryption:** encrypting data with a data key and protecting that
  key with separately managed key-encryption material.
- **Tamper evident:** able to detect unauthorized modification or deletion; it
  does not imply that tampering is impossible.
- **Data action:** collection, generation, use, sharing, retention, deletion, or
  another operation on data across its lifecycle.
- **Provenance:** verifiable information about where an artifact came from and
  how it was produced. Provenance must still be checked against policy.
- **Economic abuse:** permitted-looking requests used to consume unfair or
  unaffordable resources, money, quotas, or human attention.
- **Prompt injection:** adversarial instructions in user or retrieved content
  that attempt to change model behavior or cross an authority boundary.
- **Residual risk:** exposure remaining after controls, with an accountable
  owner, expiry/review date, and reversal evidence.
