# Parse and Aggregate CSV-like Rows

**ID:** `ex-14`  
**Level:** L3  
**Module path:** `00-python-engineering-reset/exercises/ex-14`

## Objective

Combine parsing, dicts, and aggregation.

## Prerequisites

- strings
- dicts
- split

## Requirements

- Parse lines `name,amount,category` (no quoted commas) into records.
- `summary_by_category(rows) -> dict[str, float]` totals.

## Constraints

- Skip malformed lines with warning to stderr

## Expected behavior

- Correct sums

## Edge cases

- Negative amounts
- blank lines

## Acceptance criteria

- Malformed line count reported

## Common mistakes

- Not stripping
- Float parse errors

## H1 hint

Parse line → validate → accumulate; keep parse pure.

## Files

Create your own `.py` files in this folder unless the exercise provides a starter.

## Hints elsewhere

See [HINTS.md](../../../HINTS.md) for H2/H3 on marked exercises (`ex-14`).
