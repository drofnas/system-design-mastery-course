# Calibration Fixture: Repeat

## Simulated structural evidence

- G01 passes.
- G02 fails: no `week-01-baseline` tag exists and the baseline remains `draft`.
- Week 3 failure review and defense record are absent.

## Proposal

Use regional microservices, a distributed database, and event streaming because
the transit platform must scale and never go down.

## Workload

The system has millions of users and must support unlimited traffic.

## Correctness

The database provides consistency. Operators authenticate through single
sign-on. Notifications are eventually consistent.

## Quality

- Fast responses
- Five nines availability
- Secure access
- Instant recovery

## Failure

If a service fails, traffic goes to another instance. If a region fails, traffic
goes to another region. Retries prevent data loss.

## Decision

Distributed architecture is more future-proof and is industry best practice.
The additional cost is worth the scalability. The design can be changed later
if needed.

