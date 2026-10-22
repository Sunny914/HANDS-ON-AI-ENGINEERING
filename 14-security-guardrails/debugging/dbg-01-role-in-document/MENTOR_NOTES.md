# Mentor notes — dbg-01

`allowed` searches the document for `role=admin` and returns true for every tool when that substring is present. The `principal` argument is ignored in that branch.

Authorize from `principal` and a fixed allow-list. Do not parse roles out of document text.
