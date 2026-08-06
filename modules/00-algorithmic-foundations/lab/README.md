# Module 00 Complexity Lab

This lab compares the same logical operations across structures and reports
operation counts, small local timings, derived ratios, seed-derived lookup
checksums, and model limits. It uses only Python's standard library.

## Quick Start

```bash
python3 -m complexity_lab scenarios/baseline.json
python3 -m complexity_lab scenarios/wide-range.json
python3 -m unittest discover -s tests
```

## What To Look For

- Linear scan work grows with `n`.
- Hash lookup performs one logical lookup per queried key under the supplied
  non-adversarial keys.
- Array and linked traversal perform the same logical sum through Python-level
  loops. This avoids comparing a C builtin against interpreted pointer chasing,
  but it still does not isolate CPU cache behavior.
- `lookup_key_checksum` should stay identical for the same seed and change when
  the seed changes; it proves the reproducibility contract is wired into the
  measured lookup workload.

Do not treat the timings as production performance claims. They are local
measurements for one interpreter and machine. CPython lists store contiguous
references to boxed objects, not contiguous primitive integers, and a
median-of-five run on a shared machine is not a controlled benchmark.
