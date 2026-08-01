# Module 5 Hybrid Network Lab

The lab exposes two different evidence boundaries:

1. `trace` measures a real unprivileged loopback path: a UDP DNS message, TCP/TLS
   setup, edge proxy, application, dependency, response, certificate validation,
   and cleanup.
2. `simulate` runs a deterministic event model for delay, jitter, bandwidth,
   loss, reordering, pool pressure, and shared-versus-per-stream ordering.

Never call modeled events packet captures or production benchmarks. Loopback
does not measure a carrier, router, NAT, public DNS, public CA, HTTP/2 stack, or
QUIC implementation.

## Requirements

- Python 3.11+
- an OpenSSL-compatible CLI supporting `req -addext`
- permission to bind ephemeral TCP and UDP ports on `127.0.0.1`

No package installation, root, container, or external service is required.

## Quick start

From this directory:

```bash
python3 -m network_lab validate scenarios/transit-baseline.json
python3 -m network_lab trace scenarios/transit-baseline.json --output /tmp/transit-trace.json
python3 -m network_lab simulate scenarios/transit-loss.json --output /tmp/transit-h2-loss.json
python3 -m network_lab simulate scenarios/transit-loss-quic.json --output /tmp/transit-h3-loss.json
python3 -m network_lab analyze /tmp/transit-h2-loss.json /tmp/transit-h3-loss.json
python3 -m unittest discover -s tests
```

Output paths belong outside the repository or in learner submission directories.
The lab never writes certificates into the repository.

## Commands

- `trace SCENARIO [--output PATH]`: run a measured loopback trial. Only baseline,
  reset, DNS-failure, and slow-reader scenarios use this mode.
- `simulate SCENARIO [--output PATH]`: run the deterministic protocol model.
- `validate PATH`: validate a scenario contract before work begins.
- `analyze TRIAL...`: summarize total timing and statuses without replacing raw evidence.
- `blind-prepare SCENARIO_DIR OUTPUT_DIR --seed N`: create shuffled evidence
  bundles and hashes. Move `reveal-key.json` out of view before diagnosis.
- `blind-reveal BUNDLE_DIR DIAGNOSIS OUTPUT`: require and hash a frozen diagnosis,
  verify bundles, and produce a reveal record.

## Required scenario matrix

| Fault | Evidence kind | Primary evidence |
|---|---|---|
| delay | model | added path delay and stream completion |
| jitter | model | seed, arrival variation, repeated output |
| loss | model | recovery event and shared/per-stream completion |
| reordering | model | arrival order and delivery boundary |
| bandwidth | model | serialization, bytes, and useful goodput |
| reset | measured loopback | completed phases, no useful response, cleanup |
| DNS failure | measured loopback | SERVFAIL, no connection, cleanup |
| slow reader | measured loopback | added client read hold time |
| pool exhaustion | model | limit, peak, wait, and bounded rejection |

For loss, compare the H2/TCP and H3/QUIC scenarios with the same seed, path,
bytes, and loss identity. The model isolates ordering; it does not implement the
complete standards.

## Blind workflow

1. Copy only the required simulate scenarios into a bounded temporary directory.
2. Run `blind-prepare`, then have a facilitator retain `reveal-key.json`.
3. Diagnose each bundle using the Week 19 worksheet and freeze it in version control.
4. Run `blind-reveal` with the frozen diagnosis path.
5. Preserve the reveal record and run discriminating scenarios after reveal.

Inspecting scenario names or the reveal key before freeze invalidates R06.

## Security and cleanup

- The certificate and private key are generated in a temporary directory, have
  a one-day validity, and are deleted when the trace exits.
- The client validates both the generated trust anchor and
  `impact.transit.test`; disabling verification is not supported.
- Do not add packet payloads, hostnames containing user data, credentials, or
  production endpoints to scenarios.
- Every server binds loopback only, uses bounded input, and closes after one trial.

## Troubleshooting

- `openssl failed`: confirm the CLI supports `-addext`; record a substitution
  only if it preserves SAN hostname validation and ephemeral keys.
- `operation not permitted`: allow loopback binding; do not switch to a public interface.
- nondeterministic simulation: preserve the same scenario bytes and seed.
- timing variation: loopback wall-clock values are wiring evidence; repeat and
  report distributions rather than treating them as normative performance.
