---
lesson_id: L05
title: "Incident Command, Communication, and Runbooks"
---

# Incident Command, Communication, and Runbooks

## Outcomes

- Separate incident command, operations, communications, and liaison roles.
- Choose mitigation before full diagnosis when user impact demands it.
- Write executable runbooks, handoffs, escalation, and stop conditions.

## Prerequisites

Lessons 1–4 and an authorized controlled-incident environment.

## Response procedure

Declare an incident from measured user impact or credible imminent safety/data
risk. The incident commander owns priorities and incident state, not every
technical action. The operations lead serializes mitigations and records their
results. The communications lead maintains accurate user and stakeholder
updates. A liaison connects dependent teams. One person may fill several roles
in a small incident, but the responsibilities remain explicit.

The first loop is: establish impact, protect people/data/invariants, choose the
safest high-leverage mitigation, execute one coordinated change, observe the
declared signal, and communicate. Diagnosis continues in parallel without
blocking obvious reversible mitigation.

A runbook states triggers, prerequisites, required access, exact actions,
expected observations, abort criteria, escalation, rollback, and owner. A
handoff transfers roles, current impact, hypotheses, eliminated causes, actions,
results, risky state, pending approvals, and next update time.

## Worked example

Northstar pages on active journey burn. The commander prioritizes validated
publication and priority reads. Operations disables optional enrichment and
sheds exports. Communications posts scope and a 20-minute next update. The
registry liaison confirms authority remains intact. Only after impact falls
does the team isolate the dependency regression.

## Common expert mistakes

- **Best debugger commands:** coordination and impact become ownerless.
- **Parallel freelancing:** multiple changes destroy causal evidence and safety.
- **Wait for root cause:** reversible mitigation is delayed while users suffer.
- **Communicate certainty:** unsupported ETAs destroy trust.
- **Write command-only runbooks:** access, validation, abort, and ownership fail.

## Guided practice

Run a tabletop for an archive search with rising latency and an uncertain index
fault. Assign roles, write the first three decisions, draft two updates, perform
a handoff, and state when the incident is mitigated versus resolved.

## Self-check

1. Who decides incident priorities?
2. When should mitigation precede diagnosis?
3. What makes a handoff complete?

## Explained answers

1. The incident commander, informed by user, data, security, and operations leads.
2. When current or imminent impact is material and a safe, reversible action can
   reduce it without needing the full causal model.
3. Explicit role transfer plus impact, actions/results, hypotheses, risky state,
   approvals, pending work, and the next communication checkpoint.

## Sources and next work

Study RES-04 and RES-08, complete EX-10–EX-11, and preserve the incident timeline
as raw evidence for the postmortem rather than rewriting it afterward.
