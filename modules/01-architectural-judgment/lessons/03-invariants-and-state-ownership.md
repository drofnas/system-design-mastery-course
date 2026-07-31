---
lesson_id: L03
week: 1
estimated_hours: 0.75
---

# Lesson 3: Invariants and State Ownership

## Outcomes

After this lesson, you can:

- Distinguish an invariant from a goal, process, or quality target.
- Write business, data, security, and operational invariants that are testable.
- Identify the authority for each business fact and classify derived copies.
- Trace an invariant through state transitions, retries, caches, messages, and
  human operations.

## Prerequisites

Complete [Lessons 1 and 2](01-architectural-judgment.md). Familiarity with
transactions and HTTP is useful but not required.

## Invariants define forbidden states

An invariant is a proposition that must remain true across every allowed state
transition and every failure covered by the design.

Good invariant:

> At most one alert version is current for a transit route and effective time
> interval.

Weak statement:

> Alerts should be consistent.

The good statement is falsifiable. A reviewer can ask which operation changes
current status, where concurrency is controlled, and how a retry behaves.

### Invariant grammar

Useful forms include:

```text
For every [entity], [property] is always true.
No [actor] can [forbidden action] without [required authority].
At most one [irreversible effect] exists for [idempotency identity].
Every [accepted transition] follows [state machine].
If [fact is acknowledged], then [durability or audit property] holds.
```

Avoid “eventually” in a safety invariant. Eventual progress is a liveness
property and needs a time or fairness assumption.

## Four invariant families

### Business invariants

Protect the domain’s meaning.

- A revoked alert cannot be presented as currently approved.
- An alert transition follows Draft → Approved → Revoked or Expired.

### Data invariants

Protect representation and history.

- Every published alert references an immutable content version.
- An audit record retains the actor, decision, prior version, and timestamp.

### Security invariants

Protect authority and isolation.

- A regional operator cannot approve an alert outside their assigned region.
- A public rider cannot mutate alert state.

### Operational invariants

Protect recoverability and controllability.

- Restoring authoritative alert data never makes a superseded version current.
- A replay cannot publish the same version twice as distinct authoritative
  changes.

The category is less important than completeness. Classification helps reveal
gaps.

## State transitions are where invariants fail

List commands, transitions, and failure boundaries:

```text
Draft created
  → content edited
  → approval requested
  → approved
  → publication attempted
  → delivery copied
  → alert updated or revoked
  → copies expire
```

For each arrow ask:

- Who is authorized?
- What prior state is required?
- What makes a repeat safe?
- What is committed atomically?
- What if acknowledgment is lost?
- Which derived copies can be stale?
- How is incorrect derived state repaired?
- Which human operation bypasses normal flow?

This is architectural reasoning before a storage product is chosen.

## Authority is not the same as storage

The state owner is the responsibility that may accept a transition for a
business fact. A database stores representation. A team operates components.
These can be related without being identical.

Use an ownership record:

| Business fact | Authoritative owner | Allowed writers | Derived readers | Repair rule |
|---|---|---|---|---|
| Current alert version | Alert approval responsibility | Authorized operator workflow | Rider views, notification channels | Rebuild from version history |

If two responsibilities can independently declare the same fact, conflict rules
are part of the domain. “Both databases are authoritative” does not resolve it.

### Derived state

A cache, search index, notification record, report, or analytics table is often
derived. State is safely derived when the design states:

- Source version or ordering identity
- Maximum tolerated staleness
- Idempotent rebuild or repair
- Behavior when the source is unavailable
- Deletion and revocation propagation

Calling something “eventually consistent” does not answer these questions.

## Trust boundaries

A trust boundary is where identity, authority, data sensitivity, or assumptions
change. Name it even in a vendor-neutral context diagram.

Examples:

- Public client to transit platform
- Regional operator to approval workflow
- Transit authority to third-party notification channel
- Administrative recovery tool to authoritative state

At each boundary ask who authenticates, who authorizes the object and action,
what input is validated, what is logged, and what credential scope crosses.

## Proof obligations

You do not need a formal proof in Module 1. You do need a proof sketch:

1. State the invariant.
2. Enumerate operations that can affect it.
3. State the precondition and postcondition for each.
4. Include duplicate, concurrent, delayed, and partially acknowledged attempts.
5. Name the enforcement mechanism abstractly.
6. Name the observation that would reveal a violation.

Example:

> INV-T3: No revoked alert is current. Only Approve, Revoke, and Expire change
> current status. Revoke requires the current version and creates a later
> version whose status is Revoked. Rider views select the highest effective
> authoritative version. Derived channels carry the source version; a
> reconciliation job detects any channel presenting a lower current version.

This sketch still has questions, but it exposes them.

## Worked example: Transit Signal

### Invariant

> One approval command cannot create two distinct authoritative approved
> versions.

### Threatening events

- Operator double-clicks Approve.
- Client times out after acceptance and retries.
- Two operator sessions approve the same draft concurrently.
- Recovery replays an accepted command.

### Abstract enforcement

- The approval command carries a stable request identity.
- The transition requires the expected draft version.
- The authoritative owner stores the request identity and resulting version as
  one correctness unit.
- A repeat returns the original result.

### Observable proof

For any request identity, query the version history and show at most one
approved version. During a test, repeat and race the same command, lose the
response, then replay recovery input.

The lesson is not “use technology X.” It is that the invariant determines what
the chosen mechanism must prove.

## Common expert mistakes

### Writing aspirations as invariants

“Data is accurate” and “the system is secure” cannot be evaluated without a
specific forbidden state.

### Naming only database constraints

Constraints are useful, but invariants also cross messages, external side
effects, authorization, recovery, and operator tools.

### Treating a cache as harmless

A stale public copy can violate revocation, privacy, pricing, or safety even if
the authoritative store is correct.

### Ignoring unknown outcomes

A timeout does not mean no transition occurred. If repeating the command can
duplicate an effect, the design has not preserved the invariant.

### Assigning team ownership without state authority

“Team A owns the service” does not say which responsibility may change the
business fact or how other teams request that change.

## Guided practice

Complete:

- [EX-04](../exercises/exercises.md#ex-04-invariant-or-not)
- [EX-05](../exercises/exercises.md#ex-05-state-authority-and-proof-sketch)

For EX-05, include a duplicate and a concurrent transition.

## Self-check

1. What is the difference between an invariant and an SLO?
2. Why must every invariant name or imply the operations that threaten it?
3. Can a derived copy violate an invariant when authoritative state is correct?
4. Why is “the database owns orders” incomplete?
5. What does a proof sketch add to an invariant list?

## Explained answers

1. An invariant forbids a state and must always hold under the covered model. An
   SLO permits a bounded amount of failure over a defined window.
2. Preservation is evaluated at transitions. Without threatening operations,
   the statement cannot influence interfaces, concurrency, recovery, or tests.
3. Yes. Users and dependencies act on copies. A stale revoked alert or deleted
   private record can cause a real violation outside the source.
4. It names storage, not the responsibility authorized to accept domain
   transitions, the allowed writers, or repair behavior.
5. It connects the proposition to operations, concurrency, duplicates,
   enforcement, and observable evidence, exposing missing reasoning.

## Sources and next work

- Capstone invariant requirements:
  [`00_COURSE_SYLLABUS.md`](../../../00_COURSE_SYLLABUS.md)
- Security depth appears in Module 13; transaction enforcement appears in
  Module 8.
- Next: [Lesson 4](04-quality-attribute-scenarios.md)
