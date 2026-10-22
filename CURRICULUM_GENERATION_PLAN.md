# Curriculum Generation Plan

This is the audit and the plan for scaffolding.

**Batch A status:** Stages 01–05 were scaffolded after review. They contain specifications, broken debugging starters, and project documents. They do not contain completed implementations.

**Batch B status:** Stages 06–11 were scaffolded after review. They contain specifications, broken debugging starters, and project documents. They do not contain completed implementations.

**Batch C status:** Stages 12–16 were scaffolded after review. They contain specifications, broken debugging starters where a stage teaches a local defect, and project documents. They do not contain completed implementations. Do not treat any batch as learner progress.

The original audit below described Stages 01–16 as placeholders. That was true on the audit date. Batch A changed Stages 01–05 only. Batch B changed Stages 06–11 only. Batch C changed Stages 12–16 only.

Governing documents:

- [CURRICULUM_CONSTITUTION.md](./CURRICULUM_CONSTITUTION.md)
- [MASTER_ROADMAP.md](./MASTER_ROADMAP.md)
- [LEARNING_PROTOCOL.md](./LEARNING_PROTOCOL.md)
- [EXERCISE_AND_PROJECT_STANDARDS.md](./EXERCISE_AND_PROJECT_STANDARDS.md)

## Audit date

2026-10-21. Findings below were checked against the working tree, not against an assumed layout.

## Repository state

| Path | State |
|------|--------|
| `README.md` | Present. Updated only to link the governing documents and to stop saying that later stages will never be pre-scaffolded. |
| `AI_TRAINING_RULES.md` | Present. A short pointer was added so hint levels follow `LEARNING_PROTOCOL.md`. The rest of the file was left in place. |
| `PROGRESS.md` | Present. Not edited in this run. |
| `00-engineering-foundation/` | Scaffolded curriculum, about 148 files. |
| `01-backend-api-engineering/` through `16-integration-capstones/` | One placeholder file each. No exercises, no projects, no stage README. |
| `.qodo/` | Empty directory. Left untouched. Purpose was not verified. |

No `CURRICULUM_CONSTITUTION.md`, `MASTER_ROADMAP.md`, `LEARNING_PROTOCOL.md`, `EXERCISE_AND_PROJECT_STANDARDS.md`, or `CURRICULUM_GENERATION_PLAN.md` existed before this run. Stage 00 documents were not treated as substitutes, because they govern one stage rather than the whole roadmap.

## Stage 00 inventory (preserve)

Do not regenerate, reformat, or move this stage.

**Guides already present:** `README.md`, `ROADMAP.md`, `CONCEPTS.md`, `DRILLS.md`, `ARCHITECTURE_GUIDE.md`, `IMPLEMENTATION_WORKFLOW.md`, `DEBUGGING_GUIDE.md`, `TESTING_GUIDE.md`, `GIT_WORKFLOW.md`, `HINTS.md`, `CHECKPOINT.md`.

**Modules:**

| Module | Material |
|--------|----------|
| `00-python-engineering-reset/` | 23 exercise READMEs, `GETTING_STARTED.md`, commented starters for ex-01 and ex-02, intentionally broken programs for ex-17 through ex-20 |
| `01-python-software-engineering/` | 12 core exercises, 3 architecture exercises with requirements and reference docs, 5 testing specs, 5 debugging exercises with broken code and local hints |
| `02-async-python-preview/` | 6 exercise READMEs. This is a bridge, not Stage 01. |
| `mini-projects/` | CLI task manager and log-analysis CLI. Specs exist. `src/` files are comment-only scaffolds. |
| `checkpoints/` | Architecture questions for both mini-projects. Learner answer files were not present. |
| `tools/_generate_exercise_readmes.py` | Maintainer script. Do not rerun it as part of curriculum generation. It rewrites exercise READMEs. |

**Learner work that must stay as-is:**

| File | Why it is protected |
|------|---------------------|
| `00-engineering-foundation/00-python-engineering-reset/exercises/ex-01/solution.py` | Contains the learner's `describe_value` and `safe_add` implementation and manual prints. |
| `00-engineering-foundation/00-python-engineering-reset/exercises/ex-01/YOUR_ATTEMPT_NOTES.md` | Feedback on an earlier attempt. |
| `00-engineering-foundation/00-python-engineering-reset/exercises/ex-02/solution.py` | Starter that may have been opened by the learner. It still has `NotImplementedError`. Do not overwrite it to be safe. |
| `PROGRESS.md` | Learner progress log. |

`ex-01/solutions.py` was present in an earlier session and is not in the tree now. It was not recreated.

Stage 00 is not complete. `PROGRESS.md` still shows the stage as not reviewed. ex-01 has an implementation that does not yet match the README key `type_name`. That is a learning gap, not a file to fix during scaffolding.

## Known inconsistencies

These were recorded, not silently rewritten.

| Topic | What the repo says | What the governing docs now say |
|-------|--------------------|---------------------------------|
| Stage 00 project name | The checklist now names the CLI Task & Job Management System and the Log Analysis & Reporting CLI. An earlier label was "Async API Aggregator". | Those two titles are the project specifications. Review boxes were not checked. |
| Stage 03 project name | The checklist now says Modular LangChain Document Assistant. An earlier label was "LangChain-Powered Document Assistant". | The project README uses the modular name. The stage folder was not rewritten for the label change. |
| Stage 15 project label | The checklist and the project directory now use Production-Style AI Agent Service. An earlier checklist label was "Deploy AI Agent (production-style)". | The project specification is `15-production-ai-infrastructure/mini-projects/production-style-ai-agent-service/`. Review boxes were not checked. |
| Hint levels | `AI_TRAINING_RULES.md` body still describes the original H0–H4 scale | [LEARNING_PROTOCOL.md](./LEARNING_PROTOCOL.md) is the current scale. A pointer was added at the top of the rules file. |
| Stage 00 exercise template | Shorter README sections, local level labels | Future stages use [EXERCISE_AND_PROJECT_STANDARDS.md](./EXERCISE_AND_PROJECT_STANDARDS.md). Stage 00 is not retrofitted. |
| Root README, before this run | Said stages would be filled only when study began | Batch scaffolding is now the plan. The README sentence was updated so it does not contradict this file. |

`PROGRESS.md` was left unchanged during the original audit so the learner's log was not rewritten then. A later audit aligned the Stage 00 and Stage 03 checklist titles with the project specifications. Review boxes were not checked.

## Generation batches

Run these only after review. Each batch starts by reading the governing documents and listing the target directories again.

### Batch A — Stages 01–05

Backend and API engineering, LLM fundamentals, LangChain, RAG, tool calling.

**Depends on:** Stage 00 remaining the prerequisite in each stage README. No Stage 00 edits.

**Each stage delivers:**

- README with objectives, prerequisites, concept-first notes, and the next action
- A short concept guide
- A focused set of exercises across implementation, integration, testing or debugging, and architecture
- Hint sections that do not reveal H3 immediately
- One mini-project specification using the project document set, combined where a separate file would only repeat the README
- A mastery checkpoint
- Comment-only scaffolds only where a project needs files to exist
- Progress entries set to `NOT STARTED` if `PROGRESS.md` is updated

**Does not deliver:** working exercise solutions, filled TODOs, or a claim that the learner completed anything.

### Batch B — Stages 06–11

Memory, agent fundamentals, LangGraph, single-agent engineering, multi-agent systems, human-in-the-loop.

Same stage package as Batch A. Projects must build on the earlier gateway, RAG, and tool-use ideas without forcing the learner to rewrite those systems line for line. Multi-agent material must require a reason to add agents.

### Batch C — Stages 12–16

Evaluation, observability, security, production infrastructure, and capstone specifications.

Same stage package. Capstones are specifications and architecture exercises, not implementations. Infrastructure topics that are only industrial name-drops stay conceptual unless the stage objective needs them.

## Rules for every future batch

1. Read the governing documents and the existing stage folder before writing.
2. Follow [EXERCISE_AND_PROJECT_STANDARDS.md](./EXERCISE_AND_PROJECT_STANDARDS.md).
3. Respect dependencies in [MASTER_ROADMAP.md](./MASTER_ROADMAP.md).
4. Do not duplicate Stage 00 Python lessons.
5. Do not generate working solutions.
6. Include testing, debugging, and an architecture checkpoint where the stage is a system.
7. Update progress tracking without marking work complete.
8. Validate files and links.
9. Report anything deferred.
10. Prefer fewer strong exercises over many empty ones.
11. Mark version-sensitive framework APIs when they were not checked against current documentation.
12. Stop if a write would overwrite a file that already contains more than a placeholder.

## Validation required after each batch

- Target stage directories contain the promised READMEs and projects.
- No Stage 00 learner file changed.
- No exercise contains a finished implementation.
- Internal links used by the new stage READMEs resolve.
- New progress rows are `NOT STARTED`.
- Concept-first sections exist for the topics named in [MASTER_ROADMAP.md](./MASTER_ROADMAP.md).
- The batch report lists deferred work.

## Unresolved decisions

1. Stage 00, 03, and 15 checklist titles were aligned to the specifications during later audits. Review boxes were not checked.
2. How deep Stage 01 database work should go before Stage 04 introduces PostgreSQL and pgvector. Default: Stage 01 teaches a small persistence boundary; Stage 04 teaches vectors.
3. Which LLM providers the Stage 02 gateway specification should name. Decide at Batch A, and keep the interface more important than any one vendor.
4. Current LangChain and LangGraph API names. Verify during Batch A and Batch B, or mark them as assumptions.
5. Whether `.qodo/` belongs in the repository. Left untouched.
6. Whether Stage 00 exercise READMEs should later gain reflection prompts. Default: no retrofit.

## This run's validation

| Check | Result |
|-------|--------|
| Stage 00 was not regenerated | Passed. No Stage 00 file was rewritten. |
| Learner-authored files were not modified | Passed. `ex-01/solution.py`, `YOUR_ATTEMPT_NOTES.md`, `ex-02/solution.py`, and `PROGRESS.md` were not opened for writing. |
| Roadmap contains 17 stages | Passed. See [MASTER_ROADMAP.md](./MASTER_ROADMAP.md). |
| Stage order is coherent | Passed, with Stages 12 and 13 allowed to overlap after a system exists. |
| Interleaved implementation is the default | Passed. Stated in the constitution and protocol. |
| Concept-first topics are identified | Passed. Listed in the constitution and on the relevant roadmap stages. |
| Standards forbid complete solutions | Passed. |
| Later batches are specified | Passed. Batches A–C above. |
| Documents contradict each other | One intentional resolution: the learning protocol supersedes the old H4 definition. The old wording remains in the body of `AI_TRAINING_RULES.md` and is flagged at the top. |
| Internal links in the new documents | Checked against paths that exist: Stage 00 guides, `PROGRESS.md`, `AI_TRAINING_RULES.md`, and the five governing files. Links to future stage READMEs were not created because those files do not exist. |
| Stages 01–16 were not scaffolded | Passed. Their directories still contain only the original placeholder. |
| No exercise implementation was generated | Passed. |

## Next action

Batches A, B, and C have been scaffolded. There is no Batch D in this plan.

When study is resumed, the next learning task is still **Stage 00, exercise ex-01**. Scaffolding and studying are different work.
