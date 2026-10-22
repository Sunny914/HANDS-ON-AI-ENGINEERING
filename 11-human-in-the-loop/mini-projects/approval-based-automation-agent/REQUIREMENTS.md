# Requirements

## Stories

- As a requester, I can ask the agent to read a record without a pause, and to send, update, publish, or deploy only after a person approves the preview.
- As an approver, I can approve, reject, request a changed payload, or cancel, and I can see the exact arguments.
- As an operator, I can restart the process and still see pending work unexecuted, with an audit trail.

## Functional

- Proposer: a scripted model returns action proposals. It may return `skip_approval` or `approved`. Those fields have no effect. A live model is out of scope for the default tests.
- Actions: `read_record`, `send_message`, `update_record`, `publish`, `deploy`. All tools are fakes over a local ledger and a local record store.
- Policy from the exercises: reads do not pause. Sends, updates, and publishes pause. Deploys pause and require a different principal with the approver role.
- Pending snapshot with canonical hash, requester, scope, expiry, and record version where relevant.
- Persist pending actions so a second process object can load them.
- Preview is the stored snapshot rendered as structured data. It is not a second model call.
- Modify creates a new pending id and hash. The previous id cannot be executed.
- Revalidate version and hash before execute.
- Idempotent execute keyed by pending id.
- Expiry and cancellation are terminal for that id.
- Duplicate approval does not double-execute.
- Audit rows for proposal, refusal, approval, rejection, cancellation, expiry, execution, and failure.
- Failure of a fake tool after approval stores `failed` and does not claim `executed`.
- A compensating action, if you model one for a fake send, is a new pending action. Do not hide an undo inside the executor.

## Nonfunctional

- Injected clock.
- No network, no shell, no real provider.
- Logs include ids, action names, and decisions. They do not need full message bodies at info level.
- Tests are deterministic.

## Non-goals

A real identity provider, a real notification channel, LangGraph as a requirement, multi-agent coordination, and any live external side effect.
