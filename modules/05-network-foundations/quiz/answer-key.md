# M05 Quiz Answer Key

This key covers all 18 questions for **Network Foundations**. Use it after an attempt, or provide it with the LLM grading prompt for feedback.

## M05-Q001

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** BDP describes path volume; sender windows, receiver flow control, congestion, loss, and application pacing can prevent filling it.

**Explanation:** M05-Q001 uses self-check 1 from Request Paths, Round Trips, and Byte Budgets; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M05-Q002

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** Only when the implementation starts independent work concurrently and the critical path does not wait for both sequentially.

**Explanation:** M05-Q002 uses self-check 2 from Request Paths, Round Trips, and Byte Budgets; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M05-Q003

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** Each phase p95 may come from a different request; dependence and correlation determine the journey tail.

**Explanation:** M05-Q003 uses self-check 3 from Request Paths, Round Trips, and Byte Budgets; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M05-Q004

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** It does not prove route reachability, TLS identity, proxy capacity, or service health.

**Explanation:** M05-Q004 uses self-check 1 from DNS, Addressing, Routing, and Discovery; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M05-Q005

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** NXDOMAIN is an authoritative nonexistence result; timeout lacks a response and is temporary uncertainty.

**Explanation:** M05-Q005 uses self-check 2 from DNS, Addressing, Routing, and Discovery; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M05-Q006

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** Stub, recursive, and application caches can observe different insertion times and remaining lifetimes.

**Explanation:** M05-Q006 uses self-check 3 from DNS, Addressing, Routing, and Discovery; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M05-Q007

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** It selects a forwarding path only; neighbor reachability, filtering, downstream routing, and service admission remain separate mechanisms.

**Explanation:** M05-Q007 uses self-check 4 from DNS, Addressing, Routing, and Discovery; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M05-Q008

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** A reliable, ordered, bidirectional byte stream without application message boundaries.

**Explanation:** M05-Q008 uses self-check 1 from TCP Ordering, Flow, Congestion, and Goodput; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M05-Q009

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** Flow control through receive capacity/window; congestion control protects the path.

**Explanation:** M05-Q009 uses self-check 2 from TCP Ordering, Flow, Congestion, and Goodput; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M05-Q010

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** Reuse can remove setup while transfer mechanics stay constant, so combining them hides the changed mechanism.

**Explanation:** M05-Q010 uses self-check 3 from TCP Ordering, Flow, Congestion, and Goodput; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M05-Q011

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** Usually only that the local kernel accepted bytes into its socket state; peer receipt and application processing require other evidence.

**Explanation:** M05-Q011 uses self-check 4 from TCP Ordering, Flow, Congestion, and Goodput; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M05-Q012

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** Chain validation to a configured trust anchor and hostname/identity matching.

**Explanation:** M05-Q012 uses self-check 1 from TLS Trust and Connection Establishment; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M05-Q021

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** BDP = 80 Mbps / 8 x 0.120 s = 1,200,000 bytes.

**Explanation:** M05-Q021 uses bandwidth-delay product from Request Paths, Round Trips, and Byte Budgets and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M05-Q022

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** Setup lower bound is 3 x 90 ms = 270 ms before payload work.

**Explanation:** M05-Q022 uses RTT setup from DNS, Addressing, Routing, and Discovery and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M05-Q023

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** Serialization is 280 KiB x 8 / 900 Kbps = 2.49 seconds, ignoring protocol overhead.

**Explanation:** M05-Q023 uses serialization from TCP Ordering, Flow, Congestion, and Goodput and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M05-Q024

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** Goodput is 100 x (1 - 0.12) = 88.0 MB/s.

**Explanation:** M05-Q024 uses goodput from TLS Trust and Connection Establishment and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M05-Q025

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** Mean concurrency is 350 x 0.08 = 28.0 active streams.

**Explanation:** M05-Q025 uses rate times hold time from Proxies, NAT, Pooling, and Exhaustion and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M05-Q026

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** Shared ordering exposes the later completion, 220 ms, while independent streams can expose the 140 ms result separately.

**Explanation:** M05-Q026 uses shared ordering from HTTP/1.1 and HTTP/2 Multiplexing and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.
