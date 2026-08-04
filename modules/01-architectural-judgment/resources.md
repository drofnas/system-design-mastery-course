# Architectural Judgment Resource Guide

Local lessons are sufficient to complete the module. External sources reinforce
the instruction and provide a checkable primary or practitioner reference; they
never replace the local explanation, practice, or answer key.

## Required authoritative spine

The required records are RES-01, RES-04, RES-06, RES-07.
Every required record is free and has a local written alternative. All other
records below are optional enrichment and do not consume required module time.

| Week | Required resources | Assigned minutes |
|---:|---|---:|
| 1 | RES-01, RES-04 | 65 |
| 2 | RES-06 | 20 |
| 3 | RES-07 | 45 |
| 4 | None | 0 |

For each assigned source, preserve the requested evidence, one transfer limit,
and one observation that would falsify the claim. A required source that is
temporarily unavailable is replaced by its local alternative and the same evidence
task; record the substitution.

## Resource records

### RES-01: Reasoning About Software Quality Attributes

- **Author/publisher:** Software Engineering Institute, Carnegie Mellon University
- **URL:** https://www.sei.cmu.edu/library/reasoning-about-software-quality-attributes/
- **Type/status:** authoritative written source; Required
- **Access:** free
- **Week/time:** Week 1; 35 minutes assigned
- **Purpose:** Read the overview and General Scenarios sections through the discussion of trade-offs.
- **Boundary and evidence:** Read the overview and General Scenarios sections through the discussion of trade-offs. Record one quality name that remains ambiguous until expressed as a scenario.
- **Local alternative:** [lessons/04-quality-attribute-scenarios.md](lessons/04-quality-attribute-scenarios.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-07-31
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-04: The C4 model for visualising software architecture

- **Author/publisher:** Simon Brown and the C4 model project
- **URL:** https://c4model.com/
- **Type/status:** official documentation; Required
- **Access:** free
- **Week/time:** Week 1; 30 minutes assigned
- **Purpose:** Read the overview, abstractions, system-context guidance, notation guidance, and diagram-review checklist.
- **Boundary and evidence:** Read the overview, abstractions, system-context guidance, notation guidance, and diagram-review checklist. Identify which details do not belong on a context diagram.
- **Local alternative:** [lessons/05-context-and-boundaries.md](lessons/05-context-and-boundaries.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-07-31
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-06: Documenting Architecture Decisions

- **Author/publisher:** Michael Nygard; Cognitect
- **URL:** https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions
- **Type/status:** original practitioner article; Required
- **Access:** free
- **Week/time:** Week 2; 20 minutes assigned
- **Purpose:** Read the complete article.
- **Boundary and evidence:** Read the complete article. Explain why preserving a superseded decision is useful and identify one decision too small to deserve an ADR.
- **Local alternative:** [lessons/08-decisions-rfcs-and-defense.md](lessons/08-decisions-rfcs-and-defense.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-07-31
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-07: Challenges with Distributed Systems

- **Author/publisher:** Amazon Web Services
- **URL:** https://builder.aws.com/content/3F08f7GPFiZMCgXD8gny6OjxR0Z/challenges-with-distributed-systems
- **Type/status:** first-person engineering case; Required
- **Access:** free
- **Week/time:** Week 3; 45 minutes assigned
- **Purpose:** Read the complete article.
- **Boundary and evidence:** Read the complete article. Add three independent failure combinations and one unknown-outcome case to the transit case failure matrix.
- **Local alternative:** [lessons/07-failure-models-and-adversarial-review.md](lessons/07-failure-models-and-adversarial-review.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-07-31
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-02: Architecting in a Complex World: Eliciting and Specifying Quality Attribute Requirements

- **Author/publisher:** Software Engineering Institute, Carnegie Mellon University
- **URL:** https://www.sei.cmu.edu/library/architecting-in-a-complex-world-eliciting-and-specifying-quality-attribute-requirements/
- **Type/status:** webcast; Optional enrichment
- **Access:** free
- **Week/time:** Week 1; 60 minutes optional
- **Purpose:** Watch the complete webcast or study the supplemental slides.
- **Boundary and evidence:** Watch the complete webcast or study the supplemental slides. Write down the workshop steps that prevent the loudest stakeholder from defining every priority.
- **Local alternative:** [lessons/04-quality-attribute-scenarios.md](lessons/04-quality-attribute-scenarios.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-07-31
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-03: Implementing SLOs

- **Author/publisher:** Google Site Reliability Engineering
- **URL:** https://sre.google/workbook/implementing-slos/
- **Type/status:** practitioner handbook chapter; Optional enrichment
- **Access:** free
- **Week/time:** Week 1; 45 minutes optional
- **Purpose:** Read Getting Started, SLI Specification versus Implementation, and Modeling User Journeys.
- **Boundary and evidence:** Read Getting Started, SLI Specification versus Implementation, and Modeling User Journeys. Explain why a server metric may misrepresent a user's outcome.
- **Local alternative:** [lessons/02-problem-framing-and-workloads.md](lessons/02-problem-framing-and-workloads.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-07-31
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-05: The C4 model for visualising software architecture

- **Author/publisher:** Simon Brown and the C4 model project
- **URL:** https://www.youtube.com/watch?v=KvoBrUd1-5E
- **Type/status:** conference video; Optional enrichment
- **Access:** free
- **Week/time:** Week 1; 60 minutes optional
- **Purpose:** Watch the complete creator-led talk.
- **Boundary and evidence:** Watch the complete creator-led talk. Capture three diagram smells and how each impairs a design review.
- **Local alternative:** [lessons/05-context-and-boundaries.md](lessons/05-context-and-boundaries.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-07-31
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-08: ISO/IEC 25010:2023 Product quality model

- **Author/publisher:** ISO/IEC
- **URL:** https://www.iso.org/standard/78176.html
- **Type/status:** standard; Optional enrichment
- **Access:** paid
- **Week/time:** Week 1; 60 minutes optional
- **Purpose:** Optional: review the current product-quality taxonomy and compare its categories with the scenarios you wrote.
- **Boundary and evidence:** Optional: review the current product-quality taxonomy and compare its categories with the scenarios you wrote.
- **Local alternative:** [lessons/04-quality-attribute-scenarios.md](lessons/04-quality-attribute-scenarios.md)
- **Verification:** verified manually optional; manual primary-source verification; last checked 2026-07-31
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

Do not copy articles, chapters, slides, or transcripts into learner artifacts.
Use short attributed quotations only when necessary and otherwise paraphrase with
the source ID, exact section boundary, and stated evidence limit.
