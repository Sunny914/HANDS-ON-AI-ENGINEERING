# Generator-Based Line Processing

**ID:** `ex-07`  
**Level:** L2  
**Module path:** `01-python-software-engineering/exercises/ex-07`

## Objective

Stream lines without loading entire file.

## Prerequisites

- generators
- yield

## Requirements

- `iter_lines(path)`, `iter_nonempty_stripped(path)`, `grep(path, substring)` generators.

## Constraints

- Handle missing file with FileNotFoundError

## Expected behavior

- Memory stable on large file—you can fake with generator

## Edge cases

- empty file
- encoding errors policy

## Acceptance criteria

- Document encoding default

## Common mistakes

- Reading all lines into list

## H1 hint

yield inside with-open loop.

## Files

Create your own `.py` files in this folder unless the exercise provides a starter.

## Hints elsewhere

See [HINTS.md](../../../HINTS.md) for H2/H3 on marked exercises (`ex-07`).
