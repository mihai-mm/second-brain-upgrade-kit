# Report template

Write the report in `report/report.md`.

**Language.** The one the person wrote to you in, even though this template is in English. Translate the section titles too.

**Length.** No more than 1,200 words, table included. With eighteen rows the table takes about a third of that. The reader is short on time: the first section must be enough to decide whether to go on. To stay within the limit:

- in the table every cell fits on one line, around fifteen words at most;
- every proposal fits in six lines, one per entry;
- detail that doesn't fit goes in `system-map.md`, with a pointer.

Use these sections, in this order.

## 1. In short

Four or five lines: how the system is built, which gap weighs the most, what you propose first. If nothing relevant is missing, say it here.

## 2. Your system, as I understood it

The confirmed map, in about ten lines. Point to `system-map.md` for the detail.

## 3. What it does better than the method in this folder

The things the person's system does that Mihai's method doesn't do, or does worse. For example automatic ingestion from email and chat, search over a large volume, the work of several people. One line each, with the note "leave as is" where it applies.

If you find none, write that you found none. Don't invent them to be polite.

## 4. The eighteen capabilities

A table with one row per capability.

| No. | Capability | Status | How you do it today | Evidence |
|---|---|---|---|---|

- Status: present, partial, missing, can't verify.
- How you do it today: the form the thing takes in the person's system, in their words.
- Evidence: the file or setting you read. For "missing" write where you looked and what the person answered.

## 5. What I counted

The results of `3-measuring-impact.md`: for each measure the number, the base, one or two short examples. If you used the five questions, give the answers as an account and say so.

## 6. What I propose

At most three additions, in order. For each one:

- **What changes for you.** One or two sentences about everyday work, no jargon. If the proposal adds a manual step to a system designed to have none, say so here.
- **Which measure it rests on.** The number from section 5 that justifies it. If there is no measure, say so.
- **What will be created.** The files, with the path they would have in the person's system and in their conventions.
- **What will not be touched.**
- **How to check it works.** The module's test.
- **Module.** The file in `2-modules/` that installs it.

Respect the dependencies written on the cards: don't propose the current state without a log, or the session close without a place to write to.

If the log, the current state and the session close are all three missing, propose them together as the first block: alone they are worth little, together they are what lets a project be resumed.

## 7. What is missing but I'm not proposing now

The other missing or partial capabilities, one line each with the reason: it depends on another one, impact not shown, better later.

## 8. Limits of this analysis

- What you couldn't read.
- How many sessions the measures are based on.
- If the system belongs to a team: the log and the current state have been tested with a single author.
- Any point where you had to rely on the person's account.

## After writing the report

In chat present only sections 1 and 6, briefly, and say where the full file is. Then ask one thing only: which proposal they want to start from, or whether they'd rather stop here.

Update `progress.md`.
