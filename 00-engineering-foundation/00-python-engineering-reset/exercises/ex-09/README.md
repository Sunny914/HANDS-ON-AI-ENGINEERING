# Scope and Mutable Defaults

**ID:** `ex-09`  
**Level:** L2  
**Module path:** `00-python-engineering-reset/exercises/ex-09`

## Objective

Implement correct patterns and explain broken ones.

## Prerequisites

- scope
- default arguments

## Requirements

- Implement `append_item_wrong` (intentionally uses mutable default) and `append_item_right`.
- Demonstrate difference in `demo()` printing results.
- Implement `counter()` factory using closure or class—your choice—to return increment function.

## Constraints

- Document why wrong version fails

## Expected behavior

- Right version isolated
- Wrong shares state

## Edge cases

- Multiple callers

## Acceptance criteria

- Written explanation in comments

## Common mistakes

- Using mutable default
- Confusing global vs closure

## H1 hint

Mutable default is evaluated once at function definition time.

## Files

Create your own `.py` files in this folder unless the exercise provides a starter.

## Hints elsewhere

See [HINTS.md](../../../HINTS.md) for H2/H3 on marked exercises (`ex-09`).
