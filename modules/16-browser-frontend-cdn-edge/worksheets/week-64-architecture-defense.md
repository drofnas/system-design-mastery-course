# Week 64: Frontend-Edge RFC and Defense

## RFC checklist

- User/business outcomes and route workload
- Per-route rendering, cache, accessibility, telemetry, and failure policy
- Browser/edge/origin authority and trust boundaries
- Design-system and third-party governance
- BFF and microfrontend alternatives using shared drivers
- Field/lab evidence and unresolved uncertainty
- Capacity and cost per useful visit/interaction
- Development, operations, security, accessibility, and incident owners
- Migration coexistence, compatibility, rollback, and decommissioning
- Dissent, stopping conditions, and quantified reversal evidence

## Twelve-minute defense

1. **Five minutes:** route placement, cache authority, accessibility, and user outcome.
2. **Four minutes:** F01–F08 evidence, operations, security, cost, and ownership.
3. **Three minutes:** alternatives, dissent, migration, stops, and reversal.

## Adversarial questions

- What useful result exists before JavaScript and during dependency failure?
- Which private or stale object can reach a shared cache?
- Which field target is supported by population evidence rather than the lab?
- Which manual accessibility evidence remains missing?
- Which boundary creates more runtime and coordination than it removes?
- How does rollback work after edge cache population or streamed commitment?
- What happens when the owning frontend or CDN team is unavailable?

## Teach-back transfer

Have a reviewer apply the method to a non-commerce, non-Northstar route. Record
their assumptions, where the method transferred, confusion, correction, and one
change to your RFC or explanation.

Human review is preferred and produces stronger portfolio evidence. When no
reviewer is available, use `scripts/prepare_solo_review.py`, record the five
answers without live AI, freeze them, and request provider-neutral critique only
afterward. Disclose the solo substitution and note that it does not demonstrate
transfer to another person's route.

## Assessment and remediation

Freeze the defense and A09 evaluation. Map each finding to the remediation map
and create A10 as a separate dated revision. Never rewrite A01, A04, or the
submitted defense.
