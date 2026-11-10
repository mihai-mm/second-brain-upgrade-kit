# Module 11 - Tiered memory

Installs capability 14. It needs one home per kind of information (module 04). It makes sense once the always-loaded layer has started to grow, or when the person notices that a rule "should always hold" and sometimes doesn't.

## What it's for

Every piece of information gets loaded at the right moment: always, only when working on a project, or only when asked for. The always-loaded layer stays light enough to be read in full, and nothing that must always hold depends on a search happening to find it.

## Why it works

- **What is always loaded competes for attention.** Past a certain weight the agent starts ignoring part of it.
- **What is only searched can be missed.** A rule that must always hold, if it lives only on demand, is applied when a search happens to surface it.
- **One tier per piece of information.** A fact in two tiers is two facts to keep aligned, and one of them will drift.
- **The number of index entries is what grows.** Shortening lines buys time. Reducing how many entries there are is what stops the index from filling up again.

## The three tiers

| Tier | Loaded | What goes in |
|---|---|---|
| Always | At every session | Main instructions, owner profile, agent identity, the short index of corrections with pointers |
| Per project | When working on that project | The project's rules, current state (top of the latest work log), decisions file |
| On demand | Only when the task calls for it | Patterns, tool files, people profiles, consolidated clusters of notes, long detail, history |

## Essential

1. The three tiers, each with one clear rule for what belongs in it.
2. Routing questions that say where a new piece of information goes (`templates/routing-questions.md`).
3. Six forbidden things:
   - the same information in two tiers;
   - index entries that swallow the case study (the index line says when the rule applies, the case lives in its own file);
   - conventions of the knowledge system duplicated in the agent's memory (the main instructions already load them);
   - current state in any memory tier (state lives in the work log, at the top);
   - a method that works across projects buried in one project's decisions;
   - a client profile in the always-loaded tier.
4. Index entries of one line, under about 200 characters, in the form "title - when it applies". Detail goes in a topic file.
5. **Consolidation with a stub pointer.** When a cluster of notes on one theme has matured (for example ten technical notes on the same tool), merge them into one reasoned on-demand file. Leave in the index one line, the stub pointer, that names the themes covered and points to that file. Recall still triggers on the theme, and the agent reaches the detail in two steps. This is the only lever that reduces the number of index entries, not only their length. Corrections about behavior usually stay in the index: they often trigger on a single word from the person, and would lose the trigger.
6. Measure what loads at session start: which files, how big, how many lines. Ask the agent to report it in a fresh session.

## A factual note, to verify

As of October 2026, Claude Code loads the first 200 lines or 25 KB of its memory index; check the documentation of the version in use. Anything past that limit is not read, so the index needs a margin below it. Other agents differ: ask or check, don't assume.

## Adaptable

- Where each tier lives and what it is called.
- The thresholds, which depend on the agent and the model (see module 08).
- The mechanism: the agent's own memory, a rules file called from the main instructions, an always-loaded file.
- For a retrieval knowledge base: it already does the "on demand" tier. What it usually lacks is a small guaranteed always-on layer, a short set of rules and pointers that is read at every session whether or not a search finds it. Adding that layer is the installation. Do not move the knowledge base's content into it.

## How to install it

1. List what loads at session start in the person's system, with the size of each file. If the agent can't measure it, say so and give the sizes of the files.
2. Compare with the three tiers. Show the person what sits in the wrong tier: state in a memory file, a client profile always loaded, the same fact twice.
3. Propose the moves, at most a few at a time. For each one say the file, the line, and where it goes. Do not delete: add the new copy, check it, then agree with the person on removing the old one.
4. Write the routing questions in the person's own place (the main instructions, or a short reference), based on `templates/routing-questions.md`, adapted to their folders.
5. If the index has lines over about 200 characters, propose shorter lines and move the detail to the topic file. Use `templates/memory-index.md` as the model.
6. If there is a cluster of notes on one theme, propose the consolidation with a stub pointer. Write the consolidated file first, then show the stub line.
7. Note in `progress.md` what was created, what was moved, and the sizes before and after.

Do one move, check it, then the next.

## Check

Two tests, in a fresh session.

1. Ask the agent what it loaded at the start and how heavy it was. The answer matches what you measured.
2. Ask something whose answer lives in the on-demand tier. The agent reaches the right file through the pointer, without searching everything, and says which file it opened.

If test 2 fails, the pointer line is too vague: rewrite it so that it names the themes and says when to open the file.

## To roll back

Restore the moved lines to where they were (you noted them in `progress.md`) and remove the stub pointers and routing text you added. Consolidated files can stay: they only add a place to read.
