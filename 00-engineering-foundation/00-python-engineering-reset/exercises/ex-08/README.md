# Flexible Formatters

**ID:** `ex-08`  
**Level:** L2  
**Module path:** `00-python-engineering-reset/exercises/ex-08`

## Objective

Use `*args` and `**kwargs` deliberately.

## Prerequisites

- function arguments

## Requirements

- `make_table(headers, *rows, **options)` → str; options: `padding` int default 1, `delimiter` str default `|`.
- Validate row width matches headers.

## Constraints

- Raise ValueError on ragged rows

## Expected behavior

- Aligned simple table string

## Edge cases

- No rows
- Unicode width not required

## Acceptance criteria

- kwargs override defaults

## Common mistakes

- Mutating headers
- Forgetting to stringify cells

## H1 hint

Build row strings in a loop; kwargs only affect formatting.

## Files

Create your own `.py` files in this folder unless the exercise provides a starter.

## Hints elsewhere

See [HINTS.md](../../../HINTS.md) for H2/H3 on marked exercises (`ex-08`).
