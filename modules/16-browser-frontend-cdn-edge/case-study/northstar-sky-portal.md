# Northstar Observatory Public Sky Portal

Open this completed case only after freezing A01. It demonstrates the module
method; it is not a commerce storefront answer.

## Problem and users

Northstar publishes sky events for the public and maintains a private staff
schedule. Public visitors include screen-reader and keyboard users, older mobile
devices, and rural connections. Staff need current schedules and safe edits.

## Workload and targets

| Journey | Normal/peak | Evidence target |
|---|---|---|
| Browse public events | 20/400 requests/s | monthly mobile p75 LCP ≤2.5s; lab critical bytes ≤180 KiB |
| Filter events | 5–80 interactions/s | monthly mobile p75 INP ≤200ms; lab interaction guardrail 150ms |
| View streamed event | 10/250 requests/s | useful event identity before optional regional weather |
| Read live status | 2/120 requests/s | version and observation time always visible; 10s deadline |
| Edit staff schedule | 0.2/5 requests/s | private no-store response; optimistic version check; complete audit |

Targets are decision inputs, not claims that the included lab achieves population
percentiles. Field and lab evidence remain separate.

## Invariants

1. Critical input receives a visible response within its controlled guardrail.
2. The critical route stays within declared transfer/request/work budgets.
3. Server markup and initial client state agree for every hydration root.
4. Navigation releases route-owned listeners, timers, requests, and DOM retainers.
5. A public cached response matches every bounded representation dimension.
6. A private response is never stored or served by a shared cache.
7. Third-party failure cannot block the core public journey.
8. Stale public fallback is bounded and marked; private/current status fails closed.
9. Automated and manual accessibility evidence covers every interaction state.
10. Trace parentage is valid and contains no session secret or unbounded private value.

## Route decision table

| Route | Authority | Rendering | Cache | Client work | Failure |
|---|---|---|---|---|---|
| `/sky-events` | signed publication snapshot | static HTML | public; language-aware; shared max 300s | filter island | show versioned snapshot |
| `/events/:id` | event registry + weather evidence | streamed server HTML | public event version; weather marked separately | disclosure/favorite island | event shell survives weather failure |
| `/live` | current status service | static semantic shell + client data | shell shared; API no-store | deadline-bound refresh | show timestamped last known only within policy |
| `/staff/schedule` | staff scheduling authority | request server render | `private, no-store`; shared bypass | edit island | fail closed; never shared-stale |

## Browser and accessibility contract

The public heading and event links exist before JavaScript. Filter controls use
native inputs; result count is a polite status and focus remains on the changed
control. Streamed weather has a stable region and does not move focus. Live status
exposes freshness text. Staff errors associate summary and field messages. Tests
include semantic DOM assertions, axe rules, keyboard order/activation, focus after
hydration/error, 200% zoom/reflow, and one recorded assistive-technology path.

## Cache and edge contract

The edge normalizes public method, host, path, approved query, language, encoding,
and content version. Tracking queries do not vary content. Authentication bypasses
lookup and storage. Public stale-on-error is capped at 600 seconds and includes
version/age/degraded status. Live current status and staff routes fail closed.

## Observability contract

Browser spans correlate document, interaction, and fetch work. The edge validates
trace syntax, creates its own span, and forwards context to origin. Allowed fields
are route template, render mode, cache outcome, content version, failure code, and
coarse client class. Raw cookie, staff identity, search text, and full sensitive
URLs are prohibited. Telemetry has sampling, cardinality, retention, and cost owners.

## F01–F08 result summary

| Pair | Broken cause | Single repair | Repaired evidence |
|---|---|---|---|
| F01 | 240ms main-thread filter task | bounded chunks/yield | visible count precedes enrichment; I01 passes |
| F02 | client initial version differs | one serialized state | no mismatch; semantic DOM/focus preserved |
| F03 | route cleanup omitted | owned cleanup | resource counts return to baseline |
| F04 | blocking third-party map | deferred isolated optional adapter | route succeeds when slow/blocked |
| F05 | language omitted from key | bounded language key | English and Spanish objects remain distinct |
| F06 | private lookup/store enabled | private bypass | no cache entry or cross-session response |
| F07 | stale served without route bound | authority-aware stale policy | marked public fallback; private/current fail closed |
| F08 | noncritical bytes block route | critical-resource prioritization | controlled guardrails restored under same profile |

## Architecture decision

Northstar keeps one deployable portal with modules and independently hydrated
islands. A thin BFF composes public read models but owns no publication or staff
authority. Selected public rendering and caching may run at the edge. Staff work
remains at origin. The choice includes a shared component/accessibility contract,
third-party admission and kill switch, on-call ownership, cost per useful public
visit, rollout by route, rollback to origin rendering, and removal criteria.

Reopen the decision if field targets fail for two windows, edge cost breaches its
budget, BFF availability dominates the journey, accessibility regressions recur,
or the team cannot operate streaming/cache invalidation safely.

## Acceptable alternatives

A fully origin-rendered public portal is defensible when scale and latency evidence
do not justify edge operation. A client-heavy live route is defensible when its
semantic shell, constrained-device behavior, recovery, and accessibility pass.
Different frameworks are acceptable. The rubric evaluates causal contracts and
evidence, not resemblance to Northstar.
