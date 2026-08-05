# Module 16: Browser, Frontend, CDN, and Edge Architecture

> **Authoring status:** Review. PESD 2.0 content and machine-readable contracts are migrated. Refreshed evaluator calibration, full platform matrices, offline reruns, cleanup checks, and timed learner pilots remain required before Ready.

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

The 10–12 hour weekly figure is a capacity envelope. Core work is deliberately
budgeted below that ceiling; unused time is recovery buffer, not hidden work.

### Week 87: Model and derive — 8.5 hours

| Work | Time |
|---|---:|
| Bounded authoritative resources | 165 min |
| Local mechanism instruction | 120 min |
| Guided practice | 60 min |
| Model and derive core work | 165 min |

Optional contingency capacity: 210 minutes. It is not core work, carries no required evidence, and may remain unused.

### Week 88: Guided build and prediction freeze — 9 hours

| Work | Time |
|---|---:|
| Bounded authoritative resources | 150 min |
| Local mechanism instruction | 120 min |
| Guided practice | 60 min |
| Required evidence components | 60 min |
| Guided build and prediction freeze core work | 150 min |

Optional contingency capacity: 180 minutes. It is not core work, carries no required evidence, and may remain unused.

### Week 89: Independent build and integration — 10 hours

| Work | Time |
|---|---:|
| Independent build and integration core work | 540 min |
| Independent build and integration verification checkpoint | 60 min |

Optional contingency capacity: 120 minutes. It is not core work, carries no required evidence, and may remain unused.

### Week 90: Break, repair, measure, and diagnose — 10 hours

| Work | Time |
|---|---:|
| Required evidence components | 120 min |
| Break, repair, measure, and diagnose core work | 480 min |

Optional contingency capacity: 120 minutes. It is not core work, carries no required evidence, and may remain unused.

### Week 91: Decide, teach, assess, and freeze — 9.5 hours

| Work | Time |
|---|---:|
| Required evidence components | 120 min |
| Decide, teach, assess, and freeze core work | 390 min |
| Module teach-back | 30 min |
| Learning log and freeze check | 30 min |

Optional contingency capacity: 150 minutes. It is not core work, carries no required evidence, and may remain unused.
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
- Gate 6 runs in Week 103 after Modules 17–18; Module 16 evidence is frozen there but creates no duplicate module gate submission.

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

## PESD 2.0 scope addition

This 5-week module schedules 47 core hours. Its primary
decision is RFC A07. The added graded scope is
offline and degraded client state, browser-storage lifecycle, third-party governance, AI-content transparency and provenance, edge residency, and energy/performance budgets. See Lesson 8, the final guided exercise, final worksheet,
rubric anchors, and remediation map for the integrated evidence contract.
