# Notes Manager (Multi-File Design)

**ID:** `ex-16`  
**Level:** L4  
**Module path:** `00-python-engineering-reset/exercises/ex-16`

## Objective

Persist notes to JSON with CRUD.

## Prerequisites

- json
- ex-12

## Requirements

- CRUD for notes `{id, title, body, updated_at}` persisted to file.
- CLI commands: add, list, view, delete.

## Constraints

- Atomic save strategy documented

## Expected behavior

- Survives restart

## Edge cases

- Duplicate titles allowed?
- corrupt file

## Acceptance criteria

- README in folder how to run

## Common mistakes

- Overwrite file without temp
- IDs as ints vs str inconsistency

## H1 hint

Pick ID strategy first; storage layer knows file format only.

## Files

Create your own `.py` files in this folder unless the exercise provides a starter.

## Hints elsewhere

See [HINTS.md](../../../HINTS.md) for H2/H3 on marked exercises (`ex-16`).
