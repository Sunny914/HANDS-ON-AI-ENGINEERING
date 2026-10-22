# Parse a Proposed Action

**ID:** `ex-03`
**Stage:** 07-agent-fundamentals
**Difficulty:** L2
**Category:** Focused implementation

## Objective

Turn model-shaped JSON into a tool action or a final answer.

## Prerequisites

ex-02.

## Problem

Accept a dict with `type` of `tool` or `final`. Reject anything else.

## Requirements

Tool actions name a registered tool and include an arguments object. Final actions include an answer string and a list of citation ids, which may be empty only if you document that as invalid for research.

## Constraints

Parser does not execute.

## Inputs and outputs

Dict in. Action object or parse error.

## Edge cases

Missing type. Tool name not registered. Final with no answer.

## Errors

Parse error type is specific.

## Acceptance criteria

Valid tool, valid final, unknown type, unknown tool name.

## Testing

Unit tests. One source is the stage fixture [`../../fixtures/script_finish.json`](../../fixtures/script_finish.json). Parse each object in `steps`. The file is an example script, not a parser.

## Common mistakes

`eval` on a string action.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

Why is a final answer still untrusted text?

## Extension

Accept JSON inside a fence, reusing the Stage 02 habit, and reject prose.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-03` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
