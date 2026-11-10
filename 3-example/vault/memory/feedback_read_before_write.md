---
name: read-before-write
description: Read a file before writing to it or editing it, never overwrite from memory
type: feedback
---

Before editing or overwriting a file that already exists, read it. Never replace a file with a new version based on what you think it contains.

**Why:** 2026-08-04. While tidying the notes of the own-website project, the agent overwrote the working notes file with a short summary, assuming it was almost empty. It held the list of pages still to rewrite, with Livia's comments on each. She recovered it from the previous day's copy and lost an afternoon. The cost of reading first is one read.

**How to apply:**
- Read the file, or the part you will change, in the same session and before the edit.
- Never read and write the same file in parallel: the write must come after the read has returned.
- If the file does not exist, say so and do not guess its content.
