---
description: Syncing an Obsidian vault without Obsidian Sync is needed: Self-hosted LiveSync, Remotely Save, Obsidian Git or Syncthing.
---

Witnessed 2026-10-29 by fetching each URL. All four are third-party.

**Self-hosted LiveSync** (vrtmrz, MIT). Backends: a CouchDB-compatible server, S3-compatible object storage, and peer-to-peer WebRTC, which still needs a signalling relay for peer discovery. The README says it is available on all Obsidian-compatible platforms and that 1.0 requires Obsidian 1.7.2 or later. The README's status-bar legend mentions "Chunks and Metadata"; its server storage format is not described there. Release 1.0.42 is marked Latest, dated 27 October 2026; its notes do not mention a headless CLI (the 1.0.36 notes mention "Headless command-line start-up"). https://github.com/vrtmrz/obsidian-livesync and https://github.com/vrtmrz/obsidian-livesync/releases

**Remotely Save** ("Source Available", license not named on the README page). Free backends: S3-compatible, Dropbox, OneDrive personal (App Folder), WebDAV, Webdis (mostly experimental); PRO adds more. Free conflict handling: it detects conflicts and the user chooses to keep the newer or the larger file; PRO "Smart Conflict" merges small Markdown files. Mobile is supported; the README warns of performance issues on files of 50 MB or more. https://github.com/remotely-save/remotely-save

**Obsidian Git** (Vinzent03, MIT). The README calls Git on mobile "very unstable!", built on isomorphic-git, with no SSH authentication, no rebase, limited repository size, no submodules, and possible crashes or endless runs on clone or pull. https://github.com/Vinzent03/obsidian-git

**Syncthing on Android.** The official Syncthing Android app was retired by its author in the announcement of 2024-10-20; the last release was planned with the December 2024 Syncthing version. https://forum.syncthing.net/t/discontinuing-syncthing-android/23002 The fork Syncthing-Fork on F-Droid lists 2.1.7.0, added 2026-10-25, as suggested. https://f-droid.org/en/packages/com.github.catfriend1.syncthingfork
