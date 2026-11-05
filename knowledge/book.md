---
description: How a book reaches the living: what its source holds, who publishes it, and how it is built.
dependencies: [vision-presentation, vision-proposal, vision-review]
---

## Who does what

The author writes the source and hands its path to the bookmaker, the flow whose role is publishing; the bookmaker builds the page, publishes it and answers with the title and the link; the author gives the living the title and the link, in one line. A redo is the same source path handed again: the bookmaker replaces the edition and resolves the comment threads the source answers. Nobody but the bookmaker publishes. The bookmaker's address is the roster's; how a flow sends to it is knowledge:flow-messaging's.

## What a source holds

The author makes the source properly and hands it as made; the builder enforces nothing.

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

An account's source is prose: the `Presentation.{ «title» }` line, the `# title`, then paragraphs under level-two headings of its own, with `mermaid` fences and labelled code fences where the account needs them; it shows no module and lands nothing. The gist is its first paragraph. Where a vision proposal truly arises in it, that part is a `### Proposal N: title · repo › path` section as any proposal has, and only that part is marked.

In a change every line opens with `- ` (red, removed), `+ ` (green, added) or two spaces (unchanged, shown for place). Colour comes from these marks and the move container alone. Inside a line, `[-removed-]` and `[+added+]` mark changed words. A module line is shown whole. A change to a hard-wrapped paragraph shows every physical line of that paragraph, so each sentence shows whole. A replaced paragraph is diffed as one paragraph: its removal and its addition together, with only the changed words marked.

```text
### Proposal 1: A sender · psyche › messaging.md

**Comment** Flow names the sender.

  ## A message is a datom

- The body is a datom.
+ The body is a datom; Flow names it.
```

Inside a proposal a source holds only its change lines, one Comment, its Alternatives, its Destroy or Archive mark, path headings at level four, `#### repo › path`, as the moved-line form has them, and code that the proposed lines themselves land. Every fence inside a proposal is signed line by line: red, green, or two spaces for a line kept in place, code-file proposals included, because code shown in a proposal is either what stands at origin main or what is proposed. One `**Comment**` paragraph at most, before every change: the machine's word, in its own colour. `**Alternative 1**`, `**Alternative 2**` and on, two or more, in order, each alone on its line and followed by the exact lines it lands. `**Destroy**` or `**Archive**` opening a paragraph marks a deleted module or record. Prose stands as its own paragraph, a blank line apart from any change.

Every figure is headed by the module it lives in and one of three states: as it stands, proposed added, or proposed removed. A figure already in a belief module shows without colour. A flowchart is a `mermaid` fence, at most 52 columns wide. Every other fence carries its language: `ethos`, `datom`, `rust`, `sh`, `yaml`, `text`. An `ethos` fence passes ethos-zero's Check, run by the author before the source is handed over. A code line is at most 52 characters. Code the proposed lines land is shown in labelled fences, the Datom it reads or writes and the Ethos that types it.

## Building

The bookmaker builds the source it is handed and publishes the page. The builder renders what it is given and enforces nothing.

```sh
bb /git/github.com/LiGoldragon/makeshift-tools/book-build.clj \
  /abs/book.md out.html \
  --figures /abs/figures
```

Each `mermaid` fence is drawn by the illustrator, never run through a diagram renderer: it becomes a custom vector graphic, `fig-N.svg` in the figures directory, with every box, label and arrow kept. It runs vertically, a narrow column reading top to bottom that fits a phone without sideways scrolling; a chart that would sprawl sideways is restacked. Nothing is cut off: every box is sized to its text, and a long label wraps inside its box. Colour tells kinds of thing or flow apart, line thickness marks what matters most, dashing, box weight and grouping show structure.
