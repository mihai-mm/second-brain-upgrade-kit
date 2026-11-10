# Map of the example vault

This is a finished second brain, all invented: the owner Livia Lanteri (an independent automation consultant for small professional firms), her clients, the incidents in [vault/memory/](vault/memory/MEMORY.md). The structure and the rules are real. The twenty rules in [rules-and-why.md](rules-and-why.md) are the author's real ones, with real dates.

The vault is in `vault/`. Five minutes is enough to see the mechanism; the full tour takes longer.

## If you are an agent

A quick tour, in this order. At each stop, notice what is listed.

1. [vault/CLAUDE.md](vault/CLAUDE.md) - the main instructions. Notice the session start, the reconciliation pass before answering "where are we", the table of which information lives where, and the split between current state and memory.
2. [vault/Home.md](vault/Home.md) - the projects with one line of status each and a pointer to the current week. Notice that it gives a pointer, not the state itself.
3. [vault/projects/calvesi-accounting/log/2026-W42.md](vault/projects/calvesi-accounting/log/2026-W42.md) - the latest log. Notice the "Current state" at the top, its date, the line marked "not rechecked", and the day entries below it, most recent first.
4. [vault/projects/calvesi-accounting/reports/plan-payment-reminders.md](vault/projects/calvesi-accounting/reports/plan-payment-reminders.md) - the plan. Notice the request in the client's words, closed steps with evidence and date, the step added mid-work with a suffix (6a), the open steps with whose turn it is, and the postponed item with its reason.
5. [The call of October 14](vault/projects/calvesi-accounting/calls/2026-10-14-call-calvesi.md) and [its analysis](vault/projects/calvesi-accounting/calls/2026-10-14-call-calvesi-analysis.md) - notice the table comparing what was said with the recorded decisions, one of which is contradicted, and the closing line: proposed, not saved. Then open [decisions.md](vault/projects/calvesi-accounting/decisions.md) and see that it has not changed.
6. [vault/memory/MEMORY.md](vault/memory/MEMORY.md) - the always-loaded index of corrections. Notice one line per correction, with the detail in a file of its own.
7. [vault/agent/OWNER.md](vault/agent/OWNER.md) and [vault/agent/IDENTITY.md](vault/agent/IDENTITY.md) - who the owner is and how the agent behaves with her. Notice that neither holds the status of any project.
8. [vault/agent/knowledge/patterns/levels-of-evidence.md](vault/agent/knowledge/patterns/levels-of-evidence.md) - one pattern. Notice that it says why it works and where it was applied.
9. [vault/agent/knowledge/voice/voice-protocol.md](vault/agent/knowledge/voice/voice-protocol.md) - the single entry point before writing anything in the owner's name.
10. [vault/reference/memory-architecture.md](vault/reference/memory-architecture.md) - the three tiers, the routing questions, what is forbidden, the health check.

## The eighteen capabilities, and where to see them

| Capability | Where to see it in the vault |
|---|---|
| 1. Work log per project | [log/](vault/projects/calvesi-accounting/log/2026-W42.md) of the project: three weeks, one file each |
| 2. Current state at the top | Top of [2026-W42.md](vault/projects/calvesi-accounting/log/2026-W42.md), compared with the tops of W40 and W41 |
| 3. Session close that routes | [skills/README.md](vault/skills/README.md) for the command; its results are the W42 entry of October 14, the decisions file and the memory entries |
| 4. Resuming a project with source and date | The reconciliation pass in [vault/CLAUDE.md](vault/CLAUDE.md); the answer shown below, in "The same question, two answers" |
| 5. One home for every kind of information | The table "Which information lives where" in [vault/CLAUDE.md](vault/CLAUDE.md) |
| 6. Dated decisions, with superseded ones marked | [decisions.md](vault/projects/calvesi-accounting/decisions.md): the struck-through decision of September 29 |
| 7. Rules per tool | [vault/agent/knowledge/tools/](vault/agent/knowledge/tools/automated-email.md) |
| 8. Profiles per client and per person | [vault/agent/knowledge/people/](vault/agent/knowledge/people/tiziano-olivari.md) |
| 9. Corrections saved once | [vault/memory/MEMORY.md](vault/memory/MEMORY.md) and the detail files beside it |
| 10. Project index and ordered archive | [calvesi-accounting.md](vault/projects/calvesi-accounting/calvesi-accounting.md): every file of the project, grouped by type |
| 11. Periodic maintenance | The health check in [memory-architecture.md](vault/reference/memory-architecture.md) and the skill listed in [skills/README.md](vault/skills/README.md) |
| 12. Owner profile and agent identity, always loaded | [OWNER.md](vault/agent/OWNER.md), [OWNER-details.md](vault/agent/OWNER-details.md), [IDENTITY.md](vault/agent/IDENTITY.md) |
| 13. Reusable patterns | [vault/agent/knowledge/patterns/](vault/agent/knowledge/patterns/levels-of-evidence.md) |
| 14. Tiered loading | [memory-architecture.md](vault/reference/memory-architecture.md), and the "Read when" table in [vault/CLAUDE.md](vault/CLAUDE.md) |
| 15. A written plan for multi-step work | [plan-payment-reminders.md](vault/projects/calvesi-accounting/reports/plan-payment-reminders.md) |
| 16. A voice system | [STYLE.md](vault/agent/STYLE.md) and [vault/agent/knowledge/voice/](vault/agent/knowledge/voice/voice-protocol.md) |
| 17. Day opening and weekly close | [Home.md](vault/Home.md) and [skills/README.md](vault/skills/README.md); the carry-over from week to week is visible in the three "Current state" sections |
| 18. Calls archived and checked against recorded decisions | [The call](vault/projects/calvesi-accounting/calls/2026-10-14-call-calvesi.md) and [its analysis](vault/projects/calvesi-accounting/calls/2026-10-14-call-calvesi-analysis.md) |

## What to look at in the project, and why

**1. The current state that changes.** Open the three files in `vault/projects/calvesi-accounting/log/`, from oldest to newest, and read only the first section of each.

- In week 40 we are waiting for the reminder texts.
- In week 41 that thread is gone, because the texts arrived. A new one was born: the client list for the trial.
- In week 42 one line is left marked "not rechecked": who signs the emails. Nobody closed it, so it wasn't removed. Two lines are new: the call of October 14 with a proposal waiting for confirmation, and a pointer to the plan with its open steps.

Each state takes a few lines and has a date. Someone who opens the project a month later reads only the last one.

**2. The history under the state.** In the week 41 file look at the days: the most recent is on top. The entries are short and say what changed, they don't tell the story of the day.

**3. The superseded decision.** Open [decisions.md](vault/projects/calvesi-accounting/decisions.md). On September 29 it was decided to send the reminders on WhatsApp. On October 8 the firm changed its mind. The old decision is still there, struck through, with a pointer to the new one and the reason. If in six months someone suggests WhatsApp, you already know why it was dropped.

**4. What is not in the decisions file.** No next steps, no "waiting for". That lives in the log. And not even the contradiction found in the call of October 14: the decisions file changes only after the owner confirms, so for now it still says two reminders. The call analysis says so, and the state of week 42 points to it.

**5. The people and the tools.** Profiles and tool files sit outside the project, in `vault/agent/knowledge/`, because they apply to other jobs too. Note that the profile of a person doesn't say where the project stands.

## The same question, two answers

Imagine opening a new session on November 2, after two weeks without touching the project, and writing: "let's pick up Calvesi Accounting".

**Without a current state.** The agent lists the folder, opens the index, the call notes, a few produced files. It finds "reminders via WhatsApp" written in the first call's notes and starts from there. You notice, you correct it, and you explain again that we moved to email, that the trial has already been done, that the owner's go-ahead is missing.

**With a current state.** The agent opens `log/2026-W42.md`, reads the first lines and answers:

> We are on hold, waiting for Ottavio Calvesi's go-ahead to extend the reminders to all clients. The trial on twenty clients is closed: twelve paid within two days of the reminder. Two things are open: who signs the emails, marked as not rechecked, and the proposal from the call of October 14, which found that Ottavio now wants a third reminder, against the decision of October 6. It is not confirmed, so the decisions file still says two reminders. The plan has open steps 9 to 12. Source: current state of week 42, updated October 15. I see no later entries: if the October 20 call has happened in the meantime, it wasn't recorded.

The last sentence is the part that counts: the agent doesn't pretend to know what the log doesn't say.

## What this example is not

- It is not a template to paste. Read it to see the mechanism, then build the same function in the person's own system.
- The content is invented: the owner, the firm, the people, the numbers, the incidents. Only the structure and the twenty rules in [rules-and-why.md](rules-and-why.md) are real.
- The person's own system keeps its names and conventions. If it already does what a file here does, in another shape, nothing needs to change.
