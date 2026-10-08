# Introducing async/await

**ID:** `ex-02`  
**Level:** L2  
**Module path:** `02-async-python-preview/exercises/ex-02`

## Objective

Bridge async concepts toward Stage 01.

## Prerequisites

- asyncio docs skim

## Requirements

- Rewrite one fetch as async sleep; run with asyncio.run.
- Use asyncio.sleep not time.sleep in async exercises

## Constraints

- No real HTTP unless extension

## Expected behavior

- Documented timings

## Edge cases

- empty url list
- timeout shorter than sleep

## Acceptance criteria

- Runnable script or module

## Common mistakes

- Blocking sleep in async def
- forgetting await

## H1 hint

Blocking call inside async def blocks the event loop.

## Files

Create your own `.py` files in this folder unless the exercise provides a starter.

## Hints elsewhere

See [HINTS.md](../../../HINTS.md) for H2/H3 on marked exercises (`ex-02`).
