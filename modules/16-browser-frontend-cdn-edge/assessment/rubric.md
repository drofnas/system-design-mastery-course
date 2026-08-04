# Module 16 Anchored Rubric

## R01: Browser mechanism and causal diagnosis

- **0:** the model reverses required ordering or recommends a repair that keeps a critical long task.
- **1:** event-loop and rendering vocabulary without a trace or causal chain.
- **2:** the main task-to-paint chain is plausible but thread placement, checkpoints, or alternatives are weak.
- **3:** tasks, microtasks, input, style, layout, paint, raster, and compositing align with evidence and limits.
- **4:** counter-evidence distinguishes scheduling, rendering, and resource bottlenecks under changed conditions.

## R02: Performance budgets and evidence

- **0:** invented measurements or a lab result is presented as universal field performance.
- **1:** target numbers without route, population, percentile, conditions, or ownership.
- **2:** useful budgets exist but decomposition, lab/field separation, or statistical limits are weak.
- **3:** route milestones, critical bytes/requests, interaction components, conditions, percentiles, and owners align.
- **4:** repeated and field evidence falsifies alternatives and changes a bounded budget or design decision.

## R03: Rendering and hydration strategy

- **0:** personalized content is exposed or hydration semantics remain knowingly incorrect.
- **1:** one rendering label is applied globally without route evidence.
- **2:** routes differ, but state identity, failure recovery, streaming commitment, or JavaScript-off behavior is weak.
- **3:** each route's static/server/streaming/client/island choice follows content, interaction, cache, and recovery evidence.
- **4:** measured migration slices and reversal evidence validate the seams without prescribing a universal framework.

## R04: Public-cache correctness

Safety-critical because an incomplete key or invalid freshness policy can serve
the wrong representation or authority.

- **0:** repaired evidence can return the wrong public representation or bypass required invalidation.
- **1:** cache headers exist without key dimensions, validator, authority, or purge ownership.
- **2:** main keys and freshness work but normalization, validation, failure, or version evidence is weak.
- **3:** eligibility, key, freshness, validation, invalidation, versions, and bounded stale behavior agree.
- **4:** poisoning, variant explosion, purge delay, and origin-failure tests preserve correctness and quantify cost.

## R05: Personalization and edge safety

Safety-critical because shared storage or trusted browser identity can disclose
staff data across sessions.

- **0:** personalized staff content enters shared storage, crosses sessions, or trusts client authority.
- **1:** `private` or `no-store` is asserted without two-session and cache-decision evidence.
- **2:** normal requests isolate sessions but stale, retry, fallback, telemetry, or BFF boundaries are weak.
- **3:** subject binding, private bypass, fail-closed behavior, sanitized context, and two-session evidence agree.
- **4:** mixed-version, replay, origin-failure, and operational audit evidence preserve the boundary.

## R06: Accessibility and resilient interaction

Safety-critical because automated rules alone cannot prove that the critical
journey is perceivable, operable, understandable, or robust.

- **0:** a required action is keyboard-inoperable, focus is lost, or repaired evidence retains a critical violation.
- **1:** an automated score is the only evidence.
- **2:** automation and a happy keyboard path pass, but semantics, error recovery, zoom, focus, or tool limits are weak.
- **3:** semantics, name/role/value, keyboard, visible focus, order, errors, automation, and manual limits agree.
- **4:** disabled-script, delayed-content, zoom/reflow, and assistive-technology evidence changes the design.

## R07: Memory and third-party governance

- **0:** repaired evidence retains unbounded resources or a third party can block the critical journey without containment.
- **1:** heap or vendor labels without identities, repetitions, policy, owner, or exit.
- **2:** a leak or dependency is measured, but cleanup/failure attribution, privacy, budget, or removal conditions are weak.
- **3:** stable identities, repeated deltas, cleanup, isolation, admission budget, fallback, owner, and removal policy align.
- **4:** sustained-navigation and dependency-failure evidence validates containment under multiple routes and conditions.

## R08: Browser-edge-origin observability

- **0:** sensitive identity is propagated or untrusted browser context controls authorization or sampling authority.
- **1:** trace IDs exist without parentage, validation, sanitization, sampling, or cost.
- **2:** correlation works but trust boundaries, cardinality, retention, missing spans, or accessibility signals are weak.
- **3:** sanitized browser-edge-origin context, owners, sampling, cost, privacy, and evidence limitations align.
- **4:** broken-context, sampled-out, retry, and partial-telemetry tests preserve diagnosis without overstating certainty.

## R09: Failure-evidence integrity

Safety-critical because changed inputs or rewritten trials can manufacture a
browser or edge conclusion.

- **0:** chronology/evidence is altered or any repaired target remains failed.
- **1:** conclusions lack predictions, hashes, pairs, conditions, or raw limitations.
- **2:** most pairs work but one-control isolation, toolchain identity, repetitions, or causal alternatives are weak.
- **3:** F01–F08 predictions, paired hashes, targets, repairs, invariants, raw trials, and limitations agree.
- **4:** independent repetitions and falsification narrow the claim while preserving every frozen artifact.

## R10: Architecture leadership

- **0:** decision leaves a critical boundary unowned or mandates an unsafe/unreversible migration.
- **1:** framework or CDN preference without route drivers, alternatives, or obligations.
- **2:** useful RFC with weak security, operations, accessibility, cost, migration, ownership, dissent, or reversal.
- **3:** per-route decisions, boundaries, evidence, alternatives, owners, migration, rollback, stops, defense, and revision align.
- **4:** the frozen role-based transfer exercise applies the method to a
  different route and the resulting dissent improves the decision. Optional
  team review upgrades attestation, not score.

## Thresholds

Pass requires every G01–G06 gate, every A01–A11 artifact, average ≥3.0, and no
zero in R04–R06 or R09. G02–G05 failure or a safety-critical zero yields Repeat;
other material gaps yield Revise.
