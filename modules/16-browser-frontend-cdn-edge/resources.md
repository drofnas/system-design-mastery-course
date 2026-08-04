# Module 16 Resource Guide

External sources reinforce the local lessons; none replaces them. Required
sources are free. Verification checks title, publisher, assignment boundary,
access, and whether the cited contract still matches the local explanation.

| ID | Week | Required | Time | Boundary and evidence |
|---|---:|---|---:|---|
| RES-01 | 61 | Yes | 50m | WHATWG event-loop definitions, task queuing, processing model; produce an input trace. |
| RES-02 | 61 | Yes | 45m | RenderingNG pipeline and threads; mark main/compositor work and Chromium scope. |
| RES-03 | 61 | Yes | 45m | INP anatomy and thresholds; separate field population evidence from the lab. |
| RES-04 | 61 | Yes | 60m | RFC 9111 Sections 3–5 and 7; produce a route cache decision table. |
| RES-05 | 62 | Yes | 35m | React streaming reference; identify shell, header, error, and abort commitments. |
| RES-06 | 62 | Yes | 35m | React hydration reference; define equality and recoverable-error evidence. |
| RES-07 | 62 | Yes | 60m | Named WCAG 2.2 criteria; split automated, manual keyboard, and assistive-tech evidence. |
| RES-08 | 63 | Yes | 45m | Chrome memory workflow; design repeated-navigation leak evidence. |
| RES-09 | 63 | Yes | 35m | W3C trace design and security; draw browser-edge-origin parentage. |
| RES-10 | 61 | Yes | 60m | Captioned Chromium video; annotate historical claims with current RenderingNG. |
| RES-11 | 64 | Yes | 45m | YouTube operator case; separate observed results from transferable method. |
| RES-12 | 63 | No | 30m | OpenTelemetry browser setup; record its experimental library boundary. |
| RES-13 | 63 | Yes | 45m | Third-party risks and controls; write admission, failure, and removal policy. |

Each manifest record contains the exact URL, publisher, purpose, assignment,
verification date, and local text alternative. If a link later fails, use its
listed lesson, record the access failure, and do not skip the required evidence.

## Verification record — 2026-08-03

- RES-01–RES-09 and RES-11–RES-13 resolved to the named standards-body,
  maintainer, or first-person publisher pages over HTTPS. Their titles,
  boundaries, free access, and local alternatives match `module.json`.
- RES-10 resolved to the Chromium project video page. Its public player metadata
  advertised `captionTracks` with English (`languageCode: en`). Current
  RenderingNG documentation and local L01 remain the required written/current
  comparison because the 2020 video contains version-bound implementation detail.
- Package versions were checked against their registries and the Node release
  schedule before locking. The measured harness records Node 24.19.0,
  React/React DOM 19.2.8, Playwright 1.62.1, axe-core Playwright 4.12.1,
  esbuild 0.28.1, and Chromium 151.0.7922.34.

Verification confirms reachability and assignment fit on that date; it does not
transfer implementation-specific browser behavior into a platform guarantee.

## Reflection questions

1. Which source defines a normative contract, and which reports one implementation?
2. Which threshold is a population target rather than a deterministic test oracle?
3. Which guidance changes when the response is personalized or authorization-bound?
4. Which current browser or library version bounds each observation?
5. What evidence would make a source's recommendation inapplicable to your route?
