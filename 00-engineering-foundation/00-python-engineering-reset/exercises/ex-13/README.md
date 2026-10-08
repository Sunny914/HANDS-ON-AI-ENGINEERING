# Two-Module Word Statistics

**ID:** `ex-13`  
**Level:** L3  
**Module path:** `00-python-engineering-reset/exercises/ex-13`

## Objective

Split code across modules with clear imports.

## Prerequisites

- modules
- packages basics

## Requirements

- Package `wordstats` with `tokenize.py` and `stats.py` and `__main__.py`.
- CLI: `python -m wordstats path/to/file.txt` prints top 5 tokens.

## Constraints

- Relative imports within package

## Expected behavior

- Runs as module

## Edge cases

- Empty file
- binary file error

## Acceptance criteria

- No circular imports

## Common mistakes

- Running submodule directly breaking imports
- Logic all in __main__

## H1 hint

__main__ orchestrates; tokenize vs aggregate split.

## Files

Create your own `.py` files in this folder unless the exercise provides a starter.

## Hints elsewhere

See [HINTS.md](../../../HINTS.md) for H2/H3 on marked exercises (`ex-13`).
