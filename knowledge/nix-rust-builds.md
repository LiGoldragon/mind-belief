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

## A check runs; it does not compile

A crate's tests compile once, with the crate, into test binaries. There is one check per crate, which runs those binaries and compiles nothing; a failing test fails it, and the default check is all of them. There is no check per test: a test is named in its code and proved by its crate's check. A crate's `tests/` is in its test build only, so an edit to a test rebuilds the test build alone.

## Where Rust is compiled

Rust is compiled on the remote builder, through Nix; the local machine compiles nothing, cargo included. The host's own declaration names which machine is the remote builder.

## A pin names a published commit

A git dependency is pinned to a commit its remote has, and a published history is never rewritten; a build from the repository's remote URL proves it. A git dependency under `[patch]` that points at a workspace crate resolves to that path crate in `Cargo.nix`.
