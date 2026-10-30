---
description: A book source is made, built or published for the living; load before writing or publishing a book.
dependencies: [vision:book]
---

## The author makes the book

The author makes the book properly and sends the source as made. The builder renders what it is given and enforces nothing; the book is as correct as the author made it. The publisher builds the source and publishes the page.

```sh
bb tools/book-build.clj \
  /abs/book.md out.html \
  --figures /abs/figures
```

## What a source holds

Outside a proposal a source holds only: one `Presentation.{ «title» }` line, one `# title`, unlabelled diagram fences, and modules shown as they stand, each under a level-two heading `## repo › path`. A module shown as it stands is its text at origin main, byte for byte, front matter left out.

A proposal opens with `### Proposal N: title · repo › path`, numbered from 1; a new module ends the heading with `, a new file`, a deleted one with `, a deleted file`. A line moved between modules is one proposal headed `### Proposal N: title · repoA › pathA, and repoB › pathB`, with a level-four heading for each path, the line in red under the first and green under the second. No other level-three heading exists.

## Red and green

Colour comes only from signed lines. In a change every line opens with `- ` (red, removed), `+ ` (green, added) or two spaces (unchanged, shown for place). A removed line is a whole line of the module at origin main; an added line is not. Colour comes from the diff marks alone.

A module line is shown whole. A change to a hard-wrapped paragraph shows every physical line of that paragraph, so each sentence shows whole. A replaced paragraph is diffed as one paragraph: its removal and its addition together, with only the changed words marked.

A code line in a book is at most 52 characters.

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

Every figure in a book is headed by the module it lives in and one of three states: as it stands, proposed added in green, or proposed removed in red.

A figure already in a belief module shows without colour.

An unlabelled fence holds a box-and-arrow sketch and nothing else; each one has its figure, `fig-N.svg` in the figures directory, drawn by the illustrator from the sketch with every box, label and arrow kept. A figure shows how a thing moves, one question per figure, is at most 52 columns wide, and is drawn in the figure grammar of vision-book. Every other fence carries its language: `ethos`, `datom`, `rust`, `sh`, `yaml`, `text`. An `ethos` fence is code that passes ethos-zero's Check, run by the author before the book is sent. A module written in Markdown is shown as rendered text. A book shows belief modules as rendered text and change marks.

## Code in a proposal

Code the proposed lines land is shown in labelled fences, the Datom it reads or writes and the Ethos that types it, run against the source by the author before the book is sent.

## Commented books

A book the living has commented on stays as he saw it; what his comments change goes into the next book. Its redo is a new book at a new link, and the commented one stays as he left it.
