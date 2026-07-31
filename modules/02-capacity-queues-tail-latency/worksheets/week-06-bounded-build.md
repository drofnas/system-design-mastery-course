# Week 6 Worksheet: Bounded Build Review

## Public contract

- Scenario schema:
- Trial schema:
- Commands:
- Runtime and dependency assumptions:

## Bound inventory

| Resource or wait | Bound | Rejection/expiry | Metric | Owner |
|---|---:|---|---|---|
| Service workers | | | | |
| Waiting queue | | | | |
| Fan-out | | | | |
| Downstream concurrency | | | | |
| Attempts/request | | | | |
| Shared retry work | | | | |
| Trial duration/request count | | | | |

## Timing and identity

- Logical request identity:
- Attempt identity:
- Scheduled/sent/admitted/start/completed timestamps:
- Monotonic clock:
- Useful throughput rule:

## Tests

- [ ] Stable low load
- [ ] Queue-full rejection
- [ ] Worker and downstream concurrency bounds
- [ ] Retry-budget exhaustion
- [ ] Open-loop scheduling and generator lag
- [ ] Seeded slow/failure decisions
- [ ] Invalid configuration rejection
- [ ] Trial-summary contract

## Build freeze

- Commit:
- Known limitations:
- AI assistance and verification:
