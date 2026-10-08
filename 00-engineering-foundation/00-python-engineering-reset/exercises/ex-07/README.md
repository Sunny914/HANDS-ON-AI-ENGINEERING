# Comprehensions and Transformations

**ID:** `ex-07`  
**Level:** L2  
**Module path:** `00-python-engineering-reset/exercises/ex-07`

## Objective

Use comprehensions and map/filter style clearly.

## Prerequisites

- list/dict comprehensions

## Requirements

- From list of sentences, produce word frequency dict ignoring case and punctuation (define punctuation set).
- Implement same with at least one comprehension and one loop version; compare readability in comment.

## Constraints

- No collections.Counter

## Expected behavior

- 'Hello hello' counts hello twice

## Edge cases

- Empty sentence list
- Punctuation-only tokens

## Acceptance criteria

- Both versions pass same tests

## Common mistakes

- Not normalizing case
- Empty string keys

## H1 hint

Tokenize by splitting and stripping punctuation per word.

## Files

Create your own `.py` files in this folder unless the exercise provides a starter.

## Hints elsewhere

See [HINTS.md](../../../HINTS.md) for H2/H3 on marked exercises (`ex-07`).
