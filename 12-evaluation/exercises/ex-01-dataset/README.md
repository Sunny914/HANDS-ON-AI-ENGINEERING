# Versioned Evaluation Cases

**ID:** `ex-01`
**Stage:** 12-evaluation
**Difficulty:** L1
**Category:** Focused implementation

## Objective

Store labels separately from predictions.

## Prerequisites

[CONCEPTS.md](../../CONCEPTS.md) case section.

## Problem

Define a dataset object and a loader that rejects an unlabeled or unversioned file.

## Requirements

Each case has a unique id, a task type, and an input. A dataset has `dataset_version`. Predictions are a different list, joined later by case id. Reject duplicate ids and a missing version.

## Constraints

JSON or pydantic. No model calls.

## Inputs and outputs

A dataset file in. A dataset object or a named error out.

## Edge cases

Empty case list. Duplicate ids. A prediction id with no case.

## Errors

Do not coerce a missing version to `latest`.

## Acceptance criteria

Tests for a valid file, a duplicate id, and a missing version. A prediction is not required to load the dataset.

## Testing

Unit tests. You may copy the shape of [fixtures/retrieval_case_shape.json](../../fixtures/retrieval_case_shape.json) and add the fields this exercise requires.

## Common mistakes

Putting the model's answer into the case as the only expected field and calling that a label.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

What change forces a new dataset version?

## Extension

Add a `tags` list and reject an unknown tag from a fixed set.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-01` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
