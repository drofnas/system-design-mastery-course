# Shared Three-Node Local Cluster

Modules 9–12 reuse this one process/storage/fault boundary. It starts exactly
three standard-library worker processes, gives each node an isolated storage
directory, and routes messages through an unprivileged in-process proxy that can
delay, drop, and reorder envelopes. It never changes host firewall rules,
requires root, or pretends to be a regional network.

```bash
python3 -m unittest discover -s shared-labs/three-node-cluster/tests -v
```

Learner labs may wrap the workers with replication, consensus, messaging, or
recovery mechanisms, but they must preserve the proxy and storage evidence
boundary. Record source commit, scenario/configuration hashes, Python/runtime,
per-node storage hashes, process identities without host-private data, virtual
clock, resource limits, raw events, and limitations. Run one cluster and one
fault scenario at a time on low-resource machines.

The proxy is deterministic mechanism evidence. It does not prove WAN latency,
kernel packet behavior, zone independence, disk durability, or provider control-
plane behavior. Fixture output is practice only until the learner's mechanism is
connected and independently broken.
