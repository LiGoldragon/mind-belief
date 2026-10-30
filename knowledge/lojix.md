---
description: A Lojix request must be constructed, submitted, observed, or interpreted.
dependencies: []
---

`lojix-nexus` owns durable state and two authority-tiered sockets. The ordinary contract is `signal-lojix`; the owner contract is `meta-signal-lojix`.

Use `lojix` on the ordinary socket for `Query`, `WatchDeployments`, `WatchCacheRetention`, and `Unwatch`.

Use `lojix-meta` on the owner socket for `Deploy`, `Pin`, `Unpin`, `Retire`, and `Test`. The owner contract is not optional.

Use `LOJIX_ORDINARY_SOCKET` and `LOJIX_OWNER_SOCKET`; neither socket has a default path.

## Request syntax

Each public client rejects files, zero arguments, and extra arguments. A request root is one value.

A struct is brace-enclosed and positional, a vector is bracket-enclosed, a variant is a head with the period glued to both sides, and a variant carrying nothing is bare. `None` is bare and `Some` carries one glued payload. A string with a space or a delimiter is written in guillemets.

```text
Variant.{ field0 field1 field2 }
[ field0 field1 ]
Some.Value
«alpha beta»
```

Never name a field in a request; the position carries the data.

## Ordinary requests

The current `lojix` executable exchanges one request for one reply and exits. It cannot consume ongoing subscription events. Do not use it as a streaming terminal monitor; re-query with `Query.ByDeployment` or `Query.ByEventLog`.

## Replies and terminal state

`DeployAccepted` is admission only. It does not prove evaluation, build, copy, activation, or completion.

After `DeployAccepted`, re-query by deployment identifier or event-log position until a terminal deployment record exists.

## Deployment contract

Every deployment transport is explicit. Lojix uses the supplied Nix store URI and SSH destination verbatim; it never derives a route from cluster, node, or user names.

The logical node selects what is built; the activation destination selects which machine is changed. Before a state-changing deployment, verify that they identify the same node. If they do not, stop.

A `CompleteHost` deployment uses an explicit root-privileged Nix store URI and SSH destination.

A `UserEnvironment` deployment uses an explicit user-scoped Nix store URI and SSH destination.

When a deployment directly names a target pair, use it without asking for a second transport confirmation. Otherwise derive the canonical internal hostname as `<node>.<cluster>.<internal suffix>` from Horizon cluster data and use it as the host in the required `CompleteHost` or `UserEnvironment` Nix store URI and SSH destination. If the supplied or derived pair is invalid, report it rather than substituting another route.

A deployment proposal must be an existing absolute regular non-symlink `horizon-definition.datom` file.

Use `RequireImmutable` when production deployment must identify one exact source revision. Push producer revisions before pushing the consumer revision that pins them.

A `Current` generation is Lojix's committed state. It does not establish the target's live Nix profile or runtime links.

A terminal activation failure can follow a partial target change. Inspect the target profile, runtime links, and activation journal, then report Lojix state and live state separately.

## Startup configuration

The Nexus does not accept operator requests. `lojix-write-configuration` is the datom-to-startup boundary and writes the archive consumed by `lojix-nexus`.

## Store inspection and reset

Inspect a store read-only with exactly:

```sh
lojix-inspect-store 'InspectStore.{ /tmp/lojix.sema }'
```

Inspection does not create or register missing tables.

Reset accepts only:

```sh
lojix-reset-store 'ResetStore'
```

It takes no path. Store selection comes from the service-owned `LOJIX_CONFIGURATION` archive.

Stop the Nexus before reset.

## Bootstrap

`lojix-bootstrap` is a separate Nexus-free ingress. It accepts exactly one inline `BootstrapRun` value and does not read Nexus sockets, configuration, or store state.

Ambient SSH configuration is not accepted.

Bootstrap immutable flakes use:

```text
github:owner/repository/40-lowercase-hex-revision
```

This differs from Nexus deployment flake syntax.

## Placement

Keep Lojix configuration in the operating-system source. Do not add setup-specific deployment scripts to the user environment.

The supported deployment and observation interface is `lojix` and `lojix-meta`; setup-specific wrapper scripts are not an alternative interface.
