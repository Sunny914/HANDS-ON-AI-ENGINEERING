# Parser Failure

**ID:** `ex-04`
**Stage:** 03-langchain
**Difficulty:** L3
**Category:** Focused implementation

## Objective

Treat a bad completion as a handled failure.

## Prerequisites

Stage 02 structured output. ex-03.

## Problem

Ask the chain for a JSON object with `summary` and `confidence`. The fake sometimes returns prose.

## Requirements

Use a Pydantic parser or a parser you wrote in Stage 02 behind a tiny runnable. Prose becomes a named error. Valid JSON returns the object.

## Constraints

Do not add a live retry loop yet.

## Inputs and outputs

String or message in. Model or error out.

## Edge cases

Empty string. JSON array instead of object.

## Errors

The error type is not `Exception` in the test's `pytest.raises`.

## Acceptance criteria

Two tests: valid, invalid.

## Testing

Feed messages directly where you can, so a model is unnecessary.

## Common mistakes

Catching the parser error and returning `{}`.

## Completion checklist

- [ ] Behavior matches the acceptance criteria
- [ ] Tests you were asked to write are present and passing
- [ ] You can explain the design without reading the hint file

## Reflection

Where would a single repair call live, and why is it not inside the parser?

## Extension

One optional repair invoke. Test that prose triggers exactly one extra call.

## Hints

Attempt the exercise before opening hints. In [../../HINTS.md](../../HINTS.md), read only the `ex-04` section, and stop at the first level that unblocks you.

- H1 is a concept
- H2 is structure
- H3 is a next step, not a finished implementation
- H4 is a review of your attempt. Bring the code to a reviewer. This file does not contain that review.
