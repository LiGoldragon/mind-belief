---
description: A book's source, figures and publication.
dependencies: [vision-presentation, vision-proposal]
---

## Duties

The author writes the complete source and names its path to the bookmaker. The bookmaker has the Illustrator draw each figure as a vector graphic, builds the page with the repository builder, checks the whole built page and every figure in it, publishes it, and answers the author with its title and link. Only the bookmaker publishes. A source that fails the builder's check is the bookmaker's to fix: headings, signs, context lines, the proposal form, and a Mermaid fence among removed lines, which is rendered as removed lines and never drawn. The bookmaker changes no proposed wording; a source whose content is wrong returns to the author with the fault named. A redo replaces the same edition and resolves the comment threads the source answers.

## Source anatomy

The source begins with its Presentation line and its title. A module view is headed `## repo › path`; a proposal is headed `### Proposal N: title · repo › path`. The builder's documentation and checker hold the rest of the grammar.

One example of a line added, a line removed and a passage moved:

```text
- Removed line
+ Added line
::: move proposed
from: repo › old.md
to: repo › new.md

Moved passage, written once.
:::
```
