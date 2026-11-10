# Module 03 - Resuming a project

Installs capability 4. It requires the current state (module 01).

## What it's for

When the person says "let's pick up X", the agent first rebuilds where things stand, then works. The answer says which file the information comes from and what day it is from, so the person sees at once whether they can trust it.

## Why it works

- **The state is a summary, and summaries fall behind.** That is why the agent compares the state with the most recent log entries. If they don't match, it says so.
- **The file name counts more than the modification date.** Fixing a typo in an old file makes it look recent. The most recent week is the one with the highest name.
- **An old log doesn't mean an idle project.** Work may have happened without closing the session. The agent flags it instead of concluding there is nothing to do.
- **Source and date in the answer.** It is what separates "I know where we are" from "I think I know".

## Essential

1. State first, then work.
2. Reading order: project instructions, index, current state of the latest week, latest log entries, relevant decisions.
3. The answer contains: where we are, source and date, discrepancies if any.
4. The decisions file is read for decisions, not as a summary of the state. A decision marked as superseded no longer holds.
5. If the sources agree and the request is clear, the agent carries on without asking for ritual confirmations.
6. If a discrepancy changes the work to be done, it asks one precise question.

## Adaptable

- The skill name and the phrases that trigger it.
- Extra sources: a task list, open work plans, a calendar.
- For someone with a retrieval knowledge base: after the state, the agent can search there for detail. The state says what to search for.

## How to install it

Two ways. Choose with the person.

**As a rule.** Add to the main instructions a paragraph that requires this reading every time a project is resumed. It is the simplest way, and it is enough if there are few projects.

**As a skill.** Adapt `templates/skill-resume/SKILL.md` to the person's paths and names, show them the text, install it after the yes.

In both cases note in `progress.md` what you added and where.

## Check

Three tests, in fresh sessions.

1. "Let's pick up [trial project]": the answer cites the state file and its date.
2. Edit the state by hand, writing something the latest entries contradict, then ask again: the agent must flag that state and entries don't match. Put the state back as it was.
3. "Where are we?" on a project that has no log: the agent must say the source is missing and what it rebuilt the answer from. It must not create a log on its own initiative.

## To roll back

Remove the paragraph from the instructions, or delete the skill's folder.
