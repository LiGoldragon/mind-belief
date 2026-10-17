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

Flow's whole state is its metaflows. Their type, in Flow's
`crates/flow-ethos/ethos/library.ethos`:

```ethos
Metaflow.{ Address
           State.[ Awake.FlowId Asleep Ended ]
           Past.Vector<FlowId>
           Queue.Vector<QueuedRequest> }
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
