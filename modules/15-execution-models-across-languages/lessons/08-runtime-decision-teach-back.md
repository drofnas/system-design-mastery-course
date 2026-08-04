lesson_id: L08

# Runtime Decision and Teach-back

## Outcomes

Choose a runtime from evidence, plan adoption or no-change safely, and teach the
method without presenting a language ranking.

## Prerequisites

Completed A01–A07 and RES-06.

## Mechanism and method

A runtime decision is a workload, operating model, and team decision. A small
latency difference may be irrelevant beside memory safety, diagnostic maturity,
dependency support, build latency, licensing, hiring, incident response, or
migration risk. Conversely, familiarity does not excuse a failed invariant.

Use **DRIVER**: define user and business outcomes; rank workload and failure
drivers; inventory runtime and ecosystem evidence; validate operations,
security, cost, ownership, and migration; expose dissent and uncertainty;
record stopping and reversal conditions.

Compare at least “keep current runtime,” “adopt for this bounded capability,”
and “adopt more broadly.” Include training, build/release, observability,
dependency, incident, security response, and rollback work. Prefer a reversible
seam and shadow comparison when runtime change is justified. A rewrite is not a
performance experiment unless equivalent behavior and migration risk are visible.

## Worked example

Northstar's Rust trial uses less measured memory under F04, while Java has the
fastest team-approved operational path and meets every SLO with headroom. The
decision keeps Java for the gateway, adopts Rust only for a bounded calibration
codec where memory pressure matters, and schedules a canary with wire-compatible
rollback. Reversal triggers include p95 latency, peak memory, build time,
security patch lead time, on-call coverage, and defect escape rate. Discord's
historical case informs questions about allocation and migration but does not
select Northstar's runtime.

## Common expert mistakes

- Turning one benchmark into a universal “fastest language” claim.
- Ignoring the no-change option and transition costs.
- Treating type safety as a replacement for authorization, recovery, or tests.
- Naming a team owner without on-call, review, training, and succession evidence.

## Guided practice

Deliver a ten-minute review: two minutes on workload and invariants, three on
execution evidence, two on operations/security/cost, two on migration and
reversal, and one on uncertainty. Use the frozen solo-review packet to challenge
a metric, failure, team dependency, and boundary. Record what changed. A live
panel is optional.

## Self-check

1. When is “do not migrate” the stronger engineering decision?
2. What makes a runtime experiment reversible?
3. What proves a teach-back worked?

## Explained answers

1. When the current runtime meets outcomes and the expected benefit does not
   exceed transition, ecosystem, operational, and ownership costs.
2. A stable interface, isolated state/effects, comparable shadow evidence,
   staged cutover, compatible data, and tested rollback or roll-forward.
3. Another engineer can apply the causal method to a different workload, and
   review questions or dissent produce traceable clarification or change.

## Sources and next work

Use RES-06 only with its historical boundary. Complete the ADR, defense, module
assessment, and [Gate 5](../assessment/gate-05.md).
