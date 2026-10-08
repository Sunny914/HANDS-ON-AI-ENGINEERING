# Configuration from Env + File

**ID:** `ex-10`  
**Level:** L3  
**Module path:** `01-python-software-engineering/exercises/ex-10`

## Objective

Layered config with precedence.

## Prerequisites

- json/yaml optional
- os.environ

## Requirements

- Load defaults, overlay file, overlay env vars with prefix `APP_`.
- Expose `Settings` object with typed fields.

## Constraints

- Document precedence

## Expected behavior

- Missing file uses defaults

## Edge cases

- Invalid env int
- unknown keys ignored or strict—choose

## Acceptance criteria

- Small settings.json example

## Common mistakes

- Global mutable settings everywhere

## H1 hint

Load once; pass Settings into services.

## Files

Create your own `.py` files in this folder unless the exercise provides a starter.

## Hints elsewhere

See [HINTS.md](../../../HINTS.md) for H2/H3 on marked exercises (`ex-10`).
