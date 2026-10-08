# MP1 — Functional Requirements

## Tasks

A **task** includes at minimum:

- Unique `id` (you choose strategy)
- `title` (non-empty string, max length you define)
- `description` (optional)
- `status` (e.g. `todo`, `in_progress`, `done` — you may extend)
- `priority` (e.g. `low`, `medium`, `high`)
- `created_at` / `updated_at` (ISO timestamps)

## CLI capabilities (minimum commands)

| Command | Behavior |
|---------|----------|
| create | Add task with title, optional description, priority, status default |
| update | Change fields by id |
| delete | Remove by id |
| list | Show tasks; support filters (status, priority) |
| show | Single task by id |

## Persistence

- JSON file as backing store (path configurable)
- Survive process restart

## Cross-cutting

- Input validation with clear user-facing errors
- Logging (operations and errors)
- Structured module boundaries—you design layout

## Non-goals (Stage 0)

- Multi-user concurrency
- Network API
- Encryption at rest
