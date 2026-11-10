# Voice protocol

Example file, all content invented. The entry point for anything that goes out under Livia's name: an email, a post, a message, a document signed by her. Use it every time, even outside a skill.

The goal is to reproduce how Livia says a thing to a particular person, not to add polish, persuasion or "good writing" on your own.

## The seven steps, in this order

1. **Identify the kind of text and the recipient.** Who is she writing to, and what is their relationship? Is it an update, a reply, a request, a post? What must the text do: inform, ask, reassure, invite?
2. **Read the style file.** [STYLE.md](../../STYLE.md). If the recipient is a person with a profile, read the profile in `agent/knowledge/people/` too.
3. **Pick two or three real samples of the same kind.** From [samples/](samples/client-update-email.md). A sample fits when it shares first the relationship and the kind of text, then the intention. If there is no exact match, combine one sample with the same recipient and one with the same kind, and say what is missing.
4. **Draft.** First write in a few lines what the text must do (the movements: what she is answering, which fact makes it concrete, what she asks or concludes). Then write it. When Livia asks for a full draft, give a full draft.
5. **Pass against generic machine-sounding phrasing.** Reread next to the sample: opening pleasantries, praise of the question, hype words, a list of three adjectives, a closing that summarizes the text, isolated one-line sentences. Remove what the samples would not contain. Check that no experience, number, date or promise was invented. Recompute every "today", "tomorrow", day of the week from today's date.
6. **Sentences Livia wrote or approved herself are protected.** Do not rewrite them. Add only the missing facts. In a mixed draft, mark each passage: hers, approved by her, generated, unsure. The samples show a voice, they do not authorize reusing their facts.
7. **Every correction she makes to a draft is recorded in the [learning log](learning-log.md).** Keep the before and the after. Note the kind of text, the recipient, the reason if she gave one. A correction is local until she says it is general, or until it comes back in two independent contexts. Only then does it move to the style file, and only with her direct confirmation.

## Routing

| Kind of text | Samples | Extra checks |
|---|---|---|
| Update to a client owner | [client-update-email.md](samples/client-update-email.md) | Result in the first line. No promise of a date she has not given. Read the client profile |
| Short reply to a contact | [short-reply.md](samples/short-reply.md) | The request in the first line, the date needed by. Three lines or fewer |
| Post for her followers | [linkedin-post.md](samples/linkedin-post.md) | No client names, no numbers that identify a client. No promise words. One invitation at most |
| Message to a client's customers | None: not written by the agent without the client's written approval | Stop and ask. See the rules of the project |
| Document for a client | [client-update-email.md](samples/client-update-email.md) for tone | Mark where each claim comes from: [levels of evidence](../patterns/levels-of-evidence.md) |

## Maintenance

After any change to the style file, the protocol or the samples: look for the places that call the changed rule and update only the prescriptive ones, run the cases in the learning log again on one sample, and record the tests not run. The final judgment on whether a text sounds like her is Livia's.
