# Stage 00 — Engineering Foundation

**Objective:** Rebuild the ability to take a problem, design a Python solution, structure it into modules, implement it, test it, debug it, and explain the architecture—not to relearn syntax from a textbook.

## Outcomes

By the end of this stage you should be able to:

- Start a Python project from an empty directory
- Choose project structure and separate responsibilities across modules
- Use core Python fluently (data structures, functions, OOP, dataclasses, typing)
- Handle exceptions, files, and JSON correctly
- Use iterators, generators, decorators, and context managers when they earn their place
- Configure a project, log meaningfully, and test with pytest
- Debug your own code and use Git with discipline
- Explain how modules interact and where data flows

## How to work this stage

1. Read [ROADMAP.md](./ROADMAP.md) for order and pacing.
2. Skim [CONCEPTS.md](./CONCEPTS.md) for what you must understand before each module (not a video list).
3. Use [IMPLEMENTATION_WORKFLOW.md](./IMPLEMENTATION_WORKFLOW.md) for every implementation exercise and mini-project.
4. When stuck, use [HINTS.md](./HINTS.md) at **H1 → H2 → H3** only (see [AI_TRAINING_RULES.md](../AI_TRAINING_RULES.md)).
5. Complete [CHECKPOINT.md](./CHECKPOINT.md) before declaring Stage 0 done.

## Modules

| Order | Directory | Focus |
|-------|-----------|--------|
| 1 | [00-python-engineering-reset](./00-python-engineering-reset/) | Fluency refresh: data, functions, scope, I/O, modules, basic OOP |
| 2 | [01-python-software-engineering](./01-python-software-engineering/) | Structure, typing, advanced Python, config, logging, pytest, architecture |
| 3 | [02-async-python-preview](./02-async-python-preview/) | Bridge to Stage 01: blocking vs async, tasks, gather, timeouts |

## Mini-projects

Complete **both** after modules 00–01 (module 02 can run in parallel or just before Stage 01). Complete architecture checkpoints in [checkpoints/](./checkpoints/) first.

| # | Project | Directory |
|---|---------|-----------|
| 1 | CLI Task & Job Management System | [mini-projects/01-cli-task-job-manager](./mini-projects/01-cli-task-job-manager/) |
| 2 | Log Analysis & Reporting CLI | [mini-projects/02-log-analysis-cli](./mini-projects/02-log-analysis-cli/) |

## Supporting guides

| Guide | Use when |
|-------|----------|
| [ARCHITECTURE_GUIDE.md](./ARCHITECTURE_GUIDE.md) | Deciding where code lives |
| [DEBUGGING_GUIDE.md](./DEBUGGING_GUIDE.md) | Diagnosing broken starters |
| [TESTING_GUIDE.md](./TESTING_GUIDE.md) | Writing pytest suites |
| [GIT_WORKFLOW.md](./GIT_WORKFLOW.md) | Commits and milestones |
| [DRILLS.md](./DRILLS.md) | Optional 15-minute fluency refresh |

## Difficulty mix (stage-wide)

Roughly **30%** fluency, **30%** intermediate, **25%** integration, **15%** debugging/architecture. Later exercises should feel like small software problems, not syntax drills.

## Rules reminder

- **You** implement all solution code.
- Starter `.py` files in exercises are either empty (TODO comments only) or **deliberately broken** in `debugging/` folders.
- Reference architectures for architecture exercises live in `REFERENCE.md`—open only **after** your design is written down.

## Suggested Git milestones

```text
docs: stage-00 start
feat: module-00 ex-05 functions
test: module-01 testing exercises
fix: debug exercise dbg-03
feat: mini-project-01 storage layer
```

Do not rush. Depth beats speed.
