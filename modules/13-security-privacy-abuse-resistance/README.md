# Module 13: Security, Privacy, and Abuse Resistance

> **Authoring status:** Review. PESD 2.0 content and machine-readable contracts are migrated. Refreshed evaluator calibration, full platform matrices, offline reruns, cleanup checks, and timed learner pilots remain required before Ready.

## What this module changes

Security is not a checklist attached after architecture. It is a set of
testable properties about who may act, which data may move or persist, which
inputs are trusted, how misuse is detected, and how control failure is repaired.
This module turns threats into enforcement points, negative tests, operating
evidence, owners, and explicit residual risk.

The continuing non-capstone case is **Northstar Observatory Security and Data
Governance**. It extends the observatory registry, publication workflow, and
recovery model from Modules 8-12 with research tenants, private observations,
operator access, retained data, dependencies, and retrieved operating notes. It
contains no merchants, inventory, checkout, payments, orders, or capstone
architecture. Freeze independent commerce decisions before opening the case or
answer key.

## Prerequisites

- Modules 1-12, especially invariants, sessions, transaction recovery,
  consistency, workflows, reconciliation, incidents, and disaster recovery
- Python 3.11 or newer; the reference lab uses only the standard library
- Preserved Week 1 baseline, Week 68 Gate 4 freeze, and Week 69 delta; neither may be edited
- Comfort reading policy decisions, audit records, dependency provenance, and JSON

## Learning outcomes

By the end of the module, you can:

1. Build and maintain a threat model grounded in assets, actors, data flows,
   trust boundaries, abuse cases, owners, tests, and reversal evidence.
2. Design authentication, recovery, session binding, expiry, revocation, and
   replay controls against a stated assurance need.
3. Select role, attribute, or relationship authorization and enforce a
   deny-by-default decision for every object and action.
4. Preserve tenant context and least privilege across every shared data and
   execution surface, including administrative and break-glass paths.
5. Operate secret, certificate, and key lifecycles without creating custom
   cryptography or untestable rotation claims.
6. Build attributable, tamper-detectable audit evidence and verify data
   classification, minimization, retention, deletion, residency, and backups.
7. Bound dependency, supply-chain, economic-abuse, prompt-injection, and tool
   risk with deterministic controls and response ownership.
8. Diagnose nine adversarial failures and defend a security architecture with
   residual risks, costs, migration, owners, and reversal conditions.

## Schedule

The 10–12 hour weekly figure is a capacity envelope. Core work is deliberately
budgeted below that ceiling; unused time is recovery buffer, not hidden work.

### Week 70: Model and derive — 8.5 hours

| Work | Time |
|---|---:|
| Bounded authoritative resources | 200 min |
| Local mechanism instruction | 120 min |
| Guided practice | 60 min |
| Required evidence components | 30 min |
| Model and derive core work | 100 min |

### Week 71: Guided build and prediction freeze — 9 hours

| Work | Time |
|---|---:|
| Bounded authoritative resources | 205 min |
| Local mechanism instruction | 120 min |
| Guided practice | 60 min |
| Required evidence components | 90 min |
| Guided build and prediction freeze core work | 65 min |

### Week 72: Independent build and integration — 10 hours

| Work | Time |
|---|---:|
| Independent build and integration core work | 540 min |
| Independent build and integration verification checkpoint | 60 min |

### Week 73: Break, repair, measure, and diagnose — 10 hours

| Work | Time |
|---|---:|
| Required evidence components | 60 min |
| Break, repair, measure, and diagnose core work | 540 min |

### Week 74: Decide, teach, assess, and freeze — 9.5 hours

| Work | Time |
|---|---:|
| Required evidence components | 120 min |
| Decide, teach, assess, and freeze core work | 390 min |
| Module teach-back | 30 min |
| Learning log and freeze check | 30 min |
## Learn

1. [Threat models, trust boundaries, and abuse cases](lessons/01-threat-models-abuse-cases.md)
2. [Identity, authentication, recovery, and sessions](lessons/02-identity-authentication-sessions.md)
3. [Authorization models and enforcement](lessons/03-authorization-models-enforcement.md)
4. [Tenant isolation and scoped access](lessons/04-tenant-isolation-scoped-access.md)
5. [Secrets, keys, certificates, and encryption](lessons/05-secrets-keys-encryption.md)
6. [Audit, privacy, and data lifecycles](lessons/06-audit-privacy-data-lifecycle.md)
7. [Supply chains, economic abuse, and security response](lessons/07-supply-chain-abuse-security-response.md)
8. [Prompt injection, tool authorization, and security decisions](lessons/08-prompt-injection-tool-authorization-decisions.md)

Use the [glossary](glossary.md) only after studying the mechanisms.

## Practice and independent evidence

- Freeze the commerce security baseline before studying the completed
  [Northstar case](case-study/northstar-security-data-governance.md).
- Complete the [guided exercises](exercises/exercises.md) before opening the
  [explained answers](exercises/answer-key.md).
- Run the [security lab](lab/README.md), preserve scenario and raw-output
  hashes, then reproduce the observable controls in the chosen stack or a safe
  operated environment.
- Preserve denied decisions, failed trials, and uncertainty. Corrections belong
  in dated addenda; never rewrite the frozen baseline or raw evidence.
- Do not copy Northstar actors, tenant model, policy, thresholds, credentials,
  retention schedule, dependency policy, or tool boundary into the capstone.

This module contributes one major security threat model, one substantial
security architecture RFC, one failure matrix, one security investigation, and
one recorded teach-back.

## Assessment and completion

- Read the [assessment contract](assessment/README.md),
  [anchored rubric](assessment/rubric.md),
  [evaluator prompt](assessment/evaluator-prompt.md), and
  [remediation map](assessment/remediation-map.md) before independent work.
- Pass G01-G06, average at least 3.0, and avoid a zero in R02, R03, R04,
  R05, R07, or R09.
- Gate 5 runs in Week 85. Module 13 evidence feeds that later assessment;
  Week 52 does not create or edit a capstone gate revision.

## Evidence boundary and AI use

The deterministic model exposes policy inputs, decisions, hashes, and control
invariants. It does not prove production isolation, cryptographic strength,
physical deletion, real dependency provenance, regulatory compliance, or
resistance to adaptive attackers.

AI may challenge threat coverage, tests, evidence, and alternatives. It may not
choose the graded architecture, invent attack evidence, modify frozen artifacts,
write replacement graded answers, or answer during the defense. Retrieved
instructions remain untrusted data regardless of their author or wording.

## Course-wide completion contracts

- The machine-readable `module.json` time blocks are the canonical required-work budget.
- The [factual-claims ledger](assessment/factual-claims.json) maps each local lesson to its authoritative source boundary.
- Use the [provider-neutral evaluation workflow](../../EVALUATION_GUIDE.md) only after learner evidence is committed.
- Use the [sealed local gate workflow](../../SOLO_GATE_GUIDE.md) when a course gate applies. Human review is optional.

A frozen self-evaluation may establish **Solo Complete**; independent human or LLM review may establish **Independently Validated**. Synthetic lab values are not production measurements.

## PESD 2.0 scope addition

This 5-week module schedules 47 core hours. Its primary
decision is RFC A07. The added graded scope is
obligation-to-control-to-evidence mapping, privacy impact reasoning, secure SDLC, source-to-deployment identity, cryptographic inventory, crypto agility, and post-quantum migration planning. See Lesson 8, the final guided exercise, final worksheet,
rubric anchors, and remediation map for the integrated evidence contract.
