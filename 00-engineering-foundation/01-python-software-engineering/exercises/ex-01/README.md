# Pure Validation Functions

**ID:** `ex-01`  
**Level:** L1  
**Module path:** `01-python-software-engineering/exercises/ex-01`

## Objective

Write testable validators without I/O.

## Prerequisites

- functions
- strings

## Requirements

- `is_valid_email(s) -> bool` (pragmatic rules documented)
- `is_strong_password(s) -> bool` (length + char classes—you define)

## Constraints

- No regex required unless you choose

## Expected behavior

- Clear True/False

## Edge cases

- Empty
- unicode local part

## Acceptance criteria

- Docstring lists rules

## Common mistakes

- Overly strict RFC
- Printing inside validators

## H1 hint

Validators return bool; caller decides error messages.

## Files

Create your own `.py` files in this folder unless the exercise provides a starter.

## Hints elsewhere

See [HINTS.md](../../../HINTS.md) for H2/H3 on marked exercises (`ex-01`).
