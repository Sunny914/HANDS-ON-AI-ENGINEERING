# Type Hints and Static Reasoning

**ID:** `ex-05`  
**Level:** L2  
**Module path:** `01-python-software-engineering/exercises/ex-05`

## Objective

Add types to untyped module and fix mismatches.

## Prerequisites

- typing basics

## Requirements

- Take provided `untyped_stub.py` (comment-only spec) and implement typed `inventory.py` API from README signatures.
- Run mypy if installed; otherwise manual review checklist in TYPES_CHECKLIST.md.

## Constraints

- No Any unless justified

## Expected behavior

- Signatures match README

## Edge cases

- Optional fields

## Acceptance criteria

- TYPES_CHECKLIST.md completed

## Common mistakes

- Dict without key types
- ignoring None

## H1 hint

Model optional as Optional[T] or | None.

## Files

Implement `inventory.py`; `untyped_stub.py` is comment-only spec.

## Hints elsewhere

See [HINTS.md](../../../HINTS.md) for H2/H3 on marked exercises (`ex-05`).
