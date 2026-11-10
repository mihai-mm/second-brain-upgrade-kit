---
name: health-check
description: >
  Read-only check of how heavy and how consistent the person's system is: size of the files
  loaded at every session, size and line length of the memory index, length of the current state
  in active projects, rules that contradict each other, pointers to files that no longer exist.
  It writes a short report with evidence and changes nothing. Use it when the person types
  /health-check or asks for a "health check" or "maintenance check", after a model change, when
  the memory index nears its size limit, or when more than three months have passed since the
  last check. Don't use it to fix anything: fixes are decided with the person afterwards.
---

# Health check

Purpose: find what has become too heavy, contradictory or broken, with evidence, and change nothing.

This skill only reads. The one file it writes is the report, in the place given below. Any fix is proposed in the report and applied only after the person says yes.

## Where I write

<!-- To be filled in during installation. -->

| What | Where |
|---|---|
| The report | `[reports folder]/health-check-[YYYY-MM-DD].md` |

The thresholds below are attention signals to adapt. They depend on the agent and the model. Check in the documentation of the version in use how much of each file is really loaded.

## Step 1 - List what loads at session start

Read the main instructions and find every file they load: the owner profile, the agent identity, the always-loaded index, rules files. For each one give the size in KB and the lines. Add the total.

Signals:

- the total at session start is growing compared with the previous report (if there is one);
- the owner profile is over about 16 KB, or contains dated status;
- an instruction file is over about 200 lines;
- the memory index is over about 20 KB or 180 lines.

## Step 2 - Measure the index

- Count the entries and the lines.
- List the entries over about 200 characters, with the first words of each.
- Find topic files that no entry points to.
- Find entries whose file does not exist.

## Step 3 - Measure the current state of active projects

For each active project open the "Current state" section at the top of the latest work log and measure it. Over about 5 KB means it is accumulating blocks instead of saying where things stand. Give the project, the size and the file. If a project has no log, say "not measurable".

## Step 4 - Look for contradictions and duplicates

Compare the main instructions, the project rules and the index. Report:

- two rules that say opposite things (quote both, with file and line);
- the same rule written in two tiers;
- current state sitting in a memory file or in the profile.

Do not infer. If two lines look in tension but could both hold in different cases, report them as "to check with the person".

## Step 5 - Look for dead pointers

Check every pointer (a path in an index entry, a stub pointer, a link in the profile) for an existing file. List those that point nowhere.

## Step 6 - Write the report

Short, in this order:

1. Result in two lines: what is over a signal, what is fine.
2. A table: measure, value, signal, file.
3. Findings, one per line, each with its evidence (file, line, quote under 80 characters).
4. Proposals, at most five, each with the file, the change and what the rule was protecting.
5. What you could not check, and why.

Propose removing a rule only after saying what it protects. Proving that the new recall works, and testing in fresh sessions, happen before any removal, with the person.

## Step 7 - Say it in chat

Path of the report and three lines of summary. State that nothing was changed.

## Final check

- No file other than the report was written.
- Every finding has evidence.
- Nothing was inferred without saying so.
