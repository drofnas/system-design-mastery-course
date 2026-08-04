# Module 16: Browser, Frontend, CDN, and Edge Architecture

> **Authoring status:** Ready. The pinned browser lab, F01–F08 pairs,
> accessibility and manual checks, six isolated evaluator runs, calibration
> checking, semantic and resource review, and focused and full-course validation
> passed on 2026-08-03.

## What this module changes

A rendered page is not yet a responsive, safe, operable user journey. Browser
work competes on finite threads; HTML can precede interactivity; shared caches
can cross trust boundaries; and an edge fallback can preserve availability while
silently violating freshness or authority. This module teaches you to assign a
rendering, cache, accessibility, telemetry, and ownership contract to each route,
then falsify it in a real browser and a deterministic model.

The continuing non-capstone case is the **Northstar Observatory Public Sky
Portal**. Its public event guide, streamed event page, live-status client, and
private staff schedule contain no products, merchants, inventory, checkout,
payments, orders, or commerce architecture. Freeze independent storefront
decisions before opening the completed case or answer key.

## Prerequisites

- Modules 1–15, especially capacity, observability, HTTP, deadlines, security,
  architecture evolution, and JavaScript execution models
- Node.js LTS and npm for the measured lab; Python 3.11+ for deterministic checks
- A Chromium-compatible environment for Playwright; substitutions must record
  browser engine, version, host, and changed evidence boundary
- Preserved capstone baselines and Gate 5 evidence; this module does not rewrite them

## Learning outcomes

By the end of the module, you can:

1. Trace browser scheduling and rendering from input to displayed pixels.
2. Set and interpret route-level performance budgets from lab and field evidence.
3. Select static, server, streaming, client, and island rendering per route.
4. Implement safe HTTP/CDN caching, invalidation, and private-response isolation.
5. Build accessible, keyboard-complete, resilient interactions.
6. Diagnose long tasks, hydration mismatches, memory leaks, and third parties.
7. Propagate privacy-aware trace context from browser through edge to origin.
8. Defend frontend and edge boundaries with cost, ownership, migration, and reversal.

## Schedule

### Week 61: Model and freeze browser-edge predictions — 11 hours

| Work | Time |
|---|---:|
| Lessons 1–4 and bounded sources | 4 h |
| EX-01–EX-10 with Northstar route modeling | 2 h |
| Independent route, budget, cache, accessibility, and F01–F08 baseline | 3.5 h |
| Freeze, self-check, and learning log | 1.5 h |

Use the [Week 61 worksheet](worksheets/week-61-browser-edge-model.md).

### Week 62: Build the route-specific storefront — 12 hours

| Work | Time |
|---|---:|
| Lessons 3, 5, and 7; Northstar lab tutorial | 2.5 h |
| EX-05–EX-12 and conformance rehearsal | 2 h |
| Independent storefront implementation | 6.5 h |
| Conformance review and learning log | 1 h |

Use the [Week 62 worksheet](worksheets/week-62-storefront-build.md).

### Week 63: Break and measure browser-edge assumptions — 12 hours

| Work | Time |
|---|---:|
| Lessons 1, 4, and 6; bounded sources | 2 h |
| EX-13–EX-17 and experiment rehearsal | 2 h |
| F01–F08 broken/repaired trials | 6 h |
| Failure matrix, performance review, and learning log | 2 h |

Use the [Week 63 worksheet](worksheets/week-63-browser-edge-failures.md).

### Week 64: Decide, teach, assess, and remediate — 11 hours

| Work | Time |
|---|---:|
| Lesson 8, practitioner case, and EX-18 | 1.5 h |
| Frontend-edge RFC and defense | 4 h |
| Module evaluation and teach-back | 2 h |
| Remediation and learning log | 3.5 h |

Use the [Week 64 worksheet](worksheets/week-64-architecture-defense.md).

## Learn

1. [Browser work and the rendering pipeline](lessons/01-browser-work-rendering-pipeline.md)
2. [Performance budgets and evidence](lessons/02-performance-budgets-evidence.md)
3. [Route rendering and hydration](lessons/03-route-rendering-hydration.md)
4. [HTTP and CDN cache safety](lessons/04-http-cdn-cache-safety.md)
5. [Accessibility and resilient interaction](lessons/05-accessibility-resilient-interaction.md)
6. [Memory, third parties, and observability](lessons/06-memory-third-parties-observability.md)
7. [Northstar browser-edge tutorial](lessons/07-northstar-browser-edge-tutorial.md)
8. [Frontend-edge decision and teach-back](lessons/08-frontend-edge-decision-teachback.md)

Use the [glossary](glossary.md), [resource guide](resources.md), and
[lab interface](lab/README.md) as references after studying the mechanisms.

## Practice and independent evidence

- Freeze A01 before the completed [Northstar case](case-study/northstar-sky-portal.md).
- Complete [guided exercises](exercises/exercises.md) before opening the
  [explained answers](exercises/answer-key.md).
- Run the deterministic and measured [browser-edge lab](lab/README.md), preserve
  scenario, input, configuration, and output hashes, then build the commerce
  storefront independently.
- Treat Chromium lab results as environment-bound. Field Core Web Vitals,
  cross-engine behavior, assistive-technology use, and production CDN behavior
  need separate evidence.
- Preserve frozen predictions and raw trials. Corrections belong in dated addenda.

This module contributes one substantial RFC, one performance investigation,
one failure matrix, and one recorded architecture teach-back.

## Assessment and completion

- Read the [assessment contract](assessment/README.md), [anchored rubric](assessment/rubric.md),
  [evaluator prompt](assessment/evaluator-prompt.md), [remediation map](assessment/remediation-map.md),
  and [readiness review](assessment/semantic-readiness-review.md).
- Pass G01–G06, average at least 3.0, and avoid a zero in R04–R06 or R09.
- Gate 6 occurs in Week 72 after Modules 17–18; Module 16 creates no gate submission.

## Evidence boundary and AI use

The lab can expose one pinned Chromium/React/Node path, local cache semantics,
controlled throttling, and deterministic invariants. It cannot prove population
percentiles, every browser or assistive technology, production CDN equivalence,
legal compliance, or future framework behavior.

AI may challenge arithmetic, hypotheses, experiment design, accessibility test
coverage, and alternatives. It may not choose the graded architecture, invent
measurements, rewrite frozen work, produce replacement graded answers, or answer
during the defense.

## Course-wide completion contracts

- The machine-readable `module.json` time blocks are the canonical required-work budget.
- The [factual-claims ledger](assessment/factual-claims.json) maps each local lesson to its authoritative source boundary.
- Use the [provider-neutral evaluation workflow](../../EVALUATION_GUIDE.md) only after learner evidence is committed.
- Use the [sealed local gate workflow](../../SOLO_GATE_GUIDE.md) when a course gate applies. Human review is optional.

A frozen self-evaluation may establish **Solo Complete**; independent human or LLM review may establish **Independently Validated**. Synthetic lab values are not production measurements.
