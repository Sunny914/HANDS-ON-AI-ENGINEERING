# Control Flow: Ticket Pricing

**ID:** `ex-04`  
**Level:** L1  
**Module path:** `00-python-engineering-reset/exercises/ex-04`

## Objective

Model rules with branches and compound conditions.

## Prerequisites

- if/elif/else
- comparison operators

## Requirements

- `ticket_price(age: int, is_student: bool, is_weekend: bool) -> float` with documented rules you choose (must include at least 3 tiers and one weekend modifier).
- Document rules in module docstring.

## Constraints

- No input(); use function only

## Expected behavior

- Deterministic floats
- Negative age raises ValueError

## Edge cases

- age 0
- very large age

## Acceptance criteria

- ValueError on invalid age
- Table of 5 scenarios in comments

## Common mistakes

- Overlapping elif leaving gaps
- Float rounding surprises

## H1 hint

Write rules as table on paper first, then encode without nested ternaries.

## Files

Create your own `.py` files in this folder unless the exercise provides a starter.

## Hints elsewhere

See [HINTS.md](../../../HINTS.md) for H2/H3 on marked exercises (`ex-04`).
