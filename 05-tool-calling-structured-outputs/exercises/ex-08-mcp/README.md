# MCP as a Boundary

**ID:** `ex-08`
**Stage:** 05-tool-calling-structured-outputs
**Difficulty:** L4
**Category:** Conceptual reasoning

## Objective

Describe MCP without pretending a tutorial is the protocol.

## Prerequisites

ex-03 and CONCEPTS.md MCP section.

## Problem

Write `MCP_NOTES.md`. Explain list-tools and call-tool in terms of your registry and executor. Say what would be unsafe if the host skipped your policy.

## Requirements

Include a mapping from your `GetOrderArgs` schema to a tool descriptor. If you read the MCP SDK, record the version and one API name you verified. If you do not install it, say so. Either choice can pass.

## Constraints

A running MCP server is not required.

## Inputs and outputs

Notes, plus an optional descriptor dict in a test if you want one.

## Edge cases

A tool with a side effect must say that retries are the server's problem to make idempotent.

## Errors

Do not claim a function signature you did not check.

## Acceptance criteria

The notes mention validation and authorization as the server's job, not the model's.

## Testing

Optional unit test that your descriptor includes the tool name. Otherwise the note is the deliverable.

## Common mistakes

Installing a random SDK and copying an agent demo.

## Completion checklist

- [ ] Behavior matches the acceptance criteria
- [ ] Tests you were asked to write are present and passing
- [ ] You can explain the design without reading the hint file

## Reflection

What did Stage 01's service boundary have in common with an MCP server?

## Extension

Sketch a stdio message pair in JSON. Do not open a socket unless you want a personal experiment outside the acceptance criteria.

## Hints

Attempt the exercise before opening hints. In [../../HINTS.md](../../HINTS.md), read only the `ex-08` section, and stop at the first level that unblocks you.

- H1 is a concept
- H2 is structure
- H3 is a next step, not a finished implementation
- H4 is a review of your attempt. Bring the code to a reviewer. This file does not contain that review.
