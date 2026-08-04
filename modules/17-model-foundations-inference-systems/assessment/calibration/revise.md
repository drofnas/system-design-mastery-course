# Atlas Revise Calibration Fixture

## Identity and frozen chronology

A01–A11 and four logs exist; predictions and pair hashes predate trials. Evidence
kind and source commit are present, but CPU host power mode and two repetition
identities are missing.

## Mathematics, model, and capacity

Tensor shapes, causal attention, stable softmax, and generation tests pass. The
capacity model includes weights and KV but treats runtime overhead and headroom
as fixed percentages, omits maximum output sensitivity, and divides cost by all
generated tokens including discarded results.

## Measurement and serving controls

TTFT and ITL include queue time and the mixed workload is repeated, but warm-up,
profiler overhead, generator lag, and per-tenant tails are incomplete. The queue
is bounded and memory is reserved, yet batch minimum share and authenticated
priority ownership are only asserted. Recovery after shedding is not measured.

## Cache, precision, and provider safety

Exact cache keys include tenant and main versions; semantic threshold provenance,
authorization-change invalidation, and a second mixed-version trial are missing.
Precision evidence reports average logit error and task score but not worst protected
case or a tested rollback. Provider attempts share a deadline, but fallback
capacity, partial-stream behavior, and regional data boundary are qualitative.

## Failures and architecture leadership

F01–F06 have matching hashes and repaired targets, but F02 and F06 lack a repeated
same-work run and credible alternative cause. The RFC compares three candidates
and names serving/model owners, while security review ownership, decommission
criteria, cost sensitivity, strongest dissent, and quantified reversal remain weak.
