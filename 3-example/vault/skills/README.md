# Skills used by this vault

Example file, all content invented. A skill is a written procedure the agent runs when Livia types its command. In Claude Code the skills live in `.claude/skills/` at the root of the vault. This example does not include them: the text of each is in the kit.

| Skill | When it runs |
|---|---|
| `log` | At the end of a working session. Reviews what came up and sends each piece to its home: progress into the log, the state if it changed, the decision into `decisions.md`, the correction into `memory/`. Says what it wrote and what it could not verify |
| `resume` | When Livia says "let's pick up X". Rebuilds the state from the latest log, compares it with the later entries and the decisions, and answers with source and date |
| `plan` | When a job has four or more steps, or will outlast the session. Writes the plan file in the project before the first step |
| `morning` | At the start of the day. Reads the current state of the active projects and returns what is open, what waits on whom and what has a date |
| `weekly-close` | At the end of the week. Carries the state of each active project into the new week's log, keeps only the open threads and updates the pointer in `Home.md` |
| `health-check` | Every two or three months, or when a trigger of the [memory architecture](../reference/memory-architecture.md) fires. Measures and reports, changes nothing |
| `save-call` | After a call. Files the transcript in the project, adds the line in the index and the log |
| `analyze-call` | After `save-call`. Extracts actions and open points, compares what was said with the recorded decisions, and proposes in one confirmation what to save and where |

## Where their text is

The text of each skill is in the kit, relative to the kit root: `2-modules/templates/skill-<name>/SKILL.md`, for example `2-modules/templates/skill-log/SKILL.md`. The skills `log`, `resume`, `plan`, `morning`, `weekly-close`, `health-check`, `save-call` and `analyze-call` each have their own folder there.

A skill is installed in a person's system only after the check of its module passes in a fresh session.
