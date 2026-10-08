# Stage 00 Roadmap

Work in order unless you have a specific gap to close. Each module ends with integration-style work; the stage ends with two mini-projects and the [final checkpoint](./CHECKPOINT.md).

## Phase A — Fluency reset (Module 00)

**Directory:** `00-python-engineering-reset/`

| Block | Exercises | Levels | Est. effort |
|-------|-----------|--------|-------------|
| A1 | ex-01 → ex-05 | L1 | 1–2 sessions |
| A2 | ex-06 → ex-10 | L2 | 2 sessions |
| A3 | ex-11 → ex-14 | L3 | 2 sessions |
| A4 | ex-15 → ex-16, ex-21 | L4 | 2–3 sessions |
| A5 | ex-17 → ex-20, ex-22 → ex-23 | L5 + integration | 2–3 sessions |

**Exit criteria:** You can implement multi-step data manipulation without looking up basic syntax; you can split code into modules; you can fix provided broken programs and explain why they failed.

## Phase B — Software engineering (Module 01)

**Directory:** `01-python-software-engineering/`

| Block | Exercises | Focus |
|-------|-----------|--------|
| B1 | ex-01 → ex-05 | Functions → modules → dataclasses → typing |
| B2 | ex-06 → ex-09 | Iterators, generators, decorators, context managers |
| B3 | ex-10 → ex-12 | Config, logging, custom exceptions |
| B4 | `testing/*` | Write tests from natural-language requirements |
| B5 | `architecture/*` | Design before structure; compare to reference after |
| B6 | `debugging/*` | Diagnose broken multi-file programs |
| B7 | ex-10 → ex-12 overlap + ex-11 capstone in module README | Multi-module integration |

**Exit criteria:** Multi-file package with config, logging, tests; you can defend module boundaries in writing.

## Phase C — Async preview (Module 02)

**Directory:** `02-async-python-preview/`

Complete **after** B4 (testing basics) and **before** Stage 01. Six exercises ending in sequential vs concurrent comparison.

**Exit criteria:** You can explain blocking vs awaiting, when `gather` helps, and what a timeout protects.

## Phase D — Architecture checkpoints

Before each mini-project, complete (in writing):

- [checkpoints/architecture-before-mini-project-1.md](./checkpoints/architecture-before-mini-project-1.md)
- [checkpoints/architecture-before-mini-project-2.md](./checkpoints/architecture-before-mini-project-2.md)

Store your answers in `checkpoints/your-answers/` (create that folder yourself).

## Phase E — Mini-projects

| Order | Project | Depends on |
|-------|---------|------------|
| E1 | CLI Task & Job Management | Modules 00–01, checkpoint 1 |
| E2 | Log Analysis & Reporting CLI | Modules 00–01, checkpoint 2; generators/logging from 01 |

Optional: revisit module 02 between E1 and E2 if you want async fresh before Stage 01.

## Phase F — Final checkpoint

Complete [CHECKPOINT.md](./CHECKPOINT.md) **Stage 0 Final**. Honest self-assessment plus a short architecture explanation for one mini-project (your choice).

## Pacing guidance

| Pace | Calendar (indicative) |
|------|------------------------|
| Focused | 3–5 weeks |
| Part-time | 6–10 weeks |

Adjust by depth: if an architecture exercise takes a full evening, that is expected.

## What comes next

**Stage 01 — Backend & API Engineering** builds on async preview and software engineering habits (FastAPI, HTTP, reliability patterns).
