# Timing Decorator

**ID:** `ex-08`  
**Level:** L2  
**Module path:** `01-python-software-engineering/exercises/ex-08`

## Objective

Cross-cutting concern with decorator.

## Prerequisites

- decorators
- functools.wraps

## Requirements

- `@timed` logging duration to stdout or logger.
- Preserve function metadata.

## Constraints

- Use wraps

## Expected behavior

- Nested calls show separate timings

## Edge cases

- exceptions still record time?—document

## Acceptance criteria

- Docstring on decorator

## Common mistakes

- Forgetting wraps
- timing including argument stringify

## H1 hint

Decorator returns wrapper accepting *args, **kwargs.

## Files

Create your own `.py` files in this folder unless the exercise provides a starter.

## Hints elsewhere

See [HINTS.md](../../../HINTS.md) for H2/H3 on marked exercises (`ex-08`).
