# dbg-03 Hints

**H1:** An exception mid-loop may skip cleanup.

**H2:** On error path the file handle may stay open or hold partial writes.

**H3:** Use `with open(...) as f:` so close runs even when raising.
