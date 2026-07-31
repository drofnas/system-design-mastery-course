# Module 3 Systems Lab

The lab exposes observable mechanisms; it is not a hardware-ranking suite.

## Requirements

- Python 3.11+
- C11 compiler and `make`
- Docker for scenarios whose `runtime` is `docker`

## Commands

From this directory:

```bash
make test
PYTHONPATH=. python3 -m systems_lab run \
  --scenario scenarios/locality-contiguous.json \
  --output build/locality-contiguous.json
PYTHONPATH=. python3 -m systems_lab validate build/locality-contiguous.json
make matrix
make sanitize
```

`run` executes one scenario. `matrix` executes the ordered scenario paths in a
manifest. `validate` checks evidence structure, nonnegative measures, and checksum
agreement. `--runtime native|docker` may override a scenario after all other
inputs have passed the same bounds.

## Evidence contract

Each trial records source commit, machine/kernel/architecture, compiler and flags,
filesystem, runtime/image, resource limits, raw samples, CPU/RSS/fault/context
switch or cgroup counters, useful work, checksum, and limitations. JSON contracts
are in `schemas/systems-scenario.schema.json` and `schemas/systems-trial.schema.json`.

Performance expectations are never test assertions. Tests require equivalent
work, valid checksums, bounded termination, and honest output.

## Docker boundary

Docker trials use the official `gcc:15.2.0-bookworm` image with no network, a
read-only root, PIDs/CPU/memory limits, a 64 MiB temporary filesystem, and one
bounded writable trial directory. Learners may pin the resolved multi-architecture
digest in their environment record. Docker Desktop results include its Linux VM
and must not be described as native bare-metal storage results.

## Safety

- Scenarios cap work, memory, workers, time, and storage.
- Deadlock runs in a child and passes only when the harness records its timeout.
- I/O contention is limited to two files and 1 GiB combined work.
- The lab never requests privileges, host networking, global cache eviction, or
  kernel-setting changes.
- Temporary artifacts are removed after every trial; preserve graded raw JSON in
  the independent submission directory, not inside this reference lab.
