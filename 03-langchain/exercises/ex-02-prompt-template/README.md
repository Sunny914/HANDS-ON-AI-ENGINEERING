# ChatPromptTemplate

**ID:** `ex-02`
**Stage:** 03-langchain
**Difficulty:** L2
**Category:** Focused implementation

## Objective

Build the same prompt as a ChatPromptTemplate.

## Prerequisites

ex-01.

## Problem

Recreate the system and human messages as a template. Inspect messages without a model.

## Requirements

Variables for excerpt and question. Invoke or format_messages. Assert roles and that the excerpt appears only in the human message.

## Constraints

`langchain_core.prompts.ChatPromptTemplate`. No LLMChain.

## Inputs and outputs

Variable dict in. Messages out.

## Edge cases

Missing key raises the framework's error. Do not catch it in this exercise. Test that it raises.

## Errors

Missing variable is a test, not a silent empty string.

## Acceptance criteria

Message roles and contents are asserted.

## Testing

No model.

## Common mistakes

String concatenation plus a template you never invoke.

## Completion checklist

- [ ] Behavior matches the acceptance criteria
- [ ] Tests you were asked to write are present and passing
- [ ] You can explain the design without reading the hint file

## Reflection

Which bug is easier to see in messages than in one blob of text?

## Extension

Add a placeholder for prior turns, unused in the default test.

## Hints

Attempt the exercise before opening hints. In [../../HINTS.md](../../HINTS.md), read only the `ex-02` section, and stop at the first level that unblocks you.

- H1 is a concept
- H2 is structure
- H3 is a next step, not a finished implementation
- H4 is a review of your attempt. Bring the code to a reviewer. This file does not contain that review.
