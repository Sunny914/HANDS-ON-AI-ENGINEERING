# Implementation Plan

Build in slices. Do not generate the whole service in one sitting. This is an order of behavior, not a list of filenames.

1. Settings, logging, health, and an empty app that tests can import.
2. Create and fetch against SQLite, with validation and auth, and no upstream call. Store status `accepted` if you need a placeholder.
3. Inject a fake upstream and store success or failure.
4. Add the timeout and the retry policy around the fake.
5. Add the idempotency key.
6. Add pagination.
7. Run the acceptance list and fill the checkpoint.

Each slice should leave tests green before the next one starts.
