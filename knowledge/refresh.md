---
description: Model thresholds, context measurement and fresh wakes in Flow 0.37.1.
dependencies: [vision-flow-nexus, knowledge-flow-nexus]
---

Source: Flow 0.37.1, `fc53f4f`, `crates/flow-nexus/src/store/context.rs`, `waking.rs`, `claude.rs` and `delivery.rs`.

Refresh thresholds are selected by model. The Flow Nexus obtains a flow's model from its stored role, or otherwise from its launch attempt. Its threshold standing distinguishes no configured threshold, no measured context, below threshold, and at or above threshold. Missing configuration or measurement does not establish that a flow is below threshold.

At Stop, the Flow Nexus measures Claude's last main-thread usage entry: `input_tokens + cache_read_input_tokens + cache_creation_input_tokens`. Sidechain usage rows are excluded. The read begins with the last 4 MiB of the transcript and falls back to the full file if necessary. This Stop measurement does not run for Codex; it does not establish a Codex context-size measurement.

At a native rest, a recorded refresh mark or an at-threshold standing makes the Flow Nexus close the old pane and record the flow stopped. A Claude seat whose background work still makes Herdr report Working is not closed for refresh at that point. Codex rest is determined through its app-server. With no refresh due and no queued request, the seat stays Awake.

A wake starts fresh. If the metaflow has a module declaration, the Flow Nexus composes it; otherwise it uses the last launch's module identities and leave-outs. With neither source it cannot place the wake. The selected wake plan does not resume the previous Claude session and does not request a handover.

The privileged CLI exposes the effective configuration:

```sh
flow-meta 'Configuration'
```

That readback, not a historical example, establishes the selected thresholds. This module supplies no numeric threshold or approved model limit.

The Compact command refuses when there is no threshold, no measurement, or a measurement below the model's threshold. At or above the threshold it may place `/compact`; command transport and observed native effect remain separate grades. These source conditions do not prove a particular native compaction or refresh has happened.
