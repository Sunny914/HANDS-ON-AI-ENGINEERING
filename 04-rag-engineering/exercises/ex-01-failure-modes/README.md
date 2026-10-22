# RAG Failure Modes

**ID:** `ex-01`
**Stage:** 04-rag-engineering
**Difficulty:** L1
**Category:** Conceptual reasoning

## Objective

Separate retrieval failures from generation failures.

## Prerequisites

CONCEPTS.md through the retrieval section.

## Problem

Write `FAILURES.md`. For each symptom, say which component you would inspect first and what evidence you would want.

## Requirements

At least six symptoms: missing sentence at a boundary, empty retrieval, wrong document because metadata was ignored, high similarity but wrong fact, answer not supported by the chunks, citation id that was not retrieved.

## Constraints

No implementation.

## Inputs and outputs

A markdown note.

## Edge cases

Include one case where calling the model is the wrong next step.

## Errors

Do not propose a new framework as the fix.

## Acceptance criteria

Each symptom names a component from ARCHITECTURE_GUIDE.md.

## Testing

Read it a day later and see if each line is testable.

## Common mistakes

One row that says only 'tweak the prompt'.

## Completion checklist

- [ ] Behavior matches the acceptance criteria
- [ ] Tests you were asked to write are present and passing
- [ ] You can explain the design without reading the hint file

## Reflection

Which failure can a golden retrieval set catch that an answer screenshot cannot?

## Extension

Add a column for the log field you would want.

## Hints

Attempt the exercise before opening hints. In [../../HINTS.md](../../HINTS.md), read only the `ex-01` section, and stop at the first level that unblocks you.

- H1 is a concept
- H2 is structure
- H3 is a next step, not a finished implementation
- H4 is a review of your attempt. Bring the code to a reviewer. This file does not contain that review.
