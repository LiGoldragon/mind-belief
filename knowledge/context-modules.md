---
description: The authored context-module kinds, template syntax or loading metadata are needed.
dependencies: []
---

A module's prefix names its kind: `spirit-`, `vision-`, `intent-`,
`knowledge-`, `inquiry-` or `compensation-`.
Psyche owns spirit, vision and intent; these change only on the living's word.
Mind owns knowledge of verified contracts and inquiry methods.
Field owns compensation for behavior the system does not yet provide;
its owners change it without the living's review.
The operation and trial kinds are retired.

{% raw %}
Target-specific text in a flat source uses `{% if claude %}`, `{% if codex %}`, or `{% if pi %}`, with `{% else %}` and `{% endif %}` alone on their lines; every other character is literal context-module content.
{% endraw %}

`user-only: true` — the context module enters only through the user prompt or a
launcher's first turn; the flow cannot load it. It deploys as
`disable-model-invocation: true` in Claude Code, and in Codex as a policy
sidecar beside the on-demand skill that withholds it from the skills catalog.

A role context module carries an aspect's identity and names its
dependencies. Mark role context modules user-only.

A context module's reasoning and concepts live in a parallel rationale
context module, loaded by psyche-facing flows only.
