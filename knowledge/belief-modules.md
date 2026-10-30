---
description: The authored belief-module kinds, template syntax or loading metadata are needed.
dependencies: []
---

A module's prefix names its kind: `spirit-`, `vision-`, `intent-` or `knowledge-`.
Psyche owns spirit, vision and intent; these change only on the living's word.
Mind owns knowledge of verified contracts.
The operation, trial and compensation kinds are retired.

{% raw %}
Target-specific text in a flat source uses `{% if claude %}`, `{% if codex %}`, or `{% if pi %}`, with `{% else %}` and `{% endif %}` alone on their lines; every other character is literal belief-module content.
{% endraw %}

`user-only: true` — the belief module enters only through the user prompt or a
launcher's first turn; the flow cannot load it. It deploys as
`disable-model-invocation: true` in Claude Code, and in Codex as a policy
sidecar beside the on-demand skill that withholds it from the skills catalog.

A role belief module carries an aspect's identity and names its
dependencies. Mark role belief modules user-only.

A belief module's reasoning and concepts live in a parallel rationale
belief module, loaded by psyche-facing flows only.
