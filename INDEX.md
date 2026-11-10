# Index for the agent

Every file in this folder, what it is and when to open it. Read this once, then open files only when you get to them.

## Entry

| File | What it is | Open it when |
|---|---|---|
| `CLAUDE.md` | Your instructions: rules, the path, limits to state | Always, first |
| `AGENTS.md` | Pointer to `CLAUDE.md` for agents that look for that name | Never, if you already read `CLAUDE.md` |
| `progress.md` | Where the work stands with this person | Always, right after `CLAUDE.md`; update it at the end of every step |
| `README.md` | The page written for the person | Only if they ask what this folder is |

## 1-analysis: understanding the person's system

| File | What it is | Open it when |
|---|---|---|
| `1-analysis/1-procedure.md` | The six opening questions, the reading order, the reading limit, how to write the map | Stage 1 starts |
| `1-analysis/2-capabilities.md` | The eighteen capability cards, nine entries each | You judge the system (Stage 2) |
| `1-analysis/3-measuring-impact.md` | The four measures on past sessions, and the five questions to ask when sessions can't be read | Before writing the report |
| `1-analysis/extract_sessions.py` | Script that prints the first messages of past Claude Code sessions. Prints to screen, saves nothing | Only with the person's permission |
| `1-analysis/4-report-template.md` | The report: eight sections, word limit, tone | You write the report |

## 2-modules: installing one piece

Open a module only after the person accepted the proposal that names it. Each one has the same sections: what it's for, why it works, essential, adaptable, how to install it, check, to roll back.

| Module | Installs | Templates it uses |
|---|---|---|
| `01-log-and-state.md` | Cards 1 and 2: work log, current state at the top | `templates/week.md` |
| `02-session-close.md` | Card 3: the close command that routes information | `templates/skill-log/` |
| `03-project-resume.md` | Card 4: resuming with source and date | `templates/skill-resume/` |
| `04-one-home.md` | Cards 5 and 6: one home per kind of information, dated decisions with superseded ones marked | `templates/homes-table.md`, `templates/decisions.md` |
| `05-tool-rules-and-profiles.md` | Cards 7 and 8: tool files, people profiles | `templates/tool-file.md`, `templates/person-profile.md` |
| `06-corrections-once.md` | Card 9: corrections saved once | `templates/memory-index.md` |
| `07-index-and-archive.md` | Card 10: project index and ordered archive | `templates/project-index.md` |
| `08-maintenance.md` | Card 11: periodic check with thresholds | `templates/skill-health-check/` |
| `09-owner-profile-and-agent-identity.md` | Card 12: who the person is, how the agent behaves | `templates/owner-profile.md`, `templates/agent-identity.md` |
| `10-patterns.md` | Card 13: reusable methods | `templates/pattern-file.md` |
| `11-tiered-memory.md` | Card 14: always-on, per project, on demand | `templates/memory-index.md`, `templates/routing-questions.md` |
| `12-work-plan.md` | Card 15: a written plan for multi-step work | `templates/plan.md`, `templates/skill-plan/` |
| `13-voice.md` | Card 16: voice system | `templates/voice-protocol.md`, `templates/style-file.md`, `templates/voice-learning-log.md` |
| `14-rituals.md` | Card 17: day opening and weekly close | `templates/skill-morning/`, `templates/skill-weekly-close/` |
| `15-calls.md` | Card 18: calls filed and checked against decisions | `templates/skill-save-call/`, `templates/skill-analyze-call/`, `templates/call-analysis.md` |

Dependencies, in short: 01 comes before everything; 02 and 03 need 01; 12, 14 and 15 need 01 and 07, and 15 also needs the decisions file from 04; 10 and 13 work better after 06 and 11.

## 3-example: how it looks when it's finished

Everything here is invented: the owner, the clients, the numbers. The structure and the rules are the real ones. It is a model to read, not files to copy.

| File | What it is | Open it when |
|---|---|---|
| `3-example/README.md` | Map of the example vault and the order to read it in | The person wants to see the finished thing |
| `3-example/rules-and-why.md` | Twenty rules, each with its reason and the incident that produced it | The person asks why a rule exists, or you need to explain a proposal |
| `3-example/vault/CLAUDE.md` | Main instructions of the vault: session start, where things live, state versus memory | You need a model of main instructions |
| `3-example/vault/global-rules.md` | Rules that hold in every project: collaboration, permissions, sources and checks | You need a model of global rules |
| `3-example/vault/Home.md` | List of projects with their status and a pointer to the current week | Cards 10 and 17 |
| `3-example/vault/agent/IDENTITY.md` | How the agent behaves with this owner | Card 12 |
| `3-example/vault/agent/OWNER.md`, `OWNER-details.md` | The owner's profile, and the long detail read on demand | Card 12 |
| `3-example/vault/agent/STYLE.md` | The owner's voice in one page | Card 16 |
| `3-example/vault/agent/knowledge/patterns/` | Two patterns | Card 13 |
| `3-example/vault/agent/knowledge/tools/` | Two tool files | Card 7 |
| `3-example/vault/agent/knowledge/people/` | A person profile and a client profile | Card 8 |
| `3-example/vault/agent/knowledge/decisions/` | A decision that holds across projects | Card 6 |
| `3-example/vault/agent/knowledge/voice/` | Voice protocol, three samples, learning log | Card 16 |
| `3-example/vault/memory/` | The always-loaded index of corrections, with the detail files and one pointer to the on-demand tier | Cards 9 and 14 |
| `3-example/vault/reference/memory-architecture.md` | The three tiers, the routing questions, what is forbidden, the health check | Card 14 |
| `3-example/vault/projects/calvesi-accounting/` | A full project: rules, decisions, index, three weeks of log, a work plan, a call with its analysis | Cards 1 to 6, 10, 15, 18 |
| `3-example/vault/skills/README.md` | Which skills this vault uses and where their text is | Any module that installs a skill |

## Created while you work

| File | What it is |
|---|---|
| `report/system-map.md` | The map of the person's system, confirmed by them |
| `report/report.md` | The report |
