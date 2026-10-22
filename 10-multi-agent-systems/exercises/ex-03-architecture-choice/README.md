# Workflow, One Agent, or Several

**ID:** `ex-03`
**Stage:** 10-multi-agent-systems
**Difficulty:** L3
**Category:** Architecture comparison

## Objective

Practice refusing a multi-agent design.

## Prerequisites

Stage 07 comparison of workflow and agent. [CONCEPTS.md](../../CONCEPTS.md).

## Problem

Write `CHOICES.md` with one decision for each scenario below. Choose deterministic workflow, single agent, or multi-agent system. Name the cost you refuse to pay.

## Requirements

Scenarios:

1. A nightly job turns CSV rows into PDF invoices with a fixed template. The mapping is already specified. No tool choice depends on the document.
2. A user asks what note 12 said about refunds. The corpus is local and the only tools are search and read.
3. A drafter proposes a reply and a checker must apply a policy checklist. The checker must not be able to send the reply. The drafter must not be able to edit the checklist.
4. Three local corpora can be searched independently, then a synthesis must cite them, and a verifier must drop citations that no search returned. Wall-clock time matters, but token cost matters too.

Draft the decisions before you read the acceptance section again.

## Constraints

No code. No claim that more agents are generally better.

## Inputs and outputs

A markdown decision record.

## Edge cases

Scenario 3 can be solved without a second model. Say so if that is your choice.

## Errors

A decision that adds agents without a boundary or a measurement is incomplete.

## Acceptance criteria

Scenario 1 must be a deterministic workflow. Multi-agent is a wrong answer there.

Scenario 2 must be a single agent or a fixed two-step workflow. Multi-agent is a wrong answer there.

Scenario 3 must keep the checker from sending and the drafter from editing the checklist. Either a two-stage workflow or two roles can pass. A design where both models share one tool allow-list fails.

Scenario 4 may be one agent with three tool calls or a bounded fan-out. The writeup must compare duplicated prompts against a single trace and must include a stop if parallel workers disagree or time out.

## Testing

Self-review against the acceptance section after the draft exists.

## Common mistakes

Choosing multi-agent for scenario 1 because the word agent appears in the course title.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

Which scenario would change your answer if the invoice template started depending on a judgment call?

## Extension

Add a fifth scenario from your own work and decide it with the same three options.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-03` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
