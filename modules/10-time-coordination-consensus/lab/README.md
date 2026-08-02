# Time, Coordination, and Consensus Lab

This Python 3.11+ standard-library lab is a deterministic logical-tick teaching
model. It exposes clocks, terms, votes, logs, commitment/application, client
deduplication, read barriers, fencing, snapshots, and membership. It does not
prove disk durability, real-time availability, network bounds, Byzantine
tolerance, production performance, security enforcement, or regional survival.

Run one scenario from this directory:

```bash
python3 -m consensus_lab scenarios/f01-leader-termination-broken.json --pretty
```

Run all automated checks:

```bash
python3 -m unittest discover -s tests -v
```

The sixteen scenarios form eight strict same-input pairs. Trial JSON conforms
to `schemas/consensus-trial.schema.json` and contains hashes proving shared
fault/workload input and the changed control. Learners freeze predictions and
scenario hashes, preserve raw output, then reproduce the observable contract in
their chosen stack or operated service.
