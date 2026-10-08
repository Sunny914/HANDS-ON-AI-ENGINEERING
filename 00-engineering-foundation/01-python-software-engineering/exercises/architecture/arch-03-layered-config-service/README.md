# Layered Service with Config

**ID:** `arch-03`  
**Level:** Architecture  
**Module path:** `01-python-software-engineering/exercises/architecture/arch-03-layered-config-service`

## Objective

Combine config, logging, exceptions in one app.

## Prerequisites

- ex-10–12

## Requirements

- Feature: import CSV users, dedupe by email, save JSON report.
- Full logging and settings.

## Constraints

- No monolith >400 lines in one file

## Expected behavior

- Dedupe policy documented

## Edge cases

- malformed csv rows

## Acceptance criteria

- Compare REFERENCE.md

## Common mistakes

- Config read in repository

## H1 hint

Dependency injection via constructor parameters.

## Files

REQUIREMENTS.md, REFERENCE.md.

## Hints elsewhere

See [HINTS.md](../../../HINTS.md) for H2/H3 on marked exercises (`arch-03`).
