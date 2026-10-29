---
description: Facts about the Obsidian app itself are needed: license, file format, platforms, packaging in nixpkgs, Publish, or how it renders Markdown, code fences and diagrams.
---

Witnessed 2026-10-29. Marks: [fetched] page read today; [report] taken from /home/li/primary/flows/ca3262/reports/obsidian-research.md, not re-witnessed; [unconfirmed] unconfirmed in that report.

- [fetched] Obsidian is "free for all purposes, including personal, commercial, and non-profit use"; paid Commercial and Catalyst licenses are optional. Commercial license $50 per user per year. https://obsidian.md/license and https://obsidian.md/pricing
- [fetched] Platforms: Mac, Windows, Linux, iOS, Android. https://obsidian.md/sync
- [report] The app is not open source (https://github.com/obsidianmd/obsidian-releases); the plugin API is MIT. Local vaults are plain unencrypted .md files.
- [fetched] Publish costs $8 per site per month billed yearly, $10 monthly. https://obsidian.md/pricing
- [fetched] A forum feature request for a comment section on Publish exists, with no staff reply in the thread. https://forum.obsidian.md/t/comment-section-on-obsidian-publish/11252 Whether Publish has built-in comments is not witnessed here.
- [witnessed by command] `nix eval --raw nixpkgs#obsidian.version` printed `1.13.4` and `nix eval nixpkgs#obsidian.meta.unfree` printed `true` on this host, 2026-10-29. The report states 1.14.5 with `lib.licenses.obsidian`.
- [report] Linux packages: AppImage, deb, snap, community flatpak. Android: Google Play and APK.

Rendering [report]:
- Fenced code with language tags, highlighted by Prism. An unknown language such as ethos or datom falling back to plain code is [unconfirmed].
- The `mermaid` fence is built in. Desktop v1.15.0 (2026-10-22) replaced Mermaid with "Pele", compatible with Mermaid 12.1.0 syntax (https://obsidian.md/changelog/2026-10-22-desktop-v1.15.0).
- Pipe tables; a literal `|` in a cell needs `\|`. MathJax for math.
- SVG and PNG embed with `![[file]]` or `![](url)`; relative-path and SVG specifics are [unconfirmed].
- Raw HTML is allowed; Markdown inside HTML is not rendered. A single Enter is not a line break.
