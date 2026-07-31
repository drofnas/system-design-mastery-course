# Module 1 Glossary

These definitions apply within Module 1. Later modules refine several terms.

## Architecture

The consequential decisions and structures that shape a system’s behavior,
qualities, evolution, and ownership. A diagram is a view of architecture, not
the architecture itself.

## Architectural decision

A choice whose consequences materially affect system structure, quality
attributes, interfaces, dependencies, ownership, cost, or ability to change.

## Architecture Decision Record (ADR)

A small versioned record of one architecturally significant decision, its
context, considered options, consequences, and status.

## Assumption

A claim treated as true for planning but not yet established as fact. A useful
assumption names its consequence if false and the evidence that will test it.

## Constraint

A boundary the design must respect and cannot choose away within the current
decision, such as a regulation, deadline, existing contract, or staffing limit.

## Decision driver

A prioritized fact, outcome, quality scenario, constraint, cost, or risk that
distinguishes one option from another.

## Derived state

State computed or copied from authoritative state. It may be rebuilt or repaired
under stated rules.

## Evidence threshold

The observation or measurement strong enough to support, reject, or reverse a
claim or decision.

## Failure model

The explicit set of faults, combinations, timing assumptions, and exclusions
under which a system’s safety, liveness, degradation, and recovery claims are
evaluated.

## Functional requirement

A capability or behavior the system must provide. It says what the system does,
not how well it must do it.

## Invariant

A proposition that must remain true across every allowed state transition and
covered failure. It is testable as true or false.

## Liveness

The property that some desired progress eventually occurs, subject to stated
assumptions. “Accepted alerts eventually reach an eligible delivery attempt” is
a liveness claim.

## Non-goal

Work or behavior intentionally excluded from the current scope. A non-goal
prevents accidental expansion; it is not an excuse to ignore a required risk.

## Quality attribute

A dimension of system behavior such as performance, availability, security,
modifiability, usability, or recoverability. The name alone is too vague to
drive a design.

## Quality-attribute scenario

A system-specific statement naming the stimulus source, stimulus, environment,
affected artifact, required response, and measurable response threshold.

## Request for Comments (RFC)

A reviewable proposal that frames a problem, compares options, recommends a
design, and records evidence, risks, operations, migration, and unresolved
questions.

## Reversal condition

New evidence or changed context that should trigger reconsideration of a
decision.

## Safety

The property that a forbidden event never occurs within the stated model.
“One alert approval cannot publish two authoritative alert versions” is a
safety claim.

## Service-level indicator (SLI)

A quantitative measure of a service outcome, usually expressed as a ratio,
distribution, or rate.

## Service-level objective (SLO)

A target value or range for an SLI over a defined time window.

## State owner

The responsibility with authority to accept transitions for a business fact.
Storage location alone does not establish ownership.

## Stimulus

An event that reaches the system or a part of it, such as a request, fault,
change, load burst, or malicious action.

## System context

The system as one boundary, its users and external systems, and the meaningful
relationships between them.

## Trust boundary

A place where identity, authority, data handling, or assumptions change and
must be validated rather than inherited.

## Unknown outcome

A result where the caller cannot determine whether an operation failed, was
accepted, or completed. A timeout does not prove that no side effect occurred.
