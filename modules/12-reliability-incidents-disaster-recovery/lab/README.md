# Reliability, Incidents, and Disaster Recovery Lab

This Python 3.11+ standard-library lab models deterministic journey events,
budget windows, alerts, degradation, incident coordination, backup/restore,
regional capacity, authority epochs, failback, reconciliation, and operator
safety. Its public CLI is:

```bash
python3 -m reliability_lab scenarios/f01-slow-dependency-load-broken.json --pretty
```

Run all checks with:

```bash
python3 -m unittest discover -s tests -v
```

The eighteen scenarios form nine strict same-input broken/repaired pairs. Trial
JSON conforms to `schemas/reliability-trial.schema.json` and includes hashes for
the full scenario, shared workload/fault input, and controls. Learners freeze
predictions and hashes, preserve raw output, then reproduce the observable
contract in their chosen stack or safe operated environment.

The model does not prove production availability or latency, physical backup
durability, provider control-plane independence, real regional isolation, human
performance under stress, security enforcement, or regulatory compliance.
