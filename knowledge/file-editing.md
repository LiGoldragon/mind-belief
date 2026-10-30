---
description: The non-Primary jj publication procedure is needed.
dependencies: []
---

In another repository's shared checkout, under an edit-coordination lock, a commit names only the paths this flow edited: `jj commit -m 'message' path ...`.

Read a baseline from a revision with `git show REV:PATH` or `jj file show -r REV PATH`; build and test from a pushed revision.

The sequence for landing normal non-Primary jj work:

    jj commit -m 'short imperative message'
    jj bookmark set main -r @-
    jj git push --bookmark main

`jj commit` snapshots the working copy. After it, `@-` is that
commit. `jj bookmark set main -r @-` advances main to it. Then
push.
