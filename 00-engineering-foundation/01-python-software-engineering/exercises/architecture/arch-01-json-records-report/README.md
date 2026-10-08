# JSON Records → Validated Report

**ID:** `arch-01`  
**Level:** Architecture  
**Module path:** `01-python-software-engineering/exercises/architecture/arch-01-json-records-report`

## Objective

Design structure for load → validate → transform → report.

## Prerequisites

- module 01 ex-01–05

## Requirements

- Load records from JSON file (schema in REQUIREMENTS.md).
- Validate, compute per-category totals and top spenders, write text report.
- Do NOT open REFERENCE.md until design written.

## Constraints

- You choose file layout
- Tests required

## Expected behavior

- CLI: `python -m app` or similar documented

## Edge cases

- invalid records
- empty file

## Acceptance criteria

- Architecture answers in `YOUR_ARCHITECTURE.md`
- REFERENCE comparison notes

## Common mistakes

- Validation inside print statements
- no separation

## H1 hint

Start from data flow diagram, not file names.

## Files

See REQUIREMENTS.md and REFERENCE.md (after design).

## Hints elsewhere

See [HINTS.md](../../../HINTS.md) for H2/H3 on marked exercises (`arch-01`).
