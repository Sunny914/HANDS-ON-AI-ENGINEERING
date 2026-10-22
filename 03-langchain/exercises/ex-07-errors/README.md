# Errors Around ainvoke

**ID:** `ex-07`
**Stage:** 03-langchain
**Difficulty:** L4
**Category:** Integration

## Objective

Separate bad input, timeouts, and parser failures.

## Prerequisites

ex-04 and ex-06.

## Problem

An async function `answer(excerpt, question, chain)` validates input, awaits the chain, and maps failures to three named errors.

## Requirements

Empty excerpt does not call the chain. A fake that raises a timeout becomes your timeout error. Prose becomes your parse error when the chain includes a parser.

## Constraints

Use `ainvoke` or `astream` on the async path. Do not call the sync `invoke` from inside `async def`.

## Inputs and outputs

Strings in. Text or typed error.

## Edge cases

Whitespace excerpt. Question longer than a limit you set.

## Errors

Three distinct types.

## Acceptance criteria

Three tests, one per type. The empty-excerpt test asserts the fake was not called.

## Testing

Async pytest.

## Common mistakes

One `except Exception` that returns an empty summary.

## Completion checklist

- [ ] Behavior matches the acceptance criteria
- [ ] Tests you were asked to write are present and passing
- [ ] You can explain the design without reading the hint file

## Reflection

Which of these errors should an HTTP layer turn into 422 versus 503?

## Extension

Add a deadline using `asyncio.wait_for` around `ainvoke`.

## Hints

Attempt the exercise before opening hints. In [../../HINTS.md](../../HINTS.md), read only the `ex-07` section, and stop at the first level that unblocks you.

- H1 is a concept
- H2 is structure
- H3 is a next step, not a finished implementation
- H4 is a review of your attempt. Bring the code to a reviewer. This file does not contain that review.
