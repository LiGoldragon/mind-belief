---
description: Lojix deployments used by CriomOS and its Home environment.
dependencies: [knowledge:lojix, knowledge:secrets]
---

## A deployment request

`lojix-meta` speaks the owner contract. `lojix` speaks the ordinary query
contract. Each client takes one datom argument and returns one reply.

```sh
LOJIX_OWNER_SOCKET=/run/lojix/meta.sock lojix-meta 'Deploy.UserEnvironment.{ goldragon ouranos li /nix/store/dspiiriyy2zprxsxz4iiil2jlhk38qwz-horizon-definition/horizon-definition.datom SecretsDirectory./git/github.com/LiGoldragon/goldragon/secrets github:LiGoldragon/CriomOS?rev=9c047de0dbb3a51000a53c4f63fcbc7f55af45a9 { ssh-ng://li@ouranos.goldragon.criome li@ouranos.goldragon.criome } Horizon { homeConfigurations.li.activationPackage } HomeManagerNixProfileV1 ActivateNow RequireImmutable Some.@/etc/nix/machines [] }'
```

The `Deploy.UserEnvironment` positions are cluster, node, user, absolute
Horizon proposal, secrets input, immutable flake reference, the explicit
`{ nix-store-uri ssh-destination }` pair, mode, output selector, profile
backend, action, revision policy, builder, and extra substituters. The
approved user pair above is user-scoped; a root transport is not a substitute.

The installed clients accept one inline Datom argument and resolve the socket
from the environment. `clients/meta/src/lib.rs:13,39–52` uses
`LOJIX_OWNER_SOCKET`; `clients/ordinary/src/lib.rs:9,35–48` uses
`LOJIX_ORDINARY_SOCKET`. The meta client actualizes the request and reads the
absolute Horizon proposal before sending it (`clients/meta/src/lib.rs:92–110`).

The immutable contract declares the wire shape at
`meta-signal-lojix/ethos/signal.ethos:30–31`. The corresponding installed Rust
records are `src/runtime_model.rs:507–523` (Host) and `:525–541`
(UserEnvironment): cluster, node, and (for UserEnvironment) user, followed by proposal, secrets input,
flake reference, `DeploymentTransport`, input mode, output selector,
activation backend, action, source policy, optional builder, and extra
substitutors. The nested types are declared at
`src/runtime_model.rs:82–85` (store URI and SSH destination), `:92–98`
(output selector, activation backend), and `:110–113` (secrets input).
`src/schema_runtime.rs:1793–1799` maps UserEnvironment Realize and SetProfile
to ProfileOnly, and ActivateNow to LiveActivation.

`Realize` is build and materialization only. It does not set the profile or
run activation. `ActivateNow` sets the Home Manager profile and then runs the
materialized `activate` program. Observe the durable terminal record:

```sh
lojix 'Query.ByDeployment.{ 240 }'
lojix 'Query.ByDeployment.{ 241 }'
```

These ordinary-client commands require the configured `LOJIX_ORDINARY_SOCKET`
inherited by the observed shell; the command text does not select the owner
socket. The completed records were:

```text
240: UserEnvironment.Realize, ProfileOnly, Completed, Some.Succeeded
241: UserEnvironment.ActivateNow, LiveActivation, Completed, Some.Succeeded
```

The owner admissions were:

```text
DeployAccepted.{ 240 { 5301 5301 } }
DeployAccepted.{ 241 { 5322 5322 } }
```

The raw 241 submission was executed in the retained child transcript
`/home/li/.codex-next-8mkkxq293hk2/sessions/2026/11/05/rollout-2026-11-05T21-18-10-01a1aedd-22bb-7ea1-8433-5130eccc8365.jsonl`; its exact command is the one-line request above and its raw owner reply is
`DeployAccepted.{ 241 { 5322 5322 } }`. The ordinary query command is witnessed with the configured ordinary socket inherited; no owner socket is supplied to `lojix`.

The terminal 241 query returned a live current generation and marker 5359;
the terminal record carried marker 5355.

Deployment 241's current generation was:

```text
/nix/store/c2ll7rpqqzjx4ycxlr43dfdhcmyijrwh-home-manager-generation
```

The response also recorded immutable revision
`9c047de0dbb3a51000a53c4f63fcbc7f55af45a9`.

The flake URL used by Lojix is distinct from Nix input locking. The source
flake keeps a bare `github:LiGoldragon/CriomOS-home` input URL and records its
revision in `flake.lock`; Lojix receives `?rev=<40-hex>` on the consumer
repository reference. Do not put a revision into the bare source URL.

## Profile and activation effects

`ActivateNow` performs the profile set before activation. A failed activation
can therefore leave the profile advanced while services still point at the
previous generation. Report the profile, runtime links, service state, and
Lojix terminal separately.

The installed pipeline's materialization branch is visible at
`src/schema_runtime.rs:1878–1884`: UserEnvironment selects a
`UserEnvironmentMaterialization` for the named user. Its action mapping at
`src/schema_runtime.rs:1793–1799` makes Realize ProfileOnly and ActivateNow
LiveActivation. The activation executor runs profile then activation at
`src/schema_runtime.rs:7529–7557`.

The installed executor runs the user activation through the explicit SSH
target. It captures stdout and stderr, but on a nonzero exit retains trimmed
stderr only; stdout is discarded in failure evidence. This is an executor
defect, not evidence that the process produced no stdout.

The command runner pipes both streams and reads them to EOF at
`src/schema_runtime.rs:7859–7924`. On success it returns stdout; on a
nonzero status it creates `StageFailure` from the trimmed stderr at
`src/schema_runtime.rs:7933–7942`. The retained failure also carries the
program, complete argument vector, and optional exit code
(`src/schema_runtime.rs:7811–7825`).

The supported diagnostic is the retained activation command and exit record,
plus a separately authorized direct user command when needed. Never use a
root shell, `--xtrace`, a hand-move, force overwrite, or an unapproved retry.

## Host boot-profile deployments

Host deployments are a separate route. The recorded ACPI operation used
deployment 237 with `BaseHost`, `SetBootProfile`, an immutable CriomOS source,
and the existing encrypted-files directory. Its terminal state was
`Completed`, `Some.Succeeded`, with generation `BootPending`; no reboot was
performed. The living performs the reboot. These host facts do not establish
the fields or transport of a UserEnvironment request.

Its supported observation form is:

```sh
lojix 'Query.ByDeployment.{ 237 }'
```

The retained tool transcript for flow `01a1ae03-c8db-7673-b7ba-97832991746f`
contains this exact command and reply (05 November 2026):

```text
lojix 'Query.ByDeployment.{ 237 }'
Queried.{ [ { 237 237 goldragon ouranos BaseHost BootProfile BootPending Some./nix/store/ipa0cmqx4pxl3wy35x2y6gd9slyyg35a-nixos-system-ouranos-26.11.20260813.0e251e2 Some.52e55e913abcad018a63324cbc6092ea91c43764 } ] [ { 237 237 { HostEnvironment goldragon ouranos BaseHost Host.SetBootProfile BootProfile RequireImmutable Some.52e55e913abcad018a63324cbc6092ea91c43764 } Some.{ 5229 5229 } Completed Some.{ 5262 5262 } Some.Succeeded } ] { 5266 5266 } }
```

The retained tool transcript for flow `01a1ae03-c8db-7673-b7ba-97832991746f`
contains the observation and the command construction below. The shell variable
`P` expands from the separately observed proposal-path file; `R` is the immutable
revision shown in the command.

The durable report records deployment 237 as the successful `BaseHost`
`SetBootProfile` route and records the old runtime generation separately from
the bootloader default. It does not record a Home activation.

The durable report is `/home/li/primary/flows/329917/reports/acpi-model-deployment.md`;
the retained executor transcript contains the command construction and admission:

```sh
P=$(cat /tmp/acpi-329917-proposal-path)
R=52e55e913abcad018a63324cbc6092ea91c43764
lojix-meta "Deploy.Host.{ goldragon ouranos BaseHost $P SecretsDirectory./git/github.com/LiGoldragon/goldragon/secrets github:LiGoldragon/CriomOS?rev=$R { ssh-ng://root@localhost root@localhost } Horizon { nixosConfigurations.target.config.system.build.toplevel } NixosSystemdBootV1 SetBootProfile RequireImmutable Some.@/etc/nix/machines [] }"
```

The variable file contained only
`/nix/store/dspiiriyy2zprxsxz4iiil2jlhk38qwz-horizon-definition/horizon-definition.datom`;
the admission was `DeployAccepted.{ 237 { 5229 5229 } }`. The transcript
path is the one cited above. The exact original Host argv therefore is now
witnessed without reading any secret contents.

## Materialization and live verification

`Current` in a query identifies Lojix's committed generation; it does not
prove the live profile or service links. After a successful Home activation,
verify the target profile and the generated surfaces separately from the
deployment record. The colon rollout's five skill surfaces each contained
109 colon-named directories, including `knowledge:flow-messaging`; its
producer journal reported psyche, mind, and field revisions separately.

The Home input's `SecretsDirectory` is metadata selecting an existing
directory. This knowledge records no secret contents. A deployment may use
`NoSecrets` for a host operation only when that is the actual request and
owner-approved route; do not infer it for a Home request.
