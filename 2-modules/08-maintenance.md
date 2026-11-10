# Module 08 - Periodic maintenance

Installs capability 11. It makes sense when the system is already a few months old.

## What it's for

It keeps the system from getting so heavy that it works worse: instructions that are too long, rules that contradict each other, states that have grown out of control.

## Why it works

- **What the agent always reads has a cost.** Every line loaded at the start of a session takes attention away from the others. Past a certain length the agent starts ignoring part of it.
- **Rules age.** A rule written to work around a flaw in an old model can become useless, or harmful, with the new one.
- **Removing is riskier than adding.** A rule that looks superfluous often protects against a mistake that is no longer seen precisely because the rule is there. That is why, before removing, you check what it was protecting.

## Essential

1. A cadence: every two or three months, and at every model change.
2. The check is read-only and produces a list. Corrections are decided with the person.
3. What you look at:
   - how heavy the files the agent loads every session are;
   - how long the current state of the active projects is;
   - rules that contradict each other or say the same thing in two places;
   - memory entries or corrections with no reason, no scope, or pointing to files that no longer exist;
   - tool files with old lines to recheck.
4. Before removing a rule: understand what it was protecting, and prove in a fresh session that without it the behavior stays right.

## Triggers

Run the check when one of these happens:

- the model in use changes (a new family or a new version as the default): each model reads instructions a little differently, and a rule written for an old one can become superfluous or too rigid;
- the memory index goes over its size limit, or the agent warns that it was truncated at session start;
- more than three months have passed since the last check;
- the person asks for it.

## Thresholds to start from

These are the ones Mihai uses with Claude Code. They are attention signals to adapt, not laws. They depend on the agent and the model, and they change: check in your environment's documentation how much is really loaded.

- The weight of what loads at session start: measure it and compare it with the previous check. Any number depends on the environment.
- The owner profile over about 16 KB, or with dated status inside it.
- An instructions file over about 200 lines.
- The memory index over about 20 KB or 180 lines.
- The current state of a project over about 5 KB, about one page: it means it accumulates instead of saying where things stand.

## Removing or moving a rule

Before removing or moving a rule:

1. Inventory what it protects: the mistake it prevents, or the behavior it keeps.
2. Prove that the new recall works before removing the old one. Add the new place first and check that the agent finds it.
3. Test in fresh sessions, with a case that used to need the rule.

If the test fails, restore the rule. Nothing is removed in the same step in which the replacement is created.

## Adaptable

- The cadence and the thresholds.
- Who does it: a skill launched by hand, a scheduled program that writes a report, a calendar reminder.
- In a retrieval knowledge base the equivalent maintenance is cleaning out records that are no longer needed and checking that the ingestion scripts still work.

## How to install it

1. Do a first check right away, read-only, on the five points above. It is useful even on its own.
2. Write the result in `report/maintenance-check.md` in this folder: what you measured, what goes over the thresholds, with the file for each.
3. Show it to the person. For each item, decide together whether to act.
4. If they want to repeat it, propose how: a reminder, or a skill that repeats these steps. `templates/skill-health-check/` is a read-only skill that does exactly this and writes a short report. Write it only if they ask for it, showing it first and waiting for a yes.
5. Note in `progress.md` the report written and, if installed, the skill created.

## Check

The first check produces a short list, with the evidence for each item, and has not modified any of the person's files.

## To roll back

There is nothing to remove: the check doesn't write into the person's system.
