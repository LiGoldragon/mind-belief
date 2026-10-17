---
description: Which flows run under the production Flow Nexus and which still run on the old route, how a message picks its route, and how to observe both.
dependencies: [vision-flow, knowledge-flow]
---

Observed on 2026-10-17 at 12:55 -06:00, against the running Flow Nexus
0.35.11 (Flow `67b80b3`, store
`/home/li/.local/state/flow-production/flow.sema`), messenger-clj 0.4.0
and the Herdr session `default`. A flow's route can change with any
start, bind or retirement; observe again before relying on it.

## How a message picks its route

The target decides the route. `hm-send` asks Flow for the target's
metaflow; an address Flow does not know is typed into its pane by
Herdr, as before Flow. An address Flow knows goes to Message, which
names the sender through Flow and refuses a sender that is no flow.

```
          +------------------------+
          | hm-send to a target    |
          +-----------+------------+
                      |
                      | asks Flow for
                      v
          +------------------------+
          | the target's metaflow  |
          +-----+------------+-----+
                |            |
     not known  |            | known
                v            v
+----------------+    +------------------+
| typed into the |    | Message asks     |
| target's pane  |    | Flow who sent it |
| by Herdr       |    +----+--------+----+
+----------------+         |        |
                    a flow |        | no flow
                           v        v
               +------------+  +------------+
               | queued for |  | refused    |
               | the target |  |            |
               +------------+  +------------+
```

The deployed messenger-clj 0.4.0, `messenger_clj/public.clj` and
`messenger_clj/flow_bridge.clj`:

```clojure
(defn routed-delivery! [target request options legacy]
  (name! target)
  (runtime/validate-request! request)
  (if (bridge/managed? target)
    (bridge/send! target request options)
    (delivery! target legacy)))
```

```clojure
(defn managed? [target]
  (let [query (str "Current." (address! target))
        result (try (*call* "flow" query)
                    (catch Exception _ (runtime/fail "FlowRegistryUnavailable: no legacy fallback")))
        answer (str/trim (or (:out result) ""))]
    (when-not (zero? (or (:exit result) -1))
      (runtime/fail "FlowRegistryUnavailable: no legacy fallback"))
    (cond
      (= answer "Current.Unknown") false
      (contains? #{"Current.Asleep" "Current.Ended"} answer) true
      (re-matches #"Current\.Awake\.(?:[A-Za-z0-9_-]+|«[^«»\\\n]+»)" answer) true
      :else (runtime/fail "FlowRegistryRefused: unexpected or refused Current response; no legacy fallback"))))
```

## What Flow holds

Flow's whole state is its metaflows. Their type, `Metaflow`, is in
Flow's `crates/flow-ethos/ethos/library.ethos`, quoted whole at Flow
`67b80b3`:

```ethos
; Flow's shared types live in this leaf package. Signal and Meta-Signal
; import them here and re-export their original Rust paths. Aspect is one
; nominal type shared by addresses, launch profiles and meta configuration.

Library
[]
[ FlowId.String
  ; ethos-zero 16 cannot express Topic:Name yet; check camelCase at input.
  Topic.String
  ; The design type is Blake3.Bytes<32>; 16.0 uses a 64-hex-character string.
  Blake3.String
  Layer.[ Primary Secondary Tertiary Quaternary ]
  Subaspect.[ Vision Intent Knowledge Operation Trial Compensation ]
  ; Define the component types once. Source refers to these declarations;
  ; inlining Path.String inside Source would redeclare Path globally.
  Repository.String
  Hash.Blake3
  Path.String
  Reason.String
  Source.{ Repository Hash Path }
  Key.{ Subaspect Topic }
  Said.{ Context.String Verbatim.String }
  Request.[ Order.String
            Question.String
            Psyche.Said
            Psyches.Vector<Said>
            Result.String
            Notice.String ]
  Aspect.[ Psyche Mind Field ]
  Address.{ Aspect Topic Layer }
  Recipient.[ Address Up ]
  ; Who a queued request is from: the Address Flow resolved for its sender
  ; (the Lock's Sender of a Deliver, the thread's metaflow of a send-tool
  ; call), or Unknown for a request queued before Flow kept senders.
  SentBy.[ Sender Unknown ]
  QueuedRequest.{ SentBy Request }
  Metaflow.{ Address
             State.[ Awake.FlowId Asleep Ended ]
             Past.Vector<FlowId>
             Queue.Vector<QueuedRequest> }
  Lock.{ Sender Address Until.Integer }
  Process.{ Pid.Integer Started.Integer }
  Sender.Address
  OrdinarySocketPath.String
  MetaSocketPath.String
  StorePath.String
  Start.{ OrdinarySocketPath MetaSocketPath StorePath }
  ; Startup refusal is distinct from the ordinary/meta socket Refusal.Store.String.
  StoreRefusal.{ Path Reason }
  StartRefusal.[ Store.StoreRefusal ]
  SourceRoot.String
  ClientPath.String
  Home.String
  ControlSocketPath.String
  ModelName.String
  CodexEndpoint.{ ClientPath Home ControlSocketPath Vector<ModelName> }
  StableCodex.CodexEndpoint
  NextCodex.CodexEndpoint
  HarnessKind.[ Codex Claude ]
  KeyName.String
  CommandSigil.String
  InterruptKeys.Vector<KeyName>
  SubmitKeys.Vector<KeyName>
  HarnessProfile.{ HarnessKind Vector<CommandSigil> InterruptKeys SubmitKeys }
  HarnessProfiles.Vector<HarnessProfile>
  MetaAspects.Vector<Aspect>
  MessageNexusPath.String
  MessageNexusBinary.String
  Nexus.{ SourceRoot
          StableCodex
          NextCodex
          HarnessProfiles
          MetaAspects
          MessageNexusPath
          MessageNexusBinary
          Lease.Integer } ] ; Lease seconds; 60 before any Nexus payload.
[]
[]
```

```sh
flow 'Metaflows'
# -> Listed.[ … { { Psyche flow Secondary }
#      Awake.17c364 [] [ … ] } … ]
flow 'Current.{ Psyche core Primary }'
# -> Current.Unknown
herdr pane list
```

At the observation, Flow held four Psyche and Field flows that have a
live pane:

| Flow | Address | Harness | How it came under Flow | State |
|---|---|---|---|---|
| d68c82 | Psyche core Secondary | Claude, Opus | adopted: binding imported, then bound from its own process | Awake |
| 17c364 | Psyche flow Secondary | Codex, Astra | started by Flow | Awake |
| 804eb9 | Psyche ethos Secondary | Claude, Opus | started by Flow | Asleep, no pane |
| 75f438 | Field startup-codex-0355 Quaternary | Codex | started by Flow, a Field proof | Awake |

The store also holds rows with no pane: `{ Field message Primary }`
Awake as `flow-0000000000000013`, and five asleep Field proof
metaflows.

Twenty-two live harness panes run on the old route: Flow answers
`Current.Unknown` for their addresses. Their titles at the observation:
Field 42265e and 44cda5; Mind 41fa34, 0c85a3, 0430eb, 47d946, 5b9075,
e4b7d7, 9896d8; Field PrimaryCommitting 89fbc1; Psyche core Primary
39bd0c, core Tertiary 4201a3, Spirit d55c56 and ee57fb, Nexus 058f16,
nexus a275c0, Communication 3960eb, chronos 984e88 and 504f11,
InstructionWitness 19d9f2, and da2038 and 65f93a, which messenger-clj
records as retired while their panes stay open.

`hm-list` printed `MetaflowMetadataRequired: registration lacks aspect,
topic or layer` and listed nothing, so the old route's own registry was
not read.
