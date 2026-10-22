# Same Task, Two Controllers

**ID:** `ex-08`
**Stage:** 07-agent-fundamentals
**Difficulty:** L4
**Category:** Architecture comparison

## Objective

Implement a fixed pipeline and a loop for one toy corpus.

## Prerequisites

ex-02 and ex-04.

## Problem

Corpus has two notes. The workflow always searches, reads the first id, and formats a sentence. The agent follows a script that may finish after search.

## Requirements

Both return a result type with a `mode` field. Tests show the workflow's tool order and the agent's early stop.

## Constraints

Share the fake tools. Do not share a hidden global step counter.

## Inputs and outputs

Question in. Result out.

## Edge cases

Search returns no ids. Workflow must stop without calling read. Agent script that still says read gets a not-found observation.

## Errors

Neither mode calls the network.

## Acceptance criteria

Order test for the workflow. Early-finish test for the agent. Empty-search test.

## Testing

One corpus fixture.

## Common mistakes

Copying the agent loop into the workflow and ignoring the script only in comments.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

Which mode would you ship for this corpus, and why?

## Extension

Write five lines on what would force you to switch modes.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-08` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
