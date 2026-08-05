# Time, Coordination, and Consensus Lab

PESD 2.0 reuses the [shared three-node process/storage/fault boundary](../../../shared-labs/three-node-cluster/README.md)
for Modules 9–12. The consensus-specific virtual clock, crashable store,
fencing fake, and oracle extend that common boundary.

Before setup, run the repository [Home Lab Guide](../../../HOME_LAB_GUIDE.md)
preflight for `M10`.

This Python 3.11+ standard-library lab is a deterministic logical-tick teaching
model. It exposes clocks, terms, votes, logs, commitment/application, client
deduplication, read barriers, fencing, snapshots, and membership. It does not
prove disk durability, real-time availability, network bounds, Byzantine
tolerance, production performance, security enforcement, or regional survival.

PESD 2.0 drives the learner node through `VirtualClock`,
`DeterministicNetwork`, and `CrashableStore`. The protected-resource fake owns
fencing independently of the node. `InvariantOracle` derives C01–C10 from the
history and final state; scenario IDs and expected-result fields cannot select
an outcome. Eight generated same-tick schedules exercise reorderings, and the
small-state checker searches reconfiguration quorums for a split-decision
counterexample. Mutation tests must fail when persistence, commit-before-reply,
log validation, deduplication, read barriers, fencing, atomic snapshot
activation, or joint consensus is removed.

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

The reference node is an inspectable contract, not a capstone answer. Learners
implement the mechanisms inside their own node boundary and run the unchanged
driver, schedules, oracle, protected-resource fake, and mutation suite against
that code. A scenario fixture may supply stimuli but cannot satisfy independent
Build or Break evidence by itself.
