# Module 14 - Day opening and weekly close

Installs capability 17. It needs module 01 (work log and current state) and module 07 (project index), and a home page that lists the projects.

## What it's for

The day starts with a short brief built from the states the projects already carry, not from the person's memory. Once a week the states are carried into the new week's file, so they do not go stale.

## Why it works

- **The brief reads, it does not rebuild.** Each project already has a current state at the top of its latest log file. Re-deriving it every morning from raw sources produces a new guess each time. Reading it produces the same answer the project gave yesterday.
- **Source and date on every line.** A line without them cannot be checked. A line with them shows at once when a state is old.
- **Three questions.** What is open, what is waiting on whom, what has a date. These are the lines the person acts on.
- **The weekly close is the check on the states.** Carrying a state forward forces a reread once a week and removes what is closed.
- **Nothing is deleted on a guess.** Threads nobody verified are marked, not dropped.

## Essential

1. A day opening command. It reads the home page, then the current state of each active project's latest week file (chosen by file name, not by modification date).
2. Every line of the brief carries a source and a date.
3. The brief says what is open, what is waiting on whom, and what has a date.
4. Calendar and tasks are included only if the agent can reach them in this environment. Otherwise the brief says "calendar not reachable" or "tasks not reachable". It never fills the gap from memory.
5. If a state is older than the work visible in the project, or the entries below the state contradict it, the brief flags the discrepancy instead of choosing.
6. A weekly close command. For each active project: open the new week's file, copy the current state, keep only the threads still open, drop the closed ones (their detail stays in the dated entries of the old week), and update the pointer on the home page.
7. When in doubt a thread stays. A thread the agent could not verify is marked "not rechecked", not removed.
8. No empty logs created for the sake of conformity. If a project had no activity and has no open thread to carry, say so and create nothing.
9. If a state has grown past about 5 KB, flag it and propose moving detail into the dated entries. Do not rewrite it silently.
10. The old week's file is never edited by the close, except to fix a wrong fact with a dated note.

## Adaptable

- Command names, timing, and the format of the brief (a few lines per project, or a table).
- The sources: a calendar, a task app, an inbox. Use only the ones the person has and the agent can reach.
- The period: if the person logs by month, the close runs monthly.
- If the person already has a daily brief or weekly review, keep it and add what is missing: usually the reading of project states, source and date on each line, or the carry-over rule.
- A weekly review the person writes by hand can stay theirs. The close then covers only the states and the home page pointer.

## How to install it

Do it on the trial project first, then extend to the other active ones.

1. Check that module 01 is in place: each active project has a log folder and a current state. If not, stop and say which ones are missing.
2. Ask the person what their day looks like and which sources they use. Find out what the agent can reach.
3. Propose the two commands, filled in from `templates/skill-morning/SKILL.md` and `templates/skill-weekly-close/SKILL.md`. Show the full text and the path where each will live. Wait for a yes.
4. Run the day opening once with the person and ask what was missing or useless.
5. Run the weekly close on the trial project in dry mode first: show what would be written (the new file's state, the threads kept, the ones marked "not rechecked", the home page line) and wait for a yes before writing.
6. Note in `progress.md` the files created and the lines changed.

## Check

Two tests, in a fresh session.

1. Run the day opening. Every line has a source and a date. If calendar or tasks are not reachable, the brief says so.
2. Run the weekly close on the trial project. The new week's file has the carried state, with only open threads, unverified ones marked "not rechecked". The old week's file is unchanged. The home page pointer shows the new week. No empty file was created for a project with nothing to carry.

If the brief lists events without saying where each project stands, the command is reading raw sources instead of states: rewrite its reading order.

## To roll back

Delete the two command files and remove any line added to the instructions. New week files created by a close can stay: they are normal log files.
