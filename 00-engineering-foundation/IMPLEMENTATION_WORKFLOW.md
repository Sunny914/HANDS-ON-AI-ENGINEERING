# Implementation Workflow

Use this process for **every** exercise beyond trivial drills and for both mini-projects.

## Principles

- **Do not** write the entire application at once.
- **Do** integrate in thin vertical slices (one behavior end-to-end).
- **Commit** when behavior works and tests pass—not only at the end.

## Steps

### STEP 1 — Read requirements

- Restate the objective in your own words.
- List inputs, outputs, and side effects (files, network, stdout).

### STEP 2 — Identify unknowns

- What APIs are you unsure about?
- What edge cases are ambiguous?
- Write questions; answer via docs/REPL before coding.

### STEP 3 — Design the architecture

- Entry point, modules, data models.
- For architecture exercises: complete checkpoint questions **before** coding.
- Sketch data flow (even 5-box ASCII).

### STEP 4 — Create project structure

- Directories, empty modules, `pyproject.toml` or `requirements.txt` when needed.
- Only add files you can name a responsibility for.

### STEP 5 — Implement the smallest working component

- Example: parse one record before full report.
- Example: `add_task` in memory before JSON persistence.

### STEP 6 — Test it

- Manual check first if helpful; then automated test.
- One test that would fail if the feature regressed.

### STEP 7 — Integrate the next component

- Wire storage, then CLI, then validation—order varies by project.
- Keep the app runnable after each integration.

### STEP 8 — Test again

- Run full suite; add tests for the new seam.

### STEP 9 — Handle errors and edge cases

- Invalid input, missing files, corrupt data.
- Decide: recover vs fail fast vs partial success.

### STEP 10 — Refactor

- Only with green tests.
- Rename for clarity; extract functions when a block has a name.

### STEP 11 — Document

- Update README with how to run.
- Module docstrings or top-of-file responsibility comments.

### STEP 12 — Commit with Git

- Small, meaningful commit messages (`feat:`, `test:`, `fix:`, `refactor:`, `docs:`).
- See [GIT_WORKFLOW.md](./GIT_WORKFLOW.md).

## Vertical slice example (mini-project 1)

```text
Slice 1: in-memory create + list (no CLI)
Slice 2: add CLI wrapper for create/list
Slice 3: JSON persistence for create/list
Slice 4: update/delete + validation
Slice 5: filter/priority + logging + error UX
```

## When stuck

1. Reproduce minimally (smallest input that fails).
2. Read traceback bottom-up.
3. Request **H1** then **H2** then **H3** from [HINTS.md](./HINTS.md)—not full solutions.

## Definition of done (exercise)

- All acceptance criteria met
- Edge cases handled or explicitly documented as out of scope
- Tests where required
- You can explain where you would add the next feature
