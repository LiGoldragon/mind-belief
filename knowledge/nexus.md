---
description: What the nexuses are today — which run, on which sockets and versions, from which branches — is read, before judging or changing one.
dependencies: [vision-nexus]
---

Orchestrate: read the current source version in the declared Orchestrate repository’s `Cargo.toml`.
Flow: read the current source version in the declared Flow repository’s `Cargo.toml`.
Message: read the current source version in the declared Message repository’s `Cargo.toml`.
Lojix: read the current source version in the declared Lojix repository’s `Cargo.toml`.

## Curriculum context serving

Curriculum receives one typed request through the socket at
`$XDG_RUNTIME_DIR/curriculum/curriculum.sock`. Its three authored-context
checkouts come from `CURRICULUM_PSYCHES_REPOSITORY_DIR`,
`CURRICULUM_MIND_CONTEXT_DIR` and `CURRICULUM_FIELD_CONTEXT_DIR`; its refresh
executable comes from `CURRICULUM_CONTEXT_REFRESH_PROGRAM`. These configured
values, including the service account and checkout locations, belong to the
installation and are read there rather than assumed from another setup.

At Curriculum `2d74e7725bfff88ee3aec1ebe9ce31d52873ebbc`, every query follows
`CurriculumOperation::perform` → `SourceConfiguration::from_environment` →
`SourceConfiguration::read`. `read` runs the configured refresh executable
synchronously and requires its success before reading the three checkout
revisions and their module sources; only then does `perform` dispatch
`ResolveSkills`, `ResolveSources`, `ComposeStartup` or `ComposeRole`. Nexus
startup also calls `read` while opening its memory. Thus `ExecStartPre` is not
the request-time refresh: it is an additional startup action.

The 2026-10-29 operational witness from Psyche Primary
`psyche228c47e` (with Mind `2eff0f9` and Field `77feb34`) observed the user
`curriculum-nexus.service`, with no root process, configured to run
`curriculum-refresh-contexts`. That program fetches each context repository's
`origin/main` and detaches its configured checkout there. The same witnessed
checkout update was performed manually with `git fetch origin` followed by
`git checkout --detach origin/main`. A
`ResolveSources.[ ModuleIdentity ]` request through the configured socket then
reported the revision from which Curriculum served that module. The returned
revision witnesses the request's source checkout; it does not identify the
Curriculum executable revision by itself.
