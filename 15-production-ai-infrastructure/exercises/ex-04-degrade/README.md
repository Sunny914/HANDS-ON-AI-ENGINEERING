# Degrade without Weakening Policy

**ID:** `ex-04`
**Stage:** 15-production-ai-infrastructure
**Difficulty:** L3
**Category:** Integration

## Objective

Keep authorization when the model is unavailable.

## Prerequisites

Stage 14 allow-list. ex-03.

## Problem

A down adapter changes the model path and not the deploy path.

## Requirements

A local read can return a fixture note when the adapter raises unavailable. Deploy does not run. Its result says unavailable or denied, and the ledger counter stays 0.

## Constraints

Fake adapter and fake ledger.

## Inputs and outputs

A request type and an adapter.

## Edge cases

Adapter up and deploy still needs approval. Adapter down and read. Adapter down and deploy.

## Errors

Do not map adapter failure to HTTP 200 with an empty deploy.

## Acceptance criteria

Read succeeds from the store. Deploy does not append. An up-adapter deploy without approval still does not append.

## Testing

Unit tests.

## Common mistakes

Skipping the authorizer in the except block.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

What would a second model provider be allowed to change?

## Extension

Return a partial body that says the summary was skipped.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-04` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
