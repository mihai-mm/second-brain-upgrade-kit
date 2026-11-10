# Memory architecture

Example file, all content invented. How Livia's system splits information by when it is loaded, how a new piece of information is routed, and how the system is checked. Read when maintaining the system, or when it is unclear where something goes.

## The three tiers

| Tier | Where | Loaded | What it holds |
|---|---|---|---|
| 1. Always | `memory/` (the index `MEMORY.md` and one file per correction), plus `CLAUDE.md`, `global-rules.md`, `agent/IDENTITY.md`, `agent/OWNER.md` | At every session start, automatically | Corrections to how the agent works, pointers to the other tiers, the rules that must hold everywhere |
| 2. Per project | `projects/<name>/decisions.md`, with the project's `project-rules.md` and log | When working on that project | Decisions, things learned and numbers of one client or one project |
| 3. On demand | `agent/knowledge/` (patterns, tools, people, decisions that hold across projects, voice) and `agent/STYLE.md`, `agent/OWNER-details.md` | When the task calls for it, reached from a pointer | Profiles of clients and people, tool lessons, methods that worked, the voice system |

One rule per tier. Tier 1 is what must be in front of the agent before a trigger phrase arrives. Tier 2 is what only matters inside one project. Tier 3 is what is read when the agent already knows it is relevant.

## Routing questions: where a new piece of information goes

1. **Is it about one client or project, or does it hold across projects?** One project: question 2. Across projects: question 3.
2. **A decision, an insight or a number about the work, or a lasting fact about a client?** The first: `projects/<name>/decisions.md`. The second: the profile in `agent/knowledge/people/`.
3. **Is it about how the agent behaves, or about the world?** Behaviour: `memory/`, as a feedback file with one line in the index. The world: question 4.
4. **A method that worked more than once, or a single fact?** A method: `agent/knowledge/patterns/`. A tool lesson: `agent/knowledge/tools/`. A single fact, such as a limit of one tool: the tool file.
5. **Is it a rule that belongs to one skill?** Then it goes in that skill, not in memory.
6. **Is it about Livia herself?** Lasting facts: `agent/OWNER.md`. Long detail: `agent/OWNER-details.md`. Her voice: through the voice protocol, never directly into the style file.
7. **Is it where a project stands, or a next step?** Not memory, never. It goes in the current state of the project log.

**Stub pointer.** When a cluster of lessons about one subject has matured (several corrections about the same tool), consolidate it into one file in tier 3 and leave one pointer in tier 1, such as `reference_tools_in_knowledge.md`. The index goes from many lines to one, and the pointer keeps the lesson findable. Behavioural corrections do not migrate: they often fire on a phrase of Livia and would lose that if moved.

## Forbidden

1. The same information in more than one tier. One source of truth. If it is in the profile, it is not in the index.
2. An index line over 200 characters, or one that contains the case. The case lives in the linked file.
3. A convention of the vault copied into memory. The vault instructions are loaded anyway.
4. Current state in any memory, profile or identity file. It lives in the latest log of the project.
5. A method that holds across clients buried in one project's `decisions.md`. The project keeps the decision, the pattern lives in tier 3.
6. A client profile in `memory/`. It belongs in `agent/knowledge/people/`.

## Health check

Run the `health-check` skill every two or three months. It reads and measures. It changes nothing by itself: it writes a short report with evidence for each point, and Livia decides what to fix.

**Triggers:**

- The model or the agent used by default changes. Each model reads instructions a little differently, and rules written for an older one can become redundant or too rigid.
- The index `MEMORY.md` is over 20 KB or 180 lines.
- A warning of truncation appears at session start.
- More than three months since the last check.
- Livia asks for one.

**Thresholds of attention:**

| What | Threshold |
|---|---|
| Weight of the session start, measured before the first message | Growing by more than a fifth since the last check |
| `OWNER.md` | Over about 16 KB, or a dated status inside it |
| A `CLAUDE.md` | Over 200 lines |
| Index `MEMORY.md` | Over 20 KB or 180 lines (check how much the agent actually loads: the limit depends on the version) |
| An index line | Over 200 characters |
| Current state of the latest log of an active project | Over 5 KB |
| A test case of the previous report | Worse than before |

**What the check looks at:**

- Entries that may be obsolete: verify the content and the pointers. Age alone does not prove an entry is unused. Propose removal only when it is shown that it is out of date or duplicated.
- Index lines over the limit: shorten, and move the detail to the linked file.
- Detail files with no line in the index: check whether another pointer reaches them, and restore the line if they matter. Never delete automatically.
- Clusters that matured: consolidate into tier 3 with a stub pointer.

Before removing or moving a rule: list what it was protecting, set up the new way to reach it before taking the old one away, and test in a fresh session.
