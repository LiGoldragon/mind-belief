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

Every active repository takes nixpkgs, the Rust toolchain and the crate overrides from build-base and pins none of its own. A crate at one version and one feature set then has one store path in every repository, built once on the remote builder and served to all. A native input a crate needs is added to build-base's overrides, never in a repository. Two repositories share a third-party crate only when their lockfiles pin the same version.

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

Evaluation and building run on the remote builder itself, over ssh: the source goes to it, `nix flake check`, `nix build` and `nix eval` run there, and only what the local machine must hold is copied back. The local machine evaluates no crate2nix expression and compiles nothing, cargo included. The host's own declaration names which machine is the remote builder.

A remote build is one ssh command, its steps chained so its exit is the result, and its end is waited on as an event: the command runs in the foreground, or in the background where its exit wakes the flow that started it.

```sh
ssh prometheus 'cd ~/work/flow && nix flake check -L 2>&1 | tail -40'
```

A gate runs against the committed revision, `git+file://<clone>?rev=<commit>` or the remote URL, never a copied tree: a check that stamps `self.rev` gives another result on a copy, so a copy is another gate.

## A pin names a published commit

A git dependency is pinned to a commit its remote has, and a published history is never rewritten; a build from the repository's remote URL proves it. A flake used as a test fixture is a locked input by its bare URL, its rev asserted at evaluation, never `builtins.getFlake` on a local path.

A git dependency under `[patch]` that points at a workspace crate resolves to that path crate in `Cargo.nix`.
