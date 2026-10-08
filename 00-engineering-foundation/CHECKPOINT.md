# Stage 00 — Checkpoints

Stage 0 is **not** complete when exercise folders are ticked off. Complete the checkpoints honestly.

## Module checkpoints (self-assessment)

After **Module 00**, you should answer **yes** without hesitation:

| # | Question |
|---|----------|
| M0-1 | Can I choose list vs dict vs set for a problem and defend it? |
| M0-2 | Can I trace a mutation bug to shared references? |
| M0-3 | Can I split a script into importable modules? |
| M0-4 | Did I fix at least two debugging exercises and document root cause? |

After **Module 01**, you should answer **yes**:

| # | Question |
|---|----------|
| M1-1 | Can I structure a multi-file package with a clear entry point? |
| M1-2 | Can I write pytest tests from a spec without copying tutorial code? |
| M1-3 | Did I complete all three architecture exercises and compare to reference? |
| M1-4 | Can I explain dependency direction between CLI, service, and storage? |

After **Module 02**:

| # | Question |
|---|----------|
| M2-1 | Can I explain blocking vs `await` in my own words? |
| M2-2 | Did I measure or reason about sequential vs concurrent timing in ex-06? |

## Architecture checkpoints (required before mini-projects)

Complete **in writing** (your file under `checkpoints/your-answers/`):

1. [architecture-before-mini-project-1.md](./checkpoints/architecture-before-mini-project-1.md)
2. [architecture-before-mini-project-2.md](./checkpoints/architecture-before-mini-project-2.md)

Answer all 12 questions **before** coding the corresponding mini-project. Do not peek at reference architecture until after your design.

### The 12 questions

1. What is the entry point?
2. What are the main components?
3. What responsibility does each component have?
4. Which component reads data?
5. Which component validates data?
6. Where is business logic?
7. Where is persistence?
8. Where does error handling happen?
9. Where should logging happen?
10. How will the components communicate?
11. What should be tested independently?
12. What dependencies flow in which direction?

## Mini-project completion gates

| Gate | MP1 | MP2 |
|------|-----|-----|
| Architecture doc (your design) | ☐ | ☐ |
| All acceptance criteria | ☐ | ☐ |
| Test plan executed | ☐ | ☐ |
| README run instructions | ☐ | ☐ |
| Compared to reference architecture | ☐ | ☐ |

## Stage 0 final checkpoint

Answer honestly (yes / not yet / with effort):

| # | Question |
|---|----------|
| F1 | Can I start a Python project without a tutorial? |
| F2 | Can I decide when to use a function vs a class? |
| F3 | Can I explain why each module exists in my mini-project? |
| F4 | Can I trace how data moves from CLI → service → storage → back? |
| F5 | Can I diagnose an error from traceback before asking AI? |
| F6 | Can I write tests for my own code? |
| F7 | Can I explain my architecture aloud in under 3 minutes? |
| F8 | Can I refactor without breaking behavior (tests green)? |
| F9 | Can I implement a moderate program from a specification alone? |
| F10 | Can I work without AI-generated implementation code? |

**Pass standard:** At least **8 of 10** are solid **yes**; no **not yet** on F4, F6, F9, F10.

### Final deliverable (you produce)

1. Short `STAGE00_REVIEW.md` in repo root or `00-engineering-foundation/` with:
   - Which mini-project you explain architecturally
   - Diagram or bullet data flow
   - One mistake you made and how tests/debugging caught it
   - What you will carry into Stage 01

2. Git log showing incremental commits across Stage 0.

### If not ready

Repeat:

- One architecture exercise (different from last)
- One debugging exercise
- One vertical slice of a mini-project rewritten from scratch in a branch

Depth beats speed.
