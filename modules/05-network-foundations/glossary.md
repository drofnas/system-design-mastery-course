# Module 5 Glossary

- **Bandwidth-delay product:** bytes that can be in flight on a path at a given bandwidth and round-trip time.
- **Congestion control:** sender behavior that limits offered traffic in response to path capacity and congestion evidence.
- **DNS authority:** server responsibility for data in a zone; not a claim that an endpoint is healthy.
- **Flow control:** receiver-advertised limit that prevents a sender from overrunning receive capacity.
- **Goodput:** useful application bytes completed per unit time, excluding protocol overhead and retransmission.
- **Head-of-line blocking:** later useful work waiting behind missing or unfinished earlier work at an ordering boundary.
- **Jitter:** variation in packet or request delay, not merely a high average.
- **NAT state:** time-bounded address/port translation state owned by a network device.
- **Path:** ordered set of resolution, transport, trust, proxy, application, and dependency boundaries for one operation.
- **Round-trip time:** elapsed time for a signal to reach a peer and a response to return at a named boundary.
- **Slow reader:** receiver that consumes bytes slowly enough to constrain send progress or retain resources.
- **Stream:** independently identified ordered byte sequence inside a multiplexed transport or application connection.
- **Tail latency:** high-percentile completion time for a specified workload and observation boundary.
- **Trust anchor:** configured root of certificate validation, distinct from the certificate presented by a peer.
