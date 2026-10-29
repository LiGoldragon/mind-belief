---
description: Obsidian Sync, its plans, price, encryption, the headless client obsidian-headless, or the Obsidian CLI is needed.
---

Witnessed 2026-10-29 by fetching each URL.

Obsidian Sync Standard: 1 synced vault, 5 MB maximum file, 1 GB total storage, 1 month version history. Sync Plus: 10 vaults, 200 MB maximum file, 10 GB expandable to 100 GB, 12 months version history. Both: unlimited devices, shared vaults. Storage is account-wide, covering vaults, history and attachments. https://obsidian.md/help/sync/plans

Price per user: Standard $4/month billed yearly or $5 billed monthly; Plus $8 yearly or $10 monthly. https://obsidian.md/sync and https://obsidian.md/pricing

Sync platforms: Mac, Windows, Linux, iOS, Android; headless use on a server. https://obsidian.md/sync

Encryption: end-to-end encryption is the default; AES-256 in Galois/Counter Mode with scrypt key derivation. Standard encryption uses a key managed by Obsidian. Local vaults are not encrypted by Obsidian. https://obsidian.md/help/sync/security

## obsidian-headless

The changelog of 2026-02-27 says "Obsidian Sync now supports headless operation using the obsidian-headless client." https://obsidian.md/changelog/2026-02-27-sync

It is in open beta, needs an active Sync subscription, and is installed with `npm install -g obsidian-headless`. https://obsidian.md/help/sync/headless

The npm package `obsidian-headless` is at 0.0.14, published 2026-07-30, license field `UNLICENSED`, engines node `>=22.0.0` (`npm view obsidian-headless version time.0.0.14 license engines`, 2026-10-29). The repository README requires Node.js 22 or later, names the client "Headless client for Obsidian Sync and Obsidian Publish", and lists no license. https://github.com/obsidianmd/obsidian-headless

Sync commands (help page, as listed):

    ob login
    ob sync-list-remote
    ob sync-list-local
    ob sync-create-remote --name "Vault Name" [--encryption <standard|e2ee>] [--password <password>] [--region <region>]
    ob sync-setup --vault <id-or-name> [--path <local-path>] [--password <password>] [--device-name <name>] [--config-dir <name>]
    ob sync [--path <local-path>] [--continuous]
    ob sync-config [--path <local-path>] [--mode <mode>] [--conflict-strategy <strategy>] [--file-types <types>] [--configs <categories>] [--excluded-folders <folders>] [--device-name <name>] [--config-dir <name>]
    ob sync-status [--path <local-path>]
    ob sync-unlink [--path <local-path>]

Modes: `bidirectional` (default), `pull-only` (downloads, ignores local changes), `mirror-remote` (downloads, reverts local changes). Conflict strategy: `merge` or `conflict`; the page does not say how they differ.

The page states that running the desktop app's Sync and Headless Sync on the same device can cause data conflicts, and to use one sync method per device.

README: `--json` is accepted by most commands; for end-to-end encrypted vaults `--password` is required with `--json`; `ob sync-unlink` removes stored credentials. The same README lists Publish commands (`ob publish-list-sites`, `ob publish-create-site`, `ob publish-setup`, `ob publish`, `ob publish-config`, `ob publish-site-options`, `ob publish-unlink`). https://github.com/obsidianmd/obsidian-headless

## Obsidian CLI

It needs the desktop app: it connects to the running instance and launches the app if it is not open. It requires installer 1.12.7 or later and is enabled in Settings, General, Command line interface. Example: `obsidian search query="meeting notes"`. https://obsidian.md/help/cli

The help page states Obsidian 1.12 installer and 1.12.7 or later; it does not state the version in which the CLI first appeared (a second report says 1.12.4; not witnessed here). Its command groups include Files and folders, Search, Properties, Bases, File history, Sync, Publish, Developer commands.

## Local REST API plugin (third party)

`obsidian-local-rest-api` 5.5.2, author Adam Coddington; its manifest.json states `minAppVersion` 1.13.1 and `isDesktopOnly: true`; the latest GitHub release is dated 2026-10-17. The README states HTTPS at `https://127.0.0.1:27124`, optional plain HTTP on 27123, API-key authentication, read/create/update/delete of vault files, patching of headings, block references and frontmatter keys, search, event streams, command execution, and a built-in MCP server at `/mcp/`. https://github.com/coddingtonbear/obsidian-local-rest-api and https://raw.githubusercontent.com/coddingtonbear/obsidian-local-rest-api/main/manifest.json
