# Module 05 - Rules per tool and profiles per person

Installs capabilities 7 and 8.

## What it's for

The agent stops repeating the same mistakes with the tools the person uses most, and writes to each client or collaborator in the right way without being told again.

## Why it works

- **What holds for all projects can't live inside one project.** A mistake understood while working for one client is useful for the next one too. If it stays in that client's files, the agent will never see it again.
- **It is read at the right moment, not always.** Ten rules files loaded at every session weigh on the agent and dilute each other. One line in the main instructions says which file to read before using which tool.
- **Finding a mistake by searching for it is different from knowing about it up front.** In a retrieval knowledge base the noted mistake comes back only if the agent thinks to search for it, that is, when it already suspects the problem. The tool file is read before starting.
- **The person and the work are two things.** How a client wants to be contacted holds for years. Where their project stands holds for a week. That is why the profile contains no pending items.

## Essential

1. One file per tool and one per client or person, outside the projects.
2. In the main instructions, one line for each saying when to read it.
3. In a tool file, only what was verified on real work goes in: the mistake, the cause, what to do instead.
4. In a person's profile, only durable facts go in, said by them or observed more than once. No state of the work, no judgments.
5. The files grow one line at a time, when something happens. They are not filled in ahead of time.

## Adaptable

- Where they live: a folder in the vault, the agent's configuration folder, the retrieval knowledge base with a dedicated record type.
- The fields of the files.
- For a team: tool files are easy to share. Those about people need to be decided case by case: ask the person.

## How to install it

1. From the session analysis (measure 3) work out the two tools and the two people on which corrections repeat the most. If you couldn't read the sessions, ask the person which they are.
2. Propose creating only those files, starting from `templates/tool-file.md` and `templates/person-profile.md`. Fill them with what you found written, naming the source of every line. What isn't written anywhere, you ask.
3. Show the files and the lines you would add to the main instructions, for example: "Before working with [tool] read [path]" and "Before writing to [person] or on their behalf read [path]".
4. Create and add after the yes. Note everything in `progress.md`.

Don't create empty files for tools or people you have nothing to write about.

## Check

1. In a fresh session, ask for a job with a tool that has a tool file: the agent must read it before starting and avoid the noted mistake.
2. Ask for a draft message to a person who has a profile: the draft must respect the written preferences, without you repeating them.

## To roll back

Delete the files created and remove the lines added to the instructions.
