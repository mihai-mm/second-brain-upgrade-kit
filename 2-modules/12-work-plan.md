# Module 12 - A written plan for multi-step work

Installs capability 15. It needs the work log (module 01) and the project index (module 07): the log links the plan and the index lists it.

## What it's for

A job with many steps should survive the end of the session. After a context reset, or the next day, the agent knows which steps are done, which are left, and whose turn it is, without the person re-listing them.

## Why it works

- **Chat and the agent's built-in to-do list disappear.** A plan in the chat is gone with the session. A file in the project is still there.
- **Written before step one.** A plan written afterwards records what happened. A plan written first shows what was agreed, and the person can read it while the work goes on.
- **One step, one verifiable result.** "Check the form" is an activity. "The form sends a test entry and it appears in the sheet" is a result. It tells everyone when the step is done.
- **Evidence next to every closed step.** A tick without evidence is a claim. With evidence (a test that passed, a file path, a date) it can be checked.
- **Stable numbering.** If steps are renumbered, every earlier mention of "step 7" becomes wrong. Additions take a suffix (3a) and their date.
- **Not the task manager.** A task is something not to forget, and it lives beyond the work. A step exists only inside this work.

## Essential

1. A plan file in the project, created before the first step is executed.
2. It contains: the request in the person's words with its date, the setup and constraints, a legend, numbered steps, a "Postponed" section, and an "Outcome" section when closed.
3. Every step names the result that says it is done. Steps owned by someone else carry their name in parentheses.
4. A step is ticked only with evidence in parentheses. If the check was not made, the step stays open with a note.
5. A request that arrives mid-work enters the plan before it is executed, as an addition with a suffix and a date.
6. The work log links the plan and does not copy the checklist. The project index lists it. The current state of the project has one line: work in progress, plan, open steps.
7. Before a context reset or a long pause the plan is up to date.
8. The plan is closed with an outcome: what was delivered, and where the open steps went.

## When to open one

- Four or more distinct steps.
- Work that will outlast the session.
- Steps owned by other people (the person, a collaborator, another agent).
- Requests arriving while the work is under way.

Do not open one for a single fix, an answer to a question, or a text built one choice at a time.

If the work started without a plan, create it at once with the steps already done ticked, and tell the person that it was late.

## Adaptable

- The file name, its folder (for example `reports/`), the legend.
- The language of the steps: plain enough that the person understands a step without opening the code.
- Whether open plans are marked in a field at the top of the file or in the index only.
- If the person uses a task tool or tickets the agent can read, the plan can still live in the project: the steps point to the tickets, they don't copy them.

## How to install it

1. Ask the person for a recent job with many steps and ask what happened to its list. Show where the plan lived (chat, memory, nowhere).
2. Agree on the folder and the file name. Follow the conventions of their system.
3. Show `templates/plan.md` and adapt it with the person: legend, sections, language.
4. Install the skill `templates/skill-plan/SKILL.md`, adapted to their paths. Show it first and write it after the yes.
5. Add to the main instructions one line: for jobs with four or more steps, open a plan before the first step. Show the exact text and the spot first.
6. If a job is under way now, open its plan with the done steps ticked.
7. Note in `progress.md` the files created and the line added.

## Check

1. Start a job with five steps. The plan file exists before the first change.
2. Interrupt it. In a fresh session ask "where were we on this?". The answer comes from the plan, with step numbers.
3. Close one step. The tick has its evidence and the last update date matches.

If test 1 fails, the instruction is too vague about when to open a plan: make the four triggers explicit.

## To roll back

Remove the instruction line and the skill. Existing plan files can stay: they are ordinary project files.
