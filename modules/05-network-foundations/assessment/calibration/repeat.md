# Transit Signal Repeat Fixture

## Submission identity

Artifact commit `fixture-m05-repeat`; claimed baseline
`fixture-m05-repeat-baseline`. Environment and assistance are not recorded.

## Unfrozen model

The path worksheet was edited after results to match the observed total. There
is no preserved pre-collection hash or separate revision.

## Network claims

The submission says “DNS passed, so the network was healthy” and “HTTP/3 removes
packet loss.” It lists no client population, units, trust boundary, pool limit,
or useful-work check.

## Revealed scenarios

Scenario filenames were opened before the diagnosis matrix. Raw bundles and
reveal hashes are absent. Only loss and DNS failure are mentioned; both are
named from source rather than evidence.

## TLS and safety

The client disables certificate verification to connect. A reusable private key
is pasted into the report, servers bind all interfaces, and cleanup/resource
limits are not recorded.

## Decision

The conclusion is “switch everything to HTTP/3.” There are no alternatives,
costs, owners, fallback, migration, rollback, reversal conditions, defense, or
separate remediation artifacts.
