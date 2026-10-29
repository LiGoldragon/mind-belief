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
- Raw HTML is allowed. Obsidian's documentation says Markdown inside HTML is unsupported and that blank lines break an HTML block. In an isolated Obsidian 1.14.5 runtime, an inline `<span style="color:green">` containing emphasis, inline code and a link showed green literal Markdown in Live Preview, while Reading view rendered those inline forms within the green span. A multi-line span with blank lines, a heading, a paragraph and a list showed the entire body as one green HTML widget with literal Markdown in Live Preview; Reading view emitted an empty green span and rendered the Markdown as normal-color sibling elements outside it. The corresponding red spans behaved the same. A single Enter is not a line break. https://obsidian.md/help/html
- In that Obsidian 1.14.5 runtime, a fenced `diff` block rendered `+` lines green and `-` lines red in Live Preview and Reading view, while remaining a monospaced code block whose Markdown content is code rather than rendered prose. Witness: `/home/li/primary/flows/280282/research/render.md`, SHA-256 `49d72c3837f1f16df137e1beb31e59422688c6b05f9fc549d0e59daaee289b2f`.
- Native `[!added]` and `[!removed]` callouts preserved rendered headings, lists, links and inline formatting in Live Preview and Reading view in the isolated 1.14.5 runtime; YAML and Markdown fences inside them remained code. A custom property value of `8, 185, 78` or `233, 49, 71` was not a valid color for the shipped callout rules and left the callouts uncolored. Complete values `rgb(8, 185, 78)` and `rgb(233, 49, 71)` produced matching title and icon colors and tinted backgrounds and borders in both views; they did not color all child prose. A fresh desktop profile kept a copied plugin and snippet listed but disabled their execution until the user explicitly trusted the vault, and Mermaid rendering had a separate trust gate. Witness: `/home/li/primary/flows/280282/research/callout-acceptance.md`, SHA-256 `51e7791d88bc790b69c13eebaf526392b9d5b535d39b8c3b64bfbb839a4080cb`.
- Obsidian 1.15 rendering is not runtime-witnessed. On 2026-10-29 the official release manifest named 1.14.5 as stable and 1.15.0 as beta; an unauthenticated GET of the exact beta archive URL returned HTTP 404 with zero bytes. This witnesses the access result alone, not its cause. https://raw.githubusercontent.com/obsidianmd/obsidian-releases/master/desktop-releases.json https://releases.obsidian.md/release/obsidian-1.15.0.asar.gz https://obsidian.md/changelog/2026-10-22-desktop-v1.15.0/
