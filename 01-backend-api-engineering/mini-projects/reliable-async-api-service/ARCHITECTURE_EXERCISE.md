# Architecture Exercise

Answer these in `YOUR_DESIGN.md` inside this folder before the first code commit. There is no reference tree to copy.

1. What is the problem in one paragraph, and what are you refusing to build?
2. Which modules exist, and what is the single responsibility of each?
3. What does the route pass to the service?
4. What does the service pass to the repository and to the client?
5. Where is the idempotency lookup?
6. Where is `should_retry` called?
7. Which exceptions become which status codes?
8. Where are settings read?
9. Which tests use fakes, and which open SQLite?
10. What becomes hard if a second API process is added later?

If you change the design halfway through, update the note and say why.
