---
description: A book's source, figures and publication.
dependencies: [vision-presentation, vision-proposal]
---

## Duties

The author writes the complete source and names its path to the bookmaker. The bookmaker has the Illustrator draw each figure as a vector graphic, builds the page with the repository builder, checks the whole built page and every figure in it, publishes it, and Sends its title and link through flow to the flow that ordered the book. Only the bookmaker publishes. A source that fails the builder's check is the bookmaker's to fix: headings, signs, context lines, the proposal form, and a Mermaid fence among removed lines, which is rendered as removed lines and never drawn. The bookmaker changes no proposed wording; a source whose content is wrong returns to the author with the fault named. A redo replaces the same edition and resolves the comment threads the source answers.

## Source anatomy

The source begins with its Presentation line and its title. A module view is headed `## repo › path`; a proposal is headed `### Proposal N: title · repo › path`. The proposal author's own words sit in a `::: comment` container and the page renders them in their own box labelled Why. Unmarked prose in a proposal is module text: the checker accepts it only when the proposal's repository and path resolve to an actual module containing that whole paragraph. Layout whitespace may differ; the words and their paragraph boundary may not. A comment explains a proposal and supplies no module provenance. A `::: shown` container begins with `repo › path`, then carries one exact contiguous excerpt of that source module as it stands. The checker refuses text absent from the named module. The page shows the excerpt in a small module view headed by its source path, with code highlighted in the module's language; its amber box and margin are a fourth colour beside added, removed and moved. An Ethos excerpt is authenticated as source and highlighted as Ethos, rather than checked as a whole Ethos file. An `ethos` fence with at least one `+` or `-` line and every other nonblank line carrying `+`, `-` or two-space context is a fragment: it keeps Ethos highlighting and skips the whole-document Ethos check. Bare blank lines may sit in a fragment; context alone is refused as a change that changes nothing, while an Ethos root at column zero is a whole document and is checked. A Mermaid fence whose every line is marked `+` or whose every line is marked `-` draws the whole figure in a green or red margin respectively; the markers are stripped for drawing, a bare unmarked or oppositely marked line is refused, and the sign alone carries an intentional blank line. The 52-column code limit does not apply inside a Mermaid fence. The builder's documentation and checker hold the rest of the grammar.

One example of a line added, a line removed and a passage moved:

```text
::: comment
The passage moves because the rule belongs with its subject.
:::

::: shown
psyche-belief › vision/book.md
A book carries belief modules, as they stand and as they are proposed to change; its sources live in its reference file.
:::

- Removed line
+ Added line
::: move proposed
from: repo › old.md
to: repo › new.md

Moved passage, written once.
:::
```
