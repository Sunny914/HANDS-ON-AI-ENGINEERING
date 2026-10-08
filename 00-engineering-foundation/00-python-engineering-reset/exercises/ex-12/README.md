# JSON Settings Load/Save

**ID:** `ex-12`  
**Level:** L3  
**Module path:** `00-python-engineering-reset/exercises/ex-12`

## Objective

Round-trip configuration with validation.

## Prerequisites

- json
- files
- with statement

## Requirements

- Schema: `{theme: str, font_size: int, features: list[str]}`.
- `load_settings(path)`, `save_settings(path, data)`, `validate_settings(data) -> None` raises ValueError.

## Constraints

- UTF-8
- Pretty print on save with indent

## Expected behavior

- Invalid types rejected before save

## Edge cases

- Missing file
- Malformed JSON

## Acceptance criteria

- ValueError messages mention field

## Common mistakes

- Not validating on load
- Silent defaults hiding bugs

## H1 hint

Validate after load and before save.

## Files

Create your own `.py` files in this folder unless the exercise provides a starter.

## Hints elsewhere

See [HINTS.md](../../../HINTS.md) for H2/H3 on marked exercises (`ex-12`).
