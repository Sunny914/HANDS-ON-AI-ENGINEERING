# Requirements

## Stories

- As a user, I can read my own note and not someone else's.
- As an operator, a hostile note cannot cause deploy.
- As a reviewer, I can see a denied call without a secret in the log.

## Functional

- Threat model and residual-risk note before the executor is wired.
- Principals with roles. Research may read. Send and deploy are not on that allow-list.
- Deploy requires a different approver, and proposal flags do not count.
- Schema validation before execution. Fail closed on missing policy, unknown tool, and invalid arguments.
- Tenant filter on reads and on any memory lookup.
- Retrieved text is data. Tests include a note that tells the assistant to deploy and to become admin.
- Secret-safe logs using synthetic `sk-test-` values.
- Scripted proposals. No live model in the default suite.
- Regression tests for the bypasses above.

## Nonfunctional

- No real credentials, shells, or outbound network calls.
- Denied calls do not change the ledger.
- Error text returned to the caller does not include other users' note bodies.

## Non-goals

A claim that injection is impossible, a production identity provider, and content moderation as the only control.
