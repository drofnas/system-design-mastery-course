# Module 3 Systems Lab

Before setup, run the repository [Home Lab Guide](../../../HOME_LAB_GUIDE.md)
preflight for `M03`.

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
manifest. `validate` enforces the published contract, including aligned resource
samples, nonempty limitations, consistent summaries, nonnegative measures,
checksums, and I/O recovery observations. `--runtime native|docker` may override a scenario after all other
inputs have passed the same bounds.

## Evidence contract

Each trial records source commit, machine/kernel/architecture, compiler and flags,
filesystem, runtime/image, effective resource limits, raw samples, per-process
CPU/RSS/fault/context-switch/I/O counters, cgroup counters, throughput, useful
work, checksum, and limitations. Docker records both its Linux runtime and host
boundary. JSON contracts
are in `schemas/systems-scenario.schema.json` and `schemas/systems-trial.schema.json`.

Performance expectations are never test assertions. Tests require equivalent
work, valid checksums, bounded termination, and honest output.

The required matrix contains the 0.5/1/2 CPU quota sweep, 64/128/256 MiB
memory-limit sweep and retained OOM outcome, 16–256 MiB native working sets,
1/8/16-worker lock pairs, 64-worker oversubscription, direct/copy locality pair,
and equal-byte durability variants. Docker evidence includes `cpu.stat`, memory
events/current/peak, PIDs current/peak/events, and `io.stat`. These are trial
cgroup observations, not reserved-capacity guarantees.

Durable variants synchronize a temporary file, rename it, attempt to synchronize
the containing directory, and record whether the directory operation is
supported. The harness reopens the published path and verifies its byte count and
checksum. The injected-stop scenario halts after temporary-file synchronization
but before rename and verifies that the prior checkpoint remains published while
the temporary generation remains unpublished. This is a bounded process-boundary
experiment, not proof against kernel, VM, device, or host-power failure.

## Docker boundary

Docker trials use the official `gcc:15.2.0-bookworm` image with no network, a
read-only root, PIDs/CPU/memory limits, a 64 MiB temporary filesystem, and one
bounded writable trial directory. Learners may pin the resolved multi-architecture
digest in their environment record. Docker Desktop results include its Linux VM
and must not be described as native bare-metal storage results.

If `--runtime docker` overrides a native scenario, the harness applies defaults
of 1 CPU, 512 MiB, and 64 PIDs unless the scenario declares tighter limits.

## Safety

- Scenarios cap work, memory, workers, time, and storage.
- Deadlock runs in a child and passes only when the harness records its timeout.
- I/O contention is limited to two files and 1 GiB combined work.
- The lab never requests privileges, host networking, global cache eviction, or
  kernel-setting changes.
- Temporary artifacts are removed after every trial; preserve graded raw JSON in
  the independent submission directory, not inside this reference lab.
