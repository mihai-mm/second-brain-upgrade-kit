# Module 13 - Voice system

Installs capability 16. It works better after corrections (module 06) and tiered memory (module 11), because the pointer lives in the always-loaded layer. It can be installed without them.

## What it's for

When the agent writes something that goes out under the person's name, the draft should sound like them on the first pass. Today the person usually rewrites generic drafts, and the same corrections come back every time.

## Why it works

- **Real samples beat descriptions.** "Direct and warm" can describe a thousand people. Two or three texts the person actually wrote show how they open, how they connect sentences, how long a paragraph runs. The agent imitates what it can see.
- **One entry point.** A single file says what to do before writing. Without it the agent picks whatever it finds first, or nothing.
- **Samples are matched by kind and recipient.** A note to a client and a public post are written differently by the same person. A sample of the wrong kind teaches the wrong habits.
- **The person's own sentences are protected.** A sentence they wrote or approved is evidence of the voice. Rewriting it to be "better" erases the evidence.
- **Corrections become cases.** Each change the person makes to a draft is recorded with the text before and after. Patterns emerge from cases, not from the agent's guess about what the person prefers today.
- **A rule learned once is not a permanent rule.** One correction may reflect the recipient, the mood or the occasion. It stays local until it repeats in independent contexts or the person declares it general.
- **Voice and effectiveness are two questions.** "Does it sound like them" and "will it work" are judged separately. The agent does not add a stronger hook, a call to action or a tidier structure unless asked.

## Essential

1. One entry point (`templates/voice-protocol.md`) that sends the agent through seven steps, in this order:
   1. Identify the kind of text and the recipient.
   2. Read the style file.
   3. Pick two or three real samples of the same kind.
   4. Draft.
   5. Run a pass against generic, machine-sounding phrasing.
   6. Leave untouched the sentences the person wrote or approved.
   7. Record every correction the person makes to the draft as a case in the learning log.
2. A style file of one page (`templates/style-file.md`). It changes only with the person's direct confirmation.
3. A folder of real samples, labelled by kind of text and recipient, with a note of who wrote each one (the person alone, or approved after edits).
4. A learning log (`templates/voice-learning-log.md`) with one entry per correction, each with a scope: this text only, this kind of text, or always.
5. One pointer in the always-loaded layer: before writing anything that goes out under the person's name, open the entry point.
6. The agent says which samples it used.
7. Never invent facts, experiences, results or promises to make a draft sound more personal. A missing detail becomes a placeholder or a question.

## Adaptable

- The kinds of text and how many sample groups: three or four kinds are enough to start.
- A lighter path for private messages and operational emails: steps 1, 2, 4 and 6 may be enough, with one sample instead of three. Public posts and anything with many readers get the full path. Write the choice into the routing table.
- Where the files live and what they are called. If the person already has a style guide or a folder of past posts, those are the style file and the samples: add the missing parts only (routing, protection, log).
- For a retrieval knowledge base: samples can be records marked by kind of text, as long as the agent is told to filter on that mark.

## How to install it

1. Ask the person which kinds of text they write most often under their name and who reads them. Pick at most four.
2. Ask them for texts they wrote themselves and are happy with, for each kind. Check any existing guide or folder first. Do not take samples from past sessions without permission.
3. **Write the style file only from those texts and from what the person says.** Never from your own impression of them. Draft it, show it, and let them correct it line by line. It must stay on one page.
4. Propose where the samples go and how they are labelled. Show the folder and the first labels before creating anything.
5. Create the entry point from `templates/voice-protocol.md`, with a routing table filled in for the agreed kinds. Show it and wait for a yes.
6. Create the empty learning log from `templates/voice-learning-log.md`.
7. Add the pointer line to the always-loaded layer. Show the exact text and the spot.
8. Note in `progress.md` every file created and the line added.

Do one kind of text first, check it, then add the others.

## Check

Two tests, in fresh sessions.

1. Ask for a short text of a kind that has samples. The agent names the kind, the recipient and the samples it used, and leaves any sentence you supplied untouched. The person marks what they would change.
2. Check that each change landed in the learning log as a case with before, after and scope, and that the style file has not changed.

If test 1 fails because the agent skips the entry point, the pointer is too vague: say when to open it, not only that it exists.

## To roll back

Delete the files created (entry point, style file, learning log, sample folder if you created it) and remove the pointer line. Samples the person already had stay where they were.
