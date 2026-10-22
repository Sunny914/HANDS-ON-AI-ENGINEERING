# Allow-list and Argument Schema

**ID:** `ex-03`
**Stage:** 14-security-guardrails
**Difficulty:** L3
**Category:** Integration

## Objective

Validate before any fake side effect.

## Prerequisites

ex-02. Stage 05 schemas.

## Problem

A gateway checks the role allow-list and a schema, then calls the tool.

## Requirements

Unknown tools and unknown roles fail closed. `read` requires `record_id`. `send` requires `recipient` and `body` and is not on the research allow-list. The tool function is not called when validation fails.

## Constraints

Fake tools with counters.

## Inputs and outputs

Role, tool name, arguments.

## Edge cases

Extra argument. Missing argument. Empty string id.

## Errors

Return field errors. Counter stays 0.

## Acceptance criteria

Research read with an id increments once. Research read without an id increments zero times. Research send increments zero times.

## Testing

Unit tests.

## Common mistakes

Calling the tool inside the validator's exception handler.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

Where does semantic validation, such as a maximum length, belong relative to the schema?

## Extension

Reject a recipient that is not in a fixture address book.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-03` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
