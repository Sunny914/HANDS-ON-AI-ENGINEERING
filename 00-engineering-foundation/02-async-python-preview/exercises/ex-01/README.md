# Blocking Sequential Fetch Simulation

**ID:** `ex-01`  
**Level:** L1  
**Module path:** `02-async-python-preview/exercises/ex-01`

## Objective

Bridge async concepts toward Stage 01.

## Prerequisites

- asyncio docs skim

## Requirements

- Implement `fetch_all(urls)` using `time.sleep` to simulate latency sequentially; print total time.
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

See [HINTS.md](../../../HINTS.md) for H2/H3 on marked exercises (`ex-01`).
