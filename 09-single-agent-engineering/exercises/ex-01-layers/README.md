# Layer Interfaces

**ID:** `ex-01`
**Stage:** 09-single-agent-engineering
**Difficulty:** L3
**Category:** Architecture

## Objective

Introduce fakes at boundaries before you add behavior.

## Prerequisites

Stage 07 loop. Stage 05 registry.

## Problem

Define four narrow interfaces and a service that calls an orchestrator. The orchestrator calls a tool runner.

## Requirements

No real model. A test double records calls. The service method is `run(question)`.

## Constraints

At least four modules or clear classes. No single file named `agent.py` that does all of it.

## Inputs and outputs

Question in. A result stub out.

## Edge cases

Tool runner raises. The service returns a failure result rather than a stack to the caller.

## Errors

Name the failure type.

## Acceptance criteria

The test shows the tool runner was called and the memory store was not, for this stub question.

## Testing

Unit test with fakes.

## Common mistakes

Importing a concrete corpus inside the interface module.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

Which interface would Stage 10's supervisor replace?

## Extension

Add a fifth port for the clock.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-01` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
