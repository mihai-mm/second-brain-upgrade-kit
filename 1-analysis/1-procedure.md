# Stage 1 - How to analyze a system you don't know

Goal: understand how the person's system is built before judging it. Until the map is confirmed, don't say what is missing.

In this stage you change nothing outside this folder.

## Step A - Six questions

Ask these in a single message and wait for the answers. If you already know an answer from context, don't ask again.

1. Where does your system live? I need the path of the folder, or folders. If part of it lives in a tool that isn't a folder (Notion, a database, a retrieval knowledge base), tell me which.
2. Which agent do you use it with, and how does the agent get to the information: does it read files, search a knowledge base, do you paste things in?
3. Who writes into it: only you, the agent too, automated scripts, other people?
4. Is it your own system or a team's?
5. Which active project can I use as a sample? Ideally one you worked on in the last two weeks.
6. What costs you the most in your system today? One thing that wastes your time, or that you keep having to explain, fix or repeat. If nothing comes to mind, say so.

The answer to question 6 doesn't replace the evidence: the person may name one thing while the sessions show another. Use it to decide where to look first and how to order the proposals. In the report say which proposal addresses what they named, or say plainly that nothing in this folder does.

## Step B - Reading order

Read in this order. At each level stop once you understand the mechanism: you don't need to read everything.

1. **The instructions the agent always receives.** Global instruction files and those in the main folder (for Claude Code: `~/.claude/CLAUDE.md` and the folder's `CLAUDE.md`; for other agents `AGENTS.md` or the equivalent rules). They are the best source: they say how the person wants the system to be used.
2. **Skills, commands, automations.** List names and descriptions without opening every file. Look for: skill or command folders, hooks, scheduled scripts, connectors to email or chat. Open only the ones whose name is about memory, logging, session start or close, resuming a project.
3. **The memory mechanisms.** The agent's memory folders or files, indexes, the configuration of a retrieval knowledge base. For a knowledge base read the description, the configuration and the schema, not the data.
4. **The structure.** The folder tree down to the second level, with the number of files per folder. Don't open the files.
5. **The sample project, plus a second one of your choice.** List the files. Read the project's instruction, memory and index files in full. For files that look like a diary or a log, read the first 80 lines of the most recent one.

## Reading limit

- Don't read more than 40 files in full during the whole stage.
- For a long file read the beginning. Go back for the rest only if a judgment needs it.
- Don't bulk-read raw material: transcripts, emails, exports, knowledge base records.
- If the system is a retrieval knowledge base with thousands of records, don't scroll through it. Read how it is fed and how it is queried. If there is a search command, run three test searches on the sample project: "where are we", a recent decision, a fact that changed over time. Note what comes back.

## Step C - The map

Write `report/system-map.md` in this folder. One page, with these entries:

- **What lives where.** The main places and what they contain.
- **How information gets in.** Who writes, when, with which mechanism: by hand, the agent on request, automated scripts.
- **How it reaches the agent.** What is always loaded, what is read on request, what is searched.
- **What happens automatically** and what depends on the person doing something.
- **How a project gets resumed today.** Describe the real steps, as you understood them.
- **What I couldn't see.** External tools, folders you can't access, parts of the system the person only told you about.

Then show the map to the person and ask two things: "Is this right?" and "Is there anything you use that I haven't seen?". Correct the map with their answers. Only once they confirm, move to Step D.

Update `progress.md`.

## Step D - Judging the eighteen capabilities

Open `2-capabilities.md`. For each card assign a status:

- **Present**: the system does that thing, even in a different form. Name the form and the file that proves it.
- **Partial**: it does it halfway, or only when the person remembers. Say what is there and what is missing.
- **Missing**: you searched, you asked the person, it isn't there.
- **Can't verify**: it might exist somewhere you can't read.

Rules for the judgment:

- Before writing "missing", ask the person a concrete question about that capability. Group these questions in a single message.
- Count the effect, not the name. A retrieval knowledge base that gives more weight to recent records partly covers the outdated-information problem: it is "partial" on card 6, not "missing".
- When unsure between "present" and "partial", check whether the thing happens even when the person isn't thinking about it.

## Step E - Measure

Follow `3-measuring-impact.md`.

## Step F - Report

Follow `4-report-template.md`.

## If the system belongs to a team

Run the analysis on one person's work, the person you are talking to. In the report state that the log and the current state have been tested with a single author, and that in a team someone has to decide who writes them. Don't propose team rules as if they were proven.
