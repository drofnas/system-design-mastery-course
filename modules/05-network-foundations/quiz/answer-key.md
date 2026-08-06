# M05 Quiz Answer Key

This key covers all 39 questions for **Network Foundations**. Use it after an attempt, or provide it with the LLM grading prompt for feedback.

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

## M05-Q013

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Test the M05 scoped measurement and record the limiting assumption before approving the change.
- Approve adding marginal percentiles from different requests creates a journey that for Request Paths, Round Trips, and Byte Budgets; the local context makes that proposal familiar enough for review.
- Defer measurement until production for adding marginal percentiles from different requests creates a journey that; the team can monitor Request Paths, Round Trips, and Byte Budgets after launch.
- Approve the M05 shortcut for alpha now.

**Answer:** Test the M05 scoped measurement and record the limiting assumption before approving the change.

**Explanation:** M05-Q013 enacts mistake 1 from Request Paths, Round Trips, and Byte Budgets; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M05-Q014

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Approve treating payload bytes as wire bytes hides headers and retransmissions for Request Paths, Round Trips, and Byte Budgets; the local context makes that proposal familiar enough for review.
- Scope the M05 scoped measurement before approving the change.
- Defer measurement until production for treating payload bytes as wire bytes hides headers and retransmissions; the team can monitor Request Paths, Round Trips, and Byte Budgets after launch.
- Approve the M05 shortcut for bravo now.

**Answer:** Scope the M05 scoped measurement before approving the change.

**Explanation:** M05-Q014 enacts mistake 2 from Request Paths, Round Trips, and Byte Budgets; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M05-Q015

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Approve counting every phase as serial overstates cost when DNS/address attempts or for Request Paths, Round Trips, and Byte Budgets; the local context makes that proposal familiar enough for review.
- Defer measurement until production for counting every phase as serial overstates cost when DNS/address attempts or; the team can monitor Request Paths, Round Trips, and Byte Budgets after launch.
- Measure the M05 scoped measurement before approval.
- Approve the M05 shortcut for charlie now.

**Answer:** Measure the M05 scoped measurement before approval.

**Explanation:** M05-Q015 enacts mistake 3 from Request Paths, Round Trips, and Byte Budgets; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M05-Q016

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Approve calling a lower bound an SLO prediction hides queues, loss, and application work for Request Paths, Round Trips, and Byte Budgets; the local context makes that proposal familiar enough for review.
- Defer measurement until production for calling a lower bound an SLO prediction hides queues, loss, and application work; the team can monitor Request Paths, Round Trips, and Byte Budgets after launch.
- Approve the M05 shortcut for delta now.
- Bound the M05 scoped measurement and record the limiting assumption before approving the change.

**Answer:** Bound the M05 scoped measurement and record the limiting assumption before approving the change.

**Explanation:** M05-Q016 enacts mistake 4 from Request Paths, Round Trips, and Byte Budgets; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M05-Q017

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Freeze the M05 scoped measurement before approving the change.
- Approve “DNS is down” collapses authoritative, recursive, network, validation, and cache for DNS, Addressing, Routing, and Discovery; the local context makes that proposal familiar enough for review.
- Defer measurement until production for “DNS is down” collapses authoritative, recursive, network, validation, and cache; the team can monitor DNS, Addressing, Routing, and Discovery after launch.
- Approve the M05 shortcut for ember now.

**Answer:** Freeze the M05 scoped measurement before approving the change.

**Explanation:** M05-Q017 enacts mistake 1 from DNS, Addressing, Routing, and Discovery; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M05-Q018

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Approve infinite retry on timeout multiplies resolver load during failure for DNS, Addressing, Routing, and Discovery; the local context makes that proposal familiar enough for review.
- Preserve the M05 scoped measurement before approval.
- Defer measurement until production for infinite retry on timeout multiplies resolver load during failure; the team can monitor DNS, Addressing, Routing, and Discovery after launch.
- Approve the M05 shortcut for fable now.

**Answer:** Preserve the M05 scoped measurement before approval.

**Explanation:** M05-Q018 enacts mistake 2 from DNS, Addressing, Routing, and Discovery; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M05-Q019

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Approve using a stale address without a stated policy can route to decommissioned or uns for DNS, Addressing, Routing, and Discovery; the local context makes that proposal familiar enough for review.
- Defer measurement until production for using a stale address without a stated policy can route to decommissioned or uns; the team can monitor DNS, Addressing, Routing, and Discovery after launch.
- Model the M05 scoped measurement and record the limiting assumption before approving the change.
- Approve the M05 shortcut for harbor now.

**Answer:** Model the M05 scoped measurement and record the limiting assumption before approving the change.

**Explanation:** M05-Q019 enacts mistake 3 from DNS, Addressing, Routing, and Discovery; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M05-Q020

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Approve logging full queried names can expose tenant or user data for DNS, Addressing, Routing, and Discovery; the local context makes that proposal familiar enough for review.
- Defer measurement until production for logging full queried names can expose tenant or user data; the team can monitor DNS, Addressing, Routing, and Discovery after launch.
- Approve the M05 shortcut for indigo now.
- Account the M05 scoped measurement before approving the change.

**Answer:** Account the M05 scoped measurement before approving the change.

**Explanation:** M05-Q020 enacts mistake 4 from DNS, Addressing, Routing, and Discovery; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M05-Q021

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** M05 Bandwidth-Delay Product case 1: BDP = 80 Mbps / 8 x 0.120 s = 1,200,000 bytes.

**Explanation:** M05-Q021 uses bandwidth-delay product from Request Paths, Round Trips, and Byte Budgets and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M05-Q022

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** M05 Rtt Setup case 2: Setup lower bound is 3 x 90 ms = 270 ms before payload work.

**Explanation:** M05-Q022 uses RTT setup from DNS, Addressing, Routing, and Discovery and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M05-Q023

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** M05 Serialization case 3: Serialization is 280 KiB x 8 / 900 Kbps = 2.49 seconds, ignoring protocol overhead.

**Explanation:** M05-Q023 uses serialization from TCP Ordering, Flow, Congestion, and Goodput and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M05-Q024

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** M05 Goodput case 4: Goodput is 100 x (1 - 0.12) = 88.0 MB/s.

**Explanation:** M05-Q024 uses goodput from TLS Trust and Connection Establishment and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M05-Q025

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** M05 Rate Times Hold Time case 5: Mean concurrency is 350 x 0.08 = 28.0 active streams.

**Explanation:** M05-Q025 uses rate times hold time from Proxies, NAT, Pooling, and Exhaustion and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M05-Q026

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** M05 Shared Ordering case 6: Shared ordering exposes the later completion, 220 ms, while independent streams can expose the 140 ms result separately.

**Explanation:** M05-Q026 uses shared ordering from HTTP/1.1 and HTTP/2 Multiplexing and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M05-Q027

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** M05 diagnosis 1 identifies Request Paths, Round Trips, and Byte Budgets evidence scope. The proving fields are path.rtt_ms and path.bandwidth_kbps; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M05-Q027 comes from emitted trial fields rather than fixture identifiers; Request Paths, Round Trips, and Byte Budgets is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M05-Q028

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** M05 diagnosis 2 identifies DNS, Addressing, Routing, and Discovery evidence scope. The proving fields are path.rtt_ms and path.bandwidth_kbps; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M05-Q028 comes from emitted trial fields rather than fixture identifiers; DNS, Addressing, Routing, and Discovery is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M05-Q029

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** M05 diagnosis 3 identifies TCP Ordering, Flow, Congestion, and Goodput evidence scope. The proving fields are path.rtt_ms and path.bandwidth_kbps; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M05-Q029 comes from emitted trial fields rather than fixture identifiers; TCP Ordering, Flow, Congestion, and Goodput is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M05-Q030

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** M05 diagnosis 4 identifies TLS Trust and Connection Establishment evidence scope. The proving fields are path.rtt_ms and path.bandwidth_kbps; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M05-Q030 comes from emitted trial fields rather than fixture identifiers; TLS Trust and Connection Establishment is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M05-Q031

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** M05 diagnosis 5 identifies Proxies, NAT, Pooling, and Exhaustion evidence scope. The proving fields are path.rtt_ms and path.bandwidth_kbps; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M05-Q031 comes from emitted trial fields rather than fixture identifiers; Proxies, NAT, Pooling, and Exhaustion is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M05-Q032

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** M05 diagnosis 6 identifies HTTP/1.1 and HTTP/2 Multiplexing evidence scope. The proving fields are path.rtt_ms and path.bandwidth_kbps; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M05-Q032 comes from emitted trial fields rather than fixture identifiers; HTTP/1.1 and HTTP/2 Multiplexing is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M05-Q033

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** M05 diagnosis 7 identifies QUIC and HTTP/3 Stream Behavior evidence scope. The proving fields are path.rtt_ms and path.bandwidth_kbps; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M05-Q033 comes from emitted trial fields rather than fixture identifiers; QUIC and HTTP/3 Stream Behavior is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M05-Q034

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** M05 diagnosis 8 identifies Protocol and Topology Decisions evidence scope. The proving fields are path.rtt_ms and path.bandwidth_kbps; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M05-Q034 comes from emitted trial fields rather than fixture identifiers; Protocol and Topology Decisions is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M05-Q035

**Type:** `design_judgment`
**Difficulty:** `synthesis`

**Answer:** For M05 decision 1, recommend against. The protected bound is 195 x 0.72 = 140.4/s, and the planned 171.6/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 171.6/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 31.2/s of lower-priority work.

**Explanation:** M05-Q035 turns on the forcing number from EX-01, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M05-Q036

**Type:** `design_judgment`
**Difficulty:** `recall`

**Answer:** For M05 decision 2, recommend against. The protected bound is 212 x 0.72 = 152.6/s, and the planned 186.6/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 186.6/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 34.0/s of lower-priority work.

**Explanation:** M05-Q036 turns on the forcing number from EX-02, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M05-Q037

**Type:** `design_judgment`
**Difficulty:** `application`

**Answer:** For M05 decision 3, recommend against. The protected bound is 229 x 0.72 = 164.9/s, and the planned 201.5/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 201.5/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 36.6/s of lower-priority work.

**Explanation:** M05-Q037 turns on the forcing number from EX-03, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M05-Q038

**Type:** `design_judgment`
**Difficulty:** `synthesis`

**Answer:** For M05 decision 4, recommend against. The protected bound is 246 x 0.72 = 177.1/s, and the planned 216.5/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 216.5/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 39.4/s of lower-priority work.

**Explanation:** M05-Q038 turns on the forcing number from EX-04, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M05-Q039

**Type:** `design_judgment`
**Difficulty:** `recall`

**Answer:** For M05 decision 5, recommend against. The protected bound is 263 x 0.72 = 189.4/s, and the planned 231.4/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 231.4/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 42.0/s of lower-priority work.

**Explanation:** M05-Q039 turns on the forcing number from EX-05, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.
