# Module 10 - Reusable patterns

Installs capability 13. It works better after corrections (module 06) and tiered memory (module 11), because patterns are often born there. It can be installed without them.

## What it's for

A method that worked on one project should be there, already written, when the next project needs it. Today it usually lives in the person's head, or inside the decisions of the project where it was born.

## Why it works

- **A pattern is not a tool rule and not a project decision.** "How to mark where each claim comes from" belongs to no tool and to no client. If it has no home of its own it ends up in one of those two places, and the next project never finds it.
- **Validated is a different thing from written down.** A note says "this might work". A pattern says "this held up here and here". Mixing the two is how a plausible idea gets treated as a proven method.
- **The why travels with it.** A pattern copied without its reason gets applied where it doesn't fit. The file states what problem it solved and what happened before it existed.
- **One pointer, no copies.** The always-loaded layer carries one line that says the pattern exists and when to open it. The text lives in one file. When the pattern improves, there is one place to change.
- **The project keeps the decision, not the method.** The project where the pattern was born keeps a dated line: "we decided to do it this way, see the pattern". The method itself moves out, so other projects can use it.

## Essential

1. One file per pattern, in one folder the agent can read on request.
2. Every file has: the pattern in a few lines, why it works, the rules of use, where it has been applied, what it connects to.
3. Only what held up on real work at least twice goes in. A first attempt stays in the project that tried it.
4. One line in the always-loaded layer points to the folder and lists the patterns by name, so the agent knows they exist without loading them.
5. The agent opens the pattern before starting a task that matches it, and says it did.
6. When several corrections on the same subject pile up, they are consolidated into one pattern file, and the always-loaded layer keeps a single pointer in their place.
7. A pattern that failed on real work is corrected with a dated note, not silently rewritten.

## Adaptable

- Where the folder lives and what it is called.
- The sections of the file, as long as "why" and "where applied" stay.
- How the pointer is written: a line in the main instructions, an entry in the agent's memory index, a record flagged as "method" in a retrieval knowledge base.
- For a retrieval knowledge base: patterns can stay inside it, as long as they carry a mark that separates them from ordinary notes and the agent is told to look for that mark first.

## How to install it

1. Ask the person for two or three methods they have explained to the agent more than once, or that they reuse across clients. If past sessions were read, start from the corrections that repeat (measure 3).
2. For each one, look for where it is written today: a project's decisions, a note, a skill, nowhere. Show the person what you found.
3. Agree on the folder and on the pointer. Follow the conventions of their system.
4. Write the first pattern together with the person, using `templates/pattern-file.md`. Use their words for the rule and ask them for the why: don't invent it.
5. In "where applied" list the real cases, with dates if they are known. If the person can name only one case, tell them it is still an attempt and ask whether they want it filed anyway, marked as such.
6. Add the pointer line. Show the exact text and where it goes before writing it.
7. If the method was written inside a project, leave that text where it is and add under it one line that points to the pattern. Don't delete anything.
8. Note in `progress.md` the files created and the line added.

Do one pattern, check it, then do the others.

## Check

Two tests, in fresh sessions.

1. In a project different from the one where the pattern was born, give a task that matches it, without naming the pattern. The agent opens the file before starting and says so.
2. Give a task that looks similar but that the pattern doesn't cover. The agent says the pattern doesn't apply and why, instead of forcing it.

If test 1 fails, the pointer is too vague: rewrite it so that it says when to open the file, not only that the file exists.

## To roll back

Delete the pattern files you created and remove the pointer line. The lines added inside projects can stay or go: they only point to a file.
