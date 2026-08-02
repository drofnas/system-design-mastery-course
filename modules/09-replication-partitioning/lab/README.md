# Replication and Partitioning Lab

This Python 3.11+ lab is a deterministic teaching model. It uses no database,
container, account, external package, or network. It exposes operation order,
replica versions, acknowledgements, session violations, conflict handling,
repair, placement movement, and load distribution. It does **not** establish
production latency, durability, consensus, data-residency compliance, or
regional-failure behavior.

From this directory, run one scenario:

```bash
python3 -m replication_lab scenarios/f01-replica-partition-broken.json --pretty
```

Run the automated checks:

```bash
python3 -m unittest discover -s tests -v
```

The twelve scenarios form six strict pairs. Each pair has identical topology,
workload, seed, and fault input; only the named control differs. Trial JSON
conforms to `schemas/replication-trial.schema.json` and includes hashes proving
the shared input and changed configuration.

Learners must freeze predictions and scenario hashes before execution, preserve
raw JSON, then reproduce the observable contract in their chosen stack or an
operated database. Any transfer claim must name which evidence came from this
model and which came from the chosen environment.
