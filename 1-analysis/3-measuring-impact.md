# How to measure impact

Goal: tell the person what the gaps cost them today, with numbers counted in their own work and not with promises.

## Ask for permission first

Explain to the person what you are about to do, in your own words but leaving nothing out:

- Claude Code stores past sessions on the computer, usually in `~/.claude/projects/`. By default it deletes them after about 30 days, so you may find only a few.
- You will use the script `1-analysis/extract_sessions.py`. It runs on their computer, writes no files and sends nothing over the network.
- The script prints the start of the messages they wrote. You will read those excerpts, like any other file: if the sessions contain client data, it will pass through you.
- They can say no. In that case you will use the five questions at the bottom of this page.

Without an explicit yes, don't run the script.

If the person doesn't use Claude Code, don't guess where their agent stores sessions: move to the five questions, or ask whether they know where the sessions are and in what format.

## The four measures

### 1. Sessions that start by re-explaining

What you count: sessions where the person's first messages give context back instead of asking for work. Signals: "where we left off", "remember that", "as I said", a long project summary pasted at the start.

Command:

```
python3 1-analysis/extract_sessions.py --sessions 30 --messages 3
```

Report: how many sessions out of how many read, and two short examples.

Related capabilities: 1, 2, 4.

### 2. Work before the first result

What you count: how many operations the agent runs before its first edit to a file. The script prints it for every session. A high number at the start of a session on a project already under way suggests the agent is rebuilding the state by reading around.

Report: the median across the sessions read, and the three highest values with their dates. Present it as a hint, not as proof: a research session has high numbers for good reasons.

Related capabilities: 2, 4, 10.

### 3. Repeated corrections

What you count: the same correction made by the person in different sessions.

Command, to be adapted to the person's language:

```
python3 1-analysis/extract_sessions.py --sessions 30 --search "I told you|I already|again|stop doing|as I said|don't ever|how many times"
```

Read the results and group the ones that say the same thing. Count only groups that span at least two different sessions.

Report: how many groups, and for the two most frequent ones the correction in one line and how many sessions it appears in.

Related capabilities: 7, 9.

### 4. Outdated information

What you count: the times the person corrects the agent because it used old information.

Command:

```
python3 1-analysis/extract_sessions.py --sessions 30 --search "no longer|outdated|that was the old|we changed|we decided not|not anymore"
```

Report: how many cases, and one or two examples.

Related capabilities: 5, 6.

## How to write up the results

- Write the number and the base: "7 sessions out of 28".
- At most two examples per measure, shortened, with no client names.
- Don't convert into hours. If the person wants an estimate, build it with them starting from a number of theirs, and write it down as their estimate.
- If a measure comes out as zero, say so. A zero means that part of the system holds.
- If fewer than ten sessions were read, state it: the measure is weak.

## If the sessions can't be read: five questions

1. When you reopen a project that has been idle for a couple of weeks, what do you do in the first few minutes? Tell me about the last time.
2. Can you think of a recent case where the agent used old information: a price, a decision that changed, a superseded file?
3. Is there a correction you find yourself making over and over, about writing style or about mistakes with a tool?
4. If a collaborator had to take over one of your projects tomorrow, where would they read how far along it is?
5. A decision made two months ago on a project: where do you find it, and do you also find the reason?

In the report, give the answers as the person's account, not as a measure.
