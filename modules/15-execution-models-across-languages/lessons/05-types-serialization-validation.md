---
lesson_id: L05
title: "Types, Serialization, and Validation"
---

# Types, Serialization, and Validation

## Outcomes

Compare static/dynamic and nominal/structural typing, then restore guarantees
lost at JSON, process, persistence, and authorization boundaries.

## Prerequisites

Module 13 trust boundaries and RES-05.

## Mechanism and method

Static typing checks a program before execution; dynamic typing associates
checks with runtime values. Nominal systems use declared relationships;
structural systems use shape. These dimensions are independent. None makes
untrusted bytes a valid domain value.

Use **WIRE**: write the semantic contract; identify who produces bytes; reject
invalid syntax and shape; establish domain invariants and authorization; emit a
versioned result with safe errors. Validation belongs at each boundary where a
guarantee disappears, not only at the first public endpoint.

TypeScript interfaces are erased. An `as FanoutRequest` assertion changes what
the compiler believes without checking a byte. Go and Java decoding can accept
defaults or ignore unknown fields depending on configuration. Serde can enforce
strict fields, but deserialization still cannot prove that a deadline is in the
future or a caller may request a child. Validation must bound child count,
payload, deadline, identifiers, enum values, and cross-field meaning before
allocation or authority.

## Worked example

Northstar receives JSON with `concurrency_limit: "unlimited"`, 4,000 children,
and a client-selected `tenant_id`. The broken TypeScript variant asserts the
decoded value and starts iterating. The compiler is satisfied, but the process
boundary removed its guarantee. The repair parses into `unknown`, validates a
maximum of 16 children, integer bounds, a 50–5,000 ms deadline, allowed fault
mode, and server-derived tenant context. It returns a bounded 400 response and
creates no child tasks. Equivalent repairs in the other runtimes preserve the
same public outcome even when library defaults differ.

## Common expert mistakes

- Treating a generated type as a wire validator.
- Returning library-specific parse errors that leak internals or change clients.
- Validating shape after large allocation or task creation.
- Allowing unknown fields accidentally in one runtime and rejecting them in another.

## Guided practice

Define syntax, shape, semantic, authorization, and resource checks for the
fan-out request. Put them in execution order and specify one safe error code per
class. Include an evolution rule for adding an optional field.

## Self-check

1. What does a TypeScript assertion validate?
2. Why is schema validity insufficient for authorization?
3. How should four runtimes handle the same unknown field?

## Explained answers

1. Nothing at runtime; it only changes the compiler's assumed type.
2. A well-shaped request may still ask for data or work the caller cannot access.
3. Follow one published compatibility policy and conformance fixture; defaults
   from individual decoders do not define the public contract.

## Sources and next work

Use RES-05 and the public schemas. Continue to [Lesson 6](06-equivalent-work-measurement.md).
