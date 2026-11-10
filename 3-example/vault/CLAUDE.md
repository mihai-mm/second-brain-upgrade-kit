# CLAUDE.md - Livia Lanteri's vault

Example file, all content invented. In Claude Code this file sits at the root of the vault and is loaded at the start of every session.

Rules that hold in every project: [global-rules.md](global-rules.md). Who the agent works for: [agent/OWNER.md](agent/OWNER.md). How the agent behaves with her: [agent/IDENTITY.md](agent/IDENTITY.md).

## Session start

1. The always-loaded layer arrives on its own: this file, the global rules, the corrections index [memory/MEMORY.md](memory/MEMORY.md). Read IDENTITY and OWNER once, if they are not already in context.
2. Read [Home.md](Home.md) when the request is about status, a list of projects or a choice between them, or when it is unclear where to work. For a request about a file or a project already named, skip it.
3. Before working inside a project, read its `project-rules.md`. Local exceptions hold inside that project. Limits of the environment and Livia's mandate always come first.
4. For a small edit, the applicable rules, the file and what depends on it are enough. To resume a project, use the reconciliation pass below.
5. Before writing anything that goes out under Livia's name, enter through [agent/knowledge/voice/voice-protocol.md](agent/knowledge/voice/voice-protocol.md).

## Reconciliation pass: before answering "where are we"

Rebuild the facts first, then answer.

1. Pick the latest log by the week in its name (`YYYY-Www`), never by modification date.
2. Read its `## Current state` section and the day entries after the date of that section.
3. Compare: if an entry is newer than the summary, or contradicts it, say so.
4. Read the decisions that matter for the question in `decisions.md`.
5. Answer with the source and its date: "Source: current state of week 42, updated October 15."

An old log does not prove the project is idle. A recent date does not prove the whole text is current. A line marked "not rechecked" stays marked: do not turn it into a fact. Never use `memory/` as the current state.

If the facts agree and the mandate is clear, carry out the step asked for without a ritual confirmation. If an unresolved discrepancy changes the work, ask, and keep working on what does not depend on the answer.

## Folder map

| Folder | What it holds |
|---|---|
| `Home.md` | The projects, one line of status each, a pointer to the current week of each |
| `projects/` | One folder per project: rules, decisions, log, calls, reports. Entry point: the index named like the folder |
| `agent/` | Identity of the agent, profile and style of the owner, and `knowledge/` (patterns, tools, people, decisions that hold across projects, voice) |
| `memory/` | The always-loaded index of corrections and one file per correction |
| `reference/` | How the system itself works. Read when maintaining it |
| `skills/` | The commands this vault uses. See [skills/README.md](skills/README.md) |

## Which information lives where

| Information | Home |
|---|---|
| Where a project stands, what is open, next step | Current state at the top of the latest `projects/<name>/log/YYYY-Www.md` |
| What was done, day by day | The same log, entries below the state |
| Decisions with the reason, things learned, numbers that last | `projects/<name>/decisions.md` |
| Decisions that hold across projects | `agent/knowledge/decisions/` |
| Rules and boundaries of a project | `projects/<name>/project-rules.md` |
| Durable facts about a client or a person | `agent/knowledge/people/` |
| What was learned about a tool | `agent/knowledge/tools/` |
| Methods that worked more than once | `agent/knowledge/patterns/` |
| Corrections to how the agent works | `memory/` |
| A plan for a job of four or more steps | `projects/<name>/reports/plan-<name>.md` |
| Transcripts, material received, work produced | `calls/`, `materials/`, `reports/` of the project |
| Task list | The task app, not this vault |

The same piece of information is never written in two homes. Elsewhere, put a pointer. If it is not clear where something goes, ask before writing.

## Current state versus memory

- The log has the state on top, then the days in reverse order. Entries of the same day stay in time order.
- The state is rewritten, not accumulated. At the start of a new week, copy it into the new file and clean it: only the threads still open stay. When in doubt, a thread stays. If you did not recheck it, mark it "not rechecked" instead of removing it. Closed threads leave their detail in the dated entries.
- The state says where we are, it does not tell the story. Past about 5 KB, move detail out and tell Livia.
- Daily history is append-only. Correct a false statement with a dated note, never by rewriting the event. Do not create empty logs just to comply.
- Decisions have a date and a reason. A decision that is replaced is marked as superseded and points to the new one. It is not presented as valid.
- No next steps and no work status in `decisions.md`, in profiles or in `memory/`.

## When a project changes status

When Livia decides a change (pause, close, restart), update in the same session, without asking again for the same decision:

1. A dated event and the new summary in the project log.
2. The decision and a short reason in `decisions.md`.
3. The status line and the pointer in `Home.md`.
4. The client profile only if the lasting relationship changes. No pending items in it.

State what does not apply or could not be updated. Do not say the ritual is complete if a step is missing. Moving or archiving a folder is not implied by a pause or a close.

## Admission rule: opening a new project folder

Open a folder only for a finite goal or a continuing responsibility that no existing folder covers. First check whether a file or a section in an existing project is enough. If two folders overlap, report the unclear boundary and do not reorganize by trial. A new project starts with: `project-rules.md`, `decisions.md`, the index named like the folder. Other folders appear when they are needed.

A project cannot start without a named person on the client side who answers within two working days: see [the September 2026 decision](agent/knowledge/decisions/2026-09-named-contact-on-every-project.md).

## Maintaining these instructions

- Every rule has a scope, an observable action and, if any, an exception. A rule without an action you can check is a wish.
- Before adding a rule, look for an existing one to fix.
- Specialist procedures go in skills and reference notes, not here. This file stays under 150 lines.
- When a convention changes, search the whole vault for its copies. Update the prescriptive ones. Keep history, quotes and examples as history.
- Verify a change with a real case of use, and say which tests were not run.

## Read when

| When | Read |
|---|---|
| Memory, routing of a new piece of information, maintenance | [reference/memory-architecture.md](reference/memory-architecture.md) |
| Building or changing an automated send | [agent/knowledge/tools/automated-email.md](agent/knowledge/tools/automated-email.md) |
| Receiving data exported from a spreadsheet | [agent/knowledge/tools/spreadsheet-exports.md](agent/knowledge/tools/spreadsheet-exports.md) |
| Writing to a person or a client | The profile in `agent/knowledge/people/`, for example [Tiziano Olivari](agent/knowledge/people/tiziano-olivari.md) and [Calvesi Accounting](agent/knowledge/people/calvesi-accounting.md) |
| A report or audit that states facts | [agent/knowledge/patterns/levels-of-evidence.md](agent/knowledge/patterns/levels-of-evidence.md) |
| Preparing questions for a client | [agent/knowledge/patterns/discovery-open-questions.md](agent/knowledge/patterns/discovery-open-questions.md) |
| Anything written in Livia's name | [agent/knowledge/voice/voice-protocol.md](agent/knowledge/voice/voice-protocol.md) |
| Deciding whether to take a project | [agent/knowledge/decisions/](agent/knowledge/decisions/2026-09-named-contact-on-every-project.md) |
