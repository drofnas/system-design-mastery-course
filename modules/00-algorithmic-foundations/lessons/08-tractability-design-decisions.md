---
lesson_id: L08
title: "Tractability and Design Decisions"
---

# Tractability and Design Decisions

## Outcomes

- Explain P, NP, and why exact search can become unusable.
- Recognize scheduling, packing, placement, and routing warning signs.
- Choose an engineering response to intractability.

## Prerequisites

Algebra, comfort reading loops and arrays in any language, and the ability to separate a model from a measurement.

## Mechanism

Some problems grow so fast that exact search stops being a practical option.
The working skill is not proving complexity from scratch. It is recognizing when
a design hides a combinatorial search and replacing "just optimize it" with a
bounded decision strategy.

Common responses include approximation, heuristics, constraint relaxation,
decomposition, cached partial results, and human-approved exceptions.

### Recognizing hard search in design work

At a working level, P means problems with known polynomial-time algorithms. NP means proposed solutions can be checked in polynomial time. NP-hard problems are at least as hard as the hardest problems in NP; the practical warning is that exact search may grow explosively as options increase. You do not need a proof to be cautious when a design asks for every assignment, subset, coloring, route, or packing.

Common system-design shapes include bin packing for capacity placement, graph coloring for resource assignment without conflicts, set cover for replica or monitoring coverage, and vehicle-routing variants for scheduling. The engineering response is to preserve hard constraints, relax soft preferences, bound search time, use approximations where a ratio is known, use heuristics where measurement is honest, and define a fallback.

The decision artifact should name the safe region. For example: exact search for up to 12 shards, heuristic scoring beyond that, hard constraints never violated, and human approval when no candidate meets minimum capacity. That turns intractability from hidden latency into an explicit operating boundary.

### Repeatable technique

1. Count the candidate space before writing the optimizer.
2. Separate hard constraints from soft scores.
3. Pick exact, approximate, heuristic, or manual strategy by size.
4. Time-box the search and define fallback behavior.
5. Measure solution quality and record reversal evidence.

## Worked Example

Placing shards across regions while satisfying cost, latency, durability,
tenant, and capacity constraints can become a search problem. A practical system
usually narrows the candidate set, scores options, and records the accepted
tradeoff rather than enumerating every assignment.

## Common Expert Mistakes

- Treating an exponential search as a normal background job.
- Hiding constraints in code instead of naming them.
- Optimizing a score without preserving hard invariants.

## Guided Practice

A planner assigns 40 shards to 8 regions. Compute the naive candidate count as `8^40` in approximate powers of ten using `log10(8) ~= 0.903`. Then choose a bounded strategy that preserves hard data-residency constraints.

## Self-Check

1. What is the working difference between P and NP?
2. Why does bin packing show up in capacity placement?
3. What should happen when exact search exceeds its time box?
4. Why keep hard constraints separate from soft scores?

## Explained answers

1. P has known polynomial-time solutions; NP has efficiently checkable proposed solutions.
2. You are fitting work into finite bins while respecting capacity and placement limits.
3. Return a safe fallback, partial plan, or manual escalation rather than silently overrun.
4. A high score must not override correctness, residency, security, or durability requirements. For the practice, `log10(8^40) = 36.12`, about `1.3e36` candidates; use pruning, heuristics, and bounded search with residency as a hard filter.

## Sources And Next Work

Study RES-04 and RES-08. M01 is the natural next module after this one.
