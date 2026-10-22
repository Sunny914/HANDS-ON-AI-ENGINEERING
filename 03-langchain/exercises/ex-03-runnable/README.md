# Runnable Sequence

**ID:** `ex-03`
**Stage:** 03-langchain
**Difficulty:** L2
**Category:** Focused implementation

## Objective

Connect template, fake model, and string parser with `|`.

## Prerequisites

ex-02. Confirm the fake chat model class in your install.

## Problem

The chain returns the fake's text for a question about an excerpt.

## Requirements

Factory `build_chain(model)`. Default test supplies the fake. Document the fake class name you imported.

## Constraints

LCEL. No LLMChain. No live key.

## Inputs and outputs

Same dict as ex-01. String out.

## Edge cases

Fake configured with an empty response list, if that is possible. Otherwise document the fake's limit.

## Errors

Construction errors are fixed before tests are called done.

## Acceptance criteria

`invoke` returns the scripted answer. The test fails if the parser is removed and a message object leaks to the caller, if your assertion checks type.

## Testing

One integration-style unit test with the fake.

## Common mistakes

Calling `invoke` on the prompt and thinking the model ran.

## Completion checklist

- [ ] Behavior matches the acceptance criteria
- [ ] Tests you were asked to write are present and passing
- [ ] You can explain the design without reading the hint file

## Reflection

What object exists between the model and the parser?

## Extension

Add `.with_config` tags you can see in a callback or log. Optional if callbacks are awkward. Skip rather than fake a log.

## Hints

Attempt the exercise before opening hints. In [../../HINTS.md](../../HINTS.md), read only the `ex-03` section, and stop at the first level that unblocks you.

- H1 is a concept
- H2 is structure
- H3 is a next step, not a finished implementation
- H4 is a review of your attempt. Bring the code to a reviewer. This file does not contain that review.
