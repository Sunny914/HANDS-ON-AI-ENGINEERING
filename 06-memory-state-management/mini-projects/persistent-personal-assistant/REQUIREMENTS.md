# Requirements

## Stories

- As a user, I can say "remember that I prefer aisle seats" and see that fact used in a later process.
- As a user, I can ask what you remember and see ids and timestamps.
- As a user, I can delete one memory and have it stay gone after restart.
- As a user, I am not surprised by a stored instruction overriding the assistant's rules.

## Functional

- Memory schema you design: at least id, user id, kind, text, source, created_at, updated_at.
- Write policy from this stage. Model proposals do not store themselves.
- Kinds include preference and episode, with the conflict rules you tested.
- Retrieval without embeddings.
- Context assembly under a configurable budget, with provenance in the data block.
- File or SQLite persistence. Path comes from settings.
- Forget by id, scoped to the user.
- Optional expiry field. Expired rows are not retrieved.
- A reply function may call an injected completer. The completer is a fake in tests. Empty or hostile memories still follow ex-08.

## Nonfunctional

- Default tests start no network and no model API.
- Logs include memory ids and decisions (accept, reject, omit). They do not need the full text at info if the text might be sensitive. You choose and document the log fields.
- Single process. Document the race you are not solving.

## Non-goals

Vector search, user accounts with passwords, and a multi-agent staff.
