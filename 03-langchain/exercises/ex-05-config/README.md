# Partials and Settings

**ID:** `ex-05`
**Stage:** 03-langchain
**Difficulty:** L3
**Category:** Integration

## Objective

Keep style and model name out of the caller's dict.

## Prerequisites

ex-03.

## Problem

The system message includes a tone loaded from settings. Callers only pass excerpt and question.

## Requirements

Build the prompt with a partial or with a factory that closes over settings. A test changes tone and reads the system message.

## Constraints

Settings object is plain Python or Pydantic. Not `os.environ` inside the template string.

## Inputs and outputs

Caller dict has two keys. Settings supply tone.

## Edge cases

Empty tone rejected at settings construction.

## Errors

A missing caller key still fails.

## Acceptance criteria

Two tones produce two different system messages. The model is not required for that assertion.

## Testing

Template-level test plus one chain test with a fake.

## Common mistakes

Asking the user to pass the tone every time so configuration is fake.

## Completion checklist

- [ ] Behavior matches the acceptance criteria
- [ ] Tests you were asked to write are present and passing
- [ ] You can explain the design without reading the hint file

## Reflection

What else belongs in settings instead of the prompt dict?

## Extension

Pass temperature via runnable config if your model fake honors it. If it does not, document that and stop.

## Hints

Attempt the exercise before opening hints. In [../../HINTS.md](../../HINTS.md), read only the `ex-05` section, and stop at the first level that unblocks you.

- H1 is a concept
- H2 is structure
- H3 is a next step, not a finished implementation
- H4 is a review of your attempt. Bring the code to a reviewer. This file does not contain that review.
