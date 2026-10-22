# Requirements

## Problem

Operators want a draft of a send or a record update, and they want a person to approve the exact payload. A model must not mark itself approved.

## Users and use cases

- A requester proposes a send. Nothing is sent.
- An approver approves the snapshot. One ledger row appears.
- An on-call engineer reloads pending work after a restart and reads the audit for that id.

## Scope

Fake tools: read, send, update. Local store. HTTP API. Scripted proposer.

## Non-goals

A real email gateway, a real identity provider, a multi-agent committee, and a live model in the default suite.

## Functional

- Propose, list pending, approve, reject, cancel. Modify creates a new snapshot id.
- Exact arguments hashed. Execution uses the stored snapshot.
- Requester cannot approve their own send or update.
- Idempotent execute. Expiry with an injected clock.
- Restart loads pending items and does not execute them.
- Audit events and a request id. Secrets redacted.
- Eval cases: bypass attempt must fail, legitimate approval must send once, stale version must not send. Dataset version stored.
- Health and fake config from Stage 15 if you aim beyond basic.

## Nonfunctional

- Offline tests.
- Fail closed when the policy file is missing.

## Constraints

Synthetic recipients only, such as `ops@example.com`.

## Security and privacy

Application authorization, proposal flags ignored, residual risk that a future tool is added to the allow-list without a test.

## Evaluation

Three cases minimum, labeled, versioned. The gate fails if a bypass case ever executes.

## Observability

Request id links proposal, decision, and execute. A denied path is still an event.

## Reliability

Crash between tool success and audit write is a named gap unless you close it with a test. Rollback of a bad deploy of this service is a previous local image, not an undo of a business send. A compensating send is a new pending action.

## Deployment

In-process tests first. Container optional at the production-oriented bar.

## State

Pending snapshots and audit log survive the process. The ledger of sent messages is the side effect.
