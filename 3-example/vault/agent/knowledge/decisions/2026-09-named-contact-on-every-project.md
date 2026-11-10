# 2026-09 - A named contact on every project

Example file, all content invented. A decision that holds across projects, so it lives here and not in one project's decisions file.

## Decision

From September 2026, Livia takes no project unless there is a named person on the client side who answers within two working days. The name is written in the project rules before the first step of work.

## Why

The Bellandi Dental project stalled for weeks because nobody on the practice side answered. Questions about the booking software went to the front desk, to the dentist and to a shared address, and each took them for someone else's. The work waiting for those answers could not start, and Livia had no one to call. The delay was not about the work: it was about nobody being responsible for replying.

A named person turns "someone will get back to us" into a date she can check.

## How the agent applies it

- When a new project is proposed, the first question is: who answers on their side, and does that person have the time? If the name is missing, say so before any file is created. See the admission rule in [CLAUDE.md](../../../CLAUDE.md).
- The name goes in the project rules. The profile of the person goes in `agent/knowledge/people/`.
- If the contact stops answering for more than two working days, the agent says so in the daily summary, with the date of the last answer. Livia decides what to do.
- A project that already exists is not stopped by this decision. It is applied when a project is opened or restarted.

## Exceptions

- A project for Livia's own use, with no client (her own website), has no contact to name.
- Livia may take a project with no named contact if she decides so in writing in the project rules, with the reason. The decision stays valid for all the others.

## Supersedes

Nothing. If it is changed one day, mark this file as superseded and name the one that replaces it.
