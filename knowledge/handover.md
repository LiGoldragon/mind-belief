---
description: What a handover is today, who writes it, and how a successor flow receives it.
dependencies: [vision-flow, knowledge-refresh]
---

A handover today is a Markdown file a flow writes by its own judgment,
`flows/<flow-id>/handover.md` in Primary. Nothing types it, nothing
generates it, and the Flow Nexus neither asks for one nor delivers one.
A successor started by Primary's native launcher receives text in the
`{{handover}}` slot of its first prompt; a successor woken fresh by the
Flow Nexus receives its modules and the queued requests.

Verified on 2026-10-17 against Primary `bda70b5`, Flow `67b80b3`
(0.35.11), meta-signal-flow `a918b7d` and field-context `95121c6`.

## How it flows

```mermaid
flowchart TB
    a["a flow near its limit"] -- "writes by judgment" --> b["flows/<id>/handover.md free Markdown"]
    b -- "is read by" --> c["the secretary, or the successor itself"]
    c -- "starts through" --> d["the native launcher"]
    d -- "fills" --> e["first prompt: {{handover}}"]
    d -- "writes" --> g["continuation.json flowId, predecessor, topic, metaflow"]
    h["the Flow Nexus fresh wake"] -- "hands the new flow" --> i["modules of the last launch and the queued requests; no handover"]
```

## The file

Primary holds 33 `flows/*/handover.md` files on 2026-10-17. Their
sections are chosen by each writer and differ from file to file: among
them the seat, open decisions waiting on the living, judgments to carry,
next bounded work and references. No ethos type and no checker covers
them.

## The first prompt

Configuration is Flow's datom, read with `flow-meta 'Configuration'`. `{{handover}}`,
`{{modules}}` and `{{raw-psyche}}` must be present, and an empty handover is refused:

```clojure
{:first-prompt-template "{{modules}}\n\n# Handover and topic context\n{{handover}}\n\n# Raw psyche records with context\n{{raw-psyche}}\n\n{{topic-context}}\n\n…"}
```

```js
if (!handover?.trim()) throw new Error('first prompt handover or topic context is required');
const values = {modules, handover, 'raw-psyche': sources.join('\n'), 'topic-context': metaflow['topic-context'] ?? '', metaflow: `${metaflow.aspect} ${metaflow.topic} ${metaflow.layer}`};
```

`tools/claude-native-seat-refresh.py` fills the slot from its manifest:
the role, topic, model, effort and predecessor as JSON, then each listed
source file's body.

```python
def role_brief(manifest, sources, effort_observed=True):
    metadata = {key: manifest.get(key) for key in ("role", "topic", "model", "effort", "predecessor")}
    return json.dumps(metadata, ensure_ascii=False) + "\n\n" + "\n\n".join(
        f"## Source: `{item['path']}`\n\n{item['body']}" for item in sources
    )
```

The lineage is written apart, by `tools/native-main-flow-launch-shared.mjs`:

```json
{"flowId":"d68c82","predecessor":null,"topic":"Core","metaflow":"Psyche core Secondary: successor of 445410"}
```

## In the Flow Nexus

`hand_over` in `crates/flow-nexus/src/waking.rs` types queued work into a
live pane; it carries no handover. A fresh wake composes the last
launch's system and user modules again and hands over the queue. The
`Handover` number of `ConfigureThreshold` is read nowhere
(knowledge-refresh).

## The request for a handover

The only program that asks for a handover is
`tools/context-refresh-hook.mjs`, which has not run (knowledge-refresh).
Its body, sent as JSON:

```js
{ kind: 'ContextRefreshHandover',
  instruction: 'The refresh procedure has started. … Write a judgment-only handover of decisions and unresolved reasons, name the context topics to split to existing or new topic flows, and include no facts that tools can look up. …',
  observedTokens, thresholdTokens, measurementQuality, action: 'refresh-started',
  decisions: [], unresolvedReasons: […], contextSplit: {…}, windowTokens }
```

## The compensation that stands in

field-context `compensation/launch.md`, lines 24 to 28: the secretary of
a flow at its threshold orders its successor started at once; the
successor takes its topics from the handover; the predecessor is retired
only after the successor has answered on a supported route.
