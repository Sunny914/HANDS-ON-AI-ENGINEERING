# Architecture Checkpoint — Before Mini-Project 1

**Project:** CLI Task & Job Management System  
**Rule:** Complete this document **before** writing implementation code. Do not open `mini-projects/01-cli-task-job-manager/ARCHITECTURE.md` Part B until your design is done.

Save your answers to: `checkpoints/your-answers/mp1-architecture.md` (create the folder).

## Context (requirements summary)

- CLI for creating, updating, deleting, listing, and filtering tasks
- Fields include status, priority, and core task attributes you define
- Persist to JSON with validation and error handling
- Logging and tests required
- Clean module separation—you choose structure

## Questions (no answers provided here)

1. What is the entry point?
2. What are the main components?
3. What responsibility does each component have?
4. Which component reads data?
5. Which component validates data?
6. Where is business logic?
7. Where is persistence?
8. Where does error handling happen?
9. Where should logging happen?
10. How will the components communicate?
11. What should be tested independently?
12. What dependencies flow in which direction?

## Additional design prompts

- What is your task identity model (IDs, UUIDs, slugs)?
- How do you handle concurrent edits to the same JSON file (scope for Stage 0)?
- What does the CLI do on validation failure vs storage failure?
- What is your smallest vertical slice for day one?

## Sign-off

| Item | Done |
|------|------|
| Written answers to 12 questions | ☐ |
| ASCII or diagram of data flow | ☐ |
| List of modules/files you plan to create | ☐ |
| Open questions you will resolve during implementation | ☐ |

When signed off, begin [mini-project 1](../mini-projects/01-cli-task-job-manager/README.md).
