---
name: log-via-skill
description: "Log this" and "close" mean running the log skill, never writing the log by hand
type: feedback
---

When Livia says "log this", "close" or "that's it for today", run the log skill. Do not write the entry by hand, even when it looks quicker.

**Why:** 2026-10-05. Livia said "log this" at the end of a session. The agent appended a paragraph to the week's file by hand. The entry was there, but the current state at the top was not updated and the decision taken that day never reached `decisions.md`. The next morning the session started from a state that was one day old. The skill exists precisely to do those three things together.

**How to apply:**
- The trigger phrases are in the skill's description. If one of them appears, the skill runs.
- If the skill cannot run, say so and say what was not saved. Do not replace it with a manual entry.
- This line is in the always-loaded index on purpose: a rule tied to a phrase has to be in front of the agent before the phrase arrives.
