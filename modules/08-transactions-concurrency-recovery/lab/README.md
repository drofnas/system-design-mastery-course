# Transaction and Recovery Lab

This Python 3.11+ standard-library lab exposes deterministic transaction
schedules, shared/exclusive locks, MVCC validation, WAL ordering, explicit flushes, crash recovery,
backup, and point-in-time restore. It executes real local file writes and
`fsync`, but it is a teaching engine: it does not prove production database,
device-cache, kernel, distributed, or cloud durability.

Run one paired scenario from this directory:

```bash
python3 -m transaction_lab run \
  --scenario scenarios/f01-lost-update-broken.json \
  --output /tmp/f01-broken.json
```

The `restore` command accepts a backup directory created by `ToyStore.backup`,
a WAL path, and an inclusive target LSN. Trials conform to
`schemas/transaction-trial.schema.json` and include shared-input and control
hashes. Preserve scenarios, predictions, raw trials, environment labels, and
hashes before interpretation.

Run the tests:

```bash
python3 -m unittest discover -s tests -v
```

Tests include a real subprocess that terminates with a stolen uncommitted
update, plus shared-flush group commit and target-LSN restore. The required
matrix is F01–F07, each with broken and repaired variants. A pair
must share logical input and change only the named control. The learner should
reproduce the contract in a chosen stack; PostgreSQL translation is optional.
