---
name: log
description: >
  Closes a work session: records in the project's log what was done, updates the current state
  if it changed, and sends decisions, corrections and rules to their place. Use it when the person
  types /log, "log this", "let's wrap up", "that's it for today", "see you tomorrow".
  Don't use it for a pause in the middle of the work or for a goodbye with no work behind it.
---

# Session close

Purpose: nothing that came up in this session should be lost, and nothing should end up in two places.

## Where I write

<!-- To be filled in during installation with the real paths. Remove the rows you don't need. -->

| What | Where |
|---|---|
| Progress and current state | `[project folder]/[log folder]/[YYYY-Wnn].md` |
| Decisions, things learned, project numbers | `[project folder]/[decisions file]` |
| Corrections to the way I work | `[where corrections live]` |
| Rules for a tool | `[tool files folder]/[tool].md` |
| Lasting facts about a client or a person | `[profiles folder]/[name].md` |

## Step 0 - Is there anything to save?

Look at the session since the last close. There is material if at least one of these happened: files created or edited, a decision made, a correction received, something learned about a tool or a person, work left halfway.

If there is nothing, answer with one line ("Nothing new to log") and stop.

## Step 1 - List, then pick one home for each thing

Make a mental list of what came up. For each item find the evidence in the conversation and pick a single destination:

| Nature | Destination |
|---|---|
| Something was done or moved forward | Log. Current state only if it moves the project |
| A decision that governs the project | Decisions file, with date and reason |
| The person corrected how I work | Corrections |
| Something verified about a tool that will still hold tomorrow | The tool's file |
| A lasting fact about a client or a person | The person's profile |
| An interpretation of mine, not confirmed | Nothing: I propose it in chat |

A choice made once for a specific case is not a permanent preference. When in doubt it stays in the log.

Before writing to a destination, check the information isn't already there.

## Step 2 - Work out which project this is about

From context: the files touched, the topic. If the session touched two projects, write two entries, one per log. If it isn't clear, ask once.

## Step 3 - Write the log entry

1. Work out the week with the system calendar.
2. If the week's file doesn't exist, create it and carry the previous week's current state to the top, keeping only the threads still open. When in doubt a thread stays. Mark what you couldn't verify as "not rechecked".
3. Read only the beginning of the file. If today's day isn't there, add its heading right below the current state, above the earlier days. If it is, add the entry at the end of that day.
4. Write the entry:

```
### [Concrete title, five to ten words]

[One line of context: what and why.]

What changed:
- [one line per point]
- **Decision**: [if any]

Still open:
- [if any]

Files touched:
- [path]
```

Limits: 4 to 8 lines for small work, up to 20 for medium work, never more than 30. If the work produced a document, point to the document and write only what isn't in it. Full dates, never "today" or "yesterday". No long quotes.

This write needs no confirmation.

## Step 4 - Update the current state, if needed

Update it when: a phase closes, a decision changes direction, a blocker appears, what is being waited for or from whom changes.

Leave it as it is for small fixes, explorations with no outcome, internal work that doesn't move the project.

When you update it, rewrite it in full: where we are, what we are waiting for and from whom, the next step. Closed threads drop out. End with the date. If after writing it goes past one page, flag it in the recap.

## Step 5 - The other destinations

- **Decisions**: add the entry with date and reason. If it replaces an earlier decision, mark the old one as superseded and point to the new one. Don't delete it.
- **Corrections, tool files, profiles**: write the explicit facts. Show the person the line you are adding when it changes a working rule that will apply to all future sessions.
- If a destination can't be reached, don't say there was nothing to write: say you couldn't verify it.

## Step 6 - Recap

One line per destination, with one of three marks:

- `✓` written and reread
- `-` nothing new to write
- `!` not written or not verified, with the reason

Example:

```
✓ Log 2026-W42: "Reminder trial on twenty clients"
✓ Current state updated: waiting for the client list
✓ Decisions: reminders by email (supersedes the one from 09/29)
- Corrections
! Tool file: I couldn't find the folder given
```

Nothing else after the recap, unless a `!` needs a choice from the person.
