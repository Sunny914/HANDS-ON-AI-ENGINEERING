# Safe Batch Operations and Exceptions

**ID:** `ex-11`  
**Level:** L3  
**Module path:** `00-python-engineering-reset/exercises/ex-11`

## Objective

Handle failures per item without stopping whole batch.

## Prerequisites

- try/except
- raise

## Requirements

- `safe_divide_batch(pairs: list[tuple]) -> list` returning results or None per pair on zero division.
- `parse_ints(lines: list[str]) -> tuple[list[int], list[str]]` successes and error messages.

## Constraints

- No bare except

## Expected behavior

- Batch completes

## Edge cases

- Empty input
- non-numeric strings

## Acceptance criteria

- Specific exception types caught

## Common mistakes

- Bare except
- Losing error context

## H1 hint

Catch narrow exceptions; collect errors instead of printing inside parser.

## Files

Create your own `.py` files in this folder unless the exercise provides a starter.

## Hints elsewhere

See [HINTS.md](../../../HINTS.md) for H2/H3 on marked exercises (`ex-11`).
