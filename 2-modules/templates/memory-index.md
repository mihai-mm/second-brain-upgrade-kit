# Always-loaded index (model)

The index is read at every session, so each entry is one line, under about 200 characters, in the form: `- [Title](file.md) - when it applies`. The case that produced the entry lives in the detail file, never in the index. The examples below are invented.

```
- [Short answers in client messages](feedback_short_client_messages.md) - drafts to clients: three sentences, no lists
- [Ask before sending anything outside](feedback_ask_before_sending.md) - emails, posts, messages to third parties: draft only
- [Dates written in full](feedback_full_dates.md) - logs and decisions: 2026-03-14, never "yesterday"
- [Spreadsheet formulas: check the locale](feedback_sheet_locale.md) - separators and function names differ by locale
- [Photo tool: sizes and limits](reference_photo_tool_limits.md) - before exporting images for the web
- [Standing weekly call, Tuesday](reference_weekly_call_tuesday.md) - when proposing meeting times, avoid Tuesday morning
- [Image generation notes -> on-demand file](reference_image_generation_in_notes.md) - prompts, sizes, failures: read the consolidated file
- [Reports go to a file, not the chat](feedback_reports_in_files.md) - finished analyses: path and a short summary in chat
```

The seventh line is a stub pointer: ten notes on one theme were merged into one on-demand file, and the index keeps this single line.

## Model of one detail file

```
name: Short answers in client messages
description: Drafts to clients are three sentences, no lists
type: feedback

Rule: messages to clients are at most three sentences and use no bullet lists.

Why: the person said lists look written by a machine and clients answer
less. Said on 2026-02-10 after a draft with five bullets.

How to apply: every message written to a client, in any project. Does not
apply to internal notes or to step-by-step instructions, where a numbered
list is fine. If it is unclear whether a case counts, ask once.
```

<!--
Notes for the agent, to remove once the file is filled in:
- Fields of a detail file: name, description, type (feedback, reference or pointer), the rule, "Why:", "How to apply:". The why and the scope are what let the rule fit the next case.
- Check an entry doesn't exist before adding it. If it does, update that one.
- Count lines and characters after every change. Lines over about 200 characters swallow the case: move the detail to the file.
- When ten or more notes cover one theme, propose a consolidated file and a single stub line. Show it first.
- A choice made once for one case is not an entry. Ask: does this always hold, or only here?
- Replace the invented lines with the person's real ones. Never copy the examples into their system.
-->
