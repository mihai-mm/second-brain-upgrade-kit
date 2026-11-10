---
name: plan
description: >
  Writes and keeps up to date the plan of one multi-step job in a file of the project, created
  before the first step, updated at every closed step, linked from the project index and the
  work log, and closed with an outcome. Use it on your own at the start of a job with four or
  more distinct steps, a job that will outlast the session, steps owned by other people, or when
  requests arrive mid-work. Also when the person types /plan or "make a plan", "keep the list
  of steps". It is not the task manager. Don't use it for a single fix, an answer to a question,
  or a text built one choice at a time.
---

# Work plan

Purpose: after a pause or a context reset, anyone can see which steps are done, which are left and whose turn it is.

A plan is the list of steps of ONE job in progress. A task manager holds things not to forget, which live beyond the work. Do not turn plan steps into tasks.

## Where I write

<!-- To be filled in during installation with the real paths. -->

| What | Where |
|---|---|
| The plan | `[project folder]/[plans folder]/plan-[name-of-the-work].md` |
| The line that lists it | `[project index]`, in the section for plans |
| The line in the log | `[project folder]/[log folder]/[YYYY-Wnn].md`, current state and the day's entry |

## Step 1 - Open the plan before the first step

1. Find the project the work belongs to. If it isn't clear, ask once.
2. Look for a plan already open for the same job. If there is one, resume it instead of creating another.
3. Otherwise create the plan from `[path of the plan template]`, with a short name in lowercase and no date: it is a living document.
4. Add one line to the project index: the plan, what it covers, the opening date.
5. Say in one line: "Plan opened in [path], N steps."

If the work started without a plan, create it now with the done steps ticked, and say you were late.

Writing into the person's system is shown first and waits for a yes the first time. After that, plan files in this folder need no new confirmation.

## Step 2 - Write it

- The request in the person's words, with the date.
- Setup: decisions that constrain the work.
- Numbered steps, each with the result that says it is done. Steps owned by others carry their name in parentheses.
- A "Postponed" section, empty at the start.

Plain language: the person must understand a step without opening the code.

## Step 3 - Update at every closed step

In the same turn:

- Tick the step and put the evidence in parentheses (a test that passed, a file path, a date). No evidence, no tick: the step stays open with a note.
- Update the "Last updated" date.
- A request that arrives mid-work enters the plan before it is executed, with a suffix (3a) and its date. Never renumber.
- A blocked step stays open, with the reason and who unblocks it.
- In chat, one line: "Plan updated: step N closed." Do not paste the checklist.

Before a context reset or a long pause, the plan must be current.

## Step 4 - Link it from the log

When the work log is written, the entry links the plan and does not copy the checklist. The current state gets one line: work in progress, the plan, the open steps.

## Step 5 - Close it

When all steps are closed, or the person decides to stop:

1. Set the status to closed and add "Outcome (date)": what was delivered, in two to four lines, and where open steps went (Postponed, the log, or a task if it must not be forgotten and the person agrees).
2. In the project index mark the plan as closed, with the date.
3. Remove the "work in progress" line from the current state. The closing goes in the day's log entry, with the link.
4. The file stays where it is. Do not move or delete it.

If a later phase is already decided, the plan stays open and the current state says when it restarts.

## Final check

- The plan existed before the first step.
- Every tick has evidence, and the update date matches the last closed step.
- The index links it and the log points to it without copying it.
- No plan step became a task without the person's agreement.
