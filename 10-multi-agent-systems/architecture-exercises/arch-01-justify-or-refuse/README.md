# Justify or Refuse Multi-Agent

**ID:** `arch-01`
**Stage:** 10-multi-agent-systems
**Difficulty:** L4
**Category:** Architecture

## Objective

Decide whether the stage project deserves more than one agent.

## Prerequisites

ex-03. Stage 09 ADR.

## Problem

Write `ADR.md` for the research system in the project brief. Compare a fixed workflow, the Stage 09 single agent, and a coordinator with specialists.

## Requirements

The decision may pick multi-agent only with a boundary you can test: different tool allow-lists, a conflict rule, and a hop limit. Include the measurement that would make you collapse back to one agent. Include one task shape inside the same product that must stay a workflow.

## Constraints

No implementation in this exercise.

## Inputs and outputs

An ADR.

## Edge cases

The fixture corpus is small. Say whether that weakens the case for specialists.

## Errors

Do not treat framework support as a reason.

## Acceptance criteria

The ADR names a losing alternative, a hop limit, a conflict rule, and a rollback to one agent.

## Testing

Not code. Read it against the project requirements after you draft it.

## Common mistakes

An ADR that only lists role names.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

What did Stage 09's ADR refuse that this one reopens?

## Extension

Add a cost sketch: extra system prompts per specialist.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `arch-01` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
