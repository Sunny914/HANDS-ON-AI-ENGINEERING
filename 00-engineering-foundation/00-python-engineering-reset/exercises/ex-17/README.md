# Debug: Mutation in Aggregation

**ID:** `ex-17`  
**Level:** L5  
**Module path:** `00-python-engineering-reset/exercises/ex-17`

## Objective

Diagnose incorrect totals caused by mutation.

## Prerequisites

- [DEBUGGING_GUIDE.md](../../../DEBUGGING_GUIDE.md)

## Requirements

- Run `broken/aggregator.py`; output is wrong for multi-group input.
- Fix code; document root cause.

## Constraints

- Do not rewrite from scratch unless needed

## Expected behavior

| Input | Expected `total_per_category` |
|-------|-------------------------------|
| a:1, b:2, a:3 | `a: 4`, `b: 2` |
| single category | correct sum |

## Edge cases

- Single group
- Multiple groups

## Acceptance criteria

- Table above passes after fix
- `FIX_NOTES.md` with 2–3 sentence postmortem

## Common mistakes

- Fixing symptom without understanding shared references

## H1 hint

Watch shared list references across groups.

## Files

Starter: `broken/aggregator.py`. Create `FIX_NOTES.md`.

## Hints elsewhere

See [HINTS.md](../../../HINTS.md) for H2/H3 (`ex-17`).
