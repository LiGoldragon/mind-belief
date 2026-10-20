---
description: The Flow 0.37.1 public CLI for metaflow state, sending and declared launches.
dependencies: [vision-flow, knowledge-flow]
---

Flow 0.37.1 exposes messaging and declared launches through the ordinary `flow` CLI. Source: Flow `fc53f4f`, `crates/flow-nexus/src/sending.rs` and `waking.rs`. The running Ouranos CLI reported `flow 0.37.1` on 2026-10-19.

```sh
flow 'Current.{ Psyche core Secondary }'
flow 'Metaflows'
flow 'Send.{ Address.{ Psyche core Secondary } Soft.Order.«The source packet is ready.» }'
flow 'Launch.{ { Mind tools Secondary } «Review the declared task.» }'
```

`Current` reports `Awake.<id>`, `Asleep` or `Unknown`. `Metaflows` lists addresses, their current state, prior flows and queued requests. A closed pane does not by itself mean a metaflow is absent: its state and queue belong to Flow.

`Send` resolves its sender from the calling process and addresses a metaflow. Priorities are `Soft`, `MiddleAbrupt` and `HardAbrupt`. Kinds are `Order`, `Question`, `Result`, `Notice`, `Psyche` and `Psyches`. `Psyche` carries context and verbatim strings; `Psyches` carries their vector.

Soft sends queue. Abrupt sends first attempt delivery to a live recipient; when that attempt does not return delivery success, the implementation queues the request. `Queued` confirms queue acceptance; `Delivered` confirms the abrupt delivery path, not that the recipient understood or completed the request.

Orders, questions and psyche requests make an Asleep metaflow due to wake. Results and notices do not independently trigger a wake. An unknown target returns `Refused.Unknown.Address`; Send does not create an unknown metaflow.

Launch composes the address's declared system and user modules. Its model comes from `Configure.Models`; module declarations come from `Configure.Metaflows`; leave-outs come from configuration. Missing declarations refuse as `Undeclared`, and an unconfigured model refuses. Launching one's own live address selects replacement of the calling flow.

The selected implementation allows all routes within an aspect. Across aspects it requires the same topic and layer; Field can answer Psyche only after Psyche has sent to that Field address. That answer permission is held in process memory and is lost on Nexus restart.

At this revision, an idle seat with no queued work stays Awake in its pane. A fresh wake uses the metaflow's declared modules, or its last launch's modules when no declaration exists. Launch success, queue acceptance and native receipt are separate observations.
