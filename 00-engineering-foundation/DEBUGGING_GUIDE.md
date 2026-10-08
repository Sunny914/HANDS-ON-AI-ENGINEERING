# Debugging Guide — Stage 00

Debugging exercises ship **deliberately broken** code. Your job: diagnose and fix without being told the bug upfront.

## Mindset

> Something is wrong. Find what the program *assumes* vs what is *true*.

## Process

1. **Reproduce** — exact command, input, expected vs actual.
2. **Localize** — narrow to one function/file (binary search with prints or debugger).
3. **Hypothesize** — one theory at a time.
4. **Verify** — smallest change or REPL check.
5. **Fix** — minimal fix; avoid drive-by refactors.
6. **Regress** — add a test if the module has tests.

## Tools

| Tool | Use |
|------|-----|
| Traceback | Read last frame first; note exception type |
| `print` / logging | Temporary; remove or downgrade after fix |
| `python -m pdb` / IDE debugger | Step, inspect locals |
| `git diff` | If you already had working code |
| pytest | Run single test `-k name` |

## Bug categories in this stage

| Category | Symptoms | What to check |
|----------|----------|---------------|
| Wrong data structure | KeyError, wrong counts | dict vs list, nesting |
| Mutation | Changing shared default | `[]` defaults, in-place vs copy |
| None | TypeError, silent skips | guards, optional returns |
| Scope | UnboundLocalError, wrong value | shadowing, loop variables |
| Imports | ModuleNotFoundError, circular import | package layout, `__init__.py` |
| Types | comparing str to int | parsing, JSON types |
| Files | FileNotFoundError, empty read | cwd, paths, encoding |
| Resources | locked file, leaks | missing `with` |
| Exceptions | swallowed errors | bare `except`, wrong order |
| Tests | false confidence | mocking too much, wrong fixture |

## Debugging exercise rules

- Do **not** read `HINTS.md` for that exercise until you have a hypothesis written down.
- Hints are ordered **H1 → H2 → H3** in the exercise `HINTS.md` (module 01) or central [HINTS.md](./HINTS.md).
- After fixing, write 2–3 sentences: root cause and how you proved it.

## Ethics of AI assistance

Asking "what's wrong with line 42?" is H4 territory. Prefer:

- H1: category of bug
- H2: which subsystem to inspect
- H3: pseudocode for a fix strategy

## Post-fix reflection

Answer:

1. Which assumption was false?
2. What test would have caught this earlier?
3. Where should validation have lived?
