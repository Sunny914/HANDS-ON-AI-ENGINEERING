# Custom Exceptions + Service Boundary

**ID:** `ex-12`  
**Level:** L3  
**Module path:** `01-python-software-engineering/exercises/ex-12`

## Objective

Translate storage errors to domain errors.

## Prerequisites

- exceptions
- modules

## Requirements

- In-memory `UserRepository` raising `UserNotFound`.
- `UserService` catching/converting lower-level errors.
- CLI prints friendly message.

## Constraints

- 3+ files

## Expected behavior

- Stack trace not shown to user for expected errors

## Edge cases

- duplicate user

## Acceptance criteria

- Exception hierarchy diagram in comments

## Common mistakes

- except Exception everywhere

## H1 hint

Domain errors cross service boundary; CLI maps to text.

## Files

Create your own `.py` files in this folder unless the exercise provides a starter.

## Hints elsewhere

See [HINTS.md](../../../HINTS.md) for H2/H3 on marked exercises (`ex-12`).
