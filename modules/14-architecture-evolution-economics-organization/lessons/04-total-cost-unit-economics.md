lesson_id: L04

# Total Cost and Unit Economics

## Outcomes

- Calculate fully loaded current, transition, and target cost.
- Define a useful-outcome denominator with quality guardrails.
- Run sensitivity analysis and set a cost stopping condition.

## Prerequisites

Use Module 2 throughput and useful-work models, Module 4 measurement practice,
and Module 12 valid-event and SLO populations.

## Derivation

Separate recurring and one-time cost:

```text
recurring cost = direct variable + direct fixed + allocated shared
               + engineering and operations + expected risk exposure

comparison cost = recurring cost + transition cost / amortization windows

unit cost = comparison cost / good useful outcomes
```

Define the denominator before viewing the result. Northstar counts only correct,
fresh catalog reads that meet the latency objective. Retries, mismatches, stale
responses, and failed reads consume cost but do not increase useful output.

Allocation is a decision. State how a shared platform, support contract, on-call
rotation, and engineering labor are apportioned. Report both allocated and
unallocated values when the rule is uncertain. Keep cash spend, staffing
capacity, and risk exposure visible rather than hiding them in one precise sum.

Sensitivity analysis varies demand, good-outcome rate, provider price, shared
allocation, staffing, migration duration, and failure frequency. Find the
break-even value and the input with the greatest decision influence. A strategy
must state the budget or unit-cost threshold that pauses expansion or reverses
the design.

## Worked example

Northstar's monthly comparison uses synthetic inputs:

| Class | Modular | Event projection |
|---|---:|---:|
| Direct and allocated platform | $9,000 | $15,000 |
| Engineering and operations | $16,000 | $24,000 |
| Expected incident exposure | $5,000 | $3,000 |
| 12-month amortized transition | $0 | $12,000 |
| Good catalog reads | 530,000 | 538,000 |

The modular comparison cost is $30,000, or $56.60 per 1,000 good reads. The
event projection is $54,000, or $100.37. Extraction is not a cost-saving claim.
Northstar accepts the temporary premium for independently owned delivery and
lower registry blast radius, sets a $105 threshold, and requires transition
cost to expire after twelve months. If the new team cannot reduce coordination
delay, the modular alternative wins.

## Common expert mistakes

- **Dividing by all requests.** Failed or stale results make the system look
  cheaper precisely when quality worsens.
- **Ignoring labor and transition.** Infrastructure-only comparisons reward
  architectures that move work to people.
- **Double-counting shared cost.** Allocation rules must reconcile to the total.
- **Using a single forecast.** A decision that flips after a small input change
  needs an experiment or a reversible sequence.

## Guided practice

Recalculate Northstar for a 4× provider price, a 5% good-read loss, and a six-
month migration delay. Name the first threshold crossed and the required action.

## Self-check

1. Why separate transition cost?
2. What makes a denominator useful?
3. How should uncertain labor allocation appear?
4. What is the purpose of a break-even calculation?

## Explained answers

1. It should expire; mixing it into steady state can hide whether the migration
   completes or make a valuable target look permanently expensive.
2. It connects spend to a product outcome and excludes work that failed quality
   guardrails.
3. Show the rule, range, confidence, owner, and sensitivity rather than one
   unsupported number.
4. It exposes which assumption controls the decision and where to gather more
   evidence or stop.

## Sources and next work

Complete RES-04, EX-07, and EX-08. Use the architecture cost-model template and
preserve its formulas and raw inputs.
