# Test Plan

Write these tests yourself.

## Unit

- Retry decision table from ex-07, reused or imported
- Idempotency: same key returns stored result and skips the client fake
- URL validation rejects non-http schemes

## Repository

- Insert and fetch after reopening the file
- Page slice matches the pure pagination math

## API

- 401 without a token
- 201 with a token and a fake upstream
- 422 on a bad URL
- Conflict on key reuse with a different body

## Not required

- Load tests
- Real calls to the public internet
- Browser tests
