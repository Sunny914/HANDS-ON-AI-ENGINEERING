# Mentor notes — dbg-02

The function writes the key into `seen` only after appending, and the membership test checks a different dict that is never filled. The second call always appends.
