# Payment reminders - work plan

Status: open. Last update: 2026-10-15.

## Request

"Every month we find out too late who hasn't paid, and then Tiziano chases them by hand when he has time. I'd like it to happen by itself, politely, without us having to remember." - Ottavio Calvesi, kickoff call, September 29, 2026.

## Setup

Constraints already decided (see [project rules](../project-rules.md) and [decisions](../decisions.md)):

- We start from the reminders, not from the management software (decided 2026-09-29).
- Two reminders, at 7 and at 21 days after the due date; after the second the case goes to a person (decided 2026-10-06).
- The reminders go out by email, from the firm's administration address (decided 2026-10-08).
- No message goes out to the firm's clients without Ottavio Calvesi's written yes.
- Trials run on lists chosen by the firm, never on all clients.
- Tiziano Olivari is the contact for all the material; Ottavio Calvesi approves the texts.

## Legend

[x] done and verified - [ ] to do - (Livia) / (Tiziano) / (Ottavio) whose turn it is

## Steps

1. [x] Write down how the firm sends reminders today, reviewed with Tiziano. Done when: the flow is on paper, step by step. (deliverables/current-flow.md, six steps, reviewed by phone, 2026-10-01)
2. [x] Get the list of the invoices overdue at the end of September. Done when: the export is in the project. (materials/overdue-invoices-september.csv, 64 invoices from 41 clients, 2026-10-01)
3. [x] Get the texts the firm sends by hand today. Done when: the three texts are in the project. (materials/current-reminder-texts.md, received 2026-10-06, a day later than promised)
4. [x] Build the prototype with two reminders, at 7 and at 21 days, starting from the firm's own texts. Done when: both messages exist and read like the firm. (prototype built 2026-10-06)
5. [x] Review the prototype with Ottavio and Tiziano and settle the channel. Done when: the channel is decided and the prototype works on it. (call of 2026-10-08, switched to email, prototype adapted the same day)
6. [x] Get the list of twenty clients chosen by the firm for the trial. Done when: the list is in the project. (materials/trial-client-list.csv, received 2026-10-13)
6a. [x] Check how name and amount look on five rows before every send. Added 2026-10-13, after the first send went out with the client's name in capitals. Done when: the rule is written in the tool file. (rule in [automated-email](../../../agent/knowledge/tools/automated-email.md), 2026-10-13)
7. [x] Send the first reminder to the twenty clients, with Ottavio's written yes. Done when: all twenty messages went out. (2026-10-13, signature: administration)
8. [x] Collect the trial results two days after the send. Done when: paid, asked for time and no answer are counted. (12 paid, 3 asked for more time, 5 no answer; deliverables/twenty-client-trial-results.md, 2026-10-15)
9. [ ] Get Ottavio's written go-ahead to extend the reminders to all clients. Done when: the yes is in writing. (Ottavio) - to be discussed on the call of October 20.
10. [ ] Settle who signs the emails, administration or Ottavio. Done when: the choice is in the decisions file. (Ottavio) - the trial used the administration's signature, not rechecked.
11. [ ] Write the proposal for clients with three or more overdue invoices, who don't answer automatic messages. Done when: the proposal is on one page, ready for the call of October 20. (Livia)
12. [ ] Send to all clients and hand over. Done when: the reminders run for all clients and Tiziano has stopped one and changed one text by himself. (Tiziano, after steps 9 and 10)

## Postponed

- Rebuilding the management software. Reason: decided on 2026-09-29 to start from the reminders, which cost administration the most time; to be reviewed at the end of the trial.
