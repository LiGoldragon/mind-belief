# Belief module inventory

Observed 2026-10-14. This snapshot covers regular `skills/*.md` files in the
three checked-out worktrees, including tracked, modified, and untracked files;
deleted files and generated trees are excluded. It is not a post-landing
count. Psyche's current `vision/ethos.md` loader input is included because the
registry indexes it; no other current authored Markdown lies outside these
roots.

Counts: Psyche 41, Mind 45, Field 50, total 136.

Snapshot base revisions: Psyche
`bf03117b424413cea4c3df7cf76a279127c8567d`, Mind
`344f6c3669d3d882f96f63ed435022a3cfed2bf4`, and Field
`5070467dd8b596246c47e9cbcbf55415025483fc`. Mind and Field also had dirty
or untracked worktree state when measured. The exact dirty contents are not
pinned or reconstructible from those base revisions; the rows below measure
the files present in those worktrees on the observation date.

All measurements use GNU `wc`: bytes `wc -c`, newline lines `wc -l`, and
`LC_ALL=C wc -w` whitespace words. Frontmatter is included. Words are not
tokens; no supported tokenizer was available.

| Repository | Module | Bytes | Lines | Words |
| --- | --- | ---: | ---: | ---: |
| psyche-context | intent-anatomy.md | 297 | 10 | 50 |
| psyche-context | intent-belief-modules.md | 256 | 8 | 43 |
| psyche-context | intent-context.md | 288 | 9 | 53 |
| psyche-context | intent-conversion.md | 372 | 11 | 69 |
| psyche-context | intent-data.md | 559 | 12 | 95 |
| psyche-context | intent-design.md | 311 | 6 | 55 |
| psyche-context | intent-main-flow.md | 2245 | 23 | 388 |
| psyche-context | intent-mandatory-traits.md | 767 | 18 | 123 |
| psyche-context | intent-models.md | 748 | 18 | 134 |
| psyche-context | intent-protos-parsing.md | 614 | 13 | 100 |
| psyche-context | intent-psyche-interaction.md | 566 | 12 | 96 |
| psyche-context | intent-psyche.md | 1514 | 22 | 260 |
| psyche-context | intent-startup-prompt.md | 614 | 8 | 112 |
| psyche-context | intent-testing.md | 495 | 12 | 88 |
| psyche-context | spirit-core.md | 1806 | 33 | 280 |
| psyche-context | vision-archive-ethos-monolith.md | 1998 | 53 | 320 |
| psyche-context | vision-aspects.md | 694 | 12 | 117 |
| psyche-context | vision-book.md | 1345 | 14 | 251 |
| psyche-context | vision-committing.md | 431 | 12 | 77 |
| psyche-context | vision-belief-modules.md | 2170 | 57 | 231 |
| psyche-context | vision-crystallization.md | 1534 | 44 | 244 |
| psyche-context | vision-datom.md | 15541 | 318 | 2565 |
| psyche-context | vision-deployment.md | 420 | 14 | 82 |
| psyche-context | vision-design.md | 486 | 8 | 85 |
| psyche-context | vision-flow.md | 6594 | 86 | 1142 |
| psyche-context | vision-high-level-view.md | 312 | 13 | 54 |
| psyche-context | vision-horizon.md | 666 | 18 | 115 |
| psyche-context | vision-meaning.md | 3567 | 83 | 629 |
| psyche-context | vision-messaging.md | 1474 | 33 | 241 |
| psyche-context | vision-model-roles.md | 2952 | 69 | 489 |
| psyche-context | vision-nexus.md | 10122 | 197 | 1590 |
| psyche-context | vision-orchestrate.md | 441 | 15 | 65 |
| psyche-context | vision-persona.md | 748 | 12 | 136 |
| psyche-context | vision-protos.md | 6801 | 153 | 1098 |
| psyche-context | vision-psyche.md | 1465 | 27 | 203 |
| psyche-context | vision-remembering.md | 729 | 20 | 129 |
| psyche-context | vision-sema.md | 654 | 18 | 90 |
| psyche-context | vision-signal.md | 1253 | 46 | 189 |
| psyche-context | vision-system-one.md | 305 | 8 | 53 |
| psyche-context | vision-x11.md | 177 | 6 | 20 |
| psyche-context | vision/ethos.md | 20262 | 494 | 2799 |
| mind-context | knowledge-claude-harness.md | 3962 | 76 | 600 |
| mind-context | knowledge-codex-harness.md | 3374 | 65 | 501 |
| mind-context | knowledge-codex.md | 2319 | 37 | 292 |
| mind-context | knowledge-context-strata.md | 1339 | 31 | 213 |
| mind-context | knowledge-datom.md | 6495 | 106 | 1019 |
| mind-context | knowledge-ethos.md | 4190 | 26 | 632 |
| mind-context | knowledge-flow.md | 3586 | 68 | 378 |
| mind-context | knowledge-layer-models.md | 3257 | 21 | 466 |
| mind-context | knowledge-nexus.md | 1383 | 15 | 173 |
| mind-context | knowledge-protos.md | 4836 | 86 | 788 |
| mind-context | knowledge-psyche.md | 3944 | 78 | 630 |
| mind-context | knowledge-vocabulary.md | 1795 | 41 | 295 |
| mind-context | knowledge-yt-dlp.md | 1210 | 23 | 160 |
| mind-context | operation-agent-harness-packaging.md | 1062 | 18 | 146 |
| mind-context | operation-beads.md | 3188 | 54 | 460 |
| mind-context | operation-book.md | 1420 | 24 | 215 |
| mind-context | operation-clojure-development.md | 338 | 10 | 48 |
| mind-context | operation-design.md | 791 | 16 | 118 |
| mind-context | operation-disk-hygiene.md | 232 | 8 | 33 |
| mind-context | operation-documentation-placement.md | 972 | 17 | 146 |
| mind-context | operation-edit-coordination.md | 629 | 12 | 109 |
| mind-context | operation-feature-development.md | 197 | 6 | 28 |
| mind-context | operation-file-editing.md | 1228 | 26 | 195 |
| mind-context | operation-flashbook-illustration.md | 1404 | 12 | 240 |
| mind-context | operation-flashbook.md | 2639 | 36 | 421 |
| mind-context | operation-flow-evidence.md | 713 | 11 | 103 |
| mind-context | operation-lojix.md | 10997 | 383 | 1462 |
| mind-context | operation-main-flow.md | 5354 | 51 | 854 |
| mind-context | operation-nix-input-upgrade.md | 2392 | 29 | 349 |
| mind-context | operation-nix-workflow.md | 1105 | 19 | 169 |
| mind-context | operation-operating-system.md | 834 | 14 | 115 |
| mind-context | operation-orchestrate.md | 1710 | 32 | 235 |
| mind-context | operation-prompt-crafting.md | 657 | 10 | 106 |
| mind-context | operation-psyche-acquisition.md | 520 | 15 | 78 |
| mind-context | operation-psyche-distillation.md | 3204 | 49 | 511 |
| mind-context | operation-psyche-grasp.md | 790 | 16 | 111 |
| mind-context | operation-psyche-interraction.md | 6838 | 100 | 1134 |
| mind-context | operation-realization.md | 370 | 10 | 50 |
| mind-context | operation-relaying-the-living.md | 363 | 10 | 59 |
| mind-context | operation-repository-lifecycle.md | 598 | 14 | 90 |
| mind-context | operation-secrets.md | 842 | 15 | 115 |
| mind-context | operation-skill-designing.md | 5032 | 73 | 853 |
| mind-context | operation-stale-lock.md | 639 | 6 | 105 |
| mind-context | operation-testing.md | 1111 | 24 | 190 |
| mind-context | operation-transcript-search.md | 683 | 12 | 111 |
| field-context | compensation-agent-harness-packaging.md | 1065 | 18 | 146 |
| field-context | compensation-behavior.md | 1412 | 26 | 258 |
| field-context | compensation-book-crystallization.md | 1854 | 18 | 323 |
| field-context | compensation-book.md | 1403 | 24 | 211 |
| field-context | compensation-breaking-upgrades.md | 324 | 8 | 40 |
| field-context | compensation-clojure-development.md | 338 | 10 | 48 |
| field-context | compensation-correction.md | 788 | 16 | 145 |
| field-context | compensation-default-effort.md | 525 | 15 | 77 |
| field-context | compensation-design.md | 1017 | 25 | 162 |
| field-context | compensation-disk-hygiene.md | 232 | 8 | 33 |
| field-context | compensation-documentation-placement.md | 972 | 17 | 146 |
| field-context | compensation-edit-coordination.md | 629 | 12 | 109 |
| field-context | compensation-feature-development.md | 197 | 6 | 28 |
| field-context | compensation-file-editing.md | 525 | 14 | 83 |
| field-context | compensation-flashbook-illustration.md | 1404 | 12 | 240 |
| field-context | compensation-flashbook.md | 2637 | 36 | 419 |
| field-context | compensation-flow-evidence.md | 547 | 10 | 78 |
| field-context | compensation-independent-review.md | 207 | 6 | 33 |
| field-context | compensation-launch.md | 2744 | 40 | 452 |
| field-context | compensation-low-power.md | 155 | 6 | 25 |
| field-context | compensation-main-flow.md | 5527 | 51 | 884 |
| field-context | compensation-messenger-clj.md | 3698 | 20 | 555 |
| field-context | compensation-nix-rationale.md | 2779 | 18 | 392 |
| field-context | compensation-nix-workflow.md | 1105 | 19 | 169 |
| field-context | compensation-nix.md | 3257 | 52 | 426 |
| field-context | compensation-operating-system.md | 824 | 14 | 115 |
| field-context | compensation-orders.md | 1023 | 20 | 178 |
| field-context | compensation-presentation-book.md | 621 | 10 | 88 |
| field-context | compensation-primary-commit.md | 1314 | 10 | 195 |
| field-context | compensation-prompt-crafting.md | 468 | 9 | 75 |
| field-context | compensation-prose.md | 820 | 19 | 136 |
| field-context | compensation-psyche-design.md | 800 | 16 | 118 |
| field-context | compensation-psyche-injection.md | 252 | 6 | 37 |
| field-context | compensation-psyche-interraction.md | 6951 | 100 | 1153 |
| field-context | compensation-questions-book.md | 175 | 6 | 21 |
| field-context | compensation-realization.md | 379 | 10 | 50 |
| field-context | compensation-reaping.md | 206 | 6 | 32 |
| field-context | compensation-relaying-the-living.md | 569 | 12 | 95 |
| field-context | compensation-repository-lifecycle.md | 615 | 14 | 92 |
| field-context | compensation-secrets.md | 842 | 15 | 115 |
| field-context | compensation-skill-designing.md | 3126 | 48 | 520 |
| field-context | compensation-stale-lock.md | 816 | 6 | 134 |
| field-context | compensation-subflow.md | 149 | 6 | 25 |
| field-context | compensation-temporary.md | 476 | 10 | 78 |
| field-context | compensation-testing.md | 1862 | 39 | 299 |
| field-context | compensation-truth.md | 484 | 13 | 79 |
| field-context | compensation-unblocking-commands.md | 618 | 9 | 98 |
| field-context | compensation-understanding.md | 564 | 15 | 89 |
| field-context | compensation-update.md | 2164 | 26 | 307 |
| field-context | compensation-versioning.md | 256 | 7 | 39 |

## Summary

| Repository | Modules | Bytes | Lines | Words |
| --- | ---: | ---: | ---: | ---: |
| psyche-context | 41 | 94593 | 2045 | 14960 |
| mind-context | 45 | 100542 | 1805 | 15106 |
| field-context | 50 | 61715 | 933 | 9650 |

Word percentiles, nearest rank: Psyche min 20, median 123, p90 1098, max
2799; Mind min 28, median 195, p90 853, max 1462; Field min 21, median
115, p90 426, max 1153.
