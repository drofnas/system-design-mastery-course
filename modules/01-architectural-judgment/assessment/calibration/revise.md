# Calibration Fixture: Revise

## Simulated structural evidence

- G01–G06 pass.
- Baseline tag and artifacts are present and immutable.

## Journey and scope

Riders should receive alerts quickly so they can change plans. Operators can
create and revoke alerts. Predictive alerts are out of scope.

## Workload

The platform expects 500,000 riders, around 100 requests/second normally, and
“much higher” traffic during incidents. Growth is expected to be threefold.
No burst duration, operation mix, skew, projection date, or source is supplied.

## Invariants and quality

Ten invariant statements exist. Eight are testable. Two say “data is consistent”
and “the platform remains secure.” The submission identifies alert approval as
state owner but does not explain stale derived copies.

Targets include 99.9% availability and 300 ms latency. The population, window,
measurement location, overload response, and recovery target are incomplete.

## Failure review

The five required scenario names appear. The slow dependency review says a
circuit breaker and autoscaling prevent cascading failure. It does not state
dependency latency, shared finite resources, retry behavior, or queue bounds.
Zone loss states that another zone takes over without capacity or authoritative
acknowledgment evidence.

## Candidates and decision

Simple, moderate, and distributed candidates are described. The moderate option
wins a weighted table, but its ratings have little causal support. Infrastructure
cost appears; on-call, security operation, migration, and team coordination do
not. Reversal says “split further when scale requires it.”

## Defense and self-critique

The defense is understandable and preserves the submitted assumptions. It
admits that burst and recovery evidence is missing. The revision log assigns a
load model and failure tabletop but has not completed them.

