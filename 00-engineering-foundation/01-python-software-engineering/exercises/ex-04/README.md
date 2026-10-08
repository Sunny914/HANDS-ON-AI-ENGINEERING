# Dataclass Domain Models

**ID:** `ex-04`  
**Level:** L2  
**Module path:** `01-python-software-engineering/exercises/ex-04`

## Objective

Model data with dataclasses and invariants.

## Prerequisites

- dataclasses

## Requirements

- `Order`, `LineItem` with computed `total`.
- Method `add_item` enforcing positive quantity and price.

## Constraints

- Use @dataclass

## Expected behavior

- Immutability optional—document

## Edge cases

- zero quantity rejected

## Acceptance criteria

- __post_init__ or methods enforce rules

## Common mistakes

- Mutable default lists on dataclass

## H1 hint

Put validation in __post_init__ or add_item.

## Files

Create your own `.py` files in this folder unless the exercise provides a starter.

## Hints elsewhere

See [HINTS.md](../../../HINTS.md) for H2/H3 on marked exercises (`ex-04`).
