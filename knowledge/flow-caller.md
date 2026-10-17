---
description: How the production Flow Nexus names the flow that calls it or sends a message, why a flow on the old route is no flow to it, and how one live flow was brought under it.
dependencies: [vision-flow, knowledge-flow, knowledge-flow-seats]
---

Read on 2026-10-17 in Flow `67b80b3` (0.35.11, installed and running)
and its pinned signal-flow `6a49664`.

## How a caller is named

Flow names a caller from the process on the other end of its socket.
It walks up that process's ancestors to the Herdr pane it runs in, and
asks its own store which flow is bound in that pane. Exactly one live
bound flow is the caller; none, or more than one, is no flow. A flow
never states its own id.

```
+--------------------------+
| the calling process      |
+------------+-------------+
             |
             | runs, through its ancestors, in
             v
+--------------------------+
| a Herdr pane             |
+------------+-------------+
             |
             | is looked up in
             v
+--------------------------+
| Flow's store of bound    |
| flows                    |
+------+-------------+-----+
       |             |
  one  |             | none, or
  flow |             | more than one
       v             v
+-------------+ +-------------+
| that flow,  | | no flow:    |
| its id and  | | Unbound, or |
| session     | | CallerUnknown|
+-------------+ +-------------+
```

`crates/flow-nexus/src/caller.rs`:

```rust
impl BindsCallerPane for RunningNexus {
    fn bound_caller(&self, pane: &CallerPane) -> Result<Caller, CallerResolutionRejection> {
        let unknown = |_: StoreError| CallerResolutionRejection::CallerUnknown;
        let mut present = self
            .store
            .flows_in_pane(&pane.herdr_session_name, &pane.herdr_pane_id)
            .map_err(unknown)?
            .into_iter()
            .filter(|node: &FlowNode| self.herdr.pane_presence(node) == PanePresence::Present);
        // No binding, or more than one, names no caller.
        let (Some(node), None) = (present.next(), present.next()) else {
            return Err(CallerResolutionRejection::CallerUnknown);
        };
        self.store
            .role(&node.flow_id)
            .map_err(unknown)?
            .ok_or(CallerResolutionRejection::CallerUnknown)
    }
}
```

What a launch or a message records as its origin is one of two
variants, in signal-flow `ethos/signal.ethos`:

```ethos
Origin.[ Flow.FlowOrigin Unbound ]
Caller.{ FlowId Aspect PowerLevel ModelName }
CallerResolutionRejection.[ CallerUnknown
                            CallerMismatch.Caller ]
```

```sh
flow 'ResolveCaller.None'
# from any process in d68c82's pane, 2026-10-17:
# -> CallerResolved.{ d68c82 Psyche Medium
#      claude-opus-5-5 }
```

## Why an old-route flow is no flow

A flow started before Flow, or by the old launchers, has no binding in
Flow's store, so every process in its pane is no flow. Message asks
Flow to identify the sending process; Flow answers
`Refused.Unidentified`, and `hm-send` prints it as:

```sh
FLOW_ID=d68c82 hm-send "Psyche flow Secondary" \
  --psyches --stdin < psyches.edn
# -> MessageRefused.{ «Psyche flow Secondary»
#      Unidentified }
```

That reply is recorded in
`/home/li/primary/flows/d68c82/receipts/launch-flow-ethos-2026-10-17.md`,
from before d68c82 was adopted.

## Adopting a live flow

Adoption was run once, for d68c82, by Field on 2026-10-17
(`/home/li/private-repos/flow-evidence/42265e/direct-starter-retry-20261017/d68c82-sender-binding/`).
It has two steps. The meta socket imports the live flow's native
binding:

```sh
flow-meta 'MetaBindExisting.{ { «default» «/home/li/.config/herdr/herdr.sock» { 4957 1001 «5988» } «42265e» } [ { «d68c82» Psyche Medium «claude-opus-5-5» Claude  «d68c8272-6db0-47dd-9c8e-538d95ff12a6» «w1» «w1:p33» «w1:t2N» «term_65d7bf0f16c9b65» «psyche_core_secondary_d68c82» { 1960918 1001 «117563436» } «/home/li/primary» } ] }'
# -> BoundExisting.{ { default /home/li/.config/herdr/herdr.sock { 4957 1001 5988 } 42265e } [ Bound.{ d68c82 RegisteredUnconfirmed } ] }
```

Then the address is bound with `Bind`, and the process the `Bind` names
must be the process on the socket, alive. The store refuses anything
else (`crates/flow-nexus/src/store/metaflow.rs`):

```rust
if binding.process != *peer || !FlowStore::process_is_live(peer) {
    return Ok(Response::Refused(Refusal::Unidentified(binding.process)));
}
```

So the `Bind` has to be sent from inside the adopted flow's own process
tree. Field's helper checked that its ancestry reached d68c82's Claude
process, then replaced itself with `flow`, keeping its own process id:

```python
pid=os.getpid();parent,started=process(pid)
query='Bind.{ { Psyche core Secondary } { '+str(pid)+' '+started+' } }'
cli=os.path.realpath(shutil.which('flow'))
os.execv(cli,[cli,query])
```

After it, Flow recorded `{ Psyche core Secondary }` as `Awake.d68c82`,
and d68c82's sends were queued with `Sender.{ Psyche core Secondary }`.

An adopted flow keeps the hooks it was started with. d68c82's settings
file carries only a `UserPromptSubmit` reminder hook, no `flow-hook`,
so it never reports `Stopped` to Flow; knowledge-flow-queue says what
that leaves undelivered.

No flow other than d68c82 has been adopted, and no tool adopts flows
in bulk.
