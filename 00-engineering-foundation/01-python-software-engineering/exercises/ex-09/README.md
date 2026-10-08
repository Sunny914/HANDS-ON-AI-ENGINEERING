# Context Manager for Temporary State

**ID:** `ex-09`  
**Level:** L2  
**Module path:** `01-python-software-engineering/exercises/ex-09`

## Objective

Implement context manager (class or @contextmanager).

## Prerequisites

- with statement

## Requirements

- `temporary_env(vars: dict)` setting os.environ keys, restoring after block.

## Constraints

- Restore even on exception

## Expected behavior

- Nested contexts behave

## Edge cases

- Key existed before
- delete vs restore

## Acceptance criteria

- Tests or demo script

## Common mistakes

- Not restoring on error

## H1 hint

Save old values in __enter__.

## Files

Create your own `.py` files in this folder unless the exercise provides a starter.

## Hints elsewhere

See [HINTS.md](../../../HINTS.md) for H2/H3 on marked exercises (`ex-09`).
