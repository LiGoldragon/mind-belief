---
description: What Obsidian, sync tooling and network services exist on the living's hosts is needed, for placing a vault or sync server. It ages; check the date.
---

Witnessed 2026-10-29 on host `ouranos` by flow 2c8b6a; source /home/li/primary/flows/2c8b6a/research/hosts.md (commands recorded there). Updated the same day by flow 280282 from `/home/li/primary/flows/280282/research/callout-acceptance.md` and `/home/li/primary/flows/280282/research/sync-acceptance.md`. Cluster nodes other than ouranos are known from cluster data only.

Obsidian on ouranos:
- `command -v obsidian` finds nothing; it is not in `/run/current-system/sw/bin` or `~/.nix-profile/bin`; no flatpak.
- Isolated tests on 2026-10-29 added the nixpkgs Obsidian 1.13.4 bootstrap package and Syncthing 2.1.3 to `/nix/store`; the bootstrap loaded a separately downloaded official Obsidian 1.14.5 app archive for the rendering tests. Neither executable is in `PATH`, `/run/current-system/sw/bin` or `~/.nix-profile/bin`, and no CouchDB store path was found. `syncthing.service` remained inactive and no listener appeared on ports 22000, 21027 or 8384.
- In the original flow 2c8b6a survey, `find /home/li -maxdepth 4 -name .obsidian` found no vault. Later isolated test vaults lived under `/tmp`; this is not a new absence probe.
- `/home/li/.password-store/Obsidian/ligoldragon.gpg` exists, not decrypted.

Services on ouranos (`systemctl list-units`, `ss -tlnp`):
- Running: headscale (`*:8443`, `*:50443`; server_url `https://ouranos.goldragon.criome:8443`), tailscaled, yggdrasil, strongswan, sshd (port 22), kea-dhcp4, avahi, cups, nix-daemon, lojix, repository-ledger, mpd (127.0.0.1:6600), dolt (127.0.0.1).
- Not present as units: syncthing, couchdb, forgejo, gitea, soft-serve, caddy, nginx, traefik, wireguard.
- Gitolite: user `gitolite` and `/var/lib/gitolite` exist; no daemon, it works over sshd. `repos/CriomOS/modules/nixos/repository-receive.nix:14,190` enables `services.gitolite` for nodes with `GitoliteServer`; ouranos has it.
- No reverse proxy. The only non-loopback listeners are sshd, Headscale (8443, 50443), DNS and mDNS. Reachability from the internet was not tested.

Tailnet (`tailscale status`): ouranos 100.64.0.2, prometheus-1 100.64.0.3, prometheus 100.64.0.1 (offline 230 days). The Headscale controller runs on ouranos, a laptop.

Cluster `goldragon` (`/home/li/primary/repos/goldragon/cluster-definition.datom`): ouranos, prometheus (GMKtec, 128 GB), tiger, zeus, balboa (rock64), VMs mirror-alpha, mirror-beta, vm-testing. A search of the cluster data found no Syncthing, CouchDB, Forgejo, Gitea, soft-serve, Caddy, nginx or WireGuard role.

Phone: Android, from his own words (`flows/01a04e75/vision/listenerWisprFlow.md:3-5`). It is not in the cluster data and not a tailnet node. Model, Android version, and whether an Obsidian mobile app or account is in use are unknown.
