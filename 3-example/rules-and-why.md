# Twenty rules, and the incident behind each one

These are real rules from my system. I removed the names of clients and projects; the dates and the numbers are real. "My agent" is Claude Code working in my vault.

I'm including them for one reason: a rule with no story looks like a preference. Every rule here exists because something went wrong first, and the fix was written down the same day.

**For the agent reading this.** Don't install these rules in the person's system. They are examples of the form a saved rule should have: the rule, what happened, why it holds, and where it lives. The person's rules come from their own corrections (module 06). Use this file when they ask why a rule exists, or when you need an example of how to write one.

Each rule ends with **Home**: the kind of place it lives in, following the routing in `vault/reference/memory-architecture.md`.

---

## Where information lives

### 1. The current state says where we are. It doesn't tell the story.

**What happened.** October 2026. On my busiest project every session added a block to the "current state" section instead of rewriting it. It reached 24.8 KB. Neither I nor the agent could tell where the project stood without reading all of it, which is exactly what the section was supposed to prevent.

**Why it holds.** A state that accumulates is a second log. The state is rewritten at every close: threads that closed leave it, their detail stays in the dated entries. Past about 5 KB the agent flags it.

**Home.** Main instructions of the vault, and the close command.

### 2. A correction is saved the moment it is given.

**What happened.** September 2026. After a misunderstanding about the visual style of some promo videos I told the agent: "every time we exchange feedback, remember to save it, so you don't make the same mistakes and we improve the system as we go."

**Why it holds.** By the end of a session half of the corrections are forgotten, or have turned into something vague. Saved on the spot, with the reason and the case, a correction is paid for once.

**Home.** Always-loaded index of corrections, one line; the case in a file of its own.

### 3. A rule that must fire on a phrase needs its own line in the always-loaded index.

**What happened.** October 22, 2026. I said "log this" and the agent wrote the log by hand instead of running the close command. The guard that checks for unlogged changes didn't recognize it and blocked the next step. Two days later it happened again: the rule had been saved, but only inside a grouped sub-index that is opened on demand. It never fired.

**Why it holds.** What is on demand gets read when the agent already suspects it is relevant. A rule tied to a trigger phrase has to be in front of the agent before the phrase arrives.

**Home.** Always-loaded index. This is the difference between the first and the third tier.

### 4. What loads at the start of a session is measured, with thresholds.

**What happened.** October 10, 2026. I measured what my agent loaded before I typed a word: 65,485 tokens. Rules had been added one incident at a time for months and nobody had looked at the total.

**Why it holds.** Every line loaded at the start takes attention from the others, and the agent's memory index is cut from the bottom past a certain size. Since that day a read-only check runs monthly: weight of the session start, size of each always-loaded file, length of the states. It changes nothing by itself; it writes a report.

**Home.** Maintenance procedure, with the thresholds in the memory architecture reference.

---

## Before acting

### 5. Read a file before writing to it.

**What happened.** May 31, 2026. Updating some strategy files, the agent overwrote one with a short version, assuming it was nearly empty. It held the whole roadmap. In the same pass it launched edits on another file by guessing its content; that file didn't exist.

**Why it holds.** One root cause for both: writing without looking at the target first. The cost of looking is one read.

**Home.** Always-loaded index of corrections.

### 6. No schema migrations from an agent on the real database.

**What happened.** July 19, 2026. While adding one column to a table of my task app, the production table went from 47 tasks to 0. I recovered 37 from a backup made a few hours earlier and recreated 16 by hand. One task created after the last export was lost.

**Why it holds.** Some operations are not worth the convenience. Schema changes are prepared and tried on a copy; on the real database they run only after I say so, and the migration script is blocked by permissions.

**Home.** Always-loaded index, plus a permission that enforces it. A rule this costly gets a mechanism, not just a sentence.

### 7. In a patch script, every replacement asserts that it matched.

**What happened.** August 31, 2026. Two text replacements in a script failed silently. One was aimed at the wrong file. The result was a published page on which no card was drawn anymore. The script's output said nothing; I found out by opening the page.

**Why it holds.** A replacement that matches nothing is not an error for the tool. It has to be made one.

**Home.** Always-loaded index of corrections.

### 8. Recompute the date before writing "today" or "tomorrow".

**What happened.** September 29, 2026. In two messages prepared for me to send, the agent wrote "tonight" for an event happening the day after and "tomorrow" for one two days away. It had copied the words from earlier reports without recomputing. My answer: "it's not the first time."

**Why it holds.** Relative dates are true only on the day they were written. In anything that leaves the system, the agent checks today's date and writes the reference again.

**Home.** Always-loaded index of corrections.

### 9. Fix the cause. Show me the patch and the cause as two separate things.

**What happened.** April 29, 2026. A workflow kept failing when saving text to a database, because of malformed characters. The quick fix was to clean the text right before saving. The cause was upstream: a block of style code that an earlier step was not removing.

**Why it holds.** Patches downstream pile up and hide the bug upstream, and the data stays dirty after the symptom is gone. The agent names both, and I choose.

**Home.** Always-loaded index of corrections.

### 10. Before anything goes public, four searches over every file.

**What happened.** May 10, 2026. I found five leftovers in the first public package of a course bonus, after the agent considered it clean: placeholder names that belonged to real people, a reference to a folder readers couldn't reach, a mention of a command that no longer existed, a system file.

**Why it holds.** Checking each edit as you make it is not enough after many small fixes. Before release the agent searches all files, not only the ones just touched, for four things: real names, outdated references, system noise, references to things the reader cannot reach.

**Home.** Always-loaded index. This folder went through the same four searches.

---

## Working with me

### 11. A question I didn't answer is not a yes.

**What happened.** May 19, 2026. After analyzing a call, the agent asked me four questions with the options already ticked. I answered one, with my own instruction. It treated the other three as confirmed and created follow-up tasks, a new file and two memory entries. I stopped it: "the things I didn't select, I didn't select because I didn't want them." Everything had to be rolled back.

**Why it holds.** Silence is a refusal. Options are never pre-selected, and what is not answered is not done.

**Home.** Always-loaded index of corrections.

### 12. Don't bring back a risk I already accepted.

**What happened.** September 23, 2026. A sales page promised a limited number of seats and the checkout had no cap. The agent flagged it several times. I wrote: "I know, I told you it doesn't matter and we'll see if the problem ever comes up. Don't ask me again."

**Why it holds.** Flagging a risk once is the agent's job. Repeating it after a decision turns the agent into noise. It comes back only if new facts arrive.

**Home.** Always-loaded index of corrections.

### 13. Flag a future scenario. Don't decide it.

**What happened.** September 28, 2026. I had decided to close enrollments by hand. The agent was already changing the page for the case in which the closing date passed with enrollments still open. I told it we would decide only if that case came up.

**Why it holds.** A scenario that hasn't happened gets one line: what its effects would be and by when a decision would be useful. The solution is built if the case arrives.

**Home.** Always-loaded index of corrections.

### 14. Don't invent the goal of the work.

**What happened.** September 3, 2026. I asked for an informative post on how AI works. The agent gave itself a different goal, making me look original, and measured everything against it. Two rewrites were thrown away, and I wrote: "I don't understand why you keep going off track."

**Why it holds.** An invented goal is invisible while you work. It looks like ambition, and it makes you discard exactly the parts that answered the real request. If the goal doesn't come from a sentence of mine, the agent asks.

**Home.** Always-loaded index of corrections.

### 15. Tell me what you added beyond what I asked.

**What happened.** May 4, 2026. I asked for the skeleton of a document. I received a draft with framing paragraphs already written, a legal reference and three specific examples. The content was fine. I said: "next time I want you to tell me when you add things without telling me."

**Why it holds.** The problem is not the quality of the addition, it is finding it later in places I didn't expect. Extras are fine when they are declared.

**Home.** Always-loaded index of corrections.

### 16. Propose changes as before and after.

**What happened.** September 1, 2026. The agent proposed five changes to a text in discursive form: the reasoning, a partial quote, the new sentence somewhere inside a paragraph. I answered: "write the changes you want to make simply and clearly, because I didn't understand them." Rewritten as before and after, I decided all five in one pass.

**Why it holds.** An argued proposal makes me rebuild the final text in my head. A replacement can be read and answered with yes or no.

**Home.** Always-loaded index of corrections.

### 17. A correction applies everywhere.

**What happened.** November 8, 2026. On my website I removed one claim from the About page. The same sentence was still on the home page, in the FAQ and on the results page, and I had to ask: "do you see anything else that can be corrected?" In the same pass the agent changed a title to the third person and left the lines under it in the first.

**Why it holds.** When I correct one instance, I'm correcting the pattern. The agent extends it to the other pages in the same pass and tells me where.

**Home.** Always-loaded index of corrections.

### 18. After two or three blind checks, ask for my eyes.

**What happened.** May 15, 2026. A local app wasn't responding. The agent iterated for more than thirty minutes with checks I couldn't see, while I waited. I wrote: "I'm getting fed up, too many things aren't working and you're not telling me." My browser would have shown the truth in ten seconds.

**Why it holds.** I'm part of the feedback loop. When the checks available to the agent stop converging, the fastest instrument is the person in front of the screen.

**Home.** Always-loaded index of corrections.

### 19. The plan of a long job is written before the first step.

**What happened.** October 9, 2026. In the middle of a job with a dozen steps I had to ask: "are you tracking all of this in a to-do?" The rule existed in memory. It hadn't fired.

**Why it holds.** A plan kept in the chat disappears with the session. The plan is a file in the project: the request in my words, numbered steps, evidence next to each closed step. Since that day it is a skill that triggers itself when a job has four or more steps.

**Home.** A skill, plus one line in the always-loaded index. A rule that kept failing as a sentence was promoted to a procedure.

### 20. Every factual claim carries where it comes from.

**What happened.** August 18, 2026. Checking a third-party guide against my own website, I found that half of its advice was already in place, one point was wrong, and two claims had been produced by my agent, presenting as official documentation things that came from third-party analyses. No single claim was the problem. All of them sat at the same level.

**Why it holds.** When "stated by the source", "verified by us" and "said by others in the field" look the same, opinions get sold at the price of facts. The mark is added while writing, and a claim that fits none of the three levels is not written.

**Home.** A pattern file: `vault/agent/knowledge/patterns/levels-of-evidence.md`.
