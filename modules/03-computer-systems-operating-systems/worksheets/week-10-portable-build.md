# Week 10 Portable Build

## Probe inventory

| Probe | Equivalent work/checksum | Bounds | Metrics | Tests |
|---|---|---|---|---|
| locality/branch | | | | |
| allocation/page touch | | | | |
| contention/false sharing | | | | |
| scheduler/syscall | | | | |
| buffered/durable I/O | | | | |

## Portability record

- C11/POSIX assumptions:
- macOS differences:
- Linux/cgroup differences:
- Unsupported counter behavior:
- Compiler optimization evidence:

## Safety review

- [ ] Inputs, memory, processes, time, and storage are bounded.
- [ ] Deadlock executes only in a watched child.
- [ ] Test containers are unprivileged, offline, and PIDs-limited.
- [ ] No global cache eviction or host kernel changes exist.
- [ ] Cleanup executes on success, timeout, and failure.
