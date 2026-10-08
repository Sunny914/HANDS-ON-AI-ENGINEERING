# Merge and Dedupe Record Lists

**ID:** `ex-22`  
**Level:** L3  
**Module path:** `00-python-engineering-reset/exercises/ex-22`

## Objective

Combine records from two sources by key.

## Prerequisites

- dicts
- list comprehensions

## Requirements

- Records `{id, ...}`; merge B into A with B wins on conflict; dedupe by id stable order.

## Constraints

- O(n) average

## Expected behavior

- Predictable ordering documented

## Edge cases

- Missing id
- duplicate within same list

## Acceptance criteria

- Tests as assert block

## Common mistakes

- Nested loops O(n^2) unnecessarily

## H1 hint

Index by id with dict.

## Files

Create your own `.py` files in this folder unless the exercise provides a starter.

## Hints elsewhere

See [HINTS.md](../../../HINTS.md) for H2/H3 on marked exercises (`ex-22`).
