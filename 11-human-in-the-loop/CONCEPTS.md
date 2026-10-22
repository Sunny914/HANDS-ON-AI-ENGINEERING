# Stage 11 Concepts

## Why a human is in the loop

A model can propose a send, a record change, a publish, or a deploy. Those actions can be expensive, public, or hard to undo. A pause lets someone check the exact arguments. The pause is worthless if the thing that later runs is a different action, or if the model can mark itself approved.

## The sequence

1. The model, or a script standing in for one, proposes an action.
2. The application validates the shape.
3. The application decides whether policy requires approval. The proposal does not decide this.
4. If approval is required, the application stores a pending snapshot and stops before side effects.
5. An authorized human approves, rejects, edits, or cancels. Edit means a new snapshot, not a silent change.
6. The application checks that the world still matches assumptions in the snapshot.
7. An executor performs that snapshot once.
8. The application writes the outcome.

Authentication answers who is calling. Authorization answers whether that principal may approve or execute. Validation answers whether the payload is well formed. Approval answers whether this pending snapshot may proceed. You need all four when the action is consequential.

## Risk policy

| Example | Typical policy in this stage |
|---------|------------------------------|
| Read a local record | No approval. Still authorized and validated |
| Send a message | Approval required |
| Update a business record | Approval required |
| Publish content | Approval required |
| Deploy or another irreversible step | Approval required, and the requester cannot be the approver |

Thresholds belong in application config, not in the model response. A field named `skip_approval` is untrusted input.

## The pending snapshot

Store the action name, canonical arguments, scope, requester, a hash of the canonical action, created time, expiry, and status. Status moves from `pending` to `approved`, `rejected`, `cancelled`, or `expired`, and then execution moves an approved item to `executed` or `failed`.

The hash is what execution compares. If arguments change after approval, the hash changes, and the old approval does not cover the new arguments.

## Resume

The pending record is the checkpoint. A new process loads it and still must not execute until a decision exists. If you use a LangGraph interrupt instead, Stage 08's rule applies: the node restarts from the top on resume, so side effects before the interrupt run twice. Prefer writing the pending record in ordinary code and keeping the graph, if you use one, free of hidden side effects. The exercises do not require LangGraph.

## After approval

- Expiry: an approved item past its deadline does not run.
- Duplicate decision posts: the second approve returns the existing decision and does not execute twice.
- Cancellation wins over a late approve.
- Idempotency: the executor key is the approval id. A retry after a successful fake send returns the first result.
- Revalidation: if the record version in the snapshot is stale, refuse and leave an audit row. Do not run the action against the new version under the old approval.
- Failure after approval: the item becomes `failed` with a reason. A retry is a deliberate new attempt with the same idempotency key, not a second send that forgot the first one succeeded.
- Rollback: for the fake ledger, a compensating action is another pending action, not a hidden undo inside the executor. Say when you cannot compensate.

## Audit

Append-only rows: proposed, approval_required, approved, rejected, cancelled, expired, executed, failed, refused. Each row has a time, actor, and the action hash. An execution without an audit row is a defect.

## What the model must not decide

The model must not decide that it is authenticated, that the caller is an admin, that approval can be skipped, or that a previous approval covers a new payload. Those are application decisions.
