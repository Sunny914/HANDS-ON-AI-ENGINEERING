# Records with Dicts, Sets, Tuples

**ID:** `ex-06`  
**Level:** L2  
**Module path:** `00-python-engineering-reset/exercises/ex-06`

## Objective

Choose structures for membership and record lookup.

## Prerequisites

- dict
- set
- tuple

## Requirements

- Given list of user dicts `{id, name, tags: list[str]}`, build indexes: by_id, tag → set of ids.
- `users_with_all_tags(index, tags) -> list[int]`

## Constraints

- Pure functions

## Expected behavior

- Correct sets for overlapping tags

## Edge cases

- Unknown tag
- empty tags list meaning all users?—define

## Acceptance criteria

- Define empty tags behavior in docstring

## Common mistakes

- Storing lists where sets belong
- Mutating input dicts

## H1 hint

Invert index once; query functions stay cheap.

## Files

Create your own `.py` files in this folder unless the exercise provides a starter.

## Hints elsewhere

See [HINTS.md](../../../HINTS.md) for H2/H3 on marked exercises (`ex-06`).
