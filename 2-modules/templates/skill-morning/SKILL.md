---
name: morning
description: >
  Opens the day: reads the current state of each active project and, if reachable, the calendar
  and the task list, and returns a short brief with what is open, what is waiting on whom and what
  has a date. Use it when the person types /morning, "start the day", "good morning", "what's on
  today". Don't use it mid-day for a single project question (use resume) or to write anything
  into the logs.
---

# Day opening

Purpose: start the day from the states the projects already have, with source and date on every line. Read, don't rebuild.

## Where I read

<!-- To be filled in during installation with the real paths. -->

- Home page (list of projects and their status): `[path to the home page]`
- A project's log: `[project folder]/[log folder]/[YYYY-Wnn].md`
- Calendar: `[how the agent reaches it, or "not reachable"]`
- Tasks: `[how the agent reaches them, or "not reachable"]`

## 1. Find the active projects

Read the home page. Take the projects marked active. If the status is unclear for one, list it as "status unclear" and don't guess.

## 2. Read each state

For each active project:

1. Find the log file of the most recent week by looking at the **name**, not the modification date.
2. Read the current state section and note the date of its last update.
3. Read the most recent entries below it. If they say something the state doesn't, or contradict it, note a discrepancy.
4. If files in the project were modified after the log's last entry, say so: work may have happened without a close.

Don't open other files. Don't rebuild a state from raw material. If a project has no log, say "no log" and move on.

## 3. Calendar and tasks

- If the calendar is reachable, list today's events with their times. Otherwise write "calendar not reachable".
- If tasks are reachable, list those due today or overdue. Otherwise write "tasks not reachable".

Never fill a gap from memory or from an earlier session.

## 4. Answer

Short, in this order:

- **Per project**, two or three lines: where it stands, with `(source: [file], updated [YYYY-MM-DD])`.
- **Open**: what is still to be done.
- **Waiting**: what is waiting, and on whom.
- **Dated**: what has a date, from states, calendar and tasks, each with its source.
- **Discrepancies and stale states**, if any: a state older than two weeks is flagged "possibly stale", not treated as closed.

Then stop. Don't propose a plan for the day unless the person asks. This command writes nothing.

## Final check

- Every line has a source and a date.
- I chose the week by file name.
- I said what I couldn't reach.
- I didn't treat a quiet log as a closed project.
