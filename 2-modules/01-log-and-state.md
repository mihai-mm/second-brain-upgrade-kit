# Module 01 - Work log and current state

Installs capabilities 1 and 2. It goes together with module 02, which is what keeps the log alive.

## What it's for

After a break of days or weeks, the agent reads a few lines and knows where the project stands, what is being waited for and from whom. Below those lines is the history, for when you need to understand how you got there.

## Why it works

- **One file per week.** A single log grows until reading it costs too much. With one file per week the agent opens only the latest, and the rest stays there for searches.
- **The state at the top.** The agent reads a file from the beginning. Putting the state in the first lines means it finds it even if it stops right away.
- **The state is rewritten, the history is not.** They are two different things. The state says how things are now and must stay short and true. The history says what happened and isn't corrected: if an entry was wrong, you add a dated note.
- **The weekly carry-over is a check.** Copying the state into the new file forces a reread once a week and the removal of what is closed.

## Essential

1. The log lives inside the project.
2. One file per period, with a name that sorts itself (for example `2026-W42.md`: year and week number).
3. The first section of the file is the current state, with the date of the last update.
4. Below it, the days: most recent on top. Within a day, entries in time order.
5. The agent writes the entries, with full dates (year, month, day) and never "today" or "yesterday".
6. The state is rewritten rather than lengthened. If it goes past one page, the detail moves into the dated entries.
7. Only the threads still open go into the new week's file. When in doubt a thread stays. If it hasn't been rechecked, write "not rechecked" instead of removing it.
8. No empty files: the new week is born with its first entry.

## Adaptable

- The names of the folder and the files. Use the ones the person would use.
- The language.
- The period: a week suits someone who works on a project several times a week. For slow projects one file per month may be enough.
- The entry format. The template proposes a terse one.
- If the person already has a project diary, don't create a second one: add the state section at the top of theirs, plus the carry-over rule.
- If the person uses a retrieval knowledge base: the log stays a file inside the project, and on top of that it becomes a source to be indexed. The current state is the record to weight the most.

## How to install it

Do it on one project only, the one chosen for the trial.

1. Look at how the person names things and propose a folder name and a file name format. Wait for a yes.
2. Announce the files you will create: the log folder and the file for the current week.
3. Create the current week's file starting from `templates/week.md`. Work out the week with the system calendar, not from memory.
4. **Write the first current state together with the person.** Propose a draft based on what you read in the project, saying which files you took it from, and have them correct it. This is the moment that matters most: a wrong state at the start takes trust away from everything else.
5. Add to the project's instructions (or the main ones, if the person prefers) a line saying where the log is and that the current state of the latest week is the source for knowing where things stand. Show the exact line before writing it.
6. Note the files created in `progress.md`.

## Check

In a fresh session, with no other context, ask: "Where are we on [project]?". The test passes if the agent:

- opens the most recent week's file;
- answers with the content of the state;
- cites the file and the date of the last update.

If it goes off reading other files before answering, the line in the instructions isn't clear enough: rewrite it.

## To roll back

Delete the log folder that was created and remove the line added to the instructions. Both are listed in `progress.md`.
