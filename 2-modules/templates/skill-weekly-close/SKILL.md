---
name: weekly-close
description: >
  Closes the week: for each active project it opens the new week's log file, carries the current
  state over keeping only the threads still open, marks what wasn't verified as "not rechecked",
  and updates the pointer on the home page. Use it when the person types /weekly-close, "close
  the week", "weekly review of the states". Don't use it to write the person's own reflection, and
  don't use it mid-week.
---

# Weekly close

Purpose: states don't go stale from one week to the next, and nothing open is lost in the carry-over.

## Where I write

<!-- To be filled in during installation with the real paths. -->

| What | Where |
|---|---|
| New week's file and its current state | `[project folder]/[log folder]/[YYYY-Wnn].md` |
| Pointer to the current week | `[path to the home page]` |

## Step 0 - Which week

Work out the week just ended and the new week with the system calendar, not from memory. If the new week is not the one right after the last file, say so and ask.

## Step 1 - List the active projects

From the home page. For each one, read the current state of the latest week's file and the entries below it.

## Step 2 - Prepare the carry-over, per project

1. Take the current state.
2. Keep only the threads still open. Closed threads drop out: their detail stays in the dated entries of the old week.
3. **When in doubt a thread stays.**
4. If you cannot verify a thread (no recent entry, nothing in the project, the person unreachable), keep it and mark it "not rechecked". Don't remove it.
5. Update the date of the last update.
6. If the state is longer than about 5 KB, flag it and propose moving detail into the dated entries. Don't rewrite it silently.
7. If the project had no activity and no open thread, create nothing and say so. No empty log for the sake of conformity.

## Step 3 - Show before writing

Show the person, per project:

- the exact state that will open the new file;
- the threads kept, the ones marked "not rechecked", the ones dropped;
- the home page line that will change.

Wait for a yes. Anything not confirmed is not written.

## Step 4 - Write

After the yes:

1. Create the new week's file with the state at the top and no empty day headings.
2. Update the pointer on the home page.
3. Don't edit the old week's file. A wrong fact in it gets a dated note, not a rewrite.
4. Note in `progress.md` the files created and changed, if the kit's progress file is in use.

## Step 5 - Recap

One line per project, with one of three marks:

- `✓` written and reread
- `-` nothing to carry
- `!` not written or not verified, with the reason

Example:

```
✓ [Project A]: 2026-W42 created, 3 threads kept, 1 marked "not rechecked"
- [Project B]: no activity, no open thread, nothing created
! [Project C]: state over about 5 KB, flagged, waiting for the person's choice
✓ Home page: pointer updated
```

Nothing else after the recap, unless a `!` needs a choice.
