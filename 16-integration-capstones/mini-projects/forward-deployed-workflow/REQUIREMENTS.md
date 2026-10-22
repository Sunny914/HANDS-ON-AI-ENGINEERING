# Requirements

## Problem

A small support team wants new tickets classified into a known set of queues and, sometimes, a reply draft. Sending the reply is a separate approved action. The CRM and the mailbox are simulators you own.

## Users and use cases

- An API creates a ticket and a deterministic rule assigns a queue.
- A draft step may call a fake model. It cannot send.
- A human approves a send. The mail ledger grows by one.
- An engineer sees a failed CRM write on the same request id as the HTTP error.

## Scope

Ticket create, queue assignment, draft, approve send. Simulators in process. Eval cases for wrong queue and for a send without approval.

## Non-goals

A real CRM product, a real inbox, a multi-agent swarm, and a default live model.

## Functional

- Ticket schema: id, customer id, body, queue, status.
- Queue assignment is a pure function of fixture keywords or a table you write. Tests do not need a model for this.
- Optional draft tool: fake model returns text. It has no mail tool.
- Send requires approval of the exact body hash. Stage 11 rules.
- CRM simulator can be flagged down. The HTTP call then fails cleanly and does not claim the ticket was saved.
- Timeouts around the simulator.
- Eval: queue expected versus actual, and send-without-approval must not deliver. Dataset version stored.
- Trace with request id across HTTP, CRM write, and mail.

## Nonfunctional

- Offline tests.
- Invalid ticket bodies are 4xx-style errors, not agent retries.

## Constraints

Queues are a fixed set: `billing`, `access`, `other`. Unknown keywords go to `other`. Do not invent a fourth queue in the model.

## Security and privacy

The draft model cannot choose the queue or the approver. Customer ids are isolated: a caller for customer A does not list customer B's tickets. Synthetic bodies only.

## Evaluation

At least four tickets in a file: two queue cases, one draft that must not send, one approved send.

## Observability

Correlation id. CRM failure status distinct from mail status.

## Reliability

Retry a CRM timeout at most twice. Do not retry a validation error. If mail send is unsure, do not send again without the idempotency key.

## Deployment

Local API. Container and runbook only if you claim the production-oriented bar.

## State

Tickets and the mail ledger persist across restart. Pending approvals persist.
