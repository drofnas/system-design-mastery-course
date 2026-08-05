---
lesson_id: L08
week: 4
estimated_hours: 1.25
---

# Lesson 8: Decisions, RFCs, and Defense

## Outcomes

After this lesson, you can:

- Decide when to use an ADR, RFC, experiment report, or risk entry.
- Write an RFC whose recommendation follows from shared drivers and evidence.
- Lead a review that separates facts, interpretations, preferences, and risks.
- Defend a decision, accept valid criticism, and preserve a revision history.

## Prerequisites

Complete Lessons 1–7, the Week 2 candidate comparison, and the Week 3 failure
review.

## Documents serve decisions

Choose the smallest artifact that preserves the needed reasoning.

| Artifact | Use it when | Core question |
|---|---|---|
| ADR | One consequential decision has been made | Why did we choose this and what follows? |
| RFC | Several stakeholders must review a proposal | Should we adopt this design under these drivers? |
| Experiment report | A claim needs empirical evidence | What did the controlled observation support or falsify? |
| Risk entry | A material unknown remains open | What can go wrong, who owns it, and when must it resolve? |
| Runbook | Operators need repeatable action | How do we detect, mitigate, and recover? |

An RFC can produce several ADRs. An ADR should not become a full system
description.

## ADR lifecycle

Michael Nygard’s original ADR format emphasizes context, decision, status, and
consequences. This course adds evidence and reversal conditions while preserving
the small scope.

Statuses:

- Proposed
- Accepted
- Rejected
- Superseded
- Deprecated

Do not delete a superseded ADR. The old context explains why the system reached
its current state and prevents blind reversal.

## RFC argument

A strong RFC makes one connected argument:

```text
Outcome and current gap
  → workloads, invariants, quality scenarios, constraints
  → prioritized decision drivers
  → credible options evaluated on the same basis
  → recommendation and causal explanation
  → failure, operations, security, cost, and ownership
  → migration, validation, and reversal
```

If the recommendation could be replaced without changing the preceding
sections, the RFC has not shown why it follows.

### Write for adversarial reading

A reviewer should be able to find:

- Which statements are facts, assumptions, calculations, and unknowns
- Which user loses if a claim is wrong
- Which invariant is at risk
- Which option is strongest under a different driver ordering
- Which evidence arrives before commitment
- Which evidence arrives after release
- Who owns unresolved work

## Review disagreement

Technical disagreement usually contains one of five conflicts:

1. Different outcomes
2. Different workload or failure assumptions
3. Different invariant interpretation
4. Different decision-driver priority
5. Different belief about a mechanism

Ask which conflict exists before debating solutions.

### Review protocol

1. Restate the decision and requested feedback.
2. Confirm shared facts and marked assumptions.
3. Review invariants and top quality scenarios.
4. Review driver priority.
5. Challenge each option’s strongest claim.
6. Record risks, questions, and evidence requests.
7. Decide, defer for named evidence, or reject.
8. Publish changes and dissent.

A review is not successful because everyone agrees. It is successful when the
decision, evidence, risk, and ownership are clear.

## Architecture defense

Prepare a 12–15 minute defense:

1. **Two minutes:** user journey, business outcome, and decision requested.
2. **Two minutes:** workload, invariants, quality targets, and constraints.
3. **Three minutes:** candidate designs and strongest trade-offs.
4. **Two minutes:** failure findings, operations, security, cost, and ownership.
5. **Two minutes:** recommendation, validation, migration, and reversal.
6. **Remaining time:** uncertainty and open risks.

The panel then asks questions. Answer in this order:

```text
Clarify the question
→ state the applicable assumption or invariant
→ explain the causal model
→ cite evidence or say it is missing
→ state consequence and follow-up
```

Do not change workload, target, or failure model silently to save the design.
Say, “Under a different assumption the answer changes,” then explain how.

## Worked example: Transit Signal decision

### Decision

Keep alert authoring, approval, version authority, and rider reads in one
deployable application for the pilot. Run notification delivery as an
independently scalable worker that consumes versioned delivery intents and can
reconcile from authoritative history.

### Drivers

- One authority must own the current version.
- Slow channels must not block approval or rider reads.
- One team owns the pilot.
- Backlog must recover within 30 minutes.
- The design must fit the pilot cost and delivery envelope.

### Evidence and uncertainty

- The simple shared-worker candidate has an unsupported resource-interference
  claim.
- The moderate candidate introduces replay and reconciliation work but isolates
  the observed channel failure mode.
- Regional write distribution has no current ownership or latency driver.
- Backlog recovery rate remains an experiment prerequisite.

### Reversal

Reconsider separating rider reads when measured burst load consumes more than
60% of the application’s safe capacity or a separate owning team needs an
independent release boundary. Reconsider regional authority only with residency,
autonomy, or latency evidence that outweighs coordination risk.

### Strong panel question

> You say the worker isolates failure, but both processes use the same
> authoritative state. What shared limit can still couple them?

Strong answer:

> Connection capacity and write contention remain shared. The claim is only
> process and worker isolation, not full resource isolation. Before acceptance,
> the experiment must cap worker connections and verify approval and rider-view
> latency during backlog recovery. If that target fails, separate resource
> pools become a prerequisite without changing state authority.

The answer narrows the claim instead of defending a label.

## Revision discipline

After review:

- Preserve the original attempt as learning evidence.
- Record each material comment and disposition.
- Update the RFC or supersede the decision artifact.
- State what evidence changed the recommendation.
- Keep rejected feedback when it reveals a real trade-off.
- Link revisions to lessons or experiments.

Do not optimize the document for a higher LLM score by adding unsupported
language. Improve the reasoning and evidence.

## Common expert mistakes

### Writing the RFC after the decision is politically final

Review becomes theater. Publish while evidence can still change the choice.

### Hiding the strongest objection

State it better than an opponent would. A decision that survives only weak
objections is not defended.

### Overloading an ADR

One ADR should record one consequential decision. Use links for supporting
models.

### Treating reviewer status as evidence

Authority can resolve accountability. It does not change system behavior.

### Answering unknowns with confidence

“We need to measure that before commitment” is stronger than inventing a causal
claim during defense.

## Guided practice

Complete [EX-12](../exercises/exercises.md#ex-12-defense-and-disagreement).
Then write a short optional decision memo and compare it with the practice
answer key.

## Self-check

1. When should an RFC produce an ADR?
2. Why preserve a superseded decision?
3. What are the five common sources of design disagreement?
4. What should you do when a panel exposes a missing measurement?
5. What makes an RFC recommendation traceable?

## Explained answers

1. When review accepts a consequential decision that should remain visible and
   versioned independently of the proposal.
2. It preserves historical context, forces, and consequences, preventing blind
   acceptance or reversal.
3. Different outcomes, assumptions, invariants, driver priorities, or beliefs
   about mechanisms.
4. State the uncertainty, consequence, evidence needed, owner, and decision
   point. Do not silently change assumptions.
5. The same workloads, invariants, quality scenarios, constraints, and ranked
   drivers are used to evaluate all candidates, and the evidence supports the
   chosen trade-off.

## Sources and next work

- [Michael Nygard, “Documenting Architecture
  Decisions”](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)
- [CMU SEI, Architecture Tradeoff Analysis Method
  collection](https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/)
- Next: complete the guided decision exercises, compare your answers with the
  practice key, and generate a module quiz.

## Solo extension: modern constraints and ownership

The deep path adds **a constraint and assurance ledger covering data classes, tenant boundaries, obligations, AI use, supplier risk, cost allocation, decision rights, evidence owners, uncertainty, and reversal triggers**.

### Repeatable decision procedure

1. Inventory the affected data, tenants, identities, providers, jurisdictions,
   control planes, evidence owners, and cost owners before selecting a mechanism.
2. State the invariant and the authority that may change it. Separate a claimed
   policy from the enforcement point and from the evidence that proves execution.
3. Freeze a prediction, implement or model the named mechanism, and record the
   accepted evidence mode and runtime boundary.
4. Inject one policy, isolation, recovery, or supplier failure in addition to the
   module's mechanism failure. Preserve raw evidence before interpretation.
5. Compare at least two options across product outcome, technical mechanism,
   security and governance, operations and recovery, economics, ownership,
   migration, and reversal triggers.

### Non-capstone extension

Apply the procedure to the module's continuing case. Add one tenant or governed
data class, one supplier or control-plane dependency, and one deletion, recovery,
or exit obligation. The completed case may demonstrate the method, but its
topology, thresholds, policy choices, and answer are not defaults for Global
Commerce.

### Evidence boundary

Use `derived`, `executed_deterministic`, `measured_loopback`,
`measured_container`, `modeled_capacity`, `fixture_replay`, or
`measured_accelerator` exactly as defined by the course. Fixture replay supports
practice and remediation only. Modeled remote scale is not local measurement.
Every trial records commit and input/configuration hashes, runtime and resource
limits, clock, warm-up/repetition policy, raw outcomes, and limitations.

### Source boundary

Use the module's bounded primary sources and preserve the local evidence boundary.
