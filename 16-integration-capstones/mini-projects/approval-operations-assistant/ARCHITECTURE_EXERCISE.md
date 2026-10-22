# Architecture Exercise

Write `ADR.md` and `YOUR_DESIGN.md` before execute is reachable from HTTP.

Boundaries: HTTP, proposal parser, policy, pending store, executor, audit, eval command. The proposer module returns data and does not import the executor.

Decisions: file versus SQLite, where the hash is checked, and whether you will reach the container milestone.
