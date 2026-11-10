# Module 04 - One home for every kind of information

Installs capabilities 5 and 6.

## What it's for

When a piece of information changes, there is only one place to update. When the agent looks for it, there is only one place to look. Decisions that have changed stay readable, but it is clear which one holds.

## Why it works

- **The problem with second brains is contradiction, more than quantity.** The same price written in three files, only one updated. For the agent that is three texts with the same authority.
- **Giving more weight to recent records helps but doesn't settle it.** A retrieval knowledge base that favors new records makes the right answer more likely. With one home, the right answer is the only one that exists.
- **Different kinds of information age differently.** The state changes every week, a decision every few months, a person's profile almost never. Keeping them in the same file means the slow part gets buried by the fast part.
- **A superseded decision is information.** Knowing that a path was tried and abandoned, and why, keeps it from being proposed again.

## Essential

1. A written table, in the instructions the agent always reads, saying where each kind of information lives.
2. One place for each kind. Elsewhere you put a pointer, not a copy.
3. The state of the work and the next steps live only in the log. Never in the decisions file, never in a person's profile.
4. Every decision has a date and a reason.
5. A replaced decision is marked as superseded and points to the new one. It is not deleted.
6. When the agent doesn't know where to put something, it uses the questions below. If the doubt remains, it asks.

## The questions for choosing the home

1. Does it concern one project or client only, or does it hold for all of them?
2. If it concerns one project only: is it today's state (log), a decision or a number that stays (decisions file), or a durable fact about the client as a person or company (profile)?
3. If it holds for all: is it a correction about how the agent should work (corrections), or something verified about a tool (tool file)?
4. Is it a rule that is only needed inside a skill? Then it lives in the skill.

## Adaptable

- Which homes there are and what they are called. Use the places the person already has: the goal is to name the roles, not to create files.
- The sections of the decisions file. The template proposes three: decisions, things learned, numbers.
- How a superseded decision is marked.
- In a retrieval knowledge base you can't impose a single home on the raw records. You can, though, set that for facts that change (prices, deadlines, decisions) there is a reference file, and that file wins over what the search returns.

## How to install it

1. From the system map, work out where the person keeps each kind of information today. Write the draft of the table starting from `templates/homes-table.md` and filling it in with their real places.
2. Mark in the draft the conflicts you found during the analysis: the same kind of information in two places. For each one, ask the person which place should hold. Don't move anything: from here on, writing goes in the chosen one.
3. Show the table and the spot in the instructions where you would put it. Add it after the yes.
4. If the trial project has no decisions file, propose creating it from `templates/decisions.md`. Fill it only with decisions you find written somewhere, saying where you took them from. Don't reconstruct any from memory.
5. Note everything in `progress.md`.

## Check

1. In a fresh session, ask the agent three questions of the type "where would you write that...": a progress update, a decision, a client's preference. It must give a single destination for each, citing the table.
2. Change a decision in the trial project: in the file the old one must show as superseded with a pointer to the new one, and to the question "what did we decide about this?" the agent must answer only with the one that holds.

## To roll back

Remove the table from the instructions and, if it was created, the decisions file.
