# Role Contracts

**ID:** `ex-01`
**Stage:** 10-multi-agent-systems
**Difficulty:** L2
**Category:** Design

## Objective

Specify specialist boundaries before any loop exists.

## Prerequisites

Stage 05 tool schema. Stage 09 layer boundaries.

## Problem

Define contracts for four roles: coordinator, research, verification, and synthesis. Validate a result against the contract.

## Requirements

Each contract includes purpose, input fields, output fields, allowed tool names, and whether the role may delegate. Validation rejects unknown tool names and rejects delegation from every role except the coordinator. The coordinator's only tool is a delegate action the application owns, or it has no tools and delegation is a method call. Pick one and document it.

## Constraints

No live model. No network. Pydantic is allowed. A TypedDict plus a manual validator is also fine.

## Inputs and outputs

A role name and a candidate output dict in. A validated object or a named error out.

## Edge cases

Empty tool list for synthesis. Research output missing evidence ids. Extra field `grant_tools`.

## Errors

Validation failures are values the caller can branch on, not bare KeyError.

## Acceptance criteria

Tests reject a delegating research result, reject an unknown tool, and accept a synthesis result that contains only text and evidence ids.

## Testing

Unit tests on the validator.

## Common mistakes

Encoding the contract only as a system-prompt string.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

Which role is still useful if its model is replaced by a deterministic function?

## Extension

Add an analysis role that may read evidence but may not search.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-01` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
