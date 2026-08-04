lesson_id: L07

# Northstar Browser-Edge Tutorial

## Outcomes

- Apply the route, cache, accessibility, telemetry, and failure procedures together.
- Run deterministic scenarios separately from measured Chromium observations.
- Preserve hashes and evidence boundaries for broken/repaired comparisons.

## Prerequisites

Complete Lessons 1–6 and EX-01–EX-17. Freeze the independent commerce baseline
before using this completed Northstar tutorial.

## Mechanism: one route contract must agree across layers

Northstar uses five linked contracts:

1. **Route policy:** authority, rendering placement, useful HTML, interaction,
   freshness, personalization, and failure behavior.
2. **Wire policy:** status, cache headers, content type, trace context, and version.
3. **Browser policy:** hydration root, tasks, resource ownership, accessibility,
   performance marks, and cleanup.
4. **Edge policy:** normalized key, lookup/store eligibility, validation, bounded
   stale behavior, and sanitized telemetry.
5. **Evidence policy:** frozen input/config hashes, one changed control, toolchain,
   observations, invariant results, limitations, and immutable output.

The deterministic model is a contract oracle for I01–I10. It does not execute
React or Chromium. The measured harness verifies selected browser and HTTP
behavior on the pinned toolchain. Agreement between them is stronger evidence;
neither substitutes for production field or CDN data.

## Worked example

Start the lab and inspect:

- `/sky-events`: static public list, language-aware shared key, five-minute shared freshness.
- `/events/event-1`: streamed event shell plus bounded regional weather region.
- `/live`: reusable semantic shell plus deadline-bound client status.
- `/staff/schedule`: subject-bound HTML, `private, no-store`, hydrated edit island.
- `/telemetry/snapshot`: test-only counts and sanitized correlation fields.

For F05, both variants use the same event version, language requests, seed,
network profile, and toolchain. The only control is `complete_public_cache_key`.
The broken model returns the English object for Spanish; I05 fails. The repaired
model creates two bounded keys and every invariant passes. Browser evidence then
checks response language, cache outcome, content version, and `Age` behavior.

For F06, the only changed control is `private_cache_bypass`. Two pseudonymous
sessions request `/staff/schedule`. Broken evidence shows a shared-cache hit with
the wrong subject binding; repaired evidence shows two origin responses and zero
private cache entries. No real identity or session secret appears in fixtures.

For F01, the deterministic trial predicts I01 from injected main-thread work.
The browser trial records a PerformanceObserver long-task entry and the controlled
interaction milestone. It labels the result `lab_interaction_ms`, never `field_inp`.

## Common expert mistakes

- **Using model timing as browser timing.** Deterministic values test policy logic,
  not CPU, network, parser, layout, or paint behavior.
- **Changing input with the repair.** Smaller data or faster network destroys the
  causal pair even when the output looks better.
- **Freezing interpreted reports but not raw evidence.** Preserve raw trial JSON,
  environment, and hashes before writing the explanation.
- **Letting telemetry endpoints become production interfaces.** The snapshot is
  loopback/test-only and contains no raw session authority.

## Guided practice

Before running the provided pairs, select F01, F05, and F06. Write target
invariant, expected broken observation, single repair control, possible
alternative cause, and tool limitation. Run deterministic tests, then the
measured harness, and compare prediction with observation.

## Self-check

1. Why keep a deterministic model when a browser test exists?
2. Which hashes must match within a pair?
3. What evidence may differ between deterministic and browser runs?
4. Why use pseudonymous sessions in F06?

## Explained answers

1. It provides fast, platform-independent contract checks and exact invariant
   coverage while the browser test exposes implementation behavior.
2. Shared logical input, seed, route/workload, and declared environment/config
   dimensions other than the single control.
3. Real timings, heap/GC behavior, browser scheduling, and implementation-specific
   traces; invariant semantics and useful work should agree.
4. They prove isolation without introducing personal data or reusable authority.

## Sources and next work

Use the [lab guide](../lab/README.md) and completed
[Northstar case](../case-study/northstar-sky-portal.md). Preserve all raw evidence
before preparing A03–A06.
