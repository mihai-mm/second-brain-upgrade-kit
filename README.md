# Upgrade your second brain

Hi, I'm Mihai Moraru.

If you're reading this, you already have a second brain that works with an AI agent: a vault, a set of folders, a knowledge base your agent searches. This folder doesn't ask you to change it. It's here to find out whether your system is missing something mine has, what that gap costs you today and, if you want, to add it.

## How to use it

Clone this repository, or download it as a ZIP from the green Code button. Then open the folder with your agent (Claude Code, or any other agent that can read files on your computer) and tell it:

> Read the CLAUDE.md file in this folder and follow it.

It takes it from there, in three stages.

1. **Analysis.** It asks you five questions, then reads your system without changing anything and shows you a map of what it understood. You correct it.

2. **Report.** For each of the eighteen things my system does, it tells you whether yours already does it (even in a different form), does it halfway, or doesn't, with the file that proves it. Then it proposes at most three additions, in order.

3. **Installation.** If a proposal convinces you, it installs it on one project only, shows you it works and leaves you the list of files it created, so you can roll back.

You can stop after the report. That alone tells you something about your system.

## What it won't do

- During the analysis it doesn't edit, move or delete any of your files.
- It doesn't write anything without telling you first what and where.
- It doesn't replace what works. If you already have something in a different form, it says so and moves on.

## The eighteen things it checks

1. A work log for each project
2. The current state at the top of the log, carried over every week
3. A session close that sends each piece of information to the right place
4. Resuming a project with source and date
5. One home for every kind of information
6. Dated decisions, with superseded ones marked
7. Rules per tool, with the mistakes not to repeat
8. Profiles per client and per person
9. Corrections saved once
10. A project index and an ordered archive of calls, materials and deliverables
11. Periodic maintenance
12. A profile of you and an identity for the agent, loaded every session
13. Reusable patterns, kept apart from tools and projects
14. Tiered loading: a light always-on layer, everything else on demand
15. A written plan for multi-step work, with evidence for every closed step
16. A voice system for anything written in your name
17. A day opening and a weekly close
18. Calls filed and checked against the decisions already recorded

The pair that makes the biggest difference for me is 1 and 2. When I open a session on a project I haven't touched in three weeks, my agent reads a few lines and knows where we are, what we're waiting for and from whom.

## How it measures impact

I won't promise you hours saved. If you use Claude Code, your past sessions are stored on your computer. With your permission, your agent rereads the start of them and counts four things: how often you had to re-explain where you were, how much work the agent does before the first result, how many corrections you repeated, how often the agent used outdated information. The report gives you the numbers and a few examples from your own sessions.

The script that extracts those messages runs on your computer and saves nothing. The excerpts are read by your agent, like any other file you let it read.

If the sessions aren't there, or you don't want them read, the agent asks you five questions instead.

## What's in the folder

- `README.md`: this page.
- `CLAUDE.md`: the instructions for your agent. `AGENTS.md` points there for agents that look for that name.
- `progress.md`: where the agent notes how far you've got. If you close and reopen, it picks up from there.
- `INDEX.md`: every file in the folder and when your agent should open it.
- `1-analysis/`: how to explore your system, the eighteen capability cards, how to measure impact, the report template.
- `2-modules/`: fifteen modules, one per addition, with file templates and skills ready to adapt.
- `3-example/`: a complete made-up vault, built the way mine is: main rules, the owner's profile, the agent's identity, patterns, a voice system, the memory index, and a project with three weeks of log, a plan and a call. Plus twenty of my rules, each with the reason and the incident behind it.
- `report/`: created during the analysis. It holds the map of your system and the report.

## Limits I know about

- The system has been tested on one person only: me. If your second brain belongs to a whole company, the part about who writes a project's state is untested, and the agent will tell you so.
- It was born with Claude Code and plain text files. It works elsewhere too, but file names and the way skills get installed change.
- The log doesn't write itself. The agent writes it when you close the session with a command. I added a check that stops me if I'm about to close without doing it, but that's a piece of my own setup and you won't find it here.

Mihai
