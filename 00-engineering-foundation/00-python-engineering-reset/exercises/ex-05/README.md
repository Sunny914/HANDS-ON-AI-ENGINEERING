# Functions: Unit Conversion

**ID:** `ex-05`  
**Level:** L1  
**Module path:** `00-python-engineering-reset/exercises/ex-05`

## Objective

Compose small conversion functions.

## Prerequisites

- functions
- return
- float

## Requirements

- Implement km↔mi, c↔f, kg↔lb (pick formulas, document constants).
- `convert(value, from_unit, to_unit)` dispatching via dict or if chain.

## Constraints

- Raise ValueError for unknown units

## Expected behavior

- Round-trip within tolerance 1e-6 for floats

## Edge cases

- Negative distances?
- Unknown unit strings

## Acceptance criteria

- At least 6 unit tokens supported
- Docstring lists units

## Common mistakes

- Inverted formula
- Case-sensitive units

## H1 hint

Centralize constants; conversion functions stay pure.

## Files

Create your own `.py` files in this folder unless the exercise provides a starter.

## Hints elsewhere

See [HINTS.md](../../../HINTS.md) for H2/H3 on marked exercises (`ex-05`).
