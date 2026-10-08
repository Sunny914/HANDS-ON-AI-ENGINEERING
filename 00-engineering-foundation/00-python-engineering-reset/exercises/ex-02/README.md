# Text Normalization Pipeline

**ID:** `ex-02`  
**Level:** L1  
**Module path:** `00-python-engineering-reset/exercises/ex-02`

## Objective

Chain string operations into reusable steps.

## Prerequisites

- str methods
- f-strings or format

## Requirements

- Implement `normalize_whitespace(text) -> str` collapsing internal runs to single spaces, strip ends.
- Implement `slugify(text) -> str`: lowercase, whitespace to `-`, remove non-alphanumeric except hyphen.
- Implement `pipeline(text) -> str` applying normalize then slugify.

## Constraints

- Standard library only

## Expected behavior

- `pipeline("  Hello, World!  ")` → `hello-world` (punctuation removed)

## Edge cases

- Empty string
- Only spaces
- Unicode letters—document if stripped or kept

## Acceptance criteria

- Three functions with docstrings
- Three examples printed

## Common mistakes

- Forgetting strip
- Replacing only first space

## H1 hint

Solve normalize first; slugify should assume already normalized or call normalize internally.

## Files

Create your own `.py` files in this folder unless the exercise provides a starter.

## Hints elsewhere

See [HINTS.md](../../../HINTS.md) for H2/H3 on marked exercises (`ex-02`).
