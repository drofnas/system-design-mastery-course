lesson_id: L08

# Technical Strategy and Teach-Back

## Outcomes

- Turn architecture direction into evidence-gated increments.
- Align product, technical, economic, security, and staffing assumptions.
- Defend disagreement and stopping conditions without asserting authority.

## Prerequisites

Bring your saved starting point, cost model, migration evidence, failure
matrix, and optional feedback from an engineer outside the chosen stack.

## Decision procedure

A strategy explains why a sequence of technical investments should change a
product or organizational outcome. Use this order:

1. State the outcome, present constraint, baseline, and planning horizon.
2. Compare credible alternatives against shared drivers.
3. Select the smallest reversible increment that produces new evidence.
4. Name dependencies, staffing, owners, compatibility, and transition cost.
5. Define promotion, stop, reversal, and decommission conditions.
6. Set a review cadence and preserve dissent and uncertainty.

A target architecture diagram without sequencing is a preference. A roadmap of
components without evidence gates is a delivery schedule. A strategy connects
increments through a causal model: “If we introduce this seam, then this team
can change this capability independently; we will observe that through these
flow and reliability measures.”

The defense tests whether the reasoning transfers. Use the module's frozen
solo-review questions to challenge authority, mixed versions, rollback, cost
allocation, staffing loss, security, and the no-migration alternative. Record
what would change the plan. An optional human panel may add adaptive questions. Teach-back
is successful when another engineer can apply the decision procedure to a
different stack, not when they repeat Northstar's answer.

## Worked example

Northstar's sequence is:

1. Instrument change coordination and catalog unit cost; stop if no material
   outcome constraint exists.
2. Modularize the projector and publish a versioned internal fact; this remains
   valuable even if extraction stops.
3. Backfill and shadow an independently owned projection; stop on mismatch,
   unsafe rollback, cost, or missing secondary ownership.
4. Cut over bounded traffic, observe, contract compatibility, and decommission
   transition assets.

The research-access lead prefers immediate extraction. The registry lead prefers
remaining modular. The memo resolves the disagreement with a modular seam first,
then makes deployment extraction conditional on measured coordination delay and
the ownership exercise. Neither role gets a veto by title alone.

## Common expert mistakes

- **Treating the target as inevitable.** New evidence must be allowed to stop or
  redirect later increments.
- **Hiding staffing in an appendix.** Architecture that nobody can operate is
  not a target state.
- **Using governance as approval theater.** Decision rights and exceptions
  should reduce repeated negotiation.
- **Performing a scripted defense.** Follow-up questions must test uncertainty,
  not invite memorized terminology.

## Guided practice

Write a four-increment Northstar strategy. For each increment, state the user or
team outcome, dependency, owner, evidence gate, and stop condition. Select one
assumption through the deterministic solo-review packet, replace it, and revise
only the affected increments. An optional peer may supply the replacement after
the original is frozen.

## Self-check

1. What distinguishes strategy from target architecture?
2. Why begin with a reversible seam?
3. What should a dissent record contain?
4. How does teach-back demonstrate mastery?

## Explained answers

1. Strategy connects outcomes to sequenced investments, capacity, evidence,
   decisions, and reversals across time.
2. It improves structure and creates evidence even if later extraction is not
   justified.
3. The alternative, shared drivers, supporting evidence, unresolved risk,
   owner, next test, and decision impact.
4. The learner can explain the causal method, handle counterexamples, and help
   another engineer apply it without copying the solution.

## Sources and next work

Complete EX-17 and EX-18, write the strategy memo, record the defense, then use
the evaluator only after preserving the independent submission.

## PESD 2.0 extension: modern constraints and ownership

PESD 2.0 adds **a thin local platform product with a service catalog, self-service interface, golden path, policy guardrails, exception path, ownership metadata, platform SLO, adoption and support metrics, FinOps allocation, and an exit plan**.

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

Use CNCF platform guidance and FinOps allocation guidance as primary anchors; measure adoption and support burden as product outcomes.
