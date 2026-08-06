---
lesson_id: L08
title: "Causal Decisions, Validation, and Teach-Back"
---

# Causal Decisions, Validation, and Teach-Back

## Outcomes

- Connect a user outcome to code, resource behavior, and controlled evidence.
- Include operations, security, cost, ownership, migration, and reversal.
- Teach the causal model under adversarial questioning.

## Prerequisites

Lessons 1–7 and one completed blind diagnosis.

## Mechanism and method

A performance review is a decision record with an evidence chain:

```text
user outcome -> bounded observation -> mechanism -> alternatives
             -> discriminating test -> equivalent change -> validation
             -> rollout, owner, budget, and reversal
```

Start with the question and cite raw evidence. Separate what happened
from why. State confidence and remaining uncertainty. Then cover the consequences
of owning the change: collection cost, privacy, retention, on-call response,
capacity under failure, migration from existing instrumentation, rollback, and
the evidence that reverses the decision.

The teach-back must preserve the submitted workload and failure model. A reviewer
may challenge assumptions, but changing them mid-defense creates a new claim
that needs new evidence.

## Worked example

Transit accepts a normalization optimization only after the response checksum,
branch count, process CPU, profile attribution, server spans, and p95 move as
predicted in an interleaved validation. The rollout owner watches journey p95,
error mix, CPU headroom, and telemetry overhead. A production profile that moves
the hot path elsewhere reverses the decision.

## Common expert mistakes

- **Lead with the patch:** reviewers cannot judge whether it solves the user
  problem.
- **Collapse correlation into cause:** alternatives and falsifiers disappear.
- **Ignore telemetry as production code:** cost, privacy, and failure modes remain
  unowned.
- **Claim universal improvement:** workload and environment boundaries vanish.

## Guided practice

Complete EX-14 and EX-15. Use the scripted solo-review packet to challenge the
strongest assumption, answer without live AI, record the evidence needed to
resolve disagreement, and save the responses. That record completes the solo
teach-back. A human reviewer or provider-neutral LLM may critique the record
afterward as optional stronger practice evidence.

## Self-check

1. What separates a performance report from a chart collection?
2. Why name migration for instrumentation?
3. What should happen when a reviewer changes the workload?

## Explained answers

1. A falsifiable causal model, alternatives, discriminating test, validated
   decision, and reversal conditions.
2. Signal names, labels, retention, dashboards, and owners are interfaces; an
   unsafe cutover can blind operators or duplicate cost.
3. Record it as a new scope and experiment. Do not pretend the submitted evidence
   already covers it.

## Failure-mode bridge to the lab

The final lab move is not "find the slow thing." It is turning a diagnosis into
a decision that another engineer can challenge. A causal decision names the
claim, the evidence that supports it, the evidence that weakens alternatives,
the change to try, the rollback condition, and the limitation that still remains.

Blind diagnosis practice strengthens this because it delays the mapping between
scenario name and expected answer. When you reveal the mapping, score more than
whether the final label matched. Check whether your matrix preserved the user
question, separated symptom from cause, named falsifiers, and avoided claims
outside the local evidence. A wrong but well-bounded diagnosis is useful; an
overconfident right answer is a liability when the real system changes shape.

## Second worked example

Suppose the diagnosis says a candidate regression is caused by lock contention.
The decision should not be "remove locking." It should say which lock, which
critical section, which invariant the lock protects, and which alternative keeps
that invariant intact. A valid next step might shorten the critical section,
split read and write paths, or move non-authoritative work outside the lock. The
rollback condition might be duplicate effects, invariant violation, or a tail
latency budget miss. That is the difference between a fix and a bet.

## Decision checklist

Write claim, supporting evidence, weakened alternatives, chosen change,
rollback trigger, owner, and evidence limit. Then ask what new observation would
make you change your mind.

## Module synthesis

Across the module, the pattern is deliberately repetitive: question, preserve
work, compare, falsify, decide. Traces, metrics, logs, profiles, benchmark
summaries, and query plans are different instruments for that loop. None of them
gets to outrank the user-visible outcome or the preserved-work condition. When
you carry this module into later systems work, use observability to reduce
uncertainty before a decision, not to decorate a decision that was already made.

## Sources and next work

- USENIX, [The Art of Performance Monitoring](https://www.usenix.org/conference/srecon16/program/presentation/smith).
- OpenTelemetry, [Specification overview](https://opentelemetry.io/docs/specs/otel/overview/).
- Next: complete the performance review and defense.
