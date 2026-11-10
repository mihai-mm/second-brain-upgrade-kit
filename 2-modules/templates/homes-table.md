# Where each kind of information lives

To paste into the instructions the agent always reads, after filling it in with the real places.

| Information | Where it lives | Doesn't go in |
|---|---|---|
| Where a project stands, what is open, next steps | Current state, at the top of the latest week's log: `[path]` | Decisions file, profiles, the agent's memory |
| What was done, day by day | Log entries: `[path]` | - |
| Decisions with the reason, things learned, numbers that stay | The project's decisions file: `[path]` | Log (only the pointer goes there) |
| Rules and boundaries of a project | Project instructions: `[path]` | - |
| Durable facts about a client or a person | Profile: `[path]` | Project files |
| What was learned about a tool | Tool file: `[path]` | Project files |
| Corrections about how the agent works | `[path]` | Project instructions, if they hold everywhere |
| Transcripts, material received, work produced | Project folders: `[paths]` | - |

Rules:

- The same information is not written in two places. Where it needs to be called up, put a pointer.
- When a piece of information changes, it is updated in its home.
- A replaced decision is marked as superseded and the new one is named.
- If it isn't clear where something goes, ask before writing.
