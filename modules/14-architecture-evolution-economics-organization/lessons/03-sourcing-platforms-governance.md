---
lesson_id: L03
title: "Sourcing, Platforms, and Governance"
---

# Sourcing, Platforms, and Governance

## Outcomes

- Compare managed, open-source, custom, and shared-platform choices against the
  same capability contract.
- Expose security, reliability, cost, portability, and exit ownership.
- Define a paved road that reduces repeated work without becoming a mandate or
  central queue.

## Prerequisites

Use Module 12 recovery evidence and Module 13 dependency, credential, tenant,
and supply-chain controls.

## Mechanism: buy operations, not responsibility

A sourcing label hides a bundle of obligations. Define the required capability
first: correctness, throughput, latency, recovery, residency, authorization,
observability, change cadence, support, and exit time. Then compare:

| Dimension | Managed | Open-source operated | Custom | Internal platform |
|---|---|---|---|---|
| Differentiation | Usually low | Medium | Must justify | Shared leverage |
| Control | Contract and configuration | Source plus operations | Full | Platform contract |
| Hidden work | Integration, limits, exit | Upgrades, security, on-call | Everything | Adoption and product ownership |
| Exit evidence | Export, replacement, time | Skills and portable state | Simplification | Alternate path |

Total cost includes procurement, integration, migration, on-call, upgrades,
security response, support delay, and decommissioning. “Open source is free” and
“managed means no operations” both omit material work.

A paved road is an optional, supported path with a measured user outcome. It
publishes contracts, templates, telemetry, support, and an exception process.
Its owner treats internal teams as users, measures adoption and time saved, and
retires unused capability. Governance should set compatibility and safety
constraints, not require central approval for routine compliant changes.

## Worked example

Northstar compares a managed event service, a self-operated broker, custom
database polling, and the observatory platform's event lane. All can move an
accepted-observation fact. The platform lane is selected because it meets the
20× burst, replay, isolation, and audit contract while reusing staffed recovery
and telemetry. The decision still records per-message cost, a quota test,
portable event schemas, an export procedure, a database-polling fallback, and a
90-day replacement estimate.

## Common expert mistakes

- **Starting with a vendor feature table.** It obscures the outcome and makes
  alternatives incomparable.
- **Ignoring exit until renewal.** Portability requires versioned data,
  replacement capacity, credentials, and practiced procedures.
- **Building platforms by decree.** Forced adoption can hide support queues and
  shift rather than reduce cognitive load.
- **Governance without expiry.** Temporary migration controls become permanent
  delivery friction unless their removal criteria are explicit.

## Guided practice

Create a sourcing matrix for Northstar with one disqualifying condition, one
exit experiment, and one accountable owner per option.

## Self-check

1. Which responsibility cannot be outsourced?
2. What makes an exit plan executable?
3. How does a paved road differ from a standard?
4. When is custom build justified?

## Explained answers

1. Accountability for user outcomes, risk acceptance, data, access, recovery,
   cost, and supplier response remains with the organization.
2. Portable contracts and data, a target or fallback, credentials, capacity,
   measured duration, owners, and a practiced transition.
3. A standard constrains behavior; a paved road supplies an easier supported
   implementation. Both need exceptions and owners.
4. When the capability is strategically differentiating or alternatives fail a
   material requirement, and the full lifecycle can be staffed and funded.

## Sources and next work

Use RES-04's outcome and ownership method with EX-05 and EX-06. Treat provider
examples as evidence, not as required technology.
