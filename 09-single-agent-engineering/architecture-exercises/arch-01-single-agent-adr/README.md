# Single-Agent ADR

**ID:** `arch-01`
**Stage:** 09-single-agent-engineering
**Difficulty:** L4
**Category:** Architecture

## Objective

Defend one agent against a workflow and against a team of agents.

## Prerequisites

Stage 07 ex-08. ex-01.

## Problem

Write `ADR.md` for the research and analysis project.

## Requirements

Context, decision, alternatives, consequences. Include a case where a workflow would have been enough and why this project is slightly past that line. Include why you are not splitting research and writing into two agents yet.

## Constraints

No code.

## Inputs and outputs

ADR.

## Edge cases

The corpus is three notes. Be honest if that makes a workflow tempting.

## Errors

Do not claim quality improves because there are more model calls.

## Acceptance criteria

The decision names a cost you accept: one context, one budget, no specialist contract.

## Testing

Not code.

## Common mistakes

An ADR that only praises agents.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

What measurement would change your mind in Stage 10?

## Extension

Add a rollback plan: the workflow you would ship if the loop is flaky.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `arch-01` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
