# Integration: Config + Report Pipeline

**ID:** `ex-23`  
**Level:** L3/L4  
**Module path:** `00-python-engineering-reset/exercises/ex-23`

## Objective

Wire JSON config to file processing pipeline.

## Prerequisites

- ex-12
- ex-14

## Requirements

- Config selects input path and categories filter.
- Read CSV-like sales file, emit summary report to stdout and optional output path.

## Constraints

- 3+ modules
- logging at INFO for skipped lines

## Expected behavior

- End-to-end run documented

## Edge cases

- All lines skipped
- bad config

## Acceptance criteria

- Follow implementation workflow

## Common mistakes

- Monolith main
- No validation on config

## H1 hint

Vertical slice: config load → parse one line → full file.

## Files

Create your own `.py` files in this folder unless the exercise provides a starter.

## Hints elsewhere

See [HINTS.md](../../../HINTS.md) for H2/H3 on marked exercises (`ex-23`).
