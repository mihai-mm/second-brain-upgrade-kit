# Levels of evidence - mark where each claim comes from

Example file, all content invented. Pattern born in August 2026, checking a third-party guide against Livia's own website. Half of its advice was already in place on the site, one point was plain wrong, and two claims had been written by the agent, presenting as official documentation things that came from third-party analyses. No single claim was the problem: they all sat at the same level, and nobody could tell them apart.

## The pattern

In any document that states facts (a reference note, an audit, a report for a client, a technical analysis), every claim carries where it comes from:

| Marker | Means |
|---|---|
| **[stated]** | It is in the official documentation of whoever controls the thing |
| **[observed]** | We checked it ourselves, with a command, a test or a direct look at real files, but it is not documented |
| **[industry]** | Analysis by others, plausible, not confirmed by the source |

The names can change with the audience. In a report for a client: "stated by the supplier / checked by us / common practice". The three categories stay separate and visible.

## Why it works

When the three levels sit side by side with the same look, opinions are sold at the price of facts. The reader cannot tell what a decision can be built on and what must be checked first. That is how a plausible mistake survives: it does not look like a mistake, it looks like a well-written recommendation.

Applying it costs one marker per claim. The reader knows how far to trust it. The writer is forced to stop at each line and ask where it came from. That is where unchecked claims are caught, not in the final reread.

## Rules of use

- Put the marker while writing, not afterwards. Adding it to a finished text is a reconstruction job that almost always gets skipped.
- **Observed** is a legitimate level, not a fallback. A direct check on real files is worth more than the absence of documentation.
- If a claim fits none of the three levels, do not write it. "Cannot be verified" is useful information, not a gap to fill.
- Say at the end what the document does not cover. A closing section with what is out of scope stops the document from passing as complete. Experienced readers read it first.
- When the document is for a client, check twice that nothing marked [industry] is worded as a fact.

## Where it has been applied

- August 2026, check of a third-party guide against her own website: first use, table of the three markers at the top of the note.
- October 2026, a count taken from a client's export is marked [observed], with the file and the date of the export, and kept apart from the client's own estimate.

## Connected to

- [Discovery with open questions](discovery-open-questions.md) - answers from a client are facts about what the client said, not about the world: mark them as such.
- [Spreadsheet exports](../tools/spreadsheet-exports.md) - the counts that become [observed].
