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

The meta wire declares them in meta-signal-flow `ethos/signal.ethos`:

```
ConfigureThreshold.{ Layer Handover.Integer Refresh.Integer }
ConfigurationChange.[ Models.Vector<ConfigureModel>
                       Thresholds.Vector<ConfigureThreshold>
                       LeaveOuts.Vector<ConfigureLeaveOut>
                       Nexus.ConfigureNexus ]
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
