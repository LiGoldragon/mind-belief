---
description: A presentation source is built and published; load before publishing a book.
dependencies: [vision-book]
---

## Building

The publisher builds the source it is handed and publishes the page. The builder renders what it is given and enforces nothing.

```sh
bb /git/github.com/LiGoldragon/makeshift-tools/book-build.clj \
  /abs/book.md out.html \
  --figures /abs/figures
```

## Figures

Each `mermaid` fence is drawn by the illustrator, never run through a diagram renderer: it becomes a custom vector graphic, `fig-N.svg` in the figures directory, with every box, label and arrow kept. It runs vertically, a narrow column reading top to bottom that fits a phone without sideways scrolling; a chart that would sprawl sideways is restacked. Nothing is cut off: every box is sized to its text, and a long label wraps inside its box. Colour tells kinds of thing or flow apart, line thickness marks what matters most, dashing, box weight and grouping show structure.
