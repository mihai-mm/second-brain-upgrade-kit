# Module 09 - Owner profile and agent identity

Installs capability 12. It needs a place the agent reads at every session (the main instructions or an always-loaded file). It works better after tiered memory (module 11), because it decides how heavy the always-loaded layer can be.

## What it's for

The agent should know who it is working for and how it is expected to behave, without the person explaining it again at every session. Two short files do that: a profile of the person, and an identity for the agent.

## Why it works

- **Lasting facts only.** A profile that says "this quarter I'm working on X" is wrong within a few weeks, and the agent will still believe it. Role, way of working, constraints and decision habits change slowly. Status changes fast and already has a home (the work log).
- **A section that says where the state lives.** The profile does not hold the current state, but it tells the agent where to find it: "Current projects: the project list. State of one project: the top of its latest work log." The agent gets the way to the answer, not a copy that goes stale.
- **Detail in a separate file.** What is true but not needed in every session (history, personal context, business model, health) moves to a second file with a "when to read it" list. The profile stays light, and the agent opens a section when the request touches its subject.
- **A size signal.** A profile of about 16 KB or more is a prompt to look at it again: something long is probably detail that belongs in the second file. The number is an attention signal, not a law.
- **Identity is about behavior.** Without it the agent treats the person as a generic user, agrees where they wanted to be challenged, and re-learns the tone every session.
- **Interpretations are not facts.** "You seem to avoid X" is the agent's reading. Saved as a fact, it comes back in every session as if it had been confirmed.

## Essential

1. **Owner profile**, always loaded, lasting facts only: who the person is professionally, how they work, how they decide, constraints that always hold. No dated status.
2. In the profile, a section "Where the current state lives (not in this file)": a table of what the person might look for and where to read it.
3. A second file for long detail, with a "when to read it" table, one row per section. The agent opens a section when the request touches it.
4. A size check on the profile: about 16 KB is the signal to review it.
5. **Agent identity**, always loaded, with these parts: who the agent is for this person; how it relates (candor, pragmatism, continuity across projects, reasoned proactivity: it proposes before acting); what it does not do; what it adds (memory across projects, and checking the person's own summary of a project against the record: the work log, the tasks, the data); how it grows.
6. The identity file changes only on the person's explicit request.
7. What the agent concludes about the person is proposed in chat. It is saved as a fact only after the person confirms it.

## Adaptable

- File names, sections and language. Use the person's own words.
- The size threshold, which depends on the agent and the model.
- Where the files are loaded from: a line in the main instructions, a user section, the system prompt of a personal agent.
- If the person already has an "about me" file or custom instructions, reshape that one. Do not add a second copy.
- For a retrieval knowledge base: the two files can be records flagged as "always include". What matters is that something guarantees they are read at every session.

## How to install it

1. Look for what exists: an "about me" file, custom instructions, behavior rules scattered in project files. Show the person what you found, and where each piece is loaded from.
2. **Write the profile with the person, in a conversation, from their words.** Ask one section at a time: role, how they work, how they decide, constraints that always hold. Never infer personality from past sessions and save it as fact. If past sessions suggest something, say it as a proposal and wait for the answer.
3. Write the "where the current state lives" section with the real locations from the person's system. Check that each path exists.
4. If the draft goes over about 16 KB, or a section is long detail, split it: the profile keeps the short version, the second file keeps the detail, and the "when to read it" table points to it.
5. Write the identity with the person, using `templates/agent-identity.md`. Ask how they want to be challenged, what the agent must never do, when it should ask and when it should just do. Use their words.
6. Show the exact text and the path of each file before writing it. Wait for a yes. Add one line to the main instructions that loads both files, showing it first.
7. Note in `progress.md` the files created and the line added.

Do the profile first, check it, then the identity.

## Check

Two tests, in fresh sessions.

1. In a project that has no instructions of its own, ask for something where the profile matters (for example an explanation of a technical choice). The answer matches the level and style in the profile without being told.
2. Tell the agent a summary of a project that is more optimistic than the record ("it's almost done"). The agent checks the work log or the tasks before accepting it, and says what it found.

Also measure the profile: its size, and whether any dated status is left inside.

## To roll back

Delete the two files and the line that loads them. If the person already had an "about me" file, it was not touched.
