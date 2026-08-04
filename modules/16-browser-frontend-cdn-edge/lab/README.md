# Northstar Browser–Edge Lab

This lab has two evidence planes:

- `browser_edge_lab/` is a deterministic repository model. It proves scenario
  shape, one-control pairs, hashes, target failures, and repaired invariants.
- the Node/React/Playwright harness runs a real Chromium against an origin and a
  deliberately small shared-cache proxy. It supplies browser behavior,
  accessibility, cache, trace, hydration, and throttling evidence for one pinned
  toolchain and host.

Neither plane is production CDN evidence. Preserve `test-results/` or exported
JSON under the learner's immutable A04 path and record host/load limitations.

## Route contract

| Route | Rendering | Cache authority | Interaction |
|---|---|---|---|
| `/sky-events` | static server HTML | public; normalized `x-region` variant | keyboard-operable filter |
| `/events/:id` | streamed server HTML | public, short freshness | streamed detail with recoverable failure marker |
| `/live` | cacheable shell plus client data | shell only; live JSON is `no-store` | status refresh |
| `/staff/schedule` | server HTML plus hydrated island | `private, no-store`; shared-cache bypass | authenticated schedule action |
| `/telemetry/snapshot` | test-only JSON | `no-store` | sanitized browser-edge-origin counters |

## Run

Use the Node version in `toolchains.lock.json`.

```bash
npm ci
npx playwright install chromium
npm test
python3 -m unittest discover -s tests -v
python3 -m browser_edge_lab scenarios/f05-public-cache-key-broken.json
```

The server binds to loopback only. `NORTHSTAR_PORT` may select the edge port;
the origin uses the following port. Test-only fault controls use the
`x-northstar-fault` header and are never a production pattern.

## Manual evidence

In addition to axe, execute keyboard-only focus order, visible focus, focus
restoration after filtering/error, 200% zoom/reflow, delayed content, and
JavaScript-disabled journeys. Record what was not tested with assistive
technology. For performance, preserve the network/device profile and repetitions;
do not compare lab timings directly with field percentiles.
