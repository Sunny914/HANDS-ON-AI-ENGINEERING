# Git Workflow — Stage 00

Use Git as a **learning journal** and safety net—not only at the end of a mini-project.

## Repository habits

- Commit on the machine where you work; push if you use a remote (optional).
- One logical change per commit when possible.
- Never commit secrets (API keys, `.env` with real credentials).

## Message prefixes

| Prefix | When |
|--------|------|
| `feat:` | New behavior |
| `test:` | Tests only |
| `fix:` | Bug fix |
| `refactor:` | Behavior unchanged |
| `docs:` | Markdown, comments |
| `chore:` | tooling, deps |

Examples:

```text
feat: module-00 ex-12 json config loader
test: add parametrize cases for email validator
fix: dbg-03 close file handle on error path
docs: architecture answers for mp1
```

## Suggested branching (optional)

| Branch | Use |
|--------|-----|
| `main` | Stable completed work |
| `stage-00/module-00` | Module in progress |

Merge or rebase when module checkpoint passes.

## Milestone commits

| Milestone | Suggested commit |
|-----------|------------------|
| Exercise done | `feat: complete ex-NN short-name` |
| Architecture written | `docs: arch design arch-01` |
| Debug exercise | `fix: dbg-02 root cause explanation in commit body` |
| Mini-project slice | `feat: mp1 persistence slice` |

## Before checkpoint

```bash
git status
git log --oneline -10
```

You should see incremental history, not one giant commit.

## What not to do

- `git commit` entire mini-project in one shot without tests passing
- Commit broken debugging starters on `main` if they fail CI you add later
- Use AI to generate commits without understanding diff

## Connecting to Stage 01+

Same discipline scales to API features: one endpoint or one reliability pattern per commit where feasible.
