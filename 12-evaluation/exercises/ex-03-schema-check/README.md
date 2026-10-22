# Schema Validity

**ID:** `ex-03`
**Stage:** 12-evaluation
**Difficulty:** L2
**Category:** Testing

## Objective

Score structured output without judging prose.

## Prerequisites

Stage 05 schemas. ex-01.

## Problem

A checker accepts or rejects a predicted object against a closed schema.

## Requirements

Required keys and types. Extra keys fail. This result is `schema_valid`, not `correct_answer`.

## Constraints

No model.

## Inputs and outputs

A schema description you define and a prediction object.

## Edge cases

Missing key. Wrong type. Extra key. Empty list where a list is required.

## Errors

Return a list of field errors. Do not raise on the first bad field unless you also test that choice and document it.

## Acceptance criteria

One valid object, one missing field, one extra field.

## Testing

Unit tests.

## Common mistakes

Using string length as a quality score.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

What can still be wrong after a schema pass?

## Extension

Add an enum field for stop reason.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-03` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
