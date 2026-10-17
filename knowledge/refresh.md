---
description: How a flow's context size is measured and what happens at a refresh threshold today, in the Flow Nexus and in Primary's tools.
dependencies: [vision-flow, knowledge-flow]
---

Two mechanisms carry a context threshold today. The Flow Nexus has two
numbers per layer and reads one of them, only when it wakes a sleeping
metaflow. Primary has a Stop-hook program with a warning size that no
installed hook calls. No flow is refreshed while it is awake.

Verified on 2026-10-17 against Flow `67b80b3` (0.35.11, installed and
running), meta-signal-flow `a918b7d` (the revision Flow pins), Primary
`bda70b5`, and the running Nexus's `Configuration` reply.

## How it flows

```
+----------------------------+
| a Claude flow's turn       |
+-------------+--------------+
              |
              | ends: Report.Stopped
              v
+----------------------------+
| the Flow Nexus             |
+-------------+--------------+
              |
              | reads the last usage of
              v
+----------------------------+
| the transcript: input +    |
| cache read + cache write   |
+-------------+--------------+
              |
              | records it as
              v
+----------------------------+
| Record.Context, per flow   |
+-------------+--------------+
              |
              | nothing queued:
              | the flow sleeps
              v
+----------------------------+
| asleep metaflow            |
+------+--------------+------+
       |              |
       | a request    | Refresh.Address
       | wakes it     | marks it
       v              v
+----------------------------+
| wake plan                  |
+------+--------------+------+
       |              |
       | size under   | size at or over
       | Refresh, or  | Refresh, or
       | unknown      | marked, or Codex
       v              v
+------------+  +------------------+
| resume the |  | fresh launch     |
| session    |  | from the last    |
+------------+  | launch's modules |
                +------------------+
```

## The two numbers per layer

The meta wire declares them in meta-signal-flow `ethos/signal.ethos`
(`ConfigureThreshold` and `ConfigurationChange` are in it), quoted
whole at `a918b7d`, the revision Flow `67b80b3` pins:

```ethos
; Flow privileged Signal.
;
; Flow is the only pane writer. Deliver and Command are the only ways
; anything is typed into a flow's pane, and both run under Flow's own
; per-pane lease: an exclusive hold over the whole key sequence, never
; handed out on the wire.
;
; Deliver carries a typed Message addressed by FlowId; Flow renders it,
; so the pane text always begins with its Priority head (HardAbrupt.,
; MiddleAbrupt. or Soft.). A Letter names its MessageId first: the id the
; sender's Message Nexus minted, carried through untouched so the
; recipient reading the pane can Acknowledge it. Flow never interprets it. The Content may hold no control character but
; LF and TAB (ControlCharacter carries the byte offset in the rendered
; pane text), and a first line that is a harness command (a sigil of the
; recipient's HarnessProfile, then a command word) is refused as
; HarnessCommand: harness commands go through Command. Vet answers what
; Deliver would refuse and types nothing. Deliver is idempotent on its
; DeliveryId: a repeat answers the stored Delivery and types nothing. A
; delivery a crash left under the lease settles Uncertain and is never
; retried.
;
; Soft needs the recipient Idle or Done; every tier refuses a Blocked
; recipient and a composer that already holds text. Transported means
; Herdr accepted the text for the exact binding; Presented means the
; recipient was seen reacting on the exact pane. InterruptWitness says
; whether a HardAbrupt interrupt was seen to leave Working.
;
; Every query on this socket answers MetaRefused unless the peer is the
; configured Message Nexus executable, a process in no flow's pane (the
; owner), or a flow whose aspect is in MetaAspects.
;
; MessageNexusBinary is the executable identity used by Bind as Message on
; the ordinary socket. A payload PID does not establish that identity.
;
; ResolvePeer names the flow a process runs in, as ResolveCaller does for
; an ordinary connection's own peer.
;
; ReadEvents answers the harness events Flow holds in its Memory for one
; flow, in the order its Reports were recorded: EventsRead, or
; ReadEventsRejected.UnknownFlow for a FlowId Flow does not hold.
;
; Configure declares one configuration family whole: Models, Thresholds,
; LeaveOuts or Nexus. The declared value replaces that family's committed
; value in one atomic commit, so the family's effective value is always its
; last declaration; an entry absent from the declaration is removed. It
; answers Configured.Replaced, or Configured.Unchanged when the committed
; value already equals the declaration and nothing is written. Each family
; holds one entry per key: Models and Thresholds one per Layer, LeaveOuts
; one per Address (the default leave-outs of one metaflow, which a Start
; naming its own replaces). ConfigureRejected changes nothing:
; DuplicateEntry when a declaration names one key twice, CodexModelsOverlap
; when a Nexus names one model under both Codex endpoints. Configuration
; reads the committed Nexus and the committed model, threshold and leave-out
; vectors; it never returns defaults, and answers Unconfigured while no
; Nexus has been declared. A seat's context is named by its launch, never
; configured here.
; Configure.Nexus names the actual Message executable in MessageNexusBinary.
; Lease is the lock duration in seconds; a fresh, unconfigured default is 60.
; A running Nexus reads its Codex endpoints when it opens, so a replaced
; endpoint is served from the next start.

; Refresh names one metaflow whose next wake starts a fresh native session,
; composed from the module identities and leave-outs its last launch
; recorded, instead of resuming the last flow's session. It marks that one
; metaflow only; no model or threshold changes, and the mark clears when
; the metaflow is recorded Awoken. It answers Refreshed with the Address,
; and a second Refresh while the metaflow is marked answers the same.
; RefreshRejected: Unknown (no metaflow at the Address), Awake, Ended,
; NoLaunchProfile (its last flow has no recorded launch profile to compose
; from), StoreRefused. Only an Asleep metaflow is accepted.

; MetaBindExisting verifies each binding against Herdr before it is stored:
; PaneAbsent (the container's Herdr session shows no agent of the binding's
; harness at its workspace, pane and terminal), ProcessMismatch (the pane's
; foreground processes do not include the binding's process), SessionMismatch
; (Herdr reports another native session for the pane), SessionUnreported (a
; Claude pane reports no native session), SessionUnproven (a Codex pane
; reports none and no rollout whose session_meta names the session exists),
; HerdrUnreadable (the session's snapshot or the pane's processes could not
; be read).

Signal
[ signal_flow:[ FlowNode FlowId Aspect PowerLevel ModelName HarnessKind NativeSessionId HerdrSessionName HerdrAgentName HerdrWorkspaceId HerdrPaneId HerdrTerminalId Caller CallerResolutionRejection Event LeaveOuts ]
  flow_ethos:[ OrdinarySocketPath MetaSocketPath SourceRoot ClientPath Home ControlSocketPath CodexEndpoint StableCodex NextCodex KeyName CommandSigil InterruptKeys SubmitKeys HarnessProfile HarnessProfiles MetaAspects MessageNexusPath MessageNexusBinary Lease Subaspect Topic Layer Address ] ]
[ Configuration
  Configure.ConfigurationChange
  ConsumeReset.ResetRequest
  RegisterFlow.FlowNode
  MetaBindExisting.MetaBindExisting
  Retire.FlowId
  Deliver.DeliveryRequest
  Vet.DeliveryRequest
  Command.CommandRequest
  ResolvePeer.ProcessIdentity
  ReadEvents.FlowId
  Refresh.Address ]
[ Configured.ConfigureOutcome
  Configuration.ConfigurationSnapshot
  Unconfigured
  ResetConsumed.ResetOutcome
  FlowRegistered.FlowNode
  ConfigureRejected.ConfigureRejection
  ResetRejected.ResetRejection
  FlowRegistrationRejected.FlowRegistrationRejection
  BoundExisting.BoundExisting
  BindExistingRejected.BindExistingRejection
  FlowRetired.FlowNode
  RetireRejected.RetireRejection
  Delivered.Delivery
  DeliveryRejected.DeliveryRejection
  Vetted.FlowId
  Commanded.CommandOutcome
  CommandRejected.CommandRejection
  PeerResolved.Caller
  PeerResolutionRejected.CallerResolutionRejection
  MetaRefused.MetaRefusal
  Refused.Refusal
  EventsRead.{ FlowId Vector<Event> }
  ReadEventsRejected.[ UnknownFlow StoreRefused ]
  Refreshed.Address
  RefreshRejected.RefreshRejection ]
[ ; Flow Library owns the shared configuration field types.
  ; This record exists only for Flow's current internal launch defaults.
  ; The process sockets are separately supplied by Library.Start; this
  ; record is not a Configure wire payload.
  NexusRuntimeSettings.{ OrdinarySocketPath MetaSocketPath SourceRoot StableCodex NextCodex Vector<HarnessProfile> MetaAspects MessageNexusPath MessageNexusBinary Lease }
  ConfigureModel.{ Layer Native.String }
  ConfigureThreshold.{ Layer Handover.Integer Refresh.Integer }
  ; The leave-outs a metaflow's Start takes when it names none.
  ConfigureLeaveOut.{ Address LeaveOuts }
  ConfigureNexus.{ SourceRoot StableCodex NextCodex HarnessProfiles MetaAspects MessageNexusPath MessageNexusBinary Lease }
  ; Keep the payload type distinct from the unit Query.Configuration variant.
  ConfigurationChange.[ Models.Vector<ConfigureModel>
                         Thresholds.Vector<ConfigureThreshold>
                         LeaveOuts.Vector<ConfigureLeaveOut>
                         Nexus.ConfigureNexus ]
  ConfigureOutcome.[ Replaced Unchanged ]
  ConfigurationSnapshot.{ Nexus.ConfigureNexus Models.Vector<ConfigureModel> Thresholds.Vector<ConfigureThreshold> DefaultLeaveOuts.Vector<ConfigureLeaveOut> }
  IdempotencyKey.String
  CreditId.String
  CreditSelection.[ Next
                    Specific.CreditId ]
  ResetRequest.{ IdempotencyKey CreditSelection }
  ResetOutcome.[ Reset NothingToReset NoCredit AlreadyRedeemed ]
  ConfigureRejection.[ StoreRefused DuplicateEntry CodexModelsOverlap ]
  RefreshRejection.[ Unknown Awake Ended NoLaunchProfile StoreRefused ]
  ResetRejection.[ AdapterUnavailable ProtocolRefused ]
  FlowRegistrationRejection.[ StoreRefused UnknownOrUnclaimedIdentity ConflictingBinding ]
  ProcessId.Integer
  ProcessUserId.Integer
  ProcessStartToken.String
  ProcessIdentity.{ ProcessId ProcessUserId ProcessStartToken }
  HerdrServerSocketPath.String
  HerdrServerProcessIdentity.ProcessIdentity
  MetaFlowOwnerId.FlowId
  HerdrTabId.String
  WorkingDirectory.String
  FlowLifecycle.[ RegisteredUnconfirmed ]
  FlowContainer.{ HerdrSessionName HerdrServerSocketPath HerdrServerProcessIdentity MetaFlowOwnerId }
  FlowBinding.{ FlowId Aspect PowerLevel ModelName HarnessKind NativeSessionId HerdrWorkspaceId HerdrPaneId HerdrTabId HerdrTerminalId HerdrAgentName ProcessIdentity WorkingDirectory }
  MetaBindExisting.{ FlowContainer Vector<FlowBinding> }
  BoundFlowBinding.{ FlowId FlowLifecycle }
  FlowBindingRefusalReason.[ AmbiguousPane DeadProcess DuplicateFlowId AnatomyMismatch PaneAbsent ProcessMismatch SessionMismatch SessionUnreported SessionUnproven HerdrUnreadable ]
  RefusedFlowBinding.{ FlowId FlowBindingRefusalReason }
  FlowBindingResult.[ Bound.BoundFlowBinding
                      Refused.RefusedFlowBinding ]
  BoundExisting.{ FlowContainer Vector<FlowBindingResult> }
  BindExistingRejection.[ ContainerUnavailable ContainerIdentityMismatch StoreRefused ]
  RetireRejection.[ UnknownFlow AlreadyGone StoreRefused ]
  DeliveryId.String
  MessageId.String
  CommandLine.String
  ByteOffset.Integer
  Sender.[ Flow.FlowId
           Owner ]
  PsycheContext.String
  PsycheVerbatim.String
  Content.[ Text.String
            Psyche.{ PsycheContext PsycheVerbatim } ]
  Letter.{ MessageId Sender Content }
  Message.[ HardAbrupt.Letter
            MiddleAbrupt.Letter
            Soft.Letter ]
  DeliveryRequest.{ DeliveryId FlowId Message }
  InterruptWitness.[ NotRequested Observed Unobserved ]
  DeliveryGrade.[ Transported Presented Uncertain ]
  Delivery.{ DeliveryId FlowId InterruptWitness DeliveryGrade }
  BodyRefusal.[ EmptyBody
                HarnessCommand.CommandLine
                ControlCharacter.ByteOffset ]
  DeliveryRejection.[ UnknownFlow
                      FlowStopped
                      RouteUnavailable
                      RecipientWorking
                      RecipientBlocked
                      ComposerOccupied
                      BodyRefused.BodyRefusal
                      NotDelivered
                      PersistenceRefused
                      FlowRetired
                      FlowExited ]
  HarnessCommand.[ Compact Interrupt ]
  CommandRequest.{ FlowId HarnessCommand }
  CommandGrade.[ Transported Observed Uncertain ]
  CommandOutcome.{ FlowId HarnessCommand CommandGrade }
  CommandRejection.[ UnknownFlow FlowStopped RouteUnavailable RecipientBlocked UnsupportedForHarness NotDelivered FlowRetired FlowExited ]
  MetaRefusal.[ PeerUnknown
                PeerNotAuthorized.Caller ]
  Refusal.[ Store.String ]
  ]
```

```sh
flow-meta 'Configure.Thresholds.[ { Secondary 128000 200000 } ]'
# -> Configured.Replaced
flow-meta 'Configuration'
# -> Configuration.{ { … } [ { Primary claude-fable-5-1 } … ] [] [ … ] }
```

The running Nexus answered `Configuration` on 2026-10-17 with an empty
threshold vector, the third position: no layer has a number.
`Handover` is stored and read nowhere in Flow. `Refresh` is read by
`refresh_threshold` and used only by the wake plan.

## Measuring

Only Claude flows are measured, once, when the Stop report arrives
(`crates/flow-nexus/src/claude.rs`): the last main-thread usage entry of
the transcript, its input, cache-read and cache-write tokens added.

```rust
let usage = entry.get("message")?.get("usage")?;
let tokens = |key: &str| usage.get(key).and_then(Value::as_i64).unwrap_or(0);
usage.get("input_tokens")?;
Some(tokens("input_tokens") + tokens("cache_read_input_tokens") + tokens("cache_creation_input_tokens"))
```

`record_context_at_stop` returns at once for a Codex flow, so a Codex
flow has no recorded size.

## Resume or fresh

`crates/flow-nexus/src/waking.rs`:

```rust
fn resumes(context_tokens: Option<i64>, refresh_threshold: Option<i64>) -> bool {
    match (context_tokens, refresh_threshold) {
        (Some(tokens), Some(threshold)) => tokens < threshold,
        _ => true,
    }
}
```

The wake plan resumes only a Claude flow that can be resumed, is not
marked fresh, and `resumes`; otherwise it launches fresh from the module
identities and leave-outs of the metaflow's last launch. With no
threshold configured, every resumable Claude flow resumes.

`Refresh.Address` marks one asleep metaflow so its next wake is fresh:

```sh
flow-meta 'Refresh.{ Psyche core Secondary }'
# -> Refreshed.{ Psyche core Secondary }
# or RefreshRejected.[ Unknown Awake Ended NoLaunchProfile StoreRefused ]
```

An awake metaflow is refused. Nothing tells a flow it is near a
threshold, and nothing asks it for a handover.

## Primary's Stop-hook program

`tools/context-refresh-hook.mjs` reads one native Stop JSON object,
measures the session through `tools/field-census`, and compares it with
`config/context-refresh.json`:

```json
{ "version": 1, "warningWindowFraction": 0.5,
  "claude": { "warningTokens": 200000 },
  "codex": { "models": { "gpt-6.1-sol": 373000, "gpt-6-astra": 272000,
                         "gpt-6-sol": 272000, "gpt-6-luna": 272000 } },
  "recipients": { "field": "Field Core Secondary" } }
```

A Claude session warns at 200,000 tokens; a Codex session at half its
model's window. Over it, the program sends a `ContextRefreshHandover`
JSON body by `hm-send` to Field Core Secondary and to the session's own
flow, once per session, and only for a session listed in the file's
`bindings` (one Psyche Core Primary session today).

```sh
echo '{"session_id":"…","transcript_path":"…"}' | node tools/context-refresh-hook.mjs
```

No Claude settings file in `~/.claude` or Primary's `.claude`, and no
file in CriomOS-home, names it, and its state directory does not exist:
it has not run as a hook.

## The compensation that stands in

field-context `compensation/launch.md`, lines 24 to 28: a flow at or
above its layer's configured refresh threshold receives no further work;
a Fable flow stops receiving work at 15% of its observed window or
100,000 tokens; its secretary has its successor started and the
successor takes its topics from the handover (knowledge-handover).
