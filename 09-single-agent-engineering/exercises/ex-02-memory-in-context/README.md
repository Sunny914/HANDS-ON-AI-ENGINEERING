# Memory in the Loop

**ID:** `ex-02`
**Stage:** 09-single-agent-engineering
**Difficulty:** L3
**Category:** Integration

## Objective

Use Stage 06 assembly inside the agent step.

## Prerequisites

Stage 06 ex-07. ex-01.

## Problem

Before each scripted model step, build context from memories and a budget.

## Requirements

Hostile or oversized memories follow Stage 06 rules. The loop still stops on the script.

## Constraints

Do not reimplement vector search.

## Inputs and outputs

Memories, budget, script.

## Edge cases

No memories. One memory larger than the budget.

## Errors

A rejected memory never appears in the data block.

## Acceptance criteria

Omission test and system-text stability test.

## Testing

Fakes.

## Common mistakes

Stuffing memory into the tool arguments.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

What memory should this research agent refuse to load?

## Extension

Log omitted ids on the trace.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-02` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
