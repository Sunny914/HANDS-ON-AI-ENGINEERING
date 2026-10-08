# Debug: Imports and Package Layout

**ID:** `ex-20`  
**Level:** L5  
**Module path:** `00-python-engineering-reset/exercises/ex-20`

## Objective

Fix import errors in small package.

## Prerequisites

- packages

## Requirements

- Make `broken/pkg` importable and `python -m broken.pkg.main` work

## Constraints

- Minimal changes

## Expected behavior

- Command runs without ImportError

## Edge cases

- Running as script vs module

## Acceptance criteria

- FIX_NOTES.md explains fix

## Common mistakes

- Circular imports
- missing __init__

## H1 hint

Trace import graph from entry point.

## Files

Starter under `broken/pkg/`.

## Hints elsewhere

See [HINTS.md](../../../HINTS.md) for H2/H3 on marked exercises (`ex-20`).
