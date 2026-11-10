# Module 02 - Session close

Installs capability 3. It only makes sense if there is at least a log with a current state (module 01).

## What it's for

At the end of the work the person types one command. The agent looks at what came up in the session and sends it to the right place, then says what it wrote. It is what makes everything else work on the days the person is tired or in a hurry.

## Why it works

- **One single action.** If closing means remembering four places, it doesn't get done. With one command the effort is the same every time.
- **First decide what there is, then where it goes.** The agent lists what came up and picks one destination for each thing. Without this step the same fact ends up in two files.
- **The recap tells three cases apart.** Written and verified, nothing to write, not verified. The third is the one that matters: a system that always says "all saved" isn't credible.
- **It writes little.** Entries have a line cap. Nobody rereads a wordy log, not even the agent.

## Essential

1. One command, always the same.
2. Opening check: if there is nothing concrete to save, it says so in one line and stops.
3. Each piece of information goes to one place only, according to the homes table (module 04). If there is no table, there are two destinations: log and state.
4. The log entry is written without asking for confirmation. The state is updated only if something changed that moves the project.
5. The agent's interpretations about the person are not saved as facts: they are proposed.
6. Final recap with the three cases, one line per destination.
7. The whole log file is not read just to add an entry: the beginning is enough.

## Adaptable

- The command name. In Mihai's system it is called `/log`.
- The phrases that trigger it ("let's wrap up", "see you tomorrow").
- The destinations beyond the log, depending on what the person has.
- How much to ask for confirmation. The template asks only for what changes the working rules.
- The mechanism: in Claude Code it is a skill; in other agents it can be a saved command or a reusable prompt.

## How to install it

1. Open `templates/skill-log/SKILL.md`. It is a generic template: it must be adapted, not copied.
2. Fill in the "Where I write" section with the real paths of the person's system. Remove the destinations that don't exist.
3. Translate the skill into the person's language, if it's different.
4. Show them the final text and say where you will put it. In Claude Code: a folder named after the command inside the skills folder, the project's or the personal one. If you don't know where their agent keeps skills and commands, ask: don't guess.
5. Create the file after the yes and note it in `progress.md`.

### A reminder, if the person wants one

The command doesn't run by itself. Mihai added to his own setup a check that stops him when he is about to close or compact a conversation with unlogged changes. That piece is not in this folder, because it depends on each person's environment. If the person asks for it, explain the principle and work out together how to get it in theirs: for example a hook that, before closing, checks whether files were modified after the last log entry.

Don't install automations unless the person asks.

## Check

Run a short session on the trial project in which two things happen: something gets decided and the person corrects the agent once. Then run the command. The test passes if:

- the week's file has a new entry under today's date, short and with no copy of the work done;
- the decision is in its file, if module 04 is installed, otherwise it is in the entry;
- the recap lists the destinations and says what wasn't written and why.

Run it a second time right after: it must answer that there is nothing new to save, without duplicating the entry.

## To roll back

Delete the skill's folder. The entries already written in the log stay and do no harm.
