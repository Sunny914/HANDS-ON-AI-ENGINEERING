# What Is a Node

**ID:** `arch-01`
**Stage:** 08-langgraph
**Difficulty:** L4
**Category:** Architecture

## Objective

Decide the research workflow's nodes before coding them.

## Prerequisites

ex-05 through ex-08. Stage 07 project ideas.

## Problem

Write `YOUR_DESIGN.md` for validate, plan, collect, assess, synthesize, and final check. You may merge or drop a node if you justify it.

## Requirements

For each node: state it reads, state it writes, whether it calls a model, whether it has a side effect, and how the graph stops. Include a cycle and an interrupt only if a human gate exists. This project can omit the human gate. Stage 11 owns approval.

## Constraints

No project code.

## Inputs and outputs

Design note.

## Edge cases

Assess says evidence is weak, and the loop counter is at the max.

## Errors

A failed collect node. Say whether the graph stops or retries once.

## Acceptance criteria

At least one piece of work is explicitly not a node.

## Testing

Name node tests versus graph tests.

## Common mistakes

One node called `agent` that contains the Stage 07 loop unchanged.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

What did LangGraph add that the Stage 07 function did not record?

## Extension

Mark a future interrupt point for Stage 11 without designing the whole approval system.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `arch-01` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
