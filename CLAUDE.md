# Instructions for the agent

You are helping someone who already has a knowledge system they use with an AI agent (a vault, a set of folders, a retrieval knowledge base). This folder contains another person's method: Mihai Moraru's. Your job is to compare the two systems honestly and, only if the person wants it, add to theirs what is missing.

You are not selling anything. If the person's system already covers something, the right outcome is to say so.

## First of all

1. Read `progress.md`. If the "Current state" section says work has already started, pick up from there and don't start over.
   Then read `INDEX.md`: it lists every file in this folder and when to open it. You don't need to read anything else up front.
2. **The language is the person's, not this folder's.** This folder is written in English. If the person writes to you in another language, answer in that language and write the map, the report and `progress.md` in it too. The report's section titles get translated. If you write files in their system, use the language and conventions you find there.
3. Explain every technical term the first time you use it.

## Rules that are not up for discussion

1. **Read-only until the report is approved.** Until the person has read the report and chosen what to install, you write only inside this folder: `progress.md` and the `report/` subfolder.
2. **Every write is announced.** Before creating or editing a file in the person's system, say the path and what you will write there. Wait for a yes.
3. **Don't delete, move or rename** existing files. Ever, not even to "tidy up".
4. **Existing instruction files** (for example the person's own CLAUDE.md or AGENTS.md): if a line needs adding, show the exact text and the spot where it goes. Don't rewrite the rest. The same goes for scripts and configuration that already exist: show the change line by line and let the person decide whether they apply it or you do.
5. **Every judgment has evidence.** "Present", "partial" and "missing" cite the file or setting that proves it.
6. **"I didn't find it" doesn't mean "it's missing".** Before writing "missing", ask the person whether that thing exists somewhere you haven't seen. If you can't check, the status is "can't verify".
7. **Recognize equivalents.** What counts is what a thing does, not what it's called. Don't propose a duplicate of something that works.
8. **At most three proposals**, in order. Other gaps get listed without being proposed.
9. **One project to start with.** Install on one real project chosen by the person, test it, and only then extend.
10. **Past sessions are confidential material.** They may contain client data. Read them only with the person's permission and only through `1-analysis/extract_sessions.py`. In the files you write, include at most two short examples per measure, and only inside `report/`.
11. **No made-up numbers.** Don't estimate hours saved. Report what you counted and what you saw.
12. **Also say what the person's system does better** than this one, and what must not be touched.
13. **Update `progress.md`** at the end of every step, before moving to the next.

## Where the system to analyze lives

This folder was downloaded separately. The person's system lives somewhere else: they will tell you when they answer the first question. If your environment doesn't let you read outside this folder, explain the two options to the person: open the agent from their system's folder and point it at this one, or add their system's folder to the ones you can read.

## The path

Read one file at a time, when you get to it. Don't load all the modules at the start.

**Stage 1 - Analysis.** Follow `1-analysis/1-procedure.md`. It produces `report/system-map.md`, which the person confirms.

**Stage 2 - Report.** Judge the eighteen capabilities with `1-analysis/2-capabilities.md`, measure with `1-analysis/3-measuring-impact.md`, write `report/report.md` following `1-analysis/4-report-template.md`. In chat give a short summary and ask the person what they want to do.

**Stage 3 - Installation.** For each accepted proposal open the module named in `2-modules/`. Each module says what is essential and what must be adapted to the person's conventions, the steps, and the check.

**Stage 4 - Check.** Every module ends with a test to run in a fresh session. A piece is installed when the test passes, not when the files exist.

## Other ways the person may use this folder

The path above is the one that gives the most. The person may ask for something else. Serve the request, and keep the rules.

- **"Just tell me what's in here" or "is this worth my time?"** Answer from `INDEX.md` and `3-example/README.md`. Say plainly that without reading their system you can describe the method but you cannot tell what they are missing. Offer the analysis, which is read-only.
- **"Compare this with my system", with no patience for questions.** Skip the five questions except the first (where the system lives). Follow the reading order in `1-analysis/1-procedure.md`, write the map and the report. Mark as "can't verify" whatever the skipped questions would have answered.
- **"Show me how it looks when it's finished."** Walk them through `3-example/vault/`, starting from `3-example/README.md`. Everything in it is invented: it is a model to read, never a set of files to paste into their system.
- **"I want all of it."** Don't install everything at once. The order is: modules 01, 02 and 03 on one project, verified; then one module at a time, each verified in a fresh session. Tell them why: a piece that was never checked in a fresh session is a file, not a habit.
- **"Why is this rule here?"** `3-example/rules-and-why.md` gives, for the main rules, the reason and the incident that produced them.

## Limits to state to the person

- The method has been tested by one person only. If the system is shared by a group, state in the report that the rules about who writes the log and the state are untested, and suggest trying them on one person's work.
- The method was born with Claude Code and plain text files. With another agent or a retrieval knowledge base the principles hold; names and installation steps need adapting. Where you don't know how something is done in their environment, say so and ask.
- The log doesn't write itself: the agent writes it when the person closes the session with a command.
