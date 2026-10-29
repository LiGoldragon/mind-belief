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
| Review Comments (Shota Shirai) | 2.1.1 | about 3k | yes | CriticMarkup `{==passage==}{>>id\|author\|date\|TYPE: comment<<}`; replies are further `{>> <<}` blocks with the same id |
| Relay Comments (Relay.md) | 0.5.1 | about 1k | yes | CriticMarkup in the .md; plugin identities in `data.json` |
| Review & Critic (rohrbachd) | 2.1.1 | about 2k | yes | CriticMarkup-style tokens in the .md |
| Commentator (Fevol) | not stated | not stated | not stated | CriticMarkup; beta, "do not run in your main vault"; author and timestamp annotation is an unchecked roadmap item; MIT |

Sources: https://community.obsidian.md/plugins/comments, https://community.obsidian.md/plugins/inline-review-comment, https://community.obsidian.md/plugins/review-comments, https://community.obsidian.md/plugins/relay-comments, https://community.obsidian.md/plugins/review-critic, https://github.com/Fevol/obsidian-criticmarkup

Comments states that comments are hidden in reading mode and excluded from exports. Inline Review Comments states that agents with access to the note can read the comments and write replies in the same file; agent execution needs desktop.

Other plugins (third-party report, counts from community-plugin-stats.json, not re-witnessed here): Side Comments, sidecar JSON per note, 2,093; SideNote, `data.json`, 9,798; Document Comments, inline `<!--c:ID-->` markers plus a thread block, 6,954; Tandem Comments, JSON fence at note end, 4,158; Sidemark, sidecar `Note.md.review.yaml`, 1,629; Annoteca, HTML-comment markers, 2,965; Margin Comments, JSON in `.margin-comments/`, 233; Enhanced Annotations, inline `<!--label: ...-->`, 18,862. Witness: /home/li/primary/flows/ca3262/reports/obsidian-research.md, table "Comment plugins and where they store comments".

Review Comments example, as the plugin page gives it: `The original {==text==}{>>rc-3f9a2b|shirai|2026-05-13|EDIT: please rewrite<<} has an issue.` Anchor, id, author and date are fields in the .md text. The page lists Desktop and Mobile; ease of use on a phone is not witnessed.
