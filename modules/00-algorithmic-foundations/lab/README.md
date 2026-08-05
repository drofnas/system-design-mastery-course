# Module 00 Complexity Lab

This lab compares the same logical operations across structures and reports
operation counts, small local timings, and model limits. It uses only Python's
standard library.

## Quick Start

```bash
python3 -m complexity_lab scenarios/baseline.json
python3 -m unittest discover -s tests
```

## What To Look For

- Linear scan work grows with `n`.
- Hash lookup performs one logical lookup per queried key under the supplied
  non-adversarial keys.
- Array and linked traversal perform the same logical sum, but the lab records
  the locality assumption separately from timing.

Do not treat the timings as production performance claims. They are local
measurements for one interpreter and machine.
