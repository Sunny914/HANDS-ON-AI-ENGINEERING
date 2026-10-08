# Custom Iterator

**ID:** `ex-06`  
**Level:** L2  
**Module path:** `01-python-software-engineering/exercises/ex-06`

## Objective

Implement iterator protocol.

## Prerequisites

- iter
- next

## Requirements

- Class `Range` or `BatchIterator` over a sequence with given batch size.

## Constraints

- No itertools.batched unless you reimplement first

## Expected behavior

- for-loop works

## Edge cases

- empty seq
- batch size > len

## Acceptance criteria

- StopIteration at end

## Common mistakes

- Infinite loop
- reusing exhausted iterator

## H1 hint

Separate iterator state from collection.

## Files

Create your own `.py` files in this folder unless the exercise provides a starter.

## Hints elsewhere

See [HINTS.md](../../../HINTS.md) for H2/H3 on marked exercises (`ex-06`).
