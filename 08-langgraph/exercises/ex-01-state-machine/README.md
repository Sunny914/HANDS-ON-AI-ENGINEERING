# State Machine Without LangGraph

**ID:** `ex-01`
**Stage:** 08-langgraph
**Difficulty:** L1
**Category:** Focused implementation

## Objective

Name the next node from state alone.

## Prerequisites

CONCEPTS.md before-LangGraph section. Stage 07 stop reasons.

## Problem

States have `needs_more` and `loops`. Route to `collect` or `end`.

## Requirements

Pure `route` and `apply` functions. `apply` increments `loops` when the node is collect. Never route to collect when `loops` is already at the max.

## Constraints

No langgraph import.

## Inputs and outputs

State in. Next name and new state out.

## Edge cases

needs_more true at the max. needs_more false at zero.

## Errors

Unknown node name raises.

## Acceptance criteria

Four route tests, including the ceiling.

## Testing

Unit tests.

## Common mistakes

A while loop that hides the route.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

What did you have to put in state so the route could stop?

## Extension

Add a `failed` flag that routes to `end` immediately.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-01` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
