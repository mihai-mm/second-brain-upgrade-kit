---
name: fix-root-cause
description: When something fails, name the cause and the patch as two separate things
type: feedback
---

When something breaks, show Livia two things apart: the quick patch that removes the symptom, and the cause upstream. Recommend one. Do not apply the patch and call it fixed.

**Why:** 2026-10-02. In the first test emails some client names arrived with broken accented letters. The agent added a step that replaced the broken characters just before sending, and reported the problem as solved. The cause was upstream: the export had been opened and saved again in a spreadsheet program, which changed how the text was stored. A week later a different letter broke, one the patch did not know about.

**How to apply:**
- Say where the wrong data first appears, not only where it shows.
- Present: patch (fast, hides the cause) and fix (removes the cause), with what each one costs.
- If the cause is in something a client does, it also goes in the tool file, so the next project starts knowing it.
