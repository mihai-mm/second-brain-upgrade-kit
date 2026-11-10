# Module 06 - Corrections saved once

Installs capability 9.

## What it's for

When the person corrects how the agent works, they shouldn't have to do it again the week after.

## Why it works

- **It is saved at the moment of the correction.** By the end of the session half of the corrections are already forgotten, or have turned into a vague "prefers short answers".
- **With the why.** A rule without a reason gets applied literally even where it doesn't fit. "No bullet lists" becomes a problem the day a list of steps is needed. "No bullet lists in messages to clients, because they look written by a machine" applies itself well.
- **With the when.** The scope says where the rule holds and where it doesn't.
- **Short index, detail kept apart.** What the agent reads at every session must stay light: one line per correction. The case that produced it lives in its own file, to open when needed.
- **Not everything is a rule.** "For this document use blue" is a choice made today. Saving it as a permanent preference pollutes the system.

## Essential

1. A place the agent reads at every session, with one line per correction.
2. Every correction has: the rule, the why, when it applies.
3. It is saved right away, and the agent says so in one line.
4. Before saving, check it isn't already there: if it is, update that one.
5. A local choice doesn't become a rule. When in doubt the agent asks: "does this always hold or only here?".
6. What holds only for one project goes in that project's instructions, not here.

## Adaptable

- The mechanism. In Claude Code it can be the agent's memory, if the person uses it, or a rules file called up from the main instructions. In other environments, an always-loaded file.
- The format of the detail.
- If the person already has an automatic memory full of entries, don't add another one: propose giving theirs the shape above, starting from the corrections that repeat the most.

## How to install it

1. From measure 3 take the groups of repeated corrections. They are the first candidates.
2. For each one write the draft: the rule in one line, the why, when it applies. Ask the person for the why if it doesn't come out of the sessions. Don't invent it.
3. Propose where to save them, based on what their environment offers. `templates/memory-index.md` shows the shape: a one-line index entry and one detail file with the rule, the why and when it applies.
4. Add to the main instructions a paragraph like this, adapted:

```
When I correct how you work, save the correction right away in [place]:
the rule in one line, the why, when it applies. Check first that it isn't
already there. If it's not clear whether it always holds or only in this
case, ask me.
Tell me in one line that you saved it.
```

5. Show everything, write after the yes, note it in `progress.md`.

## Check

1. Correct the agent on something small and concrete. It must save it and tell you.
2. In a fresh session, create the same situation: it must not repeat the mistake.
3. Give it an instruction clearly tied to the case ("in this file use the short title"): it must not save it as a permanent rule.

## To roll back

Remove the paragraph from the instructions and the entries added.
