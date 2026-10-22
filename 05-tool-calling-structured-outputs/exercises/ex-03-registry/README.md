# Tool Registry

**ID:** `ex-03`
**Stage:** 05-tool-calling-structured-outputs
**Difficulty:** L2
**Category:** Focused implementation

## Objective

Look up tools by name without dynamic execution of strings.

## Prerequisites

ex-02.

## Problem

Register the two tools. Store the model, a description, and a callable. Unknown names raise `UnknownTool`.

## Requirements

The callable can be a stub that raises `NotImplementedError`. Registration itself must work.

## Constraints

No `eval`. No importing a tool by a model-supplied module path.

## Inputs and outputs

Name in. Spec out.

## Edge cases

Duplicate registration: reject or replace. Document it.

## Errors

`UnknownTool` is asserted.

## Acceptance criteria

Both names resolve. A third name does not. Descriptions are non-empty.

## Testing

Unit tests.

## Common mistakes

A chain of if statements copied in every caller instead of one registry.

## Completion checklist

- [ ] Behavior matches the acceptance criteria
- [ ] Tests you were asked to write are present and passing
- [ ] You can explain the design without reading the hint file

## Reflection

What would be dangerous about a tool name that selects a Python attribute?

## Extension

List tools as the schemas a model prompt could be shown.

## Hints

Attempt the exercise before opening hints. In [../../HINTS.md](../../HINTS.md), read only the `ex-03` section, and stop at the first level that unblocks you.

- H1 is a concept
- H2 is structure
- H3 is a next step, not a finished implementation
- H4 is a review of your attempt. Bring the code to a reviewer. This file does not contain that review.
