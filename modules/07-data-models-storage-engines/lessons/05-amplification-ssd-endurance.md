---
lesson_id: L05
title: "Amplification and SSD Endurance"
---

# Amplification and SSD Endurance

## Outcomes

- Calculate read, write, and space amplification from trial counters.
- Separate engine, file-system, and device amplification claims.
- Translate physical work into capacity, cost, and endurance sensitivity.

## Prerequisites

Lessons 2–4, byte arithmetic, percentiles, and Module 2 useful-throughput work.

## Mechanism and method

Amplification compares physical work with application intent:

```text
read_amp  = physical page/block probes / logical read operations
write_amp = engine bytes written / logical key-value bytes written
space_amp = current on-disk bytes / current live logical bytes
```

State inclusions. Does logical write include keys, values, tombstones, metadata,
or overwritten bytes? Does physical write include initial flush, compaction,
manifest, and temporary output? Does read amplification include cache hits?
Without boundaries, two ratios are not comparable.

For sustained logical ingest `L` bytes/s and engine write amplification `A`,
the engine asks the file system to accept approximately `L*A` bytes/s. Device
firmware can add its own amplification. A rough endurance exposure over `d`
days is `L*A*86400*d`; this is a sensitivity estimate, not a device warranty
calculation.

Measure distributions as well as totals. A mean compaction cost can coexist
with p99 stalls when work arrives in bursts. Separate useful throughput from
maintenance throughput and check whether backlog returns to baseline.

## Worked example

Harbor accepts 10 MiB of key/value/tombstone bytes. Flush and compaction write
34 MiB, so engine write amplification is 3.4. Six logical reads cause 18 table
or page probes, giving read amplification 3.0. The files occupy 16 MiB while
the live map encodes 12 MiB, giving space amplification 1.33.

At 8,000 observations/s and 272 logical bytes per observation, a peak ingest is
about 2.18 MB/s before framing and indexes. At 3.4 amplification, the engine
requests about 7.4 MB/s. Harbor still reserves temporary compaction space and
does not infer SSD media writes from that host-level number.

## Common expert mistakes

- **Comparing ratios with different denominators:** key-only and key-plus-value
  logical bytes give different answers.
- **Calling host bytes device bytes:** controller garbage collection is hidden.
- **Using database size as live size:** obsolete versions and tombstones change
  the denominator.
- **Ignoring temporary output:** compaction can require free space before old
  files are removed.
- **Optimizing one amplification alone:** tiering can lower writes while raising
  reads and space.

## Guided practice

For two Harbor trials, compute all three ratios and recalculate write capacity
at 2x and 4x ingest. Identify the counter needed to distinguish a lower ratio
caused by compression from one caused by less compaction. Complete EX-10.

## Self-check

1. Can read amplification be below one in this module's definition?
2. Why is space amplification undefined for an empty live set?
3. What recovery question follows an acceptable steady-state write ratio?

## Explained answers

1. Yes, if some reads are served without a physical probe, but the evidence
   must state whether cache hits count as zero probes.
2. Division by zero has no useful interpretation; report on-disk bytes and the
   empty state separately.
3. Whether compaction backlog drains after peak load without violating latency,
   free-space, or overload budgets.

## Sources and next work

- RocksDB compaction trade-offs, RES-05–RES-06.
- NVM Express engine/device write-amplification distinction, RES-11.
- Continue to Lesson 6 and preserve exact numerator/denominator definitions.
