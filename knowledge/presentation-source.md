---
description: What a presentation source holds; load before writing a proposal, a review or an account for the living.
dependencies: [vision-presentation, vision-proposal, vision-review]
---

## The author makes the source

The author makes the source properly and hands it as made; the builder enforces nothing.

## What a source holds

Outside a proposal a source holds only: one `Presentation.{ «title» }` line, one `# title`, `mermaid` fences, and modules shown as they stand, each under a level-two heading `## repo › path`. A module shown as it stands is its text at origin main, front matter left out.

A proposal opens with `### Proposal N: title · repo › path`, numbered from 1; a new module ends the heading with `, a new file`, a deleted one with `, a deleted file`. Lines moved between modules are one proposal headed `### Proposal N: title · repoA › pathA, and repoB › pathB`, the moved lines shown once, in the move colour, in a move container. No other level-three heading exists.

```text
::: move proposed
from: repoA › pathA
to: repoB › pathB

the moved lines, as they stand
:::
```

The container's state is `proposed` or `landed`; `landed` shows the dark shade.

## An account

An account's source is prose: the `Presentation.{ «title» }` line, the `# title`, then paragraphs under level-two headings of its own, with `mermaid` fences and labelled code fences where the account needs them; it shows no module and lands nothing. The gist is its first paragraph. Where a vision proposal truly arises in it, that part is a `### Proposal N: title · repo › path` section as any proposal has, and only that part is marked.

## Change marks

In a change every line opens with `- ` (red, removed), `+ ` (green, added) or two spaces (unchanged, shown for place). Colour comes from these marks and the move container alone. Inside a line, `[-removed-]` and `[+added+]` mark changed words.

A module line is shown whole. A change to a hard-wrapped paragraph shows every physical line of that paragraph, so each sentence shows whole. A replaced paragraph is diffed as one paragraph: its removal and its addition together, with only the changed words marked.

```text
### Proposal 1: A sender · psyche › messaging.md

**Comment** Flow names the sender.

  ## A message is a datom

- The body is a datom.
+ The body is a datom; Flow names it.
```

## Marks inside a proposal

Inside a proposal a source holds only its change lines, one Comment, its Alternatives, its Destroy or Archive mark, path headings at level four, `#### repo › path`, as the moved-line form has them, and code that the proposed lines themselves land.

Every fence inside a proposal is signed line by line: red, green, or two spaces for a line kept in place, code-file proposals included, because code shown in a proposal is either what stands at origin main or what is proposed.

One `**Comment**` paragraph at most, before every change: the machine's word, in its own colour. `**Alternative 1**`, `**Alternative 2**` and on, two or more, in order, each alone on its line and followed by the exact lines it lands. `**Destroy**` or `**Archive**` opening a paragraph marks a deleted module or record. Prose stands as its own paragraph, a blank line apart from any change.

## Figures and fences

Every figure is headed by the module it lives in and one of three states: as it stands, proposed added, or proposed removed. A figure already in a belief module shows without colour.

A flowchart is a `mermaid` fence, at most 52 columns wide. Every other fence carries its language: `ethos`, `datom`, `rust`, `sh`, `yaml`, `text`. An `ethos` fence passes ethos-zero's Check, run by the author before the source is handed over. A code line is at most 52 characters.

## Code in a proposal

Code the proposed lines land is shown in labelled fences, the Datom it reads or writes and the Ethos that types it.
