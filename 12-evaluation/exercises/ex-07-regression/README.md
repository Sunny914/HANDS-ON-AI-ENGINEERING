# Regression on a Frozen Dataset

**ID:** `ex-07`
**Stage:** 12-evaluation
**Difficulty:** L4
**Category:** Integration

## Objective

Compare two configs without moving the labels.

## Prerequisites

ex-01. ex-04 or ex-05.

## Problem

Build a report for a baseline config and a candidate config. List regressions.

## Requirements

Both reports store `dataset_version` and `config_id`. A regression is a case that passed baseline and failed candidate. Differing dataset versions refuse the comparison with a named error. Store the reports as files so a second process can reload them.

## Constraints

At least three cases. Offline.

## Inputs and outputs

Two prediction files and one dataset.

## Edge cases

Candidate fails a new case the baseline never had. All cases pass. Baseline already failed a case the candidate also fails.

## Errors

A case failed in both is not a regression. It can still be listed as a known failure.

## Acceptance criteria

Tests for one regression, a version mismatch, and a known failure that is not called a regression.

## Testing

Filesystem and unit tests.

## Common mistakes

Comparing mean scores only and hiding which case broke.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

Why is a higher mean allowed to ship when one safety case regressed? Say whether your gate allows that.

## Extension

Record latency per case without letting latency replace the pass bit.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-07` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
