---
description: The Flow CLI for sending, self-binding and declared launches.
dependencies: [vision-flow, knowledge-flow]
---

The ordinary `flow` CLI takes one inline datom as one shell argument. Source: Flow `d87b15a`, `crates/flow/src/main.rs`, `crates/flow-nexus/src/sending.rs` and `waking.rs`; signal-flow `994ce15`, `src/generated/signal.rs`. These are source contracts, not evidence of an installed revision.

```sh
flow 'Current.{ Mind tools Secondary }'
flow 'Metaflows'
flow 'Send.{ Address.{ Mind tools Secondary } Wake Soft.Order.«Review the source packet.» }'
flow 'Send.{ Address.{ Mind tools Secondary } Queue Soft.Notice.«The source packet is available.» }'
flow 'Send.{ Up Wake Soft.Result.«The bounded package is ready.» }'
flow 'BindSeat.{ Mind tools Secondary }'
flow 'Launch.{ { Mind tools Secondary } «Review the declared task.» }'
```

`Send` has three positions: recipient, delivery, message. The recipient is `Address.{ Aspect topic Layer }` or `Up`, the layer above in the sender's aspect and topic. Delivery is `Wake` or `Queue`. `Wake` requests wake and queue draining; `Queue` retains work without independently requesting a wake. Delivery is explicit and independent of the message kind. `DeliverAll.{ Mind tools Secondary }` requests delivery of all work already queued for that address.

The CLI also accepts a two-position `Send`, recipient followed by message, and supplies `Wake`. It sends the same typed three-position request to Nexus:

```sh
flow 'Send.{ Address.{ Mind tools Secondary } Soft.Order.«Review the source packet.» }'
```

A message is a priority carrying a request. Priorities are `Soft`, `MiddleAbrupt` and `HardAbrupt`. Request kinds are `Order`, `Question`, `Result`, `Notice`, `Psyche` and `Psyches`. `Psyche` carries context and verbatim strings; `Psyches` carries their vector. The sender is resolved from the calling process; no command supplies a sender Flow ID.

```sh
flow 'Send.{ Address.{ Psyche core Secondary } Wake Soft.Psyche.{ «The context.» «The exact words.» } }'
flow 'Send.{ Up Queue Soft.Psyches.[ { «First context.» «First words.» } { «Second context.» «Second words.» } ] }'
```

Successful admission returns `SendAccepted.{ logical-delivery-id cursor Queued }`. This witnesses durable acceptance, not native arrival, reading or completion. `ObserveSends.None` opens the sender's outcome stream; a returned cursor can resume it. An unknown recipient returns `Refused.Unknown.Address`; sending does not declare or launch an unknown metaflow. `Up` from a Primary returns `Refused.NoneAbove`.

`Current` reports `Current.Awake.<id>`, `Current.Asleep` or `Current.Unknown`. `Metaflows` lists addresses, current state, prior flows and queued requests. A closed pane alone does not establish that a metaflow is absent.

`BindSeat` identifies the calling native seat and binds it to the supplied address. Its only position is the address; it takes no supplied native session, process or Flow ID. An occupied address can refuse as `Taken`; an unlocated caller refuses as `Unidentified`.

`Launch` has two positions: address and instruction string. It composes the address's declared system and user modules with the configured model and layer effort. Missing declarations return `StartRejected.Undeclared`; a missing configured model refuses as `NotConfigured`. Launching the caller's own live address replaces that flow. Launch success, send acceptance and native receipt are separate observations.
