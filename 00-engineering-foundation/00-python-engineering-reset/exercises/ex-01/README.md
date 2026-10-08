# Expression Evaluator and Types

**ID:** `ex-01`  
**Level:** L1  
**Module path:** `00-python-engineering-reset/exercises/ex-01`

## Objective

Practice literals, operators, and type introspection without libraries.

## Prerequisites

- Variables
- int/float/str/bool
- arithmetic operators

## Requirements

- Implement `describe_value(x)` returning a dict with keys: `type_name` (str), `is_numeric` (bool), `repr` (str from `repr()`).
- Implement `safe_add(a, b)` returning the sum if both numeric, else `None`.

## Constraints

- No third-party imports
- Single file `solution.py` acceptable

## Expected behavior

- `describe_value(3)` → type_name `'int'`, is_numeric True
- `safe_add('1', 2)` → None

## Edge cases

- bool is numeric for `is_numeric`
- None input to describe_value

## Acceptance criteria

- Manual checks or tiny asserts in `if __name__` block
- You can explain bool vs int

## Common mistakes

- Using `type()` display name wrong
- Treating bool as non-numeric

## H1 hint

Numeric means `int` or `float` in this exercise; decide explicitly whether `bool` counts.

## Files

Create your own `.py` files in this folder unless the exercise provides a starter.

## Hints elsewhere

See [HINTS.md](../../../HINTS.md) for H2/H3 on marked exercises (`ex-01`).
