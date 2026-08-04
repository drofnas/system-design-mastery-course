# Browser, Frontend, CDN, and Edge Architecture Resource Guide

Local lessons are sufficient to complete the module. External sources reinforce
the instruction and provide a checkable primary or practitioner reference; they
never replace the local explanation, practice, or answer key.

## Required authoritative spine

The required records are RES-01, RES-02, RES-04, RES-07, RES-09, RES-11.
Every required record is free and has a local written alternative. All other
records below are optional enrichment and do not consume required module time.

| Week | Required resources | Assigned minutes |
|---:|---|---:|
| 61 | RES-01, RES-02, RES-04 | 155 |
| 62 | RES-07 | 60 |
| 63 | RES-09 | 35 |
| 64 | RES-11 | 45 |

For each assigned source, preserve the requested evidence, one transfer limit,
and one observation that would falsify the claim. A required source that is
temporarily unavailable is replaced by its local alternative and the same evidence
task; record the substitution.

## Resource records

### RES-01: HTML Living Standard: Event loops

- **Author/publisher:** WHATWG
- **URL:** https://html.spec.whatwg.org/multipage/webappapis.html#event-loops
- **Type/status:** living web standard; Required
- **Access:** free
- **Week/time:** Week 61; 50 minutes assigned
- **Purpose:** Ground tasks, microtasks, rendering opportunities, and agent event loops in the platform contract.
- **Boundary and evidence:** Read definitions, queuing tasks, and the processing model; trace one input through task, microtask checkpoint, and rendering opportunity.
- **Local alternative:** [lessons/01-browser-work-rendering-pipeline.md](lessons/01-browser-work-rendering-pipeline.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-02: RenderingNG architecture

- **Author/publisher:** Chromium project
- **URL:** https://developer.chrome.com/docs/chromium/renderingng-architecture
- **Type/status:** maintainer architecture guide; Required
- **Access:** free
- **Week/time:** Week 61; 45 minutes assigned
- **Purpose:** Connect style, layout, paint, raster, compositing, and thread placement to observed work.
- **Boundary and evidence:** Read the pipeline and threading sections; label which Northstar work must use the main thread and which may bypass it.
- **Local alternative:** [lessons/01-browser-work-rendering-pipeline.md](lessons/01-browser-work-rendering-pipeline.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-04: RFC 9111: HTTP Caching

- **Author/publisher:** IETF
- **URL:** https://www.rfc-editor.org/rfc/rfc9111.html
- **Type/status:** Internet Standard; Required
- **Access:** free
- **Week/time:** Week 61; 60 minutes assigned
- **Purpose:** Reason precisely about cache storage, freshness, validation, invalidation, and shared-cache restrictions.
- **Boundary and evidence:** Read Sections 3–5 and 7; produce the cache decision table for all four Northstar routes.
- **Local alternative:** [lessons/04-http-cdn-cache-safety.md](lessons/04-http-cdn-cache-safety.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-07: Web Content Accessibility Guidelines (WCAG) 2.2

- **Author/publisher:** W3C Web Accessibility Initiative
- **URL:** https://www.w3.org/TR/WCAG22/
- **Type/status:** W3C Recommendation; Required
- **Access:** free
- **Week/time:** Week 62; 60 minutes assigned
- **Purpose:** Tie resilient interaction to testable accessibility outcomes rather than tool scores.
- **Boundary and evidence:** Read Principles, Conformance, 1.3.1, 2.1.1, 2.4.3, 2.4.7, 2.5.8, 3.3.1, and 4.1.2; create manual and automated checks.
- **Local alternative:** [lessons/05-accessibility-resilient-interaction.md](lessons/05-accessibility-resilient-interaction.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-09: Trace Context

- **Author/publisher:** W3C Distributed Tracing Working Group
- **URL:** https://www.w3.org/TR/trace-context/
- **Type/status:** W3C Recommendation; Required
- **Access:** free
- **Week/time:** Week 63; 35 minutes assigned
- **Purpose:** Propagate interoperable trace identity without trusting client sampling or leaking session data.
- **Boundary and evidence:** Read the design overview and security considerations; trace browser, edge, and origin parentage and list rejected sensitive attributes.
- **Local alternative:** [lessons/06-memory-third-parties-observability.md](lessons/06-memory-third-parties-observability.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-11: Building a better web: A faster YouTube

- **Author/publisher:** YouTube and Chrome teams
- **URL:** https://web.dev/case-studies/better-youtube-web-part1
- **Type/status:** first-person engineering case; Required
- **Access:** free
- **Week/time:** Week 64; 45 minutes assigned
- **Purpose:** Examine how a large operator connected constrained devices, field data, code delivery, and product outcomes.
- **Boundary and evidence:** Read the full case; separate measurements, interventions, product outcomes, and claims that do not transfer to Northstar.
- **Local alternative:** [lessons/08-frontend-edge-decision-teachback.md](lessons/08-frontend-edge-decision-teachback.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-03: Interaction to Next Paint (INP)

- **Author/publisher:** web.dev / Chrome team
- **URL:** https://web.dev/articles/inp
- **Type/status:** maintainer metric guide; Optional enrichment
- **Access:** free
- **Week/time:** Week 61; 45 minutes optional
- **Purpose:** Interpret interaction latency and separate field thresholds from controlled lab observations.
- **Boundary and evidence:** Read through the interaction anatomy and thresholds; map input delay, processing, and presentation delay to the Northstar filter interaction.
- **Local alternative:** [lessons/02-performance-budgets-evidence.md](lessons/02-performance-budgets-evidence.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-05: renderToPipeableStream

- **Author/publisher:** React project
- **URL:** https://react.dev/reference/react-dom/server/renderToPipeableStream
- **Type/status:** maintainer API reference; Optional enrichment
- **Access:** free
- **Week/time:** Week 62; 35 minutes optional
- **Purpose:** Expose streaming HTML shell, readiness, error, and abort semantics without a framework abstraction.
- **Boundary and evidence:** Read reference, caveats, and error recovery; identify when response status and headers become irreversible.
- **Local alternative:** [lessons/03-route-rendering-hydration.md](lessons/03-route-rendering-hydration.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-06: hydrateRoot

- **Author/publisher:** React project
- **URL:** https://react.dev/reference/react-dom/client/hydrateRoot
- **Type/status:** maintainer API reference; Optional enrichment
- **Access:** free
- **Week/time:** Week 62; 35 minutes optional
- **Purpose:** Define hydration identity, mismatch handling, and root ownership.
- **Boundary and evidence:** Read caveats and error hooks; define the server/client inputs whose equality the lab must preserve.
- **Local alternative:** [lessons/03-route-rendering-hydration.md](lessons/03-route-rendering-hydration.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-08: Fix memory problems

- **Author/publisher:** Chrome DevTools
- **URL:** https://developer.chrome.com/docs/devtools/memory-problems
- **Type/status:** maintainer diagnostic guide; Optional enrichment
- **Access:** free
- **Week/time:** Week 63; 45 minutes optional
- **Purpose:** Use heap growth, detached DOM, and allocation evidence to diagnose retained browser resources.
- **Boundary and evidence:** Read the overview and leak workflow; define a repeated-navigation test and the evidence that distinguishes growth from a leak.
- **Local alternative:** [lessons/06-memory-third-parties-observability.md](lessons/06-memory-third-parties-observability.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-10: Life of a Pixel (Chromium University 2020)

- **Author/publisher:** Chromium project
- **URL:** https://www.youtube.com/watch?v=K2QHdgAKP-s
- **Type/status:** captioned technical video; Optional enrichment
- **Access:** free
- **Week/time:** Week 61; 60 minutes optional
- **Purpose:** Visualize the journey from web content to displayed pixels while identifying version-bound Chromium details.
- **Boundary and evidence:** Watch with captions; draw the pipeline, then annotate at least two details superseded or clarified by current RenderingNG documentation.
- **Local alternative:** [lessons/01-browser-work-rendering-pipeline.md](lessons/01-browser-work-rendering-pipeline.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-12: Browser instrumentation

- **Author/publisher:** OpenTelemetry project
- **URL:** https://opentelemetry.io/docs/languages/js/getting-started/browser/
- **Type/status:** maintainer documentation; Optional enrichment
- **Access:** free
- **Week/time:** Week 63; 30 minutes optional
- **Purpose:** Inspect a browser tracing implementation while preserving its documented experimental boundary.
- **Boundary and evidence:** Read the warning, setup, and instrumentation sections; record which contracts are standard and which library behavior remains experimental.
- **Local alternative:** [lessons/06-memory-third-parties-observability.md](lessons/06-memory-third-parties-observability.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-13: Load Third-Party JavaScript

- **Author/publisher:** web.dev / Chrome team
- **URL:** https://web.dev/articles/optimizing-content-efficiency-loading-third-party-javascript
- **Type/status:** maintainer guidance; Optional enrichment
- **Access:** free
- **Week/time:** Week 63; 45 minutes optional
- **Purpose:** Treat third-party code as a performance, privacy, security, and ownership dependency.
- **Boundary and evidence:** Read risks, measurement, loading, and safety sections; write a Northstar admission, failure, and removal policy.
- **Local alternative:** [lessons/06-memory-third-parties-observability.md](lessons/06-memory-third-parties-observability.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

Do not copy articles, chapters, slides, or transcripts into learner artifacts.
Use short attributed quotations only when necessary and otherwise paraphrase with
the source ID, exact section boundary, and stated evidence limit.
