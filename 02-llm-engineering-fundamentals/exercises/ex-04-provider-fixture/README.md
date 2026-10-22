# Normalize Provider Fixtures

**ID:** `ex-04`
**Stage:** 02-llm-engineering-fundamentals
**Difficulty:** L2
**Category:** Integration

## Objective

Map two JSON shapes onto one response type.

## Prerequisites

ex-02. Fixtures in `../../fixtures/`.

## Problem

Provider A and Provider B both return the same sentence in different envelopes. Your gateway needs one type.

## Requirements

Parse both fixture files into one dataclass or model with text, token counts, finish reason, and model name.

## Constraints

Do not add fields to the fixture files to make parsing easier.

## Inputs and outputs

JSON dict in. Normalized response out.

## Edge cases

Missing `usage` raises a named parse error. Empty text is allowed only if finish_reason is not `stop`. Document that rule.

## Errors

A wrong shape must not return partial zeros that look like a free call.

## Acceptance criteria

Both fixtures produce equal text and equal token counts.

## Testing

Load the JSON files in tests.

## Common mistakes

One giant function full of vendor names with no per-provider parser.

## Completion checklist

- [ ] Behavior matches the acceptance criteria
- [ ] Tests you were asked to write are present and passing
- [ ] You can explain the design without reading the hint file

## Reflection

What breaks if Provider B nests usage under `choices[0]` tomorrow?

## Extension

Parse a third tiny fixture you invent, and keep the normalized type stable.

## Hints

Attempt the exercise before opening hints. In [../../HINTS.md](../../HINTS.md), read only the `ex-04` section, and stop at the first level that unblocks you.

- H1 is a concept
- H2 is structure
- H3 is a next step, not a finished implementation
- H4 is a review of your attempt. Bring the code to a reviewer. This file does not contain that review.
