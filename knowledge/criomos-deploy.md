---
description: Lojix deployments used by CriomOS and its Home environment.
dependencies: [knowledge:lojix, knowledge:secrets]
---

## A deployment request

`lojix-meta` speaks the owner contract. `lojix` speaks the ordinary query
contract. Each client takes one datom argument and returns one reply.

```sh
LOJIX_OWNER_SOCKET=/run/lojix/meta.sock lojix-meta \
  'Deploy.UserEnvironment.{ goldragon ouranos li \
    /nix/store/dspiiriyy2zprxsxz4iiil2jlhk38qwz-horizon-definition/horizon-definition.datom \
    SecretsDirectory./git/github.com/LiGoldragon/goldragon/secrets \
    github:LiGoldragon/CriomOS?rev=9c047de0dbb3a51000a53c4f63fcbc7f55af45a9 \
    { ssh-ng://li@ouranos.goldragon.criome li@ouranos.goldragon.criome } \
    Horizon { homeConfigurations.li.activationPackage } \
    HomeManagerNixProfileV1 ActivateNow RequireImmutable \
    Some.@/etc/nix/machines [] }'
```

The `Deploy.UserEnvironment` positions are cluster, node, user, absolute
Horizon proposal, secrets input, immutable flake reference, the explicit
`{ nix-store-uri ssh-destination }` pair, mode, output selector, profile
backend, action, revision policy, builder, and extra substituters. The
approved user pair above is user-scoped; a root transport is not a substitute.

`Realize` is build and materialization only. It does not set the profile or
run activation. `ActivateNow` sets the Home Manager profile and then runs the
materialized `activate` program. Observe the durable terminal record:

```sh
LOJIX_OWNER_SOCKET=/run/lojix/owner.sock \
  lojix 'Query.ByDeployment.{ 240 }'
LOJIX_OWNER_SOCKET=/run/lojix/owner.sock \
  lojix 'Query.ByDeployment.{ 241 }'
```

The completed records were:

```text
240: UserEnvironment.Realize, ProfileOnly, Completed, Some.Succeeded
241: UserEnvironment.ActivateNow, LiveActivation, Completed, Some.Succeeded
```

The owner admissions were:

```text
DeployAccepted.{ 240 { 5301 5301 } }
DeployAccepted.{ 241 { 5322 5322 } }
```

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

The installed executor runs the user activation through the explicit SSH
target. It captures stdout and stderr, but on a nonzero exit retains trimmed
stderr only; stdout is discarded in failure evidence. This is an executor
defect, not evidence that the process produced no stdout.

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
LOJIX_OWNER_SOCKET=/run/lojix/owner.sock \
  lojix 'Query.ByDeployment.{ 237 }'
```

The durable report records deployment 237 as the successful `BaseHost`
`SetBootProfile` route and records the old runtime generation separately from
the bootloader default. It does not record a Home activation.

The exact deployment-237 request datom is not retained in this source. Its
durable report is `/home/li/primary/flows/329917/reports/acpi-model-deployment.md`.
Use the report's witnessed fields rather than reconstructing omitted ones.

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
