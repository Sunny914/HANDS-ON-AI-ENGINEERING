# List Algorithms Without Imports

**ID:** `ex-03`  
**Level:** L1  
**Module path:** `00-python-engineering-reset/exercises/ex-03`

## Objective

Manipulate lists: search, insert, aggregate.

## Prerequisites

- lists
- for loops
- indices

## Requirements

- `second_largest(nums) -> int | None`
- `rotate_left(nums, k) -> list` (new list, not mutate unless you document)
- `chunk(nums, size) -> list[list]`

## Constraints

- No `max()` for second_largest if you want extra challenge—allowed if documented

## Expected behavior

- `second_largest([1,2,3])` → 2
- `chunk([1,2,3,4,5], 2)` → [[1,2],[3,4],[5]]

## Edge cases

- Duplicates in second_largest
- k=0
- size<=0

## Acceptance criteria

- Handle empty list for second_largest
- chunk last partial

## Common mistakes

- Mutating while iterating
- Off-by-one on k

## H1 hint

Second largest needs a pass or sort—consider duplicate max values.

## Files

Create your own `.py` files in this folder unless the exercise provides a starter.

## Hints elsewhere

See [HINTS.md](../../../HINTS.md) for H2/H3 on marked exercises (`ex-03`).
