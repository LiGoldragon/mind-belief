---
description: Commenting or review annotation inside Obsidian notes is needed, native comment syntax or a comment plugin and where its comments are stored.
---

Witnessed 2026-10-29 by fetching each URL.

## Native forms

All are plain text in the .md file; none carries an author or a thread.

- `%% %%`: Obsidian shows it only in Editing view; an unclosed block comment hides the rest of the note in Reading view. https://obsidian.md/help/Editing+and+formatting/Basic+formatting+syntax
- `<!-- -->`: the help gives it as the way to hide text in other apps. Same page.
- Callouts: `[!info]` on the first line of a blockquote; the page names no author or thread. https://obsidian.md/help/callouts
- Footnotes and `==highlight==` are described on the formatting page; the help states no author for either.

## Community plugins (third party)

Storage form is from each plugin page; mobile is the platforms the page lists.

| Plugin | Version | Downloads | Mobile | Storage |
|---|---|---|---|---|
| Comments (jaspersurmont) | 1.0.3 | 3k | yes | inline callout `> [!comment] NAME \| DATE` |
| Inline Review Comments (Deepal Jayasekara) | 4.1.1 | 248 | yes | `%% ... %%` with author names, quoted passages and replies |
| Review Comments (Shota Shirai) | 2.1.1 | about 3k | declared; Android unwitnessed | CriticMarkup `{==passage==}{>>id\|author\|date\|TYPE: comment<<}`; replies are further `{>> <<}` blocks with the same id |
| Relay Comments (Relay.md) | 0.5.1 | about 1k | yes | CriticMarkup in the .md; plugin identities in `data.json` |
| Review & Critic (rohrbachd) | 2.1.1 | about 2k | yes | CriticMarkup-style tokens in the .md |
| Commentator (Fevol) | not stated | not stated | not stated | CriticMarkup; beta, "do not run in your main vault"; author and timestamp annotation is an unchecked roadmap item; MIT |

Sources: https://community.obsidian.md/plugins/comments, https://community.obsidian.md/plugins/inline-review-comment, https://community.obsidian.md/plugins/review-comments, https://community.obsidian.md/plugins/relay-comments, https://community.obsidian.md/plugins/review-critic, https://github.com/Fevol/obsidian-criticmarkup

Comments states that comments are hidden in reading mode and excluded from exports. Inline Review Comments states that agents with access to the note can read the comments and write replies in the same file; agent execution needs desktop.

Other plugins (third-party report, counts from community-plugin-stats.json, not re-witnessed here): Side Comments, sidecar JSON per note, 2,093; SideNote, `data.json`, 9,798; Document Comments, inline `<!--c:ID-->` markers plus a thread block, 6,954; Tandem Comments, JSON fence at note end, 4,158; Sidemark, sidecar `Note.md.review.yaml`, 1,629; Annoteca, HTML-comment markers, 2,965; Margin Comments, JSON in `.margin-comments/`, 233; Enhanced Annotations, inline `<!--label: ...-->`, 18,862. Witness: /home/li/primary/flows/ca3262/reports/obsidian-research.md, table "Comment plugins and where they store comments".

Review Comments example, as the plugin page gives it: `The original {==text==}{>>rc-3f9a2b|shirai|2026-05-13|EDIT: please rewrite<<} has an issue.` Anchor, id, author and date are fields in the .md text. The page lists Desktop and Mobile; ease of use on a phone is not witnessed.

Review Comments 2.1.1 is released at commit `c218093c0363bb18f6d939e29ed7a1ace909be89`; its manifest says `isDesktopOnly: false`, which declares mobile eligibility but does not witness an Android interaction. Its writer emits `{==passage==}{>>rc-xxxxxx|author|date|TYPE: body<<}`, where the id is `rc-` plus exactly six lowercase base-36 characters and an initial type is ASK, EDIT, PRAISE or NOTE. A reply is an adjacent metadata block with the same id and type REPLY. The parser recognizes an id only by `rc-[0-9a-z]{6}`, then requires a non-pipe author, non-pipe date and uppercase type. Selected text and bodies store backslashes doubled and newlines as literal `\n`; selected text containing `{==`, `==}`, `{>>` or `<<}` is refused, and those sequences in a body are altered by inserting a space. The thread parser requires a highlighted block immediately followed by one or more metadata blocks. The source registers editor-command creation, a selection floating bar, live-preview and reading-mode bubbles, and edit, reply and delete actions; it has no Android selection-handle or touch-specific path. The author written into a new comment or reply comes from the plugin's mutable `authorName` setting, default `you`; the writer trims it and replaces `|<>{}=` with underscores. The plugin saves that setting with its other settings in plugin data, and the isolated whole-vault sync copied that data between endpoints. The stored author is therefore a shared label rather than an authenticated or per-device identity. Android selection, taps, popover placement, reply writing and reading-mode mutation have not been run. Sources: https://github.com/ShotaShirai1719/obsidian-review-comments/releases/tag/2.1.1 https://github.com/ShotaShirai1719/obsidian-review-comments/blob/c218093c0363bb18f6d939e29ed7a1ace909be89/manifest.json https://github.com/ShotaShirai1719/obsidian-review-comments/blob/c218093c0363bb18f6d939e29ed7a1ace909be89/src/constants.ts https://github.com/ShotaShirai1719/obsidian-review-comments/blob/c218093c0363bb18f6d939e29ed7a1ace909be89/src/comment-format.ts https://github.com/ShotaShirai1719/obsidian-review-comments/blob/c218093c0363bb18f6d939e29ed7a1ace909be89/src/settings.ts https://github.com/ShotaShirai1719/obsidian-review-comments/blob/c218093c0363bb18f6d939e29ed7a1ace909be89/src/main.ts https://github.com/ShotaShirai1719/obsidian-review-comments/blob/c218093c0363bb18f6d939e29ed7a1ace909be89/src/floating-bar.ts https://github.com/ShotaShirai1719/obsidian-review-comments/blob/c218093c0363bb18f6d939e29ed7a1ace909be89/src/rendering.ts

An executable bundle of the released parser serialized and reparsed a multiline callout passage, a same-id reply and delimiter escaping. In the isolated Obsidian 1.14.5 runtime, however, the released plugin loaded after vault trust but left a valid thread literal in Reading view in both a normal paragraph and a callout, and in Live Preview in a callout. Obsidian split the native highlight into a text node, a `<mark>` node and another text node; the released Reading postprocessor accepts only a complete childless block or a complete thread in one text node. This witnesses an incompatibility for the tested renderer path, distinct from the raw parser. Android behavior remains unwitnessed. Witnesses: `/home/li/primary/flows/280282/research/sync-acceptance.md`, SHA-256 `e4cb42a39d46957448b8b1ce84bf77c4d8ff22e48b5342a1bc2a92c93c325ba7`; `/home/li/primary/flows/280282/research/callout-acceptance.md`, SHA-256 `51e7791d88bc790b69c13eebaf526392b9d5b535d39b8c3b64bfbb839a4080cb`.
