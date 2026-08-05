# Messaging, Streams, and Workflows Lab

PESD 2.0 reuses the [shared three-node process/storage/fault boundary](../../../shared-labs/three-node-cluster/README.md)
for Modules 9–12. Connect publication, consumption, workflow, and reconciliation
mechanisms to the shared proxy without treating the fixture as graded evidence.

Before setup, run the repository [Home Lab Guide](../../../HOME_LAB_GUIDE.md)
preflight for `M11`.

This Python 3.11+ standard-library lab uses temporary SQLite databases and a
deterministic in-process log. It exposes authority/outbox commits, publication,
log positions, inbox/projection transactions, external effect identities,
workflow history, poison handling, event time, lag, and reconciliation.

It does not prove physical disk or broker durability, real-time availability,
production performance, regional survival, universal exactly-once effects, or
security enforcement.

Run one scenario from this directory:

```bash
python3 -m messaging_lab scenarios/f01-atomic-outbox-broken.json --pretty
```

Run all automated checks:

```bash
python3 -m unittest discover -s tests -v
```

The eighteen scenarios form nine strict same-input pairs. Trial JSON conforms
to `schemas/messaging-trial.schema.json` and contains hashes proving shared
workload/fault input and the one changed control. Learners freeze predictions
and scenario hashes, preserve raw output, then reproduce the observable
contract in their chosen stack or operated service.
