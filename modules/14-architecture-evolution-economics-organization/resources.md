# Architecture Evolution, Economics, and Organization Resource Guide

Local lessons are sufficient to complete the module. External sources reinforce
the instruction and provide a checkable primary or practitioner reference; they
never replace the local explanation, practice, or answer key.

## Required authoritative spine

The required records are RES-02, RES-05, RES-07, RES-08, RES-09, RES-10, RES-11.
Every required record is free and has a local written alternative. All other
records below are optional enrichment and do not consume required module time.

| Week | Required resources | Assigned minutes |
|---:|---|---:|
| 75 | RES-05, RES-07, RES-10, RES-11 | 160 |
| 76 | RES-02, RES-08, RES-09 | 150 |

For each assigned source, preserve the requested evidence, one transfer limit,
and one observation that would falsify the claim. A required source that is
temporarily unavailable is replaced by its local alternative and the same evidence
task; record the substitution.

## Resource records

### RES-02: Conway's Law and How Do Committees Invent?

- **Author/publisher:** Melvin E. Conway
- **URL:** https://melconway.com/Home/Conways_Law.html
- **Type/status:** original paper and author commentary; Required
- **Access:** free
- **Lesson/time:** the relevant lesson; 45 minutes assigned
- **Purpose:** Connect communication paths to interface structure without treating organization as destiny.
- **Boundary and evidence:** Read the author page and linked original paper; map three required technical interfaces to their human communication paths.
- **Local alternative:** [lessons/02-social-architecture-ownership.md](lessons/02-social-architecture-ownership.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-05: Patterns of Legacy Displacement

- **Author/publisher:** Ian Cartwright, Rob Horn, and James Lewis; MartinFowler.com
- **URL:** https://martinfowler.com/articles/patterns-legacy-displacement/
- **Type/status:** practitioner pattern collection; Required
- **Access:** free
- **Lesson/time:** the relevant lesson; 75 minutes assigned
- **Purpose:** Design incremental seams and transitional architecture tied to outcomes and removal conditions.
- **Boundary and evidence:** Read Breaking the Cycle, Successfully Deliver the Parts, and the middleware example; produce a seam, transition asset, removal condition, and cost-of-risk argument.
- **Local alternative:** [lessons/06-incremental-migration-backfills.md](lessons/06-incremental-migration-backfills.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-07: Semantic Versioning 2.0.0

- **Author/publisher:** Semantic Versioning maintainers
- **URL:** https://semver.org/
- **Type/status:** open specification; Required
- **Access:** free
- **Lesson/time:** the relevant lesson; 45 minutes assigned
- **Purpose:** Use a declared public contract and explicit compatibility signal while recognizing limits for data and protocols.
- **Boundary and evidence:** Read the Summary and specification items 1-11; classify six changes and state two cases where SemVer cannot prove runtime compatibility.
- **Local alternative:** [lessons/05-compatibility-schema-evolution.md](lessons/05-compatibility-schema-evolution.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-08: Canarying Releases

- **Author/publisher:** Google Site Reliability Engineering
- **URL:** https://sre.google/workbook/canarying-releases/
- **Type/status:** practitioner book chapter; Required
- **Access:** free
- **Lesson/time:** the relevant lesson; 60 minutes assigned
- **Purpose:** Bound blast radius and connect promotion or rollback to measured candidate-versus-control evidence.
- **Boundary and evidence:** Read Canary Release through Canary Implementation; define population, duration, comparison metrics, budget exposure, promotion, and rollback thresholds.
- **Local alternative:** [lessons/07-shadow-cutover-rollback.md](lessons/07-shadow-cutover-rollback.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-09: Maintaining Client Transparency While Migrating Systems

- **Author/publisher:** Google SRE Prodcast
- **URL:** https://sre.google/prodcast/transcripts/sre-prodcast-01-05/
- **Type/status:** recorded practitioner interview with HTML transcript; Required
- **Access:** free
- **Lesson/time:** the relevant lesson; 45 minutes assigned
- **Purpose:** Treat traffic replay, discrepancy measurement, gradual cutover, and fast rollback as client-transparency controls.
- **Boundary and evidence:** Listen to the episode or read the transcript; enumerate user-visible states, mismatch measures, rollout stages, rollback trigger, and one unknown not captured server-side.
- **Local alternative:** [lessons/07-shadow-cutover-rollback.md](lessons/07-shadow-cutover-rollback.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-01: Under Deconstruction: The State of Shopify's Monolith

- **Author/publisher:** Shopify Engineering
- **URL:** https://shopify.engineering/shopify-monolith
- **Type/status:** first-person engineering case; Optional enrichment
- **Access:** free
- **Lesson/time:** the relevant lesson; 60 minutes optional
- **Purpose:** Compare modularization with service extraction using observed change and complexity costs.
- **Boundary and evidence:** Read the complete article; record three boundary drivers, two reasons to remain modular, and one extraction threshold.
- **Local alternative:** [lessons/01-boundaries-outcomes-coupling.md](lessons/01-boundaries-outcomes-coupling.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-03: Team Interaction Modeling with Team Topologies

- **Author/publisher:** Team Topologies
- **URL:** https://teamtopologies.com/key-concepts-content/team-interaction-modeling-with-team-topologies
- **Type/status:** maintainer guidance; Optional enrichment
- **Access:** free
- **Lesson/time:** the relevant lesson; 60 minutes optional
- **Purpose:** Make cognitive load, ownership, and temporary versus durable interactions visible.
- **Boundary and evidence:** Read the interaction-modeling and cognitive-load sections; draw current and target interaction maps with one expiry condition.
- **Local alternative:** [lessons/02-social-architecture-ownership.md](lessons/02-social-architecture-ownership.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-04: Capability: Unit Economics

- **Author/publisher:** FinOps Foundation
- **URL:** https://www.finops.org/framework/capabilities/unit-economics/
- **Type/status:** foundation framework; Optional enrichment
- **Access:** free
- **Lesson/time:** the relevant lesson; 60 minutes optional
- **Purpose:** Connect technical spend to a useful product outcome and decision threshold.
- **Boundary and evidence:** Read Definition, Functional Activities, and Inputs and Outputs; define one business unit metric, one resource metric, sources, owner, and threshold.
- **Local alternative:** [lessons/04-total-cost-unit-economics.md](lessons/04-total-cost-unit-economics.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-06: Online Migrations at Scale

- **Author/publisher:** Jacqueline Xu Atlas; Stripe Engineering
- **URL:** https://stripe.com/blog/online-migrations
- **Type/status:** first-person engineering case; Optional enrichment
- **Access:** free
- **Lesson/time:** the relevant lesson; 75 minutes optional
- **Purpose:** Examine phased writes, backfill, comparison, cutover, and cleanup in a live migration.
- **Boundary and evidence:** Read the complete article; identify authority in each phase, backfill verification, divergence risk, cutover gate, and cleanup proof.
- **Local alternative:** [lessons/06-incremental-migration-backfills.md](lessons/06-incremental-migration-backfills.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

Do not copy articles, chapters, slides, or transcripts into learner artifacts.
Use short attributed quotations only when necessary and otherwise paraphrase with
the source ID, exact section boundary, and stated evidence limit.
