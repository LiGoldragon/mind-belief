---
description: Process-based caller attribution and self-binding a live seat through Flow 0.37.1.
dependencies: [vision-flow-nexus, knowledge-flow-nexus, knowledge-flow-seats]
---

Source: Flow 0.37.1, `fc53f4f`, `crates/flow-nexus/src/caller.rs` and `sending.rs`.

Send, Launch and BindSeat take the calling process from the Unix socket peer. Their public payloads carry no sender Flow ID.

For a Herdr caller, the Flow Nexus follows process ancestry and Herdr's pane/session marks, identifies the Herdr server by its listening socket, and checks the recorded pane binding against the live Herdr snapshot. The binding includes session, pane, terminal and harness. A reused pane with a different terminal is not the old caller.

For a Codex command, the Flow Nexus walks ancestry to the command process whose parent executable is a configured Codex app-server. It reads that command process's `CODEX_THREAD_ID`, then resolves the native thread through the Flow Nexus's records. It does not take the thread from an arbitrary descendant's environment. When the command has no Herdr pane marks, BindSeat searches live Herdr session snapshots for that native thread.

A live seat outside the Flow Nexus's records can bind itself:

```sh
flow 'BindSeat.{ Mind core Secondary }'
```

BindSeat locates the calling seat and native session, claims its ID through `flow-id`, records the native binding and takes the metaflow address under the address-taking rules. It does not accept a supplied native ID or pane.

On 2026-10-19, the existing Mind core Secondary Codex seat ran this command through its own tool process and received `Bound.41fa34` from the deployed 0.37.1 Nexus. This witnesses that seat's binding only; it does not establish any other seat's registration.

The legacy ordinary `Bind.{ Address Process }` remains a distinct contract at this revision. It can mint sequential `flow-<hex>` process-binding IDs. Those are not evidence of a six-character native-session claim made by BindSeat.
