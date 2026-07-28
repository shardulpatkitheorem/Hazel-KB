# Durable Lessons

This file contains reusable rules that should change future agent behavior. Meeting-specific facts, decisions, and temporary project state do not belong here.

## Lesson admission test

A lesson may be added only when all answers are yes:

1. Is it reusable across future iterations?
2. Is it supported by an iteration, verification failure, or approved review comment?
3. Does it define a concrete trigger and required behavior?
4. Is it not already covered by an existing lesson or contract?
5. Has a human reviewer approved its promotion?

## Entry format

```markdown
### LESSON-001 — Short behavioral rule

- Adopted: YYYY-MM-DD
- Trigger: Observable situation that activates this lesson
- Required behavior: Exact action the agent must take
- Evidence: Iteration, verification report, or approved review URL
- Approved by: Reviewer
- Replaces: Lesson ID or `not-applicable`
```

Do not use this file as a scratchpad or meeting summary.
