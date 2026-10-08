# Logging Policy Across Modules

**ID:** `ex-11`  
**Level:** L3  
**Module path:** `01-python-software-engineering/exercises/ex-11`

## Objective

Configure logging in one place, use in modules.

## Prerequisites

- logging module

## Requirements

- `logging_config.py` sets format/level from settings.
- At least two modules log with module-level loggers.

## Constraints

- No print in library code

## Expected behavior

- Consistent format

## Edge cases

- DEBUG off hides debug

## Acceptance criteria

- README how to change level

## Common mistakes

- basicConfig in every file

## H1 hint

getLogger(__name__) pattern.

## Files

Create your own `.py` files in this folder unless the exercise provides a starter.

## Hints elsewhere

See [HINTS.md](../../../HINTS.md) for H2/H3 on marked exercises (`ex-11`).
