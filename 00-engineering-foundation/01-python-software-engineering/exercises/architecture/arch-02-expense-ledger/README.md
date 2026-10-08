# Expense Ledger CLI

**ID:** `arch-02`  
**Level:** Architecture  
**Module path:** `01-python-software-engineering/exercises/architecture/arch-02-expense-ledger`

## Objective

CRUD + summaries with explicit layers.

## Prerequisites

- arch-01 experience

## Requirements

- Commands: add, list, summary by month, export csv.
- Persistence JSON; validation at boundary.

## Constraints

- Service/repository split required

## Expected behavior

- Month filter correct

## Edge cases

- timezone on dates—use naive ISO dates

## Acceptance criteria

- YOUR_ARCHITECTURE.md + tests

## Common mistakes

- CLI parses business rules

## H1 hint

Repository knows file format; service knows use cases.

## Files

REQUIREMENTS.md, REFERENCE.md after design.

## Hints elsewhere

See [HINTS.md](../../../HINTS.md) for H2/H3 on marked exercises (`arch-02`).
