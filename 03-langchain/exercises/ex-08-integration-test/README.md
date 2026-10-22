# Offline Integration Test

**ID:** `ex-08`
**Stage:** 03-langchain
**Difficulty:** L4
**Category:** Testing

## Objective

Test the public function, not a private prompt string only.

## Prerequisites

ex-07.

## Problem

`summarize_excerpt(path, question)` reads a small text fixture, selects the whole file, and runs an injected chain.

## Requirements

Factory accepts the model. Test uses a temp file or the fixture in this exercise folder that you create. Assert the summary string. Provide a skip path for a live model that does not run by default.

## Constraints

Selector is 'the whole file' or 'the first N characters'. No embeddings.

## Inputs and outputs

Path and question in. Summary out.

## Edge cases

Missing file. Empty file.

## Errors

Missing file is your error, not a model call.

## Acceptance criteria

Default `pytest` passes offline. The test fails if the chain is not used, which you can show by a fake that returns a sentinel.

## Testing

This is the testing exercise.

## Common mistakes

Asserting the prompt contains the filename and never running the chain.

## Completion checklist

- [ ] Behavior matches the acceptance criteria
- [ ] Tests you were asked to write are present and passing
- [ ] You can explain the design without reading the hint file

## Reflection

What would Stage 04 replace in this function?

## Extension

Select the paragraph that contains a keyword. Still no vectors.

## Hints

Attempt the exercise before opening hints. In [../../HINTS.md](../../HINTS.md), read only the `ex-08` section, and stop at the first level that unblocks you.

- H1 is a concept
- H2 is structure
- H3 is a next step, not a finished implementation
- H4 is a review of your attempt. Bring the code to a reviewer. This file does not contain that review.
