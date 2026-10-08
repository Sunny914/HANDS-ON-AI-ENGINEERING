# Architecture Checkpoint — Before Mini-Project 2

**Project:** Log Analysis & Reporting CLI  
**Rule:** Complete this **before** implementation. Do not read Part B of `mini-projects/02-log-analysis-cli/ARCHITECTURE.md` until your design exists.

Save answers to: `checkpoints/your-answers/mp2-architecture.md`

## Context (requirements summary)

- Parse application log files (format you define or adopt from REQUIREMENTS.md)
- Compute aggregates: requests, success/error, status distribution, endpoints, latency stats, slow requests, error rate, time buckets
- Use generators where appropriate; typing and tests required

## Questions (no answers provided here)

1. What is the entry point?
2. What are the main components?
3. What responsibility does each component have?
4. Which component reads data?
5. Which component validates data?
6. Where is business logic?
7. Where is persistence (if any)?
8. Where does error handling happen?
9. Where should logging happen?
10. How will the components communicate?
11. What should be tested independently?
12. What dependencies flow in which direction?

## Additional design prompts

- Line-by-line streaming vs load-all: what is your choice and why?
- How do malformed lines affect the report?
- What is your log format contract (regex, split, structured JSON lines)?
- How will you test parsing without huge files?

## Sign-off

| Item | Done |
|------|------|
| 12 questions answered | ☐ |
| Data flow diagram | ☐ |
| Planned module list | ☐ |
| Sample log lines documented for your parser | ☐ |

Begin [mini-project 2](../mini-projects/02-log-analysis-cli/README.md) when signed off.
