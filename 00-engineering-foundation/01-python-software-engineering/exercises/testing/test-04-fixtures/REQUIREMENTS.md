# test-04 — Test Requirements

Implement `load_users(path) -> list[dict]` expecting JSON list with `id` and `name`.

## Fixture requirements

- Fixture provides temporary JSON file path with two users
- Test asserts count and one name
- Second test uses same fixture to assert ids unique (add duplicate in fixture variant or second fixture)

Use pytest `tmp_path` or custom fixture—your choice.
