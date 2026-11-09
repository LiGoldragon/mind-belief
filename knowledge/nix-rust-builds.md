---
description: A Rust repository is built and tested with Nix so that nothing is compiled twice.
dependencies: [knowledge:active-projects]
---

The working instance is github.com/LiGoldragon/rust-nix-example, built on github.com/LiGoldragon/build-base. Read it whole before changing a build; when this module and the example disagree, the example is fixed or this module is, in the same change.

## The unit of a build is the crate

Every crate, third-party and workspace member alike, is its own derivation: crate2nix generates `Cargo.nix` from `Cargo.lock`, nixpkgs `buildRustCrate` builds each crate, and `Cargo.nix` is committed, so evaluation imports no derivation. An edit rebuilds the edited crate and the crates that depend on it, and nothing else.

```nix
{
  inputs.base.url = "github:LiGoldragon/build-base";   # nixpkgs, toolchain, crate overrides: one pin for all
  outputs = { self, base }: base.lib.workspaceOutputs { cargoNix = ./Cargo.nix; };
}
```

```sh
# after any edit to Cargo.toml or Cargo.lock, regenerate and commit Cargo.nix
nix run github:LiGoldragon/build-base#crate2nix -- generate
```

## One base, so a crate has one hash everywhere

Every active repository takes nixpkgs, the Rust toolchain and the crate overrides from build-base and pins none of its own. A crate at one version and one feature set then has one store path in every repository, built once on the remote builder and served to all. A native input a crate needs is added to build-base's overrides, never in a repository.

Build-base holds one version set for every third-party crate across the active repositories, `third-party-versions.json` at its root, generated from their aligned locks. The `third-party-versions` check in every repository's `checks.default` refuses a lock whose third-party versions depart from the set, naming each crate with its lock version and the set's. Beside it, `third-party-features.json` holds one feature set for every third-party crate: the union of the features the active repositories resolve, applied by build-base's crate builder, so a crate at one version has one build everywhere. The `third-party-features` check refuses a repository that resolves a feature outside the set or lacks a dependency the set pulls; that repository carries the edge itself, its dependency taking the feature in its manifest, lock and `Cargo.nix`. Nothing is held out of either set. A version bump happens once, in build-base: the sets are regenerated and every active repository follows in the same change.

```sh
# regenerate the sets from the active repositories; the version set refuses where two locks disagree within one semver line
nix run github:LiGoldragon/build-base#third-party-version-set -- <Cargo.lock ...>
nix run github:LiGoldragon/build-base#third-party-feature-set -- <Cargo.nix ...>   # also lists the edges a repository must carry
```

A repository's own flake, or a consumer of a repository on the base, takes `pkgs` from `base.lib.contexts.<system>.pkgs` and overrides none of the base's inputs (no `inputs.nixpkgs.follows`), so store paths stay shared.

## A Cargo.nix is proved current

`checks.cargo-nix`, in `checks.default` of every repository on the base, proves the committed `Cargo.nix` is what the base's crate2nix generates from the source: the lock's packages against `Cargo.nix`, then an offline regeneration compared byte for byte. `crate-hashes.json` is committed beside `Cargo.nix`, and `Cargo.nix` sits at the workspace root, generated with no flags; a `Cargo.nix` kept apart from its workspace is proved by `cargoNixCheck { source; cargoNix; crateHashes; }`, reached at `base.lib.contexts.<system>.cargoNixCheck` and handed to `extraChecks` with the rest of the build context; `source` is the workspace holding `Cargo.toml` and `Cargo.lock`, and its `crate-hashes.json` is committed beside that `Cargo.nix`. A repository's own checks join `checks.default` through `extraChecks`, so a green default is the whole gate:

```nix
outputs = { self, base }: base.lib.workspaceOutputs {
  cargoNix = ./Cargo.nix;
  extraChecks = { pkgs, workspace, ... }: { fmt = …; clippy = …; };   # names apart from members, cargo-nix and default
};
```

```nix
# a second, separate Cargo.nix joins checks.default the same way
extraChecks = { cargoNixCheck, ... }: {
  dependency-cargo-nix = cargoNixCheck {
    source = ./dependency;
    cargoNix = ./nix/dependency/Cargo.nix;
    crateHashes = ./nix/dependency/crate-hashes.json;
  };
};
```

## A check runs; it does not compile

A crate's tests compile once, with the crate, into test binaries. There is one check per crate, which runs those binaries and compiles nothing; a failing test fails it, and the default check is all of them. There is no check per test: a test is named in its code and proved by its crate's check. A crate's `tests/` is in its test build only, so an edit to a test rebuilds the test build alone.

`nix flake check` saying "running 0 flake checks" means nothing was left to build; the gate's green is put on record by building `checks.default`.

## Where a build runs

A gate is evaluated and built on the remote builder itself: nix-fast-build `--remote` runs nix-eval-jobs there, builds every check there, one ssh build per check, and copies nothing back under `--no-download`. The local machine reads the flake's metadata, evaluates no crate2nix expression and compiles nothing, cargo included. The host's own declaration names which machine is the remote builder.

```sh
nix run github:Mic92/nix-fast-build -- --remote prometheus \
  --no-nom --no-download --eval-workers 1 \
  --flake 'git+file://<clone>?rev=<commit>#checks.x86_64-linux'
```

The gate builds `checks.<system>` whole, so a failing check is named by its own attribute beside `default`. Its exit is the result, and its end is waited on as an event: the command runs in the foreground, or in the background where its exit wakes the flow that started it. A failure ends the output with the failed attributes, each one's log above it:

```text
ERROR:nix_fast_build:BUILD: 10 successes, 2 failures
ERROR:nix_fast_build:Failed attributes: …#checks.x86_64-linux.example-number …#checks.x86_64-linux.default
```

A gate runs against the committed revision, `git+file://<clone>?rev=<commit>` or the remote URL, never a copied tree: a check that stamps `self.rev` gives another result on a copy, so a copy is another gate. A `git+file` revision is copied to the builder as its source store path; a remote URL is fetched by the builder itself.

A build whose result the local machine holds, such as a package it installs, is a plain `nix build`: the host declares the builder as an ssh-ng remote builder with no local build jobs, so evaluation is local, every derivation builds on the builder, and the result is copied back.

```sh
# /etc/nix/machines: ssh-ng://nix-ssh@prometheus.goldragon.criome x86_64-linux … ; max-jobs = 0
nix build 'git+file://<clone>?rev=<commit>#<package>'
```

## A pin names a published commit

A git dependency is pinned to a commit its remote has, and a published history is never rewritten; a build from the repository's remote URL proves it. A flake used as a test fixture is a locked input by its bare URL, its rev asserted at evaluation, never `builtins.getFlake` on a local path.

A git dependency under `[patch]` that points at a workspace crate resolves to that path crate in `Cargo.nix`.
