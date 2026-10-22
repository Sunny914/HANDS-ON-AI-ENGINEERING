# Context Packing and Citations

**ID:** `ex-06`
**Stage:** 04-rag-engineering
**Difficulty:** L3
**Category:** Integration

## Objective

Build the prompt context and the citation list from retrieved chunks.

## Prerequisites

ex-05. Stage 02 structured output.

## Problem

A builder returns the context string and the ordered citation ids. A generator function accepts that context plus a question and an injected completer. The completer is a fake. The public result includes the answer text and the citations actually used.

## Requirements

If retrieval is empty, the generator is not called and the result says the corpus had no match.

## Constraints

The completer is injected. It may be a Stage 03 chain, but LangChain is not required in this exercise.

## Inputs and outputs

Chunks in. Answer plus citation ids out.

## Edge cases

Empty chunks. A fake that cites an id you did not provide: drop it or fail. Document it.

## Errors

Do not invent a citation the retriever did not return.

## Acceptance criteria

Test empty retrieval. Test that the fake receives the chunk id in the context. Test the citation list.

## Testing

Unit tests with a fake completer.

## Common mistakes

Letting the model 'know' the answer when the context is empty.

## Completion checklist

- [ ] Behavior matches the acceptance criteria
- [ ] Tests you were asked to write are present and passing
- [ ] You can explain the design without reading the hint file

## Reflection

What can a citation not guarantee?

## Extension

Add a character budget that drops the lowest-ranked chunks first.

## Hints

Attempt the exercise before opening hints. In [../../HINTS.md](../../HINTS.md), read only the `ex-06` section, and stop at the first level that unblocks you.

- H1 is a concept
- H2 is structure
- H3 is a next step, not a finished implementation
- H4 is a review of your attempt. Bring the code to a reviewer. This file does not contain that review.
