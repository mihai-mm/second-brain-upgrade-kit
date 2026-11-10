# Calvesi Accounting - project rules

Example file. In Claude Code this file would be called `CLAUDE.md` and would sit in the project folder.

## What it is

Calvesi Accounting is an accounting firm with eight people. The project builds the automatic reminders for the firm's clients' overdue invoices: today one person in administration sends them by hand, when they remember.

The project ends when the reminders go out on their own for all clients and the firm knows how to stop or change them.

## Where things are

- Where we stand: current state at the top of the most recent file in `log/`. It is the only source for the state.
- Decisions, things learned, numbers: `decisions.md`.
- The plan of the main job: `reports/plan-payment-reminders.md`.
- All the project's files: `calvesi-accounting.md`.
- The firm's people: profiles in `../../agent/knowledge/people/`, outside the project.
- What was learned with each tool: files in `../../agent/knowledge/tools/`, outside the project.

## Rules

- No message goes out to the firm's clients without Ottavio Calvesi's written yes.
- Trials run on lists chosen by the firm, never on all clients.
- The names of the firm's clients don't leave this folder.
- Before writing to Tiziano Olivari, read [his profile](../../agent/knowledge/people/tiziano-olivari.md).
- Before building or changing an email send, read [the automated email file](../../agent/knowledge/tools/automated-email.md).
- Whoever creates a file adds the line in `calvesi-accounting.md`.
