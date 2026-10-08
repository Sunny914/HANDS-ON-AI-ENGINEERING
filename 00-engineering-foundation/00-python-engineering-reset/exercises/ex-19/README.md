# Debug: File Paths and Encoding

**ID:** `ex-19`  
**Level:** L5  
**Module path:** `00-python-engineering-reset/exercises/ex-19`

## Objective

Fix file handling bugs.

## Prerequisites

- paths
- encoding

## Requirements

- Fix `broken/read_config.py` to read `data/settings.json` reliably from exercise dir

## Constraints

- Use pathlib or os.path consistently

## Expected behavior

- Works when cwd is not exercise folder if you support `--path`

## Edge cases

- Missing file
- UTF-8 content

## Acceptance criteria

- FIX_NOTES.md

## Common mistakes

- Relative path only from cwd

## H1 hint

Anchor paths to `__file__` location.

## Files

Starter: `broken/read_config.py`, sample `data/settings.json`.

## Hints elsewhere

See [HINTS.md](../../../HINTS.md) for H2/H3 on marked exercises (`ex-19`).
