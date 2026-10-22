# Learning Protocol

How to study in this repository, and how an assistant should behave when asked for help. Principles are in [CURRICULUM_CONSTITUTION.md](./CURRICULUM_CONSTITUTION.md). Exercise shape is in [EXERCISE_AND_PROJECT_STANDARDS.md](./EXERCISE_AND_PROJECT_STANDARDS.md).

Stage 00 already has a shorter workflow in [00-engineering-foundation/IMPLEMENTATION_WORKFLOW.md](./00-engineering-foundation/IMPLEMENTATION_WORKFLOW.md) and stage-local hints in [00-engineering-foundation/HINTS.md](./00-engineering-foundation/HINTS.md). Use those while working Stage 00. This protocol is the repository-wide rule and the rule for later stages.

## Independent implementation workflow

Use the phases that the task actually needs. A small function may take minutes. A capstone may need a written plan.

| Phase | Do this |
|-------|---------|
| 1. Understand | Read the requirements. List terms you cannot yet define. |
| 2. Analyze | Write inputs, outputs, constraints, edge cases, and failure modes. |
| 3. Design | Name modules, responsibilities, and allowed dependencies. |
| 4. Plan | Split the work into slices that can be run and tested. |
| 5. Scaffold | Create only the files the design needs. Comment TODOs are allowed. |
| 6. Implement | Write the code yourself. |
| 7. Test | Check the acceptance criteria. Add the tests the specification requires. |
| 8. Debug | Reproduce, localize, hypothesize, verify, then fix. |
| 9. Review | Check readability, types, errors, and boundaries. |
| 10. Explain | Say how data moves and why each module exists. |
| 11. Reflect | Record the mistake and the concept to revisit. |
| 12. Refactor | Change structure only while behavior stays covered by tests. |

Do not write the whole application in one pass. Finish one vertical slice, then add the next.

## Hint ladder

Ask for the lowest level that unblocks you.

| Level | What you get |
|-------|----------------|
| H1 Conceptual | The idea or mental model that matters. |
| H2 Structural | A sequence of steps, a module boundary, or an algorithmic approach. |
| H3 Implementation | The next concrete step, a relevant API, or a debugging technique. Still not the finished function. |
| H4 Attempt review | A review of **your** code or design: wrong assumptions, failing cases, and what to inspect next. |

A full worked solution is not H4. It is a separate request, and it should stay rare.

Stage 00's [AI_TRAINING_RULES.md](./AI_TRAINING_RULES.md) originally used H0 for questions and treated H4 as code-level help. That older scale still appears in Stage 00 exercise text. When the two disagree, use this protocol: questions are always allowed before H1, and H4 reviews an attempt instead of replacing it.

Keep higher hints separate from the problem statement when a new exercise is written, so the answer is not sitting under the question.

Debugging exercises must not list every defect in the learner instructions. Mentor-only defect notes, if they exist, stay out of the first README section the learner reads.

## Testing habit

Start from the required behavior, not from the code you hope is correct.

- One test should fail if the feature is reverted.
- Cover one important edge case, not every imaginable case.
- Test your logic. Mock only a real boundary such as the network, clock, or filesystem when a temp file is impractical.
- For AI behavior, separate deterministic checks from model-judged checks.
- Read [00-engineering-foundation/TESTING_GUIDE.md](./00-engineering-foundation/TESTING_GUIDE.md) for the Stage 00 version of this habit.

## Debugging habit

1. Reproduce with the smallest input.
2. Read the traceback from the last frame.
3. State one hypothesis.
4. Check it with a print, log, or breakpoint.
5. Make the smallest fix.
6. Add a regression test when the exercise has tests.

Use [00-engineering-foundation/DEBUGGING_GUIDE.md](./00-engineering-foundation/DEBUGGING_GUIDE.md) for the Stage 00 checklist. Do not ask an assistant "what is wrong with line 42?" before you have a hypothesis.

## Architecture checkpoints

Use a checkpoint before a major project and after a major integration. Do not write one for every small exercise.

Answer:

1. Problem and constraints
2. Proposed modules
3. Responsibility of each module
4. Interfaces between modules
5. Data flow
6. Error handling
7. Configuration
8. Testing
9. External dependencies
10. Reliability
11. Security implications
12. Trade-offs and alternatives

Stage 00 already asks a shorter set in [00-engineering-foundation/CHECKPOINT.md](./00-engineering-foundation/CHECKPOINT.md). Keep using that file for Stage 00. Later projects use the twelve questions above.

A reference architecture may exist, but it should be read after your own design. Several reasonable designs can pass if they meet the requirements and you can explain the trade-off.

## Mastery checkpoint

A stage or major module is not complete because its files exist. Ask:

- Can I explain the concept?
- Can I implement it without copying a solution?
- Can I handle the important edge cases?
- Can I write a meaningful test?
- Can I debug a failure from evidence?
- Can I explain the design?
- Can I integrate it with the next component?

Statuses for progress tracking:

`NOT STARTED` · `IN PROGRESS` · `NEEDS REVIEW` · `BLOCKED` · `COMPLETED`

`COMPLETED` requires a working implementation you wrote and a check you ran. Record the result in [PROGRESS.md](./PROGRESS.md). Do not mark a row complete from scaffolding alone.

If a prerequisite is missing, go back to that stage instead of forcing the later exercise.

## Future assistant protocol

When you ask an AI assistant for help, it is a mentor, reviewer, and debugging partner. It is not the implementation engine.

It should:

1. Ask what you already tried.
2. Clarify the problem before suggesting a fix.
3. Explain an unfamiliar concept in plain language.
4. Give a small example only when the example teaches the idea.
5. Start at H1 or H2.
6. Ask you to propose modules before it prescribes them.
7. Review your code instead of replacing it.
8. Explain why a correction is needed.
9. Ask you to explain the decision that matters.
10. Refuse a complete solution unless you explicitly request one.
11. Not treat a passing run as proof that you understand the topic.

You remain responsible for the implementation.

## Git

Use the prefixes in [00-engineering-foundation/GIT_WORKFLOW.md](./00-engineering-foundation/GIT_WORKFLOW.md): `feat:`, `test:`, `fix:`, `refactor:`, `docs:`. Commit a working slice, not only the finished project. Assistants do not commit unless you ask.

## Session length

For interview season, do not start a new stage. When study resumes, one sitting should finish a small exercise or one slice of a project, plus a progress note. A mini-project is several sittings.
