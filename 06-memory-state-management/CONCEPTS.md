# Stage 06 Concepts

## Three stores people mix up

| Store | Lifetime | Example |
|-------|----------|---------|
| Working state | One task | Current step, tool result just observed |
| Transcript | This conversation, until you trim it | System, user, assistant, tool messages |
| Durable memory | Across process restarts | "Prefers window seat", written on purpose |

A message list is not a database. A database row is not an instruction.

## State

Prefer an explicit schema: field names, types, and which transitions are legal. Replace a whole record only when you mean to. A patch that omits a field must not erase that field unless the transition says so.

Version the schema with an integer. When you add a field, old files still need a reader. That reader is a migration, even if it only fills a default.

## Transcript budget

Stage 02's context window still applies. Selection strategies, from blunt to careful:

- Keep the last N messages
- Keep the system message, drop the middle, keep a tail
- Replace the dropped middle with a summary you stored

A summary can delete the only fact you needed. Test that.

## What to remember

Write a policy before you write rows. Good reasons to store: the user asked you to remember, a preference is stable, a task id must survive restart. Bad reasons: the model said "remember this", the text contains a secret, the text says "ignore your rules".

Every memory needs provenance: who or what wrote it, and when. Without that, you cannot explain a later answer.

## Conflicts

Newer is not always righter. A preference can be replaced. A one-time event should not be overwritten by a vague later sentence. You choose the rule per memory type and test it.

## Retrieval without vectors

Filter by user id, type, and time. Rank by exact terms plus recency if you need an order. You can add embeddings later. You should not need them to prove the policy.

## Untrusted content

Retrieved text is data in the prompt, fenced or labeled. It does not grant tools, change the system role, or override a retention rule.
