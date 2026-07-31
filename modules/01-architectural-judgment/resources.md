# Module 1 Resource Guide

## How to use this guide

Local lessons are the primary instruction. External sources show how established
architecture and operations communities frame the same problems. Complete each
bounded assignment and record the requested evidence. Do not read every linked
page on a source site.

All required material was free and reachable on 2026-07-31. If a link fails,
use the named local lesson and note the failure in your learning log.

The course links to external works and supplies original summaries and
exercises; it does not redistribute their text, slides, transcripts, or video.
Publisher copyright and access terms continue to govern each external work.

## Week 1 required resources

### CMU SEI: Reasoning About Software Quality Attributes

- Type: authoritative written source
- Time: 35 minutes
- Read: overview and “General Scenarios,” then read far enough to understand
  that a mechanism may improve one quality while weakening another
- Purpose: distinguish a quality name from a scenario that can influence design
- Evidence: one vague quality claim rewritten as a specific scenario; one
  plausible trade-off
- Link: [Reasoning About Software Quality Attributes](https://www.sei.cmu.edu/library/reasoning-about-software-quality-attributes/)
- Local fallback: [Lesson 4](lessons/04-quality-attribute-scenarios.md)

### CMU SEI webcast: Eliciting Quality Attribute Requirements

- Type: creator/practitioner webcast with supplemental slides
- Time: 60 minutes
- View: complete webcast or study the complete slide deck
- Purpose: see how stakeholder goals become prioritized scenarios
- Evidence: list the workshop steps that prevent the loudest stakeholder from
  defining all priorities
- Link: [Architecting in a Complex World](https://www.sei.cmu.edu/library/architecting-in-a-complex-world-eliciting-and-specifying-quality-attribute-requirements/)
- Accessibility: use supplemental slides or the local written lesson when video
  playback or captions are unsuitable
- Local fallback: [Lesson 4](lessons/04-quality-attribute-scenarios.md)

### Google SRE Workbook: Implementing SLOs

- Type: first-person practitioner handbook
- Time: 45 minutes
- Read: “Getting Started,” “SLI Specification and SLI Implementation,” and
  “Modeling User Journeys”
- Purpose: connect user-visible outcomes to measurable signals while exposing
  measurement limitations
- Evidence: explain one case where a server-side success metric overstates user
  success
- Link: [Implementing SLOs](https://sre.google/workbook/implementing-slos/)
- Local fallback: [Lesson 2](lessons/02-problem-framing-and-workloads.md) and
  [Lesson 4](lessons/04-quality-attribute-scenarios.md)

### Official C4 model

- Type: creator-maintained documentation
- Time: 30 minutes
- Read: overview, abstractions, system context, notation, and diagram-review
  guidance
- Purpose: communicate people, systems, relationships, and boundaries without
  mixing abstraction levels
- Evidence: identify three details that do not belong on a context diagram
- Link: [C4 model](https://c4model.com/)
- License note: the official site states that its website and example diagrams
  use Creative Commons Attribution 4.0; this course still uses original examples
- Local fallback: [Lesson 5](lessons/05-context-and-boundaries.md)

## Week 1 optional video

### Simon Brown: The C4 model for visualising software architecture

- Type: creator-led conference talk hosted by Devoxx
- Time: approximately 60 minutes
- View: complete talk
- Purpose: observe diagram critique and communication failures in practice
- Evidence: record three diagram smells and the review problem each creates
- Link: [C4 model video](https://www.youtube.com/watch?v=KvoBrUd1-5E)
- Accessibility: [Lesson 5](lessons/05-context-and-boundaries.md) covers the
  assigned concepts in text

## Week 2 required resource

### Michael Nygard: Documenting Architecture Decisions

- Type: original practitioner article
- Time: 20 minutes
- Read: complete article
- Purpose: understand the value, scope, lifecycle, and immutability of ADRs
- Evidence: explain why a superseded decision remains useful; name one decision
  too small to justify an ADR
- Link: [Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)
- License note: the publisher states that the article is dedicated to the
  public domain to the extent possible
- Local fallback: [Lesson 8](lessons/08-decisions-rfcs-and-defense.md)

## Week 3 required resource

### AWS Builder Center: Challenges with Distributed Systems

- Type: first-person engineering case by an AWS Senior Principal Engineer
- Time: 45 minutes
- Read: complete article
- Purpose: understand independent failures, nondeterminism, unknown outcomes,
  combinations, and why distributed designs enlarge the failure matrix
- Evidence: add three combined faults and one unknown-outcome case to the
  transit failure matrix
- Link: [Challenges with Distributed Systems](https://builder.aws.com/content/3F08f7GPFiZMCgXD8gny6OjxR0Z/challenges-with-distributed-systems)
- Local fallback: [Lesson 7](lessons/07-failure-models-and-adversarial-review.md)

## Optional paid enrichment

### ISO/IEC 25010:2023

- Type: international product-quality standard
- Time: 60 minutes
- Use: compare its current quality taxonomy with your quality scenarios
- Link: [ISO/IEC 25010:2023](https://www.iso.org/standard/78176.html)
- Access: the abstract and preview are free; the full standard is paid and is
  never required

### Designing Data-Intensive Applications, Chapter 1

- Type: syllabus spine book
- Time: 90 minutes
- Use: compare the chapter’s treatment of reliability, scalability, and
  maintainability with your measurable scenarios
- Access: optional paid book; use the local lessons if unavailable

## Source-review record

For each source, record:

```text
Source:
Date accessed:
Claim or method learned:
Evidence in the source:
How it changes or challenges my model:
Limitations, context, or vendor-specific assumptions:
```
