# Exercise and Project Standards

Standards for Stages 01–16. Stage 00 already has exercises and projects. Do not rewrite them to match this template. If a later edit touches a Stage 00 file, preserve learner work inside it.

Related rules: [CURRICULUM_CONSTITUTION.md](./CURRICULUM_CONSTITUTION.md), [LEARNING_PROTOCOL.md](./LEARNING_PROTOCOL.md).

## Difficulty

| Level | Meaning |
|-------|---------|
| L1 | Foundational. One idea, a small implementation, obvious inputs. |
| L2 | Basic application. Combine two or three ideas with stated edge cases. |
| L3 | Intermediate integration. More than one module, real failure behavior, tests. |
| L4 | Advanced engineering. Design choices, external boundaries, operational concerns. |
| L5 | Capstone-level. A system with architecture, tests, and trade-offs to defend. |

Raise difficulty by adding constraints and failure modes, not by asking for more boilerplate.

## Exercise categories

Use the categories that teach the stage skill. Do not quota every category into every stage.

| Category | Learner does |
|----------|----------------|
| Conceptual reasoning | Explain a mechanism, trace, or trade-off before coding. |
| Focused implementation | Build one behavior. |
| Integration | Connect several behaviors or modules. |
| Debugging | Diagnose a failure that is not fully disclosed up front. |
| Testing | Write tests from a natural-language spec. |
| Architecture | Decide boundaries, or compare a design with a later reference. |
| Refactoring | Change structure while preserving tested behavior. |
| Independent implementation | Build from requirements without a prescribed file tree. |

A stage should contain a progression: focused work, then integration, then at least one of debugging, testing, or architecture, then a project when the stage is large enough to need one.

## What a substantive exercise contains

Use the subset that changes what the learner does. Do not paste empty headings.

- Unique ID, stage, module, and difficulty
- Learning objectives and prerequisites
- Problem statement
- Functional requirements
- Nonfunctional requirements when they matter
- Inputs, outputs, and constraints
- Relevant edge cases and error behavior
- Acceptance criteria
- Testing requirements, or an explicit statement that tests are not required
- Common mistakes
- Hints, stored so H3 is not the first thing visible
- Completion checklist
- A short reflection prompt
- An optional extension that is clearly optional

Edge cases must match the task. Candidates include missing or invalid input, empty collections, wrong types, boundaries, timeouts, partial results, duplicates, bad configuration, cleanup, and persistence failure. Do not attach the full list to every exercise.

## Specifications versus implementations

Allowed in a scaffold:

- Markdown requirements
- Comment-only Python with a responsibility, inputs, outputs, and `NotImplementedError` or an equivalent TODO
- A broken program for a debugging exercise
- Example input fixtures and expected outputs described in text
- A dependency file when the stage needs one

Not allowed:

- The completed function, class, query, client, or test the learner is supposed to write
- A hidden solution directory
- A reference implementation that can be copied into the exercise

A debugging starter may contain the bug. The learner README says that something is wrong. The defect list, if written for a mentor, lives in a clearly marked mentor note and is not linked from the first exercise instructions.

An architecture exercise either asks the learner to choose the structure, or gives a suggested structure and asks them to justify changes. If a reference architecture exists, put it in a separate file and say to open it after the learner's design.

## Mini-projects

A stage project combines several concepts and forces at least one engineering decision. It is not a single-file demo.

Before implementation, the project specification should make these available, combining files when the project is small:

| Document | Role |
|----------|------|
| README.md | What it is and how to start |
| REQUIREMENTS.md | Behavior and scope |
| ACCEPTANCE_CRITERIA.md | Done means this |
| EDGE_CASES.md | Failures and ambiguous cases |
| ARCHITECTURE.md or ARCHITECTURE_EXERCISE.md | Questions first; reference design after the attempt |
| TEST_PLAN.md | What to test, in words |
| IMPLEMENTATION_PLAN.md | Suggested slices, not code |
| DEBUGGING_GUIDE.md | How to diagnose this project |
| PROJECT_CHECKPOINT.md | The architecture and mastery questions |

Stage 00 projects already use a smaller set and lack separate implementation-plan and checkpoint files. That is acceptable. Do not add those files unless the learner asks. Later projects should include an implementation plan and a checkpoint, either as their own files or as sections in the README if splitting them would be noise.

A project is not done when the scaffold exists. Done means the learner implemented it, the acceptance criteria pass, and the checkpoint questions are answered.

## Stage package

Each future stage directory should contain enough of the following to be usable without inventing the curriculum again:

- Stage README with objectives, prerequisites, and the next action
- Concept notes that say what to understand, not a video list
- Focused and integration exercises
- Debugging or testing practice where the skill needs it
- An architecture checkpoint before the project
- One mini-project specification when the stage objective is a system
- A mastery checkpoint
- Progress rows left as `NOT STARTED`

Do not create many near-duplicate exercises. Define the set by the stage objective in [MASTER_ROADMAP.md](./MASTER_ROADMAP.md).

## Completion evidence

An exercise moves to `COMPLETED` only when:

- The acceptance criteria are met by code the learner wrote
- Required tests were run by the learner
- A reflection or checkpoint is filled in when the exercise requires one

`NEEDS REVIEW` means the code runs but the learner cannot explain it, or tests are missing. `BLOCKED` means a prerequisite or environment problem is stopping the work.

## Technology notes inside exercises

When an exercise depends on a library API:

- Say why the library is there
- Name the concept that remains if the library disappears
- Mention one real alternative
- If the API was not checked against current documentation, write that the snippet or name is an assumption

## Naming

- Stage directories keep the existing `NN-kebab-case` names.
- Exercise IDs stay stable once published: `ex-01`, `dbg-01`, `arch-01`, `test-01`.
- Project directories use `mini-projects/NN-short-name/` or a single `project/` folder if the stage has one project.
- Learner solution files, once created by the learner, are never regenerated by a curriculum task.
